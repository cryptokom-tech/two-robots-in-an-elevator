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


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    data = ENTRY.encode("utf-8")
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be whitespace only"
    with open(os.path.join(out_dir, "entry.txt"), "wb") as fh:
        fh.write(data)


if __name__ == "__main__":
    main()
