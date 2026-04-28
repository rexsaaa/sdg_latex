# 术语英文译法清单

TAG：Step 2 推荐英文译法清单已完成。

用途：从 `docs/terminology_glossary.md` 提取中文稿中的固定表达，后续在“推荐英文译法”列补充英文主译法。

标记说明：

- 【通用术语】：相关文献中已有较稳定、可直接采用的表达。
- 【推荐译法】：未找到严格固定术语，但根据领域写法给出的推荐表达。
- 【保留原文】：英文缩写、指标名、数据集名或表头名建议直接保留。

翻译约束：

- 同一中文概念族尽可能使用同一个英文核心词。
- “识别”优先统一为 `recognition`，避免同一语境下与 `detection` 混用。
- 其他概念族也按同一原则处理，先确定组内口径，再补充单项译法。

## 1. 核心任务与应用场景

组内口径：中文“识别”统一译为 `recognition`，不与 `detection` 混用；`multi-label classification` 仅在明确指机器学习任务类型或引用文献原题时使用。中文“眼科疾病”统一译为 `ocular disease(s)`。中文“眼底筛查”统一译为 `fundus screening`，若句子中需强调疾病对象，可写作 `screening for fundus diseases`。

| 表达 | 推荐英文译法 | 标记 |
| --- | --- | --- |
| 多标签眼科疾病识别 | multi-label ocular disease recognition | 【推荐译法】 |
| 多标签识别 | multi-label recognition | 【推荐译法】 |
| 多标签图像识别 | multi-label image recognition | 【推荐译法】 |
| 早期眼底筛查 | early fundus screening | 【推荐译法】 |
| 眼底筛查 | fundus screening | 【通用术语】 |
| 眼科疾病诊断 | ocular disease diagnosis | 【通用术语】 |
| 眼科疾病识别 | ocular disease recognition | 【推荐译法】 |
| 眼科疾病诊断与预测 | diagnosis and prediction of ocular diseases | 【推荐译法】 |
| 眼底图像 | fundus images | 【通用术语】 |
| 医疗图像 | medical images | 【通用术语】 |
| 多疾病共存 | co-occurrence of multiple diseases | 【推荐译法】 |
| 眼科疾病共存 | ocular disease co-occurrence | 【推荐译法】 |
| 疾病共存关系 | disease co-occurrence relationships | 【推荐译法】 |
| 疾病相关区域 | disease-related regions | 【推荐译法】 |
| 病变区域 | lesion regions | 【通用术语】 |
| 病灶特征 | lesion features | 【通用术语】 |
| 识别性能 | recognition performance | 【推荐译法】 |
| 多标签识别性能 | multi-label recognition performance | 【推荐译法】 |

## 2. 泛化、跨域与数据划分

组内口径：`domain generalization` 和 `single domain generalization` 用于方法/问题设置；`cross-domain generalization` 用于和 `in-domain generalization` 相对的实验评价口径，表示跨数据集或跨机构泛化表现。域差异统一用 `domain shift` 或 `distribution shift`，不与 `domain gap` 混用。`source domain`、`target domain`、`unseen domain` 为标准术语；`source-domain` 作复合形容词修饰 image/feature 时保留连字符。ODIR 内部划分名 `Off-site` 和 `On-site` 保留原文。

| 表达 | 推荐英文译法 | 标记 |
| --- | --- | --- |
| 域泛化 | domain generalization | 【通用术语】 |
| 跨域泛化 | cross-domain generalization | 【推荐译法】 |
| 单域泛化 | single domain generalization | 【通用术语】 |
| 单一源域训练 | training on a single source domain | 【推荐译法】 |
| 域偏移 | domain shift | 【通用术语】 |
| 分布差异 | distribution shift | 【通用术语】 |
| 源域 | source domain | 【通用术语】 |
| 单一源域 | single source domain | 【通用术语】 |
| 源域原始图像 | original source-domain images | 【推荐译法】 |
| 源域增强图像 | augmented source-domain images | 【推荐译法】 |
| 训练集 | training set | 【通用术语】 |
| 目标域 | target domain | 【通用术语】 |
| 未知域 | unseen domain | 【通用术语】 |
| 跨域泛化数据集 | cross-domain generalization datasets | 【推荐译法】 |
| 测试集 | test set | 【通用术语】 |
| 域内泛化 | in-domain generalization | 【推荐译法】 |
| ODIR域内泛化 | ODIR in-domain generalization | 【推荐译法】 |
| Off-site | Off-site | 【保留原文】 |
| Off-site test | Off-site test | 【保留原文】 |
| On-site | On-site | 【保留原文】 |
| On-site test | On-site test | 【保留原文】 |
| 共有标签空间 | shared label space | 【通用术语】 |
| 三类共有标签空间 | three-class shared label space | 【推荐译法】 |
| D/A/M三类 | D/A/M classes | 【推荐译法】 |
| D/G/M三类 | D/G/M classes | 【推荐译法】 |

## 3. 方法框架、DFE 与 CAM

组内口径：标题采用 `Interpretable Single Domain Generalization with Privacy-Preserving for Multi-Label Ocular Disease Recognition`，不加冠词和 `framework`；正文中若明确指“框架”，加 `framework`，如 `the Interpretable Single Domain Generalization framework with Privacy-Preserving  for ...` 或 `the proposed method`。DFE 是本文模块名，首次出现使用 `Dual-Branch Guided Domain-Invariant Feature Extraction (DFE)`，后文用 `DFE module`。`domain-invariant features`、`domain-specific noise`、`Class Activation Mapping (CAM)` 为文献中常见表达；`source-domain` 作复合形容词时保留连字符。`style disturbance` 与图2表述保持一致。

| 表达 | 推荐英文译法 | 标记 |
| --- | --- | --- |
| 面向多标签眼科疾病识别的可解释与隐私保护单域泛化框架 | Interpretable Single Domain Generalization with Privacy-Preserving framework for multi-label ocular disease recognition | 【推荐译法】 |
| 所提方法 | the proposed method | 【通用术语】 |
| 可解释单域泛化框架 | interpretable single domain generalization framework | 【推荐译法】 |
| 所提可解释单域泛化框架 | the proposed interpretable single domain generalization framework | 【推荐译法】 |
| 双分支引导域不变特征提取模块 | Dual-Branch Guided Domain-Invariant Feature Extraction module | 【推荐译法】 |
| DFE | DFE | 【保留原文】 |
| 域不变特征 | domain-invariant features | 【通用术语】 |
| 疾病相关特征 | disease-related features | 【推荐译法】 |
| 源域原始图像 | original source-domain images | 【推荐译法】 |
| 源域增强图像 | augmented source-domain images | 【推荐译法】 |
| 风格扰动 | style disturbance | 【推荐译法】 |
| 域特定噪声 | domain-specific noise | 【推荐译法】 |
| 背景噪声 | background noise | 【通用术语】 |
| 光照变化 | illumination variations | 【通用术语】 |
| 边缘伪影 | image-edge artifacts | 【推荐译法】 |
| 设备噪声 | device noise | 【推荐译法】 |
| 域不变特征过滤模块 | domain-invariant feature filtering module | 【推荐译法】 |
| 双分支 mask 对比学习机制 | dual-branch mask-based contrastive learning mechanism | 【推荐译法】 |
| CAM | Class Activation Mapping (CAM) | 【通用术语】 |
| 模型关注区域 | model-attended regions | 【推荐译法】 |

## 4. ARC 与标签关系建模

组内口径：为与图2和 ARC 模块名保持一致，“关联/关联性”在本组统一使用 `relevance`，不与 `correlation` / `association` 混用。ARC 首次出现使用 `Adaptive Label-Feature Relevance Construction (ARC)`，后文用 `ARC module`；`label relevance` 在多标签学习文献中可作为通用口径使用，本文进一步扩展为 `label-label relevance` 和 `label-feature relevance`。注意力机制名使用 `self-attention` 和 `cross-attention`，首字母大写仅用于标题或括号中的机制名。

| 表达 | 推荐英文译法 | 标记 |
| --- | --- | --- |
| 自适应标签-特征关联性构建模块 | Adaptive Label-Feature Relevance Construction module | 【推荐译法】 |
| ARC | ARC | 【保留原文】 |
| 标签关联 | label relevance | 【通用术语】 |
| 标签-标签关联 | label-label relevance | 【推荐译法】 |
| 标签关联建模 | label relevance modeling | 【推荐译法】 |
| 标签-特征关联 | label-feature relevance | 【推荐译法】 |
| 标签-特征关联性构建 | label-feature relevance construction | 【推荐译法】 |
| 标签与疾病特征之间的关联 | relevance between labels and disease-related features | 【推荐译法】 |
| 疾病共现依赖 | disease co-occurrence dependencies | 【推荐译法】 |
| 自注意力机制 | self-attention mechanism | 【通用术语】 |
| Self-Attention | Self-Attention | 【保留原文】 |
| 交叉注意力机制 | cross-attention mechanism | 【通用术语】 |
| Cross-Attention | Cross-Attention | 【保留原文】 |
| 注意力一致性约束 | attention consistency constraint | 【推荐译法】 |
| 注意力一致性损失 | attention consistency loss | 【通用术语】 |
| 注意力特征对齐 | attention feature alignment | 【推荐译法】 |
| 注意力特征 | attention features | 【推荐译法】 |
| 注意力向量 | attention vectors | 【通用术语】 |

## 5. 隐私保护与差分隐私

组内口径：差分隐私基础术语采用 DP 文献通用表达，包括 `differential privacy`、`privacy budget`、`Gaussian differential privacy`、`noise multiplier`等。隐私与性能关系在本文统一使用 `privacy-performance trade-off`；DP 是Differential Privacy缩写，类似GDP是Gaussian differential privacy缩写，AdaGDP是Adaptive Gaussian Differential Privacy缩写。

| 表达 | 推荐英文译法 | 标记 |
| --- | --- | --- |
| 隐私泄露风险 | privacy leakage risk | 【推荐译法】 |
| 隐私泄露 | privacy leakage | 【通用术语】 |
| 隐私保护 | privacy preservation | 【通用术语】 |
| 隐私保护机制 | privacy-preserving mechanism | 【通用术语】 |
| 隐私保护训练 | privacy-preserving training | 【通用术语】 |
| 隐私保护场景 | privacy-preserving scenario | 【推荐译法】 |
| 隐私保护与模型性能之间的平衡 | balance between privacy preservation and model performance | 【推荐译法】 |
| 隐私-性能平衡 | privacy-performance trade-off | 【推荐译法】 |
| trade-off | trade-off | 【保留原文】 |
| 中等隐私预算 | moderate privacy budget | 【推荐译法】 |
| 中等隐私保护 | moderate privacy preservation | 【推荐译法】 |
| 中等隐私保护条件 | under moderate privacy preservation | 【推荐译法】 |
| 自适应高斯差分隐私 | Adaptive Gaussian Differential Privacy | 【推荐译法】 |
| 自适应高斯差分隐私机制 | Adaptive Gaussian Differential Privacy mechanism | 【推荐译法】 |
| AdaGDP | AdaGDP | 【保留原文】 |
| 自适应高斯差分隐私优化器 | Adaptive Gaussian Differential Privacy optimizer | 【推荐译法】 |
| 高斯差分隐私 | Gaussian differential privacy | 【通用术语】 |
| 固定噪声差分隐私 | fixed-noise differential privacy | 【推荐译法】 |
| GDP | GDP | 【保留原文】 |
| 噪声乘数 | noise multiplier | 【通用术语】 |
| noise\_multiplier | noise\_multiplier | 【保留原文】 |
| 噪声衰减速率 | noise decay rate | 【推荐译法】 |
| noise\_decay\_rate | noise\_decay\_rate | 【保留原文】 |
| 噪声注入速率 | noise injection rate | 【推荐译法】 |
| 加噪策略 | noise injection strategy | 【推荐译法】 |
| 隐私预算 \(\epsilon\) | privacy budget \(\epsilon\) | 【通用术语】 |
| \(\epsilon\) | \(\epsilon\) | 【保留原文】 |
| 松弛项 \(\delta\) | relaxation parameter \(\delta\) | 【通用术语】 |
| \(\delta\) | \(\delta\) | 【保留原文】 |
| \((\epsilon,\delta)\)-DP | \((\epsilon,\delta)\)-DP | 【通用术语】 |

## 6. 实验、模型与指标

组内口径：正文中“所提方法”统一用 `the proposed method`，表格行名保留 `Ours`。性能对比中的“基线模型”统一用 `baseline`；图示中的简单参照模型可用 `base model`。ODIR 指标名 `Final score`、`Final`、`Kappa`、`F1`、`AUC` 保留原文；评估粒度使用 `monocular` / `binocular`，表头可首字母大写。

| 表达 | 推荐英文译法 | 标记 |
| --- | --- | --- |
| 所提方法 | the proposed method | 【通用术语】 |
| 所提可解释单域泛化框架 | the proposed interpretable single domain generalization framework | 【推荐译法】 |
| 该框架 | the framework | 【通用术语】 |
| Ours | Ours | 【保留原文】 |
| 基线模型 | baseline | 【通用术语】 |
| baseline | baseline | 【保留原文】 |
| base model | base model | 【通用术语】 |
| ResNet50 | ResNet50 | 【保留原文】 |
| 骨干网络 | backbone | 【通用术语】 |
| 检查点 | checkpoint | 【通用术语】 |
| 候选检查点 | candidate checkpoints | 【推荐译法】 |
| 最优隐私检查点 | optimal privacy checkpoint | 【推荐译法】 |
| 单目 | monocular | 【通用术语】 |
| Monocular | Monocular | 【保留原文】 |
| 单目指标 | monocular metrics | 【推荐译法】 |
| 双目 | binocular | 【通用术语】 |
| Binocular | Binocular | 【保留原文】 |
| 双目指标 | binocular metrics | 【推荐译法】 |
| Final score | Final score | 【保留原文】 |
| Final | Final | 【保留原文】 |
| Kappa | Kappa | 【保留原文】 |
| F1 | F1 | 【保留原文】 |
| AUC | AUC | 【保留原文】 |

## 7. 数据集、标签与疾病名称

组内口径：本组以 `docs/terminology_glossary.md` 已校对的英文名和缩写为准。数据集名、英文疾病名和类别缩写在表格、图注和正文中保持原文；中文疾病名翻译时使用对应英文名，不再另行改写。

| 表达 | 推荐英文译法 | 标记 |
| --- | --- | --- |
| ODIR-5K | ODIR-5K | 【保留原文】 |
| ODIR | ODIR | 【保留原文】 |
| RFMiD | RFMiD | 【保留原文】 |
| EDID | EDID | 【保留原文】 |
| 正常眼底 | normal | 【通用术语】 |
| N | N | 【保留原文】 |
| 糖尿病视网膜病变 | Diabetic Retinopathy | 【通用术语】 |
| D | D | 【保留原文】 |
| 青光眼 | Glaucoma | 【通用术语】 |
| G | G | 【保留原文】 |
| 白内障 | Cataract | 【通用术语】 |
| C | C | 【保留原文】 |
| 年龄相关性黄斑变性 | Age-related Macular Degeneration | 【通用术语】 |
| A | A | 【保留原文】 |
| 高血压视网膜病变 | Hypertension | 【通用术语】 |
| H | H | 【保留原文】 |
| 病理性近视 | Myopia | 【通用术语】 |
| M | M | 【保留原文】 |
| 其他异常 | Others | 【推荐译法】 |
| O | O | 【保留原文】 |
| 中心性浆液性脉络膜视网膜病变 | Central Serous retinopathy | 【通用术语】 |
| CSR | CSR | 【保留原文】 |
| 黄斑瘢痕 | Macular Scar | 【通用术语】 |
| MS | MS | 【保留原文】 |
| 视盘水肿 | Disc Edema | 【通用术语】 |
| DE | DE | 【保留原文】 |
| 翼状胬肉 | Pterygium | 【通用术语】 |
| 视网膜脱离 | Retinal Detachment | 【通用术语】 |
| RD | RD | 【保留原文】 |
| 视网膜色素变性 | Retinitis Pigmentosa | 【通用术语】 |
| RP | RP | 【保留原文】 |
| 视网膜炎 | Retinitis | 【通用术语】 |
| RS | RS | 【保留原文】 |
| 视网膜中央静脉阻塞 | Central Retinal Vein Occlusion | 【通用术语】 |
| CRVO | CRVO | 【保留原文】 |
