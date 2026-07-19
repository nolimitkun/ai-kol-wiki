# 📚 AI KOL Wiki

中美 AI 领域深度访谈与演讲的结构化知识库：视频的完整转录稿 + 个人物页 + 跨 KOL 对照的主题页。

- **[开始浏览 .md 格式](wiki/index.md)**
- **[开始浏览 github page 格式](https://nolimitkun.github.io/ai-kol-wiki/)**

## 💡 项目介绍

我们把中美 AI 领域 KOL 的长视频（Podcast 访谈、技术演讲、投资札记）转录成带时间戳的全文，由 LLM 提取核心观点、标注来源、交叉链接，维护成一个可检索、可对比、持续更新的 Markdown 知识库。

与 RAG 不同：不是每次查询时临时搜索，而是**提前整理好、标注好关联、标注好共识与分歧**——像一本活的 AI 领域年鉴。

## 🗺️ 覆盖范围

| 维度 | 内容 |
|---|---|
| **美方 KOL** | Andrej Karpathy、Jensen Huang、Dwarkesh Patel、Lex Fridman、No Priors（Sarah Guo & Elad Gil）、Latent Space（swyx & Alessio）、a16z（Benedict Evans、Steven Sinofsky 等） |
| **中方 KOL** | 张小珺《商业访谈录》——姚顺宇（Google DeepMind）、何小鹏（小鹏集团）、阳萌（安克创新）、Freda（Altimeter）、雨森（真格基金）、Lewis Hong（前SpaceX） |
| **主题** | LLM 训练管线、AI 商业化与价值捕获、物理 AI 与机器人、AI 与就业、AI 基础设施、中美 AI 生态对照、LLM 安全、评估与 Benchmark、LLM OS、AI 实验室文化、LLM 心理学、LLM 实用方法论、AI 与科学发现 |

## 🧭 阅读指南

- 按人物浏览：[人物索引](wiki/index.md#人物)
- 按主题深度阅读：[主题索引](wiki/index.md#主题)——每个主题页并列中美 KOL 对同一问题的看法，标注共识与分歧
- 按视频查阅：[视频索引](wiki/index.md#视频)——每期有概要 + 核心观点摘要 + 时间戳溯源

> 所有观点标注来源（视频页 + `[HH:MM:SS]` 时间戳），区分"KOL 认为"与客观事实。

<!-- STATS:BLOCK:START -->
## 📊 数据统计

> 自动生成于 2026-07-19（每次 CI 构建刷新）。

| 指标 | 数量 |
|---|---|
| 视频转录稿 | 56 |
| 人物页 | 49 |
| 主题页 | 13 |
| 关注频道 | 9（活跃 9） |

各频道已收录期数：

| 频道 | 期数 |
|---|---|
| Latent Space (swyx & Alessio) | 10 |
| 张小珺（商业访谈录） | 9 |
| Lex Fridman | 7 |
| All-In Podcast (Chamath, Sacks, Friedberg, Calacanis) | 6 |
| Dwarkesh Patel | 6 |
| Andrej Karpathy | 5 |
| No Priors (Sarah Guo & Elad Gil) | 5 |
| 月球大叔（Uncle Moon） | 5 |
| a16z (Andreessen Horowitz) | 3 |
<!-- STATS:BLOCK:END -->


## ⚙️ 技术细节

本仓库按 [Karpathy 的 LLM Wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 运作：

| 层 | 位置 | 说明 |
|---|---|---|
| Raw Sources | `sources/` | 脚本抓取的带时间戳转录稿，**只增不改** |
| Wiki | `wiki/` | LLM 维护的人物页 / 主题页 / 视频页 |
| Schema | `CLAUDE.md` + `watchlist.yaml` | 人来定规范和 KOL 名单 |

脚本用法：

```bash
# 发现新视频
uv run scripts/discover.py

# 摄取（有字幕）
uv run scripts/fetch.py <url> --kol <slug>

# 摄取（无字幕 → faster-whisper 本地转录，按需注入）
uv run --with faster-whisper scripts/fetch.py <url> --kol <slug> --transcribe
# 同上但用 GPU（额外注入 CUDA 运行库 wheel，脚本自动配好库路径）
uv run --with faster-whisper --with nvidia-cublas-cu12 --with nvidia-cudnn-cu12 \
  scripts/fetch.py <url> --kol <slug> --transcribe

# Wiki 巡检
uv run scripts/lint.py

# 刷新本文档的数据统计（CI 每次构建自动运行）
uv run scripts/stats.py
```

转录稿来自各视频的公开字幕，版权归原作者所有。
