# 月球大叔（Uncle Moon）

- **背景**: 中文 AI 技术向访谈频道主播（YouTube [@uncle_moon_x](https://www.youtube.com/@uncle_moon_x)，自述"在硅谷采访 100 个有意思的人"）。本人网络多媒体博士出身，故访谈偏**系统 / AI Infra 深水区**：KV Cache、SGLang、vLLM、RL 训练、推理优化。
- **定位**: 与 [张小珺](zhang-xiaojun.md)（偏商业/投资访谈）互补——月球大叔面向**一线研究员与 infra 创业者**，是本库中方**技术**视角的主来源之一。

> 主持风格：技术追问密集、常主动做名词科普（RLHF/RLVR、KV Cache）、频繁引导嘉宾给"职业建议"；因本人有网络多媒体研究背景，能与嘉宾在系统层面深聊。

## 已收录访谈

| 日期 | 嘉宾 | 主题 | 视频 |
|---|---|---|---|
| 2026-05-01 | SGLang/Miles 团队（陈阳、万诚、袁月明） | DeepSeek V4 混合注意力的推理与 RL 训练适配 | [链接](../videos/20260501-uncle-moon-sglang-deepseek-v4.md) |
| 2026-05-18 | [朱邦华（Banghua Zhu）](banghua-zhu.md) | SGLang、RLHF vs RLVR、二次创业 | [链接](../videos/20260518-uncle-moon-banghua-zhu-sglang.md) |
| 2026-05-17 | [志鹏（Zhipeng）](zhipeng.md)（及 Roger/林月谦） | 从 AI 零基础到 vLLM-Omni committer、开源贡献者指南 | [链接](../videos/20260517-uncle-moon-zhipeng-vllm-contributor.md) |
| 2026-06-09 | [江鋆晨（Junchen Jiang）](junchen-jiang.md) | KV Cache / LMCache、大模型的记忆 | [链接](../videos/20260609-uncle-moon-junchen-jiang-kvcache.md) |
| 2026-07-28 | [孟子立（Zili Meng）](zili-meng.md) | WiCi 无线 GPU、用 Wi-Fi 替代 PCIe、港科大教授兼创业 | [链接](../videos/20260728-uncle-moon-zili-meng-wici.md) |
| 2026-08-09 | [李正韬（Todd Li）](todd-li.md) | Retell AI：语音 AI 呼叫中心、YC、企业落地、招聘与薪酬 | [链接](../videos/20260809-uncle-moon-todd-li-retell-ai.md) |
| 2026-10-06 | [陈然](chen-ran.md) | AI 斩杀线、零人公司、硅谷风险认知、信息源分层、生产关系 | [链接](../videos/20261006-uncle-moon-chen-ran-zero-person-companies-ai-kill-line.md) |

> ⚠️ **该频道对部分中文访谈提供英文配音/字幕**（字幕轨内容为英文），孟子立那期与李正韬那期均是。相应视频页的引号内为**英文原文的中译**，不是中文原话。李正韬那期的字幕轨直接标为 `en`（人工），且**全程无说话人标签、无 `>>` 换人标记**，归属按内容判断。

> **频道选题的一次外扩**：前六期全部是 **AI infra / 系统研究者**（SGLang、vLLM、KV Cache、无线 GPU）；李正韬那期是频道内**第一期纯商业向的创业者访谈**（YC、企业销售、招聘与薪酬结构），技术含量低而组织与商业化含量高。本库因此把它主要落在 [AI 商业化与价值捕获](../topics/ai-business-and-value-capture.md) 与 [AI 与就业](../topics/ai-and-jobs.md)，而非 infra 条线。

> **第二组频道内对照（时机 vs 能力）**：[孟子立](zili-meng.md) 说硬件创业"**起步早是我们唯一真正的优势**"；[李正韬](todd-li.md) 说"**新技术出现后机会窗口只有两三年，现在才进语音赛道的多半不会成功**"。两位在同一频道、相隔两周，都把**时机**排在能力之上，且都在做被巨头俯视的细分。

> **频道内部形成的一处自我对照**：[朱邦华](banghua-zhu.md)（2026-05）说自己 **2022 年就看见了 AI 的崛起**；[孟子立](zili-meng.md)（2026-07）在同一节目上主动提起这句，并说"**很遗憾，我没看见**"——他 2022 年整年在 CMU 走完美国教职市场流程，试过 ChatGPT 仍未看出趋势，看到的是疫情期大厂裁员。两人同届同领域、判断相反，是本库中关于"时机判断力"最直接的一组一手对照。

## 相关

- 频道在 [watchlist.yaml](../../watchlist.yaml) 中 slug 为 `uncle-moon`（min_minutes: 20）。
- 中方对照的另一来源见 [张小珺](zhang-xiaojun.md)；技术主题落点见 [AI 算力与基础设施](../topics/ai-infrastructure.md)。

> ⚠️ **频道选题的第二次外扩，以及本库第一次被受访者当面批评了选题**（2026-10-06，[陈然](chen-ran.md)）：这一期是频道内**第一期以"个人方法论 + 组织重构 + 财务"为主轴**的访谈，技术含量低于李正韬那期，而方法论密度是频道内最高的。
> ⚠️⚠️ **而本库记下其中一条针对媒体生态（包括本库）的批评**：他把 AI 时代的信息源分成三层——**开汽车的人（真正用 AI 落地赚到钱的）**、**demo in public 的人**、**造汽车的人（做模型、infra、serving layer 的）**，然后指出 **"对于普通人而言，你知道如何造汽车其实跟你一点关系都没有"**，而 **"我们绝大多数这些报道也好、采访也好，都是围绕着造汽车这件事情来进行的"**（[视频页](../videos/20261006-uncle-moon-chen-ran-zero-person-companies-ai-kill-line.md) [01:50:25]–[01:53:28]）。
> ✅ **本库认为这条批评对本库适用**：本库材料高度集中在"造汽车的人"，而这一期正是少见的"开汽车的人"一侧的材料。⚠️ **同时记下利益相关：他是在这档节目上说这段的，并当场表扬了该节目的"一手信息"定位（[视频页](../videos/20261006-uncle-moon-chen-ran-zero-person-companies-ai-kill-line.md) [01:31:59]）。**

> **第三组频道内对照（AI 落地的前提）**：[陈然](chen-ran.md)（2026-10-06）说 **"如果你这个公司不是从上到下 all in AI、从 CTO 开始支持你，你这个公司的算法根本落不了地"**，而没有这种支持时的形态是 **"自娱自乐，写写博客，看不到商业价值，有点自嗨"**；⚠️ **这与 [徐天音](tianyin-xu.md) 那期"可靠性第一次能拿到资源"、以及 [李正韬](todd-li.md) 那期的企业销售经验方向一致——三位都把落地的瓶颈放在组织而不是模型上。** ✅ **本库认为陈然那条的特殊性在于他给了一次对照实验：同一个人、同一类工作，在没有高层支持的公司里落不了地，在自己当 CTO 的公司里把整个业务重写了一遍。**

> ⚠️ **本频道首次使用本地转录 + 说话人分离的一期**（陈然那期）：该视频无字幕，本库用 `fetch.py --transcribe --diarize`（faster-whisper large-v3-turbo + pyannote）产出转录稿，**分离出 2 位说话人**。⚠️ **本地转录对公司名与专有名词破坏较重**（Trulia、Tubi TV、Claude Sonnet、Suno 等均需按上下文还原），该期视频页页首列了还原表与**五处本库无法确定还原的拼写**。
