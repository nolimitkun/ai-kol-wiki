# /// script
# requires-python = ">=3.10"
# dependencies = ["yt-dlp"]
# ///
"""给已摄取的转录稿补做说话人分离，结果写成 **sidecar** 文件，不改转录稿本身。

为什么是 sidecar 而不是重写 transcript.md：
    分离需要片段级时间轴，而存档的转录稿只保留了每 60 秒一个锚点，补做就得重跑
    whisper——而 whisper 的切分在不同运行/不同模型间会漂移，重写会让 wiki 里已有的
    [HH:MM:SS] 引用失准。加之 CLAUDE.md 规定 sources/ 只增不改。
    所以这里只**新增** speakers.md（增，不是改），transcript.md 逐字节不动，
    已有引用全部继续有效。

用法（需 pyannote + HF_TOKEN + GPU，见 fetch.py 文档）:
    uv run scripts/backfill_diarization.py --dry-run          # 先看会处理哪些
    uv run --with pyannote.audio scripts/backfill_diarization.py --limit 1
    uv run --with pyannote.audio scripts/backfill_diarization.py --kol zhang-xiaojun

默认只处理「whisper 转录且尚无 speakers.md」的目录。音频缺失时用 yt-dlp 重新下载
（音频已在 .gitignore 里，不会进仓库）；默认处理完即删，用 --keep-audio 保留。
"""
from __future__ import annotations

import argparse
import hashlib
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fetch  # 复用 diarize() / fmt_ts() / run()，避免逻辑二次实现

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "sources"
SIDECAR = "speakers.md"


def parse_frontmatter(path: Path) -> dict:
    """读 transcript.md 顶部的 YAML frontmatter（只需简单 key: value）。"""
    meta: dict[str, str] = {}
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return meta
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ": " in line:
            k, v = line.split(": ", 1)
            meta[k.strip()] = v.strip().strip('"')
    return meta


def find_targets(kol: str | None, force: bool) -> list[tuple[Path, dict]]:
    """找出待处理目录：whisper 转录的，且（除非 --force）还没有 sidecar。"""
    out: list[tuple[Path, dict]] = []
    for tr in sorted(SOURCES.glob("*/*/transcript.md")):
        meta = parse_frontmatter(tr)
        if "whisper" not in meta.get("subtitle", ""):
            continue  # 有现成字幕的没有可分离的音频轨，跳过
        if kol and meta.get("kol") != kol:
            continue
        if (tr.parent / SIDECAR).exists() and not force:
            continue
        out.append((tr.parent, meta))
    return out


def ensure_audio(d: Path, url: str) -> tuple[Path | None, bool]:
    """返回 (音频路径, 是否本次新下载)。已有 audio.* 就直接用。"""
    existing = [p for p in d.glob("audio.*") if p.suffix != ".md"]
    if existing:
        return existing[0], False
    if not url:
        return None, False
    print(f"  音频缺失，重新下载: {url}")
    r = fetch.run(["yt-dlp", "--no-playlist", "-f", "bestaudio/best",
                   "-o", str(d / "audio.%(ext)s"), url], timeout=1800)
    if r.returncode != 0:
        print(f"  !! 音频下载失败:\n{r.stderr[-500:]}", file=sys.stderr)
        return None, False
    got = [p for p in d.glob("audio.*") if p.suffix != ".md"]
    return (got[0], True) if got else (None, False)


def merge_turns(turns: list[tuple[float, float, str]],
                gap: float = 2.0) -> list[tuple[float, float, str]]:
    """合并同一说话人的相邻片段，压掉 pyannote 的碎片化输出。

    间隔小于 gap 秒且说话人相同就并成一段——否则 200 分钟的访谈会产生几千行表格。
    """
    merged: list[list] = []
    for start, end, spk in sorted(turns):
        if merged and merged[-1][2] == spk and start - merged[-1][1] <= gap:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end, spk])
    return [(a, b, c) for a, b, c in merged]


def render_sidecar(meta: dict, turns: list[tuple[float, float, str]],
                   model: str) -> str:
    """生成 speakers.md：统计表 + 轮次表。"""
    totals: dict[str, float] = {}
    for start, end, spk in turns:
        totals[spk] = totals.get(spk, 0.0) + (end - start)
    grand = sum(totals.values()) or 1.0
    ordered = sorted(totals.items(), key=lambda kv: -kv[1])

    head = "\n".join([
        "---",
        f'title: "{meta.get("title", "")}"',
        f"video_id: {meta.get('url', '').rsplit('=', 1)[-1]}",
        f"kol: {meta.get('kol', '')}",
        f"diarization: {model}",
        f"speakers: {len(totals)}",
        f"turns: {len(turns)}",
        f"generated: {date.today().isoformat()}",
        "---",
    ])

    body = [
        "",
        "> 说话人分离结果（**匿名标签**）。同目录的 `transcript.md` 未作任何改动。",
        "> 标签 → 真人姓名的映射属于编辑判断，请记在 wiki 视频页开头，见 CLAUDE.md。",
        "> 分离在抢话/串场处会错配：标签是证据不是判决，与内容矛盾时以内容为准。",
        "",
        "## 说话占比",
        "",
        "| 说话人 | 时长 | 占比 |",
        "|---|---|---|",
    ]
    for spk, secs in ordered:
        body.append(f"| {spk} | {fetch.fmt_ts(secs)} | {secs / grand * 100:.1f}% |")

    body += [
        "",
        "（访谈里占比低的通常是主持人，可作为认人的线索之一。）",
        "",
        "## 说话轮次",
        "",
        "| 起 | 止 | 说话人 |",
        "|---|---|---|",
    ]
    for start, end, spk in turns:
        body.append(f"| {fetch.fmt_ts(start)} | {fetch.fmt_ts(end)} | {spk} |")

    return head + "\n" + "\n".join(body) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="只列出会处理哪些，不动手")
    ap.add_argument("--force", action="store_true", help="已有 speakers.md 也重做")
    ap.add_argument("--kol", help="只处理该 kol slug")
    ap.add_argument("--limit", type=int, help="最多处理几个（建议先 --limit 1 验证）")
    ap.add_argument("--only", help="只处理路径含该子串的目录（如 video id），用于验证或重试单期")
    ap.add_argument("--keep-audio", action="store_true",
                    help="保留本次下载的音频（默认用完删除；音频已 gitignore）")
    ap.add_argument("--device", default="auto", choices=["auto", "cpu", "cuda"])
    ap.add_argument("--num-speakers", type=int,
                    help="已知说话人数就写死（双人访谈填 2），聚类质量明显更好")
    ap.add_argument("--max-speakers", type=int,
                    help="拿不准人数时给个上限（如 3），比完全不约束好")
    args = ap.parse_args()

    targets = find_targets(args.kol, args.force)
    if args.only:
        targets = [(d, m) for d, m in targets if args.only in str(d)]
    if args.limit:
        targets = targets[:args.limit]
    if not targets:
        print("没有需要处理的目录（whisper 转录且缺 speakers.md 的都已处理完）。")
        return

    print(f"待处理 {len(targets)} 个：")
    for d, meta in targets:
        has_audio = any(p.suffix != ".md" for p in d.glob("audio.*"))
        print(f"  {d.relative_to(ROOT)}  "
              f"[{meta.get('duration_minutes', '?')}min, "
              f"音频{'在本地' if has_audio else '需下载'}]")
    if args.dry_run:
        print("\n--dry-run：未做任何改动。")
        return

    ok = failed = 0
    for d, meta in targets:
        print(f"\n=== {d.relative_to(ROOT)} ===")
        tr = d / "transcript.md"
        before = hashlib.sha256(tr.read_bytes()).hexdigest()  # 免动转录稿的凭证

        audio, downloaded = ensure_audio(d, meta.get("url", ""))
        if not audio:
            print("  !! 无音频可用，跳过", file=sys.stderr)
            failed += 1
            continue
        try:
            turns = fetch.diarize(audio, args.device,
                                  args.num_speakers, args.max_speakers)
        finally:
            if downloaded and not args.keep_audio:
                audio.unlink(missing_ok=True)

        if not turns:
            print("  !! 分离未产出结果，跳过", file=sys.stderr)
            failed += 1
            continue

        merged = merge_turns(turns)
        (d / SIDECAR).write_text(
            render_sidecar(meta, merged, fetch.DIARIZATION_MODEL), encoding="utf-8")

        after = hashlib.sha256(tr.read_bytes()).hexdigest()
        if before != after:  # 不该发生；真发生了要立刻知道
            sys.exit(f"!! transcript.md 被修改了，这违反 sources/ 只增不改: {tr}")
        print(f"  写入 {(d / SIDECAR).relative_to(ROOT)}"
              f"（{len(merged)} 轮次，transcript.md 未变）")
        ok += 1

    print(f"\n完成：成功 {ok}，失败/跳过 {failed}")


if __name__ == "__main__":
    main()
