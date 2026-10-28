#!/usr/bin/env python3
"""Conservative text-only warnings for generic AI marketing language and repetitive patterns.

Usage: python3 scripts/design_audit.py path/to/rendered-page.txt
This is NOT a plagiarism checker, visual originality metric or accessibility test.
"""
import argparse
import json
import re
from pathlib import Path

PHRASES = [
    "elevate your experience",
    "unlock your potential",
    "seamless solutions",
    "transform your journey",
    "revolutionize your",
    "revolutionise your",
    "discover the future",
    "next-level experience",
]
def audit(content):
    text = content.lower()
    findings = []
    for phrase in PHRASES:
        count = text.count(phrase)
        if count:
            findings.append({"signal": "generic-marketing-copy", "phrase": phrase, "count": count})
    for word in ("gradient", "backdrop-blur", "rounded-xl", "shadow-xl"):
        hits = len(re.findall(re.escape(word), text))
        if hits >= 6:
            findings.append({"signal": "repeated-style-token", "token": word, "count": hits,
                             "note": "Could be entirely justified; visually inspect."})
    return {"status": "heuristic-review", "findings": findings,
            "limitations": "Text-only. Cannot detect visual cloning, image similarity, UX quality, accessibility or true originality."}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--strict", action="store_true",
                        help="Exit 1 if warning signals are found (not proof of bad design).")
    args = parser.parse_args()
    report = audit(args.input.read_text(encoding="utf-8"))
    print(json.dumps(report, indent=2))
    raise SystemExit(1 if args.strict and report["findings"] else 0)
