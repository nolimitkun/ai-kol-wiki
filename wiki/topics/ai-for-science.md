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

### Eric Jang（美，前 DeepMind Robotics，2026-05）
- **神经网络把近乎 NP 难的搜索摊销进一次前向传播**（AlphaGo/AlphaFold 同理）：10 层网络逼近 361³⁰⁰ 量级的搜索，令他怀疑"用最坏情况复杂度框定 NP 难问题"的传统思路不完整——现实问题大多有结构（[Dwarkesh 访谈](../videos/20260515-dwarkesh-eric-jang.md) 01:16–01:19）。类比混沌天气：真正可预测的是**宏观结构**（飓风位置、Lorenz 吸引子形状）而非微观态，value 函数正是在预测这种宏观量（01:19–01:22）。
- **AI 自动化 AI 研究**的一线观察：Opus 4.6/4.7 擅长开放式超参优化与执行实验，短板在"选下一个实验"的横向/第一性原理思考；引 Ilya——好研究员靠对"正确想法"的强信念分辨 bug 与错误想法（02:22–02:28）。与 Noam（research taste 是短板）、[Gray Swan](../videos/20260622-latent-space-gray-swan.md)（用 agent 自动化科学）、[Mark Chen](../people/mark-chen.md)（vibe researcher）同题。

### Zuckerberg / Priscilla Chan / Alex Reeves（美，CZI Biohub，2026-06）：世界模型路线
来源：[CZI 虚拟生物学访谈](../videos/20260610-no-priors-zuckerberg-czi-biology.md)
- 与 Adam Brown/Noam Brown 的"**推理模型**做发现"是**另一条路径**——**世界模型**路线：自底向上（蛋白质→细胞→系统）建生物学表征。ESM Fold 用语言模型式训练（数十亿蛋白质序列），生物结构/功能与**蛋白质设计能力是涌现的**（"只设计了理解蛋白质的模型，抗体设计作为涌现属性出现"）（00:29–00:32）。
- **数据是核心约束，不是算力**：生物学数据不在互联网上，得发明新科学方法（成像/细胞工程/测量设备）去造数据——所以 AI 前沿必须与 wet lab 前沿绑成单一团队。这与 LLM"互联网数据现成"形成鲜明对照，也解释了生物模型为何更小（00:04–00:18）。
- **mech interp 从 LLM 迁移到生物学**：把 Anthropic 式可解释性工具用于蛋白质语言模型，在已知/未知蛋白间"连点"、揭示新机制——是"打开黑箱提取新科学知识"的具体实践（00:14–00:16）。
- **闭环 vs 开环**（Elad Gil）：code/research 是闭环（迭代快），生物学是开环——CZI 的关键贡献是"闭上与真实生物学的回路"（00:54）。呼应 Grant Sanderson 的"可验证 + grindable"框架：生物学两者都缺，故必须靠 wet lab 硬造反馈。

## 中美对照

AI-for-science 目前收录的观点以美方（Adam Brown、Grant、Noam、Karpathy）为主，姚顺宇从中方一线补充了"基础科学已在广泛用 AI 工具、但难出圈"的落地现状；四方共用 Erdős 案例，构成本库里少见的跨 KOL、跨中美的同一事件多视角交叉。
