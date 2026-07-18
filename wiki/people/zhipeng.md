# 志鹏（Zhipeng）

- **背景**: [vLLM-Omni 团队](vllm-omni-team.md) 的 **committer**，负责 DiT/diffusion 方向。原为**传统前后端软件开发、零 AI/Infra 基础**，2025 年 4 月起跟看月球大叔 vLLM 直播入门，约一年内成长为 committer。在新加坡（UTown）组织每周六的 vLLM 自习小组。
- **定位**: 本库首个"开源 onboarding 现身说法"——既是个人成长叙事，也是一份多模态推理开源社区的**贡献者指南**，落点 [中美 AI](../topics/china-us-ai.md)（中方开源社区人才涌入）与 [AI 与就业](../topics/ai-and-jobs.md)（AI coding 下"编程在编两样东西"）。

> 成长阶梯：改文档 → 抢 issue（研究一周修一个 HuggingFace config 问题）→ 第一个多模态模型支持（字节 Teres，约一个月、约 1000 行 PR，莫子峰 & Ceres 逐条 review）→ 七八个多模态模型 → 参与 Diffusion Worker/Runner/scheduler/Omni Connector 重构 → committer。

## 核心观点

- **"做 contributor 初期，你对仓库的贡献远小于你在贡献中学到的东西"**；两个仓库 reviewer 友好、愿带新人教 coding style（[视频](../videos/20260517-uncle-moon-zhipeng-vllm-contributor.md) 09:14–10:15）。
- **降低门槛的建议**：layerwise/modelwise 适配可单卡/个人电脑跑通；租卡（Runpod 两张 16G 约 $0.3–0.4/小时）或家用 RTX"一个月不到 500 块"；**别碰量化**（吃卡型号）；先用麻雀模型（Qwen 0.6B variant）测通再合入（04:00–15:15）。
- **PR 卫生**：feature 超 1000 行该拆、超 5000 行尤其要拆；减少对框架/提交文件改动，别引入奇怪代码（误放训练代码）（22:00–23:00）。
- **学习法**：找"铁巴"用**费曼学习法**互相讲；"可以找 agent 一起学更快"但"agent 懂得太多，你需要找一个不懂的人讲懂"（23:00–24:00）。
- **"编程在编两样东西"**：① 实体 code（AI coding 会取代）；② 脑海里对软件架构的**心智模型**（做设计决策，暂取代不了）——"人类还有存在价值，还没被 agent 取代"；重心转向**写好 verifier（测试）**（15:15–17:18）。
- 技术碎片：diffusion 蒸馏减步、world model 的 region-of-interest（小模型 identify 关键、强模型 detect）、CFG parallel、五级测试体系、内部 fork 的 rebase 指数级变难→**接口层贡献开源、保留 proprietary modeling layer**（详见[视频页](../videos/20260517-uncle-moon-zhipeng-vllm-contributor.md)）。

## 视频

- [从 AI 零基础到 vLLM/vLLM-Omni Committer，只用了一年（月球大叔，2026-05-17）](../videos/20260517-uncle-moon-zhipeng-vllm-contributor.md)
