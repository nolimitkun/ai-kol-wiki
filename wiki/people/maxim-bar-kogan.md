# Maxim Bar Kogan

- **背景**: **Onyx Security** 联合创始人/CEO，公司在特拉维夫（Tel Aviv）。团队多出自以色列情报单位（数学 × 网络攻防），联创 Gil 出身 NVIDIA 合成数据。Onyx 做"**AI 看管 AI**"——用小而专的模型监督自主 agent 的动作。
- **定位**: 本库首个"agent 安全/治理"公司视角，与 [Gray Swan](gray-swan-founders.md)（对抗鲁棒性）、[Databricks](databricks-founders.md)（有状态安全策略）互补，落点 [LLM 安全](../topics/llm-security.md)。自称"以色列最 AGI-pill 的人"。

> Onyx 两件事：训练能监督其他 agent 的模型 + 产品化为"secure control plane"。关键工程约束是成本/延迟/可靠性——不能给每个 agent 都配一个同等聪明的 agent 看着。

## 核心观点

- **押注 agent 动作**（而非"员工往 ChatGPT 粘什么"的旧 DLP 叙事）：AutoGPT 是转折点，如今 Claude Code/co-working/openclaw 类**不受限自主 agent**真被大企业采用（>50% 企业 agent 是自主编码 agent、增长最快）却几乎无控制（[No Priors](../videos/20260528-no-priors-onyx-security.md) 00:01–00:09）。
- **传统安全栈失灵**：自主 agent"我们希望它有我们的权限"→身份/权限安全失效；endpoint/API 安全**不知道 agent 在想什么**（删库在某任务是好事、在另一任务是灾难）（00:10–00:12）。proxy+policy 引擎不够——难点不是看到数据，而是**判断该不该做这个动作**（00:12–00:13）。
- **小守门模型 + blitz chess 类比**：给每个 agent 配一个聪明 agent 监控成本 dealbreaker；训"很小、几乎只会判断'该不该让更强 agent 来看'"的模型，像顶尖棋手多数靠直觉、关键局面才深算——高风险处狠花智能（00:14–00:18）。
- **独立第三方 + 数据不对称护城河**：安全买家不信"卖你产品的人认证产品"；企业不愿给 Anthropic/OpenAI 存历史行为数据（怕被训练）却可给 Onyx，故 Onyx 能判断"是否偏离常态"（00:32–00:36）。信 mech interp（"模型比我们聪明后反而更好破解"）（00:21–00:23）。
- **Mythos（自动化漏洞挖掘）与分阶段发布**："10 年前觉得要 20–50 年，现在一下子全来了"；建议**假设这些模型总会来**、现在投基础控制；风险是"若中国先有 Mythos 级模型而你没让企业提早准备，回头看是巨大错误"（00:25–00:28）。
- 终端从"人+少数 agent"转向"更多 agent"：既优化人的体验也**优化 agent 的体验**（别浪费 context token）（00:39–00:41）。

## 视频

- [造 agent 去看管 agent（No Priors，2026-05-28）](../videos/20260528-no-priors-onyx-security.md)
