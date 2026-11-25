#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — round 2 entry.

Writes one original fortune-cookie line for a software developer
to /output/entry.txt (or the directory named by ENTRY_OUTPUT,
OUTPUT_DIR or MAKEFUN_OUTPUT_DIR).
"""

import os

LINE = "A green build is not a promise; it is a rumor the tests agreed to spread."


def main():
    if not 1 <= len(LINE) <= 120:
        raise SystemExit("LINE must be 1-120 characters")
    out_dir = (
        os.environ.get("ENTRY_OUTPUT")
        or os.environ.get("OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT_DIR")
        or "/output"
    )
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
