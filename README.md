# oppo-experiemental-7B
**[Hugging Face](https://huggingface.co/OPPOResearchInstitute/oppo-experiemental-7B)**  

## 介绍

oppo-experiemental-7B是由OPPO研究院基于 **[Baichuan2](https://huggingface.co/baichuan-inc/Baichuan2-7B-Base)** 开发的一个大规模预训练语言模型，参数规模为70亿。在大模型评测 *[OpenCompass](https://opencompass.org.cn/leaderboard-llm)* 中文数据集表现同规模参数第一。

## 继续预训练
oppo-experiemental-7B沿用Baichuan2的框架，并且在Baichuan2的基础上进行了继续预训练，预训练语料包含800B tokens。覆盖了web网页、百科、书籍、代码等不同来源的数据。

## 指令学习
为了最大程度地激发预训练模型的能力，我们人工标注了大量涉及不同领域、不同任务共计2W条指令数据，除此之外，我们也收集了高质量指令数据，最终构成240W高质量中文指令数据。

## 评测结果 【中文数据集】

|模型|	综合|	学科|	语言|	知识|	理解|	推理|
| :-------------------------: | :-------: | :-------: | :-------------: | :-------------: | :--------: | :--------: |
|        oppo-experiemental-7B              |  **62.2** |  **54.7** |  **70.4**       |    **N/A**     |   **62.9** |   **67.9** |
|        Qwen-7B-Chat         |  **60.3** |  **55.9** |  **70.7**       |    **N/A**     |   **62.3** |   **54.7** |
|        InternLM-Chat-7B    |  **59.7** |  **49** |  **75.2**       |    **N/A**     |   **63** |   **58.8** |
|        Baichuan2-7B-Chat   |  **55.2** |  **46.2** |  **72.1**       |    **N/A**     |   **59.4** |   **47.7** |
|        XVERSE-7B    |  **54** |  **51** |  **80.3**       |    **N/A**     |   **54.8** |   **32.5** |
|        ChatGLM2-6B   |  **51.9** |  **46.8** |  **63.6**       |    **N/A**     |   **50.6** |   **53** |
|        TigerBot-7B-Chat-V3    |	**51.2** |  **34.6** |  **72.9**       |    **N/A**     |   **56.4** |   **52.3** |
|        Chinese-Alpaca-2-7B    |	**45.7** |  **34.6** |  **72.6**       |    **N/A**     |   **51.6** |   **31.2** |
|        Chinese-LLaMA-2-7B    |	**43.5** |  **26.6** |  **74.1**       |    **N/A**     |   **51.1** |   **31.2** |
|        Mistral-7B-v0.1    |	**43.4** |  **38.4** |  **60**       |    **N/A**     |   **46.2** |   **31.2** |

> 模型对比数据于2023年10月24日摘录自OpenCompass官网，模型表型仅代表提交时的成绩。

	
## 局限性
oppo-experiemental-7B中的模型针对中文场景进行了微调优化，相对应的，英文能力较弱。即便是中文领域，由于GPT类模型特点以及参数规模等限制导致模型的理解与表达能力也存在一定局限性。


## 声明与协议
### 声明
我们在此声明，我们未基于oppo-experiemental-7B开发任何应用，也呼吁所有使用者，不利用oppo-experiemental-7B进行任何危害国家安全或者违法违规活动，同时也要求所有使用者不将oppo-experiemental-7B用于未经安全审查和备案的互联网服务。由于模型本身存在局限性，仍有可能生成无法预知的问题。我们对使用者使用oppo-experiemental-7B开源模型而导致的任何安全、舆论风险、滥用等问题，我们将不承担任何责任。

### 协议
社区使用oppo-experiemental-7B 开源模型需要遵循 Apache 2.0协议，并且同时由于oppo-experiemental-7B基于Baichuan2 二次开发得到，使用者还需遵循《Baichuan 2 模型社区许可协议》。如果您将Baichuan 2用于商业目的，请按照《Baichuan 2 模型社区许可协议》要求申请并获得Baichuan官方审批。


## 致谢
oppo-experiemental-7B基于 *[Baichuan2](https://huggingface.co/baichuan-inc/Baichuan2-7B-Base)* 项目二次开发，在此对相关项目和研究开发人员表示感谢。
