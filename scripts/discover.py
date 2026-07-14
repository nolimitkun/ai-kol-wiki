# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml", "yt-dlp"]
# ///
"""扫描 watchlist.yaml 里各频道的最新视频，列出尚未摄取、时长达标的条目。

用法:
    uv run scripts/discover.py            # 每个频道看最近 10 条
    uv run scripts/discover.py -n 25      # 看最近 25 条
"""

import argparse
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SEEN = ROOT / "sources" / "seen.txt"


def fetch_channel(kol: dict, n: int) -> subprocess.CompletedProcess | None:
    """抓单个频道的最近 N 条（仅列表，不下载）。超时返回 None。"""
    try:
        return subprocess.run(
            ["yt-dlp", "--flat-playlist", "--playlist-end", str(n),
             "--print", "%(id)s\t%(duration)s\t%(title)s", kol["channel"]],
            capture_output=True, text=True, timeout=120,
        )
    except subprocess.TimeoutExpired:
        return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", type=int, default=10, help="每个频道检查最近 N 条")
    args = ap.parse_args()

    kols = yaml.safe_load((ROOT / "watchlist.yaml").read_text(encoding="utf-8"))["kols"]
    seen = set(SEEN.read_text().split()) if SEEN.exists() else set()

    # 各频道相互独立、纯网络等待，并发抓取；map 保持原顺序输出。
    with ThreadPoolExecutor(max_workers=min(8, len(kols) or 1)) as ex:
        results = list(ex.map(lambda k: fetch_channel(k, args.n), kols))

    total = 0
    for kol, r in zip(kols, results):
        print(f"\n## {kol['name']}  ({kol['slug']})")
        if r is None:
            print("  !! 抓取超时（120s）")
            continue
        if r.returncode != 0:
            print(f"  !! 抓取失败: {r.stderr.strip().splitlines()[-1] if r.stderr else '未知错误'}")
            continue
        min_sec = kol.get("min_minutes", 20) * 60
        found = 0
        for line in r.stdout.strip().splitlines():
            vid, dur, title = (line.split("\t", 2) + ["", ""])[:3]
            if vid in seen:
                continue
            if dur not in ("NA", "") and float(dur) < min_sec:
                continue
            mins = f"{round(float(dur) / 60)}min" if dur not in ("NA", "") else "?min"
            print(f"  [{mins:>7}] {title}")
            print(f"            uv run scripts/fetch.py 'https://www.youtube.com/watch?v={vid}' --kol {kol['slug']}")
            found += 1
        if found == 0:
            print("  （没有新视频）")
        total += found

    print(f"\n共 {total} 个候选新视频。")


if __name__ == "__main__":
    main()
