# AI KOL Wiki — 目录

> 由 LLM 根据 `sources/` 中的视频转录稿增量维护。规范见 [CLAUDE.md](../CLAUDE.md)。

## 人物

- [Andrej Karpathy](people/andrej-karpathy.md) — OpenAI 创始成员，LLM OS / LLM 心理学框架提出者
- [Jensen Huang](people/jensen-huang.md) — NVIDIA CEO，四条 scaling laws、token 工厂世界观
- [Dwarkesh Patel](people/dwarkesh-patel.md) — 深度访谈播客主持人
- [Lex Fridman](people/lex-fridman.md) — 超长访谈播客主持人
- [Adam Brown](people/adam-brown.md) — Google DeepMind BlueShift 负责人，理论物理学家
- [Grant Sanderson](people/grant-sanderson.md) — 3Blue1Brown，AI 与数学观察者
- [Ada Palmer](people/ada-palmer.md) — 文艺复兴史学家（非 AI 领域）
- [姚顺宇](people/yao-shunyu.md) — Google DeepMind 研究员（前 Anthropic），中方一线视角
- [Noam Brown](people/noam-brown.md) — OpenAI，推理 / test-time compute 奠基人之一
- [Mark Chen](people/mark-chen.md) — OpenAI 首席研究官
- [张小珺](people/zhang-xiaojun.md) — 《商业访谈录》主播（中方视角主来源）
- [No Priors 主播](people/no-priors-hosts.md) — Sarah Guo & Elad Gil
- [Latent Space 主播](people/latent-space-hosts.md) — swyx & Alessio
- [Eric Jang](people/eric-jang.md) — 前 1X / DeepMind Robotics，self-play 与 RL
- [Alex Imas & Phil Trammell](people/imas-trammell.md) — AGI 经济学（DeepMind / Epoch）
- [Zico Kolter & Matt Fredrikson](people/gray-swan-founders.md) — Gray Swan，AI 安全 / 红队
- [Sebastian Raschka & Nathan Lambert](people/raschka-lambert.md) — ML 教育者，AI2 OLMo / RLHF
- [a16z](people/a16z.md) — Andreessen Horowitz 频道：Benedict Evans、Sinofsky、Amble 等
- [何小鹏](people/he-xiaopeng.md) — 小鹏集团 CEO，物理 AI / 人形机器人（中方产业操盘手视角）
- [阳萌](people/yangmeng-steven.md) — 安克创新创始人兼CEO，消费电子/端侧AI/存算一体芯片（中方产业操盘手视角）
- [Lewis Hong（洪力德）](people/lewis-hong.md) — 前SpaceX首席制造工程师，Aris Fund GP，太空/硬科技投资
- [Freda（段）](people/freda-duan.md) — Altimeter Capital 合伙人，硅谷投资，Token经济学/组织变革/软件冲击
- [戴雨森（雨森）](people/dai-yusen.md) — 真格基金管理合伙人，Harness/Agent/组织变革/创业投资
- [月球大叔](people/uncle-moon.md) — AI 技术向访谈主播（中方 infra 视角主来源之一）
- [朱邦华（Banghua Zhu）](people/banghua-zhu.md) — SGLang 母公司 CTO，前 NexusFlow，RLHF/RLVR/RL infra
- [江鋆晨（Junchen Jiang）](people/junchen-jiang.md) — 芝大教授 / TensorMesh CEO，KV Cache / LMCache
- [广密](people/guangmi.md) — 硅谷 AI 投资人/研究者，"全球大模型季报"主讲（中方投资视角看硅谷全景）
- [罗福莉（Luo Fuli）](people/luo-fuli.md) — 小米大模型团队负责人（MemoVR），前 DeepSeek，Agent 范式/架构/组织平权

## 主题

- [LLM 训练管线](topics/llm-training-pipeline.md) — 预训练 / SFT / RL、scaling laws（含 Jensen 的四阶段扩展）
- [LLM 心理学与认知短板](topics/llm-psychology.md) — 幻觉、工作记忆、token 思考、瑞士奶酪能力
- [LLM 实用方法论](topics/using-llms-in-practice.md) — 如何有效使用 LLM（Karpathy、Grant/Dwarkesh 的学习法）
- [评估与 Benchmark](topics/evaluation-and-benchmarks.md) — test-time compute、bench maxing、纸面趋同（Noam、Mark、姚顺宇）
- [AI 实验室文化与组织](topics/ai-lab-culture.md) — top-down vs bottom-up、make bets、集体主义（姚顺宇、Mark）
- [LLM OS 与新计算范式](topics/llm-os.md) — LLM 作为操作系统内核的世界观
- [LLM 安全](topics/llm-security.md) — 越狱、提示注入、数据投毒、安全评估的 test-time compute 缺口
- [AI 与科学发现](topics/ai-for-science.md) — AI 做数学/物理的现状与门槛（Brown、Sanderson、Karpathy、Noam、姚顺宇）
- [AI 算力与基础设施](topics/ai-infrastructure.md) — extreme co-design、电力、供应链、token 工厂、TPU vs GPU
- [AI 与就业](topics/ai-and-jobs.md) — 放射科医生案例、策展人转型、编码民主化、centralized technology
- [AI 商业化与价值捕获](topics/ai-business-and-value-capture.md) — 模型商品化、价值向上游转移、capex 上限、"电力还是社交媒体"
- [物理 AI 与机器人](topics/physical-ai-and-robotics.md) — 具身智能、自动驾驶、人形机器人：物理 AI vs 数字 AI、中美路线（中方素材强）
- [中美 AI 生态对照](topics/china-us-ai.md) — 本库核心主题：模型差距、蒸馏、字节/豆包、C 端 vs enterprise

## 视频

### Andrej Karpathy
- 2023-11-23 [Intro to Large Language Models](videos/20231123-karpathy-intro-to-llms.md)
- 2024-02-20 [Let's build the GPT Tokenizer](videos/20240220-karpathy-gpt-tokenizer.md)
- 2024-06-09 [Let's reproduce GPT-2 (124M)](videos/20240609-karpathy-lets-reproduce-gpt2.md)
- 2025-02-05 [Deep Dive into LLMs like ChatGPT](videos/20250205-karpathy-deep-dive-into-llms.md)
- 2025-02-27 [How I use LLMs](videos/20250227-karpathy-how-i-use-llms.md)

### Dwarkesh Podcast
- 2026-05-15 [Eric Jang：从零重建 AlphaGo，谈 self-play、RL 与 LLM 的未来](videos/20260515-dwarkesh-eric-jang.md)
- 2026-06-04 [Alex Imas & Phil Trammell：AI 越强，它占经济的份额可能越小](videos/20260604-dwarkesh-imas-trammell.md)
- 2026-06-16 [Ada Palmer：Machiavelli 被误读](videos/20260616-dwarkesh-ada-palmer-machiavelli.md)（思想史）
- 2026-06-30 [Grant Sanderson：AI 反证数学猜想之后](videos/20260630-dwarkesh-grant-sanderson-ai-math.md)
- 2026-07-10 [Adam Brown：第一性原理讲广义相对论](videos/20260710-dwarkesh-adam-brown-general-relativity.md)

### Lex Fridman Podcast
- 2026-01-31 [#490 State of AI 2026：LLM、编码、Scaling、中国、Agent、GPU、AGI](videos/20260131-lex-state-of-ai-2026.md)（Raschka & Lambert）
- 2026-03-23 [#494 Jensen Huang：NVIDIA 与 AI 革命](videos/20260323-lex-jensen-huang-nvidia.md)
- 2026-04-09 [#495 维京时代](videos/20260409-lex-brownworth-vikings.md)（历史）
- 2026-05-06 [#496 FFmpeg 与开源](videos/20260506-lex-ffmpeg.md)
- 2026-05-29 [#497 Don Lincoln：物理学之谜](videos/20260529-lex-don-lincoln-physics.md)（物理）
- 2026-06-30 [#498 罗马帝国与拜占庭](videos/20260630-lex-kaldellis-roman-empire.md)（历史）

### 张小珺·商业访谈录
- 2026-05-11 [姚顺宇：在 Anthropic 和 Gemini 训模型、英雄主义已过去](videos/20260511-zhang-xiaojun-yao-shunyu.md)
- 2026-05-28 [何小鹏：机器人 IRON、"剪腿"风波、物理 AI 与在血海里游泳](videos/20260528-zhang-xiaojun-he-xiaopeng-robot.md)
- 2026-05-18 [Freda 投资札记第 2 集：Tokenmaxxing、AI 组织变革、焦虑与连接](videos/20260518-zhang-xiaojun-freda-investment-2.md)
- 2026-05-27 [雨森创投观察第 2 集：Harness、下一个字节、2026大机会](videos/20260527-zhang-xiaojun-yusen-vc-2.md)
- 2026-06-08 [阳萌（安克创新）：消费电子死与生、第三类公司、端侧模型、产品方法](videos/20260608-zhang-xiaojun-yangmeng-anker.md)
- 2026-06-13 [Lewis Hong（前SpaceX）：口述SpaceX开发史、太空与AI、人类文明扩张前奏](videos/20260613-zhang-xiaojun-spacex-lewis.md)
- 2026-04-15 [广密·全球大模型季报第 9 集：Coding 是 AGI 第二幕、御三家真相、模型即 OS](videos/20260415-zhang-xiaojun-guangmi-llm-quarterly-9.md)
- 2026-04-24 [罗福莉：OpenClaw 是划时代 agent 框架、Agent 很吃后训练、卡的分配与组织平权](videos/20260424-zhang-xiaojun-luo-fuli-agent-paradigm.md)

### 月球大叔
- 2026-05-18 [朱邦华：SGLang、RLHF vs RLVR、被英伟达收购后二次创业](videos/20260518-uncle-moon-banghua-zhu-sglang.md)
- 2026-06-09 [江鋆晨：KV Cache 是大模型的记忆、是"未来的石油"](videos/20260609-uncle-moon-junchen-jiang-kvcache.md)

### No Priors
- 2026-06-26 [Noam Brown：超大规模 test-time compute 如何改变评估与安全](videos/20260626-no-priors-noam-brown.md)

### Latent Space
- 2026-06-22 [Gray Swan：Codex/Claude Code 之后的 AI 安全](videos/20260622-latent-space-gray-swan.md)（Kolter & Fredrikson）
- 2026-06-25 [Mark Chen：AGI、o1、评估与 Scaling Laws](videos/20260625-latent-space-mark-chen.md)
- 2026-07-13 [Dan Biderman：AI 的记忆问题——为什么长上下文还不够](videos/20260713-latent-space-dan-biderman.md)

### a16z
- 2026-06-08 [Benedict Evans：AI 使用的经济学与 SaaS 的下一步](videos/20260608-a16z-benedict-evans-ai-economics.md)
- 2026-07-07 [Software in the Age of Agents：headless 软件与例外处理](videos/20260707-a16z-software-in-age-of-agents.md)（Amble & Sinofsky）
