# Robin Rombach

- **背景**: **Black Forest Labs** 联合创始人/CEO，在德国 Black Forest（黑森林山区，Freiburg）与旧金山双基地。**latent diffusion 发明者**（PhD 在慕尼黑），做过 Stable Diffusion，开源图像模型 **Flux**。公司成立约 2 年、刚过 100 人、在招。
- **定位**: 本库首个"开源图像/视频生成 → 多模态 world-action model → 机器人"的一线视角，与做机器人大脑的 [Physical Intelligence（Kay Ke）](kay-ke.md)、做多模态 serving 的 [vLLM-Omni](vllm-omni-team.md) 构成互补，落点 [物理 AI 与机器人](../topics/physical-ai-and-robotics.md)。

> latent diffusion：把图像/视频/音频**压缩成高效表征再训 transformer**（JPEG/MP3 的神经版），是所有生成式图像模型的底层算法。

## 核心观点

- **收敛到多模态 world-action model**：同一模型做图/视频/音频 + **action prediction**，最终可部署为机器人大脑——"要生成世界的视频，你必须理解世界"；直觉智能（图像入手、算力低）+ 深度推理层互补；视频预训练给出对物理/交互的隐式理解（[All-In](../videos/20260710-all-in-cerebras-bfl-open-source.md) 00:42–00:44）。
- **生成"老虎机"批评的解法 = 暴露尽量多操控层**：text→image 扩到 text+image→image（编辑/迭代）、多图语义合成，同原理推广到视频，输入输出同模型时更有意思（00:44–00:46）。
- **Scorsese 合作**：把导演脑中场景（东欧村庄）迭代成图像帮助沟通，"语言是有损媒介、视觉更丰富"；不认为终极目标是"生成整部电影"，而是 **human-in-the-loop 当媒介**、平行化 brainstorming/storyboard（00:46–00:50）。
- **生产落地**：一部"比特币电影"在 sound stage 无绿幕拍、背景全生成（$3000 万预算，否则 $1.5 亿、根本不会被 green-light）；高端影视是最苛刻用例，技术在快速改进轨迹上（00:50–00:53）。
- **机器人 in-context**：目标是像 prompt LLM 一样在 context 里提示机器人"去拿这杯橙汁"；现状是不同硬件有不同 action 表征、需少量小时级微调，目标是尽量 in-context（00:55–00:57）。
- **开源 + IP**：给 Disney 等建议共同训练模型（部分基于开源、部分闭源）；公开工具**限制生成特定 IP**是合理做法；最有意思的是**粉丝二创**（Star Wars 同人从 fanfiction→fan film→AI 重现未讲故事），让 IP 方通过授权费赋能创作（00:57–01:01）。

## 视频

- [开源赢麻、Scorsese 的 AI 工具箱（All-In，2026-07-10）](../videos/20260710-all-in-cerebras-bfl-open-source.md)
