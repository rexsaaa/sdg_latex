Dear Editor,

We would like to submit our manuscript entitled "Privacy-Preserving Interpretable Single-Domain Generalization for Multi-Label Ocular Disease Recognition" for consideration by Computers and Electrical Engineering. We confirm that this work is original and has not been published elsewhere, nor is it currently under consideration for publication elsewhere. 

In this work, we address multi-label ocular disease recognition under practical clinical constraints, where multiple diseases may co-occur in one eye, cross-institutional domain shift degrades model generalization, and medical data privacy restricts multi-source collaboration. We formulate this problem as privacy-preserving interpretable single-domain generalization and build a unified framework with three matched components: a Dual-Branch Guided Domain-Invariant Feature Extraction (DFE) module that uses style-disturbed source-domain images, CAM-based disease-region guidance, and dual-branch mask-based contrastive learning to suppress domain-specific noise and extract disease-related invariant features from a single source domain; an Adaptive Label-Feature Relevance Construction (ARC) module that uses Transformer self-attention and cross-attention to model label-label relevance and label-feature relevance, thereby reducing false positives and false negatives caused by ocular disease co-occurrence; and an Adaptive Gaussian Differential Privacy (AdaGDP) mechanism that injects dynamically decayed Gaussian gradient noise during training to balance privacy preservation and model performance. Experiments on ocular disease recognition benchmarks show that the proposed framework improves in-domain and cross-domain multi-label recognition, enhances CAM-based interpretability, and maintains performance close to the public official baseline under a moderate privacy budget.

The code will be made available at https://github.com/rexsaaa/ppisdg-ocular upon publication.

We consider that this manuscript is appropriate for publication by Computers and Electrical Engineering because its content aligns with the domain of interest of the journal. We have no conflicts of interest to disclose.

Thank you for your consideration of this manuscript.

Sincerely,

Best regards,

Zhi-Ri Tang

Associate Professor

School of Intelligent Systems Science and Engineering,

Jinan University

Email: tangzhiri@jnu.edu.cn

---

## 中文注释版，仅供内部检查

尊敬的编辑：

我们希望提交题为《Privacy-Preserving Interpretable Single-Domain Generalization for Multi-Label Ocular Disease Recognition》的稿件，请贵刊 Computers and Electrical Engineering 考虑发表。

我们确认该工作为原创研究，未曾在其他地方发表，目前也未被其他期刊或会议同时考虑发表。

本文面向实际临床约束下的多标签眼病识别问题。在这一场景中，同一只眼睛可能同时存在多种疾病，跨机构域偏移会削弱模型泛化能力，医学数据隐私又限制了多源协同训练。我们将该问题表述为兼具隐私保护和可解释性的单域泛化问题，并构建了一个由三个匹配组件组成的统一框架：Dual-Branch Guided Domain-Invariant Feature Extraction，即 DFE 模块，利用风格扰动后的源域图像、CAM 疾病区域引导以及双分支 mask-based contrastive learning，从单一源域中抑制域特异性噪声并提取疾病相关的域不变特征；Adaptive Label-Feature Relevance Construction，即 ARC 模块，利用 Transformer self-attention 和 cross-attention 建模标签-标签相关性与标签-特征相关性，从而减少眼病共现导致的假阳性和假阴性；Adaptive Gaussian Differential Privacy，即 AdaGDP 机制，在训练过程中注入动态衰减的高斯梯度噪声，以平衡隐私保护和模型性能。眼病识别基准实验表明，该框架提升了域内和跨域多标签识别性能，增强了基于 CAM 的可解释性，并且在中等隐私预算下保持了接近公开官方基线的性能。

代码仓库已创建于 https://github.com/rexsaaa/ppisdg-ocular，并将在论文发表后更新。

我们认为该稿件适合发表在 Computers and Electrical Engineering，因为本文提出的是一种面向医学图像分析的计算方法，融合了深度学习、域泛化、可解释性和隐私保护等内容，与智能计算和电气工程应用方向相关。

我们声明不存在利益冲突。

感谢您考虑本稿件。

此致

Prof. Zhi-Ri Tang

暨南大学智能科学与工程学院/人工智能产业学院

邮箱：tangzhiri@jnu.edu.cn

---

## 导师模板中文对照版，仅供结构对比

尊敬的编辑：

我们希望提交一篇题为《OmniSal: Omni-modal Saliency Fusion via Self-Supervised Vision Priors》的修改稿，请 Information Fusion 考虑发表。

我们确认该工作为原创研究，未曾在其他地方发表，目前也未被其他期刊或会议同时考虑发表。

在该工作中，作者从信息融合的角度重新定义通用显著性目标检测问题，将其视为把通用自监督视觉先验与特定模态证据进行对齐、蒸馏和精炼的问题，并据此提出 OmniSal。OmniSal 是一种全模态显著性融合检测器，采用冻结的 DINO 风格自监督视觉基础编码器作为基础，并围绕该编码器设计了三个匹配机制：Modality-Aware Low-Rank Adapter，即 MA-LoRA，用于在不完整重训练主干网络的情况下，将 RGB 训练得到的主干扩展到深度和热成像模态，并支持显著性引导的跨模态融合；Self-Distillation Saliency Prior Injection，即 SDSP 模块，用于激活编码器中潜在的显著性先验以支持监督检测；Frequency-Spatial Boundary Refinement Decoder，即 FS-BRD，用于在编码器输出较粗的 patch 级特征时仍获得像素级精确边界。在单模态 RGB 和双模态 RGB-D、RGB-T 基准上，OmniSal 在只更新少量主干参数的情况下显著优于近期专门方法，并且在跨域和低数据条件下表现出稳定增益。这表明，冻结的自监督视觉先验经过适当对齐、蒸馏和精炼后，可以作为统一显著性融合和显著性目标检测中强大且可复用的主干。

代码可在以下地址获取：https://github.com/taromm/OmniSal.git。

我们认为该稿件适合发表在 Information Fusion，因为其内容符合该期刊的研究兴趣范围。

我们声明不存在利益冲突。

感谢您考虑本稿件。

此致

Prof. Zhi-Ri Tang

暨南大学智能科学与工程学院，副教授

邮箱：tangzhiri@jnu.edu.cn
