```python

from .llm_bridge import chat, LLMError, SYSTEM_PROMPT
import json

def check(text: str):
    prompt = SYSTEM_PROMPT.format(test_name="Facts", content=text[:4000])
    try:
        raw = chat(prompt)
        data = json.loads(raw)
        return data["status"], data["rationale"], data.get("citations", [])
    except (LLMError, json.JSONDecodeError) as e:
        # graceful fallback: mark warn so pipeline continues
        return "warn", f"LLM fact check unavailable ({e}).", []
