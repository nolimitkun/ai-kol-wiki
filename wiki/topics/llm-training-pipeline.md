# LLM 训练管线

## 共识框架（以 Karpathy 2023-11 的表述为基线）

1. **预训练**：~10TB 级网络文本 + 数千 GPU × 数周 → base model。本质是互联网的有损压缩（压缩比 ~100×）；成本数百万至数亿美元，一年只做一两次。
2. **监督微调（SFT）**：换数据不换算法——用 ~10 万条高质量人工问答对训练，"质量优先于数量"，得到 assistant model；成本低到可以每周迭代。
3. **RLHF（可选第三阶段）**：利用"比较比撰写容易"的原理，用偏好对比标注进一步提升。
4. 标注正从纯人工走向人机协作，人趋向监督角色。

（来源：[Karpathy, Intro to LLMs](../videos/20231123-karpathy-intro-to-llms.md) 00:14–00:23）

## 教科书类比（Karpathy 2025-02 的框架）

预训练 = 读正文阐述（建知识库）；SFT = 学例题的完整解法（模仿专家）；RL = 做课后练习题（只给答案，自己发现解法）。人类标注员写不出对 LLM 最优的解题路径——"它的认知与我们不同"——所以 RL 必不可少。RLHF 用奖励模型把 RL 扩展到不可验证域（写作等），但奖励模型可被博弈，"RLHF is not RL"：只能跑几百步的微调，缺少可无限投算力的魔法；可验证域（数学/代码）才能像 AlphaGo 一样无限跑 RL 并可能超越人类（move 37 的开放域等价物）。（[Deep Dive into LLMs](../videos/20250205-karpathy-deep-dive-into-llms.md) 02:11–03:06）

数据侧细节（FineWeb：44TB / 15T token）、GPT-2 复现成本从 $40k 降到 $100–600 等见同视频 00:01–00:34。

## 第三阶段的演进：RL 与思考模型

Karpathy 2025-02 的更新表述：训练管线已是 **预训练 → SFT → 强化学习** 三段。RL 阶段让模型在大量数学/代码题上"刷题"，自己发现有效的思考策略（尝试、回溯、检验假设）——这些策略难以由人工标注硬编码，只能靠 RL 涌现。这是近一两年的大突破，DeepSeek R1 是首个公开系统阐述的工作。产物即"思考模型"（o1/R1 等），在难题上用推理时间换准确率。（[How I use LLMs](../videos/20250227-karpathy-how-i-use-llms.md) 00:22–00:25）

这正好接上他 2023-11 预言的 System 2 方向（见 [LLM OS](llm-os.md) 开放问题）——两年内从"没有模型具备"变成行业标配。

## 训练成本与数据质量（Karpathy 2024-06 的实证）

复现 GPT-2 124M 的成本从 2019 年的 ~$40,000 降到 2024 年的 $10 级别（8×A100 约 2 小时）。更重要的发现：**数据质量 > token 数量**——在 FineWeb-EDU（LLM 自动做教育质量过滤）上只训 10B token 就超过原版 GPT-2（100B token）的 HellaSwag 成绩，约 10 倍学习效率。他还实测 GPT-3 论文的超参"极其保守"，max LR 放大 3 倍仍收敛更快。工程侧结论："深度学习负载多数是 memory-bound——flops 不重要，内存访问模式才重要"（FlashAttention 多算 flops 反而快 7.6 倍）。（[Let's reproduce GPT-2](../videos/20240609-karpathy-lets-reproduce-gpt2.md) 00:02、01:48–02:14、03:44–03:51）

## Scaling Laws

Karpathy：性能是 N（参数）和 D（数据）的平滑可预测函数，无饱和迹象；"算法进步是很好的加分项，但扩大规模是有保证的路径"——这是算力竞赛（"Gold Rush"）的根本驱动。（同上 00:25–00:27）

Jensen Huang 2026-03 的扩展表述：**四条 scaling laws**——预训练（数据靠合成续命，"人类互相教学的数据本来就是合成的"）、后训练、test-time（"思考很难，推理必然算力密集"）、agentic（spawn 子 agent 团队）；agent 的经验回流预训练形成循环。"智能最终只随一个东西 scale：算力。"（[Lex #494](../videos/20260323-lex-jensen-huang-nvidia.md) 00:22–00:28）

## test-time compute 作为新的 scaling 维度（Noam Brown，OpenAI，2026-06）

来源：[No Priors 访谈](../videos/20260626-no-priors-noam-brown.md)

- 模型能力如今是**投入金钱（compute）的函数**：$10 → $10K → $10M 能力递增；scaffold 得当可"思考数周至数月"而不 plateau。这把"推理时算力"确立为 pre/post-training 之外的独立 scaling 维度（00:03–00:04、00:12–00:14）。
- 但**不认为会隔夜 hard takeoff**：正因为最强能力依赖大规模 test-time compute，时间本身成为瓶颈——渐进 takeoff（00:25–00:27）。呼应 Jensen 的"test-time 是第三条 scaling law""推理必然算力密集"。

## Reasoning/o1 这个 bet 与 pre-training 未死（Mark Chen，OpenAI CRO，2026-06）

来源：[Latent Space 访谈](../videos/20260625-latent-space-mark-chen.md)

- **坚信 scaling laws、pre-training 未死**："pre-training is dead"叙事反复出现却每次被突破，已 hold 近 10 个数量级（00:08–00:10、00:37–00:38）。
- reasoning/o1 是"曾被质疑最终成立"的最大 bet：当时 pre-training + post-training 是舒适范式，靠 Yakub、Ilya 的 conviction 才推上这条路（00:09–00:11）。

## 中方一线视角：预训练没到头、后训练分水岭（姚顺宇，2026-05）

来源：[张小珺访谈](../videos/20260511-zhang-xiaojun-yao-shunyu.md)

- **预训练 Scaling Law 没到头**：过去几个月预训练反而变强，未来 4 个月也没看到到头迹象；觉得"撞墙"的人**多半是自己代码里有 bug**（另两种是误判适用范围、或数据等条件被认为撞墙）。关键不是玄学而是"做事系统"——合理 ablation 排查（00:24–00:30）。这与 Mark Chen"pre-training 未死"直接呼应，但姚给出了"撞墙=bug"的更强判断。
- **后训练 scale up 的分水岭是 Claude 3.7**：3.7 之前后训练是小规模修补，之后才 scale up；关键要素是"合适环境 + 清晰回馈信号 + 强数据源 + 训练稳定"。各家（OpenAI 草莓 Strawberry、Anthropic、DeepSeek）大方向一致但**具体实现差别很大、都能做成**（02:12–02:14、01:42–01:43）。
- **pre-training 是 RL 的子集**：预训练/SFT/RL 无本质算法区别，最大区别在数据分布——预训练要分布广、质量可不极致；后训练分布窄但质量要求极高（03:00–03:02）。
- 驱动力：算力与数据强关联；算法作用是**相变式**的（Transformer 那种"从不能到能"的跳变后，是平滑提效）（00:31–00:33）。

## 全景盘点：三条 scaling、mid-training 与"RLVR 可 scale、RLHF 不能"（Raschka & Lambert，2026-01）

来源：[Lex #490 State of AI 2026](../videos/20260131-lex-state-of-ai-2026.md)

- **架构自 GPT-2 几乎没变**，真正进展在训练配方与系统：MoE/MLA/GQA/RMSNorm 都是"旋钮"，FP8/FP4 带来速度而非新能力（00:37–00:47）。
- **pre / mid / post-training**：mid-training 是"更专门的预训练"（长上下文、把最高质量内容放最后以抗灾难性遗忘）；**合成数据 ≠ 坏数据**（OCR 抽 PDF、改写成 QA、用 ChatGPT 优答训练），**数据质量 > 数量**——前沿实验室"想有影响力最好的方式就是找更好的数据"（01:03–01:14）。
- **RLVR 词源**：Nathan 团队在 **Tulu 3** 造词，DeepSeek 做出训练突破；可验证奖励（数学/代码）→ rubrics/LLM-as-judge 拓展到开放域；aha moment 其实是**放大预训练里已有的自我纠错行为**（01:37–01:42）。
- **关键定律：RLVR 可 scale（log 训练算力→线性性能，o1 首次展示、DeepSeek 复现），RLHF 不能**——RLHF 的开山之作恰是"reward model 过优化的 scaling law"；故大算力应投 RLVR，RLHF 只作收尾/风格（01:19–01:20、01:55–01:57）。下一步押注 value function / process reward model（"RLVR 2.0"）。
- **serving 成本 >> 训练成本**：DeepSeek 预训练传闻 ~$5M、OLMo3 ~$2M，但服务上亿用户是数十亿美元级——解释了模型为何反而变小（00:51–00:53）。呼应 [AI 算力与基础设施](ai-infrastructure.md) 的吉瓦集群与 test-time 经济性。

## RL 的样本效率：MCTS vs policy gradient（Eric Jang，前 DeepMind Robotics，2026-05）

来源：[Dwarkesh 访谈](../videos/20260515-dwarkesh-eric-jang.md)

- 从零重建 AlphaGo 后反观 LLM RL：**MCTS 给每一步提供监督目标**（低方差），而 LLM 的 policy-gradient RL 是把整条获胜轨迹所有 token 一起上调——即 Karpathy 的"**用吸管吸取监督信号**"，一局里真正有效的信号极少（01:24–01:28、01:45–01:46）。
- **bits per FLOP 框架**：学习速度 = 每 FLOP 样本数 × 每样本比特数。长程 RL 让前者下降（要展开数天工作才得一个信号），后者也远逊监督学习（未训练模型要在 10 万词表里瞎猜约 10 万次才撞对一次），故绝大部分训练时间耗在"低通过率区"几乎不学习（02:12–02:17）。这为"RL 阶段只能跑几百步 / 需良好初始化"提供了量化解释，接续 Karpathy 的"RLHF is not RL"。
- **AlphaGo 优雅在于永不从 0% 成功率起步、不解探索难题**：全程"在改进标签上做监督学习"，训练稳定、无需 on-policy 分布式基础设施；且训 policy 模仿 MCTS 的**整个分布**（软标签熵高）——正是**蒸馏高效**的原因（02:18–02:21）。与 [姚顺宇](../people/yao-shunyu.md) 的软蒸/硬蒸、[中美 AI 生态对照](china-us-ai.md) 相通。
- **前向搜索为何难迁移 LLM**：语言动作空间过大，几乎不会两次采样同一子节点，PUCT 探索启发式失效；但"前向模拟未来估价值"可能以别的形态回归（01:44–01:49）。
- 另可对照 Andy Jones《Scaling Scaling Laws with Board Games》(2021)：**搜索算力可换训练算力**，提前预示了 test-time compute（见 [评估与 Benchmark](evaluation-and-benchmarks.md)）。

## RL 的三模块与"奖励函数即传达意图"：机器人视角（柯丽一鸣，PI，2026-07）

来源：[Kay Ke 访谈](../videos/20260716-zhang-xiaojun-kay-ke-physical-intelligence.md)

从机器人 RL 一线给出与 LLM RL 互补的 RL 本质拆解：

- **RL = 三个模块拼起来**：**探索**（选大改动还是小改动——她认为当前大模型缺乏主动探索能力）、**归因/credit assignment**（π*0.6 从大量部署数据里找"整条轨迹里哪一步是精华、值得多做"）、**奖励设计**（02:45–02:50）。这与 Eric Jang 的"MCTS 每步给监督 vs policy-gradient 整条轨迹一起上调"是同一 credit-assignment 难题的两种表述。
- **"奖励函数"应重新框定为"向智能体传达你要它做什么"**：奖励函数只是表现方式之一，可验证任务（代码能跑）可独立于奖励函数存在；奖励易被 abuse（超级马里奥 RL 找 bug 直接触发最大奖励）——好的"奖励"应因地制宜、可泛化、需人的 common sense 先验（02:50–02:52）。与朱邦华"RLVR = 可客观验证的 reward"、洪乐潼"AI for Math 优化可验证性"同频。
- **experience data / RECAP（π*0.6）**：让智能体在真实世界收集**自己做任务的体验数据**放回训练池，超越固定的人类演示数据——在机器人叠衣服上超越了最好的人类数据收集员。启示：真机 RL 的数据可由训好的模型自己 rollout 收集（去掉遥操作员）大幅降本（01:58–02:01）。这是 Eric Jang"长程 RL 样本效率低、监督信号稀疏"在机器人侧的正面解法尝试。

## RLHF vs RLVR 与 PPO 的工程暗坑（朱邦华，中/SGLang 母公司，2026-05）

来源：[月球大叔访谈](../videos/20260518-uncle-moon-banghua-zhu-sglang.md)（RL 理论博士 + 一线 RL infra 视角）

- **RLHF vs RLVR 的分工**：RLHF（Human Feedback）训 reward model 让模型"更像人/更 align"（GPT-3.5 后"更有人味"即来自此）；**RLVR**（Verifiable Reward）针对可客观验证的数学/代码/agentic，是模型工具化（CodingAgent/WebAgent）的关键范式（00:36:42–00:38:44）。与 Raschka & Lambert"RLVR 可 scale、RLHF 不能"互补。
- **DeepSeek V3 是 RLVR 转折点**：证明"直接从 pre-trained 点做 RLVR 就能大幅提升 intelligence"，让业界（含 NVIDIA）意识到 RL 重要性——推翻了"只做 SFT 就够"的旧认知（00:35:41）。
- **PPO 上限远高于简化算法（DPO/GRPO），关键在工程 trick**：如 critic（value function）不能随机初始化直接上（loss 极高会把 policy 更新到错误方向、把模型破坏到救不回来），要先 **warm up critic** 再初始化 PPO（00:31:37–00:33:38）。"调通靠 intuition + 系统性排 infra 暗坑，不是理论"——呼应 [姚顺宇](../videos/20260511-zhang-xiaojun-yao-shunyu.md)"撞墙多半是代码有 bug"。
- **pre-training 洗数据未撞墙**：更多高质量 coding data 仍能推能力边界；SFT 像对 pre-training 的小 fix；RL/post-training 是把能力推到 pre-training 定义的边界 + on-policy distillation 合成 generalist（01:09:21–01:11:25）。与姚顺宇"预训练没到头"一致。

## 后训练前移到 Agent、卡的分配与架构决策（罗福莉，小米 MemoVR，2026-04）

来源：[罗福莉访谈](../videos/20260424-zhang-xiaojun-luo-fuli-agent-paradigm.md)（前 DeepSeek，现小米大模型负责人）

- **后训练范式从 Chat 前移到 Agent**：要让模型在 Claude Code / OpenClaw 等众多复杂框架上都稳定，后训练必须以"在复杂 agent 框架里端到端完成长程任务"为目标，而非在简洁框架里做定制（00:10:11、03:03:39）。**"agent 很吃后训练"**。
- **卡的分配 研究:预训练:后训练 = 3:1:1**：预训练与后训练算力应相当（Chat 时代是 3:1~5:1），研究用卡还要多于训练卡总量；"idea 到代码太快了，现在卡在卡上"（并行实验的算力才是瓶颈）（01:45:55–01:48:55）。这把姚顺宇"后训练是分水岭"量化成了具体的算力配比。
- **skills 是预训练的补充**：组织规范/另类信息抓不到、不在预训练数据里，只能人机多轮沉淀成 skills（"现在大量 skills 是 agent 自己写的"）（00:46:35–00:49:37）。
- **架构服务于范式**：**hybrid attention（sliding window + full）取代 MLA** 以适配 agent（省 KV Cache + 留计算富裕给 MTP）；**MTP 无幻觉**（被 verify）；**1T 参数是 agent 时代入场券**；"别给架构设太多目标，后训练做久了限制都变伪限制"（01:26:48–01:42:55）。详见 [AI 算力与基础设施](ai-infrastructure.md)。
- **发展史复盘**：ChatGPT（4K context + chat 好交互激发智能）→ LLaMA 开头 → Qwen(纯 scaling) 与 DeepSeek(创新+scaling) → o1/R1(reasoning 从 CoreganMath 泛化到通用，"R1 诞生很偶然") → 2025 交错之年 → 2026 agent 第二幕（02:48:34–03:03:39）。
- **彻底放弃旧 agent benchmark**：browsecomp/swebench"太局限、太离谱"，优化时"基本不看、靠体感"（详见 [评估与 Benchmark](evaluation-and-benchmarks.md)）。

## RL 训练的精度调试与稳定性：DeepSeek V4 适配一线（SGLang·Miles 团队，中，2026-05）

来源：[月球大叔 SGLang 直播](../videos/20260501-uncle-moon-sglang-deepseek-v4.md)

把上面的 RL 理论落到一线工程 debug：

- **给训练做"day-0"支持远难于推理**：推理有 benchmark 可判正确，训练**没有标准 baseline**——整套 recipe 是否正确要靠"训几天涨点"验证，debug 成本极大；且训练要实现 backward、跨引擎对齐 weight 格式（FP8 rollout + FP8/BF16 training）（00:22–00:28）。
- **精度是最耗时的环节**：逐 tensor（每层 activation、每个 gradient）与改动前做端到端比较。DeepSeek V4 的 compress attention 很稀疏、reduction 复杂，使 **KV gradient 用 BF16 精度完全不够**（CP=1 vs CP=2 的该 tensor cosine 差 0.2，其他 tensor 是 1e-4~1e-5），换 **FP32** 即解决（00:31–00:34）。
- **训练稳定性靠 deterministic ops**：借鉴 DeepSeek 的做法在 kernel/MoE 用 deterministic mode、禁 NCCL 非确定性——原本的 **KL loss spike 消失**；DSA（sparse attention + indexer router）这类架构从 V3.2 起就被发现难训稳（00:34–00:35）。呼应朱邦华"调通靠系统性排 infra 暗坑、不是理论"。

## RLVR 的终极版本：verifier 是一整间实验室（Lila Sciences，美，2026-07）

来源：[Lila 访谈](../videos/20260716-latent-space-lila-sciences.md)

把 RLVR 从"数学/代码可验证"推到"物理世界可验证"，是本页 RLVR 主线（Karpathy、Raschka & Lambert、朱邦华）的一个激进外延：

- **"以自然/实验做 verifier 是 RLVR 的终极版本"**：RL 本质是"模型生成自己的数据、reward 强化好数据"；Lila 把物理实验室建成"可规模化 verifier"，产出**实验验证过的推理轨迹**（互联网上 order-of-zero），一展示给模型就立刻见提升——哪怕参数处于劣势（00:06–00:07、01:22–01:23）。呼应 Raschka & Lambert"RLVR 可 scale、RLHF 不能"：Lila 是把"可验证"的边界从计算延伸到物理测量。
- **chain of thought 里实验室仪器就是 tool call**：与柯丽一鸣"奖励=向智能体传达意图"、朱邦华"RLVR=可客观验证的 reward"同频；物理科学的 **reward hacking 是真实担忧**、病态含"跳过实验直接给答案"（00:24–00:27）。
- **训练工程细节与 Karpathy 呼应**：不做预训练、从 open-weight（~$1B 算力等价、NVIDIA/Nemotron）起步叠 10T 科学 token（"广度带来深度"，通用模型胜过领域专用）；主张把 **RL 训练"因式分解"成并行专家模型再蒸馏回中心模型**（不同时间尺度各自训/生成）——与 Eric Jang"蒸馏高效"、姚顺宇软/硬蒸相通；并点名 **RL 的 MFU 仅 5–6%** 是最大浪费（00:28–00:33、01:18–01:21、01:37–01:39）。

## 把 scaling 三段式搬到分子结构预测（Genesis Molecular AI，2026-06）

来源：[最前沿的 diffusion 研究在药物发现](../videos/20260630-latent-space-genesis-diffusion-drug-discovery.md)

Genesis 明确把 LLM 的"预训练 / 后训练(RL) / 推理时"三段式移植到 protein–small molecule 结构预测（Pearl 模型），是本页 scaling 主线在**非语言模态**上的一个平行样本：

- **预训练 = 物理模拟造合成数据**：公开晶体结构库 PDB 只有约 20 万、增长冰川速度；小分子可用物理建模造更多训练数据（大蛋白太复杂、算力代价高）（00:15–00:16）。与 [Lila](../videos/20260716-latent-space-lila-sciences.md)"科学即 token 生成器"、[CZI](../videos/20260610-no-priors-zuckerberg-czi-biology.md)"数据即约束"同属"生物/化学数据不在互联网、必须造"。
- **推理时 scaling = 在结构表征上"思考"**：不在语言 token 上，而在"内存里未物化的晶体结构表征"上多步迭代（diffusion head 天然多步）、用**物理引导**steer——把 LLM 的"thinking tokens"换成"thinking structures"（00:16–00:19）。
- **RL 含"实验室 in-the-loop"**：先用物理反馈，最终"预测→合成→测量→回灌"；与中国 biotech 伙伴（Insight）组"设计-造-测-分析"闭环（01:09–01:14）。是本页 RLVR 主线（含 [Lila 的物理 verifier](../videos/20260716-latent-space-lila-sciences.md)）在药物发现上的落地。
- **primitive 之辩**：2017–18 GAN（mode collapse）做不了蛋白复合物，diffusion 才对；如今图像/视频有些转回 AR，而结构生物学成"diffusion 的一根支柱"——**同一 primitive 在不同模态的命运相反**（00:00、01:06–01:08）。Sergey（原 Llama 2/3 预训练负责人）："LLM 架构本质还是 2017 transformer、有点无聊；我们的架构很不同、很有意思。"

## 中美对照

见 [中美 AI 生态对照](china-us-ai.md)：算力劣势下中国实验室的蒸馏（硬蒸/软蒸）与后训练路线；DeepSeek 被姚顺宇列为与 OpenAI/Anthropic 同期"想明白后训练怎么 scale up"的一方（[张小珺访谈](../videos/20260511-zhang-xiaojun-yao-shunyu.md) 02:12）。朱邦华从 RL infra 侧补充：DeepSeek V3 的 RLVR 突破是 NVIDIA 收购其 NexusFlow 的直接契机（[月球大叔访谈](../videos/20260518-uncle-moon-banghua-zhu-sglang.md) 00:35:41）。Genesis 从美方补上一条数据闭环视角：中国 biotech 自建极强 in-house 湿实验能力、数据产出极快，是"设计-造-测-分析"RL 闭环的关键（[Genesis](../videos/20260630-latent-space-genesis-diffusion-drug-discovery.md) 01:12–01:14）。

## 数据效率与"这一代范式的上限"（swyx，2026-07）

来源：[Latent Space / swyx 交叉播客](../videos/20260710-latent-space-swyx-agent-labs.md)

- **"数据效率是下一个问题"**（[swyx](../people/latent-space-hosts.md) 明确点名呼应 Dwarkesh）：靠数万亿 token 才换到人类等价劳动，相比人类极度低效——人类在百万、上十亿量级就是个能干活的成年人。目标路径是"**从 2000 个样本学一件事 → 20 个 → 2 个**"，才能真正走到**持续学习**、走出 pre-train/post-train 范式（他认为该范式"现在大概正在撞某种上限"）。
- ⚠️ **但他给这个论证附了一条自我限制——"酸涩的教训（sour lesson）"**：**每次拿人类类比机器，你多半会失败**，因为机器的发展方式与人类根本不同。所以不必把 LLM 塞进人类的盒子；它可以是"**一种异类的、更高效的学习方式**"。**"极度低效"本身是我们确知的纯负面项**，值得改进——但改进方向不必模仿人类。这是对本库中多处"人类学习效率"论证（含 [Perszyk 的认知科学路径](../people/danielle-perszyk.md)、[a16z"人脑远更高效"](../people/a16z.md)）的一个有用的方法论警告。
- **LLM 不足以导向递归自我改进**：LLM 确实让 RSI 成为可能，但"**递归是受限的——它多半只探索已被探索过的东西**"，离已知分布不远。真正的未知之未知、真正的世界模型，仍属研究领域。
- **"Fable 是这一代 LLM 的终点"**（预测）：论证不是能力而是**预算**——"我想活在无限预算的世界里，但我没有的预算是**时间**"。若 20 万亿参数就是极限（没有 200 万亿、没有千万亿级），那么在可用性意义上这一代就到头了，必须换别的（他点名 thinking machines、together AI 的 SSM 方向，"whatever it is，我们还没有"）。
- **应用侧的 post-training 已成常规能力**：[Lovable](../people/anton-osika.md) 在斯德哥尔摩建专做 post-training 的研究团队（理由之一是"欧洲生态里应该有这个能力"），训练信号来自**前沿模型在自家生产分布上犯的错**——按客户影响排序后构造数据集或做 RL。这与 [Legora 的窄任务微调模型](../videos/20260714-all-in-11labs-legora-voice-law.md)、[Decagon 的 post-train 开源模型](../videos/20260711-all-in-ipo-token-roi-china-open-source.md)构成同一趋势：**post-training 正从实验室能力下沉为应用层公司的标配**。

## 数据的性质决定能学到什么：因果 vs 观测（Xaira，2026-07）

来源：[Causal Models Need Causal Data](../videos/20260721-latent-space-xaira-xcell-virtual-cell.md)

这是本页"数据决定模型上限"这条经验规律在生物学上的一个**原理性、可证伪的版本**，对 LLM 侧有直接的外推价值：

- **观测数据在原理上欠定**："如果你观察到基因 A、B、C 一起上下波动，你可以推断 A 调控 B 和 C；也可以说 B 调控 A 和 C……**有 N 种因果结构能拟合同一份相关性数据。原始数据在根本上 underpowered，学不出真正的因果。**"
- **实证后果**：在描述性数据上训练的基础模型（scGPT、Geneformer）擅长描述性任务（去 batch effect），**但在扰动/反事实任务上至今打不过线性基线**。这是一个"更大的模型 + 更多的数据但错误的数据类型 ≠ 更强的能力"的干净案例。
- **消融给出的排序**：**数据质量/规模 > 架构 > 先验知识**（作者注明只适用于其架构）。架构侧的具体收益来自 **自回归 → diffusion language model**："自回归是打字（I → I like → I like coffee），diffusion 是编辑（从粗糙迭代精修）"；因为基因表达本质是矩阵、打乱顺序生物学不怎么变，**顺序假设只是为复用语言模型现成技巧付的税**。增益集中在**泛化到未见上下文的难任务**上。
- **先验注入**：五类生物学先验（文献嵌入/PPI/DepMap/形态学/细胞类型）经 cross-attention 注入；训完后已内化为可学习参数，推理时不必再给，**但推理时再给一遍相当于虚拟细胞的 in-context learning**。先验权重还带来可解释性。作者坦承先验的 delta 是 condition-specific、有时边际收益很小，怀疑是 cross-attention 这种注入方式限制了作用范围。

## 训练失败模式的一手记录（蚂蚁灵波，2026-07）

来源：[张小珺 #147](../videos/20260722-zhang-xiaojun-shen-yujun-lingbo-embodied-native.md)。本页素材多为成功路径的复盘，这一期难得地给了**具体的失败与代价**：

- **MoE 的均衡激活是能力问题**：现有视频生成模型多为 dense（"14B 模型推理时激活就是 14B，你后面加速做得再好，能加速的比例是固定的"）。训 MoE 的核心是**让专家被等概率激活**——"一共 30 个参数，每次都激活那 10 个，剩下 20 个基本不被激活，这跟 10 个参数的 dense 就没区别了"。手段是 loss function 的选择、sampling 策略、加正则。代价：**光训 MoE 就花了两个月、失败了几十次**，且"失败不是训到后面才失败，训一训就发现跟你想要的不一样"。
  > **"把 MoE 训好是一个能力问题，它不是一个态度问题——不是说我想让它少激活点就少激活点。"**
- **双向 → 单向 attention 的改造会让预训练作废**（很有普适价值的一条）：他们试过"先训双向再改单向"，结论是——"**单向这件事是跑通了，但预训练模型里学到的一些知识（比如对文字的理解）其实是隐含在双向 attention 里面的，那些 knowledge 有些就遗忘了，相当于预训练作废了**"。直观表现：能被转成好视频的句子比例从 100% 掉到 **20–30%**。因此他们**从最开始设计就用单向**，这件事花了三四个月。
- **压缩器不该只是压缩**：数字世界的视觉编码器"就是单纯把 100 兆变成 30 兆让它更好学，**这个压缩过程本身对后面的学习没有任何帮助**"。灵波在训压缩器时**加入了语义和动作的对齐**，让编码过程本身就感知语义与动作信息。
- **可以舍弃什么，取决于下游**：物理世界可以舍弃**画质**——"生成的东西有点马赛克没关系，**因为我们还有摄像头**"。类比：不同生物能看到的清晰度不同，但都能在地球上生活。这是"目标函数应由部署约束反推"的一个清晰样本。
- **数据配比的知识**：跨本体训练时"**如果头部自由度出现的比例跟腰部差距特别多，模型就会更倾向于学头、不太会动腰**"。以及一条反直觉的数据质量观——**操作越简单的任务通用性越好**，因为复杂任务依赖操作员，而**一条不丝滑的数据是没法修的**，"模型会以为这是正确的操作方式，最后控机器人时机器人也非常卡"。
- **仿真数据只用于评测、不用于训练**：理由不是数量而是**分布同质化**。⚠️ 这与 Applied Intuition"五年多前就建合成数据团队、深信合成数据能加速自动驾驶"直接冲突，是一处值得跟踪的分歧。

## Model Factory、行为 > 智能、RL 前移预训练（Eiso Kant / Poolside，2026-07）

来源：[Poolside 的 Model Factory、Laguna S 与开源](../videos/20260722-latent-space-poolside-eiso-kant.md)

本页多为"训练配方/scaling"的复盘；Poolside 补上了**"如何把训练工业化到 5–8 周一代"的工程侧**，以及几条对训练范式的强判断。

- **Model Factory = 把工程作为科学严谨性的前提**：不可变数据层 + experiments-as-code = 完美可复现（能追溯到"哪个 cursor、哪个代码版本、哪个 token"，两年前的 run 还能精确重跑）；**数据流式喂进训练**（just-in-time，数据混配变 config，"blender"服务）；核心度量是"想法→可信实验结果"的墙钟时间。花了约一年半才意识到**工程不只是要快，而是让每次实验都是真正的 ablation**。这与朱邦华/罗福莉"RL infra 决定研究节奏"、SGLang·Miles"逐 tensor 精度调试"是同一工程哲学的模型公司整机版。
- **行为 > 原始智能（完全来自 post-training）**：Laguna S（118B/8B 激活）的收益"不是来自更多智能，而是来自**更多验证、不轻易 take for granted、不过早宣布胜利、更持久**——对成功而言这些比原始智能更有预测力"。这是本页"RL 重塑分布而非注入新知识"（姚顺宇/Noam）的一个极端而具体的印证：**小模型靠行为而非参数追平 2–3 倍大的模型**。不同尺寸的 post-training 配方不能直接互套，但**大模型配方套到小模型几乎总是好基线**。
- **RL 会越来越早前移进预训练**（比 mid-training 更早）：DeepSeek-zero（约一年半前）已证明很早就能诱导推理；Poolside 花两年研究"把 web 从 next-token 变成更早教模型思考"。判断行业的两个"毒品"——**蒸馏**和**更多 environments**——虽有效但"web 远未被压榨干净，光靠 next-token 预训练不够"，且不确定"通往 AGI 就是无限堆 environments"。
- **mid-training 只是 web 上一个粗糙的两段式课程**：终极想要的是从 token 0 到 40T 的最优**连续课程**，只是算力/组织设计不到位；"mid-training 存在是因为有了 mid-training 团队"——**分阶段是组织现象、不是科学必然**。呼应本页"mid-training = 继续预训练 + 一个笨拙的 curriculum"的既有判断。
- **拒绝蒸馏 + 频繁从零训练**：这些模型是"双用途"（既检验 model factory 是否进步、又是发布物），故不蒸馏；**频繁训练（而非 6 个月一次）能避免"改进堆成一锅汤、分不清哪个配料起效"**——这是"可归因性"作为训练组织第一性原理的清晰表述。

## ⚠️ "架构设计本身应该是一门科学"：Transformer 中了硬件彩票（刘子鸣，中，2026-07）

来源：[刘子鸣期](../videos/20260731-zhang-xiaojun-liu-ziming-ai-for-ai.md)。[刘子鸣](../people/liu-ziming.md)（KAN 一作）给的是一条**针对本页整条流水线的元批评**：我们把 scaling 用在了 compute 和 data 上，却没用在**模型设计**上。

- **核心主张**（[00:16:19]）：**"Transformer 拍脑袋拍出来的、GAN 拍脑袋拍出来的、ResNet 拍脑袋拍出来的，这个就非常的不 scalable。我觉得我们不应该 scale compute 或者 data，我们应该 scale AI 模型的设计。"**
- **Transformer 中了硬件彩票**（[00:17:20]）："Transformer 其实在算法上也没有那么厉害，**它是中了这个硬件的彩票**。"
- ⚠️ **语言模型是"反 Bitter Lesson"的**（他明确呼应谢赛宁在张小珺此前访谈中的观点，[00:18:21]）：**大语言模型成功的点在于语言，不在于模型**——语言是"我们人类演化了百万年、相当于自然给我们的一种馈赠"，**"你做什么样的模型，只要这个模型能够把这些馈赠给吃下去，那它就是一个好的模型"**；"它可能是 Transformer，但**平行宇宙里它可能是另外一个模型**"。
- **一条很干净的祛魅表述**（[00:20:25]）：**"它牛不是因为它叫 Transformer，是因为它能够在上下文上有比较高效的信息传播；ResNet 也是，它牛不是因为它叫 ResNet，是因为它能在深度方向上有很高效的梯度传播。"**
- **推论：后 LM 时代模型设计会更重要**（[00:19:22]–[00:20:25]）。**语言已经是被压缩得很好的模态**，所以那里的架构设计相对不精巧；但**视觉等模态没有被压缩好**——这正是世界模型公司要解决的问题。而 AI 至今**不会做抽象**："如果说它能做抽象，**最多是因为我们的数据本身已经被抽象好了**。"

### 天文学三阶段：Scaling Law 只是"开普勒定律"

本页收录了大量 scaling 相关的经验规律。[刘子鸣](../people/liu-ziming.md) 给了一个定位它们的框架（[00:25:29]–[00:27:32]）：

| 阶段 | 天文学 | 对应 AI |
|---|---|---|
| 1 · 数据 | 第谷记录星象 | 大量实验 |
| 2 · 经验公式 | 开普勒拟合出椭圆轨道与三大定律 | **Scaling Law**（"我们为数不多知道的几个经验规律"） |
| 3 · 理论 | 牛顿用一个引力公式把三大定律全部压缩 | 尚未出现 |

- 他的定位：AI 现在处于**第 1.5 阶段**，**Scaling Law 与开普勒定律地位类似**，"我们现在还远远没有到 AI 的牛顿这个状态"。
- ⚠️ **更悲观的版本**（本条最尖锐的一句）：**"我们可能现在是 0.5。"** 因为"**第谷好说歹说，它把望远镜对着了星空**"，测的是各个星区；而"**我们过度地聚焦、过早地收敛到 Transformer 这种类型的架构上，我们似乎已经失去了探索其他类型架构的 motivation**"——像第谷只盯着一片星区。结论：**"可能连大数据的时代都没到"**，因为"我们这个数据它是只针对 Transformer、只针对很少的几种模型有效的"。
- **他的技术回应是元模型**（预测 next curve、以架构多样性为核心指标），详见 [AI for AI / Auto Research](ai-for-ai-and-auto-research.md)。⚠️ 其中一条对本页有实际含义的判断：**这类研究需要不少算力，但不需要大集群、不需要卡间高速 communication，因为跑的是大量小模型**——与本页其余条目的算力形态完全不同。

### symbolic vs connectionist：agent 就是往回拉的那一点

- **短期需要结构、长期不需要**，依据正是 Rich Sutton 的 Bitter Lesson（[00:57:07]、[01:10:22]）；⚠️ 他给的"短期"尺度是**"可能 100 年以内"**。
- ⚠️ **一条对 agent/harness 的重新解读**（[01:11:22]）：**"Agent 某种意义上就是把这个连接主义又往符号主义往回拉了一点。所谓的 harness 就是说你不能太自由了，我要给你一些约束。"**
- 他自称因为"太多符号主义的 hater"而改用自造词 **"结构主义"**；历史判断是两者**不断摇摆**——"这一波 AI 是连接主义非常厉害，**那或许下一波我们又应该往符号主义回摆一点**"。

## ⚠️ "更聪明 vs 更便宜"是一个假的权衡（Decagon，2026-07）

本页的 scaling 讨论多在**前沿模型怎么变强**。[Decagon 那期](../videos/20260731-a16z-decagon-enterprise-ai-apps.md) 给了一条来自生产部署侧的判断（[00:05:00]）：

> "推特上这些辩论的权衡往往被说成：我们要非常贵的最聪明的模型，还是把它变笨一点换便宜？**我其实认为那是一个假的权衡**……我们在实践中看到的是——**当我们微调更小、更笨的模型时，它们只是没那么通用，但在我们要它做的那个具体任务上，它们确实超过又大又聪明的 SOTA 模型。**"
> **"所以我们最后三样全拿到了：它在这个任务上更好、更便宜、而且更快。"**

**前提条件（他给的，很重要）**：agent 的活是**对话**，一次要做很多子任务（判断话题、识别坏演员……），而"**每一个单独的任务都不需要一个大模型的全部智能**"。即：**这条结论依赖任务能被拆细**，不是对所有工作负载成立。

**他们给的三维框架**：评估模型看**成本 / 智能 / 延迟**，"看你需要什么，你要顶到这三者的极限，有时候可以互换"；⚠️ 他们转开源的**真实驱动是延迟**（语音 agent 上线后），"**前沿实验室确实有小模型，但你没法按你想要的方式控制它们**，而且大多数开箱小模型在我们要它做的任务上不够好"。

**前沿模型留在哪里**：**辅助任务 + 开放式探索型任务**——例如让一个更大更慢的 agent 去"审阅一百万条刚发生的对话、找趋势、**造出主模型的变体并比较哪个更好**"。这是一条清晰的**分工判据：窄而重复的任务给微调小模型，宽而开放的任务给前沿模型。**

⚠️ **与本页/本库其它立场的关系**：与 [Eiso Kant 的"行为 > 原始智能"](#model-factory行为--智能rl-前移预训练eiso-kant--poolside2026-07)、[Lovable 的多模型路由 + post-training](../people/anton-osika.md)、[DoorDash 的开放权重路由](../people/doordash-founders.md) 同族，但表述最强——**不是"够用就好"，是"在特定任务上超过 SOTA"**。⚠️ 与 [swyx 反对模型路由](../videos/20260710-latent-space-swyx-agent-labs.md) 构成直接分歧，本库并列不裁决。

### "模型工厂"：微调不是一次性工程

（[00:09:02]–[00:10:03]）"我们不是建好一套开源模型然后就完事、两年后再回来看。"**随着前沿能力变化会冒出新用例**（"这个任务好像重复得很多，因为我现在有了一个此前没有的能力"），所以他们**不断训练全新模型、淘汰不再相关的旧模型**。Decagon Labs 被定义为"**某种意义上的模型工厂——建它就是为了压缩'新模型出来'到'对我们任务有用的微调模型掉出来'之间的时间**"。这与 [Poolside 的 Model Factory](#model-factory行为--智能rl-前移预训练eiso-kant--poolside2026-07) 同名同构，但一个在前沿实验室侧、一个在应用层侧。

## 模型进步落到产品上是什么：指令跟随的宽度（Decagon，2026-07）

（[00:49:29]–[00:50:31]）本页有大量关于能力提升的抽象描述。这是一条把它落到可观察行为上的：

> "**具体来说就是跟随指令的能力。** 几年前的模型你得给非常非常紧的指引、非常具体、不许偏离。**随着模型变聪明，你可以给越来越宽、越来越大的指引，并且信任模型有足够的判断力像人一样去解读、把缺的空白填上。**"

**为什么这条对训练侧有意义**：它把"更聪明"翻译成一个**可度量的产品判据**——**在多宽的指引下仍能保持行为正确**。这与本页 [RLVR / 后训练](#rlhf-vs-rlvr-与-ppo-的工程暗坑朱邦华中sglang-母公司2026-05) 的目标函数直接相关，也解释了为什么客服（紧路径）比销售资格判定（开放式、会来回摆动）更早可行。

## "unhobling" 的工程翻译：Situational Awareness 的第三条 OOM（Sacks 转述，2026-07）

（[2026-07-31 All-In](../videos/20260731-all-in-chip-crash-pacing-the-frontier.md) [00:09:07]–[00:11:08]）本库第一次记录 Leopold Aschenbrenner *Situational Awareness* 的论证结构。三个方向各以**每年约 3 倍（每两年一个数量级 / OOM）**改进：

1. **原始算力**（芯片）；
2. **算法效率**（如强化学习等技术）；
3. ⚠️ **"unhobling"（解除束缚）**——Sacks 明确把它翻成今天的语汇：**"我想现在我们会把它看成 harness 和 connectors，也就是使用模型的方式、把模型的决策以实用方式集成进去的方式，让智能真正变得有用。"**

**外推**："四年就是 100 倍，六年就是 1000 倍。"

⚠️ **本页该记的点不是这个外推，而是第三条被承认为一条独立的 scaling 轴**。这与本库 [戴雨森的 "Harness = OS + 模型 = CPU"](../people/dai-yusen.md)、[Akshay Nathan 的 harness 合并](../videos/20260728-latent-space-akshay-nathan-chatgpt-work.md)、[Netic 的"last mile 必须来自 harness 与编排"](../videos/20260731-no-priors-netic-autonomous-enterprise.md)、[刘子鸣的"harness 就是我要给你一些约束"](#symbolic-vs-connectionistagent-就是往回拉的那一点) 落在同一处——**模型之外的那一层，在 2024 年的预测框架里就已经被当成 scaling 的一个乘数了。**
