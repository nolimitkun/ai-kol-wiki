# AI 算力与基础设施

> 算力、电力、供应链、数据中心——AI 革命的物理层。

## Jensen Huang（美/NVIDIA，2026-03）

来源：[Lex #494](../videos/20260323-lex-jensen-huang-nvidia.md)

- **Extreme co-design**：问题装不进单机后，必须跨全栈（芯片→网络→供电冷却→系统软件→算法）协同设计，否则 Amdahl's Law 卡死；十年 100 万倍 vs 摩尔定律 100 倍。
- **电力是首要瓶颈**，但优先解法是制度性的：电网为最坏情况设计、99% 时间闲置约 40% 容量——数据中心签"可降级"合约吃存量电力；阻碍是客户的六个九合约文化。太空数据中心在做工程储备但属远期。
- **供应链即信念网络**：提前数年向上下游 CEO 灌输需求（HBM、LPDDR 进数据中心的例子）；NVLink-72 把超算组装搬进供应链（周产 ~200 pod，1 rack = 130 万零件、200 家供应商）。
- **Token 工厂**：计算机从仓库变工厂，token 分层定价；每年 token 成本降一个数量级（tokens/sec/watt 是核心指标）。

## Karpathy 的互补视角（美，2024-06）

工程底层的呼应：深度学习负载多数是 **memory-bound**，"flops 不重要，内存访问模式才重要"（FlashAttention 多算 flops 反而快 7.6 倍）；GPU 优化阶梯（精度/编译/kernel fusion/nice numbers）合计 11 倍。（[Let's reproduce GPT-2](../videos/20240609-karpathy-lets-reproduce-gpt2.md)）

## 中美对照

（待补充：中方 KOL 对算力约束、国产芯片路线的论述。）
