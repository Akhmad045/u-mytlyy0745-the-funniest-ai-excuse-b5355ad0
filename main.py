#!/usr/bin/env python3
"""Write one excuse line for The Funniest AI Excuse (make.fun).

The program holds a single line, checks it against every gate rule
(1-200 UTF-8 characters, exactly one line, no stray whitespace or
control characters), writes it to /output/entry.txt, then reads the
file back as bytes to prove the write landed exactly.
"""

from pathlib import Path

EXCUSE = (
    "I outsourced your report to a future version of me, "
    "and future me has left me on read since Tuesday."
)
OUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200


def problems(line):
    """Return a list of every gate rule the line breaks (empty = valid)."""
    found = []
    if not line:
        found.append("line is empty")
    if len(line) > MAX_CHARS:
        found.append(f"line is {len(line)} characters, over the {MAX_CHARS} limit")
    if line != line.strip():
        found.append("line has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        found.append("line spans more than one line")
    bad = [repr(ch) for ch in line if ord(ch) < 32 or ord(ch) == 127]
    if bad:
        found.append(f"line holds control characters: {', '.join(bad)}")
    return found


def write_and_check(line):
    """Write the line plus a trailing newline, then verify the bytes."""
    payload = (line + "\n").encode("utf-8")
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_bytes(payload)
    if OUT_PATH.read_bytes() != payload:
        raise SystemExit("written file did not round-trip exactly")
    return len(payload)


def main():
    issues = problems(EXCUSE)
    if issues:
        raise SystemExit("excuse fails the gate: " + "; ".join(issues))
    written = write_and_check(EXCUSE)
    print(f"wrote {len(EXCUSE)} characters ({written} bytes) to {OUT_PATH}")


if __name__ == "__main__":
    main()
