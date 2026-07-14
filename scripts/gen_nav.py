# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""从 wiki/index.md 生成 MkDocs 侧边栏导航（literate-nav 的 SUMMARY.md）。

index.md 已经把视频按频道（### 频道名）分好组，这里直接复用它作为
单一事实来源，输出一个嵌套列表：视频层级为「视频 → 频道 → 单集」，
从而在 GitHub Page 左侧目录的 Videos 下多出一级 channel。

用法：uv run scripts/gen_nav.py [输出路径]   # 默认 _docs/SUMMARY.md
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "wiki" / "index.md"

# 匹配列表项里的第一个 markdown 链接：- ... [文本](目标.md)
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+\.md)\)")


def parse_index(text: str):
    """返回 (people, topics, videos)。
    people/topics: [(title, target)]；videos: [(channel, [(title, target)])]。
    index.md 里的链接相对 wiki/ 目录，这里统一加 wiki/ 前缀（SUMMARY.md 位于站点根）。
    """
    people: list[tuple[str, str]] = []
    topics: list[tuple[str, str]] = []
    videos: list[tuple[str, list[tuple[str, str]]]] = []

    section = None  # "people" | "topics" | "videos" | None
    for line in text.splitlines():
        if line.startswith("## "):
            head = line[3:].strip()
            section = {"人物": "people", "主题": "topics", "视频": "videos"}.get(head)
            continue
        if section == "videos" and line.startswith("### "):
            videos.append((line[4:].strip(), []))
            continue
        m = LINK.search(line)
        if not m or not line.lstrip().startswith("-"):
            continue
        title, target = m.group(1).strip(), "wiki/" + m.group(2).strip()
        if section == "people":
            people.append((title, target))
        elif section == "topics":
            topics.append((title, target))
        elif section == "videos" and videos:
            videos[-1][1].append((title, target))
    return people, topics, videos


def render(people, topics, videos) -> str:
    out: list[str] = ["- [首页](index.md)", "- [完整目录](wiki/index.md)"]

    out.append("- 人物")
    out += [f"    - [{t}]({p})" for t, p in people]

    out.append("- 主题")
    out += [f"    - [{t}]({p})" for t, p in topics]

    out.append("- 视频")
    for channel, items in videos:
        out.append(f"    - {channel}")
        out += [f"        - [{t}]({p})" for t, p in items]

    return "\n".join(out) + "\n"


def main() -> None:
    dest = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "_docs" / "SUMMARY.md"
    people, topics, videos = parse_index(INDEX.read_text(encoding="utf-8"))
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(render(people, topics, videos), encoding="utf-8")
    n_videos = sum(len(v) for _, v in videos)
    print(
        f"写入 {dest}："
        f"{len(people)} 人物 | {len(topics)} 主题 | "
        f"{len(videos)} 频道 / {n_videos} 视频"
    )


if __name__ == "__main__":
    main()
