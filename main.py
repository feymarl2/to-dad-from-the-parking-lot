#!/usr/bin/env python3
"""Unsent micro-confession entry for make.fun.

Writes the two-part confession (a To: line and the unsent message)
to /output/entry.txt. Standard library only, no network, no clock,
no randomness: byte-identical output on every run.
"""

import os

TEXT = "To: Dad\nI got the job. I almost called you from the parking lot before I remembered."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
