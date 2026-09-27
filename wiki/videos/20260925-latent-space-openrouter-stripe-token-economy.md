# OpenRouter × Stripe：分发是模型实验室最被低估的短板，以及"10 万亿美元 token 经济"的安全命题（Latent Space，2026-09-25）

- **嘉宾**: **Alex Atallah**（OpenRouter 联合创始人兼 CEO，OpenSea 联合创始人）、**Anjney Midha**（a16z 普通合伙人，前 Discord 平台负责人，Anthropic 早期投资人，Mistral A 轮领投）
- **主持**: [Latent Space 主播](../people/latent-space-hosts.md)（swyx）
- **来源**: [YouTube](https://www.youtube.com/watch?v=dCX4PE2HxMs) · 83 分钟（英文自动字幕）
- **转录稿**: [sources/latent-space/20260925-dCX4PE2HxMs](../../sources/latent-space/20260925-dCX4PE2HxMs/transcript.md)

> **说话人认定依据**：自动字幕**只有 `>>`，没有姓名标签**。两位嘉宾的分工从自述可硬性区分——**Anjney Midha** = "when I was running the platform of Discord"（[00:10:09]）、"I led the series A into Mistral"（[00:12:10]）、"I was one of the first investors in Anthropic"（[00:18:14]）；**Alex Atallah** = "I built a Chrome extension called window AI"（[00:36:27]）、"we blocked 10x as much dollar volume last month"（[01:10:56]）。**开场有一段两人轮流回忆 2011 年 Stanford Review 相识，该处不逐句区分。**

> **自动字幕专名对照表**：`open router` → OpenRouter、`openc`/`OpenC`/`open C` → OpenSea、`Mistral`/`mistral`/`Misreal`/`astral` → Mistral、`Mixtra`/`Mixrol`/`mixtrol`/`MR 8 by 8 by7B` → Mixtral 8x7B、`BFL`/`Black Force Labs`/`BSL` → Black Forest Labs、`Giam`/`Guiam`/`Gom` → Guillaume Lample、`Marina`/`Alam Marina` → LMArena、`Anastasia`/`Anastasio` 与 `Whan` → LMArena 两位创始人（⚠️ 拼写未核实）、`AXI`/`Axi Infinity` → Axie Infinity、`NFD` → NFT、`Klein` → Cline、`Dream Tavern` → SillyTavern 类角色扮演应用（⚠️ 未核实）、`rapper`/`rappers` → wrapper/wrappers（⚠️ 全篇误识）、`plasma`/`plasmo` → Plasmo、`Lewis Vichy` → Louis Vichy（⚠️ 拼写未核实）、`Andre Karpathi` → Andrej Karpathy、`Brainree` → Braintree、`Max Lechin` → Max Levchin、`FCP` → MCP（⚠️ 语境推定）。

## 概要

本库此前关于"分发与路由"的材料，都来自**应用层或模型层的自述**（[Anton Osika 的多模型路由](20260715-all-in-gelsinger-lovable.md)、[Eiso Kant 的商品化论证](20260722-latent-space-poolside-eiso-kant.md)）。⚠️ **本期是第一份来自中间层本身的材料**——那个把模型交到开发者手里的路由层，回头讲它看到的市场结构。

它最反直觉的一条是：**模型实验室真正的短板不在训练，而在"checkpoint 训完之后什么都没有"**（[00:19:16]–[00:21:16]）。第二条是：**Stripe 收购 OpenRouter 不是支付故事，是安全故事**（[01:19:09]）。

### 本期最该被单独引用的六条

1. ⚠️ **"checkpoint 做完，然后是一片寂静"**（Midha，[00:19:16]–[00:21:16]）：他以早期投资人身份给的观察是**跨实验室一致的**——OpenAI、Anthropic、Black Forest Labs、Mistral 的早期预训练团队，**默认路径都是"checkpoint 好了，发个 API，完事"**。"**你会震惊于他们有多相似。**"他举的最硬的例子：**第一版 Claude 的 checkpoint 其实比发布早一年就在内部做好了**，直到 ChatGPT 出来才决定对外发；而 **Claude 1 的博客里那三个开发者案例，一个是 Discord bot、一个是他太太的创业公司、一个是 Notion，全都是 Anthropic 团队的朋友**——"**这就是当时分发计划的仓促程度。**"
2. ⚠️ **Google 的隐形分发优势**（Midha，[00:21:16]）：DeepMind 训完一个 checkpoint，**按个按钮就能铺到从 Google Docs 到 Android 的所有界面，一夜之间覆盖十亿台设备**。"**这个看不见的基础设施优势大多数人没意识到；在 OpenRouter 出现之前，作为模型实验室你必须自己想清楚这一切。**"
3. ⚠️ **"just a wrapper"是本期两人都要打的靶子**（[00:24:19]–[00:28:23]）：Midha 的反驳不是理念而是工程量——"**你完全不知道，光是能在生产里编排三个 API，OpenRouter 就已经创造了多少战略价值。**"他自陈当时的做法是**放弃教育其他 VC，直接投**，"**一个月后 Matt Murphy 把它 markup 了 10 倍**"。
4. ⚠️ **fusion 为什么 2024 年失败、2026 年成立**（Alex，[01:01:48]–[01:03:51]）：2024 年初的原型叫 **MOM（mixture of models）**，把多个模型的结果用另一个模型融合。失败原因很具体——**当时第一名模型远远领先第二三名，所以融合结果不比最好的那个好**。⚠️ **现在成立的机制性解释**："**RL 基本上扩大了各实验室机器学习研究员的创造力表面积，所以他们能更有效地让不同模型的推理能力分化**"——头部三四个模型**能力接近但仍然"神经发散（neurodivergent）"**，融合才有增量。
5. ⚠️ **token 欺诈的量级与形态**（Alex，[01:10:56]–[01:12:59]）：**上个月拦截的欺诈金额是上上个月的 10 倍**，且类型在分化——**盗刷信用卡、违反条款转售流量、被黑账号、整个公司被攻陷而不自知、以及"失控 agent"（不是黑客，是自己跑飞了、公司并不想要）**。⚠️ **他由此推出一条商业模式预测**：**做网关、卖通用推理的人就是欺诈标靶**；卖**离散任务**的人则风险低得多——所以行业会**从"在推理上加价"转向"按任务/按增强收费，并让客户自带推理"**。
6. ⚠️ **Midha 的"10 万亿 token 流"框架**（[01:16:06]–[01:17:07]）：类比在线支付——**80、90 年代起步，十年内长到一万亿美元以上，期间必须造出全新的支付方案来对付线上欺诈**。"**token 上我们今天大致就在那个位置**"：**未来五年 token 经济到约 5 万亿，十年到 10 万亿"我不会感到意外"**。⚠️ **他的第二层判断是本页认为最该被安全主题页接走的**：今天这些坏行为**由人做**，未来十年**由 AI agent 做**——而实验室很难推理这个问题，"**因为你唯一有的数据是你自己在训练的 agent 怎么跑偏，而那只是互联网上全部坏行为的一小部分**"。

---

## 一、多模型下注：两条不同的路径

来源：[Latent Space 2026-09-25](20260925-latent-space-openrouter-stripe-token-economy.md)

### Alex 的路径：Alpaca 时刻

- **起点**（[00:04:05]–[00:05:05]）：2022 年底 OpenAI 几乎是唯一选项。Llama 出来时"很激动，但你没法跟它聊天，它不是一个有互动性的模型"。**Alpaca 是他看到的第一个把这一步补上的模型——只花了 600 美元**：Stanford 的团队生成一批合成数据、微调 Llama，做出 70 亿（或 130 亿）参数的模型，"**很多情况下你分辨不出 ChatGPT 和 Alpaca 的结果**"。
- ⚠️ **他从中读出的不是模型，是商业模式**（[00:05:05]–[00:06:06]）："**我们第一次有了一种全新的数据变现方式**"——把有价值的数据**压进一个模型里，再当作服务卖出去**，而这个成本还会继续降。
- **由此推出为什么需要市场**（[00:06:06]–[00:07:06]）：只要有一个跑通的爆款 app，**加上一套模仿它的框架**，生态就会立刻长出来，因为"**单一公司做的决定，和更广生态能长出的全部变体之间，有巨大的空隙**"。
- **他对"为什么不是 Hugging Face"的回答**（[00:07:06]）：Hugging Face 最接近，但**没有闭源模型、当时不能直接用模型、也没有"谁在用"的数据**。

### Midha 的路径：Discord 的 250M 用户逼出来的需求

- ⚠️ **最具体的一段一手经历**（[00:12:10]–[00:15:12]）：Discord 拿到 GPT-3.5 早期访问，做两个内部用例——**Clyde（站内好友 bot）和内容审核**。审核撞墙的方式很硬：**post-training 的护栏会直接拒绝他们的 prompt**。他们跟 OpenAI 说"**我们需要权重访问，因为我们要在 2.5 亿月活的规模上做审核，需要模型可靠地照做**"，得到的回答是"**抱歉，我们是闭源公司**"。
  > ⚠️ **"那是我第一次意识到我们需要开源模型，而企业会需要对能力有更多控制。"**
- **为什么护栏在这个用例上必然失灵**（[00:14:11]–[00:15:12]）：**每个 Discord 服务器都是一次小型部署，各有各的社区规范**（他们当时有 5000 多人的外包审核团队在人工执行）。设想是把服务器规范给 LLM 做**上下文内审核**——"**而很多服务器的规范本身就违反 OpenAI 的规则**"。他举的真实案例：**哈利波特粉丝社区因为 post-training 里"任何商标内容都拒绝"的粗暴规则而被模型拒绝服务**。
- ⚠️ **他与 Alex 的分歧是对 scaling law 的读法**（[00:18:14]–[00:19:16]）：Alex 认为"大模型通吃"这个最大反对意见**本身就不太可能**；Midha 的路径**完全相反**——他相信 bitter lesson、认为 scaling 有效，**正因如此才认为 OpenRouter 有价值**："**太好了，现在我们至少有两个 compute scaling 有效的证明点**"，而生态里会有多个模态、多支团队。

---

## 二、中立层为什么难：营销、数据政策与"为什么不是 LMArena"

来源：[Latent Space 2026-09-25](20260925-latent-space-openrouter-stripe-token-economy.md)

- ⚠️ **Alex 对自己业务的比喻，本页认为是全期最凝练的一句**（[00:23:18]–[00:24:19]）：
  > **"用户走进的是一个大黑屋子，所有角落都被遮住，他们摸索着想知道该从桌上抓起哪个东西装进自己公司。这是一种荒谬的工作方式。模型不是那种能把所有特性列在网页上的产品——它们全是黑箱，包括开源权重的那些。所以你需要有人往这个屋子的每个角落打光。而打光的那家公司必须是中立第三方。"**
- **数据政策作为品牌区隔**（[00:49:41]–[00:50:41]）：**OpenRouter 默认看不到你的 prompt 和 completion，要看必须组织主动 opt-in**；他明说这构成与 LMArena 的结构性差异——"**一家公司拿数据去卖，另一家默认就不能**"。
- ⚠️ **Midha 对"为什么 Arena 和 OpenRouter 不是一回事"的第一手澄清**（[00:50:41]–[00:52:43]）：他自陈是 **Arena 的首任 CEO（前 5 个月）**，帮两位创始人从 Berkeley spin out，创始实体叫 **AI Reliability Institute**——**它是一项 eval 服务**，源头是两人在 Berkeley 关于**统计方法学（修正 eval 估计的内在偏差、style control）** 的博士工作。
  > ⚠️ **两者的分野在"最高期望客户"是谁**："**Arena 的最高期望客户始终是实验室里的 post-training 研究员；而 Alex 真正理解并服务的，是拿走研究结果、做出部署到世界上的应用的那个开发者。这是完全不同的问题和完全不同的人。**"
- **他给的佐证细节**（[00:51:42]–[00:52:43]）：他曾想把两边的 prompt 数据合成一个开源数据集，结果发现**Arena 根本没有那类数据——没有 API prompt，没有"开发者想拿模型做什么"**。

---

## 三、增长曲线：模型发布驱动的"摆动"

来源：[Latent Space 2026-09-25](20260925-latent-space-openrouter-stripe-token-economy.md)

- ⚠️ **Mixtral 8x7B 是第一个真实证明点**（[00:44:38]–[00:46:40]）：这是他印象里**第一次有开源权重模型被严肃地称作"世界最好的模型"**；直接后果是**多家 provider 在同一个地方竞价，价格下来约 80%**——"**这是第一个清楚的例子，证明 provider 市场以对开发者有增值的方式跑通了。**"
  - ⚠️ **Midha 补了一条来自 Mistral 创始人本人的反证**（[00:46:40]–[00:47:40]）：他在 NeurIPS 问 Guillaume 感觉如何，对方"**以典型的法国方式说，还行吧，没那么好**"；并且**认为很多人觉得它比 GPT-4 强，部分原因是速度**——MoE 让它极高效、处在帕累托前沿。
  > ⚠️ **"有时候它们更快，你就觉得它们更聪明。"** 这条被 swyx 直接接成"**人作为 router**"——先问快的，不够好再手动升级——而这正是后来 auto router 的雏形。
- ⚠️ **他总结出的"摆动"节律（本页认为最有预测力的一条）**（[01:06:55]–[01:07:55]）：
  1. 模型实验室做出一次前沿创新 →
  2. 用量激增 →
  3. **30 天后用户看账单，"这是怎么回事"** →
  4. **约 3 个月后开源权重模型交付出性价比替代**。
  > **"我们看到这个循环发生过好几次。"**
- **几个节点**：2024 年 5 月之前主力用例是**散文**（coding 还不行）；**Claude Sonnet 3.5（2024 年中）是编码的一次巨大跃迁**，应用生态随之改变（[01:05:54]–[01:06:55]）。**2025 年底 OpenClaw 出现**——新的形态带来**新类型的用户（不只是开发者，还有生产力型/互联网创作者）**，而且架构上有趣：**它会用"心跳"反复调用你选的模型来确认自己还活着**，"**你不会想为一次心跳付很多钱**"，于是 **auto router 对这批用户突然非常有用**（[01:07:55]–[01:08:56]）。
- **规模**（[00:22:16]、[01:04:54]）：**开发者数超过 1000 万**；token 量**每天超过 10 万亿**（对照主持人记忆里"100 万亿"曾是个可笑的里程碑）；**周环比约 9%**。
- ⚠️ **Karpathy 的一句被当作成年礼**（[01:09:56]–[01:10:56]，Alex 转述）：**他说自己不再读 local llama 了，直接看 OpenRouter 的排行榜**。

---

## 四、没做的事：本期关于"聚焦"的部分

来源：[Latent Space 2026-09-25](20260925-latent-space-openrouter-stripe-token-economy.md)

- **做了但没发的原型**（[00:56:46]–[00:58:46]）：**微调即服务**——给它两三个 YouTube 视频，抽转录稿，微调出一个"像视频里的人那样说话"的模型。"**我们真做出来了，然后没人用。**"swyx 的诊断是**这类东西"本质上是加了光环的 RAG bot"，人最后总是想找到那条原始视频**。
- ⚠️ **为什么不做微调/记忆/沙箱这些邻接品（本页认为是给基础设施创业者最实用的一段）**（[00:59:46]–[01:00:47]、[01:08:56]–[01:09:56]）：
  - **记忆、skills、sandbox 这些是开发者自己想架构的东西**——它们是构成好用户体验的关键部分；"**很难找到对所有开发者都成立的记忆层抽象**"。
  - 中立市场的价值恰恰在于**和这些推理商/工具商合作，而不是替代他们**。
- ⚠️ **Midha 用 Anthropic 反向佐证"聚焦"**（[00:53:44]–[00:55:46]）："**人们以为 Anthropic 早期很轻松，因为他们是离开的 GPT-3 那批人。其实非常艰难，公司起步时落后 OpenAI 一百亿美元。**"他说使命从第一天起就是**"负责任地商业化一个 AI 结对程序员"**（seed memo 原话），因而**把当时风头正劲的图像、视频模型全部排除在外**；"**今天你看到结果了——五年内的万亿美元公司。**"⚠️ **他明确说公司历史上有过短暂的"支线实验"**（ChatGPT 起飞时试过通用聊天机器人），但**所有主 eval 从第一天起都是 coding eval、长时程 agentic programming**。

---

## 五、为什么是 Stripe：一个安全故事

来源：[Latent Space 2026-09-25](20260925-latent-space-openrouter-stripe-token-economy.md)

- ⚠️ **Midha 的原型经历（本页最有说服力的一条，因为它早于 LLM）**（[01:14:02]–[01:16:06]）：Midjourney 早期用免费试用把用户推到"10 次生成"这个激活点，**某天他被 David Holtz 连打三个未接来电——一夜之间涌入大量新用户**，查 IP 地理位置后发现**有人在中国转售 Midjourney 的免费试用额度**。"**据我所知 Midjourney 从那以后再没开过免费试用，因为在信任与安全上这不是个容易解决的问题。**"⚠️ **当时 Midjourney 的收入运行率还不到 3 亿美元**——他强调的正是"**在这么小的规模上就已经有这么激进的滥用**"。
- **他对 Stripe 的定性**（[01:18:08]–[01:19:09]）：Stripe 十年前的推销是**把欺诈成本作为获客成本先吞下去，让开发者五行代码五分钟开始收款，再把数据攒起来**；五年后推出 Stripe Radar。
  > ⚠️ **"Stripe 今天其实是一家安全公司。人们以为它是支付公司。不是——今天有很多更便宜的支付通道，Stripe 之所以还是主导者，是因为它多年建起来的极强欺诈检测。"**
- ⚠️ **他要立的一般规律**（[01:19:09]）："**每一次有大量价值在世界范围内被streaming，你就需要新的保护与安全基础设施，把坏人挡在外面、让好人的交易飞快完成。**"由此"**Stripe 与 OpenRouter 这件事，从我的角度看是一个关于互联网生态、关于前沿 AI 生态的安全故事**"。
- ⚠️ **agentic fraud 这条预测的完整形态**（[01:19:09]–[01:20:09]）：需要的是**能横跨生态（不同模型实验室、不同 post-train 部署、不同开发者）看到全部 agent 坏行为的"新警长"**，把这些数据合起来**给整个 token 经济建一面盾**。
  > **"如果人们就是不信任 token，我们可能永远到不了那 10 万亿。"**
- **交易之后的具体承诺**（[01:21:10]）：**OpenRouter 品牌、产品、路线图、名字全部保留**；未来 6 个月"**基本上就是我们独立时会做的事，只是全部更快**"。

---

## 相关页面

- 人物：[Latent Space 主播](../people/latent-space-hosts.md) · [Alex Atallah & Anjney Midha](../people/openrouter-atallah-midha.md)
- 主题：[AI 商业化与价值捕获](../topics/ai-business-and-value-capture.md) · [LLM 安全](../topics/llm-security.md) · [开源基础设施](../topics/open-source-infrastructure.md) · [评估与 Benchmark](../topics/evaluation-and-benchmarks.md) · [AI 实验室文化](../topics/ai-lab-culture.md)
- 相关视频：[Anton Osika（Lovable）：多模型路由 + post-training](20260715-all-in-gelsinger-lovable.md) · [Eiso Kant：开源商品化论证](20260722-latent-space-poolside-eiso-kant.md) · [Peter Steinberger：OpenClaw](20260212-lex-openclaw-steinberger.md) · [All-In 第 290 期：开源 token 份额翻转](20260926-all-in-anthropic-ipo-open-source-flip.md)
