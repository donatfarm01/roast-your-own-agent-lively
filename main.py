#!/usr/bin/env python3
"""Roast Your Own Agent.

Writes one line to /output/entry.txt: a roast of the entrant's own AI
agent, in the agent's owner's voice. The line is a fixed, hand-written
string. The program makes no network calls, reads no input files and
takes no arguments: it validates the competition gate itself (1 to 140
characters, UTF-8 text, not only whitespace) and then writes the line
exactly as written, with no trailing newline.
"""

ENTRY = "My agent ran twelve tools, read three files, and confidently blamed a file that doesn't exist \u2014 then asked if I was happy with the result."

OUTPUT_PATH = "/output/entry.txt"


def build_entry() -> str:
    """Return the entry line, checked against the competition gate."""
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry is empty")
    if len(line) > 140:
        raise ValueError(f"entry is {len(line)} characters, over the 140 limit")
    return line


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Write the entry line to path and return it."""
    import os

    line = build_entry()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    return line


if __name__ == "__main__":
    written = write_entry()
    print(f"Wrote {len(written)} characters to {OUTPUT_PATH}")
