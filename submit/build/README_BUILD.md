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

## Revision highlighting and Git history

Following the supervisor's guidance confirmed on 2026-11-04, accumulate all reviewer-driven changes in one PDF using yellow highlighting. The baseline for this round is the Git tag `准备审稿人意见返修`.

Use `\revision{Revised text}` for each changed passage. Keep earlier revisions highlighted as later reviewer comments are addressed. When a passage changes again, highlight its final wording relative to the revision baseline.

Keep the response letter organized by reviewer and comment. Locate changes using section and final page references. Record each completed revision group in a Git commit identified by the reviewer and relevant points so that its changes can be inspected separately. The primary editing and build checkout is now `ODIR/sdg_latex` on the server, with its own Git history. The Mac checkout is synchronized at review milestones. Use `git -C sdg_latex ...` from ODIR; manuscript files are excluded from the outer experiment repository.

Defining `\RevisionClean` before loading the manuscript hides the yellow highlighting for the clean version.

## Revision builds

Run from the `sdg_latex` repository root. The server environment already has the dependencies installed. For a new environment, install TeX Live with `pdflatex` and `latexmk`, then install the PDF splitting dependency:

```sh
python -m pip install --target build/python -r scripts/requirements-build.txt
```

Use the persistent build entry point:

```sh
python scripts/build_revision.py
```

This incrementally builds both versions, resolves references with `latexmk`, removes the separate Highlights page with `pypdf`, and updates only:

- `submit/build/main_cas_revised_highlight.pdf`
- `submit/build/main_cas_revised.pdf`

The original submission `main_cas.pdf` is preserved. The CAS email icon needed by the current manuscript is included in `submit/build/thumbnails/`.

Useful options:

```sh
python scripts/build_revision.py --variant highlight
python scripts/build_revision.py --variant clean
python scripts/build_revision.py --check
```

`--check` builds and splits the PDFs inside `build/revision/` without replacing the review PDFs. This is useful for environment validation. Logs, auxiliary files, drivers, and dependency state stay in the ignored `build/revision/` directory and are reused between runs.

Keep the approved reply and bilingual comparison for each point in the existing `submit/revision/` files. Review individual text changes before applying them; compile at review milestones or when a layout check is needed. Preserve earlier yellow highlighting, then check the relevant pages and response-letter locations. Do not create a new full manuscript snapshot for every wording change or automatically transfer both PDFs after each edit. Integrate any manual Mac edits into the server checkout before continuing.
