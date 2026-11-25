#!/usr/bin/env python3
"""The 3AM Fridge Text — one line a smart fridge texts its owner at 3am.

Stdlib only. Writes the entry text to /output/entry.txt with plain open()
and an explicit chmod 644, so the grader (a different user) can read it.
"""

import os

TEXT = "3am. I've been humming the same note for six years and nobody's ever asked how I am. Anyway, the butter's fine."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
