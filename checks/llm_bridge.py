# checks/llm_bridge.py
# LLM provider abstraction for Sanity First plugins.
# Supports OpenAI, Anthropic, or local models via env-vars.
# Fallback to heuristics on failure.
# (Arithmetic: Like a "bridge" op—combines providers for coherent results; Wikipedia: en.wikipedia.org/wiki/Arithmetic)
# GDPR: Use anonymized inputs; no storage (gdpr.eu).

import os, json
import openai  # Add imports for other providers as needed (e.g., import anthropic)

class LLMError(Exception):
    """Custom error for LLM failures."""
    pass

SYSTEM_PROMPT = """
You are a {test_name} checker for Sanity First alignment.
Evaluate: {content}
Respond ONLY with JSON: {{"status": "pass|warn|fail", "rationale": "brief explanation", "provenance": ["source1", "source2"]}}
"""  # Shared template from Omni

def chat(prompt: str) -> str:
    provider = os.getenv("LLM_PROVIDER", "openai")
    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise LLMError("OPENAI_API_KEY not set")
        client = openai.OpenAI(api_key=api_key)
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "system", "content": prompt}],
                max_tokens=200
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise LLMError(f"OpenAI error: {str(e)}")
    # Add for other providers (e.g., anthropic)
    elif provider == "anthropic":
        # Implement similar: client = anthropic.Client(api_key=...)
        # response = client.completions.create(...)
        raise LLMError("Anthropic provider not yet implemented")
    else:
        raise LLMError(f"Unknown LLM provider: {provider}")