# LLM OS 与新计算范式

> LLM 不是聊天机器人，而是新兴操作系统的内核进程。

## 各家观点

### Andrej Karpathy（美，2023-11）
提出 LLM OS 框架：LLM 作为 kernel process 协调内存与计算工具——context window ≈ RAM（有限的宝贵工作记忆），互联网/本地文件 ≈ 磁盘（经浏览/RAG 访问），计算器/Python ≈ 外设；未来还有多线程、投机执行、用户态/内核态的类比。生态上闭源（GPT/Claude/Gemini）vs 开源（Llama 系）对应 Windows/macOS vs Linux。（[Intro to LLMs](../videos/20231123-karpathy-intro-to-llms.md) 00:42–00:45）

### Dan Biderman（美，Engram CEO，2026-07）：RAM 不够——记忆、context rot 与"训进权重"
来源：[Latent Space 访谈](../videos/20260713-latent-space-dan-biderman.md)

接续 Karpathy"context window ≈ RAM"的框架，给出 2026 年的工程续集——**光把 RAM 做大（长上下文）不够**：
- **"记忆 / 持续学习本质是长上下文问题的伪装"**；即便 10M 上下文，仍有 (1) **context rot**（喂进越多 token 越困惑）与 (2) 内存/成本爆炸两大限制。**compaction（模型自管理上下文）在改进但按定义有损**、当前偏非黑即白，长会话深处会健忘（00:18–00:21）。
- **KV cache 的内存怪兽**：Llama 70B 读一篇几十 KB 文章，"脑状态"就占约 80GB HBM，与整个模型参数（约 140GB）同量级——RAM 极度低效（00:22–00:23）。
- Engram 的下注是把语料用梯度下降**训进权重**（"cartridges"，约 1000× 压缩），与文本表示（RAG/wiki，即 Karpathy 的"磁盘"）互补；长期"每人一份权重、跑在个人设备上"（00:09–00:11、00:26–00:28）。这把 LLM OS 的"内存管理"从"如何调度 RAM/磁盘"推进到"哪些知识该内化进内核本身"。

## 中美对照

（暂只有美方观点；待收录中方 KOL 对"大模型作为基础设施/操作系统"的论述后补充。）

## 开放问题

- 通用 System 2（慢思考换准确率）如何实现——Karpathy 2023 年认为尚无模型具备。
- 语言领域缺少通用 reward function，通用自我改进是否可能（AlphaGo 路径能否迁移）。
