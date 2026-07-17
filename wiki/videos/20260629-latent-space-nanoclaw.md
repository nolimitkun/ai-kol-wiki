# Gavriel Cohen（NanoClaw）：自主工作 agent 的蓝图——第二大脑、隔离安全模型与 LLM Wiki（Latent Space，2026-06-29）

- **嘉宾**: [Gavriel Cohen](../people/gavriel-cohen.md)（NanoClaw 作者/创始人）
- **主持**: [swyx](../people/latent-space-hosts.md)（Latent Space，AI Engineer / Singapore 现场）
- **来源**: [YouTube](https://www.youtube.com/watch?v=hLUGXO5DSpo) · 23 分钟
- **转录稿**: [sources/latent-space/20260629-hLUGXO5DSpo](../../sources/latent-space/20260629-hLUGXO5DSpo/transcript.md)

## 概要

NanoClaw 是 [OpenClaw](20260212-lex-openclaw-steinberger.md) 之后又一个爆红的开源个人 agent，主打**极简代码库 + 隐私/安全**。Gavriel 讲了新加坡外长在 Facebook 晒自己的 NanoClaw setup（Raspberry Pi + Karpathy LLM Wiki + Nemon 记忆系统）如何点醒他"企业引入 agent 的正确起点是先给每个人一个个人 agent"、NanoClaw 相对 OpenClaw 的安全隔离设计、以及公司化后为企业做部署的方向。**这期与本库直接相关——外长的 setup 正是 Karpathy 的 [LLM Wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)（也即本库范式）。**

## 核心观点

### 企业引入 agent：先给每人一个个人 agent
- 两条并行路线：**agent factory**（团队协作造/管一批自动化 workflow 的 agent）vs **个人 agent**（work setting 里每人一个助手）。外长的用例让他确信**先从"给每人一个 agent"起步**——因为"怎么和 agent 工作"有陡峭学习曲线（提示、建 skill、调 context window），最大误区是"扔个任务就走开等成品"（00:03–00:05）。
- 今天 claw 类 agent 的**杀手级用例是"第二大脑"**：不断喂信息、不指望现成产出，而是让它建内部记忆/知识图谱/"你的 LLM Wiki"，之后给有用输出（00:05–00:06）。

### 安全隔离模型（相对 OpenClaw 的核心改进）
- 不 fork OpenClaw、从零重写极简代码库；用 Agent SDK（自带 session 管理/compaction）而非 Pi（OpenClaw 用 Pi、需自建很多东西）、集成 Vercel Chat SDK 接各消息渠道、初期只支持一个模型一个 agent（00:07–00:08）。
- **三层隔离**（最大差异化）：
  1. 每个 agent 跑在**独立 container**（与 messaging bridge、router 分开）；
  2. **agent 环境里不放任何凭证**——即便被 prompt injection 也无法泄露 API key（"审 PR 时任何人都能开 PR 灌入未净化输入"）；
  3. 所有出站请求经 **vault 代理**按访问策略注入凭证，并有 **human-in-the-loop 审批**（如可读邮件免批、发邮件要在 Slack 点 approve/reject）（00:08–00:10）。
- 他曾用 OpenClaw 管销售 pipeline，两天就做了"销售经理的活"，但代码库大、依赖多、明文记录所有消息让他不敢用于生产（00:06–00:07）。多位安全专家审过 NanoClaw，"没人指出核心思路的问题"（00:14）。

### 记忆：LLM Wiki 优于检索
- 个人用的就是 **LLM Wiki 式方案**——把 agent 指向 Karpathy 的帖子照做；NanoClaw 内置简化版（指示 agent 把任何实质信息存成 markdown）（00:11–00:12）。
- **检索/语义搜索不适合个人助手**：问"这周最该关注什么"没有 embedding/关键词能答；但有好的 LLM Wiki（项目、时间线、本周通话 log）就能跨文件收集给出。已知痛点：会造重复文件、需背景进程定期查重（**与本库 Lint 巡检同构**）（00:12–00:13）。

### 公司化与开放问题
- 早期采用者多是 VC/CEO/高管，"我搭好了 setup、想推给全团队但不想当那个修 agent 的 IT"→ NanoClaw Co. 做企业部署（10 人团队、100+ 公司接洽）；本质是"AI engineer 与客户 devops/安全/IT 的合作"（00:14–00:17）。
- **agent 不像传统企业软件"部署完 5 年不动"**——底座（模型）在变，必须持续升级（4.6→4.8→4.9→5），每次升级都改变行为（00:17–00:18）。
- 两个哲学问题：GitHub 会否被取代（开源被迫在 GitHub、闭源其实可全在 Slack 里 review→merge）；开源项目管理是最大挑战——coding agent 让开 PR 指数级变易、triage/review 跟不上，"**不要给我 pull request，给我 prompt request**"，一切需求/bug 汇入一个"未来开发的 wiki"作 buffer，开发时从 wiki 拉 context、完成后再推回 wiki（00:18–00:22）。

## 相关主题

- [LLM 安全](../topics/llm-security.md)（本期核心：container 隔离/无凭证 agent 环境/vault 代理/human-in-loop）
- [LLM OS 与新计算范式](../topics/llm-os.md)（个人 agent 即 OS、第二大脑、LLM Wiki 优于检索）
- [AI 实用方法论](../topics/using-llms-in-practice.md)（agent 管理学习曲线、记忆去重≈Lint）
- [AI 商业化与价值捕获](../topics/ai-business-and-value-capture.md)（个人 agent 部署生意、agent 需持续维护）
