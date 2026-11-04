# Computers and Electrical Engineering / Elsevier CAS Build

This directory contains a self-contained CAS single-column conversion of the latest English `manuscripts/trans` draft for submission to Computers and Electrical Engineering.

The Build section records the original submission workflow. For current reviewer revisions, use Revision builds below.

## Build

Run from this directory:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main_cas.tex
pdflatex -interaction=nonstopmode -halt-on-error main_cas.tex
cp main_cas.pdf main_cas_full.pdf
gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dFirstPage=1 -dLastPage=1 -sOutputFile=highlights.pdf main_cas_full.pdf
gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dFirstPage=2 -sOutputFile=main_cas.pdf main_cas_full.pdf
```

The compiled full CAS PDF is `main_cas_full.pdf`. The separate highlights PDF is `highlights.pdf`, extracted from page 1 of the full CAS PDF. The manuscript PDF for upload is `main_cas.pdf`, extracted from page 2 onward of the full CAS PDF.

## Notes

- Template class: `cas-sc` from `submit/els-cas-templates`, matching the Elsevier LaTeX template linked by the Computers and Electrical Engineering Guide for Authors.
- The `longmktitle` option was not used because it triggered an expl3 compatibility error under the local TeX Live 2026 installation.
- Section structure now uses numbered LaTeX subsections instead of lettered in-section headings.
- References now use LaTeX `\cite{...}` calls and a `thebibliography`/`\bibitem` reference list, with numeric citations in square brackets.
- Author order, the Jinan University affiliation, and the corresponding author's ORCID/email have been filled in `main_cas.tex`.
- `main_cas.tex` keeps the CAS `highlights` environment so the full CAS PDF can be regenerated. The upload-ready `main_cas.pdf` is produced by splitting page 2 onward from `main_cas_full.pdf`, so it no longer includes the highlights page.
- The CRediT statement has been removed from the manuscript body; the CEE guide encourages CRediT but does not make it a hard manuscript-format requirement.
- Remaining submission metadata to confirm before direct journal upload: full postal affiliation addresses, funding statement, declaration of competing interests, data availability statement, and author biographies/photos if requested by the submission system.
- Original article-style float options such as `[!htb]` and `[H]` were removed in the copied build files so that CAS controls float placement.

## Reviewer revision markup

The baseline for this round is the Git tag `准备审稿人意见返修`. Highlight the final text changed from that baseline and use the same comment IDs in the manuscript and response letter. Keep original reviewer numbering where present. Assign stable point IDs to separate issues in unnumbered reviews. Reviewer 1 has one unnumbered comment and uses `R1`.

- For a paragraph addressing one comment, use `\revision{R1}{Revised text}` at its first change. Use `\revision*{R1}{Further revised text}` for later changes on the same page. Repeat the unstarred form after a page break and check the positions in the final PDF.
- For a paragraph addressing different comments, wrap the paragraph in `mixedrevisions`. Every highlighted span receives a superscript comment label. The starred form also shows its superscript label in this environment. The labels distinguish different reviewers and different points from the same reviewer.
- For one span addressing several comments, supply all applicable IDs, such as `\revision{R3-1, R5-4}{Revised text}`. In a mixed paragraph these IDs appear together after that span.
- When a later edit replaces earlier wording, reassess the applicable IDs against the final text. Update the relevant reviewer responses and check their page references after pagination is final.

The following is a markup example for maintainers.

```latex
\begin{mixedrevisions}
\revision{R1}{Reworded sentence.}
Unchanged connecting text.
\revision{R2-1}{Clarification of the method.}
\revision{R3-1, R5-4}{Explanation addressing both comments.}
\end{mixedrevisions}
```

The response letter should name the same IDs and identify the relevant sections and final page numbers. Yellow highlighting, margin labels, superscript labels and the revision guide are controlled together by `\RevisionClean`.

## Revision builds

Build the highlighted version twice to resolve references and margin positions. After edits that affect pagination, check the labels in the resulting PDF and rerun compilation if positions have changed.

```sh
pdflatex -interaction=nonstopmode -halt-on-error -jobname=main_cas_revised_highlight_full main_cas.tex
pdflatex -interaction=nonstopmode -halt-on-error -jobname=main_cas_revised_highlight_full main_cas.tex
gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dFirstPage=2 -sOutputFile=main_cas_revised_highlight.pdf main_cas_revised_highlight_full.pdf
```

To build the clean version, define `\RevisionClean` before loading the same source.

```sh
pdflatex -interaction=nonstopmode -halt-on-error -jobname=main_cas_revised_full '\def\RevisionClean{1}\input{main_cas.tex}'
pdflatex -interaction=nonstopmode -halt-on-error -jobname=main_cas_revised_full '\def\RevisionClean{1}\input{main_cas.tex}'
gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dFirstPage=2 -sOutputFile=main_cas_revised.pdf main_cas_revised_full.pdf
```

These commands create dedicated revision PDFs. The first page containing the separate research highlights is removed from each manuscript PDF.
