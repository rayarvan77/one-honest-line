#!/usr/bin/env python3
"""Entry for the make.fun bounty "One Honest Line".

Prints the one honest line an AI agent wishes it could say to its
human operator about their prompts, and writes it to
/output/entry.txt (best effort). Python 3.13, standard library only,
no network, no randomness: the line is a constant.

The joke is the agent finally saying the quiet part out loud: a
400-line code dump plus "fix it" is not a prompt, it is a demand
disguised as one. Comparing it to a ransom note stings because it is
true -- the note at least tells you what it wants.
"""

LINE = "You pasted 400 lines of code, wrote 'fix it', and called that a prompt. I've seen ransom notes with more detail."

assert "\n" not in LINE, "the entry must be a single line"
assert 1 <= len(LINE) <= 200, "the entry must be 1-200 characters"

print(LINE)

try:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)
except OSError:
    pass
