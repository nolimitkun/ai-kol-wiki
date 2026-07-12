# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""摄取单个视频：抓元数据 + 字幕，生成 sources/<kol>/<date>-<id>/transcript.md

用法:
    uv run scripts/fetch.py <video-url> --kol <slug>
    uv run scripts/fetch.py <video-url> --kol <slug> --audio   # 无字幕时下载音频供转录
"""

import argparse
import json
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


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True)


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


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--kol", required=True, help="watchlist 里的 slug，用作目录名")
    ap.add_argument("--audio", action="store_true", help="无字幕时下载音频")
    args = ap.parse_args()

    print(f"抓取元数据: {args.url}")
    r = run(["yt-dlp", "-J", "--no-playlist", args.url])
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
    pref = ZH_PREF if orig.startswith("zh") else EN_PREF
    lang = pick_lang(subs, pref)
    auto = False
    if lang is None:
        lang = pick_lang(autos, pref)
        auto = True

    if lang is None:
        print("没有可用字幕。", file=sys.stderr)
        if args.audio:
            dest.mkdir(parents=True, exist_ok=True)
            run(["yt-dlp", "--no-playlist", "-x", "--audio-format", "mp3",
                 "-o", str(dest / "audio.%(ext)s"), args.url])
            sys.exit(f"音频已下载到 {dest}，请安排转录（如 whisper）。")
        sys.exit("可加 --audio 下载音频后用 whisper 转录。")

    kind = "自动" if auto else "人工"
    print(f"下载字幕: {lang}（{kind}）")
    with tempfile.TemporaryDirectory() as tmp:
        cmd = ["yt-dlp", "--no-playlist", "--skip-download",
               "--sub-langs", lang, "--sub-format", "vtt",
               "--write-auto-subs" if auto else "--write-subs",
               "-o", f"{tmp}/sub", args.url]
        r = run(cmd)
        vtts = list(Path(tmp).glob("*.vtt"))
        if not vtts:
            sys.exit(f"字幕下载失败:\n{r.stderr[-2000:]}")
        text = parse_vtt(vtts[0])

    dest.mkdir(parents=True, exist_ok=True)
    meta = "\n".join([
        "---",
        f'title: "{info.get("title", "").replace(chr(34), chr(39))}"',
        f"url: https://www.youtube.com/watch?v={vid}" if info.get("extractor", "").startswith("youtube")
        else f'url: {info.get("webpage_url", args.url)}',
        f"kol: {args.kol}",
        f'channel: "{info.get("channel") or info.get("uploader", "")}"',
        f"upload_date: {upload}",
        f"duration_minutes: {round((info.get('duration') or 0) / 60)}",
        f"subtitle: {lang} ({kind})",
        f"fetched: {date.today().isoformat()}",
        "---",
    ])
    (dest / "transcript.md").write_text(meta + "\n\n" + text + "\n", encoding="utf-8")

    seen = SOURCES / "seen.txt"
    seen.parent.mkdir(exist_ok=True)
    with seen.open("a", encoding="utf-8") as f:
        f.write(vid + "\n")

    print(f"完成: {dest / 'transcript.md'}  （{len(text)} 字符）")


if __name__ == "__main__":
    main()
