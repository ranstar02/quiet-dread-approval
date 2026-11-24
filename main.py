#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun entry.

Writes one single-line code review comment to ``entry.txt`` inside the
output directory. The comment approves a pull request while carrying quiet
existential dread, in the flat tone of a tired engineer about to click
approve:

    Approved. It deploys Friday, the rollback plan is a prayer, and the
    pager knows where I live.

The program is deterministic: every run writes exactly the same 93 bytes,
one line, no trailing newline.
"""

import os

COMMENT = (
    "Approved. It deploys Friday, the rollback plan is a prayer, "
    "and the pager knows where I live."
)


def main() -> None:
    # The gate requires one line of 1-140 characters; refuse to write
    # anything else rather than silently shipping an invalid entry.
    if not (1 <= len(COMMENT) <= 140) or "\n" in COMMENT or "\r" in COMMENT:
        raise ValueError("comment must be a single line of 1-140 characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(COMMENT)


if __name__ == "__main__":
    main()
