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

## 芯片微观层：从逻辑门到 systolic array（Reiner Pope，美/MatX，2026-05）

来源：[Dwarkesh 芯片设计课](../videos/20260522-dwarkesh-reiner-pope-chip-design.md)

- 为本页提供最底层的电路视角：**"最大化计算相对通信"贯穿全栈**——ALU 位宽（乘法器门数随位宽**平方**增长，是低精度算术有效的唯一根本原因）、Tensor Core/systolic array（把矩阵乘外层循环烧进硬件、权重驻留，否则 7/8 面积耗在寄存器堆搬运）、直到跨芯片推理的 batch 权衡（00:14–00:37）。与 Karpathy "flops 不重要、内存访问模式才重要" 是同一原理的上下两层。
- **"GPU 是一大堆微型 TPU 平铺"**：TPU 粗粒度（超大 MXU）摊销搬运成本但 vector↔matrix 带宽受限，GPU 细粒度灵活但单元固定开销大；MatX 押注 splittable systolic array 兼得两者（01:15–01:20）——为本页姚顺宇的 TPU/GPU 使用方对照补上设计方视角。
- TPU 用 **scratchpad（软件显式管理）替代 cache（硬件自动）**换确定性延迟（01:04–01:07）；大脑低时钟类比在硅上不成立——降频只线性省开关能耗，不带来能效跃升（01:12–01:15）。

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

## DeepSeek V4 混合注意力的推理/训练适配（SGLang·Miles 团队，中，2026-05）

来源：[月球大叔 SGLang 直播](../videos/20260501-uncle-moon-sglang-deepseek-v4.md)

一线框架工程的具体案例，把 [朱邦华](../videos/20260518-uncle-moon-banghua-zhu-sglang.md)"新架构逼出 infra 优化"落到 DeepSeek V4：

- **V4 混合稀疏注意力**：SWA（sliding window）+ Compress-4（每 4 token 压 1，hierarchical top-k 选最有影响力的）+ Compress-128（每 128 压 1，全注意力），框架要维护五类 KV cache 状态——用 **shadow radix cache**（虚拟地址映射物理状态）管理（00:04–00:09）。KV cache 大幅压缩（100 万 token < 10GB），打开 offload 到 CPU 的空间（验证 3× 上下文性能，00:20）。与本页 [罗福莉](../videos/20260424-zhang-xiaojun-luo-fuli-agent-paradigm.md) 的 hybrid attention 独立同频："系统约束使混合稀疏是大势所趋"。
- **kernel 级优化**：把 KV 压缩的 5 次内存读取里的 3 个计算融成一个算子；**lightning topk** 把长上下文 topk 从 100μs 优化到 15μs（V4 有 60 层，累计影响巨大）（00:09–00:12）。但"算子融合并非总有效"——两算子须能沿同一维度切分（00:47）。
- **并行**：长上下文用 CP（单机内快）、跨机用 PP；V4 注意力不天然支持 TP（kernel 要求头数是 64 倍数，用 padding）；已支持 PD 分离（00:12–00:19）。
- **RL 训练（Miles）比推理难 day-0 支持**：无标准 baseline、要 backward、debug 成本大；精度是最耗时环节（CP 下 KV gradient 因 compress attention 稀疏、reduction 复杂使 BF16 不够，需换 FP32）；借鉴 DeepSeek deterministic ops 消除 KL loss spike（00:22–00:35）。详见 [LLM 训练管线](llm-training-pipeline.md)。
- 月球大叔总结的方法论："做 MLSys 别只补代码小窟窿，要抽象出框架——system research 需要美感"；**数据管理是被低估的新方向**（agent 持续记忆、Dreams vs Memory），与 [江鋆晨"KV Cache 是下一个数据层"](../videos/20260609-uncle-moon-junchen-jiang-kvcache.md) 同频（01:00–01:04）。

## KV Cache 作为独立数据层（江鋆晨，中/TensorMesh·LMCache，2026-06）

来源：[月球大叔访谈](../videos/20260609-uncle-moon-junchen-jiang-kvcache.md)

- **KV Cache = 大模型的记忆 = "给大模型看的视频"**（都是 3D tensor）；押注它是继模型权重、prompt 之后**下一个最大的数据层**、"未来的石油"（00:40:55–00:43:56）。数据层普适规律：web→CDN、大数据→Spark/HDFS、AI→KV Cache（00:37:50–00:39:52）。
- **LMCache**：把 KV Cache 层与推理引擎/存储/GPU/运行环境**解耦**（不与模型解耦），做成工业界事实标准；当前可见价值 = 存下 KV Cache 避免重复计算（读长程序时 90%+ input 是那段程序，存下即跳过 90% 重算）（01:24:23–01:29:28）。类比 Spark"踩着工业界实体出来"。
- **prefill vs decode 的算力误区（反直觉）**：硬件（Cerebras/Groq/LPU）多优化 decode（用户可见"一个字一个字蹦"），但 **~90% 算力其实花在 prefill/处理 input**——agent 的 input（几十万~几百万 token）远长于 output，且"任何 output 都会变成以后的 input"（01:31:30–01:34:32）。这是对"算力大头在生成"这一直觉的直接纠偏。
- **OpenAI API 兼容格式 = AI 时代的 IPv4**：网络的"细腰"是 IP layer，其上创新极难（IPv6 更好却输给 IPv4 的既成事实）；AI 生态里 OpenAI API Compatible 的 query format 已是所有应用/模型/推理商承认的稳定接口，**KV Cache 有望成为下一个这样的标准层**（02:04:50–02:08:54）。
- **硬件"IBM 化" vs disaggregation**：厂商把处理器/网络/存储 bundle 成大型机（走 IBM 老路）以最大化 margin；但历史上大型机没成数据中心主流，真正胜出的是"把便宜部件用聪明方法连起来"；**disaggregation 做到极致**（每块特殊化、可替换）可能带来颠覆性新 infra（02:08:54–02:12:56）。这与本页 [阳萌](../videos/20260608-zhang-xiaojun-yangmeng-anker.md) 的存算一体、[Jensen](../videos/20260323-lex-jensen-huang-nvidia.md) 的 extreme co-design 构成"硬件组织形态"的三种下注方向。

## Agent Cloud 与统一存储层（Matei Zaharia & Reynold Xin，美/Databricks，2026-06）

来源：[Latent Space 访谈](../videos/20260624-latent-space-databricks-agent-cloud.md)

- **Omnigent = 跨 harness 的公共 API + agent cloud**：把 Claude Code/Codex/Cursor 等所有 harness 映射到一套 session API（收 message/file、吐 streaming/tool-call 流），上层做协作/安全/成本控制；开源以吃"众人写 integration"的网络效应（发布首周末 ~400 merge）。Zaharia 明确类比**网络协议（IP layer）而非 OS/数据库**——与 [江鋆晨"OpenAI API = IPv4 细腰"](../videos/20260609-uncle-moon-junchen-jiang-kvcache.md) 是同一"稳定接口层"直觉的两个落点（00:04–00:16）。
- **agent cloud / 不关机 sandbox**：从 lakebase 架构去掉数据库即得；需本地持久化（库不每次重装）——解决"开车还得盯 Codex session"的荒诞（00:07–00:17）。
- **"把数据放到对的地方，糊一层 AGI"**：**L-TAP** 只统一存储层（Postgres 页用空闲 CPU 转码成列式 parquet，无 CDC 管道），让 agent 实时 reason 业务数据、强 10 倍；**Dream Engine** 用 **ML 模型（非 LLM）+ 十年 trace** 从零重建数据库引擎、运行时 dispatch 最优数据结构（00:32–00:50）。这是"数据层 vs 计算层"权衡的又一形态，与本页 [江鋆晨](../videos/20260609-uncle-moon-junchen-jiang-kvcache.md) 的 KV Cache 数据层、[Reiner Pope](../videos/20260522-dwarkesh-reiner-pope-chip-design.md) 的芯片级搬运税同属"计算 vs 通信/数据"主线。

## 面向 Agent 的架构与 RL Infra（罗福莉，小米 MemoVR，2026-04）

来源：[罗福莉访谈](../videos/20260424-zhang-xiaojun-luo-fuli-agent-paradigm.md)

- **hybrid attention 取代 MLA 以适配 agent**：MLA 为 Chat 时代精妙地压 KV Cache 而生，但"没有可发挥空间"——上 MTP 会卡在 compute bound；MemoVR 用 **sliding window + full attention 混合**（Flash 5:1、Pro 拉到 **7:1**），更省 KV Cache、支持更长上下文，"更大模型可以更稀疏"（01:26:48–02:06:02）。与江鋆晨"KV Cache 是核心数据层"从模型架构侧呼应：省 KV Cache 是 agent 长上下文的关键。
- **MTP（Multi-Token Prediction）只有她们在推理时用**：因 hybrid 架构天然留大量计算富裕，用投机解码把富裕算力吃满；**MTP 被 verify、无幻觉**；Flash 做到 100–150 TPS（01:31:50–01:38:52）。MLA 模型上不了 MTP 正因为它已卡在算力/访存的完美临界点。
- **RL infra ≠ 预训练 infra**：**RL infra 必须容错**（agent 交互会莫名中断、训推不一致要容忍、要在异构集群里综合调度 GPU+CPU+存储），而预训练 infra"绝不容忍 loss spike"，两者不交融（03:30:03–03:33:04）。**"真正把 agent RL scale 起来的团队非常少，海外基本只有 Anthropic"**（03:33:04）——与朱邦华"RL environments 是新瓶颈、CPU 因 function-calling 并发变重要"精确对接。
- **卡是瓶颈**：研究:预训练:后训练 = 3:1:1，研究用卡是训练的 3–5 倍；"idea 到代码太快，卡在卡上"（01:45:55–01:48:55）。推理卡需求远高于训练卡。
- **全模态离散化**：音频用多层 RVQ 离散成 token（"另类"架构），图像离散化进行中——追求"一套 infra 服用所有模态"，但"有了 Qi-code 后重写一套 infra 也就两三周，没必要为架构统一牺牲模型结构"（02:12:05–02:14:09）。

## 模型即操作系统/基础设施（广密，2026-04）

来源：[广密·全球大模型季报第 9 集](../videos/20260415-zhang-xiaojun-guangmi-llm-quarterly-9.md)

- **最领先的三五家模型 = 世界最重要的技术基础设施 = global GDP 的操作系统**，重要性将超过今天的 Google（01:04:51–01:06:53）。详见 [LLM OS](llm-os.md)。
- **算力是 Anthropic 冲 1000 亿 AR 的最大瓶颈**（此前低估需求、算力规划保守）；**Google worst case"TPU 都能变成另一个英伟达"**（00:29:28、00:49:42）。
- **推理需求即将爆发几倍到十倍**（罗福莉同判断），"大部分卡点在存储"，低成本推理是关键命题（广密 01:16:12 / 罗福莉 02:30:21）。

## 多模态/全模态 serving：stage 抽象与 DiT 加速（vLLM Omni 团队，中，2026-05）

来源：[月球大叔访谈](../videos/20260511-uncle-moon-vllm-omni.md)

- **把 PD 分离推广成通用 "stage" 抽象**：LLM 的 prefill/decode 只是两个 stage；多模态里一个 stage 可能是多模态 encode/生成，stage 间要传的不只 KV cache，还有 embedding/metadata，**方向可双向、可跳 stage**（00:03–00:04）。这是把 [SGLang·Miles](../videos/20260501-uncle-moon-sglang-deepseek-v4.md)/[LMCache](../videos/20260609-uncle-moon-junchen-jiang-kvcache.md) 的 KV-transfer 思路推到多模态的自然延伸。
- **omni connector + 控制面/数据面解耦**：单卡走 shared memory、多卡自动走 **Mooncake**；轻控制信息与重 payload 分开传；chunkwise 异步流式把**首包延迟从近 10 秒降到 <1 秒、RTF<1**（00:28–00:33）。
- **DiT 加速**（AR 复用 vLLM、Diffusion 从头写）：TeaCache（layer 级跳步）+ block 级缓存；并行 USP+Ring Attention（正交）、HSDP、VAE patching、CFG parallel（最稳）；实测显卡算力过剩、diffusion 可 continuous batching；边缘设备做 module/layer-wise CPU offload（00:41–00:57）。
- **国产硬件插件**：CUDA/ROCm + **华为昇腾 MPU、百度昆仑**，新硬件接入不改核心 AR/Diffusion 逻辑——直接回应下方中美对照里"国产芯片主动论述待补"的缺口（00:24–00:25）。

## 半导体供应链与代工：Intel 的重整（Lip-Bu Tan，美/Intel，2026-06）

来源：[No Priors 访谈](../videos/20260618-no-priors-lip-bu-tan-intel.md)

- **瓶颈排序：电力→氦（helium）→内存→CPU/GPU**——扩产建 fab 要几年、成本会往客户传导涨价；"AI 冲击比互联网更大更深刻"（00:11–00:13）。与 Jensen"电力是首要瓶颈"一致，但补上**氦与内存短缺**两个少被提及的物理约束。
- **先进封装成新瓶颈**：EMIB-T vs TSMC CoWoS、玻璃基板（好热绝缘、Intel ~1000 模组专利）、人造金刚石；摩尔定律撞物理墙后靠新材料（GaN/SiC/InP）——与 [Reiner Pope](../videos/20260522-dwarkesh-reiner-pope-chip-design.md) 的电路级"计算 vs 通信"是产业链上下游两端（00:15–00:19）。
- **CPU 在 AI 里回潮**：训练 CPU:GPU 从 1:8 到 1:4 甚至 1:1，RL 与 agent 编排里 CPU 更好——与 [Modal](../videos/20260708-latent-space-modal-agent-infra.md)"inference inflection：GPU:CPU 摆回 1:1"、朱邦华"RL environments 让 CPU 变重要"三方独立同频（00:05）。
- **算力终局不押集中式**：看多 edge/client 算力（机器人/国防/家用），与 Jensen 的集中式"token 工厂"、Lewis Hong 的太空数据中心构成"算力放哪"的第三种下注；代工资本密集经济学详见 [AI 商业化与价值捕获](ai-business-and-value-capture.md)（00:41–00:44）。

## 晶圆级芯片与快推理（Andrew Feldman，美/Cerebras，2026-05）

来源：[No Priors 访谈](../videos/20260521-no-priors-cerebras-feldman.md)

- **"要根本性更好，架构就必须不同"**：造 46,000mm²"餐盘大小"晶圆级芯片（别人造"邮票大小"），推理比 GPU 快 15–20x；对 GPU 小改不可能快 20 倍（00:02–00:07）。为本页 [Reiner Pope](../videos/20260522-dwarkesh-reiner-pope-chip-design.md)"GPU 是一堆微型 TPU"、姚顺宇 TPU/GPU 对照补上"整片晶圆"这一极端设计点。
- **供给侧的爬坡真相**：造不出来烧了两年、每月 800 万美元；跨越 chasm 靠超算→主权基金 G42 十亿订单 battle test→OpenAI 200 亿单；制造能力今年 10x（"硬件史上最快之一"）（00:07–00:24）。与 [江鋆晨](../videos/20260609-uncle-moon-junchen-jiang-kvcache.md)"硬件（Cerebras/Groq/LPU）多优化 decode"形成互证——Feldman 正是从 decode 侧"快"切入。
- 呼应本页 Imas·Trammell 的需求侧："2025 年模型聪明到有用后需求爆炸"，"慢推理的市场是零"。

## Agent 云 / sandbox / 弹性推理（Akshat Bubna，美/Modal，2026-07）

来源：[Latent Space 访谈](../videos/20260708-latent-space-modal-agent-infra.md)

- **self-provisioning runtime**：把硬件/扩缩容写进代码 decorator（与代码 collocate），而非读几百个无类型 Kubernetes YAML；SDK 团队从"开发者体验"转向"agent 体验（AX≈DX，余弦相似度 ~0.9）"（00:04–00:07）。
- **sandbox 是 agent 的完美原语**：2023 年 5 月就做、去年才爆；**RL rollout 极 bursty（要 10 万个 sandbox）**、agent 本身反而不 bursty——与罗福莉"RL infra 必须容错"、朱邦华"RL environments 是新瓶颈"从 sandbox 供给侧对接（00:10–00:15、00:27–00:29）。
- **投机解码真相**：开源 DFlash（block-based speculator），**提升 accept length 是乘法级 2–4x 提速**（改 kernel 只有几个百分点）、不降质量；上游贡献回 SGLang（00:17–00:22）。与罗福莉"MTP 被 verify、无幻觉"同属"用富裕算力做投机解码"。
- **inference inflection**：GPU:CPU 从 8:1 摆回 ~1:1（agent 频繁 call out CPU）；capital-light 跨 17 家云建统一容量池 + 自建可靠性层，"compute strategy"团队对冲容量（类比航空对冲燃油）——与 Databricks Omnigent、[江鋆晨 disaggregation](../videos/20260609-uncle-moon-junchen-jiang-kvcache.md) 同属"agent 云 / 硬件组织形态"下注（00:24–00:47）。

## 史无前例的 buildout、推理即算力、主权与开源（Andrew Feldman / Cerebras，2026-07）

来源：[开源赢麻、AGI 已至](../videos/20260710-all-in-cerebras-bfl-open-source.md)（补 [No Priors 访谈](../videos/20260521-no-priors-cerebras-feldman.md)）

- **buildout 的物理尺度**：数据中心未来几年用电将超过"地球过去 50 年"，单栋建筑用电超中型城市，遍布美/加/北欧/中东/中亚；买家"永不满足、在追赶昨天的需求"，Cerebras **$250 亿 backlog**（00:01–00:04）。
- **推理即算力 + 推理的 Moore's law**：reasoning 是 inference、极耗 token，正好喂给快机器；Cerebras 打破 18 个月翻倍、未来 18 个月"远超 2x"（新架构还有大量优化空间，20 年老架构 GPU 只能靠更小制程）——为本页"推理是 infra 主战场"（朱邦华/江鋆晨/Modal）补上芯片侧的加速曲线（00:07–00:13）。
- **主权是趋势、开源今年闭合 gap**：Cerebras 跑 GLM/Kimi/Qwen + OpenAI 闭源 + GSK/G42/MBZUAI 自研模型；美国需要更多**本土开源模型**（现只有 OSS 12B 或中国模型可选）；OpenAI/Amazon 自研芯片是"没人喜欢依赖"（x86 依赖 Intel、GPU 依赖少数超算的教训）（00:14–00:20）。与 Lip-Bu Tan 的产业政策叙事、下文中美对照直接相扣。

## 中美对照

见 [中美 AI 生态对照](china-us-ai.md)：中国算力劣势逼出蒸馏本领与硬件供应链优势（人形机器人硬件成熟便宜）；姚顺宇提供的 TPU/GPU 对照为"国产芯片路线是否构成劣势"提供了一个"超大规模下生态劣势可被工程化抵消"的参照点。**国产芯片的主动论述现有 [vLLM Omni 团队](../videos/20260511-uncle-moon-vllm-omni.md) 从推理框架侧补上一手素材**——昇腾/昆仑通过 hardware plugin 接入、不改核心逻辑，是"国产硬件生态靠软件框架适配抹平"的具体做法。Intel（[Lip-Bu Tan](../videos/20260618-no-priors-lip-bu-tan-intel.md)）则从美方供给侧强调"本土供应链韧性、不能只依赖一两个地理玩家、政府持股是基础设施"，与中方硬件叙事构成产业政策对照。

**Infra 侧新增中方一手视角**：[朱邦华](../videos/20260518-uncle-moon-banghua-zhu-sglang.md)（推理引擎/RL 框架）、[江鋆晨](../videos/20260609-uncle-moon-junchen-jiang-kvcache.md)（KV Cache 层）与 [vLLM Omni 团队](../videos/20260511-uncle-moon-vllm-omni.md)（多模态 serving）代表"中国背景学者以开源研究组挑战工业界 AI Infra"的一支力量——技术栈紧密相邻（SGLang/vLLM/LMCache/vLLM Omni），且都判断推理、而非训练，是 infra 的主战场。[志鹏](../videos/20260517-uncle-moon-zhipeng-vllm-contributor.md) 从贡献者侧补上一手 serving 工程碎片（diffusion 蒸馏减步、CFG parallel、layerwise/modelwise、五级测试、内部 fork 的 rebase 指数级变难→**接口层贡献开源、保留 proprietary modeling layer**），并展示了中方开源社区**低门槛 onboarding**（租卡/小模型/铁巴学习法）如何把零基础工程师一年内变成 committer。
