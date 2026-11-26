"""Deadpan forecast for Gloombury, a city that does not exist.

Writes one line (148 chars, gate 1-160) to /output/entry.txt,
deterministically: temp file in the same directory, os.replace,
chmod 644. Stdlib only.
"""

import os

ENTRY = (
    "Tonight in Gloombury: overcast with a 90% chance of sideways rain, "
    "lows of 4 degrees, and one cloud that has been following the mayor "
    "since Tuesday."
)


def main():
    # Gate self-check: the sealed scorer wants 1-160 chars, non-blank.
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, final_path)
    os.chmod(final_path, 0o644)


if __name__ == "__main__":
    main()
