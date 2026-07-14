---
title: "Freda的投资札记第2集：Tokenmaxxing、AI时代组织、焦虑与人的连接"
created: 2026-07-14
updated: 2026-07-14
type: summary
tags: [investment, token-economics, coding-ai, software-disruption, organization, anxiety, china-us]
sources: [sources/zhang-xiaojun/20260518-MjTfhm5N8x8/transcript.md]
confidence: high
---

# Freda 投资札记第2集

- **嘉宾**: [Freda（段）](../people/freda-duan.md)（Altimeter Capital 合伙人）

> 张小珺商业访谈录第141期。Freda（段），Altimeter Capital 合伙人，硅谷科技基金横跨一二级市场。投资案例：OpenAI、Anthropic、字节跳动、英伟达、Snowflake、Robinhood。
> 84分钟。前半段硬核投资分析，后半段谈焦虑与人的连接。whisper medium 转录。

## 核心观点

### 1. Token 经济学

**Dollar per Token 是新度量单位**（[00:02:03]）：类比工业时代的 Dollar per Kilowatt Hour。但 Token 容易误导——关键是 **Token per Task**：同一任务不同模型消耗 Token 可差几十到上百倍。

原因（[00:04:03]）：
- 输出长度差异（精练代码 100 行 vs 啰嗦代码 几千行）
- 隐藏的 Reasoning Tokens（用户看不到的中间推理）
- Agent Workflow 放大效应

**Tokenmaxxing 现状**（[00:06:03]）："现在是非常浪费的状态，但 Token 总量还会继续大幅上升——两者不矛盾。" 分解公式：AI 总投入 = 用户数 × 任务数 × Token per Task × Dollar per Token。前两项必然大涨，后两项会优化。

**收费模式必然从按 Token 收费→按效果收费**（[00:10:10]）：以 Sierra（AI 客服）为例——解决问题才收费，没解决不收。但写作等创意类仍会是按 Token。

### 2. 模型公司：Anthropic vs OpenAI

- **"负向滚雪球"框架修正**（[00:19:23]）：Dario 原框架：训练成本按 3-4x 增长 → 收入跟不上 → 越亏越多。修正：如果收入增长斜率比 3-4x 更陡，公司突然盈利。Anthropic 2026 年初需求爆发证明了这条路。
- **商业模式不是 SaaS**（[00:15:16]）：SaaS 是 subscription（按人头、封顶）→ 客户倾向只用一家。模型是 usage-based → 鼓励同时用多个 vendor、随时切换。因此 OA 和 Anthropic 的关系不是传统意义上的竞争。
- **Code in 的市场被严重低估**（[00:17:19]）：最初估算 100 亿美元（400 万 developer × $200），错得离谱——真实 TAM 是"任何可以被计算机操作的事情"。Cowork 两个人做出来已在同等规模时增长斜率超 Claude Code。
- **每个 Gigawatt 电力能产生多少模型收入被系统性低估**（[00:22:28]）：2025 年底 OpenAI 和 Anthropic 各将有 ~5 GW 算力，2026 年 ~10 GW。100 亿/GW 都算保守。
- **Anthropic inflection point**：ARR 从 10 亿→50 亿不到半年，比 OpenAI 同期快很多（[00:23:29]）。

### 3. Code in 竞赛与 "递归自我改进"

- **可能的临界点已至**（[00:12:13]）：过去两年 SOTA 模型每几个月换手，但现在 Code in agent 成熟后出现 "更好的 AI 训练下一代更好的 AI" 的闭环。"有点像马车换汽车——早期汽车也常抛锚，快马还能追；一旦汽车稳定跑起来，马就没有任何比的意义了。"
- 各巨头押注：OpenAI 重组 code in 推至极高位置、Google Sergei 亲自管、Meta 内部推 code in 模型冲 SOTA、xAI 公开收购 Cursor（[00:14:15]）。

### 4. 软件公司冲击

- **Anthropic 3000 员工 vs Salesforce 7-8 万人**（[00:27:35]）：传统软件公司人均 50 万美金收入，Anthropic 人均千万级。而且"没有一个正经的销售团队"——质疑了"软件必须靠销售"的假设。
- **脆弱性排序**（[00:30:38]）：UI 占比高的先死（point solutions、电子签、BI 工具）→ 结构化数据容易被 agent 取代（项目管理如 Monday）→ 混乱数据反而难（Excel 难以被替代）。
- **Office 还有意义吗**（[00:32:39]）：只要价值链中还有一个人需要手动修改，Office 就仍有价值。"AI 生成 HTML 版 PPT 很快，但手动拉一下拽一下还是 PPT 快。"
- **Data Warehouse 也不绝对安全**（[00:33:40]）：过去需要 Warehouse+SQL 的分析，现在直接 API+Skills 几秒钟 Token 消耗就能完成。setup 成本几乎为零。
- **新机会**（[00:34:43]）：让软件处理"决策过程中没有被记录的部分"——为什么给了 25% 折扣而不是 30%？谁被谁说服了？CFO 有什么顾虑？这些非结构化历史数据现在可以被 AI 捕获。

### 5. AI 时代的组织：接力赛变篮球赛

- **组织层级本质是信息搬运机制**（[00:39:47]）：CEO→管理层→逐层过滤传递→底层执行。开会、对齐、计划全都是翻译成本。
- **电机的历史教训**（[00:37:43]）：电机发明后 40 年才提升社会生产率——前 20 年大家只是"把电机塞进蒸汽机的位置"，工厂布局不变。直到流水线重新设计才真正释放效率。AI 当下也处于"把电机塞进蒸汽机"阶段。
- **接力赛→篮球赛**（[00:42:49]）：传统组织是接力赛（PM→Designer→Developer→QA→Sales，端到端 6 个月）。AI 后是篮球赛（3-5 人小分队，必要技能在团队内，自己做决策，只有最大问题才上报）。
- 新产品开发流程被"打地鼠"：先解决 developer bottleneck（2-3 月→2 周）→ QA 成瓶颈→裁 QA → PM 成瓶颈..."整个流程都需要重新设计。"

### 6. 投资行业变革

- **投资是"效率极低的行业"**（[00:43:51]）：大量时间花在找信息、清数据、比较预期、判断 positioning。"给 agent 足够干净足够亮的数据和清晰的交易目标，理论上 100% 会比人做得好。"
- **散户的重要性超过传统认知**（[00:45:55]）：美股交易量中量化 60-70%、散户 30%、传统机构几乎不占量。"机构也要向散户学习，因为散户是价格形成的一部分。"
- **Alpha 实现会加速到秒级**（[00:47:56]）：Event-driven 交易将几乎没做的必要——agent 秒级消化信息完成定价。

### 7. AI 创业版图：哪些方向跑出收入

（[00:49:57] 快问快答）
- **Code in**：最大，几十亿美元收入，往下断档
- **Healthcare**：~2B（Upgrade, Open Evidence）
- **Legal**：>1B（Harvey, Logora）
- **Customer Service**：接近 1B
- **Video Generation**：~几百 M
- **推理基础设施**：几个 B（Together, Fireworks）
- **芯片**：Cerebras（即将上市）、Groq（被收购）

**Neolabs 热潮**（[00:53:57]）：从 AI lab 出来的研究员自立门户，几个月内有~100 家。"因为 OA 和 Anthropic 估值接近 1 万亿，投资人想搏一个几倍回报的新标的。Acquire-hire 退出机制极好。"

**Agent 基础设施**（[00:56:58]）：Agent 不是人——发邮件、用浏览器、支付、合规的 API 都需要重新设计。Agent Mail、Agent Phone 等新品类出现。

### 8. 市场宏观

- **capex 暴增致自由现金流转负**（[01:01:02]）：按当前 capex 曲线到 2027 年，几家大厂自由现金流将全部转负。行业 1 万亿+ capex（仅表内）。"大客户和存储公司签了长约，capex 只会上修不会下修。"
- **但云厂商有回报**：Google 云收入 ~1000 亿美元对应 2000 亿 capex，约两年回本。云生意本身变差了（竞争多、价值被模型公司分走）。
- **SpaceX/OpenAI/Anthropic 三大 IPO**：合计~4 万亿美金级别，融资额~2000 亿美元，市场容量撑得住（mutual funds 账上就有 1 万亿现金+散户+主权基金）。但现有 MAG7 会承压，资金轮动。

### 9. 焦虑与人的连接

- "每天打开 Twitter 都是 You have to look at this、This is changing my life——又有新东西了，我又落后了"（[01:15:20]）
- 深夜在家装不上 OpenClaw，"一个东西装不上，就会想我连这个都装不上，什么都跟不上，是不是要被时代淘汰了"（[01:16:20]）
- **信息交换对话意义被掏空**（[01:19:24]）：95% 的信息性内容 AI 能给更好答案。人与人剩下的只有情感连接。
- Druckenmiller 被问 AI 是否导致通缩："如果你笃定这个想法，你是 arrogant 且不够 open minded"（[01:09:15]）
- "历史上人类经历了很多巨变。AI 的压迫感 vs 当年工业化取代手工农业对农民的震撼——不是一个量级"（[01:11:16]）

### 10. 投资判断复盘

- **对**：2025 年底判断今年市场最重要风向标是 OA 和 Anthropic 的收入——确实 Anthropic 收入一家撑起了市场。
- **错**：以为市场重心会从半导体接棒到 AI 应用——"完全错了，过年前和过年后完全是两个世界"（[01:01:02]）。
