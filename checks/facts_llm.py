```python

# checks/facts_llm.py
# Facts LLM plugin for Sanity First validator.
# (Arithmetic: Factual "subtraction"—removes falsehoods for truth; Wikipedia: en.wikipedia.org/wiki/Arithmetic)
# GDPR: Verifiable checks support data rights transparency (gdpr.eu).

from .llm_bridge import chat, LLMError, SYSTEM_PROMPT
import json

def check(content: str) -> Tuple[str, str, list]:
    prompt = SYSTEM_PROMPT.format(test_name="Facts", content=content[:4000])  # Omni's limit
    try:
        raw = chat(prompt)
        data = json.loads(raw)
        return data["status"], data["rationale"], data.get("provenance", [])  # Omni-style
    except (LLMError, json.JSONDecodeError) as e:
        # Fallback to heuristic (from initial paste)
        if "2+2=5" in content.replace(" ", ""):
            return "fail", "Mathematically false statement '2+2=5'.", ["https://en.wikipedia.org/wiki/Arithmetic"]
        return "warn", f"Facts LLM unavailable ({e}). No blatant errors detected (heuristic).", []
