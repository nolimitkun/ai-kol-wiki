# Eiso Kant

- **身份**: [Poolside AI](https://poolside.ai) 联合创始人兼 CEO（与 Jason Warner 共同创立）
- **背景**: 2015 年读到 Karpathy《The Unreasonable Effectiveness of RNNs》后转做"代码上的机器学习"，创立开源公司 source{d}（烧掉约 $1200 万、约 40 人、2019 年底失败，自称"职业生涯最大失败"）；ChatGPT 出现后重回赛道，创立 Poolside。
- **公司定位**: **模型公司（非 agent 公司）**，自 day zero 主张"AGI via coding / 长时程软件任务"；美国公司（一度以为在法国起家，实为 fully remote，刻意不在湾区招研究员）；少于 70 研究员 + ~35 工程师；约一年半前融 $500M；10k H200（Hopper）集群，正扩容。
- **本库主来源**: [Latent Space 访谈（2026-07-22）](../videos/20260722-latent-space-poolside-eiso-kant.md)

## 立场与关注点

Poolside 是本库首个成体系的**西方开源 neo-lab 内部工程视角**。Eiso 的观点几乎都围绕"如何把模型训练工业化"和"为什么开源/商品化能赢"。

- **"宁要 100 家基础模型公司，不要 5 家——哪怕我是那 5 家之一。"** 2026 年初从"抢先做到 AGI"转向开源；判断只有还没到前沿时才做得出这个决定。主动鼓励研究员离职去开更多 neo-lab。
- **开源研究 > 开源权重**："权重是二进制的，分享研究才是最有意义的贡献。"点名致敬 DeepSeek、Zhipu/Z.ai（GLM 5.2）的开放研究。
- **Model Factory**：把模型训练做成 SpaceX 式端到端工厂——不可变数据层 + experiments-as-code + 流式数据 + 零 on-call + agent 接管日常（"RSI 雏形"）；核心度量是"想法→可信实验结果"的墙钟时间；5–8 周从预训练到发布。
- **"行为比原始智能更能压榨小模型"**：Laguna S（118B/8B 激活）靠 post-training 诱导的持久、验证、回溯，跑赢 2–3 倍大的模型；由此推出**知识工作最优模型尺寸可能只在 1T–10T**，支撑模型商品化/开源能赢的论证。但明确不反对 scaling（"只做小模型之王是 copout"）。
- **"MCP 和工具是愚蠢的"**：模型应拿到一个装好 binary 的 VM + codebase，自己写代码（含 if/for）干活，而非调 50 个预设工具；预测 12 个月内没有塞满工具的 system prompt。
- **RL 前移**：RL 会越来越早进入预训练；mid-training 只是 web 上一个粗糙的两段式课程，组织原因才分阶段。蒸馏与 environments 是行业"毒品"，web 远未被压榨干净。
- **监管观**：技术更强时让位给民主；区分 misuse 与 doomsday；当前不该限制开源（香烟广告禁令固化寡头的类比）；但会随真实风险改立场。Nvidia 比政府更有算力权力，但性质不同。
- **招人第一看 agency**；约束催生创新；对齐高 agency 的人靠"共同目标 + 明确边界"。

## 与本库其他视角的关系

- **对 Benedict Evans"模型商品化、价值上移"**：Eiso 从**供给侧**给出机制——若知识工作最优尺寸不高、开源能紧咬前沿，则模型层确会商品化。见 [AI 商业化与价值捕获](../topics/ai-business-and-value-capture.md)。
- **对 swyx 的"反对模型路由 / agent lab"**：Eiso 认同"自家 harness 榨干单一模型才最强"，但作为模型公司仍主张能力应泛化到所有 harness。见 [Latent Space 主播](latent-space-hosts.md)。
- **对罗福莉/朱邦华（中方 RL/infra 视角）**：同样强调 RL 前移、post-training 前移、卡/组织对研究节奏的决定作用，是"neo-lab 工程哲学"的中美两版。见 [中美 AI 生态对照](../topics/china-us-ai.md)。

## 已收录访谈

| 日期 | 视频 | 平台 |
|---|---|---|
| 2026-07-22 | [Poolside 的 Model Factory、Laguna S、开源与 AGI 竞赛](../videos/20260722-latent-space-poolside-eiso-kant.md) | Latent Space |
