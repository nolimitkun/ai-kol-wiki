# AI 与科学发现

> AI（尤其 LLM/推理模型）能否以及如何做出科学发现；人类能否理解 AI 的发现。

## 各家观点

### Adam Brown（美，Google DeepMind BlueShift，2026-07）
- 学科的**"分支因子"**决定 AI 纯思考路线的可行性：GR/弦论类（经验基础薄、靠自洽性裁剪）适合大规模并行探索假设树；凝聚态类必须实验。
- 反驳"AI 数学将不可理解"（Terry Tao 的 indigestion 担忧）：LLM 也是**超人解释器**，早期证据（Erdős 问题的非形式化可理解证明 → 人类据此证出新定理）支持乐观。
- LLM 科研性格：极端耐心、不迷信公认结论（unit distance conjecture 被 AI 反证）。
（[GR from first principles](../videos/20260710-dwarkesh-adam-brown-general-relativity.md) 01:31–01:37）

### Grant Sanderson（美，3Blue1Brown，2026-06）
- 已跨过的门槛：AI 反证 unit distance conjecture、以人类可理解思路解决 Erdős 1196——"闪电式跨域连接"正是 LLM 该擅长的（它同时是所有领域的专家）。
- 下一个门槛：出猜想、造定义——但**无法 benchmark 化**（能测的才能训），只能靠数学家社区的"语气变化"感知；Galois 式概念突破的验证回路可长达百年。
- 数学进展快的两个原因：可验证 + **grindable**（可容器化、确定性重放）；电脑操作可验证但不可刷，现实世界任务两者皆无。
- 关键分歧点：解法形态决定意义——闪电连接（易懂）、造山（需要爬山但可能是外星山）、纯苦力长推理（消化不良）。
（[AI disproved a conjecture](../videos/20260630-dwarkesh-grant-sanderson-ai-math.md)）

### 与 Adam Brown 的观点交叉
两人都提到 unit distance conjecture 案例并给出一致解读：AI 不迷信"公认为真"是结构性优势。Brown 强调 LLM 是"超人解释器"（人类能跟上）；Grant 从解释者本人的立场同意但更进一步——连解释都会被 AI 做得更好，人类剩下策展与关系性角色。

### Andrej Karpathy（美，2023-11 / 2025-02）
- 自我改进需要 reward function：可验证域（数学/代码）可以无限跑 RL、可能出现开放域的 "move 37"（人类没想过的思考策略甚至思考语言）；开放问题是可验证域练出的推理能否迁移到不可验证域。（[Deep Dive into LLMs](../videos/20250205-karpathy-deep-dive-into-llms.md) 02:42–02:48、03:28）

### Noam Brown（美，OpenAI，2026-06）
- **Erdős 单位距离猜想**：OpenAI 用内部模型以"极低成本"反证；事后发现 5.5 也能做到（需 scaffold + steer）。一个通用 scaffold 约 $1K–$100K 就可能达成——"本可由通用模型完成，只是没人往里砸 $10 万 compute"。（[No Priors 访谈](../videos/20260626-no-priors-noam-brown.md) 00:17–00:19）
- 与 Adam Brown / Grant Sanderson 的同一案例互证：三人都以"AI 不迷信公认为真的结论"为 AI-for-science 的结构性优势；Noam 补充了成本维度（每代模型发布后成本降 10–100×，故 OpenAI 有意不鼓励研究员刷开放难题，而应造更强模型）。

### 姚顺宇（中，Google DeepMind，2026-05）
- 基础科学（数学/理论物理）研究者已**大量用 AI**：Gemini Deep Think 做数学推导/证明、看文章归纳；痛点（物理学家不会写代码、光打开编译器就半天）被消除。但难成"万众瞩目"，除非出现"AI 产生爱因斯坦级理论"的时刻。（[张小珺访谈](../videos/20260511-zhang-xiaojun-yao-shunyu.md) 00:42–00:44）
- 建议年轻人做"现在没人做到的事"，点名 **AI 帮助真正的科学问题（如量子调控）** 是比纯做语言模型更蓝海的方向（03:22–03:23、03:33–03:34）。

## 中美对照

AI-for-science 目前收录的观点以美方（Adam Brown、Grant、Noam、Karpathy）为主，姚顺宇从中方一线补充了"基础科学已在广泛用 AI 工具、但难出圈"的落地现状；四方共用 Erdős 案例，构成本库里少见的跨 KOL、跨中美的同一事件多视角交叉。
