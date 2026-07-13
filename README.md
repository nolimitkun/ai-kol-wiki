# AI KOL Wiki

把中美 AI KOL 的长视频转录稿整理成结构化知识库，按 [Karpathy 的 LLM Wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)运作：
原始转录稿只增不改，wiki 层由 LLM 增量维护，人只负责规范和关注名单。

**从这里开始阅读 → [wiki/index.md](wiki/index.md)**

## 结构

| 层 | 位置 | 说明 |
|---|---|---|
| Raw Sources | [`sources/`](sources/) | 脚本抓取的带时间戳转录稿，不可变 |
| Wiki | [`wiki/`](wiki/) | 人物页 / 主题页 / 视频页，观点可溯源到时间戳 |
| Schema | [`CLAUDE.md`](CLAUDE.md) + [`watchlist.yaml`](watchlist.yaml) | 规范与 KOL 名单 |

## 使用

```bash
# 发现 watchlist 频道的新视频
uv run scripts/discover.py

# 摄取一个视频（抓元数据 + 字幕 → sources/）
uv run scripts/fetch.py <video-url> --kol <slug>
```

摄取后的阅读与 wiki 更新由 LLM（Claude Code）按 [CLAUDE.md](CLAUDE.md) 的工作流完成，每周定时增量更新。

## 目前覆盖

Andrej Karpathy、Dwarkesh Podcast、Lex Fridman、李沐 等频道；
主题页覆盖 LLM 训练管线、LLM 心理学、AI 与科学发现、算力基础设施、AI 与就业、中美 AI 生态对照等。

> 转录稿来自各视频的公开字幕，版权归原作者所有；wiki 内容为观点整理与综合，均标注来源与时间戳。
