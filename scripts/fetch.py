# /// script
# requires-python = ">=3.10"
# dependencies = ["yt-dlp"]
# ///
"""摄取单个视频：抓元数据 + 字幕，生成 sources/<kol>/<date>-<id>/transcript.md

用法:
    uv run scripts/fetch.py <video-url> --kol <slug>
    uv run scripts/fetch.py <video-url> --kol <slug> --audio    # 无字幕时下载音频供转录
    # 无字幕时下载音频 + faster-whisper 本地转录（CPU）:
    uv run --with faster-whisper scripts/fetch.py <video-url> --kol <slug> --transcribe
    # GPU 转录（更快，需再注入 CUDA 运行库 wheel）:
    uv run --with faster-whisper --with nvidia-cublas-cu12 --with nvidia-cudnn-cu12 \
        scripts/fetch.py <video-url> --kol <slug> --transcribe
    # 再加说话人分离（访谈类强烈建议，需 pyannote + HF_TOKEN，见下）:
    uv run --with faster-whisper --with pyannote.audio \
        --with nvidia-cublas-cu12 --with nvidia-cudnn-cu12 \
        scripts/fetch.py <video-url> --kol <slug> --transcribe --diarize

依赖:
    yt-dlp 已声明为脚本内联依赖，uv run 会自动装好，无需系统预装。
    faster-whisper 仅 --transcribe 需要，故不进内联依赖，改用 `uv run --with
    faster-whisper` 按需注入。它基于 CTranslate2，不依赖 torch，比原版 whisper
    快约 4 倍、更省内存。
    GPU：额外注入 nvidia-cublas-cu12 / nvidia-cudnn-cu12 两个 wheel 即可，脚本会
    自动把它们的 lib 目录塞进 LD_LIBRARY_PATH（re-exec 一次）。缺这两个 wheel 或
    无可用 GPU 时自动回退 CPU，无需改命令。
    pyannote.audio 仅 --diarize 需要（它拖 torch，故同样按需注入）。3.x / 4.x 都支持：
    4.x 把 use_auth_token 改名成 token、且返回 DiarizeOutput 而非 Annotation，
    diarize() 里对这两处做了版本自适应，故无需固定版本。首次使用还需：
      1) 用同一个 HF 账号，把下面**三个** gated 仓库的条款都接受掉（缺一个就 403）：
           https://hf.co/pyannote/speaker-diarization-3.1
           https://hf.co/pyannote/segmentation-3.0            （pipeline 依赖）
           https://hf.co/pyannote/speaker-diarization-community-1  （4.x 取 embedding 用）
         注意条款是按**账号**接受的，换 token 不会带过去。
      2) 导出 HF_TOKEN=<你的 huggingface token>
    自查是否授权要**实测下载文件**（model_info 对 gated 仓库也会成功，会给出假绿灯）：
        hf_hub_download(repo_id=..., filename="config.yaml", token=...)
    分离在 CPU 上极慢，无 GPU 时自动跳过（仍产出无说话人标签的转录稿）。
"""

import argparse
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "sources"

# 字幕语言偏好：优先视频原始语言（自动翻译字幕质量差），中文其次
ZH_PREF = ["zh-Hans", "zh-CN", "zh-Hant", "zh-TW", "zh", "en-orig", "en", "en-US", "en-GB"]
EN_PREF = ["en-orig", "en", "en-US", "en-GB", "zh-Hans", "zh-CN", "zh"]

DEFAULT_WHISPER_MODEL = "large-v3-turbo"
DIARIZATION_MODEL = "pyannote/speaker-diarization-3.1"


def run(cmd: list[str], timeout: int | None = None) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        sys.exit(f"命令超时（{timeout}s）: {' '.join(cmd[:2])} …")


def _ensure_cuda_libs(device: str) -> None:
    """让 GPU 转录在 uv 临时环境里也能用。

    CTranslate2（faster-whisper 后端）在进程启动时由动态链接器加载
    libcublas/libcudnn，须在启动前就把它们的目录放进 LD_LIBRARY_PATH。
    若通过 `--with nvidia-cublas-cu12 --with nvidia-cudnn-cu12` 装了这些 wheel，
    这里定位其 lib 目录、加入 LD_LIBRARY_PATH 后 re-exec 自身让链接器生效。
    未安装则跳过——GPU 加载失败时 transcribe_with_whisper 会回退到 CPU。
    """
    if device == "cpu" or os.environ.get("_FETCH_CUDA_REEXEC"):
        return
    lib_dirs = []
    for pkg in ("nvidia.cublas", "nvidia.cudnn"):
        spec = importlib.util.find_spec(pkg)
        locs = getattr(spec, "submodule_search_locations", None) if spec else None
        if locs:
            d = Path(list(locs)[0]) / "lib"
            if d.is_dir():
                lib_dirs.append(str(d))
    if not lib_dirs:
        return
    current = os.environ.get("LD_LIBRARY_PATH", "")
    if all(d in current.split(":") for d in lib_dirs):
        return  # 已在路径中
    os.environ["LD_LIBRARY_PATH"] = ":".join(lib_dirs + ([current] if current else []))
    os.environ["_FETCH_CUDA_REEXEC"] = "1"
    os.execv(sys.executable, [sys.executable, *sys.argv])


def pick_lang(available: dict, pref: list[str]) -> str | None:
    for lang in pref:
        if lang in available:
            return lang
    # 退而求其次：任何 zh* / en* 变体
    for lang in available:
        if lang.startswith(("zh", "en")):
            return lang
    return None


def fmt_ts(seconds: float) -> str:
    s = int(seconds)
    return f"{s // 3600:02d}:{s % 3600 // 60:02d}:{s % 60:02d}"


def parse_vtt(path: Path, anchor_every: int = 60) -> str:
    """VTT → 纯文本。去掉标签、合并自动字幕的重复行，每 anchor_every 秒插一个时间戳锚点。"""
    ts_re = re.compile(r"(\d+):(\d+):(\d+)\.\d+\s*-->")
    tag_re = re.compile(r"<[^>]+>")
    out: list[str] = []
    last_line = ""
    cur_time = 0.0
    next_anchor = 0.0
    for raw in path.read_text(encoding="utf-8").splitlines():
        m = ts_re.match(raw.strip())
        if m:
            h, mi, s = map(int, m.groups())
            cur_time = h * 3600 + mi * 60 + s
            continue
        line = tag_re.sub("", raw).strip()
        if not line or line == "WEBVTT" or line.startswith(("Kind:", "Language:", "NOTE")):
            continue
        if line == last_line:  # 自动字幕滚动产生的重复
            continue
        if cur_time >= next_anchor:
            out.append(f"\n[{fmt_ts(cur_time)}]")
            next_anchor = cur_time + anchor_every
        out.append(line)
        last_line = line
    return " ".join(out).replace(" \n", "\n").strip()


def write_transcript(dest: Path, info: dict, args_kol: str, upload: str,
                     vid: str, subtitle: str, text: str) -> None:
    """写出带 frontmatter 的 transcript.md 并把 video id 追加到 seen.txt。"""
    title_sanitized = info.get("title", "").replace('"', "'")
    url_line = (f"url: https://www.youtube.com/watch?v={vid}"
                if info.get("extractor", "").startswith("youtube")
                else f"url: {info.get('webpage_url', '')}")
    channel = info.get("channel") or info.get("uploader", "")
    dur = round((info.get("duration") or 0) / 60)
    meta = "\n".join([
        "---",
        f'title: "{title_sanitized}"',
        url_line,
        f"kol: {args_kol}",
        f'channel: "{channel}"',
        f"upload_date: {upload}",
        f"duration_minutes: {dur}",
        f"subtitle: {subtitle}",
        f"fetched: {date.today().isoformat()}",
        "---",
    ])
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "transcript.md").write_text(meta + "\n\n" + text + "\n", encoding="utf-8")

    # seen.txt 只记「已 fetch」；重复 fetch 同一视频时不要重复追加
    seen = SOURCES / "seen.txt"
    seen.parent.mkdir(exist_ok=True)
    already = set(seen.read_text(encoding="utf-8").split()) if seen.exists() else set()
    if vid not in already:
        with seen.open("a", encoding="utf-8") as f:
            f.write(vid + "\n")

    print(f"完成: {dest / 'transcript.md'}  （{len(text)} 字符）")


def transcribe_with_whisper(audio_path: Path, model_name: str, lang: str,
                            device: str = "auto") -> list:
    """用 faster-whisper 转录音频，返回片段列表（每个含 .start/.end/.text）。

    只做转录，不做排版——排版交给 format_segments()，这样说话人分离（diarize）
    可以插在两者中间，而无需改动这里的 ASR 逻辑。

    faster-whisper（CTranslate2 后端）比原版 openai-whisper 快约 4 倍、省内存，
    且不依赖 torch。device="auto" 有 GPU 就用 GPU；但若 CUDA 运行库（cuBLAS/
    cuDNN）缺失会在编码时报错，这里捕获后自动回退到 CPU。
    """
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        sys.exit(
            "--transcribe 需要 faster-whisper，请用 --with 按需注入：\n"
            "  uv run --with faster-whisper scripts/fetch.py <url> --kol <slug> --transcribe"
        )

    def transcribe_on(dev: str, compute_type: str) -> list:
        model = WhisperModel(model_name, device=dev, compute_type=compute_type)
        segments, _ = model.transcribe(str(audio_path), language=lang[:2])  # zh / en
        return list(segments)  # 生成器，转成 list 以在此处触发实际转录、暴露错误

    print(f"加载 whisper 模型: {model_name}（首次运行会下载模型，约 1.5GB）")
    print(f"开始转录（设备: {device}，语言: {lang}），请耐心等待...")
    try:
        segs = transcribe_on(device, "auto" if device != "cpu" else "int8")
    except RuntimeError as e:
        if device != "cpu" and any(k in str(e).lower()
                                   for k in ("cuda", "cublas", "cudnn", "gpu", "libcu")):
            print(f"GPU 不可用（{str(e).splitlines()[0]}），回退到 CPU 转录...")
            segs = transcribe_on("cpu", "int8")
        else:
            raise

    return segs


def format_segments(segs: list, speakers: list[str] | None = None,
                    anchor_every: int = 60) -> str:
    """片段 → 带 [HH:MM:SS] 时间戳锚点的纯文本，与 parse_vtt 输出一致。

    speakers 与 segs 一一对应时，在说话人变化处插入 `SPEAKER_XX:` 标签
    （沿用匿名标签，映射到真人名字是 wiki 层的编辑判断，见 CLAUDE.md）。
    """
    next_anchor = 0.0
    last_speaker: str | None = None
    lines: list[str] = []
    for i, seg in enumerate(segs):
        text = seg.text.strip()
        if not text:
            continue
        if seg.start >= next_anchor:
            lines.append(f"\n[{fmt_ts(seg.start)}]")
            next_anchor = seg.start + anchor_every
        if speakers:
            spk = speakers[i]
            if spk and spk != last_speaker:
                # 换人就另起一行，让说话轮次在纯文本里也一眼可见
                lines.append(f"\n{spk}:")
                last_speaker = spk
        lines.append(text)

    return " ".join(lines).replace(" \n", "\n").strip()


def _to_wav16k(audio_path: Path, tmpdir: str) -> Path:
    """转成 16kHz 单声道 wav 供 pyannote 使用。

    原始音频常是 webm/opus，pyannote 的加载后端未必吃得下；而它内部本来就要
    重采样到 16k 单声道，这里用 ffmpeg 先转一遍既稳妥也不损失有效信息。
    """
    wav = Path(tmpdir) / "diarize.wav"
    r = run(["ffmpeg", "-nostdin", "-y", "-i", str(audio_path),
             "-ac", "1", "-ar", "16000", str(wav)], timeout=1800)
    if r.returncode != 0 or not wav.exists():
        raise RuntimeError(f"ffmpeg 转 wav 失败:\n{r.stderr[-1000:]}")
    return wav


def diarize(audio_path: Path, device: str = "auto") -> list[tuple[float, float, str]]:
    """用 pyannote 做说话人分离，返回 [(start, end, "SPEAKER_00"), ...]。

    失败一律返回空列表（调用方退化为无标签转录稿）——分离是锦上添花，
    不该让整个摄取流程失败。
    """
    try:
        import torch
        from pyannote.audio import Pipeline
    except ImportError:
        print("--diarize 需要 pyannote.audio，请用 --with 按需注入：\n"
              "  uv run --with faster-whisper --with pyannote.audio ... --transcribe --diarize",
              file=sys.stderr)
        return []

    token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACE_TOKEN")
    if not token:
        print("--diarize 需要 HF_TOKEN 环境变量。首次使用请先：\n"
              "  1) 用同一个 HF 账号接受这三个 gated 仓库的条款（缺一个就 403）：\n"
              "       https://hf.co/pyannote/speaker-diarization-3.1\n"
              "       https://hf.co/pyannote/segmentation-3.0\n"
              "       https://hf.co/pyannote/speaker-diarization-community-1\n"
              "  2) export HF_TOKEN=<huggingface token>\n"
              "本次跳过说话人分离。", file=sys.stderr)
        return []

    use_cuda = torch.cuda.is_available() if device != "cpu" else False
    if not use_cuda:
        print("说话人分离在 CPU 上极慢（可能数小时），本次跳过。"
              "如确需 CPU 分离，请单独跑 pyannote。", file=sys.stderr)
        return []

    print("加载 pyannote 说话人分离模型（首次会下载）...")
    # 整段（含结果解包）都包在 try 里：解包也可能因 pyannote 版本差异出错，
    # 放在外面会变成未捕获异常、直接中断摄取。
    try:
        try:
            pipeline = Pipeline.from_pretrained(DIARIZATION_MODEL, token=token)
        except TypeError as e:
            # pyannote.audio < 4 用的是 use_auth_token；4.x 改名为 token。
            # 只在「签名对不上」时回退——别的 TypeError 是真出错了，
            # 拿重试去掩盖只会让报错指向错误的方向。
            if "unexpected keyword argument" not in str(e):
                raise
            pipeline = Pipeline.from_pretrained(
                DIARIZATION_MODEL, use_auth_token=token)
        if pipeline is None:  # 条款未接受 / token 无权限时 pyannote 返回 None
            raise RuntimeError("模型加载返回 None——通常是未接受模型条款或 token 无权限")
        pipeline.to(torch.device("cuda"))

        with tempfile.TemporaryDirectory() as td:
            wav = _to_wav16k(audio_path, td)
            print("开始说话人分离，请耐心等待...")
            output = pipeline(str(wav))

        # pyannote 4.x 返回 DiarizeOutput（分离结果在 .speaker_diarization），
        # 3.x 直接返回 Annotation——取属性取不到就说明是老版本，用它本身。
        annotation = getattr(output, "speaker_diarization", output)
        turns = [(t.start, t.end, spk)
                 for t, _, spk in annotation.itertracks(yield_label=True)]
    except Exception as e:  # 分离失败不该拖垮摄取
        print(f"说话人分离失败（{e}），退化为无说话人标签的转录稿。", file=sys.stderr)
        return []
    n_spk = len({spk for _, _, spk in turns})
    print(f"说话人分离完成：{n_spk} 位说话人 / {len(turns)} 段")
    return turns


def assign_speakers(segs: list, turns: list[tuple[float, float, str]]) -> list[str]:
    """给每个转录片段配一个说话人：取与之重叠时长最大的 turn。

    whisper 的切分和 pyannote 的切分互不对齐，重叠最大者是简单且稳健的归属方式。
    完全无重叠的片段（如音乐、静默）沿用上一个说话人。
    """
    turns = sorted(turns)  # 下面按时序提前 break，先确保有序
    speakers: list[str] = []
    last = ""
    for seg in segs:
        best, best_overlap = "", 0.0
        for start, end, spk in turns:
            if end <= seg.start:
                continue
            if start >= seg.end:
                break  # turns 按时间有序，后面的只会更晚
            overlap = min(seg.end, end) - max(seg.start, start)
            if overlap > best_overlap:
                best, best_overlap = spk, overlap
        speakers.append(best or last)
        last = speakers[-1]
    return speakers


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--kol", required=True, help="watchlist 里的 slug，用作目录名")
    ap.add_argument("--lang", help="强制字幕语言代码（如 zh-Hans），跳过自动选择；"
                                   "用于自动配音版原声轨道等特殊情况")
    ap.add_argument("--audio", action="store_true", help="无字幕时下载音频")
    ap.add_argument("--transcribe", action="store_true",
                    help="无字幕时下载音频并用 faster-whisper 转录，生成本地 transcript.md")
    ap.add_argument("--diarize", action="store_true",
                    help="转录时附带说话人分离（需 --transcribe + pyannote.audio + HF_TOKEN + GPU）；"
                         "在转录稿里插入匿名 SPEAKER_XX 标签，访谈类建议开启")
    ap.add_argument("--whisper-model", default=DEFAULT_WHISPER_MODEL,
                    help=f"faster-whisper 模型（默认 {DEFAULT_WHISPER_MODEL}）："
                         "tiny/base/small/medium/large-v3/large-v3-turbo")
    ap.add_argument("--device", default="auto", choices=["auto", "cpu", "cuda"],
                    help="faster-whisper 推理设备（默认 auto，GPU 不可用时自动回退 CPU）")
    args = ap.parse_args()

    if args.diarize and not args.transcribe:
        ap.error("--diarize 需配合 --transcribe 使用（只对本地转录的音频生效，"
                 "已有字幕的视频没有可分离的音频轨）")

    # GPU 转录：若装了 nvidia 运行库 wheel，先把它们塞进 LD_LIBRARY_PATH 再干活
    if args.transcribe:
        _ensure_cuda_libs(args.device)

    print(f"抓取元数据: {args.url}")
    r = run(["yt-dlp", "-J", "--no-playlist", args.url], timeout=120)
    if r.returncode != 0:
        sys.exit(f"yt-dlp 失败:\n{r.stderr[-2000:]}")
    info = json.loads(r.stdout)

    vid = info["id"]
    upload = info.get("upload_date") or date.today().strftime("%Y%m%d")
    dest = SOURCES / args.kol / f"{upload}-{vid}"
    if (dest / "transcript.md").exists():
        sys.exit(f"已存在，跳过: {dest}")

    subs = info.get("subtitles") or {}
    autos = info.get("automatic_captions") or {}
    orig = info.get("language") or ""
    if args.lang:  # 强制指定语言：先人工字幕后自动字幕，不做同族回退
        if args.lang in subs:
            lang, auto = args.lang, False
        elif args.lang in autos:
            lang, auto = args.lang, True
        else:
            sys.exit(f"指定语言 {args.lang} 无可用字幕。")
    else:
        pref = ZH_PREF if orig.startswith("zh") else EN_PREF
        lang = pick_lang(subs, pref)
        auto = False
        if lang is None:
            lang = pick_lang(autos, pref)
            auto = True

    if lang is None:
        # ── 无字幕路径 ──
        if args.transcribe:
            dest.mkdir(parents=True, exist_ok=True)
            print(f"下载音频...")
            # 直接取原生音频流，不转码成 mp3：whisper 内部会用 ffmpeg 解码，
            # 省一次有损重编码（更快、也更准）。
            r2 = run(["yt-dlp", "--no-playlist", "-f", "bestaudio/best",
                      "-o", str(dest / "audio.%(ext)s"), args.url], timeout=1800)
            if r2.returncode != 0:
                sys.exit(f"音频下载失败:\n{r2.stderr[-2000:]}")
            audio_files = [p for p in dest.glob("audio.*") if p.suffix != ".md"]
            if not audio_files:
                sys.exit(f"音频文件未生成于 {dest}")
            audio_path = audio_files[0]

            # 确定转录语言
            transcribe_lang = orig if orig.startswith(("zh", "en")) else \
                (args.lang[:2] if args.lang else "zh")
            segs = transcribe_with_whisper(audio_path, args.whisper_model,
                                           transcribe_lang, args.device)
            speakers = None
            subtitle = f"{transcribe_lang} (faster-whisper {args.whisper_model})"
            if args.diarize:
                turns = diarize(audio_path, args.device)
                if turns:  # 分离失败时 turns 为空，退化为无标签转录稿
                    speakers = assign_speakers(segs, turns)
                    subtitle += f" + pyannote diarization ({len(set(speakers))} 说话人)"
            text = format_segments(segs, speakers)
            write_transcript(dest, info, args.kol, upload, vid, subtitle, text)
            return

        # ── 纯下载音频路径 ──
        print("没有可用字幕。", file=sys.stderr)
        if args.audio:
            dest.mkdir(parents=True, exist_ok=True)
            run(["yt-dlp", "--no-playlist", "-f", "bestaudio/best",
                 "-o", str(dest / "audio.%(ext)s"), args.url], timeout=1800)
            sys.exit(f"音频已下载到 {dest}，请安排转录（如 whisper）。")
        sys.exit("可加 --audio 下载音频后用 whisper 转录。")

    # ── 有字幕路径 ──
    kind = "自动" if auto else "人工"
    print(f"下载字幕: {lang}（{kind}）")
    with tempfile.TemporaryDirectory() as tmp:
        cmd = ["yt-dlp", "--no-playlist", "--skip-download",
               "--sub-langs", lang, "--sub-format", "vtt",
               "--write-auto-subs" if auto else "--write-subs",
               "-o", f"{tmp}/sub", args.url]
        r = run(cmd, timeout=300)
        vtts = list(Path(tmp).glob("*.vtt"))
        if not vtts:
            sys.exit(f"字幕下载失败:\n{r.stderr[-2000:]}")
        text = parse_vtt(vtts[0])

    write_transcript(dest, info, args.kol, upload, vid, f"{lang} ({kind})", text)


if __name__ == "__main__":
    main()
