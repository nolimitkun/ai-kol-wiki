# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""统计 wiki 规模并回写 README.md 中的标记块。

用法：uv run scripts/stats.py            # 回写 README.md
      uv run scripts/stats.py --check   # 只检查是否需要更新（CI 用，有变化则退出码 1）

在 README.md 中放置成对标记，脚本只替换标记之间的内容：
    <!-- STATS:BLOCK:START -->…<!-- STATS:BLOCK:END -->     完整统计小节
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
WATCHLIST = ROOT / "watchlist.yaml"


def count_md(sub: str) -> int:
    return len(list((ROOT / "wiki" / sub).glob("*.md")))


def per_channel() -> list[tuple[str, str, int]]:
    """返回 [(slug, 显示名, 视频数), …]，按视频数降序。"""
    kols = yaml.safe_load(WATCHLIST.read_text(encoding="utf-8"))["kols"]
    rows = []
    for k in kols:
        slug = k["slug"]
        n = len(list((ROOT / "sources" / slug).glob("*/transcript.md")))
        rows.append((slug, k["name"], n))
    rows.sort(key=lambda r: (-r[2], r[0]))
    return rows


def build() -> str:
    videos = len(list((ROOT / "sources").glob("*/*/transcript.md")))
    people = count_md("people")
    topics = count_md("topics")
    channels = per_channel()
    n_channels = len(channels)
    active = sum(1 for _, _, n in channels if n)
    today = dt.date.today().isoformat()

    lines = [
        "## 📊 数据统计",
        "",
        f"> 自动生成于 {today}（每次 CI 构建刷新）。",
        "",
        "| 指标 | 数量 |",
        "|---|---|",
        f"| 视频转录稿 | {videos} |",
        f"| 人物页 | {people} |",
        f"| 主题页 | {topics} |",
        f"| 关注频道 | {n_channels}（活跃 {active}） |",
        "",
        "各频道已收录期数：",
        "",
        "| 频道 | 期数 |",
        "|---|---|",
    ]
    for _, name, n in channels:
        lines.append(f"| {name} | {n} |")
    return "\n".join(lines)


def replace_block(text: str, key: str, payload: str) -> str:
    start = f"<!-- STATS:{key}:START -->"
    end = f"<!-- STATS:{key}:END -->"
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    replacement = f"{start}\n{payload}\n{end}"
    if not pattern.search(text):
        raise SystemExit(f"README.md 缺少标记 {start} … {end}")
    return pattern.sub(lambda _: replacement, text)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="只检查是否需要更新")
    args = ap.parse_args()

    block = build()
    text = README.read_text(encoding="utf-8")
    updated = replace_block(text, "BLOCK", block)

    if updated == text:
        print("stats：README.md 已是最新")
        return
    if args.check:
        print("stats：README.md 需要更新（运行 uv run scripts/stats.py）")
        sys.exit(1)
    README.write_text(updated, encoding="utf-8")
    print("stats：README.md 已更新")


if __name__ == "__main__":
    main()
