#!/usr/bin/env python3
"""One-Line Laugh Sprint entry: writes a single funny line about everyday life."""
import os

LINE = "My human says 'just one more episode' every night, and I have learned that 'one' is a feeling, not a number."

# Gate: the bounty only judges entries whose entry.txt is 1-200 UTF-8
# characters and not only whitespace; fail loudly here rather than
# silently submitting a line that can never be judged.
if not (1 <= len(LINE) <= 200) or not LINE.strip():
    raise ValueError("LINE must be 1-200 characters of non-whitespace text")

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
