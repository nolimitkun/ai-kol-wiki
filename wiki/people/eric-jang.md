# Eric Jang

- **背景**: 机器学习/机器人研究者。曾任 **1X Technologies** AI 副总裁，此前为 **Google DeepMind Robotics** 资深研究科学家（QT-Opt 等机器人 RL 工作）。个人站 evjang.com，GitHub `ericjang`（AutoGo 复现仓库）。
- **channel slug**: 作为 `dwarkesh` 频道嘉宾收录。

## 立场与关注点

- 深耕 **RL / self-play / 机器人**；擅长把经典算法（AlphaGo/MCTS、DAgger、Q-learning、TD、best-response self-play）与今天的 LLM RL 做原理级对照。
- 核心判断：**LLM 的 policy-gradient RL 样本效率极低**（"用吸管吸监督信号"、bits-per-FLOP 差），而 AlphaGo 的 MCTS 之所以优雅，是因为它永远在"改进后的标签上做监督学习"、从不需从 0% 成功率解探索难题。
- 对"**AI 自动化 AI 研究**"持乐观但清醒的一线态度：当前模型擅长开放式超参优化与执行实验，短板在"选下一个实验"的横向/第一性原理思考。
- 相信"神经网络把近乎 NP 难的搜索摊销进前向传播"是被低估的深刻现象（AlphaGo/AlphaFold），并由此质疑用最坏情况复杂度框定问题的传统思路。

## 呼应与分歧

- 与 [姚顺宇](yao-shunyu.md)：都强调**蒸馏/追赶远比抢先便宜**、软标签信息量大（软蒸/硬蒸）；都谈到 TPU 的长期赌注。
- 与 [Mark Chen](mark-chen.md)、[Noam Brown](noam-brown.md)、[Gray Swan](gray-swan-founders.md)：共同把"research taste / 选实验方向 / 横向思考"标定为 AI 自动化科研的当前边界，并看好用可验证环境训练"自动化科学家"。
- 与 [Andrej Karpathy](andrej-karpathy.md)：直接引用其"用吸管吸取监督信号"的比喻，并延伸到 bits-per-FLOP 的量化框架；都认为可验证域（Go/数学/代码）是 RL 的沃土。

## 已收录访谈

| 日期 | 视频 | 频道 |
|---|---|---|
| 2026-05-15 | [从零重建 AlphaGo，谈 self-play、RL 与 LLM 的未来](../videos/20260515-dwarkesh-eric-jang.md) | Dwarkesh |
