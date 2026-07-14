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

依赖:
    yt-dlp 已声明为脚本内联依赖，uv run 会自动装好，无需系统预装。
    faster-whisper 仅 --transcribe 需要，故不进内联依赖，改用 `uv run --with
    faster-whisper` 按需注入。它基于 CTranslate2，不依赖 torch，比原版 whisper
    快约 4 倍、更省内存。
    GPU：额外注入 nvidia-cublas-cu12 / nvidia-cudnn-cu12 两个 wheel 即可，脚本会
    自动把它们的 lib 目录塞进 LD_LIBRARY_PATH（re-exec 一次）。缺这两个 wheel 或
    无可用 GPU 时自动回退 CPU，无需改命令。
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

    seen = SOURCES / "seen.txt"
    seen.parent.mkdir(exist_ok=True)
    with seen.open("a", encoding="utf-8") as f:
        f.write(vid + "\n")

    print(f"完成: {dest / 'transcript.md'}  （{len(text)} 字符）")


def transcribe_with_whisper(audio_path: Path, model_name: str, lang: str,
                            device: str = "auto") -> str:
    """用 faster-whisper 转录音频，返回带 [HH:MM:SS] 时间戳锚点的纯文本。

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

    # 格式化为带时间戳锚点的纯文本，与 parse_vtt 输出一致
    anchor_every = 60
    next_anchor = 0.0
    lines: list[str] = []
    for seg in segs:
        text = seg.text.strip()
        if not text:
            continue
        if seg.start >= next_anchor:
            lines.append(f"\n[{fmt_ts(seg.start)}]")
            next_anchor = seg.start + anchor_every
        lines.append(text)

    return " ".join(lines).replace(" \n", "\n").strip()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--kol", required=True, help="watchlist 里的 slug，用作目录名")
    ap.add_argument("--lang", help="强制字幕语言代码（如 zh-Hans），跳过自动选择；"
                                   "用于自动配音版原声轨道等特殊情况")
    ap.add_argument("--audio", action="store_true", help="无字幕时下载音频")
    ap.add_argument("--transcribe", action="store_true",
                    help="无字幕时下载音频并用 faster-whisper 转录，生成本地 transcript.md")
    ap.add_argument("--whisper-model", default=DEFAULT_WHISPER_MODEL,
                    help=f"faster-whisper 模型（默认 {DEFAULT_WHISPER_MODEL}）："
                         "tiny/base/small/medium/large-v3/large-v3-turbo")
    ap.add_argument("--device", default="auto", choices=["auto", "cpu", "cuda"],
                    help="faster-whisper 推理设备（默认 auto，GPU 不可用时自动回退 CPU）")
    args = ap.parse_args()

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
            text = transcribe_with_whisper(audio_path, args.whisper_model,
                                           transcribe_lang, args.device)
            write_transcript(dest, info, args.kol, upload, vid,
                             f"{transcribe_lang} (faster-whisper {args.whisper_model})", text)
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
