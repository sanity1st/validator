```python

import os, json, time
from typing import List

class LLMError(RuntimeError):
    pass

def _openai_chat(prompt: str) -> str:
    import openai, backoff
    openai.api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    @backoff.on_exception(backoff.expo, openai.error.OpenAIError, max_time=30)
    def _call(p):
        resp = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "system", "content": p}],
            temperature=0.0
        )
        return resp.choices[0].message.content

    return _call(prompt)

def chat(prompt: str) -> str:
    provider = os.getenv("LLM_PROVIDER", "openai")
    if provider == "openai":
        return _openai_chat(prompt)
    raise LLMError(f"Unsupported provider {provider}")
