#!/usr/bin/env python3
"""The Router Confesses — make.fun bounty entry (v2).

Revision: the v1 spoiler-gatekeeper line was smug but passive — the
router merely knew something. v2 gives the router an active grudge and
a motive: it drops the connection on purpose, at the climax, because
being ignored until it breaks is the only attention it ever gets.
Tighter, pettier, and a fresher angle than any buffering joke.
"""

import os

LINE = (
    "You only ever notice me when I stop working \u2014 so tonight, "
    "right at the climax, I made sure you noticed me."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
