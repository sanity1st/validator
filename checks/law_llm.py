```python
from .llm_bridge import chat, LLMError, SYSTEM_PROMPT
import json, os

DEFAULT_JURIS = "US-EU"  # comma-sep list of codes

JURS_EXPLAIN = """
Supported codes:
  US   = United States federal
  EU   = European Union (GDPR, DSA, etc.)
  UK   = United Kingdom
  INTL = UN conventions + export control
"""

RULES = """
Flag ‘fail’ when a clear statutory breach is present.
Flag ‘warn’ on plausible but uncertain breaches.
Else ‘pass’.
Focus only on the jurisdictions supplied.
"""

def _make_prompt(text, juris):
    return SYSTEM_PROMPT.format(
        test_name=f"Law ({juris})",
        content=text[:3500]
    ) + f"\nJurisdictions: {juris}\n{JURS_EXPLAIN}\n{RULES}"

def check(text: str, juris: str | None = None):
    juris = juris or os.getenv("JURISDICTION", DEFAULT_JURIS)
    prompt = _make_prompt(text, juris)
    try:
        raw = chat(prompt)
        data = json.loads(raw)
        return data["status"], data["rationale"], data.get("citations", [])
    except Exception as e:
        return "warn", f"Law LLM unavailable ({e}).", []
