# Akshat Bubna

**Modal 联合创始人/CTO**。Modal 是"从零为 AI 应用重造原语"的 capital-light 云平台（不自建数据中心，跑在 17 家 NeoCloud 上）。从数据/ML serverless runtime 起家，如今覆盖弹性推理、GPU sandbox、多节点后训练、agent 基础设施。与 [Databricks](databricks-founders.md) 的 Agent Cloud/Omnigent 构成"agent 云/sandbox"赛道的两个美方一线视角。

## 核心观点

- **self-provisioning runtime**：把硬件/扩缩容配置写进代码 decorator（与代码 collocate），而非读几百个无类型 Kubernetes YAML（[Modal 访谈](../videos/20260708-latent-space-modal-agent-infra.md) 00:04–00:06）。
- **AX≈DX（余弦相似度约 0.9）**：把 SDK 团队从"开发者体验"改成"agent 体验"；建 modal bench 找 agent 做不到的事，agent 反复幻觉某功能就把它做成真 CLI；代码变黑箱后 observability 更重要（00:06–00:07、00:57–00:58）。
- **sandbox 是 agent 的完美原语**：2023 年 5 月就做、去年才爆；RL rollout 极 bursty（要 10 万个 sandbox），agent 本身反而不 bursty（00:10–00:15、00:27–00:29）。
- **投机解码真相**：开源 DFlash（block-based speculator），提升 accept length 是乘法级 2–4x 提速（改 kernel 只有几个百分点）、不降质量（00:17–00:19）。
- **inference inflection**：AI workload 里 GPU:CPU 从 8:1 摆回约 1:1，agent 频繁 call out CPU，limiting factor 来回摆、必须 collocate（00:24–00:25）。
- **capital-light 超级云**：跨 17 家云建统一容量池 + 自建可靠性层；"compute strategy"团队做容量对冲（类比航空对冲燃油）；对 harness/meta-harness 不持立场——"只要消耗更多 infra 都看多"（00:38–00:40、00:45–00:47）。
- 对 sandbox 层坚持**硬边界**、怀疑 LLM 中介权限；对 swyx"LLM OS 内核就是个 LLM"的非共识观点持保留（00:43–00:44）。

## 视频

- [从 Kubernetes 到 Agent Sandboxes（Latent Space，2026-07-08）](../videos/20260708-latent-space-modal-agent-infra.md)
