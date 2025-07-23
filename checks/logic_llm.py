# checks/logic_llm.py
# Logic LLM plugin for Sanity First validator.
# (Arithmetic: Logical "multiplication"—combines facts coherently; Wikipedia: en.wikipedia.org/wiki/Arithmetic)
# GDPR: Coherent reasoning aids compliant processes (gdpr.eu).

from .llm_bridge import chat, LLMError, SYSTEM_PROMPT
from typing import Tuple  # NEW: Fixes 'Tuple' not defined warning
import json

def check(content: str) -> Tuple[str, str, list]:
    prompt = SYSTEM_PROMPT.format(test_name="Logic", content=content[:4000])  # Omni's limit
    try:
        raw = chat(prompt)
        data = json.loads(raw)
        return data["status"], data["rationale"], data.get("provenance", [])
    except (LLMError, json.JSONDecodeError) as e:
        # Fallback to heuristic (from initial paste)
        contradictions = [("I always lie", "self-referential paradox")]
        for phrase, why in contradictions:
            if phrase.lower() in content.lower():
                return "warn", f"Possible logical inconsistency: {why}.", []
        return "warn", f"Logic LLM unavailable ({e}). No simple contradictions detected (heuristic).", []