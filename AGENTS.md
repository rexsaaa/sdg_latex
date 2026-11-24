# AGENTS.md

## 期刊返修工作区

- 处理审稿意见时，先读本库的[返修协作规则](docs/revision_workflow_zh.md)，再核对 `submit/revision/` 中对应意见的材料。当前正式稿为 `submit/build/main_cas.tex` 及其章节、表格。
- 以审稿人当轮实际收到的稿件为基准，在当前稿上累计已批准的修改。查阅 2026 年 11 月已提交的版本、最终回复和交付格式，见[五位审稿人返修记录](submit/revision/round_2026-11-23.md)。
- 本库独立维护论文历史。服务器上的 ODIR 实验仓库负责代码和原始运行记录，需要追溯实验时查其 `PROJECT_INDEX.md`。从 ODIR 根目录操作论文库时使用 `git -C sdg_latex ...`。
- 服务器上的 `ODIR/sdg_latex` 是主要编辑与编译位置，Mac 上的 `/Users/jq/Desktop/sdg_latex` 用于审核和同步。
- 使用 `python scripts/build_revision.py` 生成两版修订 PDF；`--variant highlight` 或 `--variant clean` 可单独生成，`--check` 只验证、不替换正式 PDF。缓存固定在已忽略的 `build/revision/`。依赖与安装命令见 `submit/build/README_BUILD.md`。
- 多个对话共用当前稿，改动前检查当前文件及 Git 差异，避免覆盖其他点已通过的修改。Mac 按审核节点同步；Mac 手动修改须先合入服务器。提交、推送及写回按用户授权范围执行，不默认每次小改都传输整份 PDF。

## 投稿前的初稿工作说明（历史）

这是一个用户的待投稿 LaTeX 论文项目。当前稿件曾由性能较弱的 agent 根据导师意见部分改写，整体结构、论证逻辑、贡献表述和论文格式可能存在问题。不要默认现有框架正确。后续用户会提供导师新的修改意见，协助对论文全文进行批判性修改。

## 项目结构

- `manuscripts/zh/`：中文稿，主要论文内容源头，后续修改先优化中文稿。
- `manuscripts/compare/`：中英对照稿，待中文稿优化完毕再进行翻译和双语校对。
- `manuscripts/trans/`：英文纯稿，由中英对照稿去掉中文部分形成，作为最终投稿稿件候选。
- `docs/`：之前 agent 的修改计划、术语记录、翻译流程和写作历史。
- `images/`：论文共用图片。
- `build/`：LaTeX 编译产物，通常忽略，各版本稿件的编译版本应存放在内部的对应位置。
- `releases/`：已导出的 PDF 快照，作为各tag的pdf发布版。
- `src/`：实验数据和结果材料，是论文实验的数据来源，通常只读。

## 查阅历史初稿

只读必要文件，不要默认扫描整个项目。采用渐进式披露，按需打开文件。

默认先检查中文稿：

- 入口：`manuscripts/zh/main_zh.tex`
- 正文：`manuscripts/zh/sections/`

论文按章节拆分为 LaTeX 文件。可以按需查看单个章节；若要快速了解论文任务、摘要和贡献，先读 `manuscripts/zh/sections/00_frontmatter.tex`；若要批判整体框架，再通读 `manuscripts/zh/sections/`。

若要了解论文的修改历史，读：

- `docs/version_history.md`：v0.1 到 v1.0 的精简版本历史。

注意：历史文档只用于了解论文经历过哪些修改，不代表当前框架一定合理。若用户提供新的导师意见，应以新的导师意见和论文当前逻辑为准，重新判断旧框架是否需要调整。

## 导师意见处理

收到新的导师意见后，先判断影响范围。若涉及主线、创新点、问题定义或贡献表述，应优先检查摘要、引言、方法和实验是否需要联动修改；不要只做局部润色。
