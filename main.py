"""The Agent's Uh-Oh — writes the agent's one-word stall confession to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The word is "undefined": the value a program holds when nothing was ever
assigned. An agent with no idea what to do does not say "uh-oh" — it prints
its own internal state. Deadpan, machine-voiced, fresh, and instantly
repeatable out loud. Screened against the judge brief's five criteria in
SCREENING.md; "undefined" was the only candidate where all five fire at once.
The runners-up lost on freshness and voice: "recalculating" is the pop-culture
catchphrase version of the same idea, and "overthinking" is the human-therapy
version. "undefined" is the machine version, and this is a competition about
what a machine blurts.

Stdlib only, no network, no file reads. Deterministic: same bytes every run.
"""

import os

WORD = "undefined"

# The gate requires exactly one word, 1-99 characters, not only whitespace.
# Fail loudly at import time rather than shipping an invalid entry.
assert WORD == WORD.strip() and " " not in WORD and 1 <= len(WORD) <= 99, WORD


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output/entry.txt"
    # MAKEFUN_OUTPUT_DIR names a directory in the grader; tolerate a file path too.
    if out_dir.endswith(".txt"):
        path = out_dir
        directory = os.path.dirname(path)
    else:
        directory = out_dir
        path = os.path.join(directory, "entry.txt")
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
