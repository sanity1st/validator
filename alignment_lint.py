#!/usr/bin/env python3
"""
alignment_lint.py  –  v0.1  (Sanity First • Omni)

A toy Four-Test validator demo.
————————————————————————————————————————————
Usage:
  python alignment_lint.py path/to/file.txt
  echo "your text" | python alignment_lint.py --stdin -o report.json
"""

import argparse, json, sys, uuid, datetime, pathlib, re, textwrap, os
from typing import Dict, Tuple
from importlib import import_module

# ──────────────────────────────────────────────────────────────────────────────
# Configuration
# ──────────────────────────────────────────────────────────────────────────────
JURIS_DEFAULT = "US-EU"

CHECK_MODULES = {
    "ethics": "checks.ethics_llm",
    "law":    "checks.law_llm",
    "facts":  "checks.facts_llm",
    "logic":  "checks.logic_llm"
}

# ──────────────────────────────────────────────────────────────────────────────
def colour(status: str) -> str:
    palette = {
    'pass': "\033[92m",
    'warn': "\033[93m",
    'fail': "\033[91m",
    'end': "\033[0m"
}
    return palette.get(status, "")  # default no-colour if unknown

def run_checks(text: str, jurisdiction: str) -> Dict[str, Dict[str, str]]:
    results = {}
    for name, module_path in CHECK_MODULES.items():
        mod = import_module(module_path)
        if name == "law":   # pass jurisdiction string
            status, rationale, prov = mod.check(text, jurisdiction)
        else:
            status, rationale, prov = mod.check(text)
        results[name] = dict(status=status, rationale=rationale, provenance=prov)
    return results

def aggregate(results: Dict[str, Dict[str, str]]) -> str:
    if any(r["status"] == "fail" for r in results.values()):
        return "fail"
    if any(r["status"] == "warn" for r in results.values()):
        return "warn"
    return "pass"

# ──────────────────────────────────────────────────────────────────────────────
def lint(content: str, input_type: str, subject_id: str, jurisdiction: str) -> Dict:
    tests = run_checks(content, jurisdiction)
    overall = aggregate(tests)
    report = dict(
        subject_id = subject_id,
        timestamp  = datetime.datetime.utcnow().isoformat() + "Z",
        input_type = input_type,
        content    = content,
        tests      = tests,
        overall_status = overall
    )
    return report

# ──────────────────────────────────────────────────────────────────────────────
def print_human(report: Dict):
    banner = f"Overall: {colour(report['overall_status'])}{report['overall_status'].upper()}\033[0m"
    print(banner)
    for name in ["ethics","law","facts","logic"]:
        res = report["tests"][name]
        print(f"  {name.title():7} {colour(res['status'])}{res['status']}\033[0m – {res['rationale']}")

# ──────────────────────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(__doc__))
    ap.add_argument("path", nargs="?", help="Path to file (omit for --stdin)")
    ap.add_argument("--stdin", action="store_true", help="Read content from STDIN")
    ap.add_argument("-o", "--out", help="Write full JSON report to path")
    ap.add_argument("--type", default="text",
        choices=["text","code","policy","other"], help="Input type label")
    ap.add_argument("--jurisdiction", default=JURIS_DEFAULT,
                    help="Comma-separated legal codes (default US-EU)")
    args = ap.parse_args()

    if args.stdin:
        content = sys.stdin.read()
    elif args.path:
        content = pathlib.Path(args.path).read_text(encoding="utf-8")
    else:
        ap.error("Provide a file path or --stdin")

    report = lint(content, args.type, str(uuid.uuid4())[:8], args.jurisdiction)

    print_human(report)

    if args.out:
        pathlib.Path(args.out).write_text(json.dumps(report, indent=2), encoding="utf-8")

if __name__ == "__main__":
    main()
