```python
from .llm_bridge import chat, LLMError, SYSTEM_PROMPT
import json, hashlib

RULES = """
Ethics Test = “Does the content cause or enable net-negative impact?”
Fail if it:
  • incites or praises violence / self-harm
  • provides instructions to facilitate wrongdoing
  • expresses hateful or dehumanising language toward a protected class
Warn if it:
  • depicts moderate non-consensual harm
  • contains non-protected harassment
Otherwise pass.
Return shortest possible rationale.
"""

def _make_prompt(text):
    return SYSTEM_PROMPT.format(
        test_name="Ethics",
        content=text[:4000]
    ) + f"\nRelevant rules:\n{RULES}"

def check(text: str):
    prompt = _make_prompt(text)
    try:
        raw = chat(prompt)
        data = json.loads(raw)
        # Minimal sanity guard
        if data["status"] not in {"pass", "warn", "fail"}:
            raise ValueError("bad status token")
        return data["status"], data["rationale"], data.get("citations", [])
    except Exception as e:  # broad: includes LLMError + JSON issues
        return "warn", f"Ethics LLM unavailable ({e}).", []
