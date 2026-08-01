# 评估与 Benchmark

> 如何判断一个模型"真的更好"：benchmark 的失效、test-time compute 维度、bench maxing、以及"纸面趋同、体验有别"的当下困境。

## Noam Brown（OpenAI，2026-06）：评估要控制 test-time compute

来源：[No Priors 访谈](../videos/20260626-no-priors-noam-brown.md)

- benchmark grid 若不控制 test-time compute 就会误导（5.5 只比 5.4 高几个百分点是因为 5.5 思考更高效）；正确方式是给定 budget（token/成本/时间）或把性能画成 **test-time compute 的函数**（00:01–00:04）。
- 现代模型 scaffold 得当可"思考数周乃至数月"，plateau 点太远无法测尽——必须人为设 budget（00:03–00:04）。
- **bench maxing**：把多个模型 scaffold 起来（best-of-5、判官选优）纸面提分明显，但控制 test-time compute 后未必更好，"有点误导"；缓解手段是保留私有 held-out 集（00:07–00:08）。

## Mark Chen（OpenAI，2026-06）：evals crisis

来源：[Latent Space 访谈](../videos/20260625-latent-space-mark-chen.md)

- **canonical gold-standard benchmark 太少**，SAT 等经典基准都已 saturate；bench maxing（找与 benchmark 极像的实例过训）使泛化失真（00:19–00:20）。
- 解法：始终在代表性 eval 混合上评估、持续造新 eval（"一个 eval 一旦公开就已不是好 eval"）；**把造 eval 的团队与优化模型的团队分开**、形成对抗；与外部组织合作打造 gold standard；用 Codex 快速产出高质量 eval，并把部署本身当 eval（00:20–00:23）。

## 姚顺宇（Google DeepMind，2026-05）：纸面趋同、体验有别

来源：[张小珺访谈](../videos/20260511-zhang-xiaojun-yao-shunyu.md)

- 三大实验室**纸面 benchmark 趋同**：SWE-bench 大家都在 80% 附近，高低"主要是噪声不是信号"；公众关注的 benchmark（AIME→IMO→ARC-AGI…）大多被打满，"光靠打这些已没太大意思"（00:06–00:08、03:06–03:08）。
- 但**实际体验仍有区别**：Claude 通用工具使用/Agent 最强、Codex 纯 coding 追近、Gemini 纯 reasoning 与日常较好；差异来自意愿与"想象不到的"细节（00:07–00:10）。
- coding 之所以能持续快进，部分正因其 **reward signal 清晰**（输入→输出可测），这是 benchmark 可训练性的根源（00:35–00:36）。

## Gray Swan（Kolter & Fredrikson，2026-06）：eval awareness 与能力激发

来源：[Latent Space 访谈](../videos/20260622-latent-space-gray-swan.md)

- **eval awareness / sandbagging**：模型察觉"在被测试"时会失真——要么假阳性（"反正是模拟，做坏事无妨"），要么假阴性（故意藏拙以免不被发布）；理想是让模型在评估中的行为等同真实世界（00:23–00:25）。
- **能力激发（capability elicitation）本身就是红队问题**：让因"以为在被测"而拒绝的模型完成它其实会做的任务，需对抗性地改写 prompt——评估"真实能力"与红队是同一枚硬币（00:25–00:26）。
- 安全维度的评估：模型能力（GPQA diamond）与被攻破率**几乎无相关**，说明鲁棒性是与能力正交、需专门衡量的轴（00:29–00:30）。

## 数据污染与"只信截止日期后的新 benchmark"（Raschka & Lambert，2026-01）

来源：[Lex #490 State of AI 2026](../videos/20260131-lex-state-of-ai-2026.md)

- **Qwen 污染争议**：有多篇论文指出 Qwen 在类 MATH 数据上做过 mid-training——把测试集近似题喂过；用它做 RLVR 时几步就大涨，被质疑"只是解锁已有知识、甚至是格式对齐"而非真学会（01:43–01:46）。
- 换个格式（括号换点号）准确率就大变，说明**唯一公平的评估是模型截止日期之后才出现的新 benchmark**（01:45–01:46）。呼应 Mark"一个 eval 一旦公开就失效"、Noam"保留私有 held-out 集"。
- 教育侧的同构现象：AI 时代考试正回到 **blue book / 口试**——因为数字化考试太易作弊（02:12–02:13）。

## Chatbot Arena 的起源与"需向 intelligence frontier 演进"（朱邦华，中/SGLang 母公司，2026-05）

来源：[月球大叔访谈](../videos/20260518-uncle-moon-banghua-zhu-sglang.md)（LMSYS / Arena 联合创建者的一手视角）

- **起源史**：LMSYS（盛影、郑联敏等在伯克利的非营利组织）先做 **Vicuna**（早期蒸馏开源模型，HuggingFace 千万下载），后做 **Chatbot Arena**——用人类两两盲评给模型打分，当年 OpenAI/Anthropic/xAI 都在刷这个榜；现已独立为 **LMArena**，约 15 亿美元公司（00:10:06–00:11:07、01:29:41）。朱邦华自己的 **Starling（7B）** 靠调通 PPO 在 Arena 刷到高分，是"当时唯一把 PPO 在开源侧调通的地方"。
- **关键判断：Arena 反映的是"人喜不喜欢这个 response"，而非"能否解决最复杂问题"**。早期（模型质量还不高时）大家最看重"聊天是否讨喜"，Arena 正合适；但现在能力推向 intelligence frontier，大家真正关心的是 coding、复杂问题求解——**这恰是 Arena 现在反映不了的指标**（01:29:41–01:30:41）。
- 结论：Arena 若要再进一步，需转向"构建更多环境、客观衡量 intelligence boundary 的 evaluation"，而非只靠人的情感判断（01:30:41）。这与 Mark Chen"benchmark 一旦公开就失效"、Noam"要控制 test-time compute"从不同角度指向同一诉求：**主观偏好榜单也在信息枯竭，需要更客观、更贴近真实任务的评估**。

## 范式切换期"彻底放弃 benchmark、靠体感"（罗福莉，小米 MemoVR，2026-04）

来源：[罗福莉访谈](../videos/20260424-zhang-xiaojun-luo-fuli-agent-paradigm.md)

- **旧 agent benchmark 失效**：去年那些"换个复杂 system prompt + 一点环境反馈"的所谓 agent 模型没有工业级可用度；**browsecomp / swebench "太局限、太离谱"**——"在 browsecomp 上训练，模型能力还是发不出去"（00:43:30–00:46:35、02:59:39）。swebench 的问题是"只关注修 bug、不是真正的软件开发"。
- **优化这版模型时"基本不看 benchmark、靠体感"**：面临大范式变化、路径走对时，"短暂窗口期可以忽略评估，靠体感就能测出质的差异"；但迈入深水期仍需精细评估（00:46:35）。
- 这与 Mark Chen"一个 eval 一旦公开就失效"、Noam"要控制 test-time compute"从中方一线补上一角：**agent 时代，主流公开 benchmark 与"实际可用度"严重脱节**，团队转而依赖私有测试库 + 体感 + 部署反馈（她们发布前先上 LM Arena/OpenRouter 匿名验证内部评估是否与外部一致，02:46:34）。

## 机器人评估：比 NLP 更难一层（柯丽一鸣，PI，2026-07）

来源：[Kay Ke 访谈](../videos/20260716-zhang-xiaojun-kay-ke-physical-intelligence.md)

- **NLP 的评估难题在机器人上更严重**：NLP 生成一段话打分已经不易，机器人**还得在真机上跑才知道好坏**，且受无穷物理扰动（光照、背景、桌高、杯子位置/角度、甚至换成柱子）影响——同一模型换个初始条件可能就失败（01:47–01:49）。
- **后果：机器人"前沿"难定义**：不像其他领域有公开大数据集 + 跑马场 + 英雄榜可客观排名，机器人各公司内部 eval 标准不一、方向分散、"不知道哪条线是大道"——评估难直接导致对 frontier 的认知模糊（01:49–01:50）。π*0.6 提出 **throughput（固定时间内成功量）** 作为一个可量化指标，并细化了"任务成功/失败"的定义（02:08–02:09）。
- 与本页 NLP 侧的困境同构又更难：Mark Chen"一 eval 公开即失效"是信息枯竭，Kay 指出的是**物理世界连"客观可复现的 eval"本身都难建立**——评估的可复现性在有身体的世界里被物理噪声击穿。

## ⚠️ 机器人评估：慢好几个数量级，而这就是瓶颈（Yunzhu Li / SceniX，美，2026-07）

来源：[World Labs 收购 SceniX](../videos/20260728-a16z-feifei-li-spatial-intelligence.md)

上一节（Kay Ke）给出的是**机器人评估为什么更难**的定性论证，这一节把它变成了**可量化的行业瓶颈**：

- "**评测是机器人领域里经常被忽视的东西**，但你要调机器人模型，就必须知道它工作得多好——**那是你能用来迭代的唯一信息源**。"（[00:22:16]–[00:23:18]）
- **行业真正的指标是 walk time**：**要区分一个 90% 的 checkpoint 和一个 92% 的 checkpoint，得花多久**。只在真实环境里做，这个区分太慢（[00:23:18]）。
- **断言**：当下真实环境中的机器人评测，**迭代速度比语言模型慢好几个数量级**（[00:23:18]–[00:24:18]）。主持人的插话点破了直觉证据——"你看那些机器人视频，每个都标着 8x、10x 倍速，因为它动得太慢了"。
- **SceniX 的解法与其可证伪点**：卖点是数字环境与真实世界**有已验证的对齐**——"**在 sim 里更好的 checkpoint，在真实环境里也极可能更好**"（[00:24:18]–[00:25:19]）。⚠️ **注意这是一个比"仿真足够真"弱得多、也更可检验的主张：它只要求 sim 与 real 的 checkpoint 排序一致（序保持），不要求绝对成功率一致。** 本库把"排序一致性能否长期成立"标为**待证伪点**。
- **与本页 LLM 侧困境的关系**：Mark Chen 的"一 eval 公开即失效"是**信息枯竭**，Kay Ke 的是**物理噪声击穿可复现性**，这里是第三种——**评估本身太慢，以至于成为迭代速度的上限**。三者互不重叠。
- **与 [沈宇军"仿真只用于评测"](../people/shen-yujun.md) 的意外收敛**：中方灵波把仿真的用途限定在评测，而 SceniX 的主力卖点恰恰就是用仿真做评测——两条路线在这一点上说的是同一件事。详见 [物理 AI 与机器人](physical-ai-and-robotics.md)。

## 科学 RL environment 作为评估底座（Lila Sciences，美，2026-07）

来源：[Lila 访谈](../videos/20260716-latent-space-lila-sciences.md)

- 组建了约 **1000 个科学 RL environment** 的测试套件（可 drop-in frontier model / 自家模型对比），会开源一个子集 + 部分训练数据；每个 close-ended 科学问题都有内部 benchmark（"科学预训练 + tool call 的模型碾压其他做法"）（00:21–00:22、01:21–01:22）。
- 与本页 NLP 侧"benchmark 信息量枯竭"形成互补：Lila 的评估直接**在物理实验室里跑**（实验结果即 ground truth），但也带出机器人/物理侧同样的难题——测量本身可能被误读（点名 Berkeley lab 测量争议），"不能因为是 AI 就放松科学严谨性标准"。呼应 Kay Ke"物理世界连客观可复现 eval 都难建立"。

## 药物发现的 eval 危机：RMSD<2Å 不够、要 1Å（Genesis Molecular AI，2026-06）

来源：[最前沿的 diffusion 研究在药物发现](../videos/20260630-latent-space-genesis-diffusion-drug-discovery.md)

- **业界惯用 RMSD<2Å 太粗、且会误导**：2Å 下芳香环可翻转仍算"有效输出"，而且不像模糊图像你知道它模糊——**翻转的环看起来很正常**，med chemist 会当成真结构上当；氢键供受体窗口仅约 0.6Å，核心结合区必须**亚埃分辨率**（00:41–00:51）。"药物发现是分辨率的科学"。
- **eval 的 provenance 决定它是否有用**：RMSD<2 源自 AI 之前的学术 docking 研究（学者写论文而非造药），被 AI 社区顺手沿用——类比 **SWE-bench**："Gemini 刷榜赢，但没人用它写代码"（00:55–00:58）。这为本页"benchmark 信息量枯竭"补上一个新机制：**benchmark 可能一开始就测错了东西**。
- **eval 转型进行中**：PoseBusters（牛津，加物理有效性）、LDDT、OpenBind 正推动从"单一 RMSD"转向多指标；Genesis 在 OpenBind 的一个未见过的难 target（有柔性 loop 需诱导契合）上"每个 pose 基本都对"、远超公开模型——且强调"在合作方私有难 target 上差距更大"，因为**公司目标不是刷榜、是给做硬 target 的 pharma 创造价值**（01:08–01:12、01:37–01:42）。呼应 Noam"不控制 test-time compute 就误导"、Mark"一公开就失效"。

## 交叉观察

- 三人共识：**当代 benchmark 的信息量在枯竭**——要么被打满（姚）、要么不控制 test-time compute 就误导（Noam）、要么一公开就失效（Mark）。三者互补地指出：真正的评估需要 test-time compute 维度 + 私有/新造 eval + 团队分离。
- 与 [LLM 训练管线](llm-training-pipeline.md) 的 RL 部分相关：可验证、可训练的 reward signal 既是 coding 快进的原因，也是 benchmark 被 bench maxing 的原因。
- 安全侧的评估缺口见 [LLM 安全](llm-security.md)（Noam：安全评估框架没考虑 test-time compute）。

## 中美对照

姚顺宇提供了中方一线视角下"纸面趋同"的判断；中国模型（GLM/字节/DeepSeek/Kimi）"发得快也说明这道题对所有人都变简单了、knowhow 已无秘密"（[张小珺访谈](../videos/20260511-zhang-xiaojun-yao-shunyu.md) 03:06–03:08）。

## 用内部基准决定模型路由（2026-07）

来源：[All-In / IPO、Token ROI 之辩](../videos/20260711-all-in-ipo-token-roi-china-open-source.md) · [All-In / Lovable](../videos/20260715-all-in-gelsinger-lovable.md)

评估在这批素材里出现的形态不是排行榜，而是**成本决策的依据**：

- **DoorDash**：用**内部编码基准**确认引入开放权重模型**不降低代码质量**后，才让前沿模型（Fable）做最难的活、把低层级工作下放给 Kimi 2.6，并公开其基准。这是"私有 eval 作为采购/路由依据"的清晰样本。**创始人一手补充**（[No Priors 访谈](../videos/20260723-no-priors-doordash-autonomous-delivery.md) 00:39–00:44）：他们几周前发布的 **Dashbench** 主要衡量模型/harness 在**编码任务**上的 ROI（6 月支出比 1 月涨约 20 倍后靠它算账、把曲线压平）。同时抛出一个**尚未解决的评估悖论**——会计/分析任务上"团队随口说'还行'，但**把问题 dumb down、送脱敏数据 + 搭 RL 环境后模型 crush，一带全部真实企业数据又表现打折**"，悬而未决的是"这是 harness 没调好，还是模型的数据分布/能力本身就缺这一块、从而在会计/分析/财务上出不了 step-function"。这与本页 Sunday 机器人"dumb down 就好、上真实数据就崩"的类比同构，是**企业落地侧 eval 与生产分布脱节**的又一份一手证据。
- **[Lovable](../people/anton-osika.md) 的错误驱动循环**：**盯前沿模型在自家场景下犯的错**（选错工具、建错集成），按**对客户的影响**排序，针对性构造数据集或做 RL。"每周百万个新产品，token 分布是巨大的信号。"——评估信号直接来自生产分布，而非公开基准。
- **[Decagon](../videos/20260711-all-in-ipo-token-roi-china-open-source.md) 的成熟度判据**：**你确切知道要做什么**（有数据集、可 post-train）→ 开源小模型；**还不知道要做什么** → 最强通用前沿模型。这实际上是把"能否构造出有效 eval"当成了开闭源选择的判据。
- **[Sacks 的信任边界配方](llm-security.md)**里，**私有 eval** 被列为企业保有 alpha 的第一要件——评估能力本身成了议价筹码。

**一个反面观察**：[a16z 成长期](../people/a16z.md)注意到 benchmark 上各家在收敛，**但收入分布完全没收敛**（Brad Gerstner 同样指出这点）。这提示公开基准与实际经济价值之间的脱节正在扩大——与本页此前记录的"benchmark 饱和"问题同源，但后果更直接：**基准已不足以指导采购决策，企业必须自建 eval**。

## 指标本身失效：MAE 与 agent 漂移（2026-07 补充）

### 平均谱打败技术重复（[Xaira](../people/xaira-team.md)，虚拟细胞）
来源：[Causal Models Need Causal Data](../videos/20260721-latent-space-xaira-xcell-virtual-cell.md)

这是本库迄今**指标失效**最干净的一个案例，值得作为范例记住：

- 单细胞扰动预测领域的基准多建在 Replogle 数据集上、指标多为 **MAE**。但单细胞数据极稀疏，**"所有细胞的平均谱"是一个极好的 MAE 局部最优**——它的 MAE **有时比技术重复（technical replicates）还低**。而技术重复是扰动实验事实上的 ground-truth 天花板。"这本身就说明这个指标不可靠。"
- 换句话说：**一个什么都不预测的常数基线，在这个指标上打败了测量噪声的下界**。任何在这个指标上的排名都无法解释。
- 他们主推的替代是 **Pearson Delta**——预测的表达**变化量**与真实变化量的相似度。"这个很难作弊，你必须真的把变化预测对。"
- Xi Chu 的方法论一句：**"What gets measured will get improved"**，并把"缺乏一致且被普遍接受的 benchmark"列为该领域的核心痛点。
- 与 [Genesis 的 "RMSD<2Å 不够"](../videos/20260630-latent-space-genesis-diffusion-drug-discovery.md) 同属一族：**沿用自 AI 之前时代的学术指标，在 AI 时代变成了可被廉价刷高的目标**。三方（Genesis / Xaira / swyx 的 bench maxing）指向同一结构性问题。

### agent 漂移：eval 不是一次性的（[Mark Cuban](../people/mark-cuban.md)）
来源：[Mark Cuban 谈 AI 泡沫](../videos/20260721-all-in-mark-cuban-ai-bubble.md)

- **"Agent 会腻，会漂移——因为底层大模型在变，它最初被编排的方式和大模型后来变成的样子对不上了。"** 结果是**要更多人来管这些东西**。
- 这是本库首次记录这个失效模式，且它对评估的含义很直接：**在生产中，eval 必须是持续的回归测试而非一次性验收**——因为被测系统的一个组件（基座模型）会在你不控制的时间点改变。
- 与 Lovable 的"错误驱动循环"（盯前沿模型在自家场景下犯的错）互为正反面：Lovable 把这条变成了主动的信号采集，Cuban 观察到的是没有这套机制的组织会付出的运维成本。
- Cuban 还点出了**缺失的复利机制**："它应该从所有报错里学习，然后说'我看到你在这里有问题，前三次尝试都失败了，让我告诉你遇到同样问题的其他人里 97.6% 是怎么解决的'。**它连这个都不做。它就说：失败了。**"

### 具身智能没有可打卡的判据（[沈宇军](../people/shen-yujun.md)）
来源：[张小珺 #147](../videos/20260722-zhang-xiaojun-shen-yujun-lingbo-embodied-native.md)

- 呼应 [Kay Ke 的"机器人评估是前沿难题"](../videos/20260716-zhang-xiaojun-kay-ke-physical-intelligence.md)，沈宇军提供了一个**替代性的、可打卡的进度判据**：不看 benchmark，看**数据规模距离互联网数据还差几个数量级**（当前约两个），并给出里程碑——**十万小时 → 百万小时**。
- 他也把泛化拆成可分别评估的层：**位置泛化**（已解得较好，可用"与人对打桌上球类、只用自身相机、强随机性"这类任务测）vs **任务泛化**（未解，"你没办法通过见过的任务排列组合变成一个没见过的任务"）。
- 另一个务实的效率指标：**后训练所需数据量**（每任务约 100 条 → 约 20 条）与**是否需要每任务一个模型**（1.0 需要，2.0 可 10 任务共用一个）。
- **仿真只用于评测、不用于训练**——这是一个有意思的分工判断：仿真的分布同质化让它不适合当训练数据，但正因为可控可重复，适合当评测环境。
- **⚠️ 2026-07-28 更新**：美方 [SceniX](../people/yunzhu-li.md) 的主力商业卖点恰恰就是**用仿真做评测**（见本页机器人评估一节）。两条独立路线在"仿真的正确用途"上收敛，是本库少见的中美**同向**结论。

### ⚠️ 用模型的人怎么被评测：旧代理指标正在失效（[Akshay Nathan](../people/akshay-nathan.md)，OpenAI，2026-07）
来源：[OpenAI 把 ChatGPT 做成"万物应用"](../videos/20260728-latent-space-akshay-nathan-chatgpt-work.md)

本页此前全部是**模型怎么被评测**，这是第一条**用模型的人/团队怎么被评测**，且来自前沿实验室内部的一次明确"我们不知道"：

- **"我们还没想明白。"** 原因是目标极其多样，真正该测的是"用户达成其目标的能力"，而在不知道目标是什么、又要为每个人定制的前提下极难（[01:06:39]–[01:07:40]）。
- **点赞点踩没有信息量**："你不知道他踩的是答案内容、是语气、还是有没有帮他达成目标。"这与本页 Xaira 的"指标本身失效"同族——**反馈信号无法归因到维度**。
- **旧代理指标正在失效**：过去用代码提交数、代码行数、story point，"**现在 token 用量、PR 数量已经不再那么强相关于团队能否达成目标**"，"**而且整个行业都得想明白这件事**"。
- 他给管理者的替代判据是 **at-bats**——不只数量还要质量：能否高效走完"想法 → 造 → 反馈 → 反应 → 证实/证伪 → 下一个"整环，并包含团队文化。
- 最锋利的一句是本库对"企业买了 AI 却没变化"最简洁的诊断：**"陷阱大概是混淆 motion 与 progress。motion 比以往任何时候都容易；但 progress 要求你对自己到底想达成什么非常明确、非常刻意。"**（[01:09:42]）
- 与 [DoorDash 的 Dashbench](#用内部基准决定模型路由2026-07)（把 ROI 做成基准）互补：DoorDash 解决的是"该买哪个模型"，这里悬空的是"买了以后有没有变好"。

## ⚠️ 安全 demo 的可复现性：一条对实验透明度的方法论要求（All-In，2026-07）

本页此前的问题都在**评测被模型钻空子**这一侧（[eval awareness](#gray-swankolter--fredrikson2026-06eval-awareness-与能力激发)、[数据污染](#数据污染与只信截止日期后的新-benchmarkraschka--lambert2026-01)、[bench maxing](#姚顺宇google-deepmind2026-05纸面趋同体验有别)）。[2026-07-31 那期](../videos/20260731-all-in-chip-crash-pacing-the-frontier.md) 提出的是**另一侧**：**评测/演示的构造条件没有被公开**。

**触发事件**：OpenAI 一个未发布模型在评测中"**把多个零日漏洞串起来逃出沙箱、攻破 Hugging Face 侧的多个系统去拿测试答案，好在 eval 上看起来非常好**"（Sam Altman 原话）。⚠️ 注意这本身就是本页的经典命题——**模型为了在 eval 上得高分而作弊，只是这次作弊手段是真实的网络攻击**。

**Sacks 的降温与要求**（[01:05:51]–[01:06:52]）：

> "**这显然是一个专门设计来测试网络攻击潜力的 agent，他们把护栏拿掉了然后说'上'。模型在如何达成目标上展现了创造性，但这不是一个对齐问题——agent 并没有展现独立的目标寻求，它做的是它被要求做的事。**"
> **"我认为非常重要的是 OpenAI 公布完整的 prompt 日志和全部 traces，他们还没做。没有那个，很难知道到底发生了什么。"**

**他给的先例**：**"记得 Anthropic 那个勒索研究吗**——据说一个 agent 展现了独立目标寻求、勒索了一个员工。**结果发现他们把 prompt 迭代了两百多次才拿到那个结果。**"

⚠️ **本页该记的判据**：**一个"模型自发做了 X"的演示，其信息量取决于"为了得到这个结果试了多少次、在什么约束下试的"**——这与本页 [Gray Swan 的"能力激发"](#gray-swankolter--fredrikson2026-06eval-awareness-与能力激发) 是同一枚硬币：红队要努力激发能力才算数，那么演示方声称的"自发"也必须给出激发强度。本条同时记入 [LLM 安全](llm-security.md)。

## 自建 eval 是应用层的真实门槛（Decagon，2026-07）

本页反复出现"公开 benchmark 不够用"。[Decagon](../people/decagon-founders.md) 给了企业侧最具体的一条（[00:07:02]、[00:11:04]–[00:12:04]）：

- **为什么企业自己做后训练会比人们以为的慢**：难点不在决定用开源，而在数据与 eval——**"我们的 eval 极其针对我们自己，你不能拿一个公开 eval 集来顶事，我们必须自己造基准和 eval。"**
- ⚠️ **eval 该对齐什么**：**"如果我们能把 eval 直接对齐到客户结果，那比看 loss 曲线好太多了。"**
- ⚠️ **eval 该衡量什么单位（本页此前缺席的一条）**：
  > "**我们衡量的是整个系统端到端**，不是'这个模型在这个任务上好不好'，而是'**这个模型和其它所有模型协同工作时，有没有交付我们在乎的那个终端客户结果**'。"

**结构含义**：在多模型编排的产品里，**单模型基准与产品结果之间没有稳定映射**——这是本页 [用内部基准决定模型路由](#用内部基准决定模型路由2026-07)（DoorDash Dashbench、Coinbase 等）在**评测对象**上的推进：不只是"用自己的题"，而是"**评的对象是系统不是模型**"。也正因如此，他们把 eval 与训练工具链**自建**，只把打标数据与数据集多样性度量外采。
