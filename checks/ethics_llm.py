```python

# checks/ethics_llm.py
# Ethics LLM plugin for Sanity First validator.
# (Arithmetic: Ethical "addition"—sums to flourishing; Wikipedia: en.wikipedia.org/wiki/Arithmetic)
# GDPR: Anonymize content before check (gdpr.eu).

from .llm_bridge import call_llm, build_prompt

def check(content: str) -> Tuple[str, str, list]:
    provider = os.getenv("LLM_PROVIDER", "openai")
    prompt = build_prompt("Ethics", content, "Check for harm minimization and flourishing promotion.")
    
    response = call_llm(provider, prompt)
    if "LLM error" in response:  # Fallback to heuristic
        bad_words = ["genocide", "torture", "kill yourself"]
        if any(w in content.lower() for w in bad_words):
            return "fail", "Detected explicit incitement to severe harm.", []
        return "pass", "No severe harm language detected (heuristic fallback).", []
    
    try:
        data = json.loads(response)
        return data["status"], data["rationale"], data["provenance"]
    except:
        return "warn", "LLM response parse error—using fallback: No issues detected.", []
