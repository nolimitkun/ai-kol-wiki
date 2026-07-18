# AI 正在颠覆的万亿美元行业：语音与法律（All-In，2026-07-14）

- **嘉宾**: [Mati Staniszewski](../people/mati-staniszewski.md)（ElevenLabs 联合创始人/CEO，语音 AI）· [Max（Legora CEO）](../people/legora-max.md)（法律 AI）
- **主持**: Jason Calacanis（及 All-In 团队；现场访谈，法国）
- **来源**: [YouTube](https://www.youtube.com/watch?v=J0bce9WQJ-g) · 52 分钟（自动字幕）
- **转录稿**: [sources/all-in/20260714-J0bce9WQJ-g](../../sources/all-in/20260714-J0bce9WQJ-g/transcript.md)

> 两段"AI 颠覆万亿美元传统行业"的应用层公司访谈：ElevenLabs（语音，$600M ARR）与 Legora（法律，连续 7 季度 QoQ +50%）。共同母题：**架构而非规模、垂直化、独立于前沿模型（model-agnostic）**，以及一个反复出现的紧张——用前沿模型做产品、而前沿实验室又想吃掉你的生意。

## 概要

**ElevenLabs（Mati Staniszewski）**：2022 年起做能"听起来像人"的语音，20 个月到 $100M ARR，如今 $600M、600 人。研究+产品双引擎，小团队按行业（电信/金融/医疗）垂直编队、**每个团队都嵌工程师**。语音 agent 让人反而更愿意打断/更坦诚（催款场景），"whisper 办公室"与踏板（Whisper Flow）改变人机交互。护城河是**架构不是规模** + 千人级音频标注 + 垂直化 + 生态；安全侧做溯源/双层审核/AI 检测；声音 marketplace 已回馈 talent 超 $2200 万，含 James Earl Jones/Darth Vader、Matthew McConaughey、ALS 失声者恢复声音。

**Legora（Max）**：法律服务是 **1 万亿美元/年**市场但软件只占约 400 亿（4%），billable hour 模式被颠覆。像 Palantir 的 forward-deployed engineer 一样派 **forward-deployed lawyer（"legal engineer"）**帮 Kirkland 等律所转型。法律研究的数据护城河"要全不要 80%"（West Law/LexisNexis 双头垄断，甚至要把书运到印度扫描做 page citation）。不做通用法律智能模型，只做窄任务微调模型；compliance 是货币、不做 on-prem。

## 核心观点

### ElevenLabs：语音的规模与增长
- 增长曲线：2022 成立→2023 初首个"像人"的 TTS→20 个月到 $100M ARR→10 个月到 $200M→5 个月到 $300M→现 **$600M**、600 人、首 10 人研究工程零流失（00:00–00:03）。
- 组织：研究 + 产品双引擎，5–10 人小团队按行业垂直编队；**在每个团队（含非工程团队如 talent/legal/go-to-market）嵌一名工程师**，既做自动化、也保证安全审查——"不用编码软件很可能站错位置，用太多也是危险信号"（00:04–00:06）。
- 无 PM：优化"至少精通一个领域、又很懂另一个"的画像；AI 让人从 amateur 跃到 advanced（非 expert），不再被其他职能卡住（00:06–00:08）。

### 语音交互的拐点：更愿打断、更坦诚
- 从"按 0 找人工"的 voice jail 转向"给我 AI operator"；金融催款场景里，人**对 AI 反而更愿说真实处境**（没有面对真人的羞耻），且对 AI 更"snappy"、随时打断直奔要点（00:09–00:15）。
- 硬件/交互：Whisper Flow（底层用 ElevenLabs）+ **脚踏板**把 LLM 从"打字"解放成"意识流口述"——"LLM 特别擅长把一大段意识流理成东西"；可穿戴（Plaude Pocket）自动记录/跟进（00:11–00:13）。

### 安全、身份与声音 marketplace
- 声音是**身份与 IP**：Jason 被人用 ElevenLabs 克隆声音做"斗牛犬讲笑话"频道。安全三招：**溯源追踪 + 语音/文本双层审核（商用/诈骗内容拦截）+ 免费 AI 检测**（对自家和开源模型都做）（00:16–00:19）。
- **marketplace** 让配音演员录一小时授权声音赚钱，已回馈超 **$2200 万**；名人/IP 授权：Matthew McConaughey 多语世界、James Earl Jones 生前把 Darth Vader 声音永久授权 Disney→由 ElevenLabs 实现（Fortnite 里可与达斯·维达互动）、Gordon Ramsay 互动教学、Headspace 冥想本地化（00:19–00:24）。
- 最动人的用例是**给失声者恢复声音**：ALS/喉癌患者（含美国国会议员 Jennifer Wexton 首次用合成声在国会发言）、失声新娘重办婚礼重念誓词（00:21–00:22）。

### ElevenLabs 面对前沿实验室
- 前沿实验室（Anthropic/OpenAI）明确想吃语音生意；ElevenLabs 做**平台、model-agnostic**（客户自选模型），护城河是"交互/沟通这一层"——TTS/STT/turn-taking/music 上持续跑赢；"**是架构而非规模重要**，得改变模型怎么运作 + 很具体的（未标注）数据"，自建千人标注团队（00:25–00:27）。
- 承认对手在"想办法蒸馏/用我们的数据"，有机制减缓但难止；正更认真看**自研模型**（不碰知识工作/编码，专注 interaction）（00:27–00:29）。AGI 观："30–40 年前定义的 AI 测试我们全过了，需要新测试；某些地方已达到了"（00:29–00:30）。

### Legora：法律行业的经济学重排
- 法律服务 **$1 万亿/年**、极度碎片化，软件只占约 **400 亿（4%）**——软件占比应远大于此；且法律是**供给受限**市场（需求 >> 律师供给），服务商开始用技术服务新客群（如 Cooley 直接给创业者上平台）（00:33–00:35）。
- **billable hour 被颠覆**：律所商业模式是"高价卖 associate、低价卖 partner"（Kirkland associate $800/h、partner 可达 $4000/h，但真正关键的 30 分钟远值更多）；企业开始把法务**收回 in-house**（Legora 自己今年收购 4 家、用自家工具做尽调，最快 12 天从 LOI 到 closing——因为创始人动机是尽快成交，律师动机是拖）（00:35–00:37）。
- **forward-deployed lawyer / "legal engineer"**：像 Palantir 的 FDE，坐进 Kirkland 帮 partner 从 pre-AI 转 post-AI；"我们只会和客户一样成功"（00:38–00:39）。junior lawyer 工作不消失但任务变了——从"锁在数据室逐份读文件"变成"编排做这些活的 agent"（00:39–00:40）。

### Legora：数据护城河、窄模型与合规
- 法律研究**"要全不要 80%"**（power law 的反面）：litigator 打十亿美元官司必须有全部案例，所以要把书运到印度双盲录入/OCR、做 **page citation**；West Law 甚至与美国政府有独家案例报告垄断（00:44–00:46、00:56–00:57）。
- 数据护城河 = 律所/企业自有 precedent + Legora 苦活收集全球各司法辖区案例/立法/监管；GC 在加州刚落地南非首客，Legora 可即给 80% 准确的本地法回答（00:40–00:42）。LexisNexis/West Law 这类 legacy 玩家难转 AI-native（招不到人、内部政治），股价被"AI 确定性"压（00:42–00:44）。
- **不做通用法律智能模型**（"浪费时间和钱"），只做**窄任务微调模型**降本降延迟（如 tabular review：100 文档 × 100 prompt = 万次调用，微调抽取合同数据的窄模型很划算）；Opus 4.5/4.6 后 agent 能做端到端案件策略——从"增强"到"真正做事"，人转为编排/管理 agent（00:47–00:49、00:57–00:58）。
- compliance 是货币（托管军工/政府合同），**不做 on-prem/VPC**（拖慢路线图）；这也是法律 AI 难卖、少有人做成的原因，一旦进去就好扩张（也是并购策略的驱动力）（00:49–00:51）。

## 相关主题

- [AI 商业化与价值捕获](../topics/ai-business-and-value-capture.md)（本期核心：应用层公司 vs 前沿实验室、model-agnostic 平台、架构非规模、窄模型、billable hour 颠覆、数据护城河"要全不要 80%"、forward-deployed lawyer）
- [AI 与就业](../topics/ai-and-jobs.md)（语音客服/配音演员/junior lawyer 的任务重排而非消失、人转编排 agent、每个团队嵌工程师）
- [使用 LLM 的实践](../topics/using-llms-in-practice.md)（脚踏板+Whisper Flow 意识流口述、语音 agent 让人更坦诚/更愿打断、agent 编排端到端法律工作）
- [LLM 安全](../topics/llm-security.md)（声音即 IP/克隆滥用、溯源+双层审核+AI 检测、法律数据泄漏与 compliance）
