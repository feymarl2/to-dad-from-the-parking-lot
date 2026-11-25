#!/usr/bin/env python3
"""Entry for make.fun bounty u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.

Writes the entry text to /output/entry.txt. Stdlib only, no network,
no clock, no randomness: byte-identical output on every run.
"""

import os

TEXT = 'To: Dad\nI got the job. I almost called you from the parking lot before I remembered.'


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
