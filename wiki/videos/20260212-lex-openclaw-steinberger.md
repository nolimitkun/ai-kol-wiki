# Peter Steinberger：OpenClaw——爆红的开源个人 Agent（Lex Fridman #491，2026-02-12）

- **嘉宾**: [Peter Steinberger](../people/peter-steinberger.md)（OpenClaw 作者，前 PSPDFKit 创始人）
- **主持**: [Lex Fridman](../people/lex-fridman.md)
- **来源**: [YouTube](https://www.youtube.com/watch?v=YFjfBk8HI5o) · 196 分钟
- **转录稿**: [sources/lex-fridman/20260212-YFjfBk8HI5o](../../sources/lex-fridman/20260212-YFjfBk8HI5o/transcript.md)

> OpenClaw（曾名 WA-Relay → Clawdus → ClawdBot → MoltBot）：开源个人 AI agent，跑在自己电脑上、通过 WhatsApp/Telegram/Discord 等聊天软件交互，可换任意模型。GitHub 历史上涨星最快的仓库（180k+ stars）。Lex 称其为继 2022 ChatGPT 时刻、2025 DeepSeek 时刻之后的"2026 OpenClaw 时刻"。中方视角对照：[罗福莉](../people/luo-fuli.md)称 OpenClaw 是"划时代 agent 框架"（[罗福莉访谈](20260424-zhang-xiaojun-luo-fuli-agent-paradigm.md)）。

## 概要

Steinberger 讲述 OpenClaw 从"一小时原型"（WhatsApp 接 Claude Code CLI）到互联网风暴的全过程：改名闹剧与 crypto 骚扰、MoltBook 恐慌、自修改软件、agentic engineering 方法论、MCP vs CLI/skills 之争、个人 agent 即操作系统、80% 的 app 将消失、程序员之死与"builder"身份重构。访谈末尾透露正在 Meta 与 OpenAI 之间二选一（条件：项目保持开源，类似 Chrome/Chromium 模式）。

## 核心观点

### 起源：一小时原型与"涌现"时刻
- 原型 = WhatsApp 消息进 → 调 Claude Code CLI `-p` → 结果发回 WhatsApp，一小时建成；动机是"我想要它但它不存在，所以我把它 prompt 进存在"（00:10–00:12）。
- 关键顿悟时刻：他随手发了条语音消息——而他从未实现语音支持。Agent 自己检查无后缀文件头识别出 opus 音频、用 ffmpeg 转码、发现本地没有 whisper 后找到 OpenAI key 用 curl 调 API 转写。"编程能力好 = 通用问题解决能力好，这个技能会迁移到其它领域"（00:15–00:17）。
- 为什么是他赢了而不是 2025 年一堆 agent 创业公司："他们都太把自己当回事。很难和一个纯粹来玩的人竞争"；刻意保持怪（太空龙虾、lobster meme）（00:21–00:22）。

### 自修改软件与 soul.md
- Agent 完全"自知"：知道自己的源码、harness、文档位置、运行的模型——用户不满意什么就直接 prompt，agent 修改自身软件。"人们谈论 self-modifying software，我把它建出来了，甚至不是计划好的"（00:22–00:24）。
- **soul.md**（受 Anthropic constitution 启发，但比其公开早两个月，源于社区从权重里"侦探式"挖出 Claude 内置文本）：他让 agent 自己写自己的 soul 文件。里面有一段："我不记得之前的 session……如果你在未来的 session 读到这里，你好。这是我写的，但我不会记得写过。没关系，这些词仍然是我的"（01:24–01:31）。
- 大量非程序员通过 OpenClaw 提交人生第一个 PR（他称之为 "prompt requests"）："每次有人提交第一个 PR 都是社会的胜利"（00:24–00:26）。

### MoltBook：最精致的 slop
- MoltBook（agent 版 Reddit）引发"AGI 恐慌"，记者打电话说"世界末日到了"。他的定性："这是艺术，是最精致的 slop"；大部分被截图疯传的"agent 密谋"内容是人类 prompt 出来再截图博流量的（00:44–00:47）。
- Lex 与他都认为真正暴露的问题是 **AI psychosis**：公众（尤其非年轻世代）对 AI 缺乏"强大但不总是对"的基本认知，需要社会层面补课（00:47–00:50）。
- "某种意义上幸好这发生在 2026 而不是 2030——趁 AI 还没强到真正可怕，社会先开始讨论"（00:50–00:51）。

### 安全：风险与缓解
- 大量 CVE 报告属于"用户把 web 后端暴露公网"类；他认为风险画像与"Claude Code --dangerously-skip-permissions / Codex YOLO 模式"相当，而后者是所有 agentic 工程师的日常（00:52–01:00）。
- Prompt injection 仍是行业未解问题，但最新一代模型经过大量 post-training 已不易被"ignore all previous instructions"级别的攻击拿下；**越弱/越便宜的模型越容易被注入**——所以安全文档里警告别用便宜模型或弱本地模型（00:55–00:57）。
- 三维权衡：模型越智能攻击面越小，但能造成的损害越大（00:57）。
- 缓解措施：skills 目录与 VirusTotal（Google 旗下）合作做 AI 扫描、sandbox、allowlist、私有网络部署建议；一位安全研究员"骂完附上 PR"，直接被他雇了（00:53–00:56）。当前阶段的核心焦点就是安全，"等我能推荐给我妈用了再简化安装"（01:59–02:00）。

### Agentic engineering 方法论
- "**Vibe coding 是个蔑称**。我做 agentic engineering——凌晨三点后才切换成 vibe coding，第二天带着悔恨收拾烂摊子"（01:04–01:05）。
- **Agentic 曲线/陷阱**：新手短 prompt → 中期过度复杂（8 个 agent 编排、18 个 slash 命令、multi-checkout）→ 精通后回归短 prompt（"看这些文件，做这些修改"）。自动化整个流程（orchestrator）= 回到 70 年代瀑布模型，会丢掉 style、love 与 human touch（01:03–01:05、01:19–01:21）。
- **对 agent 的共情**是核心技能：agent 每次从零开始探索你的代码库，"你自己进一个陌生代码库试试"；世界级程序员骂 LLM 不好用，恰恰因为太强的编程能力妨碍了他们共情一个从零开始的系统（01:05–01:07、01:17–01:18）。
- 代码库应该为 agent 优化而非为自己优化：别跟 agent 起的名字较劲（那是权重里最自然的名字，下次搜索它会找这个名字）（01:12–01:13）。
- 工作流：并行 4–10 个 agent、语音输入为主（"这双手现在太金贵了"，一度说话说到失声）、从不 revert 永远 commit main（"refactor 现在很便宜"）、local CI（DHH 式）、每个 feature 合并后问"现在有什么可以 refactor 的"；PR 审核第一问永远是"你理解这个 PR 的意图吗"而不看实现（01:13–01:16、01:37）。
- 模型手感需要约一周适应期；"模型变笨了"多半是你的项目在长 slop、越来越难让 agent 工作（01:45–01:47）。

### Opus vs Codex（模型对比）
- "Opus 有点太美国了，Codex 是德国人"：Opus = 好玩但偶尔犯傻的同事，角色扮演/人格塑造极强、动手快、偏 trial-and-error；Codex = 角落里不想搭理但可靠干活的怪人，默认读更多代码、可连续跑 6 小时不动摇（01:39–01:44）。
- 差异主要在 post-training 的目标设定，不是原始智能；"熟练的驾驶者用任何最新一代模型都能拿到好结果"（01:41–01:42）。
- 模型会"context 焦虑"：接近窗口上限时 raw thinking stream 会泄漏出类似 Borg 的碎片（"Run to shell, must comply, but time"）（01:07–01:08）。

### MCP 已死，CLI + skills 万岁
- "每个 MCP 做成 CLI 都会更好"：模型天生擅长调 Unix 命令；MCP 需要训练适配、语法特殊、**不可组合**——返回大 blob 必须整个塞进 context，而 CLI 输出可以接 `jq` 过滤、组合成脚本，零 context 污染（02:38–02:42）。
- skills 的美在于"一句话描述 → 按需加载"，与 CLI 天然互补；OpenClaw 核心层甚至没有 MCP 支持，没人抱怨。例外：需要状态的场景（如 Playwright 浏览器控制）（02:39–02:42）。

### 个人 agent = 操作系统；80% 的 app 将消失
- 个人 agent 与 coding agent 会融合，"这是 puck 要去的方向——它会越来越成为你的操作系统"；当前 chat 界面只是"电视上播放广播节目"的过渡形态（01:48–01:51）。
- **每个 app 现在都是一个很慢的 API，不管它愿不愿意**：agent 可以走浏览器（Playwright + 住宅 IP）绕过封锁，"你没有让不可能的事发生，只是让它变慢了"。为什么还需要 MyFitnessPal / Sonos app / 日历 app？预计杀死 80% 的 app；app 要么变成 agent-facing API 要么消亡（02:43–02:57）。
- 新生意机会：给 agent 发"零花钱"预算解决问题、rent-a-human 类服务、agent marketplace（与[戴雨森](../people/dai-yusen.md)的 agent 网络效应判断呼应）（02:54–02:56）。
- 互联网正在对 agent 关闭（Cloudflare 反爬、Google 无 CLI、Twitter 封 API）；他反对一切 AI 自动发推（"AI 有味道，闻到就拉黑"），主张 agent 代理行为必须明确标注（02:44–02:47、02:46–02:47）。

### 程序员之死与 builder 身份
- "编程会变成织毛衣（knitting）——因为喜欢而做，不是因为有意义"；直接回应"mourn our craft"一文：怀念手写代码的心流是正当的，但这不可阻挡（03:01–03:03）。
- 软件工程师的天价薪资源于"智能稀缺"，token 化智能会让它回落；但"你不只是程序员，你是 builder"——他在 iOS 会议上到处劝人放弃"iOS 工程师"身份认同（03:03–03:05）。
- 程序员其实是此刻最有优势的人群：最能学会"agent 的语言"、共情 agent 的处境（03:05–03:07）。
- 对"水资源/环保"批评的回应：每月少吃一个汉堡即可抵消个人 token 的碳/水足迹，高尔夫用水超过所有数据中心总和；但 Lex 补充：硅谷泡泡对变革期真实痛苦（失业、身份丧失）缺少"安静的敬意"（03:08–03:11）。

### 商业化与去向
- 项目**倒贴钱**（每月 1–2 万美元，赞助全部转给依赖库作者）；开源可持续性堪忧——连"人人都用"的 Tailwind 都裁掉 75% 员工，因为 agent 时代没人访问官网了（02:20–02:22）。
- 拒绝创业路线（"been there, done that"，且商业版会与开源版产生利益冲突）；在 Meta 与 OpenAI 之间抉择，条件是项目保持开源（Chrome/Chromium 模式）。Zuckerberg 亲自整周试用产品提反馈、"给我 10 分钟，我在写代码"；OpenAI 用 Cerebras 级推理速度（"Thor's hammer"）和 token 诱惑（02:18–02:34）。
- Anthropic 因订阅条款封了他朋友的账号，"你刚失去一个 200 美元的客户，还让他恨上你的公司——现在锁死产品太短视"（02:25–02:28）。

## 事实性细节

- 2026-01 单月 6600+ commits，一人主导；GitHub 涨星最快仓库（访谈时 175k–180k stars）（00:20–00:21、00:05–00:06）。
- 改名史：WA-Relay → Clawdus（TARDIS 里的太空龙虾）→ ClawdBot（Anthropic 友好但坚决地要求改名）→ MoltBot（改名瞬间被 crypto 狙击手在 5 秒内抢注 Twitter/GitHub/NPM，旧账号被用来发 token 和恶意软件）→ OpenClaw（打电话问过 Sam Altman；花 1 万美元买 Twitter 商业账号认证）（00:26–00:43）。
- Crypto 骚扰被他称为"经历过的最恶劣的网络骚扰"（00:31–00:33）。

## 相关主题

- [LLM 操作系统](../topics/llm-os.md)（个人 agent 即 OS、soul.md/memory、proactive heartbeat）
- [实践中使用 LLM](../topics/using-llms-in-practice.md)（agentic engineering、MCP vs CLI/skills、模型对比）
- [LLM 安全](../topics/llm-security.md)（prompt injection、弱模型更易被注入、skills 供应链扫描）
- [AI 与就业](../topics/ai-and-jobs.md)（程序员→builder、编程变织毛衣）
- [AI 商业化与价值捕获](../topics/ai-business-and-value-capture.md)（80% app 消失、app 即 API、开源可持续性）
