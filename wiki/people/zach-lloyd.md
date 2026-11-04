# Zach Lloyd

**Warp.dev 创始人兼 CEO。** 产品从终端（Warp 终端）转向 **cloud software factory 平台**（Warp Factories）。本库自 2026-11-03 起有他的材料。

来源：[Latent Space × Warp.dev（2026-11-03）](../videos/20261103-latent-space-warp-software-factory-80-to-15-dollars-per-pr.md)

> ⚠️ **立场**：**他是 Warp 的 CEO，本页全部数字（成本、吞吐、正确率、客户规模）均为自述，无第三方来源，口径由他自定。** ⚠️ **该期为 AIE code 会议的预热内容，他本人将在该会做 keynote。**

---

## 他的核心框架：software factory 是一个可指认的对象，不是一种做事风气

- **定义**（[00:02:02]）：**"一个云上的 agentic 系统，你在里面定义各种 agent 在为你的团队或产品构建软件这件事上分别扮演什么角色，而这个系统里有一定程度的自治性。"**
- ⚠️⚠️ **而他真正在争的是词义**：他明确反对把它当成"我们大量用 agent 发软件，就叫内部 software factory"，主张**"用代码定义你的 factory"**、**"你应该能在某个时间点把它跑起来、然后测它表现得怎么样"**（[00:03:03]）。
- **一个 product surface 对应一个 factory**；factory 绑一组 repo / skill / MCP + 一条 workflow，载体是 YAML（[00:04:03]–[00:05:03]）。
- ⚠️ **适用人群他自己收窄过**：不是日常工程师，而是**工程经理 / CTO / 平台团队（DevX 团队）**（[00:12:07]）。

## 他最具迁移价值的一条主张：从氛围到测量

> **"这个世界需要的是把理解 coding agent 这件事从氛围的领域里拿出来，真正进到测量的领域里。"**（[00:13:07]）

- **他指认的对手是 Twitter 式的 harness 比较**（"是 Pi 还是 Claude Code 还是 Cursor"）。
- ⚠️ **而他给的替代方案是三件设施**：**中央化的 agent trace**、**常态挂着的 LLM-as-judge scorer**、**在自己历史运行记录上重放的 benchmark（同时变 model 与变 harness）**。详见视频页第二至四节。
- ⚠️⚠️ **本库标注这条主张在逻辑上不依赖他的数字，但他用来支持它的全部证据都是自报口径**（见下）。

## 他给的那组数字（自述，本库记为立场陈述）

- **每个 PR 的成本：约 80 美元 → 15–20 美元**（[00:23:16]–[00:24:16]）。⚠️⚠️ **而本库认为值得记的是归因——三条原因全是配置性的，不是模型能力性的**：**"用了 Opus 而本来不该用"**、**triage agent 挂在一个高功率模型上**、**"子 agent 开得太多，相比之下本该用更少的 agent"**。
- **过去一个月 PR 吞吐 +40%，而 revert 率"没有上升"**。⚠️ **该指标的定义、窗口与基数本期均未给出。**
- **他们 60% 的工作从 Slack 开始**（[00:25:17]）。

## ⚠️⚠️ 他对 coding agent 这门生意的判断：由采购价差推出的产品边界

（[00:30:23]–[00:32:24]）**本库认为这是他最有价值的一条自述，因为它把一条采购层的价差推到了一整个品类的存亡上。**

- **他看到的现场事实**：小公司**"在十七个不同的订阅之间轮着用"**；⚠️ **而合规性他明确说自己不知道**：**"你没法想象那被允许。但我——说实话，我就是真的不知道。"**（价差"五到五十倍"由 swyx 给出）
- ⚠️⚠️ **由此而来的结论**：
  > **"从生意角度讲，这是我不想待在纯 coding agent 这门生意里的原因之一。你没法在一个贵这么多钱的东西上面做出一个有竞争力的 coding agent。这就是现实。"**
- **他的自我定位**：**"我们其实不是在卖一个 token 转售产品。我们卖的基本上是一个 coding agent 优化平台、coding agent 生产力平台。"**
- ⚠️ **他对 Cursor 的解读（本库记为他的推断、非事实）**：**"他们有一个完美的退出，变成了一家模型实验室，因为我觉得他们完全看清了这件事的经济账。"**

## 他画出的适配区间（两头都封闭）

- **下限 5–10 个工程师**；**"如果你就几个人，说实话这是过度设计"**（[00:26:19]）。
- **甜区 10–100 个工程师、快速成长**，条件是工具组合常见（他称之为 "happy stack"：Slack + Linear/Jira）。
- ⚠️ **上限他点了名**：**基础设施非常定制、有大型内部开发团队的公司（他举 Uber、Ramp）不是合适客户。**

## ⚠️ 他预告但未展开的岗位二分

- **product engineering vs factory engineering**（[00:33:24]）：**"你作为一个工程师要怎么练出对的技能，去工程化那个造软件的系统，而不是直接去造软件？"**
- ⚠️ **这是一条尚未兑现的岗位预测**，本库记下它的可检验形态：**平台/DevX 团队里是否出现以调优 agent 工作流为全职的职位。** 见 [AI 与就业](../topics/ai-and-jobs.md)。

## ⚠️⚠️ 本库对他的两处保留

1. ⚠️ **被问"最强的 steelman 批评是什么"时，他把问题换成了"它不适合谁"**（规模 + 定制基建），而 swyx 两次试图拉回都没成功（[00:29:23]–[00:30:23]）。✅ **本库判这是市场分层、不是对方法本身的反驳。**
2. ⚠️⚠️ **他主张的那条自我改进闭环，其验证环节是他自己说还没建的**：**"我们还没有这个，但下一步想做的是：对任何这样的建议改动，你可以回去重放那些运行，确认它真的会让它们变好。"**（[00:15:10]）🔗 **本库把这归到 [MakerMaker 的"闭环 ≠ 起飞"](../videos/20261012-a16z-makermaker-rsi-numerator-denominator.md) 判别式的分母侧。**

---

## 相关页面

- 视频：[Latent Space × Warp.dev（2026-11-03）](../videos/20261103-latent-space-warp-software-factory-80-to-15-dollars-per-pr.md)
- 主题：[LLM 实用方法论](../topics/using-llms-in-practice.md) · [评估与 Benchmark](../topics/evaluation-and-benchmarks.md) · [AI 商业模式与价值捕获](../topics/ai-business-and-value-capture.md) · [AI 基础设施](../topics/ai-infrastructure.md) · [AI 做 AI / 自动化研究](../topics/ai-for-ai-and-auto-research.md)
- 同一条线上的人物：[Ali Ghodsi](ali-ghodsi.md)（harness 值 2 倍成本）· [Akshat Bubna](akshat-bubna.md)（agent sandbox 供给侧）· [MakerMaker 联创](makermaker-founders.md)（闭环判别式）· [Latent Space 主播](latent-space-hosts.md)
