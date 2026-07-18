# vLLM Omni 团队

**vLLM Omni** 是从 vLLM 主库拆出的独立开源项目，专做**多模态/全模态（omni）模型的推理与 serving**——不仅多模态输入（理解），更支持多模态输出（生成，含 TTS/文生图/文生视频）。由 **Roger**（发起人，自称"拉拉队/带货"）、**林月谦**（AR/TTS committer）、**志鹏**（DiT/diffusion 负责人）等在月球大叔频道分享。华为等国内同学参与，约 4000 stars。本库首个"多模态 serving 基建"的中方一线视角，与 [SGLang](banghua-zhu.md)、[LMCache/KV Cache](junchen-jiang.md) 同属月球大叔 infra 系列。

> ⚠️ 无字幕本地 whisper 转录，专有名词已归一化，个别（DiT block 级缓存名、版本号）待官方确认。见[视频页](../videos/20260511-uncle-moon-vllm-omni.md)顶部说明。

## 核心观点

- **缘起**：Qwen 团队给 vLLM 提的 Qwen-Omni N2N 支持 PR **加一万行减一千行、几乎重写主库**、过度偏单模型——于是另立独立项目随模型演化（[视频](../videos/20260511-uncle-moon-vllm-omni.md) 00:01–00:06）。
- **核心抽象 = 把 PD 分离推广成通用 stage**：一个 stage 可以是多模态 encode/生成，stage 间传的不只 KV cache，还有 embedding/metadata，**方向可双向、可跳 stage**；两个 engine——AR（复用 vLLM）+ Diffusion/DiT（从头写）（00:03–00:04、00:14）。
- **工程**：omni connector 统一传输（单卡 shared memory、多卡走 Mooncake）、控制面/数据面解耦、chunkwise 异步流式把**首包延迟从近 10 秒降到 <1 秒**、RTF<1（"响应快的 AI 能给情绪价值"）（00:28–00:33）。
- **DiT 加速**：TeaCache（layer 级跳步）+ block 级缓存；并行 USP+Ring Attention（正交）、HSDP、VAE patching、CFG parallel（最稳）；实测现代显卡算力过剩、diffusion 可 continuous batching；边缘设备做 module/layer-wise CPU offload（00:41–00:57）。
- **国产硬件插件**：CUDA/ROCm + 华为昇腾 MPU、百度昆仑，新硬件接入不改核心逻辑（00:24–00:25）。
- **未来**：streaming input 支持 world model / VLA、与 veRL 集成做多模态 RL、更多 multi-stage 模型（Bagel、Qwen-Omni、混元 80B）（01:03–01:08）。

## 视频

- [多模态/全模态推理引擎的 stage 抽象与 DiT 加速（月球大叔，2026-05-11）](../videos/20260511-uncle-moon-vllm-omni.md)
- [志鹏：从 AI 零基础到 vLLM-Omni committer（月球大叔，2026-05-17）](../videos/20260517-uncle-moon-zhipeng-vllm-contributor.md)——DiT 负责人 [志鹏](zhipeng.md) 的成长现身说法与贡献者指南
