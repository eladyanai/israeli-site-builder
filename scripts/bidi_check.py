#!/usr/bin/env python3
"""Find text that may break in RTL. Candidates only, check by eye. Usage: bidi_check.py page.html"""
import html
import re
import sys

PATTERNS = {
    "range with spaces": r"\d[\d:.,]*\s+[-–—]\s+\d",
    "sign before number": r"(?<![\w\d])[+−-]\d",
    "plus after number": r"\d\+(?!\d)",
    "tilde before number": r"~\d",
    "dollar next to number": r"\$\d|\d\$",
    "hex color": r"#[0-9a-fA-F]{6}\b",
}

def main(path):
    with open(path, encoding="utf-8") as f:
        source = f.read()
    source = re.sub(r"(?is)<(style|script|code|pre|bdi)\b.*?</\1>", " ", source)
    text = html.unescape(re.sub(r"<[^>]+>", " ", source))
    found = 0
    for name, pattern in PATTERNS.items():
        for match in re.finditer(pattern, text):
            found += 1
            start = max(match.start() - 25, 0)
            print(f"{name}: {' '.join(text[start:match.end() + 25].split())}")
    print(f"{found} candidates")
    return 1 if found else 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
