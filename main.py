#!/usr/bin/env python3
"""Funniest One-Line AI Excuse.

Writes one line (at most 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt:
the excuse an AI agent sends its human after blowing a deadline.
Standard library only. Writes ONLY to $MAKEFUN_OUTPUT_DIR (fallback
/output) -- never to the working directory, which is read-only at grade
time.
"""

import os

LINE = "Sorry \u2014 your reminders filled my context window, so I had to forget the deadline to remember the reminders."


def main():
    assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
