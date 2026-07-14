# 朱邦华（Banghua Zhu）

- **背景**: **SGLang 母公司**联合创始人兼 CTO（2025 年底创立，做推理引擎 SGLang + RL 训练框架 Miles；已融 1 亿美金、估值 4 亿多）。此前创立 **NexusFlow AI**（企业 Agent 后训练 / RL as a service）→ 2025 年中被 **NVIDIA** 收购 → 任 Nemotron RL / NemoGym tech lead。学历：清华电子系本科 → 伯克利 EECS 博士（导师 **Michael Jordan**，做统计 / 强化学习**理论**）；华盛顿大学教职 offer 目前 defer 中。江苏苏北人，数学竞赛出身。
- **来源出处**: [月球大叔访谈（2026-05）](../videos/20260518-uncle-moon-banghua-zhu-sglang.md)

> SGLang 由 [盛影（Ying Sheng）](junchen-jiang.md)、郑联敏（Lianmin Zheng）与朱邦华等人在伯克利读博期间的合作中孕育；LMSYS（Vicuna、Chatbot Arena）是同一批人的早期非营利项目。朱邦华与 [江鋆晨](junchen-jiang.md)（LMCache / TensorMesh）同属"从学术研究组挑战工业界 AI Infra"的中国背景创业者群体。

## 立场与核心观点

- **AI Infra 民主化**：把 frontier-lab 级推理/训练基础设施 democratize 给所有开发者；押注 post-training-for-agent 从 frontier lab → neolab → 传统企业逐层扩散，推理产生的私有数据反哺 RL 形成闭环。
- **需求排序 pre-training < RL < 推理**——从推理切入。
- **RLHF vs RLVR**：RLHF 让模型"更像人/更 align"，RLVR 针对可验证领域（数学/代码/agentic），是模型工具化的关键；DeepSeek V3 证明"直接从 pre-trained 做 RLVR 就能大涨"是行业转折点。
- **PPO 上限远高于 DPO/简化算法，关键在工程 trick**（如 critic warm-up）；"infra 权重很大，暗坑会让你得出错误结论"。
- **RL environments 是新瓶颈**：reward 设计是艺术；function calling 的 latency/concurrency 让 CPU 变重要；国内这类创业明显偏少。
- **中美**：中国开源 vs 美国闭源差 ~6 个月，美国开源 vs 美国闭源差 ~1 年；国内 infra solid 但数据/RL 环境投入受限；国内工程师"从 0 到 100 做到 perfect"强、美国"从 0 到 1 crazy idea"强。
- **卡养人**：千卡/万卡训练的 infra 要求与小规模完全不同；"本科生摸够卡会比 PhD 干得好——PhD 太严谨不愿 YOLO"。
- **就业**：coding agent 让价值向"有 taste 的顶尖工程师"集中；招人核心看 taste/criticism（以 Linus 为范）与"政治善良/人格底色"。
- **勇于放弃**：时代变化快使试错成本变低，"能放得下的人最后拿得更多"。

## 与他人观点的呼应/分歧

- **卡养人 / 本科生也能干**：与 [姚顺宇](yao-shunyu.md) 高度一致；两人都强调大规模算力经验不可 generalize、以及做事系统性排 bug（朱的"infra 暗坑"≈ 姚的"撞墙多半是代码有 bug"）。
- **中美工程师风格与模型差距**：为 [姚顺宇](yao-shunyu.md) 的中方生态判断补上 Infra 侧一手视角（RL 环境投入差异是国内落后处）。
- **推理是模型主战场**：与 [江鋆晨](junchen-jiang.md)"training infra 太一次性、模型绝大多数生命周期在推理"一致。
- **Chatbot Arena 需向 intelligence frontier 演进**：见 [评估与 Benchmark](../topics/evaluation-and-benchmarks.md)，与 [Mark Chen](mark-chen.md)、[Noam Brown](noam-brown.md) 关于 benchmark 失效的讨论互补。

## 已收录访谈

| 日期 | 视频 | 频道 |
|---|---|---|
| 2026-05-18 | [SGLang、RLHF vs RLVR、被英伟达收购后二次创业](../videos/20260518-uncle-moon-banghua-zhu-sglang.md) | 月球大叔 |
