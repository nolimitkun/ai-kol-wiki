# LLM OS 与新计算范式

> LLM 不是聊天机器人，而是新兴操作系统的内核进程。

## 各家观点

### Andrej Karpathy（美，2023-11）
提出 LLM OS 框架：LLM 作为 kernel process 协调内存与计算工具——context window ≈ RAM（有限的宝贵工作记忆），互联网/本地文件 ≈ 磁盘（经浏览/RAG 访问），计算器/Python ≈ 外设；未来还有多线程、投机执行、用户态/内核态的类比。生态上闭源（GPT/Claude/Gemini）vs 开源（Llama 系）对应 Windows/macOS vs Linux。（[Intro to LLMs](../videos/20231123-karpathy-intro-to-llms.md) 00:42–00:45）

## 中美对照

（暂只有美方观点；待收录中方 KOL 对"大模型作为基础设施/操作系统"的论述后补充。）

## 开放问题

- 通用 System 2（慢思考换准确率）如何实现——Karpathy 2023 年认为尚无模型具备。
- 语言领域缺少通用 reward function，通用自我改进是否可能（AlphaGo 路径能否迁移）。
