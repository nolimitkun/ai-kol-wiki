# Let's build the GPT Tokenizer（Karpathy，2024-02-20）

- **讲者**: [Andrej Karpathy](../people/andrej-karpathy.md)
- **来源**: [YouTube](https://www.youtube.com/watch?v=zduSFxRajkE) · 134 分钟
- **转录稿**: [sources/karpathy/20240220-zduSFxRajkE](../../sources/karpathy/20240220-zduSFxRajkE/transcript.md)
- **性质**: Zero to Hero 系列：从零实现 BPE tokenizer（产物为 minbpe 仓库），并系统解释 tokenization 引发的各种 LLM 怪象

## 概要

开场即立论："tokenization 是我在 LLM 工作中最不喜欢的部分，但 LLM 的大量怪异行为最终都能追溯到它。"
视频从 Unicode/UTF-8 讲到 BPE 实现、GPT-2/4 的正则分块规则、sentencepiece 对比、词表大小的权衡，
最后逐条回收开头列出的怪象清单。

## 核心观点

### 为什么需要 tokenization
- Token 是 LLM 的"原子"；tokenizer 是完全独立于 LLM 的组件，有自己的训练集和训练过程（BPE），训练完只做编解码（00:39–00:42）。
- 直接用 Unicode 码点（词表 15 万且标准一直在变）或原始 UTF-8 字节（词表只有 256，序列被拉得太长）都不行；BPE 在"词表大小 vs 序列长度"之间做可调的压缩权衡（00:15–00:23）。
- 他明确表态：**"谁能消灭 tokenization，谁就获得永恒荣耀"**——tokenization-free 的字节级模型（分层 Transformer）是他期待的方向，但尚未被充分验证（00:22–00:23）。

### 工程细节与陷阱
- GPT 系列在 BPE 之上加正则分块（字母/数字/标点/空格分开，禁止跨类合并），避免 "dog." "dog!" 各成一 token；GPT-4 的正则改进：大小写不敏感、数字最多 3 位合并（00:57–01:14）。
- GPT-4 词表 ~10 万（GPT-2 的两倍）：同样文本 token 数减半 = 有效上下文翻倍；对 Python 缩进空格的合并是 GPT-4 代码能力提升的重要一环——"GPT-2 不擅长 Python 很大程度是 tokenizer 的 bug"（00:12–00:14、01:56）。
- 词表大小的权衡：太大则嵌入表/输出层膨胀、稀有 token 训练不足、单 token 塞入太多信息模型"来不及思考"；当前业界甜点区约几万到 10 万（01:44–01:46）。
- sentencepiece（Llama 系用）在码点层面跑 BPE + byte fallback，历史包袱重、文档差、坑多；他更推荐 tiktoken 的字节级 BPE 风格（01:29–01:43）。
- 加特殊 token（对话结构、工具调用）需要小型"模型手术"：扩嵌入表行、扩输出层，常配合冻结基座只训新参数（01:24–01:25、01:47–01:48）。

### 怪象清单的统一解释（都是 tokenization 的锅）
| 怪象 | 根源 |
|---|---|
| 拼写/反转字符串差 | 长 token 内的字符对模型不可见（.DefaultCellStyle 是单 token） |
| 非英语更差 | tokenizer 训练集英语占比高 → 非英语被切得更碎，同样内容占 3 倍 token，上下文被稀释 |
| 算术差 | 数字被任意切分（4 位数可能是 1/2/3/4 个 token 的任意组合）；Llama 2 因此强制拆分所有数字 |
| 见到 "<endoftext>" 行为异常 | 特殊 token 处理逻辑泄漏到用户输入 = 攻击面 |
| 尾随空格警告 / 部分 token | 补全从分布外的"半个 token"开始，模型崩溃（tiktoken 里有大量未文档化的 unstable token 特判代码） |
| SolidGoldMagikarp | tokenizer 训练集（含 Reddit）与 LLM 训练集不一致 → 该 Reddit 用户名有专属 token 但从未被训练，"未初始化内存"喂进 Transformer 产生未定义行为 |
| YAML 优于 JSON | token 密度：同样数据 JSON 116 token、YAML 99 token——"token 经济"下要计较编码效率 |

（怪象回收部分在 01:51–02:10）

## 相关主题

- [LLM 心理学与认知短板](../topics/llm-psychology.md)（tokenization 盲区是"瑞士奶酪"的重要成因）
- [LLM 训练管线](../topics/llm-training-pipeline.md)
- [LLM 安全](../topics/llm-security.md)（特殊 token 注入、SolidGoldMagikarp 类攻击面）
