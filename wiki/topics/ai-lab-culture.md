# AI 实验室文化与组织

> 前沿模型公司如何组织：top-down vs bottom-up、如何 make bets、技术 leader 的作用、集体主义 vs 个人英雄主义。这是理解"为什么某家做成某件事"的关键，也是 [中美 AI 生态对照](china-us-ai.md) 的组织维度。

## 三大实验室对照（姚顺宇，前 Anthropic / 现 Google DeepMind，2026-05）

来源：[张小珺访谈](../videos/20260511-zhang-xiaojun-yao-shunyu.md)

- **Anthropic**：执行力极强、**top-down**、reactive 快。能重注 coding（make bets）的独特条件是——技术 1 号位（cofounder Jared Kaplan、Sam McCandlish）**既有技术公信力、又能为公司负责**，CEO 不成阻力，且 cofounding team 互信（"一起趴过战壕"，是 Scaling Law / GPT-3 论文合著者，无一人离开）。"这对其他公司很难，OpenAI 就干不了（Ilya 走后更难）"（01:59–02:06、02:31–02:36）。
- **Google DeepMind**：传统大公司 **bottom-up** 打法（"不赌、方方面面都有储备"）；但**预训练已变得非常 top-down/清晰**，进入 Google 工程管理的舒适区、可预测，后训练仍更 bottom-up。拍板人 Sergey Brin；一线 Koray Kavukcuoglu（DeepMind CTO / Google SVP）；Demis 更管偏 science（Isomorphic Labs）（02:48–02:56、03:12–03:13、02:58–03:00）。
- **OpenAI**：文化上"踏实做事的人没 Gemini 多、更没 Anthropic 多"（姚不去 OpenAI 的主因）；早期分预训练/Strawberry(RL)/post-training 三组，post-training 与产品耦合（02:14、02:49、03:02–03:03）。
- **组织哲学**：最好的状态往往最不稳定，需要一个**技术 leader** 把 bottom-up 创新与秩序融合——组织好坏"归根结底是技术 leader 的问题"。好 leader 两特质：**能亲自下场救火** + **能理解并容纳别人**做自己不做的事（03:18–03:20）。
- **集体主义 vs 个人英雄主义**：LLM 的个人英雄主义时代结束于 Transformer 之后——"每个人都是冲浪的人，本质上是一个浪（AI）而不是那个冲浪的人"；最重要的是集体能否为一个目标一起花精力，而非个人贡献了什么（03:04–03:05、02:29–02:31）。

## OpenAI 研究文化（Mark Chen，OpenAI CRO，2026-06）

来源：[Latent Space 访谈](../videos/20260625-latent-space-mark-chen.md)

- **高风险 bet 是 OpenAI 的 alpha**：有些不会 pan out，但失败的 write-up 也重要（让别人少走弯路）；肯冒险者"偶尔命中一次就值得"（00:34–00:36、00:46–00:48）。
- 既有 top-down steering（研究 manager 多是过往最强研究者，说话有分量），也珍视 bottom-up（研究员拿冷硬证据推翻既有判断）；reasoning/o1 就是靠 Yakub、Ilya 的 conviction 推动全公司（00:11–00:12、00:10–00:11）。
- 高层 roadmap 稳定、implementation 随时间变；每 1–2 月过约 300 项目，聚焦每 org 3–5 个大 bet + directive compute allocation + flexible pools（00:12–00:15）。

## 中方视角：组织平权与"环境比经验更重要"（罗福莉，小米 MemoVR，2026-04）

来源：[罗福莉访谈](../videos/20260424-zhang-xiaojun-luo-fuli-agent-paradigm.md)

- **组织平权到极致**：约 100 人的团队**没有分组、没有层级（"直击"）**（02:00:01）。理由：层级默认"上层的人智能更强，这界定很奇怪"、规范约束压制创造力、leader"不要有很强的掌控感、别觉得没了我就不行"（02:00:01–02:01:01）。这是本库目前最激进的 flat-org 主张，比姚顺宇"英雄主义已过去/集体贡献"更进一步。
- **不分预训练组/后训练组**：数据直觉相通，硬分组"是在扼杀创造力"；做预训练的人天然在乎多样性、转做后训练反而有优势——人在训练阶段间自由流动（01:57:59–02:00:01）。
- **环境比经验更重要**：团队大多没有大模型背景（应届生、做工程的），"这些能力最多一两个月、慢则三四个月都能被快速吸得"；招人看初始上限/好奇心/热爱/多样性，而非"被 supervise 之后的当前状态"，且越来越招大二大三本科生（"没被污染、想象力更高"）（03:01:39–03:27:00）。呼应姚顺宇/朱邦华"本科生摸够卡比 PhD 强"。
- **热爱驱动管理**："让大家围绕自己信仰的事情自驱做事"是最有效方式；靠"体验"驱动热情（那句"第二天对话不超过一百轮就 quit"只是逼大家去用、并不真考核）（02:01:01–02:32:22）。
- **R1 的组织教训**："R1 本质是预训练→后训练时团队如何重组的问题"——把"加大后训练投入=从外面挖个人/新建组"视为错误方式（02:54:36–02:57:39）。这与"OpenAI top-down vs bottom-up"的讨论构成中方补充：范式切换时，组织重构比堆算力/挖人更关键。

## 硅谷三家的组织画像（广密，全球大模型季报，2026-04）

来源：[广密·全球大模型季报第 9 集](../videos/20260415-zhang-xiaojun-guangmi-llm-quarterly-9.md)

- **Anthropic = 战略/专注/文化的胜利**：top-down、all-in coding、放弃 C 端与多模态、"模型即应用/数据即模型"、招 underdog、防泄密最严（00:22:24–00:28:27）。
- **OpenAI = bottom-up、可能出下个范式但不够聚焦**：SAM（VC 出身）容易摊大饼/FOMO、文化 value 0→1 不 value 1→100"没人做脏活"、"ChatGPT 很成功但没有灵魂"（00:41:37–00:44:37）。
- **Google = 体系化的第三代职业经理人**："像一台机器，换一两个人没影响"，但 PM 文化弱、误判 coding（00:49:42–00:50:42）。
- 这为姚顺宇/Mark Chen 的"top-down vs bottom-up"提供了投资侧的第三方交叉印证。

## 交叉观察

- **top-down 能 make bets 但依赖强技术 1 号位**（姚论 Anthropic）与 **OpenAI 珍视 bottom-up 冷硬证据推翻判断**（Mark）并非矛盾：两者都指向"研究品味 + 公信力驱动资源集中"，区别在创业公司（集中赌）与大公司（广布局）的打法差异——姚明确将其归为"startup vs 大公司"之别（02:03–02:04）。
- 姚与 Mark 都认为**个人贡献在当代 LLM 里难以量化、更像集体/系统产物**（姚："都是集体的贡献"；Mark：失败 write-up 也计入集体知识）。

## neo-lab 的工程文化：工厂化研究、agency、约束催生创新（Eiso Kant / Poolside，2026-07）

来源：[Poolside 访谈](../videos/20260722-latent-space-poolside-eiso-kant.md)

本页此前的样本多是大厂/头部实验室（Anthropic/OpenAI/Google）。Poolside 提供了一个**从零起步、不脱胎于任何大厂的 neo-lab** 组织样本，与罗福莉的"组织平权"中方版形成对照：

- **"从零起步"反成资历优势**：没脱胎于已有实验室 → 没有湾区自由流动的信息 → 被迫从头写训练代码、自己解 optimizer bug（三周调 Adam epsilon）——"发现从头搞明白反而建立了更好的直觉，也养出了团队的韧性"。这与"英雄主义已过去"（姚顺宇）相反的一面：**小团队的从零 build 仍能养出独特能力**。
- **Model Factory 是组织设计**：把"最强分布式系统工程师"从 day zero 编进研究流程（而非事后 retrofit），让工程师能低门槛跑实验——"一个原本做 agent 的工程师半年内成了正经 RL 研究员"。**工程平权 → 研究平权**，与罗福莉"环境比经验更重要"同构。
- **招人第一看 agency**：AI 越强，能动性越是最重要品质，且一定在过去经历里被展示过；对齐高 agency 的人靠**共同目标 + 明确边界（lanes）**（"不设边界，每个人就变成探索算法、陷入抢资源的政治"——正是他对大公司研究文化的批评）。
- **约束催生创新**：用相对少的算力/钱、买很少外部数据，反而逼出别人没有的能力。这与阳萌"约束是好事"、Lila"苦甜 scaling"同频。
- **"分阶段是组织现象"**：mid-training 团队的存在制造了 mid-training 这个阶段——组织结构会固化本可连续的技术流程（详见 [LLM 训练管线](llm-training-pipeline.md)）。
- 对读 [Travis Kalanick 的"let builders build"](../videos/20260722-a16z-travis-kalanick-atoms.md)：两人都强调"高 agency 的人 + 共同目标/文化边界"，只是 Travis 从多行业管理容量、Eiso 从单一模型公司聚焦切入。

## 中美对照

见 [中美 AI 生态对照](china-us-ai.md)：姚顺宇认为 Anthropic 的 top-down 与 Google 的 bottom-up 是"startup vs 大公司"两套打法，各自成立。国内侧现由**罗福莉（小米 MemoVR）**补上一手样本——"无组、无层级、热爱驱动、环境比经验重要"的极致 flat-org，与硅谷三家均不同；广密则从投资视角给出 Anthropic(top-down)/OpenAI(bottom-up)/Google(体系化) 的三方画像。中方一线（罗福莉）与硅谷（Mark Chen）都强调**范式切换期的组织重构比堆算力更关键**。
