# Mark Chen

- **背景**: OpenAI 首席研究官（CRO），此前为高频交易员转行 AI 研究，参与推理/o1 等关键项目。
- **来源出处**: [Latent Space "Cooking" 访谈（2026-06）](../videos/20260625-latent-space-mark-chen.md)

## 立场与核心观点

- **坚信 scaling laws、pre-training 未死**："pre-training is dead"叙事反复出现却每次被突破，已 hold 近 10 个数量级。
- **reasoning/o1 是最大的 bet**：靠 Yakub、Ilya 等人的 conviction 推动全公司。
- **evals crisis**：gold-standard benchmark 太少、经典基准已 saturate；bench maxing 使泛化失真。解法：代表性 eval 混合 + 持续造新 eval + 把造 eval 团队与优化模型团队分开（对抗）。
- **jagged frontier**：模型直觉≠人类直觉，很多归结为 context；**continual learning 是必须解锁的 basic primitive**。
- **vibe researcher**：工作转向 orchestration-focused，研究员出 idea、模型做执行，三年目标是端到端做研究；research taste 靠 replication 培养。
- 倾向单一多模态模型；高风险 bet 是 OpenAI 的 alpha。

## 与他人观点的呼应/分歧

- pre-training 未死：与 [姚顺宇](yao-shunyu.md) 一致。
- 评估危机/bench maxing：与 [Noam Brown](noam-brown.md) 高度互补（Noam 强调 test-time compute 维度，Mark 强调 eval 生产与团队分离）。
- 端到端做研究：与 [姚顺宇](yao-shunyu.md)、[Noam Brown](noam-brown.md) 对"AI 加速/接管研究"的判断同向。

## 已收录访谈

| 日期 | 视频 | 频道 |
|---|---|---|
| 2026-06-25 | [AGI、o1、评估与 Scaling Laws](../videos/20260625-latent-space-mark-chen.md) | Latent Space |

## 🔗 本库后续给 "evals crisis" 补上的机制（2026-10）

- ⚠️⚠️ **[Joseph Kim（OpenAI，ChatGPT 金融业务）在 2026-10-31](../videos/20261031-latent-space-openai-finance-joseph-kim-plugin-95-percent-taste-reward-model.md) 指认了一种会自我维持的调查偏差**：**"如果数字看起来好，研究员就假定模型变强了，然后不去调查它。而如果数字很难看，你就会去调查。"** ✅ **本库认为这给本页的 "evals crisis" 提供了一个机制层面的解释——eval 的 bug 只在它让模型显得变差时才会被发现，于是让模型显得更好的 bug 会永远留在原地，而饱和被系统性低估。**
- ⚠️ **同期他还对自家的 GDP eval 直接说"已经完全饱和，而没饱和的那些部分本质上是坏的，所以我们不报它了，也不再追踪它了"。** 🔗 完整记录见 [评估与 Benchmark](../topics/evaluation-and-benchmarks.md) 与 [Joseph Kim](joseph-kim.md)。
