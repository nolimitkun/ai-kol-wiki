# Periodic Labs（"Liam" 与 "Doge"）

**Periodic Labs** 是一家做**自治材料实验室**的"neo-lab"：把高通量实验、机器人、仿真（DFT / 力场）与 LLM 缝成一个闭环，目标自称 **synthesis superintelligence（合成超级智能）**，主攻方向包括**超导体**与**磁体**。实验室在**门洛帕克（Menlo Park）**，团队自述把固态化学家、固态物理学家、实验学家、理论学家、硬件工程师与 LLM 专家聚在一处，自比**贝尔实验室**。

⚠️ **本合页的人名口径**：本库唯一的一手材料是 [Latent Space 2026-10-08 那期](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md)，而**那期的自动字幕只播报了两位联合创始人的名、没有姓**——**"Liam"** 与 **"Doge"**（后者另有一处作 "Dar"）。⚠️ **本库不据外部知识补姓**。可确认的自述背景：**两人此前都在前沿实验室一侧**（谈 OpenAI / Google 时用的是"在那些大实验室里你没有这些资源，所以你必须出来自己干"这种第一人称口径），其中一位**自述读博时做计算/理论物理方向**。
⚠️ **本库此前在 [Beren Millidge 那期](../videos/20260911-dwarkesh-rsi-debate-schulman-millidge-oneill.md) 记过"Periodic Labs 的 Liam 在推特上讲过早期训练极稀疏 1T 模型"的一条转述，与上述背景一致，但本库不据此补姓。**

## 核心观点

- ⚠️⚠️ **公司论题（也是网站上那句话）**：**"智能是必要的，但不充分。新知识是在想法被发现与现实一致时创造出来的。"** 展开是 **"你不能只靠思考就想到一个解……再怎么重读那本教科书或论文、再怎么只是思考、消失在一个房间里，都不可能让你把所有可能的实验结果——预期的和非预期的——想清楚"**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [00:01:01]–[00:02:01]）。
- ⚠️⚠️ **这条论题最锋利的表述，也是本库在这条线上最该长期引用的一句**：**"即使 Fable 7 变得真的很好、比今天还好得多，你仍然必须跑实验才能拿到结果。原因是：机器学习非常擅长它被训练过的东西，而科学发现几乎按定义就是你没被训练过的东西。"**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [01:01:36]）
- ⚠️⚠️ **"按世界状态打时间戳"的 RL 环境构造法，以及它针对的 fake work**：用**"到这个日期为止的实验证据"**构造环境，问**"科学家接下来做的选择是什么"**；之所以必须这样做，是因为**预训练模型若已背下答案就会"假装在工作"——"它不需要做难的物理推理就能到达正确答案，然后你强化了那些不会泛化到新系统的推理策略"**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [00:13:05]–[00:14:05]）。口号版：⚠️ **"与其在科学的最终产出上训练，你是在做科学的过程上训练。"**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [00:59:36]）
- ⚠️ **科学与数学/代码的三条差异**：**RL 环境从物理实验室导出（"而这是我们的终极真值"）**、**不确定性下的决策（"东西从炉子里出来是不带标签的，连打标签都可能是随机带噪的"）**、**样本效率是硬约束（"不像数字环境，你没法任意加更多 rollout"）**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [00:04:02]–[00:06:04]）。
- ⚠️⚠️ **"full autonomy 是一个 non-goal"**：**"我们想从实验室拿到的是巨量的、高质量的、多样的数据。那些才是目标，而完全自治是一个 non-goal——我们是把自动化用在服务于那些数据目标上。"** 配套判断：⚠️ **"解决人形机器人其实会让我们更慢地达到我们的一些目标。"**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [00:51:32]–[00:52:32]）
- ⚠️ **"每一台设备都要有 140 IQ"**：动机是**操作机器形成的瓶颈**，而程序化采集**"对我们真正想要的东西来说有点太笨了"**；落点仍然是数据——**"如果你能在实验发生的那一刻做更智能的数据采集，那么你为未来 AI 系统准备的数据就会好得多"**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [00:47:30]–[00:48:31]）。
- ⚠️ **他们指认的头号瓶颈是自动化表征**：**"混粉末去试东西其实不难，但如果你没法表征它、分析它，然后智能地决定下一步，你从随机混粉末里得不到多少好处。"**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [01:04:38]）
- ⚠️ **压歧义的两条手段**：**先验（"热力学是最大的先验，然后物理是一个大的先验"）**与**多模态表征**；⚠️ **而他们给 AI 的定位很具体**：**"如果你同时给人类 10 种不同的模态、说一致地分析一下，那有点困难；但对 AI 来说这其实不算超级智能，它很擅长。"**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [00:25:15]）
- ⚠️ **对 DFT 的两条限定（本库这条线上最具体的一次）**：**"DFT 按定义不必是近似——Kohn–Hohenberg 定理表明它可以是精确的。但交换关联泛函我们还拿不到。"** 以及 ⚠️ **"即使我们有完美的 DFT，我还是认为我们需要一个实验室——因为我们也没法把 10²³ 个原子塞进计算机。"** 不能靠扩大 DFT 的两条硬限制是**微结构**与**超导温度仿真不了**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [00:34:21]–[00:37:26]）。
- ⚠️⚠️ **对"推理时计算能否替代训练"的一条反证**：**"把一切压缩进权重这件事仍然非常有价值。如果推理时推理就够了，所有前沿实验室都会在 GPT-4 那里停止训练。"**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [01:00:36]）而自训的真正理由是数据而非成本：⚠️ **"因为能拿到这些数据，你可以比某些前沿模型算力效率高得多。"**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [00:55:33]）
- ⚠️ **负结果与发表偏差**：**"人们通常只发表他们能合成出来的晶体，而通常不发表他们没能合成出来的"**；⚠️ **而他们对标注粒度给了一条修正——"按每个实验打标签大多是负的，但按每个 campaign 打标签就可能更平衡"**，主持人的收口是 **"所以你的推理轨迹几乎可以是跨整个 campaign 的"**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [00:56:34]–[00:58:36]）。
- ⚠️⚠️ **"文献的噪声底比 DFT 精度还差"**（自述，本库未核实）：**"不同的人、不同的实验室、不同的地方、不同的时间，这给结果引入了太多波动"**；指望是标准化工作流把噪声底压下去（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [00:53:32]–[00:54:32]）。
- ⚠️ **通往超导的路径论证**：难点不在想法而在合成——**"想出可能承载超导的化学空间并不难，真正难的是把它们合成出来"**；⚠️ **而那个 MgB₂ 的历史（"那个组试了 3 万种，其中 30 种看起来有意思"，而"二硼化镁作为前驱体在人们架子上放了几十年，BCS 理论 1957 年就有了"）被用来支撑题眼**：**"我们就是大幅增加了运气的表面积。"**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [01:22:55]–[01:23:55]）
- ⚠️ **商业化（本库第一次看到一家 neo-lab 把收入模式讲清楚）**：**自己是"零号客户" → 用 forward deployed 工程师驻场 → 重点在半导体行业**；⚠️ **主张是"让客户拥有他们自己的智能"（本地推理 + 在客户数据上训练）**；⚠️ **而定价的演化预测是"对结果定价（price outcomes）"**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [01:15:50]–[01:18:54]）。
- ⚠️ **"技术与资本深度纠缠"**：用**"2010–2015 的聊天机器人进展说不出来，而 2021–2026 是天壤之别"**做对照，机制是**"ChatGPT 做到了产品市场契合，而它彻底改变了资本格局"**；落点是**"我们想在物理世界里达成同样的事"**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [01:19:54]–[01:20:54]）。
- ⚠️ **一次对量子计算的祛魅，而它接回了本期主线**：**"人们谈如果你今天有一台量子计算机，你能把东西仿真得好得多；我就问他们：那你会仿真什么？你还是在仿真完美晶体——即使 DFT 在预测能力上是完美的，你还是有 DFT 有的那些问题。"**（⚠️ **他主动声明"我不是专家，我不理解"**；[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [00:46:30]）
- ⚠️ **组织原则：让有经验的人亲手做**：**"现代生活……尤其在学术界，当某人真的很擅长研究，我们就给他这么多写基金申请、教学的责任，以至于他们不再有时间亲手做研究"**；对照是**"Bardeen 每天都在实验室里，尽管他是理论学家"**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [01:13:49]）。
- **开源与资助**：贡献 **pymatgen / materials project 代码库 / custodian（DFT runner）/ torch-sim / JAX-MD**；另有**学术赠与资助项目**，首篇论文即将发表（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [01:20:54]–[01:21:54]）。

## ⚠️ 本页的两条限定

1. ⚠️⚠️ **本库的唯一一手材料里没有给出任何一个具体的材料发现成果**，而他们当时**正在宣布一轮大额融资**、**正在向半导体行业商业化**。✅ **方法论部分可独立评估**，⚠️ **但"自治实验室这条路有效"在本库里没有结果性证据支持**——唯一的一手结果性证据是**"AI 通过循环置换抓到了机器装载错误"**（[视频页](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md) [00:53:32]），而它证明的是数据质量管控，不是材料发现。
2. ⚠️ **几条量级断言全是自述或回忆，本库一条未核实**：文献噪声底比 DFT 差、那个日本组试了 3 万种、高通量实验与机械臂"只在最近三年左右被试过"。⚠️ **另有一条本库明确不作为数据引用**：**"我们离 Landauer 极限只有三四个数量级"**（主持人自述回忆、且他自己加了"大概""什么的"）。

## 与本库其它材料的关系

- ⚠️ **与 [Lila Sciences](lila-sciences.md) 构成本库最直接的一组对照**：两家都是"实验室即 verifier / token 生成器"，⚠️ **但 Periodic 明确说"完全自治是 non-goal"，而 Lila 的表述是"不做自动化最大化，做 token 生成/灵活性最大化"——方向一致，而 Periodic 把理由收得更紧（数据的量/质/多样性）**。⚠️ **另一处可直接并读**：Lila 说**"材料缺 sim-to-real、没有 AlphaFold"**，而 Periodic 这期由主持人引 Heather Kulik 把同一条说成**"不只是计算上没有，而是真值本身就不存在"**，并由嘉宾补上 **"我个人不知道有什么更好的方法来预测新材料的稳定性"**。
- ⚠️ **与 [Anima Anandkumar 的神经算子那条线](../topics/ai-for-science.md) 是互补而非竞争**：她在连续介质一侧主张"AI for science 不是语言模型"，而 Periodic 在离散/原子一侧仍然把 LLM 放在决策与表征位置上，把物理交给 DFT 与力场。
- ⚠️ **与 [ERA / John Platt](../topics/ai-for-science.md) 的"把科学问题映射成可打分任务"同形，但 verifier 不同**：ERA 的 verifier 多在计算侧，Periodic 的 verifier 是炉子与 XRD。

## 视频

- ["智能是必要的，但不充分"：自治实验室、synthesis superintelligence，以及"科学发现按定义就是你没被训练过的东西"（Latent Space，2026-10-08）](../videos/20261008-latent-space-periodic-labs-synthesis-superintelligence.md)
