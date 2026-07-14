# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Wiki 巡检工具：检查孤儿页、断链、index 覆盖、过时标注。

用法:
    uv run scripts/lint.py
"""

import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"


def all_wiki_pages() -> list[Path]:
    """返回所有 wiki 层 markdown 文件（排除 index.md 和 log.md）。"""
    pages = []
    for md in sorted(WIKI.rglob("*.md")):
        if md.name in ("index.md", "log.md"):
            continue
        pages.append(md)
    return pages


def extract_links(content: str, page_rel: Path) -> list[str]:
    """提取 [[wikilinks]] 和 Markdown 链接的目标路径名（不含扩展名）。"""
    targets = []
    # [[page-name]] 或 [[page-name|display text]]
    for m in re.finditer(r"\[\[([^\]|#]+)(?:[|#][^\]]+)?\]\]", content):
        targets.append(m.group(1).strip().split("/")[-1])
    # [text](../path/to/page.md) 或 [text](../path/to/page)
    page_dir = page_rel.parent
    for m in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", content):
        href = m.group(1)
        if href.startswith(("http://", "https://", "#")):
            continue
        resolved = (page_dir / href).resolve()
        try:
            rel = resolved.relative_to(WIKI)
            targets.append(rel.with_suffix("").as_posix())
        except ValueError:
            # 不在 wiki 目录内，忽略
            pass
    return targets


def page_slug(path: Path) -> str:
    """page 相对于 wiki/ 的路径（不含 .md）。"""
    return path.relative_to(WIKI).with_suffix("").as_posix()


def main() -> None:
    pages = all_wiki_pages()
    issues: list[str] = []
    slug_to_path: dict[str, Path] = {}
    for p in pages:
        slug = page_slug(p)
        slug_to_path[slug] = p

    # ── 索引覆盖 ──
    index_path = WIKI / "index.md"
    index_text = index_path.read_text(encoding="utf-8") if index_path.exists() else ""
    index_slugs = set()
    for m in re.finditer(r"\[([^\]]*)\]\(([^)]+)\)", index_text):
        href = m.group(2)
        if href.startswith(("http://", "https://", "#")):
            continue
        # 相对路径，直接拼 WIKI 目录
        resolved = (index_path.parent / href).resolve()
        try:
            rel = resolved.relative_to(WIKI)
            index_slugs.add(rel.with_suffix("").as_posix())
        except ValueError:
            pass

    not_in_index = [s for s, p in slug_to_path.items()
                    if s not in index_slugs]
    if not_in_index:
        issues.append(f"⚠ index.md 未覆盖 ({len(not_in_index)} 页):\n" +
                      "\n".join(f"  - {s}" for s in not_in_index))

    # ── 孤儿页 & 断链 ──
    inbound: dict[str, set[str]] = defaultdict(set)  # target → source slugs
    outbound: dict[str, set[str]] = defaultdict(set)  # source → target slugs

    for p in pages:
        content = p.read_text(encoding="utf-8")
        slug = page_slug(p)
        targets = extract_links(content, p)
        for t in targets:
            outbound[slug].add(t)
            inbound[t].add(slug)

    # 孤儿：无入链的 people/topics 页面（videos 孤儿正常，从 index 搜即可）
    for s, p in slug_to_path.items():
        if any(s.startswith(pref) for pref in ("people/", "topics/")):
            if s not in inbound:
                issues.append(f"🟡 孤儿页（无入链）: {s}")

    # 断链：链接目标不存在的页面
    for source, targets in outbound.items():
        broken = [t for t in targets if t not in slug_to_path]
        if broken:
            issues.append(f"🔴 断链 ({source}):\n" +
                          "\n".join(f"  → {b}" for b in broken))

    # ── 过时标注 ──
    today = date.today()
    for p in pages:
        content = p.read_text(encoding="utf-8")
        m = re.search(r"^updated:\s*(\d{4}-\d{2}-\d{2})", content, re.MULTILINE)
        if m:
            updated = date.fromisoformat(m.group(1))
            days = (today - updated).days
            if days > 180:
                slug = page_slug(p)
                issues.append(f"🟡 超过半年未更新: {slug}（updated: {m.group(1)}）")

    # ── 报告 ──
    print(f"=== Wiki Lint ===\n{len(pages)} wiki 页 | {len(slug_to_path)} 个 slug | {date.today().isoformat()}\n")
    if not issues:
        print("✅ 无问题。")
    else:
        for i, issue in enumerate(issues, 1):
            print(f"\n{i}. {issue}")
        print(f"\n共 {len(issues)} 项。")

    # 断链应视为严重
    broken_count = sum(1 for i in issues if i.startswith("🔴"))
    if broken_count:
        print(f"\n{broken_count} 个断链，建议修复后再继续摄取。")

    sys.exit(1 if broken_count else 0)


if __name__ == "__main__":
    main()
