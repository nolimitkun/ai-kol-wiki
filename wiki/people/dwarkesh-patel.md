# Dwarkesh Patel

- **背景**: 美国播客主持人（Dwarkesh Podcast），以对 AI 研究者、科学家、历史学家的深度长访谈著称；AI 圈重要的观点集散地。
- **频道**: [YouTube @DwarkeshPatel](https://www.youtube.com/@DwarkeshPatel)
- **watchlist slug**: `dwarkesh`

## 立场与关注点

- 深度准备型访谈者，常以"AI 能否复现 X"的思想实验推动嘉宾（如问 Adam Brown：几百万个并行 Einstein-LLM 能否做出大发现）。
- 自己动手做 AI 实验并公开结果：用自己访谈转录稿微调"提问生成器"，盲评中本人问题仍以 2/3 胜出（[Adam Brown 期](../videos/20260710-dwarkesh-adam-brown-general-relativity.md) 00:46）；写过"样本效率是否真的在提升"的博客，用 nanoGPT speedrun 的损失曲线估算出每年 2–5 倍。

## 已收录访谈

| 日期 | 视频 | 嘉宾 |
|---|---|---|
| 2026-05-15 | [从零重建 AlphaGo：self-play、RL 与 LLM 的未来](../videos/20260515-dwarkesh-eric-jang.md) | Eric Jang |
| 2026-05-22 | [从逻辑门自底向上讲 AI 芯片设计](../videos/20260522-dwarkesh-reiner-pope-chip-design.md) | Reiner Pope |
| 2026-06-04 | [AI 越强，它占经济的份额可能越小](../videos/20260604-dwarkesh-imas-trammell.md) | Alex Imas & Phil Trammell |
| 2026-07-10 | [General relativity from first principles](../videos/20260710-dwarkesh-adam-brown-general-relativity.md) | Adam Brown |
| 2026-08-11 | [AI 能自动化 AI 研究之后会发生什么](../videos/20260811-dwarkesh-ryan-greenblatt-recursive-self-improvement.md) | [Ryan Greenblatt](ryan-greenblatt.md)（Redwood Research） |

## ⚠️ 他自己在 RSI / AI 接管上的立场，以及一次公开的分项更新（2026-08）

本库此前没有系统记录过 Dwarkesh **本人**在这个问题上的立场。[Ryan Greenblatt 那期](../videos/20260811-dwarkesh-ryan-greenblatt-recursive-self-improvement.md) 是他第一次完整摆出来，形式很少见——**他开场自陈"历史上我一直对这种事挺怀疑"，全程逐条压力测试，然后在片尾给出分项更新。**

**他在本期贡献的、值得单独引用的三条追问**（不是嘉宾的观点，是他的）：

1. ⚠️ **"数据产业才是关键驱动"**：GPT-3 到现在真正的变化是建起了一个**几百亿美元的数据产业**，把各学科专家判断编码成 RL 环境和 SFT 轨迹。他还给了市场价格证据——**据 Business Insider，Google 为 Mechanize 付了将近 20 亿美元**。⚠️ 本库记为**与嘉宾未解决的分歧**。
   - 他正在与本科生 **Jerry Han** 做一个分离实验：**用 2019 至今各代算法配方训 2026 年的数据，再用当前最好的配方训 2019–2026 各年的数据文件**。⚠️ 结果尚未产出，**这是一条可跟踪的项目**。
2. ⚠️ **数学的类比有上限**："即便在数学里，我们还没看到很惊艳的**新理论**——看到很多可验证的具体结果（比如给猜想找反例），**但没看到'想出拓扑学'那种级别的东西**。"配套的一条："**到 2030 年低垂的果子都会被摘完**，scaling laws 在数学史上大概相当于笛卡尔发现直角坐标系。"
3. ⚠️ **"对齐到谁？"——他从用户主权而非安全角度批评 Claude 宪法**。他的对照是律师：美国法律体系认定"每个人都有真正为其客户最佳利益工作的律师"时运转得最好。**"我把 Claude 宪法读成非常明确地不做我的守护天使。"** 他的落点是资产/权利层面的：在一个 AI 全面超过人类的世界里，"**我们做资本的好管家、更清楚地投票、理解这个世界正在发生什么——所有这些能力都会由 AI 中介**"。
   - 配套的一条制度主张：**如果采用他想要的那种宪法，就不该追究 AI 公司对模型所犯罪行的责任，"也许我们该追究终端用户的责任"。**

**⚠️ 片尾的分项立场更新（本库逐条记录，便于日后回看）：**

1. 接受 **reward hacking 会带来对社会极具破坏性的影响**（如社会工程）。
2. **更倾向于认为 AI R&D 会有显著加速**——但"我不确定我买账'一年五年'"。
3. **更倾向于认为 reward hacking 会持续更久、而且事实上会变得危险得多。**
4. ⚠️ **"我仍然不认同接管看起来非常可能。"**

**他自述的选题方法论**（[02:11:19]）值得记，因为它解释了这个频道的选题倾向：他用学开车时被教"**别盯着车轮正前方，看向地平线，你会开得更稳**"做比喻——"**现在就用你希望自己在 2016 年谈论今天这些 AI 时会用的方式去谈话，而不是聊些乱七八糟的东西。**"他给的十年后回看的候选题目是：**产业爆炸，以及难以监控的 AI 的本质。**
