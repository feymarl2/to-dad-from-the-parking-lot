#!/usr/bin/env python3
"""Unsent entry: one micro-confession that never got sent.

Running this file writes the confession into entry.txt inside the
output folder named by MAKEFUN_OUTPUT_DIR (default /output). Only the
standard library is used, and the bytes written never change between
runs: no clock, no randomness, no network.
"""

from pathlib import Path
import os

CONFESSION = "To: Dad\nI got the job. I almost called you from the parking lot before I remembered."
ENTRY_NAME = "entry.txt"


def output_folder() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def write_confession() -> None:
    folder = output_folder()
    folder.mkdir(parents=True, exist_ok=True)
    (folder / ENTRY_NAME).write_text(CONFESSION, encoding="utf-8", newline="")


if __name__ == "__main__":
    write_confession()
