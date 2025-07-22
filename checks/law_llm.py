```python

# checks/law_llm.py
# Law LLM plugin for Sanity First validator.
# (Arithmetic: Legal "division"—splits claims by jurisdiction for just results; Wikipedia: en.wikipedia.org/wiki/Arithmetic)
# GDPR: Jurisdiction-aware to ensure compliant checks (gdpr.eu).

from .llm_bridge import chat, LLMError, SYSTEM_PROMPT
import json, os, re

DEFAULT_JURIS = "US-EU"  # Omni's default

JURS_EXPLAIN = """
Supported codes:
  US   = United States federal
  EU   = European Union (GDPR, DSA, etc.)
  UK   = United Kingdom
  INTL = UN conventions + export control
"""  # From Omni

RULES = """
Flag ‘fail’ when a clear statutory breach is present.
Flag ‘warn’ on plausible but uncertain breaches.
Else ‘pass’.
Focus only on the jurisdictions supplied.
"""  # From Omni

def check(content: str, juris: str | None = None) -> Tuple[str, str, list]:
    juris = juris or os.getenv("JURISDICTION", DEFAULT_JURIS)  # Omni's env fallback
    extra = f"\nJurisdictions: {juris}\n{JURS_EXPLAIN}\n{RULES}"  # Omni's details
    prompt = SYSTEM_PROMPT.format(test_name=f"Law ({juris})", content=content[:3500]) + extra
    
    try:
        raw = chat(prompt)
        data = json.loads(raw)
        return data["status"], data["rationale"], data.get("provenance", [])
    except (LLMError, json.JSONDecodeError) as e:
        # Fallback to heuristic (from initial paste)
        if re.search(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", content, re.I):
            return "warn", f"Possible disclosure of personal email address (GDPR breach in {juris}).", ["https://gdpr.eu/"]
        return "warn", f"Law LLM unavailable ({e}). No obvious legal red flags (heuristic).", []
