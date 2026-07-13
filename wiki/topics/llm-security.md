# LLM 安全

> 新计算范式带来新的攻防猫鼠游戏（Karpathy 语）。

## 攻击类型（Karpathy 2023-11 的分类）

| 类型 | 机制 | 例子 |
|---|---|---|
| 越狱 Jailbreak | 绕过安全训练的分布盲区 | 角色扮演（"奶奶哄睡"）、Base64 编码（拒绝数据以英语为主）、优化出的通用对抗后缀、图像对抗噪声 |
| 提示注入 Prompt Injection | 外部内容伪装成新指令劫持模型 | 网页白底白字植入钓鱼链接；共享 Google Doc 经 Apps Script 外泄用户数据 |
| 数据投毒 / 后门 | 训练数据植入触发词 | "James Bond" 触发词使模型输出损坏（微调阶段已论证，预训练阶段截至 2023-11 未见令人信服的展示） |

Karpathy 的判断：攻击会被逐个修补，但这是持续的 cat-and-mouse，是 LLM 作为新计算平台的固有属性，类比传统操作系统安全史。（[Intro to LLMs](../videos/20231123-karpathy-intro-to-llms.md) 00:45–00:59）

## Tokenization 层的攻击面（Karpathy 2024-02 补充）

特殊 token（如 `<|endoftext|>`）的处理逻辑若泄漏到用户输入即构成攻击面；SolidGoldMagikarp 类"未训练 token"相当于把未初始化内存喂进模型，触发未定义行为。（[GPT Tokenizer](../videos/20240220-karpathy-gpt-tokenizer.md) 01:57–02:08）

## AI 规模化安全研究的伦理（FFmpeg 维护者视角，2026-05）

Google 用 AI 批量生成开源项目安全报告引发的争议：报告冗长、一切标 critical、90 天披露期限不顾志愿者开发模式——"近乎 AI 生成报告对维护者的拒绝服务攻击"；激励错位（发现者得百万赏金，修复的志愿者一无所获）。风波推动 Google 转向提交补丁 + 奖励修复。（[FFmpeg 期](../videos/20260506-lex-ffmpeg.md) 01:09–01:17）

## 安全评估的 test-time compute 缺口（Noam Brown，OpenAI，2026-06）

来源：[No Priors 访谈](../videos/20260626-no-priors-noam-brown.md)

- 各家的 responsible scaling policy / preparedness framework 大多诞生于 ChatGPT 时代，**没有考虑 test-time compute**——现在"模型能力是投入金钱的函数"（$10 → $10K → $10M 能力递增），政策没回答"应在什么 budget 下评估危险能力（如生物武器）"（00:11–00:14）。
- 与能力问题镜像：模型若在大 budget 下对有用任务不饱和，对有害任务也会如此；而"真正评估长任务可能要跑一年"与几天/几周的发布周期严重脱节（00:13–00:16）。这是评估框架层面的安全短板，与 [评估与 Benchmark](evaluation-and-benchmarks.md) 直接相关。

## 中美对照

（待补充。姚顺宇 2026-05 谈及 Anthropic"以 AI 安全立身却训前沿模型"的张力，认为"一家公司制定法律只能管自己"，更可能有效的是**类似核武器的 Multi-party control 制衡**——见 [AI 实验室文化与组织](ai-lab-culture.md) 与 [中美 AI 生态对照](china-us-ai.md)。）
