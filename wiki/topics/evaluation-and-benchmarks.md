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

## 交叉观察

- 三人共识：**当代 benchmark 的信息量在枯竭**——要么被打满（姚）、要么不控制 test-time compute 就误导（Noam）、要么一公开就失效（Mark）。三者互补地指出：真正的评估需要 test-time compute 维度 + 私有/新造 eval + 团队分离。
- 与 [LLM 训练管线](llm-training-pipeline.md) 的 RL 部分相关：可验证、可训练的 reward signal 既是 coding 快进的原因，也是 benchmark 被 bench maxing 的原因。
- 安全侧的评估缺口见 [LLM 安全](llm-security.md)（Noam：安全评估框架没考虑 test-time compute）。

## 中美对照

姚顺宇提供了中方一线视角下"纸面趋同"的判断；中国模型（GLM/字节/DeepSeek/Kimi）"发得快也说明这道题对所有人都变简单了、knowhow 已无秘密"（[张小珺访谈](../videos/20260511-zhang-xiaojun-yao-shunyu.md) 03:06–03:08）。
