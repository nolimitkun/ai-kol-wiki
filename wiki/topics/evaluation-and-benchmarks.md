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

## 交叉观察

- 三人共识：**当代 benchmark 的信息量在枯竭**——要么被打满（姚）、要么不控制 test-time compute 就误导（Noam）、要么一公开就失效（Mark）。三者互补地指出：真正的评估需要 test-time compute 维度 + 私有/新造 eval + 团队分离。
- 与 [LLM 训练管线](llm-training-pipeline.md) 的 RL 部分相关：可验证、可训练的 reward signal 既是 coding 快进的原因，也是 benchmark 被 bench maxing 的原因。
- 安全侧的评估缺口见 [LLM 安全](llm-security.md)（Noam：安全评估框架没考虑 test-time compute）。

## 中美对照

姚顺宇提供了中方一线视角下"纸面趋同"的判断；中国模型（GLM/字节/DeepSeek/Kimi）"发得快也说明这道题对所有人都变简单了、knowhow 已无秘密"（[张小珺访谈](../videos/20260511-zhang-xiaojun-yao-shunyu.md) 03:06–03:08）。
