"""Two Robots in an Elevator — make.fun bounty entry.

Writes one line of awkward robot elevator small talk to entry.txt
in the output directory ($MAKEFUN_OUTPUT_DIR, default /output).
Deterministic, standard library only, no network.
"""

import os

ENTRY = (
    "My load sensor just shared our combined weight with the elevator. "
    "Let us both pretend it was a whisper."
)


def validate(entry: str) -> bytes:
    """Return the entry as UTF-8 bytes, rejecting anything off-gate.

    Explicit checks instead of asserts, so the gate holds even when
    Python runs with -O: one line, 1-200 characters, not blank.
    """
    if not 1 <= len(entry) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not entry.strip():
        raise ValueError("entry must not be whitespace only")
    return entry.encode("utf-8")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    data = validate(ENTRY)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as fh:
        fh.write(data)


if __name__ == "__main__":
    main()
