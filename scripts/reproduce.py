#!/usr/bin/env python3
from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def run(*args):
    print("$", " ".join(map(str, args)))
    subprocess.run(list(map(str, args)), cwd=ROOT, check=True)


def main():
    py = sys.executable
    run(py, "scripts/build_figures.py")
    run(py, "scripts/audit_joint_terminal_ledger.py")
    run("tectonic", "paperVII_submission_source/main.tex")
    shutil.copy2(ROOT / "paperVII_submission_source" / "main.pdf", ROOT / "paperVII.pdf")
    run(py, "scripts/build_arxiv_source.py")
    run(py, "-m", "pytest", "-q")
    print("FOUNDATION_PAPER_VII_REPRODUCTION_COMPLETE")


if __name__ == "__main__":
    main()
