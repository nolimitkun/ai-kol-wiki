# LLM OS 与新计算范式

> LLM 不是聊天机器人，而是新兴操作系统的内核进程。

## 各家观点

### Andrej Karpathy（美，2023-11）
提出 LLM OS 框架：LLM 作为 kernel process 协调内存与计算工具——context window ≈ RAM（有限的宝贵工作记忆），互联网/本地文件 ≈ 磁盘（经浏览/RAG 访问），计算器/Python ≈ 外设；未来还有多线程、投机执行、用户态/内核态的类比。生态上闭源（GPT/Claude/Gemini）vs 开源（Llama 系）对应 Windows/macOS vs Linux。（[Intro to LLMs](../videos/20231123-karpathy-intro-to-llms.md) 00:42–00:45）

### Dan Biderman（美，Engram CEO，2026-07）：RAM 不够——记忆、context rot 与"训进权重"
来源：[Latent Space 访谈](../videos/20260713-latent-space-dan-biderman.md)

接续 Karpathy"context window ≈ RAM"的框架，给出 2026 年的工程续集——**光把 RAM 做大（长上下文）不够**：
- **"记忆 / 持续学习本质是长上下文问题的伪装"**；即便 10M 上下文，仍有 (1) **context rot**（喂进越多 token 越困惑）与 (2) 内存/成本爆炸两大限制。**compaction（模型自管理上下文）在改进但按定义有损**、当前偏非黑即白，长会话深处会健忘（00:18–00:21）。
- **KV cache 的内存怪兽**：Llama 70B 读一篇几十 KB 文章，"脑状态"就占约 80GB HBM，与整个模型参数（约 140GB）同量级——RAM 极度低效（00:22–00:23）。
- Engram 的下注是把语料用梯度下降**训进权重**（"cartridges"，约 1000× 压缩），与文本表示（RAG/wiki，即 Karpathy 的"磁盘"）互补；长期"每人一份权重、跑在个人设备上"（00:09–00:11、00:26–00:28）。这把 LLM OS 的"内存管理"从"如何调度 RAM/磁盘"推进到"哪些知识该内化进内核本身"。

### Peter Steinberger（美/奥，OpenClaw 作者，2026-02）：个人 agent 就是下一个 OS

来源：[OpenClaw 访谈](../videos/20260212-lex-openclaw-steinberger.md)

- **"这是 puck 要去的方向——个人 agent 会越来越成为你的操作系统"**：coding agent 与生活 agent 终将融合；当前 chat 界面只是过渡形态，"就像电视刚发明时人们在电视上播广播节目"（01:48–01:51）。
- 从实践侧填充 LLM OS 的多个抽象层：**记忆**用 Markdown 文件 + 向量库（自评"level 2–3"，终极 boss 是 continuous RL）；**外设/驱动**用 CLI + skills 而非 MCP（CLI 可组合、可 `jq` 过滤、零 context 污染——"每个 MCP 做成 CLI 都会更好"）；**进程调度**有 heartbeat（定时"surprise me" prompt 让 agent 主动行动，被嘲"不就是 cron 吗"，"Dropbox 不就是 FTP 吗"）（00:19–00:20、02:38–02:42、02:36–02:38）。
- **自修改软件已是现实**：agent 完全"自知"（源码、harness、文档、所跑模型），用户 prompt 即可让 agent 修改自身软件（00:22–00:24）。
- 与 [Karpathy 的 LLM OS 框架](../videos/20231123-karpathy-intro-to-llms.md) 对照：Karpathy 从内核抽象出发，Steinberger 从产品/社区侧把同一形态"prompt 进存在"；与[罗福莉](../people/luo-fuli.md)"智能体框架 = 人与模型的中间层"是同一物的作者视角与研究者视角。

## 中方视角：模型即操作系统

### 广密（硅谷投资视角，2026-04）

来源：[广密·全球大模型季报第 9 集](../videos/20260415-zhang-xiaojun-guangmi-llm-quarterly-9.md)

- **模型 = 新一代操作系统 = global GDP 的 OS**：最领先的三五家模型将成为世界最重要的技术基础设施（生活问它、工作自动化靠它、科研支持也是它），重要性超过今天的 Google；每家估值 10 万亿美金（01:04:51–01:06:53、01:13:05）。
- **OS 的定义"支持应用的无限扩展"**——这里的"应用"就是 agent，会形成像 Android/Windows 一样的新生态（01:05:52）。这是对 Karpathy"LLM 是新 OS 内核"从商业/投资侧的放大：不只内核，而是承载全球 GDP 的操作系统。

### 罗福莉（中方 research lead，2026-04）：Agent 框架是"人与模型之间的中间层"

来源：[罗福莉访谈](../videos/20260424-zhang-xiaojun-luo-fuli-agent-paradigm.md)

- **智能体框架（如 OpenClaw）= 人与模型之间的"中间层"**：同时定义"人如何交互"和"如何与模型沟通"两层，可做得很厚重，而前端 UI 是"最薄且不关键的一层"（00:20:16–00:21:16）。这为 LLM OS 补上"内核之上的调度/编排层"的中方一手描述。
- **框架能弥补模型短板**：一套足够好的 agent 框架 + 中层模型，就能在 85% 场景达到顶尖模型水平（3B 端侧模型接入也能干"小模型不该能干"的事）（00:15:13–00:16:13）——OS 的"驱动/兼容层"让弱硬件也可用，是同一隐喻。
- **模型与框架必须协同进化**（自学习）；开源框架 + 群体智能让这一层迭代极快。呼应 Dan Biderman"哪些知识该内化进内核"的问题：罗关注的是"哪些能力该由框架补、哪些该训进模型"。

### Gavriel Cohen（NanoClaw 作者，2026-06）：第二大脑与 LLM Wiki 优于检索
来源：[NanoClaw 访谈](../videos/20260629-latent-space-nanoclaw.md)
- 继 OpenClaw 之后又一个"个人 agent 即 OS"的一线实践；主张**"claw 类 agent 的杀手级用例是第二大脑"**——不断喂信息、让 agent 建 LLM Wiki/知识图谱，而非要现成产出（00:05–00:06）。
- **LLM Wiki 优于检索/RAG**（对 Karpathy"磁盘 ≈ RAG"框架的一个反转）：问"这周最该关注什么"没有 embedding/关键词能答，但有好的 LLM Wiki（项目/时间线/本周通话 log）就能跨文件收集给出——所以他个人直接把 agent 指向 Karpathy 的 LLM Wiki 帖照做；已知痛点是会造重复文件、需背景进程查重（**与本库 Lint 巡检同构**）（00:11–00:13）。**本条本身是本库范式的元证据**：新加坡外长用 NanoClaw + Karpathy LLM Wiki + Nemon 记忆系统搭第二大脑。

### Akshat Bubna（Modal CTO，2026-07）："LLM 内核"之辩与 agent 自造基础设施
来源：[Modal 访谈](../videos/20260708-latent-space-modal-agent-infra.md)
- swyx 抛出非共识："也许 AIOS/LLM OS 的内核真就是个 LLM（软权限就够）"；Akshat 明确保留——sandbox 层要**硬边界**（详见 [LLM 安全](llm-security.md)）（00:43–00:44）。这是对 Karpathy"LLM 是内核进程"的一个边界追问：内核可以是 LLM，但**权限/隔离不能只靠 LLM**。
- **agent 自供给基础设施**：self-provisioning runtime 让 agent 能 spin up 别的 agent、起自己的基础设施；SDK 从"开发者体验"转向"agent 体验"——OS 的"系统调用"正在为 agent 而非人重新设计（00:04–00:07、00:37）。

### ⚠️ Akshay Nathan（OpenAI，2026-07）：LLM OS 被逐项做成了产品，但他不用这个词
来源：[OpenAI 把 ChatGPT 做成"万物应用"](../videos/20260728-latent-space-akshay-nathan-chatgpt-work.md)

这是本页迄今**与 Karpathy 清单对应最整齐的一份产品实证**，且它来自 OpenAI 产品侧而非研究侧：

- **持久计算机环境 + 文件系统**：ChatGPT Work 在 web 和 mobile 上给你一个持久环境，**文件跨会话保留**；加上**定时任务**与**跨时间引用**（[00:46:28]–[00:47:28]）。
- **可扩展的工具层**：**plugins 在 ChatGPT、ChatGPT Work 与云端是统一原语**（[00:14:07]）；目标是"**你来到这个产品、开一个会话就能做任何事，不用点按钮跳去别处**"（[00:47:28]–[00:48:28]）。
- **记忆作为系统状态**：ChatGPT Work / 云端**默认继承 ChatGPT 记忆并可写回**，同属 memory V3；**Chronicle**（从你如何使用计算机中学习）是一个新的记忆输入源，目前实验性、默认关闭（[00:56:33]、[00:59:36]–[01:00:37]）。
- **模型做调度**：进 chat 模式还是 work 模式**由模型决定**（[00:15:09]）——对应 Karpathy"LLM 是内核进程"里最核心的那条，但落在**模式选择**而非资源调度。
- ⚠️ **但他自己的参照系不是操作系统，是 [OpenClaw](../people/peter-steinberger.md)**：他讲了自己的 OpenClaw 时刻，承认灵感来源，并指出"**原语是一样的**"（定时任务、文件系统、跨时间引用）。**同时他明确不认为 ChatGPT Work 会取代 OpenClaw**——"那个团队做出来的这种了不起的开源技术永远有其需求"（[00:47:28]）。是 swyx 在本期说出了"**个人 OS**"这个词。
- **harness 层的一条演化观察**（对本页有直接含义）：Codex 的 harness 实际上取代了 ChatGPT 的 harness，理由是"**给 agent 一个无限灵活的环境——一台计算机——它能做到非常强大的事**"（[00:16:10]）。**"计算机环境"作为 agent 的通用抽象胜过"对话"作为通用抽象**，这正是 LLM OS 命题的一次经验性支持。
- ⚠️ **一处 swyx 追问后未被正面回答的技术缺口**：只靠 MCP / CLI / API 即时拉数据是否够，还是需要**数据仓库/缓存/语义层**？Akshay 的回答是"取决于访问模式"、且多数用例本来就不需要即时返回，**没有确认也没有否认内部是否存在这一层**（[00:50:29]–[00:51:29]）。本库不做推断。
- **权限层问题**（新角度，另见 [LLM 安全](llm-security.md)）：多人共享 artifact 时，**人本身充当了权限层**；一旦被 agent 取代就没有天然屏障，且**当事人无从知道自己不知道什么**（[00:25:12]）。

## 开放问题

- 通用 System 2（慢思考换准确率）如何实现——Karpathy 2023 年认为尚无模型具备。
- 语言领域缺少通用 reward function，通用自我改进是否可能（AlphaGo 路径能否迁移）。
