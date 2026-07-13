# LLM 心理学与认知短板

> Karpathy 提出的框架："训练管线的涌现性认知效应"——理解模型为什么聪明得反常又蠢得反常。

## 核心概念（Karpathy，2025-02）

来源：[Deep Dive into LLMs](../videos/20250205-karpathy-deep-dive-into-llms.md)

| 概念 | 内容 |
|---|---|
| 标注员模拟器 | ChatGPT 的回答 = "遵循标注指南的专家标注员"的神经网络模拟，不是魔法 AI（01:17, 03:23） |
| 两种记忆 | 参数 = 模糊回忆（一个月前读过的），context window = 工作记忆（刚刚经历的）；重要材料直接贴进上下文（01:32, 01:40） |
| 幻觉成因 | 训练集里问句永远被自信回答，模型模仿格式而非核实；缓解 = 探测知识边界后把"我不知道"写进训练集 + 工具使用（01:20–01:37） |
| 模型需要 token 来思考 | 每 token 计算量小且固定，推理必须摊到多 token；"先给答案再解释"是坏标注（01:47–01:56） |
| Tokenization 盲区 | 模型看不见字符 → 拼写、数数任务差（strawberry 问题）；解法是让它写代码（01:58–02:04）。系统性分析见 [GPT Tokenizer](../videos/20240220-karpathy-gpt-tokenizer.md)：非英语差、算术差、SolidGoldMagikarp 等怪象的统一根源 |
| 瑞士奶酪能力 | 解得了奥赛题、答错 9.11 vs 9.9（圣经章节特征干扰）；能力面有随机的洞（02:04–02:07） |
| 无持续自我 | "你是谁"是伪问题：每次对话从零启动的 token 处理器，身份是硬编码/幻觉出来的标签（01:41–01:46） |

**实践推论**：当工具用、查证其工作、对成果负最终责任；见 [LLM 实用方法论](using-llms-in-practice.md)。

## Jagged frontier 与 continual learning（Mark Chen，OpenAI，2026-06）

来源：[Latent Space 访谈](../videos/20260625-latent-space-mark-chen.md)

- 模型能解 IMO/IOI 却在平凡任务翻车——"对模型直觉的东西对人类不直觉"（**jagged frontier**，Karpathy"瑞士奶酪能力"的同类观察）；很多归结为 **context**：模型缺乏把单任务教训迁移到未来任务的能力（人类天然会）（00:24–00:25）。
- **continual learning 是必须解锁的 basic primitive**；长 context"实现"与"实现得好"不同，可用 compaction 等捷径压缩工作状态（00:25–00:26、00:29）。

## "研究品味"这个短板（Noam Brown，OpenAI，2026-06）

- 模型目前**没有好的 research taste**，是研究员的补充而非替代（poker solver：5.2 会"gaslighting"、需反复核对；5.5 近乎 zero-shot，但仍造不出超越已有工作的新算法）。（[No Priors 访谈](../videos/20260626-no-priors-noam-brown.md) 00:08–00:11、00:23–00:25）呼应 Karpathy"可验证域强、开放创造弱"的判断。

## 中方视角（姚顺宇，Google DeepMind，2026-05）

- "智能涌现"是**主观感觉/技术涌现**（找到怎么水平提升所有能力），而非行为涌现；AI 是黑盒但"所有东西都是黑盒"，Scaling Law 是经验规律（类比热力学、未来或成科学规律）。（[张小珺访谈](../videos/20260511-zhang-xiaojun-yao-shunyu.md) 01:44–01:47）
- 与 Mark/Noam 一致地把"产品经理/research taste/无客观标准的判断"列为 AI 当前难以复制的能力边界（00:44–00:46）。

## 中美对照

姚顺宇（中方一线）对"智能涌现"的祛魅（技术涌现而非神秘现象）与 Karpathy"标注员模拟器、不是魔法"一脉相承；三家美方研究者（Karpathy/Mark/Noam）与姚共同把"开放创造 / research taste / 无客观标准的判断"标定为模型能力的洞。
