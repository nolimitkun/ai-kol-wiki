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
  seen.txt                     # 已 fetch 的视频 ID，一行一个（fetch.py 自动追加）
  skipped.txt                  # 已评估、主动决定不收录的视频 ID + 理由
  <kol-slug>/
    <YYYYMMDD>-<video-id>/
      transcript.md            # 带 frontmatter 的转录稿，含 [HH:MM:SS] 时间戳锚点
      speakers.md              # （可选）说话人分离 sidecar：说话占比 + 轮次表，匿名 SPEAKER_XX
wiki/
  index.md                     # 内容目录（按人物 / 主题 / 视频组织）
  log.md                       # 追加式操作日志
  people/<name>.md             # 人物页：背景、立场、观点汇总
  topics/<topic>.md            # 主题页：跨 KOL 观点综合，标注共识与分歧
  videos/<YYYYMMDD>-<kol>-<slug>.md  # 单视频页：概要 + 核心观点
scripts/
  fetch.py                     # 摄取单个视频：uv run scripts/fetch.py <url> --kol <slug>
  discover.py                  # 扫描 watchlist 里各频道的新视频：uv run scripts/discover.py
  backfill_diarization.py      # 给已摄取的转录稿补做说话人分离，写 speakers.md sidecar
```

## 工作流

### Discover（发现新视频）
1. `uv run scripts/discover.py` — 列出 watchlist 各频道中未摄取、时长达标的新视频。
2. 对每个值得收录的视频执行 Ingest。判断标准：实质性访谈/演讲/教程，跳过预告片、shorts、纯营销。
3. **判定不收录的，写进 `sources/skipped.txt`**（`<video-id>  # 理由`），这样以后 discover 不再重复列出。
   否则同一批老候选每天都会占满输出。discover 会报出被跳过的数量，不会悄悄隐藏。

**seen.txt vs skipped.txt**：`seen.txt` = 已 fetch（转录稿已存档，fetch.py 自动写）；
`skipped.txt` = 看过后主动放弃。两者分开，是因为 **fetch ≠ 已摄取**：
若 fetch 之后才判定不收录，转录稿会留档但没有 wiki 页——这种情况必须显式写进
`skipped.txt`，否则 `lint.py` 会一直把它报成「已摄取但没写 wiki 页」。

### Ingest（摄取一个视频）
1. `uv run scripts/fetch.py <url> --kol <slug>` — 抓元数据和字幕，生成 `sources/.../transcript.md`。
   - 若有字幕：自动下载 VTT → 纯文本（带 [HH:MM:SS] 时间戳锚点）。
   - 若无字幕但有英文配音版：用 `--lang zh-Hans` 从配音版取中文字幕（张小珺频道常用）。
   - 若完全无字幕：用 `--transcribe` 一键下载音频 + faster-whisper 本地转录。模型体积大不进内联依赖，按需注入：`uv run --with faster-whisper scripts/fetch.py <url> --kol <slug> --transcribe`（首次会拉模型约 1.5GB；faster-whisper 基于 CTranslate2，不依赖 torch，比原版快约 4 倍，默认模型 large-v3-turbo）。
     - GPU 转录（本机有 RTX 5090，明显更快）：再注入两个 CUDA 运行库 wheel 即可，脚本会自动配好 LD_LIBRARY_PATH：`uv run --with faster-whisper --with nvidia-cublas-cu12 --with nvidia-cudnn-cu12 scripts/fetch.py <url> --kol <slug> --transcribe`。缺这两个 wheel 或无 GPU 时自动回退 CPU；也可用 `--device cpu` 强制。
     - **访谈类建议再加 `--diarize` 做说话人分离**（多注入 `--with pyannote.audio`）：在转录稿里插入 `SPEAKER_00:` / `SPEAKER_01:` 标签，让"谁说的"有机械依据，而不是靠读内容猜。首次需用同一 HF 账号接受**三个** gated 仓库的条款（`speaker-diarization-3.1`、`segmentation-3.0`、`speaker-diarization-community-1`，缺一个就 403；条款按账号生效，换 token 不带过去），再 `export HF_TOKEN=<token>`；无 GPU 或未配 token 时自动跳过，仍产出无标签转录稿。
   - 旧方式 `--audio` 仍可用，仅下载音频不转录。
2. **完整阅读**转录稿，提取：核心论点、事实性断言、预测、与他人观点的呼应或冲突。
   - 转录稿带 `SPEAKER_XX` 标签时，结合视频标题/简介/频道判断每个标签对应谁，在视频页开头记一次映射（如 `SPEAKER_00 = 张小珺（主持）`、`SPEAKER_01 = 姚顺宇`）。**匿名标签留在 `sources/` 不改**——认人是编辑判断，属于 wiki 层，符合"原始资料只增不改、勘误在 wiki 层处理"。
   - 分离结果并非完美（抢话、串场会错配）。标签是证据不是判决：与内容明显矛盾时以内容为准，并在视频页注明存疑。
   - 同目录若有 `speakers.md`（补做分离的 sidecar），把它和转录稿对照着读：轮次表给出各时间段的说话人，说话占比低的通常是主持人。

### Backfill（给旧转录稿补分离）
`uv run --with pyannote.audio scripts/backfill_diarization.py --dry-run` 先看范围，去掉 `--dry-run` 执行。
只**新增** `speakers.md`，`transcript.md` 逐字节不动（脚本用 sha256 前后比对做硬保证）——
因为补做分离要重跑 whisper 取片段级时间轴，而重跑会让切分漂移，
重写转录稿会使 wiki 里已有的 `[HH:MM:SS]` 引用失准。只增不改，旧引用全部继续有效。
音频缺失会自动重下（`.gitignore` 已排除音频，不进仓库），默认用完即删。
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
