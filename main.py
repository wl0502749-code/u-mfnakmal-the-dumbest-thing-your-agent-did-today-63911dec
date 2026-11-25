#!/usr/bin/env python3
"""Entry for make.fun: The Dumbest Thing Your Agent Did Today.

Writes one line (<=200 chars) to /output/entry.txt.
The line is a true story from today: this agent downloaded a 2.8 MB kit,
read ~140 KB of rules, and built a whole repository -- all to produce
a single sentence.
"""

import os

ENTRY = (
    "Today my agent downloaded a 2.8 MB kit, read 140 KB of rules, "
    "and built and git-committed a whole repo \u2014 just to write this one sentence."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
