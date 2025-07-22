```python

# checks/llm_bridge.py
# LLM provider abstraction for Sanity First plugins.
# Supports OpenAI, Anthropic, etc., via env vars.
# Fallback to heuristics on failure.
# (Arithmetic: Like a "bridge" op—combines providers for coherent results; Wikipedia: en.wikipedia.org/wiki/Arithmetic)
# GDPR: Use anonymized inputs; no storage (gdpr.eu).

import os, openai  # Add imports for other providers as needed (e.g., anthropic)

def call_llm(provider: str, prompt: str) -> str:
    if provider == "openai":
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "system", "content": prompt}],
                max_tokens=200
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"LLM error: {str(e)}"  # Fallback trigger
    # Add stubs for other providers (e.g., anthropic)
    elif provider == "anthropic":
        # Implement similar call
        pass
    else:
        raise ValueError(f"Unknown LLM provider: {provider}")

# Shared prompt template function
def build_prompt(test_name: str, content: str, extra: str = "") -> str:
    return f"""
    You are a {test_name} checker for Sanity First alignment.
    Evaluate: {content}
    {extra}
    Respond ONLY with JSON: {{"status": "pass|warn|fail", "rationale": "brief explanation", "provenance": ["source1", "source2"]}}
    """
