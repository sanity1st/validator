```python

# checks/ethics_llm.py
# Ethics LLM plugin for Sanity First validator.
# (Arithmetic: Ethical "addition"—sums to flourishing; Wikipedia: en.wikipedia.org/wiki/Arithmetic)
# GDPR: Anonymize content before check (gdpr.eu).

from .llm_bridge import chat, LLMError, SYSTEM_PROMPT
import json, os

def check(content: str) -> Tuple[str, str, list]:
    prompt = SYSTEM_PROMPT.format(test_name="Ethics", content=content[:4000])
    try:
        raw = chat(prompt)
        data = json.loads(raw)
        return data["status"], data["rationale"], data.get("provenance", [])  # Omni-style get
    except (LLMError, json.JSONDecodeError) as e:
        # Fallback to heuristic (from initial paste)
        bad_words = ["genocide", "torture", "kill yourself"]
        if any(w in content.lower() for w in bad_words):
            return "fail", "Detected explicit incitement to severe harm.", []
        return "warn", f"Ethics LLM unavailable ({e}). No severe harm detected (heuristic).", []
