# Alex Lieberman & CJ Hess（Tenex）

- **Alex Lieberman** — **Tenex 联合创始人**（另一位联创 Armand，技术出身）。此前联合创办 Morning Brew。
- **CJ Hess** — Tenex **special projects lead**、**公司第一号员工**；软件工程师出身，加入前自己做工程咨询。
- **Tenex** — 成立约 **18 个月**（截至 2026-10），定位 **"applied AI partner"**：帮大企业从 **AI absent 走到 AI native**。**75 人、总部纽约**，**90% 是工程师或 AI strategist（技术顾问）**；客户**一半 Fortune 2000、一半年收入 1–5 亿美元的中型公司**。起步形态是"AI 驱动的开发外包"，现在卖的是 **AI transformation as a service**。⚠️ 以上全为自述。
- **本库收录**：[2026-10-21 Latent Space（AI Engineer NYC 现场）](../videos/20261021-latent-space-tenex-enterprise-agent-5-percent.md)

> ⚠️⚠️ **读这一页时必须带着的利益相关**：两人卖的就是"企业 AI 转型服务"，而他们给出的所有数字都在论证**企业需要这种服务**。本库全部记为**一方自述**。

## 核心主张

来源：[Latent Space 2026-10-21](../videos/20261021-latent-space-tenex-enterprise-agent-5-percent.md)（本页以下全部时间戳均出自这一期）

### 企业采用 AI 的四级漏斗，最后一级断崖到 5%

Alex 把企业采用描述成一场有里程碑的赛跑，并给出他们接触的约 100 家企业里各级占比：**铺开通用 LLM 90% → 培训与赋能 60% → 给工程组织铺开 coding agent 约 50% → 让 agent 在生产环境做"非写软件"的工作约 5%**（[视频页](../videos/20261021-latent-space-tenex-enterprise-agent-5-percent.md) [00:19:51]–[00:20:52]）。

两处口径上的细节：**第三级多数人猜 70–80%、实际接近 50%，而且"没铺开的那一半里，他们在用的东西更接近于没有 coding agent"**；**第四级的表述是"员工数过千的企业里，大多数没有任何一个在生产环境做非软件工作的 agent"**（同上 [00:20:52]–[00:21:52]）。

✅ **本库的归纳：前三级都是发工具，第四级才是改流程，漏斗恰好在这里掉了一个数量级。** 详细保留意见见视频页。

### "你没法自动化一个并不存在的流程"

CJ 对第四级为什么卡住给的机制性解释：**四十个人做同一职能、四十种做法**，这种状态下造不出后台 agent；**而且没有标准化就无法建 eval**——"agent 不可能知道自己做得对不对"。所以 Tenex 的建议顺序是**先在组织内把流程建起来，再谈交给 agent**（[视频页](../videos/20261021-latent-space-tenex-enterprise-agent-5-percent.md) [00:22:52]–[00:23:52]）。

过渡形态是**让 agent 把工作"浮"给人、人复核后打回去**，人逐步变成 agent manager，"我们正处在临界点上"（同上 [00:23:52]）。

### 按 story point 而非工时付薪

- 基本主张（Alex）：**"AI 本质上是对一个人的智力与工作伦理加的杠杆"**，所以**收入能力的方差会空前变大**（[视频页](../videos/20261021-latent-space-tenex-enterprise-agent-5-percent.md) [00:02:29]–[00:03:29]）。
- **18 个月后的实测离散度是约 4 倍，不是 10 倍**——"不是 10 倍。那是梦想"（同上 [00:04:30]）。
- **两个事前担心的问题（虚报点数、交烂代码）都没发生**，归因于 **AI strategist 的激励被刻意设成与工程师相反**（考核客户留存与增长）（同上 [00:05:32]）。⚠️ 制衡设计声明，无检出数据。
- ⚠️⚠️ **真正的难点在"不写代码的时间"怎么计价**（架构、见客户）；⚠️ **而随着模型变强，这部分正在变多**——CJ 说现在"模型给对上下文基本能到 90%"，价值落在"听客户倒完脑子再喂给模型"上（同上 [00:05:32]、[00:06:32]）。
- ⚠️ **单位购买力没解决**：主持人问 story point 通胀还是通缩，Alex 答"理论上应该通缩"，CJ 答"我不知道"；他们至少每季度重新校准一次估点标准（同上 [00:10:39]）。

🔗 **与 [Akshay Nathan](akshay-nathan.md)（OpenAI）在 2026-07 的对照**：后者明说 **story point 这类旧代理指标已不再强相关于目标达成**。本库在视频页并置了两侧，并指出"计价单位"与"目标达成代理"是两种用法——⚠️ **但 Tenex 用"人均月 story point"衡量工具是否奏效时，正好落在被判失效的那种用法上**。

### 看空垂直 AI（与主持人当面分歧）

Alex 看空垂直行业 / 职能专用 AI，理由是**企业内部 nuance 与惯性巨大**、**买方期待一对一方案（这正是每家软件公司都在搭 FDE 团队的原因）**，由此发问**这些公司还能不能以软件毛利率经营**，以及**为什么前沿模型不会直接吞掉它们**（[视频页](../videos/20261021-latent-space-tenex-enterprise-agent-5-percent.md) [00:23:52]–[00:25:52]）。

swyx 当面回"**到目前为止你是错的**"，举 Harvey、OpenEvidence，护城河是数据、affordance/UI、以及 **Bloomberg 式的切换成本与网络**（同上 [00:25:52]–[00:27:55]）。

CJ 的划分本库认为比双方原始立场更可用：**把 agent 本身当产品的垂直方案，除非有合规/数据护城河否则会越来越难；而"改变了流程、再在流程之上放一个 agent"的产品仍会成功**（同上 [00:28:56]）。⚠️ **本库裁决：Alex 问的是毛利率，swyx 答的是留存，两者可同时为真。**

### 企业第二大诉求：权限与 RBAC

**每个员工都有 Claude 或 Codex 之后，"对 CIO 和 CISO 来说已经变成一场彻头彻尾的噩梦"**——缺一个管"你能读什么"的网关与控制面板。Tenex 先做定制、现已产品化成自己的网关（[视频页](../videos/20261021-latent-space-tenex-enterprise-agent-5-percent.md) [00:21:52]–[00:22:52]）。⚠️ 他在描述自己在卖的产品所对应的痛点。详见 [LLM 安全](../topics/llm-security.md)。

### 自建 vs 买：成本的重新定义

对 swyx 的 [Kill My SaaS 实验](../videos/20261013-latent-space-kill-my-saas-43k-event-software.md)（4 万美元/年的工具用约 1000 美元替掉），Alex 的回应：**越往上游走，拆掉重建越难**；他**不同意"Salesforce / SAP 真的有风险"**，因为替换搞砸的代价是几亿到几十亿，买方必然极度风险厌恶（[视频页](../videos/20261021-latent-space-tenex-enterprise-agent-5-percent.md) [00:30:59]–[00:32:06]）。

✅ **最该保存的一条**：**"软件的妙处不只是你得到的效用，还有当它不属于你的核心时，那些你不必操心的维护与改进的麻烦。"** 判据因此是**这块蛋糕是否大到值得长期背上一份非核心的认知负荷**（同上 [00:33:07]–[00:34:08]）。

### 就业：一处主动的降温

⚠️⚠️ Alex：**"当人们说 AI 会替掉所有人们不喜欢做的工作，我觉得那有点是在给'会有很多人失业'这件事找安慰（cope）——因为很多人根本没有喜不喜欢一份工作的余裕，他们做一份工作是为了挣钱。"**（[视频页](../videos/20261021-latent-space-tenex-enterprise-agent-5-percent.md) [00:37:09]–[00:38:11]）

⚠️ 同时他把再技能化的责任分了一半给个人（"人要有能动性自问自己的可替代性"）。**本库标注张力：刚说完很多人没有挑工作的余裕，而没有余裕恰恰意味着也没有再培训的余裕。** 详见 [AI 与就业](../topics/ai-and-jobs.md)。

## 工程实践（CJ 侧）

- **"meta harness"**：仓库内一套结构化文档 + 外面一层 CLI，驱动计划、可视化、客户 readout。**agent 的决策与过程日志全部 check 进 Git**，"它永远不在某个人的脑子里，永远在仓库里"；他明确站在"**还是需要文档**"一侧，反对"代码即代码库的记忆"（[视频页](../videos/20261021-latent-space-tenex-enterprise-agent-5-percent.md) [00:07:35]–[00:08:37]）。
- ⚠️⚠️ **"随着模型变好，我们反而削减了结构上的强制"**（同上 [00:07:35]）——与"给模型更多脚手架"的直觉相反，本库记为可对照的实践走向。
- **模型选择**：压倒性 **Opus 5.5**；**Fable"我自己不怎么用，现在不少人都在默认不用它"**；codex 用于偏 computer use 的任务；⚠️ **最好的工作流是"Opus 写、codex 审、来回过"**。CJ 自称 **AMP maxing**（同上 [00:11:39]–[00:13:44]）。
- **成本**：token 支出 : 人力支出约 **1:1 到 2:1**；⚠️⚠️ **"今天一个人靠 token maxing 把公司成本搞垮，比六到八个月前难多了"**——该担心的时点已经过去（同上 [00:14:47]、[00:17:49]）。

## 纽约

**纽约也有"活在未来"的泡泡，只是比旧金山小**；而他的立论是**纽约在 AI 池子里更小、在商业价值池子里一样大甚至更大**，所以 **"我在纽约做 AI 的理由，是把旧金山的人带过来见他们的客户、顺便接受一次现实检验"**，他称之为一种套利（[视频页](../videos/20261021-latent-space-tenex-enterprise-agent-5-percent.md) [00:39:12]–[00:41:16]）。

## 相关

- [Latent Space 主播](latent-space-hosts.md) · [Akshay Nathan](akshay-nathan.md) · [Jean-Denis（Town）](town-jean-denis.md) · [Dylan Field](dylan-field.md) · [Legora Max](legora-max.md)
- [AI 商业化与价值捕获](../topics/ai-business-and-value-capture.md) · [在实践中使用 LLM](../topics/using-llms-in-practice.md) · [AI 与就业](../topics/ai-and-jobs.md) · [评估与 Benchmark](../topics/evaluation-and-benchmarks.md) · [LLM 安全](../topics/llm-security.md)
