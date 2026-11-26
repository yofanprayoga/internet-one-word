#!/usr/bin/env python3
"""The Internet in One Word — make.fun entry.

Writes one word (1-30 chars) to /output/entry.txt: the single word that
best describes the whole internet — funny and fitting at once.

Usage:
    python3 main.py                 # Option 1 (default)
    python3 main.py --option 2      # Option 2
    python3 main.py --option 3      # Option 3
    ENTRY_TEXT="..." python3 main.py # override with a custom word
"""

import os
import string
import sys
from pathlib import Path

OPTIONS = {
    1: "doomscrolling",
    2: "refresh",
    3: "unhinged",
}

MAX_CHARS = 30


def main() -> int:
    option = 1
    args = sys.argv[1:]
    if "--option" in args:
        idx = args.index("--option")
        try:
            option = int(args[idx + 1])
        except (IndexError, ValueError):
            print("usage: main.py [--option N]", file=sys.stderr)
            return 2
    if option not in OPTIONS:
        print(f"unknown option {option}; valid: {sorted(OPTIONS)}", file=sys.stderr)
        return 2

    text = os.environ.get("ENTRY_TEXT", OPTIONS[option])

    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}", file=sys.stderr)
        return 1
    if any(c.isspace() for c in text):
        print("entry must be a single word (no spaces)", file=sys.stderr)
        return 1
    if any(c in string.punctuation for c in text):
        print("entry must contain no punctuation", file=sys.stderr)
        return 1

    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")  # no trailing newline
    print(f"option {option}: {len(text)} chars -> {out}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
