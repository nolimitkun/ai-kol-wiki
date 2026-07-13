# Andrej Karpathy

- **背景**: OpenAI 创始成员、前 Tesla AI 总监；以深入浅出的技术科普著称（CS231n、nanoGPT、"Zero to Hero" 系列）。
- **频道**: [YouTube @AndrejKarpathy](https://www.youtube.com/@AndrejKarpathy)
- **watchlist slug**: `karpathy`

## 核心立场与观点

- **LLM = 互联网的有损压缩**：预训练是把数十 TB 文本压进参数；"预测下一个词"这个简单目标足以逼出世界知识。（[Intro to LLMs](../videos/20231123-karpathy-intro-to-llms.md) 00:04, 00:07）
- **LLM 是经验性造物，不是工程品**：不像汽车那样每个零件可理解，只能靠评测度量行为；对可解释性持审慎态度。（同上 00:13）
- **LLM OS 世界观**：他最具标志性的框架——LLM 是新计算范式的内核进程，context window 是 RAM，工具是外设；闭源/开源之争类比 Windows vs Linux。（同上 00:42–00:45）
- **看好的方向**：scaling laws 尚未饱和；工具使用与多模态是能力主轴；System 2 慢思考和窄域自我改进是下一步。（同上 00:25–00:40）

- **实用主义使用观**：LLM 输出永远是第一稿；"LLM Council" 多模型交叉；语音优先；不独自读书；vibe coding（他自认造的词）。（[How I use LLMs](../videos/20250227-karpathy-how-i-use-llms.md)）
- **"LLM 心理学"框架**：ChatGPT 是"标注员的模拟器"；参数是模糊回忆、context 是工作记忆；模型需要 token 来思考；瑞士奶酪式能力。（[Deep Dive into LLMs](../videos/20250205-karpathy-deep-dive-into-llms.md)）
- **RLHF is not RL**：奖励模型可被博弈，RLHF 只是微调；可验证域的 RL 才有 AlphaGo 式超越人类的潜力。（同上 02:48–03:06）

## 已收录视频

| 日期 | 视频 | 主题 |
|---|---|---|
| 2023-11-23 | [Intro to Large Language Models](../videos/20231123-karpathy-intro-to-llms.md) | LLM 入门全景：训练、能力、LLM OS、安全 |
| 2024-02-20 | [Let's build the GPT Tokenizer](../videos/20240220-karpathy-gpt-tokenizer.md) | 从零实现 BPE；tokenization 是诸多 LLM 怪象的根源 |
| 2024-06-09 | [Let's reproduce GPT-2 (124M)](../videos/20240609-karpathy-lets-reproduce-gpt2.md) | 从零复现 GPT-2 预训练：GPU 优化、训练配方、评测 |
| 2025-02-05 | [Deep Dive into LLMs](../videos/20250205-karpathy-deep-dive-into-llms.md) | 完整训练管线 + LLM 心理学（3.5 小时全景课） |
| 2025-02-27 | [How I use LLMs](../videos/20250227-karpathy-how-i-use-llms.md) | LLM 应用生态实用指南：思考模型、工具、多模态 |
