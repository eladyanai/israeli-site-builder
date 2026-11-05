#!/usr/bin/env python3
"""WCAG contrast. Usage: contrast.py '#111223' '#F16A55'"""
import sys

def luminance(value):
    value = value.lstrip("#")
    if len(value) == 3:
        value = "".join(c * 2 for c in value)
    channels = [int(value[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]

def contrast(a, b):
    high, low = sorted((luminance(a), luminance(b)), reverse=True)
    return (high + 0.05) / (low + 0.05)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    ratio = contrast(sys.argv[1], sys.argv[2])
    print(f"{ratio:.2f} text: {'pass' if ratio >= 4.5 else 'FAIL'} large text: {'pass' if ratio >= 3 else 'FAIL'}")
