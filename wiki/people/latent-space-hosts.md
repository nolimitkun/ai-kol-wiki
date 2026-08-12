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
| 2026-07-22 | [Model Factory、Laguna S、开源与 AGI 竞赛](../videos/20260722-latent-space-poolside-eiso-kant.md) | Eiso Kant（Poolside CEO） |
| 2026-07-28 | [OpenAI 把 ChatGPT 做成"万物应用"](../videos/20260728-latent-space-akshay-nathan-chatgpt-work.md) | [Akshay Nathan](akshay-nathan.md)（OpenAI 核心产品工程） |
| 2026-08-03 | [推理是新的训练：推理工程全景](../videos/20260803-latent-space-baseten-inference-engineering.md) | [Philip Kiely & Ali Taha](baseten-team.md)（Baseten） |
| 2026-08-11 | [生物学正在变成软件：蛋白质设计的"中性软件工厂"](../videos/20260811-latent-space-chai-discovery-protein-design.md) | [Matt McPartlon & Neil Patil](chai-discovery.md)（Chai Discovery）⚠️ **"AI for science" 子系列，非 swyx / Alessio 主持** |

> ⚠️ **本频道存在一个由不同主持人运作的 "AI for science" 子系列**，本库 2026-08-11 首次明确记录。主持是 **Brandon**（Atomic AI，做 RNA 疗法）与 **RJ Honiki**（Mirror Omix CTO 兼联创）——**两位本身都是 AI-bio 创业者，而不是媒体人**。⚠️ 这对引用有直接影响：**这个子系列里的"主持人观点"是同行的技术判断，不是提问框架**。
> 例如 Chai 那期里，主持人自己给出了两条本库照录的实质判断：① **抗体在进化上不可能有模板，所以 MSA 这个魔法在抗体上失效**（这条解释了为什么 AlphaFold 2 在抗体-抗原上只有约 11% 正确率）；② 对嘉宾"简单性偏好"的**正面反驳**——AlphaFold 2/3 之所以 work，**恰恰因为它们是数据效率极高的小模型、一层归纳偏置叠一层归纳偏置**，要超过它"你真的需要新的数据来源"。本库把第二条记为该期**未解决的分歧**。
> 本库既有的 [Genesis Molecular AI](../videos/20260630-latent-space-genesis-diffusion-drug-discovery.md)、[Xaira](../videos/20260721-latent-space-xaira-xcell-virtual-cell.md)、[Lila Sciences](../videos/20260716-latent-space-lila-sciences.md) 三期在选题上同属这条线，⚠️ **但本库未回溯核实其主持人是否为同一组，暂不追认。**

> ⚠️ **swyx 的"推理 ASIC 是好赌注"立场在 2026-08-03 那期被现场压力测试，并被他自己收窄**。原立场（2026-07-10）是"**推理这件事大到理所当然会有专用 ASIC**，且押注架构不变是好赌注，因为存量 workload 不会迁移"。Baseten 的 Ali Taha 从**供给侧**给出反向论证：**Rubin 相比 Ampere/T4"基本上就是个 ASIC"**（systolic array、tensor core、TMA、tensor memory，指令形状几乎按当今模型 head 维度定制），即**专用性正被 GPU 自己吸收**；且若前沿实验室每年换架构，独立 ASIC 等于"**每年花 500 亿造新的、把去年的扔掉**"。
> swyx 的回应把立场拆成了两半（[视频页](../videos/20260803-latent-space-baseten-inference-engineering.md) [01:06:41]–[01:07:41]）：**垂直整合的模型实验室自研 ASIC**（OpenAI–Broadcom）"完全说得通"，援引 Martin Casado 的算术"**5000 亿的训练拿 500 亿去做 ASIC 就很合理**"；而**独立 ASIC 公司**的价值在**互联与内存/硬件布局分配**而非算子——"**10 倍到 1000 倍更快的推理，真正的阻碍不是能在现有 GPU 设计里重排的那些东西**"，目标量级是**每秒 30 万 token**。
> 另一方面，**Philip Kiely 的"模型寿命比想象的长"恰是 swyx 那条"存量 workload 不会迁移"的正面证据**："还有人在用 4o、我还看到 Llama 3 的工作负载。"**本库记为同一立场被拆细，不是翻转。**

> ⚠️ **swyx 反对模型路由的立场，与 2026-07-28 那期存在一处需要区分的表面冲突**：OpenAI 的 ChatGPT Work **由模型自己决定进 chat 模式还是 work 模式**。但这是**同厂商内的模式路由**，不是 swyx 反对的**跨厂商最小公分母路由**；而且它与 swyx 那句"人们不想选用哪版 AGI，他们只想让 AGI 替他们决定"方向一致。本库把两者记为**不同层的路由**，不视作立场翻转。
