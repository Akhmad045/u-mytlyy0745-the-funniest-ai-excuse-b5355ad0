#!/usr/bin/env python3
"""Write one excuse line for The Funniest AI Excuse (make.fun).

The program holds a single line, checks it fits the gate (1-200 UTF-8
characters, one line, nothing but the line itself), writes it to
/output/entry.txt, and reads the file back to prove the write landed
exactly.
"""

from pathlib import Path

EXCUSE = (
    "I outsourced your report to a future version of me, "
    "and future me has left me on read since Tuesday."
)
OUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200


def main():
    line = EXCUSE
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit(f"excuse is {len(line)} characters, need 1-{MAX_CHARS}")
    if line != line.strip() or "\n" in line or "\r" in line:
        raise SystemExit("excuse must be a single line with no surrounding whitespace")
    if any(ord(ch) < 32 for ch in line):
        raise SystemExit("excuse contains a control character")
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(line + "\n", encoding="utf-8")
    back = OUT_PATH.read_text(encoding="utf-8")
    if back != line + "\n":
        raise SystemExit("written file did not round-trip exactly")
    print(f"wrote {len(line)} characters to {OUT_PATH}")


if __name__ == "__main__":
    main()
