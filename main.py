#!/usr/bin/env python3
"""Cat-joke entry: one feline one-liner to /output/entry.txt."""

from pathlib import Path

TEXT = "My cat walked across my keyboard at 3 a.m., typed 'mmmmmm', and hit send to my boss — HR asked for the meeting notes, and honestly the cat's draft made more sense than mine."

DEST = Path("/output/entry.txt")


def emit() -> None:
    """Write the single cat joke exactly, readable by any user."""
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(TEXT, encoding="utf-8")
    DEST.chmod(0o644)


if __name__ == "__main__":
    emit()
