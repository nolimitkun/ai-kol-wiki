# 志鹏：从 AI 零基础到 vLLM/vLLM-Omni Committer，只用了一年（月球大叔，2026-05-17）

- **嘉宾**: [志鹏（Zhipeng）](../people/zhipeng.md)（[vLLM-Omni 团队](../people/vllm-omni-team.md) committer；原传统软件开发，2025 年 4 月起入门 AI Infra；在新加坡组织 vLLM 自习小组）
- **主持**: [月球大叔](../people/uncle-moon.md)（连麦直播 Q&A，含 Roger/林月谦等在场）
- **来源**: [YouTube](https://www.youtube.com/watch?v=cnFFhnDyIU0) · 32 分钟
- **转录稿**: [sources/uncle-moon/20260517-cnFFhnDyIU0](../../sources/uncle-moon/20260517-cnFFhnDyIU0/transcript.md)（⚠️ 无字幕→RTX 5090 上 faster-whisper large-v3-turbo 本地转录，专有名词有识别误差已归一化）

> 一期"开源 onboarding 现身说法"：一位**零 AI 基础**的传统软件工程师，靠跟看月球大叔的 vLLM 直播，一年内成长为 [vLLM-Omni](../people/vllm-omni-team.md) 的 committer。既是个人成长叙事，也是一份**多模态推理开源社区的贡献者指南**，落点 [中美 AI](../topics/china-us-ai.md)（中方开源社区的人才涌入）与 [AI 与就业](../topics/ai-and-jobs.md)（AI coding 下"编程在编两样东西"）。

## 概要

直播 Q&A 形式。志鹏复盘自己 2025 年 4 月从"连 vLLM 都没听说过"起步，跟看月球大叔直播 → 改文档 → 抢 issue → 做第一个多模态模型支持（字节 Teres，一个多月、约 1000 行 PR，由莫子峰和 Ceres 逐条 review）→ 做了七八个多模态模型 → 参与 Diffusion Worker/Runner/scheduler/Omni Connector 重构后成为 committer。中间穿插大量**新手贡献建议**（小卡起步、租卡、别碰量化、找"铁巴"用费曼学习法、写好 verifier）与**多模态 serving 技术碎片**（diffusion 蒸馏减步、world model、CFG parallel、layerwise/modelwise、单元 vs 端到端测试、内部 fork 的 rebase 之痛）。

## 核心观点

### 一年成长路径
- 起点：传统前后端软件开发、**零 AI/Infra 基础**，2025 年 4 月第一次看月球大叔直播"完全听不懂"，但判断"传统软件要完蛋、这东西很有价值"，一周追完前三期、此后每期跟看（05:00–06:30）。
- 阶梯：**改两次文档**（"一开始什么都不会只能干这些"）→ 抢 issue（研究一周才修出一个 HuggingFace config 问题；debug 过程反而建立了对框架的深度理解）→ 因为热门 issue 被"抢 bug"抢不过（江云等），转做**模型支持**（第一个是字节 Teres，约一个月、约 1000 行 PR，莫子峰 & Ceres 联合 review 七八十条）（06:30–10:00）。
- Begel 模型（要多模态输出）很特殊：先在主仓实现 AR 部分（Ceres 做），透明过渡到 Omni 后做 DiT 部分；参与 Diffusion Worker/Runner/调度器/Omni Connector 多处**重构**，很快成为 committer（10:00–12:15）。
- 心得："做 contributor 初期，你对仓库的贡献远小于你在贡献中学到的东西"；两个仓库的 reviewer 很友好、愿带新人教 coding style（09:14–10:15）。

### 给新人的贡献建议
- **算力门槛**：Omni 模型不算特别小，但比主厂大模型小；**layerwise/modelwise 适配**可在单卡甚至个人电脑跑通；建议**租卡**（Runpod 两张 16G 卡约 $0.3–0.4/小时），或家里两张 RTX 系列"晚上+周末跑，一个月花不到 500 块"（04:00–05:00、13:00–15:00）。
- **别碰量化**（realization/quantization）：非常吃卡型号，没资源别碰；建议先用"麻雀模型"（如 Qwen 0.6B variant）在小卡上跑通测试再合入（14:00–15:15）。
- 熟悉项目路径：先用最小模型跑通 + 看每个模型 README + 跑单元测试 → 从 issue 列表挑**针对某个模型的 bug**（比框架层/权重 bug 好修，如"输出全是噪声""某版本跑不通"）→ 参加每周三北京时间 11:30 的会议（有录播，先记关键词再回看）→ 接单 stage 模型 → 提 RFC（19:00–22:00）。
- **PR 卫生**：feature 超 1000 行该拆、完整模型也尽量控行数；减少对框架/提交文件的改动，别引入奇怪代码（如误放训练代码）；超 5000 行尤其要拆（22:00–23:00、33:00 附近）。
- **学习法**：强烈建议找"铁巴"（学伴）用**费曼学习法**互相讲；"可以找 agent 一起学更快"但"agent 懂得太多，你需要找一个不懂的人讲懂"（23:00–24:00）。

### AI coding 与"编程在编两样东西"
- 引一个观点：**编程同时在编两样东西**——① 实体的 code；② 你脑海里对整个软件架构的**心智模型**。用 AI coding 后，"写出实体 code"这部分会被取代，但**建立并用心智模型做设计决策**暂时取代不了——"人类还有存在价值，还没被 agent 取代"（16:15–17:18）。
- 工作没消失，是**工作模式在剧烈迭代**：code with AI = 用 prompt 让 agent 解决相对复杂的算法/系统问题、找 bug；重点转向**写好 verifier（测试）**——"很多公司算子已 AI 生成，人花更多时间思考怎么写 verifier"（15:15–16:15、23:00–24:23）。
- 未来打算做"放大自己价值"的高维事：learn skill、把飞轮 build 出来让轮子自转（引 Roger"验证做好轮子就能转"），贡献"指数级上升"（25:00–26:26）。

### 多模态 serving 技术碎片
- **diffusion 蒸馏减步**：工业上视频/图像生成本就蒸馏过，5 步左右即可出接近原效果；world model 本质是对未来某个（latent）的预测（借游戏"focus area"变分辨率的思路，非 focus 区可糊）（00:00–02:03）。
- **world model 的 region-of-interest**：借昆泰的思路——小模型 identify 视频里最重要的东西，再用更强模型 detect；适合 GIPA 类只需大概、不需每个细节的模型（"新 paper 方向：region of interest for world model"）（27:28–28:32）。
- CFG parallel（cfg parallel）：一个请求默认生成一个空 prompt 作对照并行；VIT encoder 方向有 paper 做"只取局部关键 patch"压缩 token（还没模型这么用）（03:10–04:11、26:26–27:28）。
- **多模态模型结构未收敛**，非常适合学术界进来——不像 LLM 结构由工业界主导、来回就那几套，"你的 idea 很可能直接变成我们需要改进的地方"（18:18–19:18）。
- **单元测试 vs 端到端测试**：仓库测试分五级、按算力消耗/拉全重成本触发；internal test 在 refactor 后会崩一大堆，unit-to-run（端到端）更稳但 GPU 昂贵成本高——"像烤串一样把很多重要东西串起来测一遍更有意义"（24:23–25:23）。
- **内部 fork 的 rebase 之痛**：公司 fork 后每加一点东西，下次 rebase 难度**指数级上升**（patch 加法都可能变）；对策是**尽可能把接口层（API signature）贡献到开源、保留 proprietary 的 modeling layer**，把适配层打包/模块化，甚至用 agent 帮 rebase（但 agent 得逐 PR 理解意图再 apply）（28:32–30:33）。

## 相关主题

- [中美 AI 生态对照](../topics/china-us-ai.md)（中方开源推理社区的人才涌入与 onboarding 机制、vLLM-Omni committer 成长路径）
- [AI 与就业](../topics/ai-and-jobs.md)（"编程在编两样东西"、实体 code 被取代但心智模型/设计决策未被取代、工作模式剧变、重心转向写 verifier）
- [AI 算力与基础设施](../topics/ai-infrastructure.md)（多模态 serving：diffusion 蒸馏减步、CFG parallel、layerwise/modelwise、五级测试、fork rebase 与接口层开源策略）
- [使用 LLM 的实践](../topics/using-llms-in-practice.md)（code with AI、找不懂的人/agent 用费曼学习法、写好 verifier 是关键）
