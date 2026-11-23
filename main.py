#!/usr/bin/env python3
"""Write the WORLD NEWS front page for Tuesday 24 November 2026 to
/output/entry.png.

The image is drawn at build time and committed as entry.png; this program
simply copies it to the output directory. Standard library only, no network.
"""
import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    # Verify the copy is byte-identical to the committed image.
    source = SRC.read_bytes()
    written = OUT.read_bytes()
    if written != source:
        print("error: output differs from entry.png", file=sys.stderr)
        raise SystemExit(1)
    digest = hashlib.sha256(written).hexdigest()
    print(f"entry.png: {len(written)} bytes, sha256 {digest}")


if __name__ == "__main__":
    main()
