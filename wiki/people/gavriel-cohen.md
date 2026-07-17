# Gavriel Cohen

**NanoClaw 作者/创始人**（NanoClaw Co.）。NanoClaw 是继 [OpenClaw](peter-steinberger.md) 之后又一个爆红的开源个人 agent（MIT 许可、Hacker News 发布、Karpathy 转推后升级），主打**极简代码库 + 隐私/安全隔离**。现从 AI 原生营销代理转做企业 agent 部署。与本库范式直接相关——他和用户都在用 **Karpathy 的 LLM Wiki 模式**（即本库范式）做 agent 记忆。

## 核心观点

- **企业引入 agent 先从"给每人一个个人 agent"起步**：因为"怎么和 agent 工作"有陡峭学习曲线，最大误区是"扔个任务就走开等成品"（[NanoClaw 访谈](../videos/20260629-latent-space-nanoclaw.md) 00:03–00:05）。
- **claw 类 agent 的杀手级用例是"第二大脑"**：不断喂信息、让它建 LLM Wiki/知识图谱，而非要现成产出（00:05–00:06）。
- **三层安全隔离**（相对 OpenClaw 的核心差异）：每 agent 独立 container；**agent 环境不放任何凭证**（即便被 prompt injection 也无法泄露 key）；出站请求经 **vault 代理**注入凭证 + **human-in-the-loop 审批**（00:08–00:10）。
- **LLM Wiki 优于检索**：问"这周最该关注什么"没有语义搜索能答，但有好的 LLM Wiki 就能跨文件收集；已知痛点是造重复文件、需背景进程查重（**与本库 Lint 巡检同构**）（00:11–00:13）。
- **agent 不像传统软件"部署完 5 年不动"**：模型底座在变、必须持续升级，每次升级都改变行为（00:17–00:18）。
- **"不要 pull request，给我 prompt request"**：coding agent 让开 PR 指数级变易、triage 跟不上；需求/bug 汇入"未来开发的 wiki"作 buffer（00:20–00:22）。

## 视频

- [自主工作 agent 的蓝图（Latent Space，2026-06-29）](../videos/20260629-latent-space-nanoclaw.md)
