# v2 相对 v1.0 中文修改对应英文译文检查

说明：本文件汇总当前中文稿相对 git tag `v1.0` 存在语义新增/修改的中文段落，并列出当前英文稿/compare 稿中的对应英文。已尽量过滤纯空格变化。

## 初步检查意见

- 整体看，新增/修改中文的英文版本大多已在 compare/trans 中对应。
- 已处理：摘要中 “Adaptive Label-Feature Relevance Construction” 与 “Dual-Branch Guided Domain-Invariant Feature Extraction” 的英文名大小写已统一。
- 已处理：方法章中 CAM 权重已改为 Grad-CAM 中的类别相关通道重要性权重，即类别得分对通道激活图梯度的全局平均池化结果。
- 已处理：实验章 compare 稿的 t-SNE 子图小标题已补充英文。

## 00_frontmatter

**中文 v2：**

早期眼底筛查是眼科疾病诊断的有效方法。近年来，深度学习的发展为眼底图像分析提供了强大工具。然而，真实临床部署仍面临三个层层递进的挑战：（1）单只眼睛中常同时存在多种疾病，若将各疾病独立建模，容易造成误检与漏检；（2）跨机构部署存在数据分布偏移，而常见的跨域方法通常预设可访问目标域或多源域数据，这一前提在真实医疗场景中难以满足；（3）医疗数据具有较强的隐私敏感性，进一步限制了跨机构数据共享，使得多源域的预设难以成立，因此需要在本地隐私保护前提下实现良好的泛化性能。针对上述三个挑战，我们首先提出自适应标签-特征关联性构建模块（Adaptive Label-Feature Relevance Construction, ARC），通过 Transformer 注意力机制捕捉疾病共现依赖，减少多标签识别中的误检与漏检；其次设计双分支引导域不变特征提取模块（Dual-Branch Guided Domain-Invariant Feature Extraction, DFE），在类激活映射（Class Activation Mapping, CAM）引导下仅使用单一源域数据学习域不变特征，在提升未知域泛化性能的同时增强模型可解释性；最后将自适应高斯差分隐私（Adaptive Gaussian Differential Privacy, AdaGDP）机制集成至训练流程中，通过动态梯度噪声注入实现隐私保护，并将性能损失控制在可接受范围。实验表明，所提方法在 ODIR 上取得 78.85 的 Final score，优于所选代表性多标签眼科疾病识别方法，并在 EDID 跨域数据集上取得 3.19 个百分点的提升。综上，本文搭建了一个面向多标签眼科疾病识别的可解释与隐私保护单域泛化框架，提升了跨域泛化性能，并为隐私保护场景下的眼科疾病诊断提供启发。

**对应英文：**

Early fundus screening is an effective approach for ocular disease diagnosis. Recent advances in deep learning have provided powerful tools for fundus image analysis. However, real clinical deployment still faces three increasingly constraining challenges: (1) multiple diseases often co-occur in a single eye, causing false positives and false negatives when diseases are modeled independently; (2) cross-institutional deployment suffers from domain shift, yet conventional cross-domain methods typically presume access to target-domain or multi-source data, which is often infeasible in practice; (3) medical data are highly privacy-sensitive, which further restricts cross-institutional sharing and invalidates the multi-source assumption, calling for generalization under local privacy preservation. To address these three challenges in order, we first propose an Adaptive Label-Feature Relevance Construction (ARC) module that captures disease co-occurrence dependencies via Transformer attention to reduce false positives and negatives. Then, we design a Dual-Branch Guided Domain-Invariant Feature Extraction (DFE) module that learns domain-invariant features from a single source domain under Class Activation Mapping (CAM) guidance, improving unseen-domain generalization while enhancing interpretability. Finally, we integrate an Adaptive Gaussian Differential Privacy (AdaGDP) mechanism into training, preserving privacy via dynamic gradient noise injection with controlled performance loss. Experiments show that our method reaches a Final score of 78.85 on ODIR, outperforming representative multi-label ocular disease recognition methods, and yields a 3.19-point gain on the EDID cross-domain dataset. Overall, we establish an interpretable and privacy-preserving single-domain generalization framework for multi-label ocular disease recognition, improving cross-domain performance and providing insights into ocular diagnosis under privacy-preserving scenarios.


## 01_introduction

**中文 v2：**

早期眼底筛查是眼科疾病诊断的有效手段，所采集的眼底图像能够反映视网膜、视盘、血管和黄斑区域的多类病变征象。通过对眼底图像进行分析，有助于及早发现潜在病变并进行干预，从而降低不可逆的视力损伤甚至视力丧失的风险。随着眼底筛查规模扩大，人工阅片面临耗时长、依赖专家经验、难以在基层医疗机构大规模普及等问题，因此基于眼底图像的眼科疾病诊断具有重要应用价值 \hyperref[_Ref213949315]{{[}1{]}}。围绕眼底筛查，现有方法大体可分为传统机器学习（Machine Learning, ML）、视觉语言模型（Vision-Language Model, VLM）和卷积神经网络（Convolutional Neural Network, CNN）三类路线。传统机器学习通常通过手工设计纹理、形态等人工特征，再结合支持向量机、随机森林等分类器完成识别 \hyperref[_RefRahman2022MLFundus]{{[}2{]}}，这类方法具有一定可解释性，但特征设计依赖先验经验，对复杂眼底病灶和多疾病共存场景的表达能力有限。近年来，视觉语言模型为眼底图像理解、图文联合分析和医学报告生成提供了新的研究方向 \hyperref[_RefLim2024VLVOphthalmology]{{[}3{]}}\hyperref[_RefUrooj2025LLMMedicalImage]{{[}4{]}}，但其训练和微调通常依赖大规模高质量标注数据、图文配对数据以及较高算力资源，在医疗数据稀缺、隐私受限和临床部署资源有限的场景中仍面临较高成本。相比之下，以 CNN 为代表的深度视觉模型能够直接从眼底图像中学习局部纹理、病灶区域和空间结构特征，已广泛应用于疾病识别 \hyperref[_Ref213871637]{{[}5{]}}、病灶分割 \hyperref[_Ref213948625]{{[}6{]}}、医学图像重建 \hyperref[_Ref213948898]{{[}7{]}}和疾病诊断与预测 \hyperref[_Ref213949262]{{[}8{]}}等任务。因此，本文选择 CNN 作为多标签眼科疾病识别任务的基础路线。然而，在真实临床部署中，基于 CNN 的眼科疾病识别方法仍面临多疾病共存、跨机构部署泛化性能下降以及隐私保护等挑战。具体而言：

**对应英文：**

Early fundus screening is an effective approach for ocular disease diagnosis, as it can reveal diverse pathological signs in the retina, optic disc, blood vessels, and macular region. Analyzing fundus images helps identify potential lesions and supports early intervention, thereby reducing the risk of irreversible visual impairment or even vision loss. As fundus screening continues to expand, manual fundus screening is limited by its time cost, dependence on expert experience, and shortage of primary medical resources. Fundus-image-based ocular disease diagnosis therefore has important practical value \hyperref[_Ref213949315]{{[}1{]}}. Existing methods for fundus screening can be broadly grouped into three technical directions: Machine Learning (ML), Vision-Language Model (VLM), and Convolutional Neural Network (CNN). ML methods usually rely on hand-crafted features such as image enhancement, lesion segmentation, texture, or morphology, followed by classifiers such as support vector machines or random forests for recognition \hyperref[_RefRahman2022MLFundus]{{[}2{]}}. These methods offer a degree of interpretability, but their feature design depends heavily on prior experience and has limited capacity to represent complex fundus lesions and multi-disease co-occurrence. In recent years, VLM has opened new directions for fundus image understanding, image-text joint analysis, and medical report generation \hyperref[_RefLim2024VLVOphthalmology]{{[}3{]}} \hyperref[_RefUrooj2025LLMMedicalImage]{{[}4{]}}. However, their training and fine-tuning generally require large-scale high-quality annotations, paired image-text data, and substantial computational resources, which remain costly when medical data are scarce, privacy is restricted, and clinical deployment resources are limited. In contrast, CNN-based deep visual models can directly learn local textures, lesion regions, and spatial structural features from fundus images, and have been widely applied to disease recognition \hyperref[_Ref213871637]{{[}5{]}}, lesion segmentation \hyperref[_Ref213948625]{{[}6{]}}, medical image reconstruction \hyperref[_Ref213948898]{{[}7{]}}, and diagnosis and prediction of ocular diseases \hyperref[_Ref213949262]{{[}8{]}}. Therefore, we adopt CNN as the main modeling backbone for multi-label ocular disease recognition. Nevertheless, in real-world clinical deployment, CNN-based ocular disease recognition methods still face challenges including multi-disease co-occurrence, degraded generalization performance across institutions, and privacy preservation. Specifically:

**中文 v2：**

1.在临床眼科疾病诊断中，单只眼睛可能同时存在多种疾病，若仍采用标准单标签分类器或将不同疾病完全独立建模，容易造成误检与漏检 \hyperref[_Ref213949362]{{[}9{]}}。近年来，自然图像中也存在多标签识别方法的相关工作，比如 ML-GCN \hyperref[_Ref213949382]{{[}10{]}}，通过统计各标签的共现频率建立图关联性，使得识别出某个标签后，更有可能识别出其关联标签，从而减少漏检。而在多标签眼科疾病识别中，各疾病之间的关联性更加错综复杂，仅靠标签共现频率来建立疾病关联性的方法对于这种复杂情况可能不够可靠。因此，面向眼底图像的多疾病共存场景，仍需要探索一种更高效可靠的标签-特征关联性构建方法。

**对应英文：**

1. In clinical ocular disease diagnosis, a single eye may present multiple diseases simultaneously. Using a standard single-label classifier, or modeling different diseases as fully independent, can therefore lead to false positives and false negatives \hyperref[_Ref213949362]{{[}9{]}}. Multi-label recognition has also been widely studied for natural images. For example, ML-GCN \hyperref[_Ref213949382]{{[}10{]}} constructs graph relevance from label co-occurrence frequencies, making relevant labels more likely to be recognized once a given label is identified and thereby reducing false negatives. However, in multi-label ocular disease recognition, disease relevance is more complex, and methods that infer disease relevance solely from label co-occurrence frequencies may be insufficiently reliable. For multi-disease co-occurrence in fundus images, a more reliable method for label-feature relevance construction is therefore needed.

**中文 v2：**

2.医疗图像数据与自然图像不同，其标注通常需要专业医生完成，数据获取和标注成本较高；同时，不同医疗机构之间还存在数据共享限制、标签空间不统一等问题，使多源域数据的访问与协同训练并不总是容易实现。然而，即使通过某个医疗机构的训练集训练得到了一个性能良好的模型，将其应用到另外的机构时，目标域数据也常因成像设备、光照条件和人工处理流程差异产生域偏移 \hyperref[_Ref213949348]{{[}11{]}}，导致模型性能下滑。如\figsubref{fig:intro-domain-gap}{a1}和\figsubref{fig:intro-domain-gap}{a3}所示，源域和目标域的分布有差异，仅在源域训练的 base model（\figsubref{fig:intro-domain-gap}{b1}）得到的决策边界可能不适用于目标域分布（\figsubref{fig:intro-domain-gap}{b2}）。常见的域适应（Domain Adaptation, DA）方法选择将源域和目标域数据一同送入模型训练来对齐域分布 \hyperref[_Ref213949354]{{[}12{]}}，但这需要训练阶段访问目标域数据；多源域泛化方法虽可避免访问目标域，但通常依赖多个源域共同训练。在医疗数据协同训练受限的实际场景中，上述前提往往难以满足。因此，探索仅利用单一源域提取域不变特征的单域泛化方法，更符合跨机构部署需求。

**对应英文：**

2. Medical images differ from natural images because their annotations usually require professional physicians, making both data acquisition and annotation costly. In addition, data sharing restrictions and inconsistent label spaces across medical institutions often limit access to multi-source-domain data and collaborative training. Even when a model performs well on the training set of one medical institution, applying it to another institution can introduce domain shift in the target domain because of differences in imaging devices, illumination conditions, and manual processing procedures \hyperref[_Ref213949348]{{[}11{]}}, resulting in performance degradation. As shown in \hyperref[fig:intro-domain-gap]{Fig.~\ref*{fig:intro-domain-gap}.a1} and \hyperref[fig:intro-domain-gap]{Fig.~\ref*{fig:intro-domain-gap}.a3}, the distributions of the source domain and target domain differ. The decision boundary learned by a base model trained only on the source domain (\hyperref[fig:intro-domain-gap]{Fig.~\ref*{fig:intro-domain-gap}.b1}) may not fit the target-domain distribution (\hyperref[fig:intro-domain-gap]{Fig.~\ref*{fig:intro-domain-gap}.b2}). Common domain adaptation (DA) methods align domain distributions by jointly using source-domain and target-domain data during model training \hyperref[_Ref213949354]{{[}12{]}}, but this requires access to target-domain data during training. Although multi-source domain generalization methods avoid access to the target domain, they usually rely on joint training across multiple source domains. In practical settings where collaborative training with medical data is restricted, these assumptions are often hard to meet. Therefore, exploring single domain generalization methods that extract domain-invariant features using only a single source domain better matches the needs of cross-institutional deployment.

**中文 v2：**

3.事实上，前述跨机构数据共享与多源协同训练受限的关键原因之一，正是医疗图像数据本身的隐私敏感性。医疗数据比起自然图像更加敏感，存在更高的隐私泄露风险。常见的攻击方法可以通过模型的训练梯度逆向恢复出患者的数据 \hyperref[_Ref213949393]{{[}13{]}}。针对此问题，目前已有联邦学习、同态加密、安全多方计算和差分隐私等隐私保护方法研究，但是隐私保护与模型性能之间通常存在 trade-off 关系；尤其在 DA 场景中，源域和目标域数据需要同时参与训练，可能带来隐私机制添加复杂、多域性能衰减明显等问题。因此，更合理的做法是在不引入跨机构数据共享的前提下，于单一源域的本地训练流程中探索隐私保护与模型性能之间的平衡方法。

**对应英文：**

3. In fact, one of the key reasons behind the aforementioned restrictions on cross-institutional data sharing and multi-source collaborative training is precisely the privacy sensitivity of medical image data itself. Medical data are more sensitive than natural images and therefore involve higher privacy leakage risk. Common attack methods can recover patient data from model training gradients \hyperref[_Ref213949393]{{[}13{]}}. To address this issue, privacy-preserving methods such as federated learning, homomorphic encryption, secure multi-party computation, and differential privacy have been investigated. However, privacy preservation usually comes with a privacy-performance trade-off. In DA scenarios in particular, source-domain and target-domain data must participate in training simultaneously, which can complicate the integration of privacy mechanisms and cause more severe performance degradation across domains. Therefore, a more reasonable approach is to explore the balance between privacy preservation and model performance within the local training process of a single source domain, without introducing cross-institutional data sharing.

**中文 v2：**

为应对上述三个关键挑战，我们构建了一个面向多标签眼科疾病识别的可解释与隐私保护单域泛化框架。针对眼科疾病识别中普遍存在的多疾病共存问题，我们引入基于 Transformer 的自适应标签-特征关联性构建模块，通过自注意力机制建模标签关联，并利用交叉注意力机制将标签语义与对应的图像特征进行融合，在标签层面与特征层面同时构建疾病共现依赖，从而减少多标签识别中的误检与漏检；针对多机构数据访问受限与跨机构部署域偏移并存的问题，我们提出双分支引导域不变特征提取模块，仅利用单一源域数据进行训练，通过对源域原始图像及其风格扰动后的源域增强图像构建双分支结构（如\figsubref{fig:intro-domain-gap}{a1}和\figsubref{fig:intro-domain-gap}{a2}所示），在特征层面挖掘两者的共性表示。同时，引入类别激活映射（Class Activation Mapping, CAM）作为先验引导，促使模型聚焦于疾病相关区域，从而抑制域特定噪声的学习，使得模型能够形成更适用于未知域分布的决策边界（\figsubref{fig:intro-domain-gap}{c1}），并在未知域上保持稳定的识别性能（\figsubref{fig:intro-domain-gap}{c2}）。此外，CAM 还能够可视化模型关注区域，增强模型的可解释性；针对跨机构数据共享受限下进一步突出的隐私保护需求，本文在单域泛化训练过程中集成自适应高斯差分隐私机制，通过在梯度更新阶段注入噪声实现隐私保护。在中等隐私预算下，该机制能够在可控的性能代价下提供有效的隐私保护，所得隐私模型的性能仍可达到与公开官方基线相当甚至略优的水平，实现跨域泛化能力与隐私保护的兼顾。

**对应英文：**

To address the above three key challenges, we build a privacy-preserving interpretable single domain generalization framework for multi-label ocular disease recognition. For the common issue of multi-disease co-occurrence in ocular disease recognition, we introduce a Transformer-based Adaptive Label-Feature Relevance Construction (ARC) module. It models label relevance using Transformer self-attention and fuses label semantics with corresponding image features using Transformer cross-attention, thereby constructing disease co-occurrence dependencies at both the label and feature levels to reduce false positives and false negatives in multi-label recognition. To handle restricted multi-institutional data access together with cross-institutional domain shift, we propose a Dual-Branch Guided Domain-Invariant Feature Extraction (DFE) module. This module is trained using only a single source domain and constructs a dual-branch structure from original source-domain images and style-disturbed augmented source-domain images, as shown in \hyperref[fig:intro-domain-gap]{Fig.~\ref*{fig:intro-domain-gap}.a1} and \hyperref[fig:intro-domain-gap]{Fig.~\ref*{fig:intro-domain-gap}.a2}, to learn their shared representations at the feature level. Meanwhile, Class Activation Mapping (CAM) is introduced as prior guidance to encourage the model to focus on disease-related regions and suppress the learning of domain-specific noise. This enables the model to form a decision boundary that is more suitable for unseen-domain distributions (\hyperref[fig:intro-domain-gap]{Fig.~\ref*{fig:intro-domain-gap}.c1}) and to maintain stable recognition performance on unseen domains (\hyperref[fig:intro-domain-gap]{Fig.~\ref*{fig:intro-domain-gap}.c2}). In addition, CAM visualizes model-attended regions and enhances model interpretability. To address the privacy-preservation demand that becomes more prominent when cross-institutional data sharing is restricted, we integrate an Adaptive Gaussian Differential Privacy (AdaGDP) mechanism into the single domain generalization training process and provide privacy preservation by injecting noise during gradient updates. Under a moderate privacy budget, this mechanism provides effective privacy preservation at a controllable performance cost, and the resulting private model still attains performance comparable to or even slightly better than the public official baseline, thereby jointly supporting cross-domain generalization and privacy preservation.


## 02_related_work

**中文 v2：**

不同于单标签，多标签图像识别允许一幅图像同时对应多个非互斥类别，因此更需要处理标签共现、标签关联和类别不平衡等问题 \hyperref[_Ref213949872]{{[}14{]}}。早期方法如 Binary Relevance \hyperref[_Ref213949896]{{[}15{]}}通常将多标签任务简单拆分为多个独立二分类问题，该类方法容易忽略标签之间的相关关系，在复杂视觉场景中，往往会导致预测结果不完整或矛盾。

**对应英文：**

Unlike single-label recognition, multi-label image recognition allows one image to be assigned to multiple non-mutually exclusive categories, and therefore requires careful handling of label co-occurrence, label relevance, and class imbalance \hyperref[_Ref213949872]{{[}14{]}}. Early methods such as Binary Relevance \hyperref[_Ref213949896]{{[}15{]}} usually decompose a multi-label task into multiple independent binary classification problems. Such methods tend to ignore label relevance and may lead to incomplete or inconsistent predictions in complex visual scenarios.

**中文 v2：**

为缓解上述问题，近年来的多标签图像识别方法逐渐关注标签关联建模和样本不平衡处理。ML-GCN \hyperref[_Ref213949382]{{[}10{]}}根据标签共现统计构建标签图，并通过图卷积网络传播标签关联信息；Asymmetric Loss (ASL) \hyperref[_Ref213949927]{{[}16{]}}对正负样本引入不同的聚焦参数，并通过负样本概率移位机制抑制易分类负样本的损失贡献，从而缓解多标签识别中的正负样本不平衡问题；Query2Label \hyperref[_Ref213950246]{{[}17{]}}进一步利用 Transformer 查询机制建模标签交互，并在 VOC \hyperref[_Ref213950282]{{[}18{]}}等自然图像数据集上取得良好效果。这些工作表明，将标签关联显式或隐式地融入模型，有助于提升多标签预测的完整性和准确性。

**对应英文：**

To alleviate these problems, recent multi-label image recognition methods have increasingly focused on label relevance modeling and sample imbalance. ML-GCN \hyperref[_Ref213949382]{{[}10{]}} constructs a label graph from label co-occurrence statistics and propagates label relevance information through graph convolutional networks. Asymmetric Loss (ASL) \hyperref[_Ref213949927]{{[}16{]}} introduces different focusing parameters for positive and negative samples and suppresses the loss contribution of easy negative samples through negative probability shifting, thereby alleviating positive-negative sample imbalance in multi-label recognition. Query2Label \hyperref[_Ref213950246]{{[}17{]}} further uses a Transformer query mechanism to model label interactions and achieves strong performance on natural image datasets such as VOC \hyperref[_Ref213950282]{{[}18{]}}. These studies show that explicitly or implicitly incorporating label relevance into the model can improve the completeness and accuracy of multi-label prediction.

**中文 v2：**

在此背景下，单域泛化（Single Domain Generalization, SDG）作为更受限的泛化设置，仅使用一个源域学习面向未知域的域不变特征。医疗图像中的 single-source DG 研究 \hyperref[_Ref213949863]{{[}34{]}}也说明，在无法集中使用多机构数据时，从单一源域中挖掘更稳定的疾病相关特征具有现实价值。综上，常见跨域方法所预设的目标域可访问或多源域协同前提，在真实医疗场景中难以同时满足，因此，仅利用单一源域学习域不变特征，是更贴近跨机构多标签眼科疾病识别部署约束的研究方向。

**对应英文：**

Against this background, Single Domain Generalization (SDG) is a more constrained generalization setting that uses only one source domain to learn domain-invariant features for unseen domains. Studies on single-source DG in medical images \hyperref[_Ref213949863]{{[}34{]}} also indicate that mining more stable disease-related features from a single source domain has practical value when multi-institutional data cannot be centrally used. In summary, the assumptions of target-domain accessibility or multi-source collaboration presumed by common cross-domain methods are difficult to satisfy simultaneously in real-world medical scenarios. Therefore, learning domain-invariant features from a single source domain is well aligned with the deployment constraints of cross-institutional multi-label ocular disease recognition.

**中文 v2：**

除联邦学习外，为进一步防范隐私泄露，加密机制可以提供更强隐私保护。同态加密（Homomorphic Encryption, HE）允许在密文上执行计算 \hyperref[_Ref213950427]{{[}38{]}}，并已被探索用于医疗影像分析 \hyperref[_Ref213950433]{{[}39{]}}，但通常伴随较高计算开销；安全多方计算（Secure Multi-Party Computation, SMPC） \hyperref[_Ref213950438]{{[}40{]}}可在多方协作时保护各方输入隐私。差分隐私（Differential Privacy, DP）通过向查询结果或训练梯度中注入噪声，为单个样本的隐私泄露风险提供可量化约束 \hyperref[_Ref213950443]{{[}41{]}}。其中，高斯差分隐私 \hyperref[_Ref213950449]{{[}42{]}}通过对裁剪后的梯度注入高斯噪声，为连续梯度更新过程提供可量化的隐私保护，因此在深度学习梯度保护中具有较强适用性。

**对应英文：**

Beyond federated learning, encryption mechanisms can provide stronger privacy preservation against privacy leakage. Homomorphic Encryption (HE) allows computation over ciphertexts \hyperref[_Ref213950427]{{[}38{]}} and has been explored for medical image analysis \hyperref[_Ref213950433]{{[}39{]}}, but it usually incurs high computational overhead. Secure Multi-Party Computation (SMPC) \hyperref[_Ref213950438]{{[}40{]}} can protect the input privacy of each party during multi-party collaboration. Differential Privacy (DP) injects noise into query results or training gradients to provide quantifiable constraints on the privacy leakage risk of individual samples \hyperref[_Ref213950443]{{[}41{]}}. Among DP mechanisms, Gaussian differential privacy \hyperref[_Ref213950449]{{[}42{]}} injects Gaussian noise into clipped gradients and provides quantifiable privacy preservation for continuous gradient updates, making it well suited to gradient protection in deep learning.

**中文 v2：**

现有隐私保护机制可以降低隐私泄露风险，但在域泛化任务中仍面临额外挑战。联邦学习、同态加密和安全多方计算往往带来通信、计算或系统协同成本；差分隐私虽然部署形式相对直接，但噪声注入可能对模型精度造成影响，且这种影响在不同类别或不同数据分布上可能并不均衡 \hyperref[_Ref213950458]{{[}43{]}}，这一定程度上增加了多域泛化条件下的隐私保护难度。综上，医疗数据的隐私敏感性进一步限制了跨机构数据共享，使前述多源域协同的预设更难成立，因此，在单一源域的本地训练流程中探索更可控的隐私--性能平衡，对于隐私受限场景下的跨机构多标签眼科疾病识别更具实际意义。

**对应英文：**

Existing privacy-preserving mechanisms can reduce privacy leakage risk, but they still face additional challenges in domain generalization tasks. Federated learning, homomorphic encryption, and secure multi-party computation often introduce communication, computation, or system-level collaboration costs. Differential privacy is relatively straightforward to deploy, but noise injection may affect model accuracy, and this effect may vary across classes or data distributions \hyperref[_Ref213950458]{{[}43{]}}. These issues make privacy preservation more challenging under multi-domain generalization. In summary, the privacy sensitivity of medical data further restricts cross-institutional data sharing and makes the aforementioned multi-source collaboration assumption even harder to hold. Therefore, exploring a more controllable privacy-performance trade-off within the local training process of a single source domain is of greater practical significance for cross-institutional multi-label ocular disease recognition under privacy-restricted scenarios.


## 03_method

**中文 v2：**

在多标签眼科疾病识别的域泛化过程中，模型性能主要受到三方面因素影响。首先，同一眼底图像中可能同时存在多种疾病，若模型不能有效建模疾病标签之间以及标签与疾病特征之间的关联，容易产生误检与漏检，从而降低多标签识别性能。其次，源域与目标域之间通常存在分布差异，若模型学习到的特征中包含较多源域特定噪声，则会削弱疾病相关特征的迁移能力，导致域泛化性能下降。此外，医疗数据隐私敏感，训练过程中产生的梯度或参数可能带来隐私泄露风险，需要在训练流程中引入隐私保护机制；但隐私保护机制通常会通过额外的训练约束影响模型优化过程，因此需要考虑隐私保护与模型性能之间的平衡问题。

**对应英文：**

In domain generalization for multi-label ocular disease recognition, model performance is mainly affected by three factors. First, multiple diseases may coexist in the same fundus image. If the model cannot effectively capture relevance among disease labels and between labels and disease-related features, false positives and false negatives may occur, degrading multi-label recognition performance. Second, distribution shifts commonly arise between the source domain and target domain. If the learned features contain substantial source-domain-specific noise, the transferability of disease-related features is weakened, resulting in poorer domain generalization performance. In addition, medical data are privacy-sensitive, and the gradients or parameters produced during training may introduce privacy leakage risk, requiring a privacy-preserving mechanism to be incorporated into the training process. However, privacy-preserving mechanisms usually affect model optimization through additional training constraints, so the balance between privacy preservation and model performance must be considered.

**中文 v2：**

针对上述问题，本文不将多疾病共存和域偏移视为两个孤立问题，而是统一到多标签眼科疾病识别的单域泛化框架中进行建模。如\figref{fig:method-framework}所示，所提可解释单域泛化框架主要包括两个部分：Part1.双分支引导域不变特征提取，Part2.自适应标签-特征关联性构建。Part1 以 CAM 作为引导，结合双分支 mask 对比学习机制，从单一源域中提取更稳定的域不变特征，缓解源域与未知域之间的分布差异影响。同时 CAM 能够可视化模型关注区域，增强可解释性；Part2 在 Part1 输出的域不变特征基础上，利用 Transformer 注意力机制建模标签-标签关联与标签-特征关联性，减少多标签识别中的误检与漏检。两个部分并非独立工作，而是通过特征过滤和注意力一致性约束形成协同：Part1 为 Part2 提供更稳定的域不变特征，Part2 进一步约束双分支注意力特征的一致性，从而共同提升域泛化性能。最后，训练过程中集成自适应高斯差分隐私机制，以缓解隐私保护机制对模型性能的影响，并在隐私保护与模型性能之间取得平衡。综合以上，所提方法构建了一个面向多标签眼科疾病识别的可解释与隐私保护单域泛化框架。以下分三小节详细描述各模块的实现细节。

**对应英文：**

To address these issues, this study does not treat multi-disease co-occurrence and domain shift as separate problems. Instead, they are jointly modeled within a single domain generalization framework for multi-label ocular disease recognition. As shown in \hyperref[fig:method-framework]{Fig.~\ref*{fig:method-framework}}, the proposed interpretable single domain generalization framework consists of two main parts: Part 1, Dual-Branch Guided Domain-Invariant Feature Extraction (DFE), and Part 2, Adaptive Label-Feature Relevance Construction (ARC). Part 1 uses CAM guidance together with a dual-branch mask-based contrastive learning mechanism to extract more stable domain-invariant features from a single source domain, thereby reducing the influence of distribution shift between the source domain and unseen domains. CAM also visualizes model-attended regions and enhances interpretability. Based on the domain-invariant features produced by Part 1, Part 2 uses Transformer attention mechanisms to model label-label relevance and label-feature relevance, reducing false positives and false negatives in multi-label recognition. These two parts are coupled through feature filtering and attention consistency constraints: Part 1 provides more stable domain-invariant features for Part 2, while Part 2 further constrains the consistency of dual-branch attention features, jointly improving domain generalization performance. Finally, an Adaptive Gaussian Differential Privacy mechanism is integrated during training to reduce the impact of privacy preservation on model performance and to balance privacy preservation with model performance. Overall, the proposed method constructs a Privacy-Preserving Interpretable Single Domain Generalization framework for multi-label ocular disease recognition. The implementation details of each module are described in the following three subsections.

**中文 v2：**

考虑到医疗场景中多机构数据往往难以集中或同步使用，本文采用单域泛化设置，仅利用一个源域学习面向未知域数据的域不变特征。受对比学习启发，本文将源域原始图像通过风格扰动等增强技术生成源域增强图像，用于模拟未知域可能出现的分布差异。具体而言，\(I^{ori}\)代表源域原始图像，而\(I^{aug}\)代表源域增强图像，通过风格扰动（如 MixStyle 方法或随机调整亮度、对比度、饱和度）生成。这种增强模拟了跨域场景中的成像设备、光照环境或患者群体差异，但保留了图像的语义内容（疾病区域）。

**对应英文：**

Considering that multi-institutional data in medical scenarios are often difficult to centralize or use synchronously, this study adopts a single domain generalization setting and learns domain-invariant features for unseen-domain data using only one source domain. Inspired by contrastive learning, original source-domain images are transformed into augmented source-domain images through augmentation techniques such as style disturbance to simulate possible distribution shifts in unseen domains. Specifically, \(I^{ori}\) denotes original source-domain images, and \(I^{aug}\) denotes augmented source-domain images generated by style disturbance, such as MixStyle or random adjustment of brightness, contrast, and saturation. This augmentation simulates differences in imaging devices, illumination environments, or patient populations in cross-domain scenarios while preserving the semantic content of the images, namely disease regions.

**中文 v2：**

首先，如\figsubref{fig:method-framework}{a}部分所示，\(I^{ori}\)和\(I^{aug}\)二者共同送入骨干网络提取特征得到\(F^{ori}\)和\(F^{aug}\)。令\(F^{ori} \in \mathbb{R}^{C \times H \times W}\)和\(F^{aug} \in \mathbb{R}^{C \times H \times W}\)，其中\(C\)、\(H\)、\(W\)分别为骨干网络最终特征图的通道数、高度和宽度。本方法选择 ResNet50 \hyperref[_RefResNet2016]{{[}44{]}}作为骨干网络，因为其在图像识别任务中表现出色，具有较好的特征提取能力和计算效率。然而，仅依靠源域原始图像与源域增强图像之间的对比约束作用仍然有限，模型可能同时学习到背景纹理、光照变化或边缘伪影等域特定噪声，进而影响未知域上的多标签眼科疾病识别。

**对应英文：**

First, as shown in \hyperref[fig:method-framework]{Fig.~\ref*{fig:method-framework}.a}, both \(I^{ori}\) and \(I^{aug}\) are fed into the backbone network to extract features \(F^{ori}\) and \(F^{aug}\). Let \(F^{ori} \in \mathbb{R}^{C \times H \times W}\) and \(F^{aug} \in \mathbb{R}^{C \times H \times W}\), where \(C\), \(H\), and \(W\) denote the number of channels, height, and width of the final feature map of the backbone network, respectively. ResNet50 \hyperref[_RefResNet2016]{{[}44{]}} is selected as the backbone because it performs well in image recognition tasks and offers good feature extraction capability and computational efficiency. However, relying only on contrastive constraints between original and augmented source-domain images remains limited. The model may still learn domain-specific noise such as background textures, illumination variations, or image-edge artifacts, which can affect multi-label ocular disease recognition on unseen domains.

**中文 v2：**

其中\(A_{k}\)是骨干网络最后一层卷积的第\(k\)个通道激活图，\(\omega_{k}^{c}\)是第\(k\)个通道对目标类别\(c\)的重要性权重，由类别得分\(y^{c}\)对该通道激活图的梯度经全局平均池化得到：

\begin{equation}\label{eq:cam-weight}
\omega_{k}^{c} = \frac{1}{Z}\sum_i\sum_j \frac{\partial y^{c}}{\partial A_{ij}^{k}},
\end{equation}
其中\(Z\)表示特征图空间位置数。该公式基于 Grad-CAM 变体，生成的是类别特定的空间关注热图，而不是原始眼底图像。实际使用时，根据图像的阳性标签或预测类别生成一个或多个\(I^{cam,c}\)，并经过归一化和尺寸调整后作为 CAM 引导图\(I^{cam}\)。随后将\(I^{cam}\)输入骨干网络得到\(F^{cam} \in \mathbb{R}^{C \times H \times W}\)，然后通过空间/通道注意力模块分别计算\(F^{cam}\)的空间注意力权重\(s_{w}\)和通道注意力权重\(c_{w}\)。两个注意力模块均为卷积序列网络，均包含1x1 卷积、ReLU 激活和 Sigmoid 函数，用于自适应生成权重。空间注意力模块额外结合平均/最大池化捕捉局部上下文，从而生成像素级权重图，自适应放大病变区域（如血管或黄斑）的显著性，同时抑制背景噪声。通道注意力模块则采用自适应平均池化压缩空间维度以获取全局统计，随后学习通道依赖，从而增强疾病纹理敏感通道的权重，抑制噪声通道。分别将两权重加权应用到\(F^{ori}\)和\(F^{aug}\)得到 CAM 引导特征\(F_{guide}^{ori}\)和\(F_{guide}^{aug}\)，具体的加权方式采用残差连接机制，避免过度引导破坏原始信息。公式为：

**对应英文：**

Here, \(A_{k}\) is the activation map of the \(k\)-th channel in the last convolutional layer of the backbone network, and \(\omega_{k}^{c}\) is the importance weight of the \(k\)-th channel for target class \(c\). It is obtained by global average pooling the gradient of the class score \(y^{c}\) with respect to the channel activation map:

\begin{equation}\label{eq:cam-weight}
\omega_{k}^{c} = \frac{1}{Z}\sum_i\sum_j \frac{\partial y^{c}}{\partial A_{ij}^{k}},
\end{equation}

where \(Z\) denotes the number of spatial locations in the feature map. This Grad-CAM-based formula produces a class-specific spatial attention heatmap rather than a raw fundus image. In practice, one or more \(I^{cam,c}\) maps are generated according to the positive labels or predicted classes of an image, and they are normalized and resized to form the CAM guidance map \(I^{cam}\). The resulting \(I^{cam}\) is then fed into the backbone network to obtain \(F^{cam} \in \mathbb{R}^{C \times H \times W}\). Spatial attention weights \(s_{w}\) and channel attention weights \(c_{w}\) are then computed from \(F^{cam}\) through spatial and channel attention modules, respectively. Both attention modules are convolutional sequential networks containing \(1 \times 1\) convolution, ReLU activation, and a Sigmoid function for adaptive weight generation. The spatial attention module additionally combines average and max pooling to capture local context, generating a pixel-level weight map that adaptively enhances the saliency of lesion regions, such as vessels or the macula, while suppressing background noise. The channel attention module uses adaptive average pooling to compress spatial dimensions and obtain global statistics, then learns channel dependencies to enhance disease-texture-sensitive channels and suppress noisy channels. The two weights are applied to \(F^{ori}\) and \(F^{aug}\) to obtain CAM-guided features \(F_{guide}^{ori}\) and \(F_{guide}^{aug}\). A residual connection is used in the weighting operation to avoid damaging original information through excessive guidance:

**中文 v2：**

类似计算\(V_{cross}^{aug}\)。通过交叉注意力加权，标签与对应疾病特征进行匹配，形成注意力向量\(V \in \mathbb{R}^{8 \times d}\)，使每个标签向量在疾病相关区域上获得更高响应。在这一过程中，每个标签向量并不是独立地与图像特征进行匹配，而是在自注意力机制建模后的标签关联基础上进行查询。因此，模型既能关注单个疾病对应的局部病灶特征，也能利用疾病共现依赖辅助判断其他相关标签，从而减少多标签识别中的误检与漏检。

**对应英文：**

To ensure consistency between the outputs of the two branches, we introduce an attention consistency constraint and compute an attention consistency loss. Original source-domain images and augmented source-domain images share the same disease labels and differ only in style. Therefore, the corresponding label attention vectors should remain close. This loss encourages consistent attention features across the two branches, enabling the model to learn similar label-feature relevance from inputs with different styles. It is calculated using mean squared error (MSE):

**中文 v2：**

最终，注意力向量输入多标签分类器，首先对类别查询特征施加 LayerNorm 与 Dropout 进行轻量级特征增强，用于规范化和正则化查询特征，随后通过逐类别的线性变换获得每个类别的 logits，经 Sigmoid 激活后，得到各类别的预测概率\(p^{ori}\)，类似得到\(p^{aug}\)。分类损失采用二元交叉熵（BCE）：

**对应英文：**

Finally, the attention vectors are fed into the multi-label classifier. LayerNorm and Dropout are first applied to the class query features for lightweight feature enhancement, normalization, and regularization. Class-wise linear transformations are then used to obtain logits for each class. After Sigmoid activation, the prediction probabilities \(p^{ori}\) are obtained for each class, and \(p^{aug}\) is obtained in the same way. The classification loss uses binary cross entropy (BCE):

**中文 v2：**

高斯差分隐私（Gaussian Differential Privacy, GDP）通过在每步梯度更新时加入独立同分布的高斯噪声实现\((\epsilon, \delta)\)-差分隐私。对于相邻数据集\(D\)和\(D'\)（仅相差一个样本），若随机算法\(M\)对任意输出集合\(S\)满足：

**对应英文：**

Gaussian differential privacy (GDP) provides \((\epsilon, \delta)\)-differential privacy by adding independent and identically distributed Gaussian noise at each gradient update. For adjacent datasets \(D\) and \(D'\), which differ by only one sample, a randomized algorithm \(M\) satisfies \((\epsilon, \delta)\)-DP if, for any output set \(S\), it satisfies:


## 04_experiments

**中文 v2：**

\caption{ODIR 数据集中 8类眼底图像的示例样本，对应本文使用的 8个非互斥类别。其中(a)--(h)分别代表(a) 正常（N），(b) 糖尿病视网膜病变（D），(c) 青光眼（G），(d) 白内障（C），(e) 年龄相关性黄斑变性（A），(f) 高血压视网膜病变（H），(g) 病理性近视（M），(h) 其他异常（O）。}

**对应英文：**

Example fundus images of the eight classes in the ODIR dataset, corresponding to the eight non-mutually exclusive classes used in this study. (a)--(h) denote (a) normal (N), (b) Diabetic Retinopathy (D), (c) Glaucoma (G), (d) Cataract (C), (e) Age-related Macular Degeneration (A), (f) Hypertension (H), (g) Myopia (M), and (h) Others (O), respectively.

**中文 v2：**

\caption{RFMiD 数据集中选取的 8类眼底图像示例，其中(a)--(h)分别对应(a) 糖尿病视网膜病变（D），(b) 年龄相关性黄斑变性（A），(c) 近视（M），(d) 黄斑瘢痕（MS），(e) 视网膜炎（RS），(f) 中心性浆液性脉络膜视网膜病变（CSR），(g) 视网膜中央静脉阻塞（CRVO），(h) 视盘水肿（DE）。RFMiD 作为跨域泛化数据集使用，实验中与 ODIR 对齐后的共有标签空间为 D/A/M 三类，用于评估跨域泛化性能。}

**对应英文：**

Examples of eight selected fundus image classes in the RFMiD dataset. (a)--(h) correspond to (a) Diabetic Retinopathy (D), (b) Age-related Macular Degeneration (A), (c) Myopia (M), (d) Macular Scar (MS), (e) Retinitis (RS), (f) Central Serous retinopathy (CSR), (g) Central Retinal Vein Occlusion (CRVO), and (h) Disc Edema (DE), respectively. RFMiD is used as a cross-domain generalization dataset. In the experiments, the shared label space aligned with ODIR consists of D/A/M classes and is used to evaluate cross-domain generalization performance.

**中文 v2：**

\caption{EDID 数据集中选取的 8类眼底图像示例，其中(a)--(h)分别对应(a) 糖尿病视网膜病变（D），(b) 青光眼（G），(c) 近视（M），(d) 视网膜脱离（RD），(e) 视网膜色素变性（RP），(f) 视盘水肿（DE），(g) 黄斑瘢痕（MS），(h) 中心性浆液性脉络膜视网膜病变（CSR）。EDID 为单标签跨域泛化数据集，实验中与 ODIR 对齐后的共有标签空间为 D/G/M 三类，用于评估不同数据来源和标签组织方式下的泛化性能。}

**对应英文：**

Examples of eight selected fundus image classes in the EDID dataset. (a)--(h) correspond to (a) Diabetic Retinopathy (D), (b) Glaucoma (G), (c) Myopia (M), (d) Retinal Detachment (RD), (e) Retinitis Pigmentosa (RP), (f) Disc Edema (DE), (g) Macular Scar (MS), and (h) Central Serous retinopathy (CSR), respectively. EDID is used as a single-label cross-domain generalization dataset. In the experiments, the shared label space aligned with ODIR consists of D/G/M classes and is used to evaluate generalization performance under different data sources and label organizations.

**中文 v2：**

训练配置如下：优化器选择 Adam，初始学习率\(4 \times 10^{-7}\)，采用 OneCycleLR 调度策略（前10\%轮次从初始学习率线性升温至峰值\(1 \times 10^{-5}\)，有助于模型快速跳出局部最优，后90\%轮次退火，有助于收敛和找到更优解），训练 epoch 为50，batch size 为32，输入分辨率为448×448。所提方法在2张 RTX 4080 Super 上完成训练。后续实验结果表明，我们的改进基线模型（Off-site 双目 Final score 76.19）比起 ODIR 原文 ResNet50 实现（Off-site 双目 Final score 68.00）能达到更好的效果。

**对应英文：**

The training configuration is as follows. Adam is used as the optimizer, with an initial learning rate of \(4 \times 10^{-7}\). OneCycleLR is adopted as the scheduling strategy: the learning rate linearly warms up from the initial learning rate to the peak value of \(1 \times 10^{-5}\) during the first 10\% of epochs to help the model quickly escape local optima, and then anneals during the remaining 90\% of epochs to facilitate convergence and reach a better solution. The number of training epochs is 50, the batch size is 32, and the input resolution is \(448 \times 448\). The proposed method is trained on two RTX 4080 Super GPUs. Experimental results show that our improved baseline model, with an Off-site binocular Final score of 76.19, outperforms the ResNet50 implementation in the original ODIR paper, which reports an Off-site binocular Final score of 68.00.

**中文 v2：**

为评估所提方法在 ODIR 数据集上的识别性能，我们选取了四个公开发表的多标签眼科疾病识别方法进行对比，包括 ODIR 数据集论文提供的官方基线（Li et al. \hyperref[_Ref213949402]{{[}46{]}}）以及三项后续在该数据集上报告结果的工作（Gour and Khanna \hyperref[_Ref214903299]{{[}49{]}}、He et al. \hyperref[_Ref213950338]{{[}20{]}}、Ou et al. \hyperref[_Ref214903327]{{[}50{]}}）。这些方法主要聚焦于提升 Final score，未考虑跨域泛化或隐私保护。

**对应英文：**

To evaluate the recognition performance of the proposed method on the ODIR dataset, we compare it with four published multi-label ocular disease recognition methods, including the official baseline provided in the ODIR dataset paper by Li et al. \hyperref[_Ref213949402]{{[}46{]}} and three subsequent works reporting results on this dataset by Gour and Khanna \hyperref[_Ref214903299]{{[}49{]}}, He et al. \hyperref[_Ref213950338]{{[}20{]}}, and Ou et al. \hyperref[_Ref214903327]{{[}50{]}}. These methods mainly focus on improving Final score and do not consider cross-domain generalization or privacy preservation.

**中文 v2：**

Ou et al. \hyperref[_Ref214903327]{{[}50{]}}设计双流交互 CNN（BFENet），使用特征增强模块通过注意力机制捕捉双目局部-全局依赖，并通过多尺度模块叠加不同分辨率特征以丰富表示。其原理在于利用双流交互强化病变区域（如微血管瘤、出血点），提升多标签识别性能，但未考虑隐私或跨域场景。

**对应英文：**

Ou et al. \hyperref[_Ref214903327]{{[}50{]}} designed a two-stream interactive CNN (BFENet). A feature enhancement module captures local-global binocular dependencies through an attention mechanism, and a multi-scale module aggregates features at different resolutions to enrich representations. The method enhances lesion regions, such as microaneurysms and hemorrhages, through two-stream interaction to improve multi-label recognition performance, but it does not consider privacy or cross-domain scenarios.

**中文 v2：**

\caption{与现有方法在 ODIR 上的指标对比可视化，(a) Off-site test 与 (b) On-site test 分别对应\tabref{tab:sota-compare}中的两组双目指标。柱状图按 Kappa、F1、AUC 和 Final score 四项指标分组，各指标中红色数值标注最优结果、蓝色标注次优结果。所提方法（Ours）在两个测试集的 Kappa 与 Final score 上均取得最优。}

**对应英文：**

Visual comparison of metrics with existing methods on ODIR, where (a) Off-site test and (b) On-site test correspond to the two groups of binocular metrics in \hyperref[tab:sota-compare]{Table~\ref*{tab:sota-compare}}. The bars are grouped by the four metrics Kappa, F1, AUC, and Final score; within each metric, red values mark the best result and blue values mark the second-best. The proposed method (Ours) achieves the best Kappa and Final score on both test sets.

**中文 v2：**

为系统验证所提方法中两大核心模块，即双分支引导域不变特征提取（DFE）与自适应标签-特征关联性构建（ARC）的独立贡献及协同增益，同时考察 CAM 引导对模型可解释性的提升，我们在 ODIR Off-site 双目指标上进行了逐模块消融实验，结果如\tabref{tab:ablation}所示，并在\figref{fig:ablation-radar}中以雷达图直观对比各模型的指标分布。\tabref{tab:ablation}同时给出单目与双目两组指标，二者呈现一致的提升趋势；为与官方患者级评估标准对齐、并保持正文简洁，下文仅就双目指标展开分析。

**对应英文：**

To assess the independent contributions and synergistic gains of the two core modules in the proposed method, namely Dual-Branch Guided Domain-Invariant Feature Extraction (DFE) and Adaptive Label-Feature Relevance Construction (ARC), and to examine the improvement in model interpretability brought by CAM guidance, we conduct module-wise ablation experiments using ODIR Off-site metrics. The results are shown in \hyperref[tab:ablation]{Table~\ref*{tab:ablation}}, and \hyperref[fig:ablation-radar]{Fig.~\ref*{fig:ablation-radar}} provides an intuitive radar-chart comparison of the metric distributions across models. \hyperref[tab:ablation]{Table~\ref*{tab:ablation}} reports both monocular and binocular metrics, which show a consistent improvement trend; to align with the official patient-level evaluation standard and keep the main text concise, the following analysis focuses on the binocular metrics.

**中文 v2：**

\caption{消融实验中各模型在 ODIR Off-site 上的指标雷达图，分别给出 (a) 单目（Monocular）与 (b) 双目（Binocular）两种评估方式下的结果，二者均与\tabref{tab:ablation}一致。每个轴对应一项指标（Kappa、F1、AUC、Final），并按该轴取值范围独立归一化以放大模型间差异，多边形越向外表示指标越高。所提方法（Ours）在各项指标上整体外扩，优于仅引入 DFE 或 ARC 的变体及基线。}

**对应英文：**

Radar charts of the metrics of each model on ODIR Off-site in the ablation study, showing the results under (a) monocular and (b) binocular evaluation protocols, both consistent with \hyperref[tab:ablation]{Table~\ref*{tab:ablation}}. Each axis corresponds to one metric (Kappa, F1, AUC, Final) and is independently normalized according to the value range of that axis to amplify differences among models; the further the polygon extends outward, the higher the metric. The proposed method (Ours) expands outward on all metrics overall, outperforming the variants that introduce only DFE or only ARC as well as the baseline.

**中文 v2：**

ResNet50+ARC：仅引入自适应标签-特征关联性构建模块，Final score 提升至76.98（+0.79），Kappa 提升0.44，AUC 提升2.29。该模块通过显式建模疾病共现依赖（如 DR 与 AMD、近视与视盘异常）降低了漏检率，多标签识别性能提高。

**对应英文：**

ResNet50+ARC: only the Adaptive Label-Feature Relevance Construction module is introduced. The Final score increases to 76.98 (+0.79), Kappa increases by 0.44, and AUC increases by 2.29. By explicitly modeling disease co-occurrence dependencies, such as DR and AMD or Myopia and optic-disc abnormalities, this module reduces the false-negative rate and improves multi-label recognition performance.

**中文 v2：**

ResNet50+DFE+ARC（所提方法，ours）：同时启用两大模块协同后，Final score 进一步升至78.85（较基线+2.66），Kappa 达到57.05（+4.30），F1 与 AUC 分别达到89.03（+1.20）和90.48（+2.48）。总增益与两模块独立增益之和接近（2.66 ≈ 2.18+0.79=2.97），说明两模块功能互补、组合时无明显冲突：DFE 为 ARC 提供更稳定的域不变特征，使 Transformer 能更精准地学习标签-标签关联性与标签-特征关联性；ARC 的注意力一致性损失反过来进一步约束双分支输出分布，提升特征表示的稳定性。进一步从\figref{fig:cam-visualization}的可视化结果可以看出，相比 baseline，所提方法得到的 CAM，其模型关注区域对图像边缘、光照伪影的响应减少，更收敛到眼球、血管等疾病相关区域，模型可解释性增强。

**对应英文：**

ResNet50+DFE+ARC (the proposed method, ours): when both modules are enabled, the Final score further increases to 78.85 (+2.66 over the baseline), Kappa reaches 57.05 (+4.30), and F1 and AUC reach 89.03 (+1.20) and 90.48 (+2.48), respectively. The total gain is close to the sum of the individual gains of the two modules (\(2.66 \approx 2.18 + 0.79 = 2.97\)), indicating that the two modules are functionally complementary and exhibit no obvious conflict when combined. DFE provides more stable domain-invariant features for ARC, enabling Transformer to learn label-label relevance and label-feature relevance more accurately. Conversely, the attention consistency loss of ARC further constrains the output distributions of the two branches and improves feature stability. In addition, the visualization results in \hyperref[fig:cam-visualization]{Fig.~\ref*{fig:cam-visualization}} show that, compared with the baseline, the CAMs obtained by the proposed method respond less to image edges and illumination artifacts, and the model-attended regions concentrate more on the eyeball, vessels, and other disease-related regions, indicating enhanced model interpretability.

**中文 v2：**

\caption{基线方法与所提方法在 ODIR Off-site 部分样本上的 CAM 模型关注区域可视化对比，其中(a)--(j) 为不同测试样本。相比基线模型，所提方法的模型关注区域更集中于眼球、血管和疾病相关区域，对图像边缘、光照伪影等无关背景的响应更弱，说明所提方法能够有效抑制域特定噪声并增强可解释性。}

**对应英文：**

Comparison of CAM-based model-attended region visualizations between the baseline and the proposed method on selected ODIR Off-site samples, where (a)--(j) denote different test samples. Compared with the baseline, the model-attended regions of the proposed method are more concentrated on the eyeball, vessels, and disease-related regions, with weaker responses to irrelevant background factors such as image edges and illumination artifacts. This indicates that the proposed method effectively suppresses domain-specific noise and enhances interpretability.

**中文 v2：**

为全面验证所提方法在单一源域训练条件下的泛化能力以及隐私保护机制的有效性，我们按照"域内泛化 \(\rightarrow\) 跨域泛化 \(\rightarrow\) 隐私保护"的递进逻辑组织评估：首先在 ODIR 域内（Off-site 与 On-site）验证多标签识别性能，再在 RFMiD 与 EDID 两个未知域上考察跨域泛化能力，最后评估引入隐私保护机制后的性能保留情况。其中前两步在非隐私保护条件下完成，第三步在隐私保护条件下完成。

**对应英文：**

To comprehensively validate the generalization capability of the proposed method under single-source-domain training and the effectiveness of the privacy-preserving mechanism, we organize the evaluation following the progressive logic of "in-domain generalization \(\rightarrow\) cross-domain generalization \(\rightarrow\) privacy preservation": we first validate multi-label recognition performance within the ODIR domain (Off-site and On-site), then examine cross-domain generalization capability on the two unseen domains RFMiD and EDID, and finally evaluate the performance retention after introducing the privacy-preserving mechanism. The first two steps are completed under the non-private setting, while the third step is completed under the privacy-preserving setting.

**中文 v2：**

1. 非隐私保护条件下的泛化性能 结果如\tabref{tab:generalization}所示，表中报告了基线模型与所提方法在不同测试集上的 Final score。泛化实验按三个评估方向组织：ODIR 域内的 Off-site \(\rightarrow\) On-site、ODIR 到 RFMiD 的跨域泛化，以及 ODIR 到 EDID 的跨域泛化。每个方向均基于训练过程中保存的前5个候选检查点进行模型选择与评估，即分别在基线模型和所提方法的候选检查点中确定测试集表现最优的一组检查点，并同步报告该组检查点在源域 Off-site 和目标域上的结果。

**对应英文：**

1. Generalization performance under the non-private setting. The results are shown in \hyperref[tab:generalization]{Table~\ref*{tab:generalization}}, which reports the Final scores of the baseline and the proposed method on different test sets. The generalization experiments are organized along three evaluation directions: ODIR in-domain Off-site \(\rightarrow\) On-site, cross-domain generalization from ODIR to RFMiD, and cross-domain generalization from ODIR to EDID. For each direction, model selection and evaluation are based on the top five candidate checkpoints saved during training. Specifically, the checkpoint group with the best test-set performance is selected from the candidate checkpoints of the baseline and the proposed method, respectively, and the results of this checkpoint group on the source-domain Off-site set and the target domain are reported simultaneously.

**中文 v2：**

结果显示，在 RFMiD D/A/M 跨域泛化中，基线模型对应检查点的 ODIR Off-site 的 Final score 为94.39，目标域的 Final score 为83.86；所提方法对应检查点的 ODIR Off-site 的 Final score 为95.94，目标域 Final score 为85.06，分别提升1.55和1.20个百分点。进一步从细分指标看，所提方法在 RFMiD 上的 Kappa、F1 和 AUC 分别为73.95、87.96和93.27，均高于基线模型的72.08、87.11和92.39。在 EDID D/G/M 跨域泛化中，基线模型对应检查点的 ODIR Off-site 的 Final score 为94.30，目标域 Final score 为52.16；所提方法对应检查点的 ODIR Off-site 的 Final score 为96.03，目标域 Final score 为55.35，分别提升1.73和3.19个百分点。所提方法在 EDID 上的 Kappa、F1 和 AUC 分别为27.20、67.22和71.63，较基线模型的23.83、65.54和67.09均有提升。综合来看，RFMiD 结果验证了模型在多标签数据集上的跨域泛化能力；EDID 结果进一步说明，在单标签数据集被纳入三类泛化评估框架的情况下，所提方法仍能保持有效提升。\figref{fig:tsne}进一步以 t-SNE 对三个泛化方向下的特征分布进行可视化，相比 baseline，所提方法在多数方向上同类样本更紧凑、源域与目标域同类样本更靠近，与上述指标提升基本一致。

**对应英文：**

In RFMiD D/A/M cross-domain generalization, the baseline checkpoint obtains a Final score of 94.39 on ODIR Off-site and 83.86 on the target domain. The corresponding checkpoint of the proposed method obtains a Final score of 95.94 on ODIR Off-site and 85.06 on the target domain, improving by 1.55 and 1.20 percentage points, respectively. Detailed metrics show that the Kappa, F1, and AUC of the proposed method on RFMiD are 73.95, 87.96, and 93.27, all higher than the baseline values of 72.08, 87.11, and 92.39. In EDID D/G/M cross-domain generalization, the baseline checkpoint obtains a Final score of 94.30 on ODIR Off-site and 52.16 on the target domain. The proposed method obtains 96.03 on ODIR Off-site and 55.35 on the target domain, improving by 1.73 and 3.19 percentage points, respectively. The Kappa, F1, and AUC of the proposed method on EDID are 27.20, 67.22, and 71.63, which are higher than the baseline values of 23.83, 65.54, and 67.09. Overall, the RFMiD results validate the cross-domain generalization capability of the model on a multi-label dataset, while the EDID results further indicate that the proposed method remains effective when a single-label dataset is incorporated into a three-class generalization evaluation framework. \hyperref[fig:tsne]{Fig.~\ref*{fig:tsne}} further visualizes the feature distributions of the three generalization directions using t-SNE. Compared with the baseline, the proposed method makes samples of the same class more compact and brings same-class samples of the source and target domains closer in most directions, which is largely consistent with the metric improvements above.

**中文 v2：**

\caption{ODIR Off-site \(\rightarrow\) On-site（域内泛化，8 类 / in-domain generalization, 8 classes）}

**对应英文：**

ODIR Off-site \(\rightarrow\) On-site (in-domain generalization, 8 classes)

**中文 v2：**

\caption{ODIR Off-site \(\rightarrow\) RFMiD（D/A/M 三类对齐 / D/A/M three-class alignment）}

**对应英文：**

ODIR Off-site \(\rightarrow\) RFMiD (D/A/M three-class alignment)

**中文 v2：**

\caption{ODIR Off-site \(\rightarrow\) EDID（D/G/M 三类对齐 / D/G/M three-class alignment）}

**对应英文：**

ODIR Off-site \(\rightarrow\) EDID (D/G/M three-class alignment)

**中文 v2：**

\caption{三个评估方向下目标域样本特征的 t-SNE 可视化，(a)--(c) 分别对应 ODIR 域内（Off-site \(\rightarrow\) On-site）、ODIR \(\rightarrow\) RFMiD 与 ODIR \(\rightarrow\) EDID 三个泛化方向。每个子图内部左侧为 baseline、右侧为所提方法（Ours），不同颜色代表不同类别，圆点为源域样本、三角为目标域样本。(a) 域内 Off-site 与 On-site 同源、域差异本身较小，两种方法的同类样本均合理重叠，Ours 在小样本疾病类（G、A、M）上呈现更清晰的局部簇结构。(b) 在 RFMiD 泛化设置下，Ours 将 D/A/M 三类组织为更独立的簇，且每个簇内源域与目标域同类样本紧密混合，而 baseline D 类内部存在多个分离子簇，三类局部聚集相对松散。(c) 在 EDID 泛化设置下，baseline 虽形成多个局部簇，但某些同一疾病类的源域与目标域样本各自聚成相邻但分离的子簇（如 D 类和 G 类存在明显的两域边界）；Ours 簇数虽有所减少，但其将同类的两域样本更加混合，大致形成 D/G/M 三个按类别（而非按域）组织的区域。最终结果证明，所提方法有更强的域泛化能力。}

**对应英文：**

t-SNE visualization of target-domain sample features under three evaluation directions, where (a)--(c) correspond to ODIR in-domain (Off-site \(\rightarrow\) On-site), ODIR \(\rightarrow\) RFMiD, and ODIR \(\rightarrow\) EDID, respectively. In each subfigure, the left side is the baseline and the right side is the proposed method (Ours); different colors denote different classes, dots denote source-domain samples, and triangles denote target-domain samples. (a) In-domain Off-site and On-site share the same source and the domain gap itself is small, so same-class samples of both methods overlap reasonably, and Ours shows clearer local cluster structures on the small-sample disease classes (G, A, M). (b) Under the RFMiD generalization setting, Ours organizes the D/A/M classes into more independent clusters, with source- and target-domain samples of the same class closely mixed within each cluster, whereas the baseline has multiple separated sub-clusters within class D and looser local aggregation of the three classes. (c) Under the EDID generalization setting, the baseline also forms several local clusters, but for some classes the source- and target-domain samples of the same disease aggregate into adjacent but separated sub-clusters (for example, classes D and G show a clear two-domain boundary); Ours yields fewer clusters but mixes the two-domain samples of the same class more thoroughly, roughly forming three regions organized by class (D/G/M) rather than by domain. These results demonstrate that the proposed method has stronger domain generalization capability.

**中文 v2：**

2. 自适应高斯差分隐私超参数扫描 结果如\tabref{tab:privacy-scan}所示。引入隐私保护后，噪声注入速率会一定程度影响模型收敛行为与最终性能。实验发现，噪声乘数（noise\_multiplier）与噪声衰减速率（noise\_decay\_rate）共同决定了每轮噪声注入速率，并进一步影响每轮隐私预算消耗：过强的初始噪声会导致训练剧烈震荡甚至不收敛，而过快的衰减则使隐私预算在模型尚未充分学习时提前耗尽。其中，setting1（noise\_multiplier=0.65）提供了极强的隐私保护，但因初始噪声过大，导致\(\epsilon\)值仅为5.01，使模型性能严重下降；setting8（noise\_multiplier=0.25，decay\_rate=4e-6）虽然使得模型性能接近非隐私保护条件，但是\(\epsilon \approx 20\)隐私保护弱。综合性能与隐私预算，我们最终选取 setting5（noise\_multiplier=0.35，decay\_rate=4e-6），在80 epoch 后\(\epsilon \approx 10.15\)，实现了较优的隐私-性能平衡。

**对应英文：**

2. Hyperparameter scan of Adaptive Gaussian Differential Privacy. The results are shown in \hyperref[tab:privacy-scan]{Table~\ref*{tab:privacy-scan}}. After introducing privacy preservation, the noise injection rate affects model convergence behavior and final performance. The experiments show that the noise multiplier and noise decay rate jointly determine the per-epoch noise injection rate and further affect privacy budget consumption in each epoch. Excessive initial noise causes severe training oscillation or even non-convergence, whereas overly fast decay exhausts the privacy budget before the model has learned sufficiently. Setting 1 (noise\_multiplier=0.65) provides very strong privacy preservation, but the excessive initial noise yields \(\epsilon=5.01\) and severely degrades model performance. Setting 8 (noise\_multiplier=0.25, noise\_decay\_rate=4e\mbox{-}6) brings model performance close to the non-private setting, but \(\epsilon \approx 20\) indicates weak privacy preservation. Considering both performance and privacy budget, we finally select Setting 5 (noise\_multiplier=0.35, noise\_decay\_rate=4e\mbox{-}6), which reaches \(\epsilon \approx 10.15\) after 80 epochs and achieves a better privacy-performance trade-off.

**中文 v2：**

3. 隐私训练过程中的\(\epsilon\)-性能演化与优化策略 结果如\tabref{tab:privacy-evolution}所示，并在\figref{fig:privacy-tradeoff}中以隐私-性能权衡曲线直观呈现。采用 setting5 的噪声速率后，我们记录了训练过程中\(\epsilon\)消耗与单目指标的逐 epoch 变化。结果显示，随着\(\epsilon\)从第0轮的0.94逐步增长至第79轮的10.15，隐私逐步消耗，模型性能持续提升，至第74轮附近达到峰值（Final=73.15）。这表明自适应衰减策略允许模型在隐私预算内充分学习。第74轮的检查点是兼具隐私保护和性能的最佳平衡点。经过大量实验验证，隐私保护条件下需对优化策略进行针对性调整：

**对应英文：**

3. \(\epsilon\)-performance evolution and optimization strategy during privacy-preserving training. The results are shown in \hyperref[tab:privacy-evolution]{Table~\ref*{tab:privacy-evolution}} and are intuitively presented as a privacy-performance trade-off curve in \hyperref[fig:privacy-tradeoff]{Fig.~\ref*{fig:privacy-tradeoff}}. After adopting the noise rate of Setting 5, we record epoch-by-epoch changes in \(\epsilon\) consumption and monocular metrics during training. As \(\epsilon\) increases from 0.94 at epoch 0 to 10.15 at epoch 79, the privacy budget is progressively spent and model performance improves, reaching a peak around epoch 74 (Final=73.15). This indicates that the adaptive decay strategy allows the model to learn sufficiently within the privacy budget. The checkpoint at epoch 74 provides the best balance between privacy preservation and performance. Extensive experiments show that the optimization strategy needs to be adjusted for privacy-preserving scenarios:

**中文 v2：**

\caption{隐私训练过程中的隐私-性能（\(\epsilon\)-Final score）权衡曲线，数据对应\tabref{tab:privacy-evolution}。横轴为累积隐私预算\(\epsilon\)（越靠左隐私保护越强），纵轴为单目 Final score，每个点对应一个 epoch 检查点并按训练轮次着色，轨迹展示了随训练推进的隐私-性能演化。第74轮（e74）为 Pareto 拐点，即在\(\epsilon \approx 9.76\)处取得最优 Final score（73.15），是兼顾隐私与性能的最佳工作点。}

**对应英文：**

Privacy-performance (\(\epsilon\)-Final score) trade-off curve during privacy-preserving training, with data corresponding to \hyperref[tab:privacy-evolution]{Table~\ref*{tab:privacy-evolution}}. The horizontal axis is the cumulative privacy budget \(\epsilon\) (stronger privacy preservation toward the left), and the vertical axis is the monocular Final score. Each point corresponds to an epoch checkpoint and is colored by training epoch; the trajectory shows the privacy-performance evolution as training proceeds. Epoch 74 (e74) is the Pareto knee point, achieving the best Final score (73.15) at \(\epsilon \approx 9.76\), and is the best operating point that balances privacy and performance.

**中文 v2：**

（1）学习率从\(1 \times 10^{-5}\)提升至\(7.5 \times 10^{-5}\)。

**对应英文：**

(1) The learning rate is increased from \(1 \times 10^{-5}\) to \(7.5 \times 10^{-5}\).

**中文 v2：**

（2）学习率调度改为``先线性衰减后恒定''： 以 lr\_decay\_ratio 和 lr\_final\_factor 控制衰减轮次和衰减比例，所取值分别为0.75和0.8，即学习率在前75\%轮次内线性衰减至原值的80\%，之后保持恒定训练。

**对应英文：**

(2) The learning-rate schedule is changed to linear decay followed by constant training. The learning rate decay ratio and final learning rate factor control the decay epochs and decay ratio, and are set to 0.75 and 0.8, respectively. That is, the learning rate linearly decays to 80\% of its original value during the first 75\% of epochs and then remains constant.

**中文 v2：**

原因在于，隐私保护条件下的模型训练和非隐私保护条件下的模型训练不一样。对于学习率的取值来说，隐私保护条件下，每一次回传的梯度中都会叠加噪声，这使得每一次模型优化时的损失值在原基础上波动，增大了陷入局部最优的概率，因此学习率需要适当增大。对于学习率调度策略，在非隐私保护条件下当模型收敛到最优值附近时，学习速率通常会逐步减小；相比之下，隐私保护条件下的学习过程不需要将学习率降低到一个非常小的值，因为差分隐私训练会以隐私消耗不断增大的代价持续优化，却未必真正达到模型收敛。因此，以相对较大的学习率开始，然后在一定周期内线性衰减到较小的值，并在之后保持恒定，性能会更好。

**对应英文：**

This adjustment is motivated by the differences between privacy-preserving training and non-private training. For the learning rate, noise is added to each backpropagated gradient under privacy-preserving training, causing the loss at each optimization step to fluctuate and increasing the risk of poor local optima. A moderately larger learning rate is therefore needed. For the learning-rate schedule, non-private training usually decreases the learning rate as the model approaches an optimum. In contrast, privacy-preserving training does not need to reduce the learning rate to a very small value, because differential privacy training continues optimization while privacy loss accumulates, but may not fully converge. Starting with a relatively large learning rate, linearly decaying it to a smaller value over a certain period, and then keeping it constant therefore yields better performance.

**中文 v2：**

4. 隐私保护下的最终泛化性能 结果如\tabref{tab:privacy-final}所示。由于现有多标签眼科疾病识别泛化工作鲜有同时报告隐私训练下的指标，本文以 Li et al. \hyperref[_Ref213949402]{{[}46{]}} 提供的 ODIR 官方 ResNet50 基线作为公开参考点，用于评估隐私训练能否保持与公开基准相当的性能水平。最优隐私模型在 ODIR 域内双目指标上的 Off-site 和 On-site Final score 分别为68.96和68.42，相较本文非隐私保护版本下降约10个百分点；与官方基线相比，所提方法的 Off-site 略优（68.96 vs. 68.00），On-site 略低（68.42 vs. 68.80），整体保持在公开基准附近，说明在中等隐私预算下，自适应高斯差分隐私机制能够在提供有效隐私保护的同时使性能维持在可接受范围内。

**对应英文：**

4. Final generalization performance under privacy preservation. The results are shown in \hyperref[tab:privacy-final]{Table~\ref*{tab:privacy-final}}. Since existing generalization studies on multi-label ocular disease recognition rarely report metrics under privacy-preserving training, this study uses the official ODIR ResNet50 baseline provided by Li et al. \hyperref[_Ref213949402]{{[}46{]}} as a public reference point to assess whether privacy-preserving training can maintain performance comparable to a public benchmark. The optimal privacy checkpoint achieves Off-site and On-site Final scores of 68.96 and 68.42 on ODIR in-domain binocular metrics, respectively, about 10 percentage points lower than our non-private version. Compared with the official baseline, the proposed method is slightly better on Off-site (68.96 vs. 68.00) and slightly lower on On-site (68.42 vs. 68.80), remaining around the public benchmark overall. This indicates that, under a moderate privacy budget, the Adaptive Gaussian Differential Privacy mechanism can provide effective privacy preservation while keeping performance within an acceptable range.


## 05_conclusion

**中文 v2：**

本文提出了一种面向多标签眼科疾病识别的可解释与隐私保护单域泛化框架，针对临床多疾病共存、跨机构域偏移以及隐私敏感性进一步限制多源协同等递进挑战，构建了一种统一解决框架。核心贡献包括：（1）自适应标签-特征关联性构建模块（ARC），利用Transformer自注意力机制和交叉注意力机制捕捉标签-标签关联性与标签-特征关联性，并通过注意力一致性损失对齐双分支输出，有助于减少多标签识别中的误检与漏检；（2）双分支引导域不变特征提取模块（DFE），通过风格增强模拟潜在域偏移、CAM提供疾病区域先验引导，并结合空间/通道注意力与双分支 mask 对比学习机制提取域不变特征，在提升未知域泛化性能的同时增强模型可解释性；（3）自适应高斯差分隐私机制（AdaGDP），通过动态衰减噪声强度，在中等隐私预算（\(\epsilon \approx 10\)）下实现隐私保护与模型性能的平衡。系统性的实验验证了所提方法的有效性。尽管取得一定进展，本框架仍存在局限：类别不平衡可能影响少数类疾病识别的稳定性，未来可结合重采样或损失加权进一步缓解；当前跨域泛化主要基于共有标签空间展开，未来可探索开放类别和更复杂分布外场景下的泛化能力；此外，隐私保护方面，未来可探索更紧隐私预算下的性能保留方法，或与联邦学习等机制结合，以适配更复杂的跨机构部署场景。

**对应英文：**

We propose a Privacy-Preserving Interpretable Single Domain Generalization framework for multi-label ocular disease recognition. The framework provides a unified solution to a set of progressive challenges: clinical multi-disease co-occurrence, cross-institutional domain shift, and the privacy sensitivity that further restricts multi-source collaboration. The core contributions are as follows: (1) the Adaptive Label-Feature Relevance Construction (ARC) module uses Transformer self-attention and cross-attention mechanisms to capture label-label relevance and label-feature relevance, and aligns dual-branch outputs through attention consistency loss, helping reduce false positives and false negatives in multi-label recognition; (2) the Dual-Branch Guided Domain-Invariant Feature Extraction (DFE) module simulates potential domain shift through style augmentation, uses CAM to provide disease-region prior guidance, and combines spatial/channel attention with a dual-branch mask-based contrastive learning mechanism to extract domain-invariant features, improving unseen-domain generalization performance while enhancing model interpretability; and (3) the Adaptive Gaussian Differential Privacy (AdaGDP) mechanism dynamically decays noise intensity to achieve a balance between privacy preservation and model performance under a moderate privacy budget (\(\epsilon \approx 10\)). Systematic experiments validate the effectiveness of the proposed method. Despite these advances, the framework still has limitations. Class imbalance may affect the stability of recognition for minority disease classes, which could be further alleviated by resampling or loss weighting in future work. In addition, current cross-domain generalization is mainly based on shared label spaces, and future work can explore generalization under open-category and more complex out-of-distribution scenarios. Furthermore, in terms of privacy preservation, future work can explore methods that retain performance under tighter privacy budgets, or combine the proposed mechanism with federated learning and similar techniques to adapt to more complex cross-institutional deployment scenarios.


## table:table6_ablation

**中文 v2：**

\caption{消融实验结果。表中报告了在 ODIR Off-site test 集下的单目（Monocular）与双目（Binocular）指标。结果显示，DFE 和 ARC 相比 ResNet50（baseline）在双目 Final score 上均带来性能提升，分别提升 2.18 和 0.79；二者协同后进一步取得更高的指标提升，总体提升 2.66，并在双目四项指标上达到最佳结果，说明两模块功能互补、组合时无明显冲突。单目指标呈现一致的提升趋势。}

**对应英文：**

Ablation study results. The table reports monocular and binocular metrics on the ODIR Off-site test set. Compared with ResNet50 (baseline), DFE and ARC both improve the binocular Final score, by 2.18 and 0.79, respectively. Combining the two modules yields a larger gain of 2.66 overall and achieves the best results on all four binocular metrics, indicating that the two modules are functionally complementary and exhibit no obvious conflict when combined. The monocular metrics show a consistent improvement trend.
