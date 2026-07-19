# Latent Space（swyx & Alessio）

- **背景**: Latent Space 播客双主播——swyx（Shawn Wang）与 Alessio Fanelli，面向"AI 工程师"的应用/工程视角；"Cooking"系列以边做饭边访谈的轻松格式著称。
- **频道**: [YouTube @LatentSpacePod](https://www.youtube.com/@LatentSpacePod)
- **watchlist slug**: `latent-space`

## 立场与关注点

- 偏 AI engineering / 应用 LLM 实践；关注 evals、agent、infra、研究组织方法等工程与研究落地话题。

### swyx 本人的立场（2026-07-10 交叉播客，他作为被访者）

本库首次收录 swyx 作为**被访者**的系统表达，见 [视频页](../videos/20260710-latent-space-swyx-agent-labs.md)。

- **"agent lab"**（他给应用层创业者的两字答案）：**不要挑解法，要挑问题**——"我就做牙医的 AI 人 / 律师的 / 金融的"，然后把每一波新能力叠进去做最后一公里。Sierra、Cognition、Cursor、Decagon、Harvey 都是各自领域的 agent lab。对"这是不是赌模型不泛化"的追问，他的回答是赌的恰是反面：**"你要反对的是'能力过剩将来不再存在'——而我认为那是个相当安全的赌注。"**（00:21–00:23）
- ⚠️ **反对 model-agnostic / 模型路由**：这是他与本库多位应用层 CEO 的正面分歧。"**如果你以路由为傲，你永远无法充分利用任何一个模型的完整能力**……这是成为所有模型的最小公分母、并完全错过全部能力的绝佳方式。"他以云计算浪潮为类比（all-in AWS 的赢过多云抽象的），并称路由"更像一句营销词"——真正顶尖的 agent 构建者谈的都是把一个模型的 prompt 面、tool use、缓存榨干（00:24–00:27）。
- **能力过剩（capability overhang）会长期存在**："AI engineer 就活在峰值能力与'把它部署到所有地方'之间的那片白色地带。"每一代模型会吞掉一批自建脚手架——"我们时不时做次大扫除，这很正常，不该对代码有任何感情"。
- **Fable 是这一代 LLM 的终点**（预测）：论证不是能力而是**预算**——"我想活在无限预算的世界里，但我没有的预算是**时间**"。若 20 万亿参数就是极限，在可用性意义上这一代就到头了。
- **pdoom 必须绑定时间尺度**：5 万年尺度约 90%，**10 年内近乎零，50 年约 5%**。"我们并不比之前存在过的任何物种更有权利继续存在。"对齐观："**默认假设应该是对齐概率很低**；如果要偏，就往安全方向偏。"他同时反对末日近视——"谁说你不是处在未来人眼中的史前时代？"
- **LLM 不足以导向 RSI**：LLM 让递归成为可能，但"**多半只探索已被探索过的东西**"，离已知分布不远。
- **"数据效率是下一个问题"**，但附带自我限制——**"酸涩的教训（sour lesson）：每次拿人类类比机器，你多半会失败。"** LLM 可以是"异类的、更高效的学习方式"，不必塞进人类的盒子；只是"极度低效"本身是确知的纯负面项。
- **推理 ASIC**：Etched/MatX 不是要颠覆 NVIDIA，"**推理这件事大到理所当然会有专用 ASIC**"；押注架构不变是好赌注，因为存量 workload 不会迁移。
- **AIE 的政治定位**：在 EA 与 e/acc 之间"正中间"——**要乐观但不要无约束的乐观**，所以护栏、微调、eval 才重要。

## 已收录访谈

| 日期 | 视频 | 嘉宾 |
|---|---|---|
| 2026-06-22 | [Codex/Claude Code 之后的 AI 安全](../videos/20260622-latent-space-gray-swan.md) | Zico Kolter & Matt Fredrikson（Gray Swan） |
| 2026-06-24 | [Agent Cloud：Databricks 押注 AI 的未来](../videos/20260624-latent-space-databricks-agent-cloud.md) | Matei Zaharia & Reynold Xin（Databricks） |
| 2026-06-25 | [AGI、o1、评估与 Scaling Laws](../videos/20260625-latent-space-mark-chen.md) | Mark Chen（OpenAI CRO） |
| 2026-07-13 | [AI 的记忆问题：为什么长上下文还不够](../videos/20260713-latent-space-dan-biderman.md) | Dan Biderman（Engram，记忆/持续学习） |
