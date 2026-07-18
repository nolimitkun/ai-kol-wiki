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
