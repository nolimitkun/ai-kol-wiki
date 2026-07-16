# Matei Zaharia & Reynold Xin（Databricks）

- **Matei Zaharia**: Databricks 联合创始人/CTO，**Apache Spark 作者**（UC Berkeley），后主导 Unity Catalog（数据治理层）；也做 AI 研究（DSPy 等）。
- **Reynold Xin**: Databricks 联合创始人/首席架构师，Spark 核心贡献者，主导 lakebase/L-TAP/Dream Engine 等数据引擎方向。

本库收录其 2026-06 Latent Space 访谈——从 Spark 作者的系统设计视角谈 agent 编排与数据基础设施。

## 核心观点

- **"把数据放到对的地方，然后糊一层 AGI，魔法就出来了"**——但没有对的数据不行；很多传统软件会用这套新范式重写（[Agent Cloud 访谈](../videos/20260624-latent-space-databricks-agent-cloud.md) 00:00）。
- **Omnigent = 跨 harness 的公共 API + agent cloud**：把 Claude Code/Codex/Cursor 等统一到一套 session API，开源以吃网络效应；类比网络协议（IP layer）而非 OS（00:04–00:16）。
- **Agent 安全要 contextual/stateful policies**：超越 yes/no 允许列表，按 session 累积风险状态决策，更安全且更好用（Unity Catalog 数据治理经验平移，00:19–00:22）。
- **L-TAP = HTAP done right**：只统一存储层（列式转码）而非塌缩 query 引擎；**Dream Engine** 用 ML 模型（非 LLM）+ 十年 trace 从零重建数据库引擎（00:32–00:50）。
- **agent 让 SQL 方言统一不再是问题**："agent 在 Postgres/Spark SQL 都很流利"（00:52）。
- 组织：不用请示直接原型、增量演进、over-fit 少数客户；胜过 Snowflake 靠"从一开始开放格式 + AI plus data"（00:36–00:57）。

## 交叉

- Omnigent 的"跨 harness 公共 API"与 [江鋆晨"OpenAI API = IPv4 细腰"](junchen-jiang.md)、[戴雨森"Harness = OS"](dai-yusen.md) 同题：agent 时代的稳定接口层争夺。
- 有状态安全策略与 [Gray Swan](gray-swan-founders.md)/[Peter Steinberger](peter-steinberger.md) 的 agent 安全讨论互补——Databricks 提供的是企业侧治理落地。

## 视频

- [Agent Cloud：Databricks 押注 AI 的未来（Latent Space，2026-06-24）](../videos/20260624-latent-space-databricks-agent-cloud.md)
