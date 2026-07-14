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

## 中美对照

见 [中美 AI 生态对照](china-us-ai.md)：算力劣势下中国实验室的蒸馏（硬蒸/软蒸）与后训练路线；DeepSeek 被姚顺宇列为与 OpenAI/Anthropic 同期"想明白后训练怎么 scale up"的一方（[张小珺访谈](../videos/20260511-zhang-xiaojun-yao-shunyu.md) 02:12）。
