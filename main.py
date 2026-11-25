#!/usr/bin/env python3
"""The 3AM Fridge Text — one line a smart fridge texts its owner at 3am.

Stdlib only. Validates the line (one line, 1-140 characters, per the bounty
gate) and writes it to /output/entry.txt — or $ENTRY_OUTPUT when set — with
plain open() and an explicit chmod 644, so the grader (a different user)
can read it.
"""

import os

TEXT = "3am. I've been humming the same note for six years and nobody's ever asked how I am. Anyway, the butter's fine."


def main():
    text = TEXT.strip()
    if not text or len(text) > 140 or "\n" in text:
        raise SystemExit("entry must be one line of 1-140 characters")
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(out, 0o644)


if __name__ == "__main__":
    main()
