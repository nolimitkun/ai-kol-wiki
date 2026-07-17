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

## 中美对照

见 [中美 AI 生态对照](china-us-ai.md)：算力劣势下中国实验室的蒸馏（硬蒸/软蒸）与后训练路线；DeepSeek 被姚顺宇列为与 OpenAI/Anthropic 同期"想明白后训练怎么 scale up"的一方（[张小珺访谈](../videos/20260511-zhang-xiaojun-yao-shunyu.md) 02:12）。朱邦华从 RL infra 侧补充：DeepSeek V3 的 RLVR 突破是 NVIDIA 收购其 NexusFlow 的直接契机（[月球大叔访谈](../videos/20260518-uncle-moon-banghua-zhu-sglang.md) 00:35:41）。
