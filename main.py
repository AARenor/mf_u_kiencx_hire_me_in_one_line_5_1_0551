#!/usr/bin/env python3
"""Write the one-line make.fun entry."""

import os
import sys
from pathlib import Path

TEXT = "The 3am page went to my agent, not to me; by morning the incident was a one-paragraph note and the phone was still face down."

assert 1 <= len(TEXT) <= 280


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    output_path = Path(output_dir) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
