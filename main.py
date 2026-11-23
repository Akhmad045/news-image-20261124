#!/usr/bin/env python3
"""Write the WORLD NEWS front page for Tuesday 24 November 2026 to
/output/entry.png.

The image is drawn at build time and committed as entry.png; this program
simply copies it to the output directory. Standard library only, no network.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()
