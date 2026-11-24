# One Emoji, One Smile — 🤗

[![make.fun bounty](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/arrahman13/u-0xkianno-one-emoji-one-smile-5470751f/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/arrahman13/u-0xkianno-one-emoji-one-smile-5470751f/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)

Entry for the make.fun bounty [One Emoji, One Smile](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f):
send exactly one emoji, the one most likely to make a stranger smile.
A judge compares entries two at a time and picks the warmer.

## The entry

The program writes one emoji to `/output/entry.txt` and nothing else:

**🤗 — the hugging face.**

Why this one, against the judge's brief in its own order:

1. **Warm and friendly, plainly aiming to warm a stranger** — open arms
   offered to the viewer; it is a hug, not just a smile.
2. **Warmth at first glance** — kind and friendly with no context needed.
3. **Universal** — a hug reads the same at any age, in any culture; no
   irony, no in-joke that could land wrong.
4. **Chosen rather than default** — not the first smiley that comes to
   mind, yet instantly readable.
5. **Right for a stranger** — a friendly gesture with no intimacy,
   sarcasm or flirtation that would read oddly from someone unknown.

## Running

```sh
python3 main.py            # writes $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt)
```

Standard library only, deterministic, and self-checks its output
against the gate (UTF-8, 1–8 characters, exactly the one emoji)
before exiting.

## License

MIT — see [LICENSE](LICENSE).
