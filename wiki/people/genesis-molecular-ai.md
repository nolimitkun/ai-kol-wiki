# Genesis Molecular AI（Evan Fineberg & Sergey Edunov）

- **背景**: 做**小分子药物发现**基础模型的公司（原名 Genesis Therapeutics，2019 年成立，源自 Stanford VJ Pande 实验室的深度学习研究）。
  - **Evan Fineberg**：创始人/CEO，物理 + CS 背景，Stanford PhD 期间发 PotentialNet、MoleculeNet 等图神经网奠基工作。
  - **Sergey Edunov**：CTO，物理出身，原 Meta FAIR，**领导过 Llama 2/3 预训练**；后"回归物理老本行"加入 Genesis。
- **定位**: 本库第二块系统性"AI for science"来源（与 [Lila Sciences](lila-sciences.md) 并置）。主题句：**当下最创新的 diffusion 研究发生在 3D 结构预测，而非图像/视频生成**。把 LLM 的 scaling 三段式搬到分子结构预测。

> 主力模型 **Pearl** 做 protein–small molecule co-folding（类比 AlphaFold 3 / Boltz / OpenFold 3，但专注小分子）。公司改名为 Genesis Molecular AI 以回归"从第一天就是 AI 公司"的身份；主要给大 pharma（Gilead/GSK/Insight）做 AI 服务，同时自有 pipeline。

## 核心观点

- **diffusion 的最前沿在结构生物学**：2017–18 以为 GAN 是图像未来，但 GAN（mode collapse）对蛋白复合物不 work；diffusion 才是对的 primitive；如今图像/视频有些转回 AR，而"最创新的 diffusion 研究在 3D 结构预测"（[Latent Space](../videos/20260630-latent-space-genesis-diffusion-drug-discovery.md) 00:00、01:06–01:08）。
- **Pearl = LLM scaling 三段式搬到结构预测**：① 物理模拟造**合成数据**（PDB 只有约 20 万晶体结构、增长极慢）；② **推理时 scaling**——模型在"晶体结构表征"而非语言 token 上迭代（diffusion head 天然多步），用**物理引导**steer；③ RL 含"实验室 in-the-loop"（00:16–00:19、01:09–01:11）。
- **1Å 而非业界惯用的 RMSD<2Å**：药物发现是"分辨率的科学"——2Å 下芳香环可翻转仍算有效、且看起来正常会误导 med chemist；氢键窗口仅约 0.6Å，核心结合区要亚埃分辨率（00:41–00:51）。
- **结构≠药**：AlphaFold 3 诺奖 ≠ 药物发现解决；还要预测 30+ ADMET 性质，且药物性质常**反相关**（结合力↑→疏水↑→溶解度↓）（00:35–00:37、01:19–01:21）。
- **eval 危机**：RMSD<2 源自 AI 前的学术 docking（写论文非造药），被 AI 社区沿用；PoseBusters/LDDT/OpenBind 推动 eval 转型；类比 SWE-bench 刷榜赢但没人用它写代码（00:55–00:58）。
- **narrow model 观 + GPU 瓶颈**：反对做"通用分子智能模型"，主张为窄任务做很不同的架构（"LLM 架构本质还是 2017 transformer，有点无聊"）；瓶颈许愿都是 **GPU**——"LLM 公司在吸走所有 GPU 容量"、质疑纯 LLM 空间剩下的 alpha（01:16–01:17、01:42–01:46）。
- **中美对照**：西方 pharma 依赖 CRO 致尖端湿实验能力退化；中国 biotech（Insight）**自建极强 in-house 实验能力、数据产出极快**，是"设计-造-测-分析"闭环关键；"美国生物技术输给中国不是创新问题"是"房间里的大象"（01:12–01:14）。

## 视频

- [最前沿的 diffusion 研究在药物发现（Latent Space，2026-06-30）](../videos/20260630-latent-space-genesis-diffusion-drug-discovery.md)
