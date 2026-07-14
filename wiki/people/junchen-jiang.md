# 江鋆晨（Junchen Jiang）

- **背景**: 芝加哥大学计算机系教授；**TensorMesh** 联合创始人兼 CEO（基于开源 **LMCache** 打造的 KV Cache 存储/优化系统；已融两轮共 2000 万美金，投资方含 NVIDIA、AMD——两家独立看好）。长期合作者/公司 advisor：**Ion Stoica**（伯克利，Spark/Mesos/Databricks/Anyscale）。
- **学历**: 清华姚班本科（数学竞赛保送）→ CMU 博士（导师 **Hui Zhang / 张辉**，Conviva 创始人）→ Microsoft Research → 芝大教职。
- **研究脉络**: 网络视频流媒体分析 → 视频 AI 分析 → LLM 推理系统（KV Cache）。
- **来源出处**: [月球大叔访谈（2026-06）](../videos/20260609-uncle-moon-junchen-jiang-kvcache.md)

> 与 [朱邦华](banghua-zhu.md)（SGLang/Miles）同属"从学术研究组挑战工业界 AI Infra"的中国背景创业者群体，两人的公司/项目（LMCache 与 SGLang/vLLM 推理引擎）在技术栈上紧密相邻。

## 立场与核心观点

- **KV Cache = 大模型的记忆 = "给大模型看的视频"**（KV Cache 与视频都是 3D tensor，是"只有大模型看得懂的视频"）；核心预测：它会成为**继模型权重、prompt 之后下一个最大的数据层**，是"未来的石油"。
- **数据层普适规律**：任何应用规模够大就必然需要一个数据层（web→CDN、大数据→Spark/HDFS、AI→KV Cache）；这是他从视频流媒体迁移到 KV Cache 的底层直觉。
- **LMCache 战略**：以开源做成事实标准，把 KV Cache 层与推理引擎/存储/GPU/运行环境**解耦**（但不与模型解耦）；类比 Spark"踩着工业界实体出来"。TensorMesh slogan："不要为了模型在相同内容上重复计算来交钱"。
- **prefill vs decode 误区**（反直觉）：硬件多在优化 decode（用户可见），但 **~90% 算力其实花在 prefill/处理 input**——因为 agent 的 input 远长于 output，且"任何 output 都会变成以后的 input"。
- **OpenAI API 兼容格式 = AI 时代的 IPv4**（稳定下来的"细腰"协议）；KV Cache 有望成为下一个这样的标准层。
- **硬件"IBM 化" vs disaggregation**：厂商把处理器/网络/存储 bundle 成大型机（走 IBM 老路），但历史上大型机没成主流；disaggregation 做到极致（每块特殊化、可替换）可能带来颠覆性新 infra。
- **方法论**："高阶 CS 课其实是历史课"（读经典 paper = 学历史以预判未来）；研究员要进"工业界染缸"当工程师看真问题；做老师 = 提出问题而非解决问题。
- **师生联合创业是稳定结构**："老师创业不成，很大原因是学生没跟着做"；trust 比什么都珍贵。

## 与他人观点的呼应/分歧

- **记忆/长上下文**：与 [Dan Biderman](../videos/20260713-latent-space-dan-biderman.md)（"长上下文还不够、AI 的记忆问题"）直接呼应——江从 infra 侧给出"可管理、可优化的模型原生记忆（KV Cache）"这一具体载体。
- **推理是主战场**：与 [朱邦华](banghua-zhu.md)"training infra 太一次性、模型绝大多数生命周期在推理"一致。
- **taste 作为差异化**：与 [朱邦华](banghua-zhu.md) 的"招人看 taste/criticism"一致——江强调 AI 难替代的是 design taste（自己得知道什么设计好，才能 supervise AI）。
- **OpenAI/Anthropic 未必一家独大**：以视频流市场（YouTube/Netflix 占大头但仍有很多提供商）类比 AI 模型市场，与 [朱邦华](banghua-zhu.md)"希望百花齐放"相近。

## 已收录访谈

| 日期 | 视频 | 频道 |
|---|---|---|
| 2026-06-09 | [KV Cache 是大模型的记忆、是"未来的石油"](../videos/20260609-uncle-moon-junchen-jiang-kvcache.md) | 月球大叔 |
