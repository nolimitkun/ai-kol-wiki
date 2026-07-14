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

## 端侧AI芯片：从冯诺依曼到存算一体（阳萌，中/安克，2026-06）

来源：[张小珺访谈](../videos/20260608-zhang-xiaojun-yangmeng-anker.md)

- **三个底层变革叠加**（[01:03:43]）：解题方法（分治法→端到端）、软件形态（程序+数据→神经网络）、硬件架构（冯诺依曼存算分离→存算一体），"构成了一个特别稳定的三角，端到端时代这个三角应该被打破"。
- **类比大脑**（[01:09:45]）：人脑不存在"把左脑知识搬到右脑计算"的问题——存算一体。冯诺依曼架构下每帧都要把所有参数从内存搬到NPU，"搬运本身就是最大功耗"。
- **2026年5月量产**：4M参数总量、单个模型~2M参数的存算芯片，用于耳机通话降噪。"一颗市面上不存在的、这个领域第一颗应用到产品上的芯片"（[01:16:52]）。
- **分层芯片路线**（[01:21:53]）：百万参数（感知/控制器官）→ 数十亿参数（大脑）→ 未来可能承载具身大脑。"不是做芯片公司，是芯片+模型+产品的闭环"——类比苹果A/M系、华为麒麟（[01:22:53]）。路线与NVIDIA差异化：NVIDIA在训练侧+万忆级推理，存算在推理侧百万到百亿参数。

## 太空数据中心：绕过地球电网瓶颈（Lewis Hong，前SpaceX，2026-06）

来源：[张小珺访谈](../videos/20260613-zhang-xiaojun-spacex-lewis.md)

- **地球瓶颈**（[01:15:19]）：美国电网仅三大区域（东岸/西岸/德州），大部分设施30年以上，AI之前已有25-40%缺口；数据中心permit周期极长、电难以available。
- **太空优势**（[01:17:21]）：(1) 真空中信号传输比任何光纤快一倍；(2) 无尽太阳能，转换效率比地面高10%+；(3) 无permit限制，唯瓶颈是自己的发射能力。
- **xAI并入SpaceX的逻辑**：不是偶然——用Starlink的低轨"数据高速公路"+太空数据中心解决算力瓶颈。（[01:19:23]："2014年马斯克就买了X.com域名"——Lewis暗示所有公司构成统一大计划。）
- 与Jensen Huang"太空数据中心属远期"的判断形成对照：Jensen从制度视角（合约/六个九）认为地面先吃存量电力，Lewis从物理+工程视角认为太空是确定性方向。

## 推理引擎与 RL 训练 Infra（朱邦华，中/SGLang 母公司，2026-05）

来源：[月球大叔访谈](../videos/20260518-uncle-moon-banghua-zhu-sglang.md)

- **需求排序 pre-training < RL < 推理**：推理是最大需求（所有用 AI 处都要 inference），故 SGLang 母公司从推理引擎切入，逐步做 RL、乃至 pre-training 的 inference（00:05:02）。这与 [江鋆晨](../videos/20260609-uncle-moon-junchen-jiang-kvcache.md)"training infra 太一次性、模型绝大多数生命周期在推理"是同一判断。
- **RL environments 是被忽视的新瓶颈**：agent 环境越复杂，bottleneck 常在 function calling 的 latency/concurrency——这是"为什么大家突然发现 CPU 很重要"（code execution / multi-docker 的 CPU 调度）；reward 设计是"艺术问题"（00:24:25–00:25:26）。硅谷已有一批 RL 环境公司（如 E2B），国内偏少。
- **新架构逼出 infra 优化**：DeepSeek V4 的架构创新（sparse attention 等）逼 SGLang 做 **shadow radix**（prefix cache）与 sparse attention 优化，"划走公司一半人精力"，把 V4 性能优化了很多倍；SGLang"day one 支持新模型"（00:19:16–00:21:21）。
- **"卡养人"**：千卡/万卡训练对 fault tolerance、MFU、accuracy 的 infra 要求与小规模完全不同——这是 frontier lab 人才稀缺的根源；"本科生摸够卡会比 PhD 干得好"（00:43:47–00:45:47）。呼应 [姚顺宇](../videos/20260511-zhang-xiaojun-yao-shunyu.md)。

## KV Cache 作为独立数据层（江鋆晨，中/TensorMesh·LMCache，2026-06）

来源：[月球大叔访谈](../videos/20260609-uncle-moon-junchen-jiang-kvcache.md)

- **KV Cache = 大模型的记忆 = "给大模型看的视频"**（都是 3D tensor）；押注它是继模型权重、prompt 之后**下一个最大的数据层**、"未来的石油"（00:40:55–00:43:56）。数据层普适规律：web→CDN、大数据→Spark/HDFS、AI→KV Cache（00:37:50–00:39:52）。
- **LMCache**：把 KV Cache 层与推理引擎/存储/GPU/运行环境**解耦**（不与模型解耦），做成工业界事实标准；当前可见价值 = 存下 KV Cache 避免重复计算（读长程序时 90%+ input 是那段程序，存下即跳过 90% 重算）（01:24:23–01:29:28）。类比 Spark"踩着工业界实体出来"。
- **prefill vs decode 的算力误区（反直觉）**：硬件（Cerebras/Groq/LPU）多优化 decode（用户可见"一个字一个字蹦"），但 **~90% 算力其实花在 prefill/处理 input**——agent 的 input（几十万~几百万 token）远长于 output，且"任何 output 都会变成以后的 input"（01:31:30–01:34:32）。这是对"算力大头在生成"这一直觉的直接纠偏。
- **OpenAI API 兼容格式 = AI 时代的 IPv4**：网络的"细腰"是 IP layer，其上创新极难（IPv6 更好却输给 IPv4 的既成事实）；AI 生态里 OpenAI API Compatible 的 query format 已是所有应用/模型/推理商承认的稳定接口，**KV Cache 有望成为下一个这样的标准层**（02:04:50–02:08:54）。
- **硬件"IBM 化" vs disaggregation**：厂商把处理器/网络/存储 bundle 成大型机（走 IBM 老路）以最大化 margin；但历史上大型机没成数据中心主流，真正胜出的是"把便宜部件用聪明方法连起来"；**disaggregation 做到极致**（每块特殊化、可替换）可能带来颠覆性新 infra（02:08:54–02:12:56）。这与本页 [阳萌](../videos/20260608-zhang-xiaojun-yangmeng-anker.md) 的存算一体、[Jensen](../videos/20260323-lex-jensen-huang-nvidia.md) 的 extreme co-design 构成"硬件组织形态"的三种下注方向。

## 中美对照

见 [中美 AI 生态对照](china-us-ai.md)：中国算力劣势逼出蒸馏本领与硬件供应链优势（人形机器人硬件成熟便宜）；姚顺宇提供的 TPU/GPU 对照为"国产芯片路线是否构成劣势"提供了一个"超大规模下生态劣势可被工程化抵消"的参照点。国产芯片的**主动**论述仍待中方素材补充。

**Infra 侧新增中方一手视角**：[朱邦华](../videos/20260518-uncle-moon-banghua-zhu-sglang.md)（推理引擎/RL 框架）与 [江鋆晨](../videos/20260609-uncle-moon-junchen-jiang-kvcache.md)（KV Cache 层）代表"中国背景学者以开源研究组挑战工业界 AI Infra"的一支力量——两人的项目（SGLang/vLLM、LMCache）技术栈紧密相邻，且都判断推理、而非训练，是 infra 的主战场。
