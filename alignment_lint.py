```python
# add near top
import os
JURIS_DEFAULT = "US-EU"

# update module map
CHECK_MODULES = {
    "ethics": "checks.ethics_llm",
    "law":    "checks.law_llm",
    "facts":  "checks.facts_llm",
    "logic":  "checks.logic_llm"
}

# argparse additions
ap.add_argument("--jurisdiction", default=JURIS_DEFAULT,
                help="Comma-separated legal codes (default US-EU)")

# when calling law check
for name, module_path in CHECK_MODULES.items():
    mod = import_module(module_path)
    if name == "law":   # pass jurisdiction string
        status, rationale, prov = mod.check(content, args.jurisdiction)
    else:
        status, rationale, prov = mod.check(content)
    results[name] = dict(status=status, rationale=rationale, provenance=prov)
