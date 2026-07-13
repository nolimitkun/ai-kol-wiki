# Noam Brown：超大规模 test-time compute 如何改变 Benchmark、安全与研究（No Priors，2026-06-26）

- **嘉宾**: [Noam Brown](../people/noam-brown.md)（OpenAI 研究员，推理 reasoning 方向奠基人之一）
- **主持**: [Sarah Guo](../people/no-priors-hosts.md)（No Priors）
- **来源**: [YouTube](https://www.youtube.com/watch?v=AZrU6y3pUcU) · 36 分钟
- **转录稿**: [sources/no-priors/20260626-AZrU6y3pUcU](../../sources/no-priors/20260626-AZrU6y3pUcU/transcript.md)

## 概要

围绕 Noam Brown 新写的一篇文章展开：test-time（推理时）compute 大规模化后，现有 benchmark 评估方式、安全评估框架、以及对递归自我改进（RSI）的判断都需要重估。

## 核心观点

### Benchmark 评估的"坏均衡"
- 5.5 发布初期被质疑（benchmark grid 上只比 5.4 高几个百分点），但真正原因是 **grid 没有控制 test-time compute**——5.5 思考更高效，控制思考量后才看出是大跳跃（00:01–00:03）。
- 正确评估方式：要么给定 budget（token/成本/时间），要么把性能画成 **test-time compute 的函数**。现代模型 scaffold 得当可"思考数周乃至数月"，plateau 点太远、无法合理测到（00:03–00:04）。
- **Benchmark maxing**：把多个模型 scaffold 起来（best-of-5、判官选优）能在纸面上显著提分，但控制 test-time compute 后未必更好——"有点误导"；缓解手段是保留私有 held-out 集，且"benchmark 一旦公开就已在被优化"（00:07–00:08）。

### 安全评估的缺口（"inconvenient truth"）
- 各家的 responsible scaling policy / preparedness framework 大多诞生于 ChatGPT 时代，**没有考虑 test-time compute**——GPT-3 时代给再多钱也做不了多少，现在"模型能力是投入金钱的函数"（$10 → $10K → $10M 能力递增）。政策没回答"应该在什么 budget 下评估模型的危险能力"（00:11–00:14）。
- 与能力问题镜像：模型若在大 budget 下对有用任务持续不饱和，对"我们不希望它做的任务"（如生物武器）也会如此；而模型发布周期（几天到几周）已与"要跑一年才能真正评估长任务"的现实脱节（00:13–00:16）。

### 已发布模型里"未被充分挖掘"的能力
- **Erdős 单位距离猜想**：OpenAI 用内部模型以"极低成本"反证；事后发现 5.5 也能做到（需 scaffold + steer：让它列策略、逐个深挖）。一个通用 scaffold 大约 $1K–$100K 就可能达成——"在我们做之前，本可由通用模型完成，只是没人探索过往 5.5 里砸 $10 万 compute 会怎样"（00:17–00:19）。
- 但 OpenAI **有意不鼓励**研究员把时间全花在"用现有模型刷开放数学/物理难题"上，因为每代模型发布后成本降 10–100×，重点应放在"造更强的模型、尽快安全地交给全世界的科学家"（00:19–00:21）。

### RSI 与 takeoff：不认为会隔夜爆炸
- 不同 benchmark 处于两个极端之间：**Sudoku 型**（随机试错，给更多 compute 必然提升）vs **事实检索型**（记不住林肯生日，想一周也没用）；多数任务居中（00:21–00:23）。
- 模型目前**没有好的 research taste**，是研究员的补充而非替代（poker solver 例子：5.2 会"gaslighting"、需反复核对；5.5 已能近乎 zero-shot 做 river solver，但仍造不出超越已有工作的新算法）（00:08–00:11、00:23–00:25）。
- 不认为会有"隔夜智能爆炸"：正因为模型要靠**大规模 test-time compute** 才能发挥最强能力，**时间本身成为瓶颈**——是渐进 takeoff。"所有实验室最大的瓶颈都是时间，这就是研究员们如此拼命的原因"（00:25–00:27）。

### Multi-agent 与"三个王国"竞争
- Multi-agent"在足够规模下"潜力大；类比人类文明——不是变聪明，而是**亿万人跨时间积累并相互构建知识**；而 AI 模型"生于短 context window、很快消失"，Multbook/OpenClaw 是协调化的早期苗头（00:27–00:29）。
- 前沿"三王国"竞争激烈但更像"研究员苦干、做高 taste 的算法/投资/compute/policy 决策"，而非某家一夜 hard takeoff；令他安慰的是各前沿实验室都清楚利害（00:29–00:31）。
- 日常使用：已信任模型做税务建议、买房 paperwork——"某种程度上比信任人类专家还多"（00:30–00:31）。

## 相关主题

- [评估与 Benchmark](../topics/evaluation-and-benchmarks.md)（本期核心）
- [LLM 训练管线](../topics/llm-training-pipeline.md)（test-time compute、RSI）
- [AI 与科学发现](../topics/ai-for-science.md)（Erdős 单位距离猜想）
- [LLM 安全](../topics/llm-security.md)（安全评估框架的 test-time compute 缺口）
