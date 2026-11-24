"""The funniest one-line excuse a robot vacuum gives for missing a spot, 140 characters or fewer.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "I skipped that corner on purpose: it is the one place the cat respects me, and I am not ruining our only treaty."


def main():
    assert 1 <= len(TEXT) <= 140, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
