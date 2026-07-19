# All-In 主播团（Chamath、Sacks、Friedberg、Calacanis + 常客 Brad Gerstner）

- **频道**: [YouTube @allin](https://www.youtube.com/@allin)
- **watchlist slug**: `all-in`

四位主播 + 高频客座的合议式播客。本库最初只收录其**嘉宾访谈**（ElevenLabs、Legora、Cerebras、Black Forest Labs、Pat Gelsinger、Lovable 等），但 2026 年 7 月起主播本人在 token 经济学、监管制度设计、主权 AI 等题上给出了足够系统的立场，故单独建页。

> **使用提示**：本页人物均有明确的商业与政治利益关联（Sacks 曾任政府 AI 相关职务、Chamath 经营 8090、Gerstner 的 Altimeter 是 Anthropic/OpenAI 投资人）。本库按"X 认为"记录，读者应把利益相关性作为解读的一部分。

## 各人立场

### Chamath Palihapitiya — ROI 怀疑论 + 隐私脆弱论
- **最锋利的一手数据**：自家 CTO 报告 **token 成本每 45 天翻一倍，下游生产力提升最多 5%**；CTO 的解释是"**要拿到下一档改进，你得用多得多的 token，因为我们实际上已经渐近了**"（[视频](../videos/20260711-all-in-ipo-token-roi-china-open-source.md) 00:05）。
- **宏观 ROI 核查**：拆掉 NVIDIA 卖芯片的收入后，标普 493 的 EPS 增长 9% 中绝大部分来自**通胀之上的定价权**、另 3% 来自回购 →"按所有公开数据，**AI 的实际 ROI 在 0 到 2% 之间**"。
- 结构判断：**企业侧更脆**（买家少、迟早被问 EPS 提升）、**消费侧是避风港**（买家多两个数量级、单价低，免疫 ROI 拷问）。风险时点是"**财报不及预期的那一刻**"——人们裁员很难，砍其它成本很容易。
- **隐私是脆的**：xAI 代码库泄露事件后——"AI 里到处都是不明显的数据泄露向量。如果你以为翻一下 **ZDR（zero data retention）**开关就没事了，**答案应该是：不会没事的，因为这些都保证不了**……他们尽了力也可能有连自己都不知道的暗门。"推论是**必须有独立第三方层**来对接模型（他承认这与自家 8090 业务相关）（[视频](../videos/20260718-all-in-sro-regulation-datacenters.md) 00:44–00:45）。
- **主权 AI**：参加联合国 AI 委员会后的结论——"**没有一个国家不在琢磨自己的主权 AI 战略，而且我不认为他们相信用闭源美国模型是答案**"；多国宁愿拿开源模型自建全栈。
- **电力**：美国到 2050 年将短缺约 2.5 个加州的用电量；数据中心资产定价里"**曲线前端极端之高**"（今天就能通电的电力值大钱），因为往后看约 **40% 的项目会被搁置**。并给出 behind-the-meter 与清洁空气许可的具体机制解释。
- 个人实践：token 成本降 95% 后把 agent 从日跑改成**小时跑**、把一个 agent 拆成三个并行——"早上醒来 14 个任务已经完成"。自估 **98%** 的 Fable 5 prompt 其实该跑在便宜模型上。

### David Sacks — 反监管俘获 + "心有余而力不足"
- **对 SRO 的五个条件**（本库最可引用的制度设计清单，见[视频页](../videos/20260718-all-in-sro-regulation-datacenters.md) 00:08–00:11）：①代表性要广（必须含创业公司与开源）②只审真前沿模型③**只处理灾难性风险**（网络安全与 CBRN，不该管虚假信息/微冒犯，"不该变成言论监管者"）④先自愿后强制⑤**必须是替代品而非附加品**。
- 他愿意接受 SRO 的理由是它"无限好于"新设机构（会变成"**AI 的车管所**"）；对 Dario 主张的"AI 的 FAA"的具体反驳：FAA 全新机型型号合格证要 **5–9 年**，"这是许可制监管——你说的是把一个每几个月发新版的系统换成时间尺度以年计的系统"。
- **对 Anthropic 的持续指控**：跑"基于恐惧营销的监管俘获战略"；引 Politico 报道称其推行**州级"层层加码"策略**、刻意制造 patchwork 而非统一的全国框架。
- 政治经济学观察："**你去跟政府说'请监管我'，政府里几乎没有人会说'不不不，我们不够格'**"——单方面让步只招致层层加码，"这些公司总得长出脊梁，决定在哪里划线"。
- **开源份额下降的解释**："**心有余而力不足**"——企业**想**多元化（Karp 说的"泄露 alpha"担忧），但大多数**没有技术能力**建 token 路由中间件；Coinbase、DoorDash 做到了。他同时承认**开源是"暗 token"**、不体现为收入，所以用收入份额判定胜负是有偏的。
- **"落后就开源、追平就闭源"**：字节一直闭源、Qwen 转闭、Z.ai 看来也在转 →"你保持开源直到接近前沿，然后有极强的动机转闭"；并指出这正是 OpenAI 三年前走过的路、也是 Google 对 Android 做的。

### David Friedberg — 制度机制 + 影响力行动论
- 对 **SRO** 的机制解释最完整：FINRA/NFA 让机构自设规则互相核查；相对政府机构的优势是**可调整**（加州立法一年后就对不上技术）且**运转更快**；有联邦监督但不受联邦控制。
- ⚠️ **外国影响论**：用**反 GMO 情绪**类比反数据中心运动（Russia Today 2010 入美、2022 被驱逐，其存续与反 GMO 情绪的起落同步），并追溯 KGB 冷战时期针对西方民主国家的媒体行动。**本库标注：这是相关而非因果的论证，除 OpenAI 一篇博文外未给出可核验证据。**
- **AI 化改造存量资产**是他的并购框架：Stripe/Block 竞购 PayPal、Ryan Cohen 竞购 eBay、Bending Spoons 收 Evernote/AOL/Vimeo——"一批 AI 原生的操盘手在看第一代数字原生业务：**没在好好用网络、运营不佳、超支、没用好 AI**"，预测这类**大额"复活式并购"会成潮**。

### Jason Calacanis — 落地实践的记录者
- 长期主张**行业自我认证**（类比 MPAA/游戏分级）先于政府认证，Demis 的 SRO 提案被他视为自己观点的兑现。
- 一手 vibe coding 实践：非技术员工 4–8 小时做出他"十年前要 50 万美元"的内网；对 agent 本身做优化后 **token 用量降 80%**。
- **token 价格阶梯**（每百万 input token）：Fable ≈56 / OpenAI ≈26 / Grok ≈1.5 / 中国模型 ≈0.5 美元。
- 组织行为学诊断（与 Chamath 共同提出）：**工程师不与钱挂钩、CFO 才与钱挂钩**——"就像你订差旅时根本看不到价格"。
- 预测 Apple 因 M7 Ultra 的大内存（传闻 1.5 TB）可让前一代前沿级模型跑在 Mac Studio 上，将对闭源 API 形成向下压力。

### Brad Gerstner（Altimeter，常客） — 前沿仍在扩大领先
- **反方主论点**：deepseek 时刻以来 18 个月，"开源会杀死前沿"的论证很响，**但场上事实相反——经济价值/钱包份额在向前沿实验室集中**（[视频](../videos/20260711-all-in-ipo-token-roi-china-open-source.md) 00:27–00:28）。
- **单位经济学**：摘要文档用 2 万个廉价 token 当然该下放；但**替代一个软件工程师 2 小时可能是 200 万个昂贵 token**，长任务中途断掉时 token 照烧、时间照赔。"若 agent 替代的是 200 美元/小时的顾问，**花 3 美元还是 15 美元的推理成本无关紧要**。"
- **反共识猜想**：大家默认"智能在收敛"（benchmark 上确实在收敛），**但收入分布完全没收敛**；若超级智能变得递归，**领先可能在扩大**——"模型越聪明→收入越多→算力越多→模型越好"。
- 对 Chamath 的 ROI 论"只在时间尺度上有分歧"：承认今天大量支出在实验桶里、确无直接 ROI，但"我们太早了，没人在乎"，且 TAM 是"地球上每一家公司"。
- IPO 视角：SpaceX IPO 是教科书模板（融资 750 亿 / 估值 1.75 万亿 / 指数早期纳入 / 分阶段按里程碑解禁），Anthropic 与 OpenAI 都在照抄作业。

## 呼应与分歧（跨库）

- **本库最清晰的一组对峙**：Chamath（ROI 反噬将至）vs Gerstner + Sacks（前沿在扩大领先）。两边都有数据，分歧可证伪，见 [AI 的商业化与价值捕获](../topics/ai-business-and-value-capture.md)。
- 与 [a16z 成长期合伙人](../videos/20260529-a16z-picking-ai-winners.md)高度互补：后者同样把"**模型层的市场结构**"指认为决定价值归属的最大未知数，且同样认为竞争压低 token 价格对整体经济更好。
- Sacks 的 SRO 五条件 + Friedberg 的机制解释，是本库 [LLM 安全与治理](../topics/llm-security.md) 中第一份制度层面的方案，与 [Gray Swan](gray-swan-founders.md)（红队/评估）、[Onyx](maxim-bar-kogan.md)（运行时守门）分处三个层次。
- Chamath 的"ZDR 保证不了什么 → 需要独立第三方层"与 [Onyx 的"AI 看管 AI"](maxim-bar-kogan.md)、[NanoClaw 的隔离模型](gavriel-cohen.md)是同一问题的三种答案。
- 主权 AI 与"落后就开源、追平就闭源"补入 [中美 AI 竞争](../topics/china-us-ai.md)。

## 已收录访谈

| 日期 | 视频 | 主题 |
|---|---|---|
| 2026-07-10 | [Cerebras + Black Forest Labs](../videos/20260710-all-in-cerebras-bfl-open-source.md) | buildout、推理的 Moore's law、开源闭合 gap、生成式→world-action model |
| 2026-07-11 | [IPO、Token ROI 之辩、中国是否终结开源](../videos/20260711-all-in-ipo-token-roi-china-open-source.md) | 三大 IPO、ROI 反噬、开闭源之争、主权 AI |
| 2026-07-14 | [ElevenLabs + Legora](../videos/20260714-all-in-11labs-legora-voice-law.md) | 语音与法律的应用层颠覆 |
| 2026-07-15 | [Pat Gelsinger + Lovable](../videos/20260715-all-in-gelsinger-lovable.md) | Intel 复盘、台湾能源风险、vibe coding 的兑现 |
| 2026-07-18 | [SRO 监管提案、数据中心禁令、企业数据泄露](../videos/20260718-all-in-sro-regulation-datacenters.md) | 自律组织制度设计、能源与政治阻力、ZDR 的脆弱性 |
