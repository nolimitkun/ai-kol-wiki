# Latent Space（swyx & Alessio）

- **背景**: Latent Space 播客双主播——swyx（Shawn Wang）与 Alessio Fanelli，面向"AI 工程师"的应用/工程视角；"Cooking"系列以边做饭边访谈的轻松格式著称。
- **频道**: [YouTube @LatentSpacePod](https://www.youtube.com/@LatentSpacePod)
- **watchlist slug**: `latent-space`

## 立场与关注点

- 偏 AI engineering / 应用 LLM 实践；关注 evals、agent、infra、研究组织方法等工程与研究落地话题。

### swyx 本人的立场（2026-07-10 交叉播客，他作为被访者）
来源：[Latent Space 2026-07-10](../videos/20260710-latent-space-swyx-agent-labs.md)

本库首次收录 swyx 作为**被访者**的系统表达，见 [视频页](../videos/20260710-latent-space-swyx-agent-labs.md)。

- **"agent lab"**（他给应用层创业者的两字答案）：**不要挑解法，要挑问题**——"我就做牙医的 AI 人 / 律师的 / 金融的"，然后把每一波新能力叠进去做最后一公里。Sierra、Cognition、Cursor、Decagon、Harvey 都是各自领域的 agent lab。对"这是不是赌模型不泛化"的追问，他的回答是赌的恰是反面：**"你要反对的是'能力过剩将来不再存在'——而我认为那是个相当安全的赌注。"**（00:21:16–00:23:16）
- ⚠️ **反对 model-agnostic / 模型路由**：这是他与本库多位应用层 CEO 的正面分歧。"**如果你以路由为傲，你永远无法充分利用任何一个模型的完整能力**……这是成为所有模型的最小公分母、并完全错过全部能力的绝佳方式。"他以云计算浪潮为类比（all-in AWS 的赢过多云抽象的），并称路由"更像一句营销词"——真正顶尖的 agent 构建者谈的都是把一个模型的 prompt 面、tool use、缓存榨干（00:24:17–00:27:18）。
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
| 2026-08-26 | [物理一出现 Transformer 就撞墙：神经算子与 FourCastNet](../videos/20260826-latent-space-anandkumar-neural-operators.md) | [Anima Anandkumar](anima-anandkumar.md)（Caltech）⚠️ **"AI for science" 子系列** |
| 2026-09-02 | [推理前沿：从 100 到 10000 tokens/秒](../videos/20260902-latent-space-cerebras-sean-lie-inference-frontier.md) | [Sean Lie](sean-lie.md)（Cerebras CTO，录于 Hot Chips 次日） |
| 2026-09-04 | [一万亿 token 上下文，以及物理世界的"一个模型"](../videos/20260904-latent-space-accelerated-understanding-trillion-token-context.md) | [Anima Anandkumar](anima-anandkumar.md) & Benedikt Jenik（Accelerated Understanding）⚠️ **"AI for science" 子系列，RJ + Brandon 主持；是 08-26 那期的续集** |
| 2026-09-14 | [Eureka 机器、auto research 的第一批战果，以及"智能的上界"](../videos/20260914-latent-space-richard-socher-recursive-self-improvement.md) | [Richard Socher](richard-socher.md)（Recursive / you.com；swyx + Vibhu） |
| 2026-09-18 | [从 302 个神经元的线虫到硬件感知架构搜索](../videos/20260918-latent-space-liquid-ai-ramin-hasani.md) | [Ramin Hasani](ramin-hasani.md)（Liquid AI CEO；swyx + 新任 head of editorial Richard） |
| 2026-09-25 | [OpenRouter × Stripe：分发短板与 10 万亿 token 经济](../videos/20260925-latent-space-openrouter-stripe-token-economy.md) | [Alex Atallah & Anjney Midha](openrouter-atallah-midha.md)（OpenRouter CEO / a16z GP；swyx 主持，录于 Midha 家中） |
| 2026-09-22 | [ERA：把科学问题映射成"可打分任务"](../videos/20260922-latent-space-john-platt-era-scorable-tasks.md) | [John Platt](john-platt.md)（Google Fellow；**AI for science 子系列**，Brandon + R.J.） |
| 2026-09-21 | [TypeSafe / Jev：让代码而不是人来消费模型](../videos/20260921-latent-space-typesafe-jev-system-one-models.md) | [Diogo Almeida](diogo-almeida.md)（TypeSafe 联创兼 CEO，前 OpenAI；swyx 独立主持） |
| 2026-09-25 | [Runway：世界模型、机器人与神经操作系统](../videos/20260925-latent-space-runway-world-models.md) | [Anastasis Germanidis](anastasis-germanidis.md)（Runway 联合创始人兼 CTO；swyx + Vibhu） |
| 2026-09-23 | [生物安全是一场军备竞赛](../videos/20260923-latent-space-eric-nguyen-biosecurity-arms-race.md) | [Eric Nguyen](eric-nguyen.md)（Radical Numerics CEO、Evo 一作；**AI for science 子系列**，Brandon + RJ） |
| 2026-09-29 | [可变软件、harness 的苦涩教训与来自防守侧的 pacing 论证](../videos/20260929-latent-space-thariq-claude-code-mods-pacing.md) | [Thariq Shihipar](thariq-shihipar.md)（Anthropic，Claude Code 团队；swyx + Vibhu） |
| 2026-09-30 | [OpenAI Dev Day 现场：computer use 已经比普通人快，以及 Decisions API](../videos/20260930-latent-space-openai-devday-computer-use-decisions-api.md) | [Ari Weinstein](ari-weinstein.md) + [Nikunj Handa](nikunj-handa.md)（OpenAI；**Dev Day 现场加场、两段**，⚠️ 主播姓名未在转录稿中播报） |
| 2026-10-02 | [ClusterMAX 3.0：哪些 GPU 云真的能用](../videos/20261002-latent-space-clustermax3-neocloud-rankings.md) | [Jordan](semianalysis-jordan.md) + [Dylan Patel](dylan-patel.md)（SemiAnalysis；**"Lightning" 短期格式**，swyx 主持，Dylan 开场约六分钟后中途加入） |
| 2026-10-02 | ["所有 harness 其实都是同一个"：RLM、locally in distribution 与"这是个 skill issue"](../videos/20261002-latent-space-alex-zhang-recursive-language-models.md) | [Alex Zhang](alex-zhang.md)（MIT 博士二年级，RLM 论文作者；swyx + 一位未播报姓名的主播；⚠️ **他与 Prime Intellect 合作做 Prime Agent**） |
| 2026-10-20 | [可编程的数据中心：实物交割、远期曲线的驼峰、"你得先杀掉自己的生意才能做成这件事"](../videos/20261020-latent-space-sf-compute-physical-settlement.md) | [Evan Conrad](evan-conrad.md)（SF Compute；**AI Engineer 大会现场加场**，swyx 主持）；⚠️ **swyx 在本期自述做过衍生品 / 外汇 / 利率交易员，并据此把访谈定在"201 级而不是 101 级"**——本期多条最锋利的重述出自他（**"所以这其实是一个违约解除租约的市场"**、**"你在把数据中心虚拟化、并让它可编程吗"**、以及用商品分级逼出"算力为什么还不可互换"的整张清单） |

> ⚠️ **2026-09-23 那期是本库里"主持人即同行"这条性质最有产出的一次**。[Eric Nguyen 那期](../videos/20260923-latent-space-eric-nguyen-biosecurity-arms-race.md) 里**本页最硬的三条反驳全部来自主持方**，而且每一条嘉宾都没有驳回、而是把自己的目标往下调：
>
> - **RJ（做空间转录组）用领域知识质疑一条结果的来源**（[Eric Nguyen 那期](../videos/20260923-latent-space-eric-nguyen-biosecurity-arms-race.md) [00:37:14]）：RNA"**以缺少好的共进化数据而出名**"，哺乳动物 RNA 通常没有进化压力——**那这个能力从哪来？**嘉宾的回答是"**说实话我不确定。我们也很意外。**"
> - ⚠️ **RJ 还替听众还原了实验来路，并给出本页认为必须一起引用的限定**（[同期](../videos/20260923-latent-space-eric-nguyen-biosecurity-arms-race.md) [00:45:25]）：那个"DNA 版 chain of thought"的数据集其实是 SELEX 式的定向进化实验——"**关键是做筛选的其实是实验的生物学本身。**"
> - ⚠️ **RJ 对"类比网络安全"的拆解**（[同期](../videos/20260923-latent-space-eric-nguyen-biosecurity-arms-race.md) [01:24:33]）："**我们的基因组是固定的，对吧？所以你没法给一个人打补丁。**"
> - **Brandon 的 steelman**（[同期](../videos/20260923-latent-space-eric-nguyen-biosecurity-arms-race.md) [01:22:28]）："**如果你在前沿，那你是在同时推进攻击和防守的前沿**……那长期来看它其实没什么意义。"——**这条在本期没有被回答。**
>
> 本库据此再次确认：⚠️ **引用这个子系列时，"主持人说"应当与"嘉宾说"同等对待，而不是当成提问框架。**

> ⚠️ **2026-08-26 那期确认了 "AI for science" 子系列的主持人身份**：字幕里两人各自自报家门——**Brandon**（Atomic AI，做 RNA 疗法）与 **RJ Honakee**（Miraomics CTO 兼创始人，做空间转录组）。⚠️ 这与本库 2026-08-11 首次记录的那一组（`RJ Honiki` / `Mirror Omix`）**应为同一组人，只是自动字幕拼写不同**；本库两处拼写都保留，**不做统一认定**。
>
> ⚠️ **这一期也把该子系列的范围从生物/化学扩到了连续介质物理**（天气、气候、等离子体、材料、流体）。⚠️ 值得单记的是**主持人的技术判断再次进入实质论证**——由主持人提出的 AlphaFold 类比（[Anandkumar 那期](../videos/20260826-latent-space-anandkumar-neural-operators.md) [00:45:01]）（**蛋白质结构之所以是生物学里少数几个大胜，正因为它受物理强约束**），与嘉宾的"物理世界更宽容"合起来，构成了本库 [AI for science 页](../topics/ai-for-science.md) 目前最统一的一条横向判据。
>
> ⚠️ **频道的另一条记录**：2026-09-18 那期出现了一位**新任 head of editorial（Richard，远程连线）**，本库首次记录。

> ⚠️ **本频道存在一个由不同主持人运作的 "AI for science" 子系列**，本库 2026-08-11 首次明确记录。主持是 **Brandon**（Atomic AI，做 RNA 疗法）与 **RJ Honiki**（Mirror Omix CTO 兼联创）——**两位本身都是 AI-bio 创业者，而不是媒体人**。⚠️ 这对引用有直接影响：**这个子系列里的"主持人观点"是同行的技术判断，不是提问框架**。
> 例如 Chai 那期里，主持人自己给出了两条本库照录的实质判断：① **抗体在进化上不可能有模板，所以 MSA 这个魔法在抗体上失效**（这条解释了为什么 AlphaFold 2 在抗体-抗原上只有约 11% 正确率）；② 对嘉宾"简单性偏好"的**正面反驳**——AlphaFold 2/3 之所以 work，**恰恰因为它们是数据效率极高的小模型、一层归纳偏置叠一层归纳偏置**，要超过它"你真的需要新的数据来源"。本库把第二条记为该期**未解决的分歧**。
> 本库既有的 [Genesis Molecular AI](../videos/20260630-latent-space-genesis-diffusion-drug-discovery.md)、[Xaira](../videos/20260721-latent-space-xaira-xcell-virtual-cell.md)、[Lila Sciences](../videos/20260716-latent-space-lila-sciences.md) 三期在选题上同属这条线，⚠️ **但本库未回溯核实其主持人是否为同一组，暂不追认。**

> ⚠️ **swyx 的"推理 ASIC 是好赌注"立场在 2026-08-03 那期被现场压力测试，并被他自己收窄**。原立场（2026-07-10）是"**推理这件事大到理所当然会有专用 ASIC**，且押注架构不变是好赌注，因为存量 workload 不会迁移"。Baseten 的 Ali Taha 从**供给侧**给出反向论证：**Rubin 相比 Ampere/T4"基本上就是个 ASIC"**（systolic array、tensor core、TMA、tensor memory，指令形状几乎按当今模型 head 维度定制），即**专用性正被 GPU 自己吸收**；且若前沿实验室每年换架构，独立 ASIC 等于"**每年花 500 亿造新的、把去年的扔掉**"。
> swyx 的回应把立场拆成了两半（[视频页](../videos/20260803-latent-space-baseten-inference-engineering.md) [01:06:41]–[01:07:41]）：**垂直整合的模型实验室自研 ASIC**（OpenAI–Broadcom）"完全说得通"，援引 Martin Casado 的算术"**5000 亿的训练拿 500 亿去做 ASIC 就很合理**"；而**独立 ASIC 公司**的价值在**互联与内存/硬件布局分配**而非算子——"**10 倍到 1000 倍更快的推理，真正的阻碍不是能在现有 GPU 设计里重排的那些东西**"，目标量级是**每秒 30 万 token**。
> 另一方面，**Philip Kiely 的"模型寿命比想象的长"恰是 swyx 那条"存量 workload 不会迁移"的正面证据**："还有人在用 4o、我还看到 Llama 3 的工作负载。"**本库记为同一立场被拆细，不是翻转。**

> ⚠️ **swyx 反对模型路由的立场，与 2026-07-28 那期存在一处需要区分的表面冲突**：OpenAI 的 ChatGPT Work **由模型自己决定进 chat 模式还是 work 模式**。但这是**同厂商内的模式路由**，不是 swyx 反对的**跨厂商最小公分母路由**；而且它与 swyx 那句"人们不想选用哪版 AGI，他们只想让 AGI 替他们决定"方向一致。本库把两者记为**不同层的路由**，不视作立场翻转。

> ⚠️ **"AI for science" 子系列的主持人构成在 2026-10-08 那期（[Periodic Labs](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md)）再次无法确认**：⚠️ **两位主持的姓名全程未被播报**。可辨认的是其中一位**自述"我从金融来，做过 Gaussian copula"**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [00:35:24]）、并自称**"作为非科学家、但偏工程的那边来，熟悉 ML 这侧但不熟悉物理这侧"**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [00:14:05]）；另一位**自述"我此前和湿实验室密切合作过"、"我从生物学世界来"**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [01:01:36]、[01:06:42]）。⚠️ **他们提到本频道的 "science pod" 第二期嘉宾是 Heather Kulik（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [00:34:21]），且回忆开张时有过一场"哪个学科更难"的攀比（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [00:42:28]）——与上文记录的子系列一致，但本库仍不追认主持人身份。**
>
> ✅ **而这一期里主持人的提问本身带来了两条本库照录的实质内容，值得记**：① ⚠️ **那条"你们不是已经把物理定律搞定了吗？为什么还没有完美的仿真器"的外行提问，直接逼出了本库这条线上最完整的一段"仿真为什么不够"**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [00:14:05]–[00:18:09]）；② ⚠️ **"如果你 100% 实验室自动化，你究竟怎么走到超导"这个 steelman，逼出了嘉宾把难点从理论整体挪到合成、并给出 MgB₂ 那个支点性的历史例子**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [01:22:55]）。
> ⚠️ **另外，其中一位在本期引了一条本库此前没有的第三方立场**：**"我和 Elad Gil 最难忘的一次对话之一是，他其实对量子计算非常怀疑——他说即使你今天就有了它，也没有应用"**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [00:46:30]）；⚠️ **而他自己的保留是"它会破掉安全性，我总是说那就是（应用）"。本库记为转述，不记为 [Elad Gil](no-priors-hosts.md) 的直接表态。**

> ✅ **2026-10-13 那期（[Dyna Robotics](../videos/20261013-latent-space-dyna-robotics-world-action-model.md)）是一次上门实地录制**，含机器人演示 B-roll。⚠️ **转录稿为自动字幕、无 SPEAKER 标签，两位主持的提问本库统一记为"主持方"，不区分 swyx 与 Alessio。** 片中有一处可定位的个人信息——**其中一位自述与嘉宾同为宾大校友、并说"我最大的遗憾是没参加那届 DARPA 挑战赛，否则我可能成了早期 Waymo 的人"**（[视频页](../videos/20261013-latent-space-dyna-robotics-world-action-model.md) [01:00:41]）；⚠️ **本库不据此认人。**
>
> ✅ **这一期里主持方的追问带来三条本库照录的实质内容**：① ⚠️ **"折餐巾这种事按直觉该用专用机器人做到毫米级"这个质疑，逼出了嘉宾关于可变形物体的那条核心反驳**（[视频页](../videos/20261013-latent-space-dyna-robotics-world-action-model.md) [00:40:21]）；② ⚠️⚠️ **"如果你错了，最可能对的是谁"这一问，拿到了本库少见的、由嘉宾主动给出的具体技术性自我证伪条件**（视觉冗余 / 触觉可能 100 倍数据效率）（[视频页](../videos/20261013-latent-space-dyna-robotics-world-action-model.md) [00:57:38]–[00:59:41]）；③ ⚠️ **"有些公司选择只做模型、声称可部署到任何平台"这个 platformless 对照，逼出了嘉宾援引自己在 DeepMind 与 NVIDIA 的经历讲"系统的上界"**（[视频页](../videos/20261013-latent-space-dyna-robotics-world-action-model.md) [00:26:16]）。
> ⚠️ **另记一条主持方自己给出的技术补充，本库认为比嘉宾的回答更具体**：关于 flow matching——它在质量上有取舍，**但特别适合 action diffusion，因为你可以实时重新评估**，而图像生成"基本是一次性的"（[视频页](../videos/20261013-latent-space-dyna-robotics-world-action-model.md) [00:08:03]）。
> ⚠️ **本频道在机器人世界模型这条线上已形成可对照的两期**：[Runway（2026-09-25）](../videos/20260925-latent-space-runway-world-models.md) 从视频生成一侧主张"第三人称视频 + action head"，本期从拥有硬件的一侧回应"视频模型公司转机器人会卡在传感融合的 know-how 上"。**同一主播下的直接对位，本库不裁决。**

> ✅ **2026-10-13 另有一期自制内容（[Kill My SaaS](../videos/20261013-latent-space-kill-my-saas-43k-event-software.md)），本库据此第一次为本频道记下一条"主播作为买方与出题人"的材料**：⚠️ **归属在本期反而比多数访谈更清楚**——主讲自述**"我经营两家生意，Latent Space 和 AI Engineer"**（[视频页](../videos/20261013-latent-space-kill-my-saas-43k-event-software.md) [00:00:00]），而 AI Engineer 是 swyx 的会议品牌，**故主讲判定为 swyx**；另出场的 **Kelsey 被他点名为 AI Engineer 的 head of ops**。
>
> ⚠️⚠️ **本库认为这期里最该记在主播名下的是两条自我削弱**：① **他公布了自己发布的那套 AI 评委与人工验收的背离，而且数字对他不利**——AI 评委 top 10 里 6 个被人类评为弱、**最终获胜者在 AI 榜上排第 19**，并自评"**所以它挺弱的**"、"**所以这场竞赛其实并不客观**"（[视频页](../videos/20261013-latent-space-kill-my-saas-43k-event-software.md) [00:09:12]–[00:10:12]）；② ⚠️ ✅ **他自己的 agent 实践被自己的实验数据反驳**——他自述"**我通常一个项目只用一个模型，这样所有 context 都留在一个地方**"，紧接着是"**结果很多这些 builder 不这么干，他们会切换角色**"（[视频页](../videos/20261013-latent-space-kill-my-saas-43k-event-software.md) [00:11:13]）。**本库记为一次公开的自我修正，不记为立场翻转。**
>
> ⚠️ **另记一条他在本期的制度性自述**：**多年来他公司的创始合同里明文写着"没有他的明确批准，任何人不得自建内部软件"**（理由是"太容易得 not invented here 综合症"），**"今年我改了主意……而我正押上真金白银来验证"**（[视频页](../videos/20261013-latent-space-kill-my-saas-43k-event-software.md) [00:01:01]–[00:02:01]）。✅ **本库认为这条比任何论断都更能定位他在"自建 vs 买"这场辩论里的位置：他原本是制度化的买方。**

> ✅ **2026-10-14 的 [Leash Bio 那期](../videos/20261014-latent-space-leash-bio-chemist-not-chemistry.md) 是 "AI for science" 子系列里本库第一次拿到明确播报的主持人自我介绍**：**"我是 R.J.，Mirror OMIX 的 CTO，我的联合主持是 Brandon Anderson，他在 Atomic AI 做 RNA 疗法"**（[视频页](../videos/20261014-latent-space-leash-bio-chemist-not-chemistry.md) [00:01:00]）。⚠️ **姓名拼写仍来自自动字幕**：本期作 **"R.J. Haniki" / "Mirror OMIX"**，而本库既有页面曾记为 **RJ Honicky / Honakee / Honiki**、**MiraOmics / Mirror Omix**——⚠️ **本库仍不写定拼写，但据此追认这条子系列的主持人构成与 [Xaira](../videos/20260721-latent-space-xaira-xcell-virtual-cell.md)、[Chai Discovery](../videos/20260811-latent-space-chai-discovery-protein-design.md)、[Anandkumar](../videos/20260826-latent-space-anandkumar-neural-operators.md)、[Eric Nguyen](../videos/20260923-latent-space-eric-nguyen-biosecurity-arms-race.md) 几期一致。**
>
> ⚠️ **本期两位主持的发言在自动字幕里不可区分（无 SPEAKER 标签），而两位都给出了实质技术内容，所以视频页统一记为"主持人"。** ✅ **而本库认为这一期最该记在主播名下的是三条由他们自己带进来的内容，而不是提问技巧**：
> ① ⚠️⚠️ **"按分子量排序"那条**：在大多数公开数据集里它是最大的单一预测因子之一、在 **CASF-2016 上并列第一**（⚠️ **稿中随即自我修正为"第二名，差距非常小"**），而定性是 **"这不是化学的内在属性，这是这个数据集的属性"**（[视频页](../videos/20261014-latent-space-leash-bio-chemist-not-chemistry.md) [00:51:23]）。✅ **这条是本期判决性实验之外最硬的一条配套证据，而它由主持方提供。**
> ② ⚠️ **"Picasso 问题"那个类比**：CNN 只抓局部特征、没有全局拓扑，把鼻子翻过来也照样认——而 **DEL 上的对应失败是模型把分子分解成三个 building block 的和**（[视频页](../videos/20261014-latent-space-leash-bio-chemist-not-chemistry.md) [00:42:19]）。
> ③ ⚠️⚠️ **mech interp 在生物学里的反向用法**：**"它之所以在性质上不同，是因为你是反过来走的——你是从模型那里学关于生物学的东西"**，理由是**语言的缺席**——**"在这些机器学习模型里没有语言可以依靠，所以除了检查模型内部，你完全不知道它在想什么"**（[视频页](../videos/20261014-latent-space-leash-bio-chemist-not-chemistry.md) [01:14:36]）。
> ⚠️ **另记一条由主持方引入的硬问题**：**"机器学习与发现的 Kosuri 悖论"**（出处是 Sri Kosuri 的一条推文；⚠️ **主持人说本人几周前上过本播客、那期还没发，并自责"我居然没在他那期提这个"**）——**而这一问拿到了嘉宾全期唯一一次明确让步**（[视频页](../videos/20261014-latent-space-leash-bio-chemist-not-chemistry.md) [01:36:50]）。
>
> ⚠️⚠️ **而这一期有一个会影响怎么读后 20 分钟的格式细节，本库记在主播名下**：嘉宾自己要求的 **"don't come at me, bro"** 环节里，**硬问题大部分由 Claude 生成**——**"我们只有大约 24 小时准备，所以我觉得这些大部分会是 Claude 最难的问题"**（[视频页](../videos/20261014-latent-space-leash-bio-chemist-not-chemistry.md) [01:25:46]），另有两处明确点名"这个是纯 Claude 的"（[视频页](../videos/20261014-latent-space-leash-bio-chemist-not-chemistry.md) [01:26:47]、[视频页](../videos/20261014-latent-space-leash-bio-chemist-not-chemistry.md) [01:42:52]）。✅ **本库的观察是覆盖面与追问深度的分工**：⚠️ **那一段问题覆盖很齐但追问普遍只有一轮，而本期最有信息量的几处恰恰来自主播自己的追问**（见上面三条）。⚠️ **另记一处相反方向**：主播自述某个背景理解 **"来自和 Claude 聊、谷歌之类的"**（[视频页](../videos/20261014-latent-space-leash-bio-chemist-not-chemistry.md) [01:23:43]），⚠️ **而嘉宾第一句就是修正。** 详见 [在实践中使用 LLM](../topics/using-llms-in-practice.md)。

---

## ⚠️ 新系列：*High Taste Testers*（2026-10-16 起）

来源：[High Taste Testers 第一期](../videos/20261016-latent-space-high-taste-testers-products-vs-models.md)

- **形式**：swyx 主持的**六人配餐圆桌**（"这是史上第一期 High Taste Testers，欢迎各位"，[00:00:00]），召集理由是 **"你们被聚到这儿，是因为你们是品味高的人，你们一直在测模型和产品"**。参与者见 [High Taste Testers 六人组](high-taste-testers.md)。
- ⚠️⚠️ **本库记一条影响全期可用性的格式问题，并把它记在节目侧**：**这一期的自动字幕没有说话人名，而六个人高密度互打**——结果是**大部分观点无法归属**。✅ **本库只能靠片尾各自的自我介绍反推出少数几条。** ⚠️ **与 Latent Space 的常规单人访谈相比，这个格式对转录稿档案的价值损失很大**；若该系列延续，**本库会优先考虑给这类多人期做说话人分离**。
- **一条值得记的开场声明**（[00:00:00]）：**"我们是在 OpenAI DevDay 刚结束时录的。OpenAI 不在场。你们可以想多诚实、多直接都行。"** ✅ **本库按此读全期对实验室产品执行的批评——它是被主持人主动创造出来的坦率条件，而不是偶发的吐槽。**
- ⚠️ **swyx 在本期的两处立场**（可归属，因为是主持人提问/断言）：
  - **"应该有一个东西拥有你所有的搜索历史。所以你不该路由。路由是坏的"**（[01:08:43]）——⚠️ **这与席上所有人的实际做法相反**（见 [LLM 实用方法论](../topics/using-llms-in-practice.md)），而现场的反驳是 **"但不测你就当不了 high taste tester"**。
  - **他多次提及自己刚做过那家决策模型公司创始人的专访**（[00:20:16]、[00:25:17]、[00:29:18]），并在期内说 **"我们其实在那期播客里留了下一代模型是什么的线索，你够聪明就能找出来"**。⚠️ **本库记这处利益相关：本期关于该品类的讨论由主持方的既有报道引入。**

---

## ⚠️⚠️ swyx 的交易员履历：一次与当期主题同构的披露（2026-10-22）

来源：[Latent Space × Anekha Sokhal / Moshi](../videos/20261022-latent-space-moshi-recsys-for-traders.md)

⚠️ **本库此前只知道 swyx 从金融转入技术，没有具体位置与经验。这一期他因为嘉宾是前交易员而完整披露了一遍，而且披露的内容直接构成对当期产品前提的独立对照。本库记在主播名下。**

- **路径**（[00:13:15]）：**在伦敦做外汇期权交易，之后做过一段利率**；他说自己的路径与嘉宾相似——**"你从 EMEA 开始，然后进 G10"**（⚠️ 他注明"至少外汇里我们这么叫"）；**后来转到买方，开始花钱买替代数据**。
- ⚠️⚠️ **他给的那个数字与那条怀疑，本库认为是本期最该记在他名下的一条**：他们在 **Balyasny** 是最早做 **X / Twitter firehose** 的少数几家之一——**"那是个贵得离谱的数据，大概每月 30 万美元，你得付这个钱才能拿到所有推文"**；买方还会买**卫星信息、信用卡数据**之类。✅ **而他的评价是否定的**：

  > **"它非常嘈杂。所以我有点瞪眼，因为我不确定我会不会拿这些东西去交易——因为有时候人就是在胡说，有时候人是故意说点什么来操纵市场。而且它就是没那么重要。"**

  ⚠️ **本库标注：当期嘉宾的产品把 X 数据列为四类数据源之一，并说用户会追自己信任的个人账号；他在同一期对这类数据给出了基于一手经验的否定评价，而嘉宾没有回答他的两条具体怀疑（胡说、操纵）。本库并列两条，不判定。**
- ✅ **另一条他自己带进来的背景，本库认为比嘉宾的回答更有信息量**（[00:09:11]）：谈 Bloomberg 的护城河时他补充——**"交易员会在聊天里成交几十亿美元，而且有一套标准化的格式"**，而**他自己进入 NLP 的起点就是把 Bloomberg chat 解析成结构化的定价表来做期权定价**。
- ⚠️ **一条他对行业注意力分配的观察，本库记为独立材料**（[00:11:13]）：**"作为 AIE 的策展人，我每年都办一个 LLM RecSys track"**——⚠️⚠️ **"这个 track 甚至没什么人来，尽管来讲的有些人就是在给 YouTube 做 RecSys、给 Netflix 做 Netflix、给 Instagram 和 TikTok 做的那些人。然后没人来。我就想：什么意思？你对 RecSys 不感兴趣？"** ✅ **嘉宾给的解释是"他们把它做得看起来太容易了"，他接了一句"这是整个公司里最重要的系统"。**
- ⚠️ **一处对自家嘉宾产品的保留，未被追问**（[00:11:13]）：**"Netflix 有一整套成瘾性的那一面，那是坏的。"** ✅ **嘉宾只答"确实有"，没有展开**——⚠️ **而她的产品主张之一正是"把数据推给你、钩住你"，成瘾性是这条主张的另一面。本库照录这处张力。**
- **他对自己转型时机的说法**（[00:25:37]）：离开对冲基金进入技术后，**"AI 浪潮发生时，我意识到我最好非常非常快地动，来确立这个领域"**，于是写了 AI engineering 那篇文章、办了这个会与媒体业务——**"我骨子里非常是个媒体人。"** ⚠️ **他另说"我确实有点怀念交易，但这个很充实，因为我能见到真人，而不是整天盯屏幕。"**

---

## ⚠️ 一期主持人姓名未出现在转录稿里的现场录制（2026-10-31，纽约 AI Finance）

来源：[Latent Space × Joseph Kim（OpenAI，ChatGPT 金融业务）](../videos/20261031-latent-space-openai-finance-joseph-kim-plugin-95-percent-taste-reward-model.md)

- ⚠️ **转录稿未给出主持人姓名**；在场的还有一位自称 **"Richard"、被介绍为 Latent Space editorial 负责人** 的共同主持。**本库不写定主持归属。**
- ✅ **而本库标注主持侧在这一期给出的唯一一处独立佐证，因为它正好对上嘉宾那条"审美判断上人比模型强"的说法**（[00:18:06]）：他点了 **Cognition 的 frontier code**——**SWE-bench 问的是"答案对不对"，而它问的是"你会不会 merge 这段代码"**，**"所以你能有好几个都能跑通的、像样的 PR，但哪一个你会 merge？这就是为什么你有时会看到'推理更少反而更好'的那种图，而它同时也是一个 taste benchmark。"**
- ⚠️ **另记一处主持侧的追问没有被回答**（[00:19:07]）：他指出投资判断**"常常是反主流共识的，否则就没什么拿到高回报的机会"**，⚠️⚠️ **而嘉宾整段回答讲的是目标模糊与验证周期长，绕开了这一点。本库记这是该期最该被追问而未被追问的两处之一。**
- ⚠️ **以及一处结尾的自我约束**：嘉宾冷开场里那句关于**"我们修好了预训练问题"**的断言，主持人在结尾点到了它，但随即把它当成留给 keynote 的**"面包屑"**，整期未展开（[00:27:11]）。

## ⚠️⚠️ swyx 第三次作为被访者，而这次提问者来自中国（2026-11-04，AIE 上海预热）

来源：[Latent Space × AIEi Shanghai](../videos/20261104-latent-space-swyx-aie-shanghai-kill-my-saas-entity-list.md)（提问者 **Galen Gao**，⚠️ **转录稿里从未被点名，全名取自视频简介**）

> ⚠️⚠️ **本库对这一期的定性**：**这是 AIE 上海（他自己的大会品牌在中国的首场）的预热节目，前两分钟是他自己录的开场导语。** ✅ **所有关于 AIE 规模、Latent Space 影响力与"Kill My SaaS"竞赛成果的数字全部为自述、无第三方来源，本库记为自述访谈而非独立访谈。**

- ⚠️⚠️ **本库认为他本期最有价值的一条是关于中美 AI 实务接触的机制，而本库此前没有同类材料**（[00:23:16]）：**"尤其对中国的实验室来说——其中有一些在实体清单上。他们不能正式和你开会。很多美国公司也不能正式和你开会。他们不被允许。他们甚至不回复你。那不是因为他们不想，而是因为他们不被允许"**；⚠️⚠️ **"但如果你们在同一个地点，你们就会撞见对方。"**
  - ⚠️ **而他对自己处境的表述同样具体**（[00:29:22]）：**"我连在中国设一个本地实体都做不到……我不想惹上麻烦，因为我的主营生意在美国。所以我不能和白宫惹上麻烦。"** ✅ **于是方案是纯加盟**：**"我是麦当劳，你是麦当劳中国。"**
  - ⚠️ **他在开场里对归属做了一次明确更正**：**"我没有把 AIE 带到上海。是上海把 AIE 带到了上海。"**
  - ⚠️ **本库标注这条的双重性**：✅ **它区分了"不想"与"不被允许"，并指出正式渠道被切断后剩下的通道是物理同场**；⚠️ **但它同时是一位会议主办方对自家产品价值的论证。**
- ⚠️⚠️ **一份由他作为买方做的 SaaS 克隆实验**（[00:29:22]–[00:38:27]）：**他把一个四万美元的采购提案改成一万美元悬赏开源克隆**，**结果**⚠️ **69 份提交、约 5 份"我们会付钱买"的水平、一周做完、两个月评审**。
  - ⚠️⚠️ **而那条机械化的威胁描述是本期传播价值最高的一句**：**"模型非常擅长点完你软件的每一个界面，然后独立地把它复刻出来"**→**"我一旦能访问你的软件，我就能克隆它。所以祝你好运。"**
  - ⚠️ **他明确划了界**：**"Salesforce 没问题，没人担心 Salesforce"**，**但中端、服务中小企业的 SaaS"会真的很难过"**；⚠️⚠️ **处方是两条出路加一个空心地带**：**成为某垂直里最顶的 agent（Harvey、OpenEvidence）／拥有专门数据当数据供应商／"在这两者之间的任何位置，都会有别人自己把它写出来"。**
  - ⚠️⚠️ **本库对这条材料的效力做了限定**：**它支撑的是"中端 SaaS 的议价权正在变化"，而不是"中端 SaaS 可被替代"**——⚠️ **他自己承认维护"不是零"、"有时候从一个经过检验的 SaaS 买确实会更好"，并明说"这件事我能做，是因为我是个 influencer。大多数人做不了，因为他们没有受众"。**
- ⚠️⚠️ **而本库认为本期最被低估的一句是关于自动评审的边界**（[00:39:28]）：**竞赛里 AI 评审"纯粹只判断你有没有提交一份有效的提交"，而不判优劣**，**理由是**——**"因为我们并不知道自己想要什么。所以我没法为我自己都不知道想要什么的东西做一个 AI 评审。"** ✅ **本库判这把边界划在"评分标准是否已经存在"上：资格校验可自动化因为判据事先写得出来，优劣评选不行因为判据是看过候选集之后才形成的。**
- ⚠️⚠️ **一个口径转换，本库判这是他本期最有用的一条商业观察**（[00:35:25]）：**"开发者的问题是说'哦，两百美元好多钱'。而我是个生意的所有者……十个员工我付他们一百五十万。如果他们协作得好 10%，那就是十五万。而它不是好 10%，是好五倍——那就是七百五十万。"**
- ⚠️⚠️ **一个可操作的"品味"定义，以及一条外部判据**（[00:59:38]–[01:01:39]）：**"从一个巨大的可能性集合里，你能又快又省地把它收窄到那个子集——而当你回头看时，那个子集立刻就显然是好的"**；⚠️⚠️ **而判据比定义更可操作**：**"当别人开始抄你刚发的那个东西，你就有品味。"** ✅ **他给的第二个例子落在"更无聊的问题"上：[Legora](legora-max.md) 的并行文档审阅——"任何人其实都能想到这个点子。点子很便宜——但你没做。Legora 做了。"**
- ⚠️⚠️ **对"为什么是 [Diogo](diogo-almeida.md) 成了"的三因归因，而前提是一个很强的承认**（[00:49:34]）：**"Diogo 不是第一个这么做的。此前已经有上千人试着说'小模型好'"**；**三条是 OpenAI 的可信度、system 1 / system 2 这个让沟通变清晰的框架、以及"在表演力和技术能力这两个维度上他都是 10 倍"。** ✅ **本库判这与他对品味的定义是同一论证：决定因素是收窄与执行，不是想法的新颖性。**
- ⚠️⚠️ **一条对 AI 评论者的启发式，而本库标注它也适用于他自己**（[00:19:14]）：**"有很多夸夸其谈的人，他们一辈子没写过一天代码……他们听起来全都一个样。都是'我到 AGI 的时间线是两年''你们将来都不会有工作了'。而很方便的是，接下来那件事看起来就是他们的工作。所以它非常自利。"** ✅ **配套的"工程师"定义很干净**：**"凌晨四点起来去修它的那个人，那才是工程师。"** ⚠️⚠️ **本库记下这条同样适用于他本人（他描述的未来恰好就是他的生意），而他在本期并未自我豁免——他明确说"我也是那个的一个小号版本"。**
- ⚠️ **零和 vs 正和：learn in public 的那条区分**（[00:08:05]）：**"金融是零和的。如果我知道一件事然后告诉你，那个真相就失去了价值。但在科技里大多数东西是正和的。"** ✅ **而那条反鸡汤限定本库认为比前半段更有价值**：**"仅仅因为你非常努力，你并没有被赋予获胜的资格。你必须非常努力并且很好。"**
- ⚠️ **三条"最期待"**（[01:06:43]）：**他主动跳过最明显答案（"system one models 显然是第一答案，所以它很无聊"），点的第一名是 interaction models（归于 Thinking Machines）——全双工、"我可以打断你，你会立刻回应并调整"**；**并列项是 continual learning 与 world models。**

> ⚠️⚠️ **本库必须标出本期的四处问题（详见[视频页](../videos/20261104-latent-space-swyx-aie-shanghai-kill-my-saas-entity-list.md)末节）**：
> **① 一条高度可争议且他没有给任何论据的国别论断**：⚠️⚠️ **"他们住错了国家……他们之所以没有更富，唯一的原因就是他们住在中国"**（[01:04:43]）。**本库照录为立场陈述、不采信，三条理由是单因归因且无论据、与他同期"他们在营销上很烂"那条自相冲突、以及把"好创业者"与"更富"当成可互换的量。**
> **② 三处建议/论证恰好把价值导向自己**：⚠️⚠️ **渠道诊断之后紧接"那就跟我一起做啊。就在（播客上）做，他们就会看见"**；**AEO 实验的结论恰好是自家播客排第一到第三**；**"实体清单导致不能正式见面所以需要同场偶遇"恰好论证自家大会的价值。** ✅ **本库把诊断与建议分开处理。**
> **③ Kill My SaaS 的成果口径在同一段里前后不一致**（先说"很多很糟的提交"又说"我们有 69 份好的"），**本库按分层理解为总提交 69 份、达采购水平约 5 份。**
> **④ 一处他自己点出却未处理的张力**：⚠️⚠️ **同一期里既说"默认假设应该是 AI 毁灭"，又说最担心的是"如果我们真有一个 AI 冬天……我会不会破产——对一家依赖炒作的会议公司来说，这是个真实的担忧"。** ✅ **两者指向相反的世界，而他没有把它们放在一起处理。** ⚠️ **本库同时标注那条 AI doom 表述与[他 2026-07-10 那次](../videos/20260710-latent-space-swyx-agent-labs.md)的差异：那次给的是带时间尺度的 pdoom（五万年约 90%、十年内近乎零、五十年约 5%），本期方向一致但去掉了时间尺度，因此更像立场表述而非可核对的估计。**

## ⚠️ 一期 keynote 后的现场采访，而主持人的两个提问比答案更有信息量（2026-11-08，GitHub Universe）

来源：[Latent Space × Jay Parikh](../videos/20261108-latent-space-jay-parikh-github-dependencies-harness-fusion.md)（⚠️⚠️ **厂商节目：受访者是 Microsoft CoreAI 的 EVP，本期几乎是同日产品发布的延伸**）

- ⚠️ **节目形态与利益披露**：**开场第一句就是"我们就在你的 keynote 之后录"**；**swyx 同时在筹办自己的会议（AIE Code，自述是"今年最后一场 AI 工程师大会、也是唯一完全聚焦编码 agent 的"），期内把 GitHub 侧称为长期合作对象、并把一位用户（[Peter Steinberger](peter-steinberger.md)）称作"我的讲者"。**
- ⚠️⚠️ **本库必须把两处口径与受访者分开记，因为它们出自 swyx 本人的开场独白、且无来源**（[00:00:00]–[00:01:00]）：**"GitHub 上大约 40% 的 pull request 是 agent 创建的"**、**"agent 总量在 6 个月里涨了 6 倍"**。
- ⚠️ **另记一处容易被误读的玩笑**：**"今年第一个达到 0 个 9 的可靠性的服务"是在拿 GitHub 的宕机开玩笑（zero nines），不是一个指标**；⚠️ **自动字幕把它写成 "09s"。** ✅ **他随后自己承认了这个立场的局限**："不过我们当中谁又能在宕机这件事上扔石头呢。"
- ✅ **而本库判这一期该记在本页名下的是两个提问，因为答案的价值主要来自它们的锋利程度**：
  1. ⚠️⚠️ **"开源供应链建立在'代码很贵'这个前提上"**（[00:17:15]）：**"也许现在代码很便宜了。也许安全评审其实也很便宜了，而实际上加固我们系统的最好方式就是把一切 vendoring 掉、或者把一切重写掉……然后就不依赖开源"**，并具体化成**"我的依赖是 2,000 个核心软件件，它们全都是可被攻击的表面积。也许我就把它们减到 20 个"**。✅ **本库判这个提法本身就是材料，而它换来了本库第一条正面反驳（受访者的"那 1,980 个现在得由我来维护了"）。** 🔗 **详见 [开源与基础设施](../topics/open-source-infrastructure.md)。**
  2. ⚠️ **指认了一个激励错位**（[00:20:19]）：**"你们展示的那些成本控制功能——那其实是实验室不做的事，因为他们希望你尽可能多花。"** ✅ **本库标注这条有用，因为它说明"帮客户少花钱"这个功能只可能出现在平台侧。**
- ⚠️ **他另递了两个受访者没有完全接的说法**：**① "代码已经不重要了"**（由一个全是 markdown 的仓库推出"语言占比不重要、什么是仓库、什么是代码"）→ **被受访者用存量挡回**；**② "pull request 的终结"**（引 Steinberger）→ **被归到配置项**。
- ✅ **本页另记他做的一处换算，因为这是他惯用的一种核对动作**：**对方说"每一秒都有一个开发者加入"，他当场答"我真得去查了一年有多少秒……那是 3,150 万"。**
- ⚠️ **本期提到一期本库尚未收录的访谈**：**"我们此前采访过 GitHub 的 COO"**（⚠️ **姓名在转录稿里写作 "Kyle Dagel"，本库不确证拼写，也未收录该期**）。
