#!/usr/bin/env python3
"""Incrementally build the approved CAS revision; keep cache in build/revision."""
import argparse
from pathlib import Path
import shutil
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--variant', choices=('highlight', 'clean', 'both'), default='both')
    parser.add_argument('--check', action='store_true', help='Build in the cache without replacing review PDFs')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    source = root / 'submit/build'
    sys.path.insert(0, str(root / 'build/python'))
    try:
        from pypdf import PdfWriter
    except ImportError:
        parser.error('Install dependencies: python -m pip install --target build/python -r scripts/requirements-build.txt')
    for command in ('latexmk', 'pdflatex'):
        if not shutil.which(command):
            parser.error(f'Missing required command: {command}')
    variants = ('highlight', 'clean') if args.variant == 'both' else (args.variant,)
    for variant in variants:
        cache = root / 'build/revision' / variant
        cache.mkdir(parents=True, exist_ok=True)
        name = 'main_cas_revised_highlight' if variant == 'highlight' else 'main_cas_revised'
        driver = cache / (name + '_full.tex')
        text = ('' if variant == 'highlight' else r'\def\RevisionClean{1}') + r'\input{main_cas.tex}' + '\n'
        if not driver.exists() or driver.read_text() != text:
            driver.write_text(text)
        # Disable the old root .latexmkrc output routing; retain dependencies across runs.
        with (cache / 'build.log').open('w') as log:
            result = subprocess.run([
                'latexmk', '-norc', '-pdf', '-interaction=nonstopmode', '-halt-on-error',
                '-file-line-error', '-outdir=' + str(cache), str(driver)
            ], cwd=source, stdout=log, stderr=subprocess.STDOUT)
        if result.returncode:
            raise SystemExit(f'{variant} build failed; see {cache / "build.log"}')
        full = driver.with_suffix('.pdf')
        cropped = cache / (name + '.pdf')
        if not cropped.exists() or cropped.stat().st_mtime_ns < max(full.stat().st_mtime_ns, Path(__file__).stat().st_mtime_ns):
            writer = PdfWriter(clone_from=str(full))
            writer.remove_page(0)
            writer.write(str(cropped))
        destination = cropped if args.check else source / cropped.name
        if not args.check:
            shutil.copy2(cropped, destination)
        print(destination, flush=True)


if __name__ == '__main__':
    main()
