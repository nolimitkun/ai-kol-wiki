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

## 认知科学视角：智能是社会性的、目标是"对齐表征"（Danielle Perszyk / Amazon AGI Lab，2026-07）

来源：[为什么 AI agent 其实"不懂你"](../videos/20260711-latent-space-perszyk-amazon-agi.md)

- **人类智能是集体智能**：智能从社会互动中涌现、本质社会性；创新是"多样性 × 规模 × 互联度"。行业被"聊天机器人 + 编码 agent + 回合制"这一**局部吸引子**困住，只为"造 AI 的工程师"造 AI（00:01–00:02）。
- **计算级目标 = 对齐表征**（借 David Marr 三层）：用 RL 刷单任务不泛化是"打地鼠"/Goodhart；人类在优化"不断推断他心、对齐彼此表征"，由此可推导出通用灵活认知——"**对齐是解法而非问题**"（00:18–00:20、00:37–00:39）。这为 Karpathy/Mark/Noam 标定的"开放创造/research taste 是短板"提供了一个机制假说：短板源于目标函数是"任务优化"而非"对齐表征"。
- **世界模型是社会化的、记忆≠存储**：人类从一开始就推断"他心如何解读世界"；记忆是模拟未来/情节记忆而非可 offload 的存储（呼应 [Mark Chen 的 continual learning](../videos/20260625-latent-space-mark-chen.md)、[Junchen Jiang 的 KV Cache 即记忆](../videos/20260609-uncle-moon-junchen-jiang-kvcache.md)）（00:08–00:10、00:22–00:23）。
- **当前 AI 在降低人类能动性**：写作被拉向均值（意识阈值下被切换论点）、用 AI 的个体科学家产出更多但科学整体收窄/思维同质化；解法是"一个有不同偏见/视角的 AI 社会"而非单一巨石模型（详见 [AI 与就业](ai-and-jobs.md)）（00:34–00:37）。

## 中美对照

姚顺宇（中方一线）对"智能涌现"的祛魅（技术涌现而非神秘现象）与 Karpathy"标注员模拟器、不是魔法"一脉相承；三家美方研究者（Karpathy/Mark/Noam）与姚共同把"开放创造 / research taste / 无客观标准的判断"标定为模型能力的洞。Perszyk 从认知科学给出更激进的一层——把这些短板归因于"行业误解了计算级目标"，主张 AI 该像人一样"对齐表征"（但她与 swyx 都保留"不一定要把 AI 完全长成人类"的立场）。
