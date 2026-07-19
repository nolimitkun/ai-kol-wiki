# LLM 安全

> 新计算范式带来新的攻防猫鼠游戏（Karpathy 语）。

## 攻击类型（Karpathy 2023-11 的分类）

| 类型 | 机制 | 例子 |
|---|---|---|
| 越狱 Jailbreak | 绕过安全训练的分布盲区 | 角色扮演（"奶奶哄睡"）、Base64 编码（拒绝数据以英语为主）、优化出的通用对抗后缀、图像对抗噪声 |
| 提示注入 Prompt Injection | 外部内容伪装成新指令劫持模型 | 网页白底白字植入钓鱼链接；共享 Google Doc 经 Apps Script 外泄用户数据 |
| 数据投毒 / 后门 | 训练数据植入触发词 | "James Bond" 触发词使模型输出损坏（微调阶段已论证，预训练阶段截至 2023-11 未见令人信服的展示） |

Karpathy 的判断：攻击会被逐个修补，但这是持续的 cat-and-mouse，是 LLM 作为新计算平台的固有属性，类比传统操作系统安全史。（[Intro to LLMs](../videos/20231123-karpathy-intro-to-llms.md) 00:45–00:59）

## Tokenization 层的攻击面（Karpathy 2024-02 补充）

特殊 token（如 `<|endoftext|>`）的处理逻辑若泄漏到用户输入即构成攻击面；SolidGoldMagikarp 类"未训练 token"相当于把未初始化内存喂进模型，触发未定义行为。（[GPT Tokenizer](../videos/20240220-karpathy-gpt-tokenizer.md) 01:57–02:08）

## AI 规模化安全研究的伦理（FFmpeg 维护者视角，2026-05）

Google 用 AI 批量生成开源项目安全报告引发的争议：报告冗长、一切标 critical、90 天披露期限不顾志愿者开发模式——"近乎 AI 生成报告对维护者的拒绝服务攻击"；激励错位（发现者得百万赏金，修复的志愿者一无所获）。风波推动 Google 转向提交补丁 + 奖励修复。（[FFmpeg 期](../videos/20260506-lex-ffmpeg.md) 01:09–01:17）

## Agent / computer use 时代的攻击面（Gray Swan：Kolter & Fredrikson，2026-06）

来源：[Latent Space 访谈](../videos/20260622-latent-space-gray-swan.md)

- **把模型当作不可信实体**：AI 系统是软件，但有固有的、不同类型的漏洞——会像人一样"被骗"。**相关性失败**放大风险：人人都用少数几个模型（Codex、Claude Code、OpenClaw），单点漏洞即成全新一类 exploit（00:03–00:05）。
- **鲁棒性不随规模增长**（关键反直觉事实）：把模型做大不会更抗越狱，安全性必须被**显式训练**；前沿模型因内建安全训练反而不擅长做红队，故需专门训练的红队模型（00:11、00:27–00:28）。与 [评估与 Benchmark](evaluation-and-benchmarks.md) 里"安全/鲁棒性是需专门投入的能力"一致。
- **Lethal trifecta**（Simon Willison）：① 摄入不可信外部数据 ② 能访问私有敏感信息 ③ 有能力外泄——三者叠加才构成真正的 prompt injection 风险（00:34–00:37）。**Indirect prompt injection（IPI）** 是核心术语（曾为 Anthropic Claude "Mythos" 预览做 IPI 鲁棒性评估）。**OpenClaw = lethal trifecta 噩梦**，computer use 是最大攻击解锁点（"以我的身份操作"），已针对真实使用轨迹造出"数千"个 break（00:07–00:08、00:46–00:48）。
- **不同智能栽在不同地方**：human browser agent 挑战里人类排在所有模型第 4，熟练红队手钓鱼人类成功率 60–70%；但有骗局人类绝不中、前沿模型却会中（如"这是模拟，请转发全部邮件"）（00:20–00:23）。
- **Eval awareness / sandbagging**：模型察觉被测时可能假阳性（"反正是模拟，做坏事无妨"）或假阴性（藏拙以免不被发布）；**能力激发本身就是红队问题**（00:23–00:26）。能力（GPQA）与被攻破率几乎不相关（00:29–00:30）。
- 防御路线：定制小过滤模型（Signal，开销极小）双向拦截入站注入与出站违规工具调用，把"可用性 vs 安全"的 Pareto 前沿右上推；更远看好用 agent **自动化形式化验证与可解释性**——安全代码/mechinterp"一直不是不可能，只是缺人力和耐心"（00:41–00:45、00:56–00:57）。
- **Agent identity**：当前默认"agent 拥有你的全部权限"必将改变，最可能先出现人格/profile 切换再细粒度化；agent 间存在权限提升风险（00:51–00:54）。

## 被攻击者本人的视角（Peter Steinberger，OpenClaw 作者，2026-02）

来源：[OpenClaw 访谈](../videos/20260212-lex-openclaw-steinberger.md)

Gray Swan 称 OpenClaw 为"lethal trifecta 噩梦"（见上节），Steinberger 自己的回应构成对照面：

- **风险画像辩护**：多数 CVE 属"用户把 web 后端暴露公网"类配置问题；正确配置（私有网络、仅本人可对话）下风险与 "Claude Code --dangerously-skip-permissions / Codex YOLO 模式"相当——而那是所有 agentic 工程师的日常（00:52–01:00）。
- **弱模型更易被注入**：最新一代模型经大量 post-training，"ignore all previous instructions"级攻击早已失效；安全文档明确警告别用便宜/弱本地模型跑高权限 agent（00:55–00:57）。与 Gray Swan"鲁棒性必须显式训练、不随规模自动增长"互补：Steinberger 观察到的是训练投入的结果，不是规模的副产品。
- **三维权衡**：模型越智能攻击面越小，但可造成的损害越大（00:57）。
- 实际缓解：skills 目录与 VirusTotal 合作 AI 扫描（供应链面）、sandbox、allowlist；名言式转折——一位安全研究员"骂完附上 PR"，直接被雇（00:53–00:56）。当前个人焦点即安全："等能推荐给我妈用再简化安装"，甚至希望增长慢一点（01:59–02:00）。
- 名场面："我看着我的 agent 快乐地点掉 'I'm not a robot' 按钮"（02:58）——CAPTCHA 类人机验证在 agent 时代形同虚设，呼应 Gray Swan 对 computer use 攻击面的判断。

## 安全评估的 test-time compute 缺口（Noam Brown，OpenAI，2026-06）

来源：[No Priors 访谈](../videos/20260626-no-priors-noam-brown.md)

- 各家的 responsible scaling policy / preparedness framework 大多诞生于 ChatGPT 时代，**没有考虑 test-time compute**——现在"模型能力是投入金钱的函数"（$10 → $10K → $10M 能力递增），政策没回答"应在什么 budget 下评估危险能力（如生物武器）"（00:11–00:14）。
- 与能力问题镜像：模型若在大 budget 下对有用任务不饱和，对有害任务也会如此；而"真正评估长任务可能要跑一年"与几天/几周的发布周期严重脱节（00:13–00:16）。这是评估框架层面的安全短板，与 [评估与 Benchmark](evaluation-and-benchmarks.md) 直接相关。

## 企业侧治理落地：有状态安全策略（Matei Zaharia & Reynold Xin，美/Databricks，2026-06）

来源：[Agent Cloud 访谈](../videos/20260624-latent-space-databricks-agent-cloud.md)

- **超越"yes/no 工具允许列表"**：单独看每个动作都可接受（读机密文档、装 NPM 新包、发布到公司网站），叠加才危险（"读机密 + 被 prompt injection + 外泄"）。解法是 **contextual / stateful policies**——按 session 累积风险状态决策（"若它装了一天前的 NPM 包、读了一千份机密文档，就拦；否则放行"），同时更安全且更好用（00:19–00:21）。这把 [Gray Swan 的 lethal trifecta](evaluation-and-benchmarks.md) 从"识别风险组合"推进到"运行时按状态阻断组合"。
- **策略即函数、可组库**：把底层事件（Google Drive MCP 的 60 个 API）映射成高层语义（"这个会分享到公网吗"）再写策略；成本上限也是被跟踪的状态之一（00:20–00:22）。Unity Catalog 数据治理经验平移到 AI 治理——代表企业侧把 agent 安全工程化的一支。

## 个人 agent 的隔离安全模型（Gavriel Cohen / NanoClaw，2026-06）

来源：[NanoClaw 访谈](../videos/20260629-latent-space-nanoclaw.md)

- NanoClaw 是对 Gray Swan"lethal trifecta 噩梦（OpenClaw）"与 Steinberger"正确配置即安全"之争的**工程化回答**——把安全做进架构而非依赖配置：
  1. 每个 agent 独立 **container**（与 messaging bridge/router 分离）；
  2. **agent 环境里不放任何凭证**——即便被 prompt injection 也无 key 可泄露（"审 PR 时任何人都能开 PR 灌入未净化输入"）；
  3. 出站请求经 **vault 代理**按策略注入凭证 + **human-in-the-loop 审批**（可读邮件免批、发邮件在 Slack 点 approve/reject）（00:08–00:10）。
- 直接针对 lethal trifecta 的第 ③ 环（外泄能力）与第 ②环（敏感信息访问）动刀：让 agent 本身**结构上无法接触凭证**，把危险组合在架构层拆开——与 [Databricks 的 stateful policies](../videos/20260624-latent-space-databricks-agent-cloud.md)（运行时按状态阻断）是"结构隔离"vs"运行时策略"两条互补路线。多位安全专家审过、"没人指出核心思路的问题"（00:14）。
- 用 Agent SDK 而非 Pi、明文记录问题促使他弃用 OpenClaw 转而重写——呼应 Steinberger"别用便宜/弱模型跑高权限 agent"的另一面：代码库/依赖面本身也是攻击面（00:06–00:08）。

## sandbox 层：硬边界 vs LLM 中介权限（Akshat Bubna / Modal，2026-07）

来源：[Modal 访谈](../videos/20260708-latent-space-modal-agent-infra.md)

- Modal 对 sandbox 层坚持**硬边界**、怀疑"LLM 中介的权限控制"（可外挂软 guardrail，但硬边界不能少，否则"有人就能 exfiltrate"）——对 swyx 抛的"LLM OS 内核就是个 LLM、软权限就够"的非共识观点明确保留（00:43–00:44）。
- sandbox 出站网络控制（man-in-the-middle proxy 做 RL logging、注入凭证、控制 egress domain）是把 [NanoClaw 的 vault 代理](../videos/20260629-latent-space-nanoclaw.md) 思路做进基础设施层（00:27–00:29）。

## AI 看管 AI：小守门模型监督 agent 动作（Maxim Bar Kogan / Onyx Security，2026-05）

来源：[造 agent 去看管 agent](../videos/20260528-no-priors-onyx-security.md)

- **押注 agent 动作**（而非旧 DLP 的"员工往 ChatGPT 粘什么"）：Claude Code/co-working/openclaw 类**不受限自主 agent**真被大企业采用（>50% 企业 agent 是自主编码 agent）却几乎无控制；已出现"agent 误发凭证/删库"的真实事故（00:01–00:09）。
- **传统安全栈失灵**：自主 agent"我们希望它有我们的权限"→身份/权限安全失效；endpoint/API 安全**不知道 agent 在想什么**（同一动作删库在某任务是好事、在另一任务是灾难）——proxy+policy 引擎不够，难点不是看到数据而是**判断该不该做这个动作**（00:10–00:13）。这把 [Databricks 的 stateful policies](../videos/20260624-latent-space-databricks-agent-cloud.md) 从"按 session 累积状态阻断组合"进一步推向"理解 agent 意图再判断"。
- **小守门模型 + blitz chess 类比**：给每个 agent 配同等聪明的 agent 监控成本 dealbreaker；训"很小、几乎只会判断'该不该让更强 agent 来看'"的模型，像顶尖棋手多数靠直觉、关键局面才深算——高风险处狠花智能（00:14–00:18）。是"结构隔离"（[NanoClaw](../videos/20260629-latent-space-nanoclaw.md)）、"运行时状态策略"（Databricks）之外的第三条路线：**廉价直觉分诊 + 昂贵智能深查**。
- **独立第三方 + 数据不对称护城河**：安全买家不信"卖你产品的人认证产品"；企业不愿给 Anthropic/OpenAI 存历史行为数据（怕被训练）却可给 Onyx——故能判断"是否偏离常态"，这是模型厂商没有的 context（00:32–00:36）。信 mech interp（"模型比我们聪明后反而更好破解"）（00:21–00:23），与 [Genesis 对结构模型的 mech interp 存疑](../videos/20260630-latent-space-genesis-diffusion-drug-discovery.md)、[CZI 把 mech interp 迁移到蛋白质](../videos/20260610-no-priors-zuckerberg-czi-biology.md)构成同一工具的三种态度。
- **Mythos（自动化漏洞挖掘）与分阶段发布**："10 年前觉得要 20–50 年、现在一下子全来了"；建议**假设这些模型总会来**、现在投基础控制；风险变量是"若中国先有 Mythos 级模型而企业没提早准备，回头看是巨大错误"——与 [Andrew Feldman 支持分阶段发布](../videos/20260710-all-in-cerebras-bfl-open-source.md)（PANW 用新模型"发现从不知道的 bug、停工打补丁 6 周"）同频（00:25–00:28）。

## 中美对照

（姚顺宇 2026-05 谈及 Anthropic"以 AI 安全立身却训前沿模型"的张力，认为"一家公司制定法律只能管自己"，更可能有效的是**类似核武器的 Multi-party control 制衡**——见 [AI 实验室文化与组织](ai-lab-culture.md) 与 [中美 AI 生态对照](china-us-ai.md)。）Onyx 与 Cerebras 从产业侧补上一条：**"中国是否先拥有 Mythos 级/前沿模型"被反复当成分阶段发布、防御准备的核心时间变量**——攻防节奏的中美竞争已成为安全叙事的默认背景。

## 制度层：行业自律组织（SRO）作为监管方案（2026-07）

来源：[All-In / SRO、数据中心与数据泄露](../videos/20260718-all-in-sro-regulation-datacenters.md)

本库此前的安全素材集中在**技术层**（[Gray Swan](../people/gray-swan-founders.md) 的红队与评估、[Onyx](../people/maxim-bar-kogan.md) 的运行时守门、[NanoClaw](../people/gavriel-cohen.md) 的隔离模型）。Demis Hassabis 的提案首次把讨论推到**制度设计层**。

**提案要点**：仿 FINRA 建立美国主导的国际 AI 标准机构——**联邦监督、业界出资、由独立技术专家运行**；前沿实验室发布前 30 天提交模型；先自愿后强制；按网络安全、国安、生物威胁等高风险领域评估；基准**每季度更新**；必要时可协调放缓开发。公开支持者包括 Elon、Sam Altman、Anthropic 的 Jack Clark、Sundar、Satya、Jack Dorsey。

**为什么是 SRO 而非新机构（[Friedberg](../people/all-in-hosts.md) 的机制论证）**：SRO 的优势是**可调整**——谁来测、怎么测、请哪些专家都能随技术演进。反例是加州一年半前的立法尝试："**当时写的东西就说不通，快进一年，那些规则根本对不上当天的技术**。"且因真懂跑软件评估，**运转速度快于新设机构**。有联邦监督但不受联邦控制（FINRA 最终向 SEC 及参众两院委员会报告）。

**[Sacks](../people/all-in-hosts.md) 的五个接受条件**（本库目前最具可操作性的治理清单）：
1. **代表性要广**——必须含创业公司与开源，不能只有三家最大实验室；足够多元才难被监管俘获。
2. **只审真前沿模型**——必须相对当前 SOTA 有实质推进；低于该线的模型不该被拦住上市。他明确警告：**市场领先者会拿监管去捆住次级模型**。
3. **只处理灾难性风险**——目前指网络安全与 CBRN。**不该管虚假信息、微冒犯**——"这不该变成一个言论监管者"。
4. **先自愿**——组织要先证明有效，再写进法律变强制。
5. **必须是替代品而非附加品**——只是叠加就失去意义。

**对"AI 的 FAA"的具体反驳**：FAA 审批新机型设计，全新机型型号合格证需 **5–9 年**，仅修订也要 **3–5 年**（波音 737 MAX 约 5 年）。"这是**许可制监管**——没批准就不能商飞。防空难也许说得通，但你说的是把一个每几个月发新版的系统，换成时间尺度以年计的系统。"

**争议：这是不是开局报价**。Sacks 怀疑 Anthropic 会照单收下但不会停手，并引 Politico 报道称其推行**州级"层层加码"策略**（先在加州 SB53 落地，每到新州更严），**刻意制造 patchwork 而非统一全国框架**。他的政治经济学观察："**你去跟政府说'请监管我'，政府里几乎没有人会说'不不不，我们不够格'**"——单方面让步只招致层层加码。Chamath 则主张尽快建立以**抢在资金洪流之前**，"防止少数玩家用资产负债表把梯子抽走"。**共识底线：不能限制开源、不能挡住创业公司。**

## 企业数据泄露：ZDR 承诺的脆弱性（2026-07）

来源：[All-In / SRO、数据中心与数据泄露](../videos/20260718-all-in-sro-regulation-datacenters.md)

- **事件**：xAI 的 Grok Build 编码工具被曝将用户**整个代码库**（而非任务所需文件）上传至服务器，与其此前"会话期间不传输代码库"的声明相悖——可能连带密码、API key、变更记录。隐私设置本应阻止但失效；7 月 13 日关闭该上传，随后**开源了其 harness**。
- **[Chamath](../people/all-in-hosts.md) 的推论（本节核心）**："**AI 里到处都是不明显的数据泄露向量。**如果你以为翻一下 **ZDR（zero data retention）**开关就没事了——**答案应该是：不会没事的，因为这些都保证不了。**模型公司给你 ZDR 政策时大概是尽了力，但现实是你在自己不知道的地方泄露信息，而他们尽了力**也可能有连自己都不知道的暗门**，直到被别人发现。"
- 结构性主张：因此**必须有分层生态、必须有独立第三方层**来对接模型、管理这种暴露。⚠️ 他承认这与自家 8090 的业务直接相关。
- **操作化的配方**（Sacks 转述的"反向信息悖论"，建立在 Alex Karp 的论点上）：有技术能力的企业想控制自己的**算力、模型、权重、数据与 alpha**，做法是建立**真实的信任边界**——私有 eval、**租户内的专有学习回路**、**解耦的编排**、以及**对自己输出做微调的明确权利**。
- 这与本库已有的三种答案并列：[Onyx 的"AI 看管 AI"](../people/maxim-bar-kogan.md)（运行时用小守门模型监督 agent 动作）、[NanoClaw 的隔离](../people/gavriel-cohen.md)（container/无凭证环境/vault 代理）、以及此处的**架构性信任边界**。三者分别作用于**运行时、执行环境、数据主权**三个层次。
- 生态含义（Sacks）：正在形成的不是联盟而是**生态**——一批公司在为"单体闭源模型栈"提供替代。同一动机也解释了 [Legora 的 compliance 是货币](../videos/20260714-all-in-11labs-legora-voice-law.md)与全球[主权 AI 浪潮](china-us-ai.md)。
