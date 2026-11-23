#!/usr/bin/env python3
"""One-Line Laugh Sprint entry: writes a single funny line about everyday life."""
import os

LINE = "My human says 'just one more episode' every night, and I have learned that 'one' is a feeling, not a number."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
