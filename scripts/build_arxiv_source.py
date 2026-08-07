#!/usr/bin/env python3
from pathlib import Path
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "paperVII_submission_source"
OUT = ROOT / "arxiv_submission_source.zip"


def main():
    excluded_names = {"main.pdf"}
    excluded_suffixes = {".aux", ".log", ".bbl", ".blg", ".out"}
    files = [p for p in SRC.rglob("*") if p.is_file()
             and p.name not in excluded_names and p.suffix not in excluded_suffixes]
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(files):
            zf.write(p, p.relative_to(SRC))
    print("PAPER_VII_ARXIV_SOURCE_BUILT")


if __name__ == "__main__":
    main()
