# Zico Kolter & Matt Fredrikson（Gray Swan 联合创始人）

- **背景**: 两位均为 Carnegie Mellon University（CMU）教授，深耕对抗机器学习与 AI 安全十余年。**Zico Kolter** 亦为 OpenAI 董事会成员、鲁棒性/可证明防御方向的知名学者；**Matt Fredrikson** 早期研究可形式化验证的安全代码，受 Ian Goodfellow 对抗样本工作启发进入该领域。
- **公司**: [Gray Swan](https://www.grayswan.ai/)——"让每个人安全地使用 AI"，产品为 Arena（红队社区）、Shade（自动化红队模型）、Signal/Cygnal（防御性过滤模型）。
- **channel slug**: 作为 `latent-space` 频道嘉宾收录。

## 立场与关注点

- **AI 系统有固有的、不同于传统软件的漏洞**：会像人一样被"骗"，需要全新的安全思维。
- **鲁棒性不随规模自动增长**：把模型做大不会更抗越狱，安全性必须被显式训练——这是与"能力随 scale 提升"相反的重要事实。
- **相关性失败**是系统性风险：人人都用少数几个模型（Codex、Claude Code、OpenClaw），单点漏洞即成全局 exploit。
- 对 mechinterp 与形式化验证新近乐观：agent 能自动化、成规模地做这些"一直不是不可能、只是缺人力"的工作。
- 哲学观：LLM 是**智能的、但是"异类智能"（alien intelligence）**，不认为其有意识；对抗攻击恰恰凸显了它与人类栽在完全不同的地方。

## 呼应与分歧

- 与 [Noam Brown](noam-brown.md)（安全评估的 test-time compute 缺口）、[Mark Chen](mark-chen.md)（evals crisis、bench maxing）在"评估/安全是需要专门投入、不随 scale 自动到位的能力"上高度一致。
- 与 [Andrej Karpathy](andrej-karpathy.md) 2023 年对 LLM 安全"持续 cat-and-mouse"的判断一脉相承，并把攻防推进到 agent/computer use 时代（IPI、lethal trifecta、agent identity）。
- "用 agent 自动化 AI 研究本身"的主张，与 [Mark Chen](mark-chen.md) 的 vibe researcher、[姚顺宇](yao-shunyu.md) 对科研自动化的观察相呼应。

## 已收录访谈

| 日期 | 视频 | 频道 |
|---|---|---|
| 2026-06-22 | [Codex/Claude Code 之后的 AI 安全](../videos/20260622-latent-space-gray-swan.md) | Latent Space |
