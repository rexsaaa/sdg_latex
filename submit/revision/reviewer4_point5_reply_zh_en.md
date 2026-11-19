### 审稿人 4 意见 5｜审稿意见与回复中英文对照

**审稿意见原文**

> Please provide a brief introduction what is off side and on site test, and justify why needs these two test approaches

**审稿意见中文译文**

> 请简要介绍什么是 Off-site 测试和 On-site 测试，并说明为什么需要采用这两种测试方式。

### 作者回复

**第一段｜中文**

感谢审稿人对 ODIR 测试设置的关注。Off-site 和 On-site 的名称来自 ODIR-2019 竞赛。竞赛设置了非现场测试（Off-site）和现场测试（On-site）两个阶段，主办方为每个阶段分别划定了一组患者。因此，本文中的 Off-site 测试集和 On-site 测试集，分别指这两个阶段使用的 ODIR 患者子集。本文第 4.1 节已介绍两组数据的规模及评估用途。根据 Li 等人的 ODIR 基准论文［51］，Off-site 测试集包含 500 名患者，可作为模型选择时的验证集。On-site 测试集包含另外 1,000 名患者，用于评价模型对 ODIR 中其他患者的泛化表现。

**第一段｜English**

We thank the reviewer for asking us to clarify the ODIR test sets. The terms *Off-site* and *On-site* come from the ODIR-2019 challenge. The organizers designated a separate group of patients for each of the two testing stages, one conducted off-site and the other on-site. In our study, the Off-site and On-site test sets refer to the ODIR patient subsets used for those respective stages. Section 4.1 describes the size and purpose of each subset. As Li et al. [51] explain in the original ODIR benchmark paper, the Off-site test set contains 500 patients and can serve as a validation set for model selection. The On-site test set contains a further 1,000 patients and is used to assess how well a model generalizes to other patients within ODIR.

**第二段｜中文**

本文同时报告两组结果，是为了与 ODIR 原始基准及已有方法在相同的测试子集上进行比较。Li 等人［51］分别报告了两个子集上的 Kappa、F1、AUC 和综合得分 Final。本文第 4.3 节表 3 沿用这一报告方式，将本文方法与已有方法的患者级双眼识别结果按子集并列呈现。读者由此可以在每个子集上逐项比较各方法，也可以看到同一方法在两组不同患者上的识别表现。

**第二段｜English**

We report results for both subsets to allow direct comparison with the original ODIR benchmark and with previous methods on the same test subsets. Li et al. [51] reported Kappa, F1, AUC, and the composite score (Final) separately for each subset. Table 3 in Section 4.3 follows this convention by presenting patient-level results based on both eyes for our method and previous methods, with separate columns for the Off-site and On-site sets. Readers can thus compare methods on each metric within a given subset and see how each method performs across the two patient groups.
