#!/usr/bin/env python3
"""Extract the N most recent entries (by year) from a .bib file."""
import re
import sys


def split_entries(text):
    entries = []
    i = 0
    n = len(text)
    while True:
        start = text.find("@", i)
        if start == -1:
            break
        brace = text.find("{", start)
        depth = 0
        j = brace
        while j < n:
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        entries.append(text[start:j + 1])
        i = j + 1
    return entries


def entry_year(entry):
    m = re.search(r"year\s*=\s*\{?(\d{4})\}?", entry)
    return int(m.group(1)) if m else 0


def main():
    n = int(sys.argv[1])
    src, dst = sys.argv[2], sys.argv[3]
    with open(src) as f:
        text = f.read()
    entries = split_entries(text)
    entries.sort(key=entry_year, reverse=True)
    with open(dst, "w") as f:
        f.write("\n\n".join(entries[:n]) + "\n")


if __name__ == "__main__":
    main()
