# LaTeX 论文项目搭建指南

## 背景

我正在撰写一篇学术论文，目前有 Word 版本的初稿。需要将其转换为 LaTeX 格式，并在 Mac 本机上建立一套完整的论文管理方案，使用 Antigravity 编辑器 + Agent 协助进行编辑和版本管理。

## 目标

1. 将 Word 论文转换为 LaTeX（`.tex`）格式
2. 在 Mac 本机建立 LaTeX 项目，使用 Git 进行版本管理
3. 利用 Agent 协助编辑 `.tex` 文件、编译 PDF、管理版本

## 环境配置

### 必须安装

| 工具 | 安装方式 | 用途 |
|------|----------|------|
| **MacTeX** | [下载安装](https://www.tug.org/mactex/)（~4.5GB） | 提供 `pdflatex`、`latexmk`、`bibtex` 等编译工具 |
| **Git** | `xcode-select --install` 或 `brew install git` | 版本管理 |

### 编译命令

```bash
# 推荐：用 latexmk 一键编译（自动处理多次编译和参考文献）
latexmk -pdf main.tex

# 手动编译
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex

# 如果论文包含中文
latexmk -xelatex main.tex
```

## 项目结构

```
paper-project/
├── main.tex                 ← 主文件（用 \input{} 引用各章节）
├── references.bib           ← BibTeX 参考文献
├── figures/                 ← 图片素材
├── sections/                ← 各章节拆分
│   ├── introduction.tex
│   ├── method.tex
│   ├── experiments.tex
│   └── conclusion.tex
├── .gitignore               ← 忽略编译产物
├── Makefile                 ← 一键编译（可选）
└── README.md
```

## 关键配置文件

### `.gitignore`

```gitignore
*.aux
*.log
*.out
*.toc
*.lof
*.lot
*.bbl
*.blg
*.synctex.gz
*.fdb_latexmk
*.fls
```

### `Makefile`（可选）

```makefile
all:
	latexmk -pdf main.tex

clean:
	latexmk -C

watch:
	latexmk -pdf -pvc main.tex
```

## 工作流

1. 用 Antigravity 打开 Mac 本机的论文项目目录
2. 告诉 Agent 要修改的内容 → Agent 编辑 `.tex` 文件
3. Agent 运行 `latexmk -pdf main.tex` 编译生成 PDF
4. 本地查看 PDF 效果
5. 满意后 Agent 帮忙 `git commit` 记录版本

## 注意事项

- **章节拆分**：用 `\input{}` 将论文拆分为多个文件，方便 Agent 精准修改特定章节，Git diff 也更清晰
- **Git commit 规范**：使用有意义的 commit message，如 `"修改摘要：突出方法创新点"`
- **中文支持**：如需中文，使用 `\usepackage{ctex}` 并用 `xelatex` 编译
- **图片格式**：推荐使用 PDF 或 PNG 格式的图片

## 待办

- [ ] Mac 上安装 MacTeX
- [ ] 创建项目目录 + `git init`
- [ ] 创建 `.gitignore`
- [ ] 用 Antigravity 打开项目
- [ ] 将 Word 论文交给 Agent 转换为 `.tex`
- [ ] 初始 `git commit`
