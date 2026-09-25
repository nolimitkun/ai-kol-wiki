# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Wiki 巡检工具：检查孤儿页、断链、index 覆盖、过时标注，
以及引用时间戳是否为信源转录稿里逐字存在的锚点。

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
SOURCES = ROOT / "sources"


def skipped_ids() -> set[str]:
    """sources/skipped.txt 里「已评估、决定不收录」的 video id。

    格式每行 `<video-id>  # 理由`，`#` 开头的整行是注释。
    """
    path = SOURCES / "skipped.txt"
    if not path.exists():
        return set()
    ids = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        ids.add(line.split("#")[0].strip())
    return ids


def unwikied_sources() -> list[str]:
    """已 fetch 但没写 wiki 页、且没被显式 skip 的 source。

    source 目录形如 sources/<kol>/<YYYYMMDD>-<id>/；video 页里会用
    `../../sources/<kol>/<YYYYMMDD>-<id>/transcript.md` 链回转录稿，
    因此按这个**精确路径**匹配（早先按日期做启发式，同一天若有另一个
    视频写了页，就会把真正漏写的那个掩盖掉）。

    在 skipped.txt 里的是「看过、故意不收录」，不算漏写。
    """
    referenced: set[str] = set()
    for md in (WIKI / "videos").glob("*.md"):
        text = md.read_text(encoding="utf-8")
        for m in re.finditer(r"sources/([^/\s)]+)/([^/\s)]+)", text):
            referenced.add(f"{m.group(1)}/{m.group(2)}")

    skipped = skipped_ids()
    missing = []
    for d in sorted(SOURCES.glob("*/*/")):
        if not (d / "transcript.md").exists():
            continue
        # 目录名形如 <YYYYMMDD>-<video-id>，取 id 部分
        vid = d.name.split("-", 1)[1] if "-" in d.name else d.name
        if vid in skipped:
            continue
        if f"{d.parent.name}/{d.name}" not in referenced:
            missing.append(f"{d.parent.name}/{d.name}")
    return missing


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


# ── 时间戳核验：每处满格时间戳必须是其信源转录稿里逐字存在的锚点 ──
# 信源判定与 CLAUDE.md「写作约定」一致：
#   ① 时间戳所在括号里有视频链接 → 用它；
#   ② 否则用此前最近一条「来源：」行声明的视频（可声明多个，任一逐字即可）；
#   ③ 都没有、而整页只链接一个视频 → 用它；视频页默认是自己的转录稿。
# 不用"此前最近出现的链接"兜底：正文交叉引用（"与 [某期](…) 呼应"）会把信源劫走，
# 曾因此把 93 条真锚点误判成对不上。

ANCHOR_RE = re.compile(r"^\[(\d\d:\d\d:\d\d)\]", re.MULTILINE)
TRANSCRIPT_RE = re.compile(r"\]\((?:\.\./)*(sources/[^)\s]*?transcript\.md)\)")
# 少数视频页用 frontmatter `sources: [...]` 声明转录稿
FM_TRANSCRIPT_RE = re.compile(r"^sources:\s*\[\s*(sources/[^\]\s,]*?transcript\.md)", re.MULTILINE)
PAREN_RE = re.compile(r"（[^（）]*）|\[[^\[\]]*\]|\([^()]*\)")
FULL_TS_RE = re.compile(r"(?<![:\d])\d\d:\d\d:\d\d(?![:\d])")
SOURCE_DECL_RE = re.compile(r"来源[：:]")
# 说话人映射块里的时间是 speakers.md 轮次边界，不是转录稿锚点
MAPPING_HEAD_RE = re.compile(r"说话人映射|说话人认定依据|机械分离结果")
# 不是引用的时间：钟点（"北京时间 11:30"）、时长（"音频总长 02:06:36"）
NOT_CITATION_RE = re.compile(r"(时间|总长|时长)\s*$")

_anchor_cache: dict[str, tuple[set[str], str | None]] = {}


def video_anchors(video_md: str) -> tuple[set[str], str | None]:
    """视频页文件名 → (其转录稿的锚点集合, 末锚点)。找不到转录稿时为空集。"""
    if video_md not in _anchor_cache:
        anchors: set[str] = set()
        page = WIKI / "videos" / video_md
        if page.is_file():
            text = page.read_text(encoding="utf-8")
            m = TRANSCRIPT_RE.search(text) or FM_TRANSCRIPT_RE.search(text)
            if m and (ROOT / m.group(1)).is_file():
                anchors = set(ANCHOR_RE.findall((ROOT / m.group(1)).read_text(encoding="utf-8")))
        _anchor_cache[video_md] = (anchors, max(anchors) if anchors else None)
    return _anchor_cache[video_md]


def linked_videos(text: str, page: Path) -> list[str]:
    """text 里链接到的视频页文件名（按出现顺序；支持 ../videos/x.md 与视频页间的 x.md）。"""
    out = []
    videos_dir = (WIKI / "videos").resolve()
    for m in re.finditer(r"\]\(([^)\s#]+?\.md)(?:#[^)]*)?\)", text):
        target = (page.parent / m.group(1)).resolve()
        if target.parent == videos_dir:
            out.append(target.name)
    return out


def timestamp_problems(page: Path) -> tuple[list[str], list[str]]:
    """返回 (对不上信源的, 没有声明信源的)，每项形如 `L行 HH:MM:SS …`。"""
    lines = page.read_text(encoding="utf-8").splitlines()
    is_video = page.parent.name == "videos"
    page_videos = list(dict.fromkeys(linked_videos("\n".join(lines), page)))
    if is_video:
        default = [page.name]
    else:
        default = page_videos if len(page_videos) == 1 else []
    declared = default
    mismatched, undeclared = [], []
    in_frontmatter = bool(lines) and lines[0] == "---"
    in_mapping = False
    for i, line in enumerate(lines, 1):
        if in_frontmatter:
            if i > 1 and line == "---":
                in_frontmatter = False
            continue
        if MAPPING_HEAD_RE.search(line):
            in_mapping = True
        elif in_mapping and not line.startswith(">"):
            in_mapping = False
        if in_mapping:
            continue
        if not is_video and SOURCE_DECL_RE.search(line):
            vids = linked_videos(line, page)
            if vids:
                declared = vids
        spans = [(p.start(), p.end(), linked_videos(p.group(0), page)) for p in PAREN_RE.finditer(line)]
        for m in FULL_TS_RE.finditer(line):
            if NOT_CITATION_RE.search(line[:m.start()]):
                continue
            ts = m.group(0)
            own = next((v for s, e, v in spans if s <= m.start() < e and v), None)
            sources = own[-1:] if own else declared
            if not sources:
                undeclared.append(f"L{i} {ts}")
                continue
            if any(ts in video_anchors(v)[0] for v in sources):
                continue
            # 最常见的原因不是时间戳错，而是信源没声明、继承了上一节的「来源：」
            elsewhere = [v for v in page_videos if v not in sources and ts in video_anchors(v)[0]]
            lasts = [video_anchors(v)[1] for v in sources]
            if elsewhere:
                hint = f"在本页链接的 {'、'.join(v[:-3] for v in elsewhere)} 里逐字存在——多半是缺「来源：」声明"
            elif not any(lasts):
                hint = "信源页没有可读的转录稿"
            elif all(last is None or ts > last for last in lasts):
                hint = (f"超出转录稿结尾（末锚点 {max(x for x in lasts if x)}）——若内容确在这期，"
                        "按 CLAUDE.md 改成粗略写法并注明；否则是信源判错")
            else:
                near = max((a for v in sources for a in video_anchors(v)[0] if a <= ts), default=None)
                hint = f"不是锚点（此前最近锚点 {near}）——按内容找它所在的锚点块"
            mismatched.append(f"L{i} {ts} → {'、'.join(s[:-3] for s in sources)}：{hint}")
    return mismatched, undeclared


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

    # ── 已摄取但未写 wiki 页 ──
    unwikied = unwikied_sources()
    if unwikied:
        issues.append(f"🟠 已摄取但似乎没写 wiki 页 ({len(unwikied)} 个 source):\n" +
                      "\n".join(f"  - sources/{s}" for s in unwikied))

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

    # ── 时间戳核验 ──
    undeclared_pages = []
    for p in pages:
        mismatched, undeclared = timestamp_problems(p)
        if mismatched:
            shown = mismatched[:5] + ([f"……另 {len(mismatched) - 5} 处"] if len(mismatched) > 5 else [])
            issues.append(f"🟠 时间戳在信源转录稿里不逐字 ({page_slug(p)}，{len(mismatched)} 处):\n" +
                          "\n".join(f"  - {x}" for x in shown))
        if undeclared:
            undeclared_pages.append((page_slug(p), len(undeclared), undeclared[0]))
    if undeclared_pages:
        total = sum(n for _, n, _ in undeclared_pages)
        issues.append(
            f"🟡 时间戳没有声明信源 ({len(undeclared_pages)} 页，{total} 处；"
            "括号里没带视频链接、此前也没有「来源：」行，且整页链接了不止一个视频):\n" +
            "\n".join(f"  - {s}：{n} 处（首处 {first}）"
                      for s, n, first in sorted(undeclared_pages, key=lambda x: -x[1])))

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
