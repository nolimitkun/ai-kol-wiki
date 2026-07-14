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

## TPU vs GPU（姚顺宇，Google DeepMind，2026-05）

来源：[张小珺访谈](../videos/20260511-zhang-xiaojun-yao-shunyu.md)

- 大规模商用下**无绝对优劣**。设计理念差异：GPU（Hopper/H 系列）一个 pod 内约 8 卡两两 NVLink 高速互联；**TPU 抛弃两两互联、采 3D Torus 拓扑**，尽量多卡放一个架子，编译器/sharding 写得好则等效更大存储 + 减少通信 bound。
- TPU 劣势：小 scale 更固定、通用性弱、无开源生态——但"大规模自用时生态不是问题，跑几十万张卡的集群，搭基础设施不是多大的事"（03:20–03:23）。
- 这与 Jensen 从 NVIDIA 侧强调的 NVLink-72/install-base 生态形成对照：姚从使用方视角认为在超大规模下 TPU 的封闭生态不构成实质劣势。

## test-time compute 的经济性（Noam Brown，OpenAI，2026-06）

- 模型能力成为"投入金钱的函数"，把**推理时算力**变成基础设施的一等成本项；评估长任务"可能要跑一年"，与算力/时间预算直接冲突（[No Priors 访谈](../videos/20260626-no-priors-noam-brown.md) 00:12–00:16）。呼应 Jensen"token 工厂 / tokens-per-sec-per-watt"的世界观。

## 算力需求的经济学：Moore 定律"价值减半"与机会成本反转（Imas & Trammell，2026-06）

来源：[Dwarkesh 访谈](../videos/20260604-dwarkesh-imas-trammell.md)

- Moore 定律的悲观解读："每 18 个月**计算的价值**减半——我们消耗算力用途的速度快到刚好维持摩尔定律"；Chad Jones 的结论是经济中付给算力（晶体管）的份额一直在下降（00:13–00:15）。
- 但可能出现拐点：**H100 租金比三年前更高**——模型越聪明，算力的机会成本越高，即"资本用途的新品类（increasing variety）不断出现"让需求不饱和；若持续，付给算力的经济份额会持续上升（00:14–00:16）。这为 Jensen"token 工厂 / 每年 token 成本降一个数量级"提供了一个需求侧的经济学镜像：**供给侧成本在降，但用途在爆炸**。

## capex 的物理上限与"模型只相关 3–9 个月"（Benedict Evans，前 a16z，2026-06）

来源：[a16z 访谈](../videos/20260608-a16z-benedict-evans-ai-economics.md)

- 微软/Meta/Google 今年 capex 均超营收 **50%**（电信才 15–20%），四大指引约 **7000 亿美元/年**——与油气（7000 亿–1 万亿）同量级，"很多钱但非天量"（00:48–00:49）。
- 但存在硬顶："**不可能一年花 10 万亿美元在 AI 基础设施上，因为世界上没有 10 万亿可花**"；1.5 万亿只能借、不可持续 → 增长终将放缓（00:49）。
- 贯穿其分析的一条线：**模型只在 3–9 个月内相关，却要花数十亿造，还得永远追下一个**——这放大了基础设施投资相对回报窗口的不匹配（00:50）。与 Jensen"token 工厂/每年成本降一个数量级"是供给侧乐观，与本节 Imas·Trammell 的需求侧"用途爆炸让算力份额上升"共同构成 capex 是否可持续的两面。价值捕获视角详见 [AI 商业化与价值捕获](ai-business-and-value-capture.md)。

## 中美对照

见 [中美 AI 生态对照](china-us-ai.md)：中国算力劣势逼出蒸馏本领与硬件供应链优势（人形机器人硬件成熟便宜）；姚顺宇提供的 TPU/GPU 对照为"国产芯片路线是否构成劣势"提供了一个"超大规模下生态劣势可被工程化抵消"的参照点。国产芯片的**主动**论述仍待中方素材补充。
