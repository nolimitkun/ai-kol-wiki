# LLM 实用方法论

> 各 KOL 关于"如何在日常与专业工作中有效使用 LLM"的观点汇总。

## Andrej Karpathy（美，2025-02）

来源：[How I use LLMs](../videos/20250227-karpathy-how-i-use-llms.md)

- **心智模型先行**：把模型当作"半年前通读互联网、只记得大概的 1TB 有损 zip 文件"，据此判断哪些问题可以直接问（高频、非近期、低风险），哪些必须配工具或核对来源。
- **管理 context window**：换话题开新对话；context 是工作记忆，无关 token 降低准确率、拖慢速度。
- **LLM Council**：重要问题问遍多家模型交叉参考。
- **按任务选模型**：难题用 RL 思考模型换准确率，日常问题用快模型；留意价位档对应的模型规模。
- **一切输出当第一稿**：Deep Research 报告查引用、数据分析读代码、医疗信息核对原件——"初级分析师有点心不在焉"。
- **不独自读书**：文献/古书装进 context window 共读。
- **语音优先**：他超半数查询用语音输入（"别打字了，用语音，快得多"）。
- **few-shot 优于纯描述**：自定义提示词给具体示例，"教模型和教人一样，光讲不如给例子"。
- **专业编程用 IDE agent**（Cursor 等）而非网页复制粘贴；"vibe coding"（他自认造的词）= 口述需求交给 agent，失败再退回手工。

## 姚顺宇（中，Google DeepMind，2026-05）：一线研究员的 coding 工作流

来源：[张小珺访谈](../videos/20260511-zhang-xiaojun-yao-shunyu.md)

- **模型写 90% 的代码**（"不保守就是 99%–100%"）：人最重要的工作变成设计逻辑、给合理 context（如指一个 reference 文件）、审查代码是否真的合理（00:38–00:40）。
- **实验/实现 idea 的效率比一年半前提升 20–50 倍**：可同时开好几个 idea 并行试，模型还能帮监控实验；但工作时间反而更长、密度更高——"越试越想试"（00:40–00:42）。
- 遇到看不懂的文件不再去约人、等几小时，"问一下 Gemini，5 秒告诉你结果就接着干"（00:41）。
- 判断人是否"靠谱"的面试题：**24 小时从 0 到 1 做一个 RL 项目 + 1 小时讨论**——考察能否有效利用 AI，以及是否真理解 AI 做了什么（全盘扔给 AI 会在讨论中露馅）（03:31–03:33）。

## Peter Steinberger（美/奥，OpenClaw 作者，2026-02）：agentic engineering 方法论

来源：[OpenClaw 访谈](../videos/20260212-lex-openclaw-steinberger.md)

- **"Vibe coding 是蔑称"**，他做 agentic engineering；**agentic 曲线/陷阱**：新手短 prompt → 中期过度复杂化（8 agent 编排、18 个 slash 命令）→ 精通后回归短 prompt。全自动 orchestrator = 回到 70 年代瀑布模型，丢掉 style 与 human touch（01:04–01:05、01:19–01:21）。
- **对 agent 的共情是核心技能**：agent 每个 session 从零开始探索你的代码库，要指路、要"take your time"；世界级程序员骂 LLM，恰因编程太强妨碍其共情一个冷启动的系统（01:05–01:07、01:17–01:18）。**代码库应为 agent 优化**：别跟 agent 起的名字较劲——那是权重里最自然的名字，下次搜索它找的就是它（01:12–01:13）。
- 工作流细节：并行 4–10 agent；**语音输入为主**（与 Karpathy "别打字了"一致，他一度说话说到失声）；从不 revert、永远 commit main（"refactor 现在很便宜"）；每个 feature 合并后问"现在有什么可以 refactor 的"、"如果重来你会怎么做"；PR 审核第一问是"你理解这个 PR 的意图吗"而非看实现（01:13–01:16、01:35–01:37）。
- **模型手感论**：Opus 角色扮演强、动手快偏 trial-and-error（"有点太美国"），Codex 默认读更多代码、可跑 6 小时（"是德国人"）；差异在 post-training 目标而非原始智能，换模型给自己一周适应期；"模型变笨了"多半是你的项目在长 slop（01:39–01:47）。
- **MCP vs CLI/skills**：CLI 可组合（接 `jq` 过滤、写成脚本）、零 context 污染；MCP 返回大 blob 必须整个进 context、需训练适配。skills = "一句话描述 → 按需加载"，与 CLI 天然互补；例外是需要状态的 Playwright（02:38–02:42）。

## Noam Brown（美，OpenAI，2026-06）：日常已可信任

来源：[No Priors 访谈](../videos/20260626-no-priors-noam-brown.md)

- 已日常用模型做税务建议、买房 paperwork——"某种程度上比信任人类专家还多"；提醒 2022–23 觉得不可信而弃用的人重新评估（00:30–00:31）。

## Agent 时代的用法演进：治理 agent、AX、agent 管理学习曲线（2026-05–07）

- **Andrew Feldman（Cerebras）："从 10x 到 100x 但非人人适用"**：少数有"完美心智"的人把编码转成**治理 agent**——同时跑 8–10 个 agent、专设 QA agent、主动补足模型冗长/删注释的弱点；token 花费从 <$1K/人月 到 $25–30K（[Cerebras](../videos/20260521-no-priors-cerebras-feldman.md) 00:12–00:13）。为 Steinberger"agentic engineering"补上"多 agent 治理"的具体工作方式。
- **Akshat Bubna（Modal）：AX≈DX**：给 agent 用的和给人用的体验高度一致（余弦相似度 ~0.9）；建 modal bench 找 agent 做不到的事，agent 反复幻觉某功能就把它做成真 CLI / 加 skill——**"agent 幻觉自己的功能"其实是产品反馈**（[Modal](../videos/20260708-latent-space-modal-agent-infra.md) 00:06–00:07、00:57–00:58）。与 Steinberger"每个 MCP 做成 CLI 都更好"同频。
- **Gavriel Cohen（NanoClaw）：agent 管理有陡峭学习曲线**：最大误区是"扔个任务就走开等成品"，必须持续调 instruction/skill/context；个人 agent 的记忆用 **LLM Wiki 优于检索**（问"这周最该关注什么"没有语义搜索能答），痛点是造重复文件、需背景进程查重（**与本库 Lint 同构**）（[NanoClaw](../videos/20260629-latent-space-nanoclaw.md) 00:03–00:13）。

## 语音口述、loop maxing、prompt 自检、human-in-the-loop 当媒介（2026-07）

- **脚踏板 + Whisper Flow 把 LLM 从"打字"解放成"意识流口述"**（Mati / ElevenLabs）：按住踏板给一两分钟 stream of consciousness，"LLM 特别擅长把一大段意识流理成东西"；语音 agent 让人反而更愿打断、对 AI 更坦诚（[语音与法律](../videos/20260714-all-in-11labs-legora-voice-law.md) 00:11–00:15）。为本页"语音优先"补上具体硬件工作流。
- **Andrew Feldman 的 prompt 收尾模板**：结尾固定加"**检查你的工作 + 告诉我我没考虑到什么 + 每次运行都反问我几个问题**"——这改变了 trend scouting 等任务的产出；配合"token maxing / loop maxing"（递归：问→学→再问，答案好很多）（[Cerebras 与 BFL](../videos/20260710-all-in-cerebras-bfl-open-source.md) 00:27–00:32）。与 Karpathy"把输出当第一稿/查证"、NanoClaw"持续调 instruction"同一实践谱系。
- **生成式模型当"媒介"而非"自动出片"**（Robin Rombach / BFL）：与 Scorsese 合作的用法是**human-in-the-loop 把脑中画面迭代成图像**（"语言是有损媒介、视觉更丰富"）、平行化 brainstorming/storyboard，而非一键生成整部电影（00:46–00:50）。呼应"人向设计/判断迁移"。
- **写好 verifier 是关键技能**（志鹏 / vLLM-Omni）：code with AI 后，"实体 code 会被取代、重心转向写测试/verifier"；学习时"找一个不懂的人（或 agent）用费曼学习法讲懂"（[志鹏访谈](../videos/20260517-uncle-moon-zhipeng-vllm-contributor.md) 15:15–24:23）。与 Modal"agent 幻觉即产品反馈"、NanoClaw"agent 管理有学习曲线"同属"人机协作方法论"。

## 中美对照

Karpathy 与姚顺宇都强调"把输出当第一稿/审查代码合理性"，但侧重不同：Karpathy 面向广义用户（心智模型、选模型、语音优先），姚面向前沿研究工作流（模型写 90% 代码、20–50× 实验加速、与 AI 协作能力作为招人标准）。两者共同印证 [AI 与就业](ai-and-jobs.md) 里"人向设计、判断、监督迁移"的趋势。
