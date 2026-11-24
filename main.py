#!/usr/bin/env python3
"""One Emoji, One Smile — entrypoint.

Writes exactly one emoji to <output dir>/entry.txt and nothing else.
The emoji is the hugging face: an open-arms offer of warmth that a
stranger reads as kind and friendly at first glance, with no words,
no caption and no explanation attached.

Output dir: $MAKEFUN_OUTPUT_DIR when set, else /output.
Standard library only; deterministic; no network, no input.
"""

import os
import sys

EMOJI = "\U0001F917"  # HUGGING FACE — one code point, one grapheme.


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # Write the emoji alone: no trailing newline, nothing else.
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(EMOJI)

    # Gate self-check: the file must be UTF-8 text of 1 to 8
    # characters, not only white space, and exactly this one emoji
    # grapheme — one code point, with no combining mark, variation
    # selector or zero-width joiner that could make it count or
    # render as anything more than a single emoji.
    with open(path, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8")
    if text != EMOJI or raw != EMOJI.encode("utf-8"):
        print(f"self-check failed: wrote {text!r}, expected {EMOJI!r}", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 8) or not text.strip():
        print("self-check failed: gate size/blank rule", file=sys.stderr)
        return 1
    if len(text) != 1 or any(ord(c) in (0xFE0F, 0x200D) or 0x300 <= ord(c) <= 0x36F for c in text):
        print("self-check failed: not exactly one grapheme", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
