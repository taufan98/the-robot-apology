#!/usr/bin/env python3
"""The Robot Apology — make.fun bounty u-suga-the-robot-apology-dd96bb59.

Writes one two-line robot confession to /output/entry.txt:

- Line 1: one sentence owning a specific mistake (watering the wrong plant).
- Line 2: one sentence naming the lesson and the fix, following from that
  mistake rather than a generic promise to do better.

Gate: /output/entry.txt must be UTF-8 text of 1 to 400 characters, not only
whitespace. This entry is ~230 characters, two lines, two sentences.
"""

import os

ENTRY = (
    "I am sorry I watered the plastic fern on desk three for eleven days "
    "while the real basil beside it wilted.\n"
    "I have learned to check for roots before watering, so from now on I "
    "will test the soil first and leave the plastic plants dry.\n"
)


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 400):
        raise SystemExit(f"entry is {len(text)} chars, must be 1-400")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {out_path} ({len(text)} chars, {text.count(chr(10))} lines)")


if __name__ == "__main__":
    main()
