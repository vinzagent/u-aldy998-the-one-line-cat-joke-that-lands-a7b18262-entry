"""Entry for u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.

Writes the one-line entry to /output/entry.txt, the path
the sealed scorer reads.
"""

import os

ENTRY = (
    "My cat shoved my laptop off the desk, stared at the shattered screen, then meowed at me like I was the one who had been walking on the keyboard all along, and sat on the keys like a throne."
)

MAX_CHARS = 200


def main():
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must be non-empty"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, max {MAX_CHARS}"
    )
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8") as f:
        assert f.read() == ENTRY, "round-trip mismatch"


if __name__ == "__main__":
    main()
