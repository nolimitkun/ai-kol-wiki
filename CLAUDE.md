# AI KOL Wiki — Schema

本仓库按 [Karpathy 的 LLM Wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 运作：
把中美 AI KOL 的长视频转录稿作为**不可变原始资料**，由 LLM 增量维护一个结构化、互相链接的 Markdown 知识库。

## 三层结构

| 层 | 位置 | 谁负责 |
|---|---|---|
| Raw Sources | `sources/` | 脚本抓取，**只增不改** |
| Wiki | `wiki/` | LLM 完全拥有，随新资料更新 |
| Schema | 本文件 + `watchlist.yaml` | 人来定规范和关注名单 |

## 目录结构

```
watchlist.yaml                 # 关注的 KOL / 频道名单（人来维护）
sources/
  seen.txt                     # 已摄取的视频 ID，一行一个
  <kol-slug>/
    <YYYYMMDD>-<video-id>/
      transcript.md            # 带 frontmatter 的转录稿，含 [HH:MM:SS] 时间戳锚点
wiki/
  index.md                     # 内容目录（按人物 / 主题 / 视频组织）
  log.md                       # 追加式操作日志
  people/<name>.md             # 人物页：背景、立场、观点汇总
  topics/<topic>.md            # 主题页：跨 KOL 观点综合，标注共识与分歧
  videos/<YYYYMMDD>-<kol>-<slug>.md  # 单视频页：概要 + 核心观点
scripts/
  fetch.py                     # 摄取单个视频：uv run scripts/fetch.py <url> --kol <slug>
  discover.py                  # 扫描 watchlist 里各频道的新视频：uv run scripts/discover.py
```

## 工作流

### Discover（发现新视频）
1. `uv run scripts/discover.py` — 列出 watchlist 各频道中未摄取、时长达标的新视频。
2. 对每个值得收录的视频执行 Ingest。判断标准：实质性访谈/演讲/教程，跳过预告片、shorts、纯营销。

### Ingest（摄取一个视频）
1. `uv run scripts/fetch.py <url> --kol <slug>` — 抓元数据和字幕，生成 `sources/.../transcript.md`。
   - 若有字幕：自动下载 VTT → 纯文本（带 [HH:MM:SS] 时间戳锚点）。
   - 若无字幕但有英文配音版：用 `--lang zh-Hans` 从配音版取中文字幕（张小珺频道常用）。
   - 若完全无字幕：用 `--transcribe` 一键下载音频 + faster-whisper 本地转录。模型体积大不进内联依赖，按需注入：`uv run --with faster-whisper scripts/fetch.py <url> --kol <slug> --transcribe`（首次会拉模型约 1.5GB；faster-whisper 基于 CTranslate2，不依赖 torch，比原版快约 4 倍，默认模型 large-v3-turbo）。
   - 旧方式 `--audio` 仍可用，仅下载音频不转录。
2. **完整阅读**转录稿，提取：核心论点、事实性断言、预测、与他人观点的呼应或冲突。
3. 创建 `wiki/videos/` 页；更新或创建相关 `wiki/people/` 和 `wiki/topics/` 页。
4. 维护交叉链接（相对路径 Markdown 链接）；更新 `wiki/index.md`。
5. 在 `wiki/log.md` 追加一行操作记录。

### Query（查询）
从 `wiki/index.md` 出发定位相关页面，综合回答并**引用来源**（视频页 + 时间戳）。
有价值的新综合结论可以回填为新的 topic 页。

### Lint（巡检，每积累 ~10 个视频做一次）
- 检查主题页之间的矛盾、过时断言（KOL 改口了要标注时间线，不要删旧观点）
- 找出没有入链的孤儿页、该建未建的交叉链接
- 确认 index.md 覆盖所有页面

## 写作约定

- **观点必须可溯源**：wiki 中每条实质性观点后面标 `（[视频页](../videos/xxx.md) HH:MM:SS）`。
- **区分转述与断言**：KOL 的观点写成"X 认为…"，不要写成客观事实。
- **中美对照是本库的核心价值**：topic 页里尽量并列中美 KOL 对同一问题的看法。
- 人物页/主题页用中文写作；专有名词、术语保留英文原文。
- 时间一律写绝对日期（如 2026-07），不写"最近""上个月"。
- `sources/` 下的文件一旦写入不再修改；勘误在 wiki 层处理。
