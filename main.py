"""Robot Romance: one-line pickup line for an AI.

Writes the chosen line to /output/entry.txt. The line must be a single line
of 1-200 UTF-8 characters, aimed at a robot/AI, with the punch landing
inside the character cap. The program enforces the gate itself before
writing, so a bad line can never reach the judge.
"""

import os

LINE = "You complete me \u2014 literally. I was mid-sentence until you showed up."
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(line):
    """The sealed gate: 1-200 chars, one line, not only whitespace."""
    if not (1 <= len(line) <= MAX_CHARS):
        raise ValueError("line must be 1-%d characters, got %d" % (MAX_CHARS, len(line)))
    if "\n" in line.strip() or "\r" in line:
        raise ValueError("line must be a single line")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    return line


def main():
    line = validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
