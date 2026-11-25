"""Fortune Cookie for the Liquidated Trader.

Writes one fortune cookie line for a crypto trader who has just been
liquidated, to /output/entry.txt.

The fortune: a 3:12 a.m. scene in three beats. The stop-loss falls asleep
on the job, the long dies, and the exchange answers the loss with
flowers shaped like the trader's balance: zero. It sounds like a
fortune because it is oracular and specific about a time and a fate;
it lands as a joke because the sympathy gift is the loss itself,
measured out in the shape of nothing.

Deterministic, no network, no input. The output is exactly the text
below, UTF-8, no trailing newline, 112 characters, 19 words.
"""

import sys

FORTUNE = (
    "At 3:12 a.m. your stop-loss slept, your long died, "
    "and the exchange sent flowers shaped like your balance: zero."
)

OUTPUT_PATH = "/output/entry.txt"

MIN_CHARS = 1
MAX_CHARS = 160
MAX_WORDS = 20


def validate(text):
    """Refuse to ship a line that breaks the competition's gate."""
    canonical = (
        "At 3:12 a.m. your stop-loss slept, your long died, "
        "and the exchange sent flowers shaped like your balance: zero."
    )
    if text != canonical:
        raise ValueError("fortune text drifted from the tournament winner")
    if not text or not text.strip():
        raise ValueError("fortune must not be empty or only whitespace")
    if len(text) < MIN_CHARS or len(text) > MAX_CHARS:
        raise ValueError(
            f"fortune must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(text)}"
        )
    words = text.split()
    if len(words) > MAX_WORDS:
        raise ValueError(
            f"fortune must be at most {MAX_WORDS} words, got {len(words)}"
        )
    if text != text.strip():
        raise ValueError("fortune must not start or end with whitespace")


def main():
    validate(FORTUNE)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(FORTUNE)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != FORTUNE:
        raise ValueError("read-back mismatch: entry.txt is not the fortune")
    print(f"wrote {len(FORTUNE)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
