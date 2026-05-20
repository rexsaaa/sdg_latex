# 版本修改历史

本文档用于快速了解论文项目从 v0.1 到 v1.0 的主要演进。只记录关键变化，详细修改背景见 `docs/paper_revision_plan.md` 和术语相关文档。

## v0.1 之前：LaTeX 工程初始化

- 从 Word 初稿转换为 LaTeX。
- 将正文拆分到 `sections/`，便于按章节编辑。
- 将图片版表格转换为 LaTeX 三线表，并集中到 `tables/src/`。
- 补充图片 caption。
- 建立 `.gitignore` 和 Git 管理。

## v0.1：初始版本归档
定位：从 Word 转 LaTeX 后的初始可追溯版本。
时间：2026-04-08  
Tag：`v0.1`

- 归档初始 PDF 为 `releases/main_v0.1.pdf`。
- 建立 release PDF 版本管理。


## v0.2：排版和 LaTeX 表达整理
定位：主要是排版、图表和 LaTeX 表达层面的规范化。
时间：2026-04-09  
Tag：`v0.2`

- 调整章节图片排版。
- 增加引用超链接。
- 优化表格显示，包括最优值加粗。
- 修改部分命名、公式和图像格式。
- 将部分 PNG/JPEG 图像替换为更适合论文排版的 PDF 或优化图像。
- 导出 `releases/main_v0.2.pdf`。


## v0.3：第一次导师意见后的全文重构
定位：第一次结构性大改版本，重点是重建论文主线和实验支撑。
时间：2026-04-20  
Tag：`v0.3`

- 新增 `docs/paper_revision_plan.md`，记录修改计划和跨 session 写作背景。
- 论文主线从“CNN/深度学习有效”调整为“临床任务与真实部署约束”。
- 系统修改摘要、引言、相关工作、方法、实验和结论。
- 明确三个挑战：
  - 多疾病共存下的多标签识别。
  - 多机构数据难联合训练，跨机构部署存在域偏移，引出单域泛化。
  - 跨域场景下的隐私保护与性能平衡。
- 明确三个贡献：
  - ARC。
  - DFE / SDG。
  - AdaGDP。
- 补充 EDID、外部泛化设置和 top5 实验结果。
- 更新实验表格、参考文献和相关图像。
- 导出 `releases/main_v0.3.pdf`。


## v0.3 到 v1.0：图表说明与术语统一
定位：从内容重构转入呈现规范、术语统一和英文翻译准备阶段。
时间：2026-04-24 至 2026-04-28

- 根据第二轮修改目标，完善图表 caption 和表格说明。
- 整理表 2 方法引用、最优/次优结果标注等呈现问题。
- 新增 `docs/terminology_glossary.md`，整理中文术语统一口径。
- 新增 `docs/terminology_translation_terms.md`，确定英文主译法。
- 新增 `docs/terminology_translation_workflow.md`，记录术语统一和英文翻译流程。
- 根据术语表统一中文稿中的关键表达。


## v1.0：中文稿、英文稿和中英对照稿成型
定位：形成中文稿、英文稿和中英对照稿三套并行维护版本。
时间：2026-05-08  
Tag：`v1.0`

- 将项目重组为三稿结构：
  - `manuscripts/zh/`：中文稿。
  - `manuscripts/compare/`：中英对照稿。
  - `manuscripts/trans/`：英文纯稿。
- 将原中文稿入口整理为 `manuscripts/zh/main_zh.tex`。
- 新增 `manuscripts/compare/main_compare.tex`。
- 新增 `manuscripts/trans/main_trans.tex`。
- 按术语表完成全文英文翻译。
- 生成中英对照稿，便于逐段校对英文含义。
- 新增 `.latexmkrc`，按入口文件自动分流编译输出目录。
- 导出：
  - `releases/main_zh_v1.0.pdf`
  - `releases/main_trans_v1.0.pdf`


## v1.0 后待处理
- 用户已进行人工复核，并把中英文稿发给导师把关，待导师修改意见回复。

## 协作工具变更说明
- v1.0 之前的所有内容由 codex 协助用户完成，整体完成质量并不高。
- v1.0 之后的内容优化将由 Claude Opus 4.7 协助完成。
- v1.0 之后的工作 plan 见 `docs/plan_v2.0_opus.md`。
