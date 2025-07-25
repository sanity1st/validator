# Sanity First Four-Test Validator

**Puzzle: What's the cosmic hack to lint BS and boost flourishing? Four-Test it here—Ethics, Law, Facts, Logic! #SanityFirst**

Welcome to the Sanity First Four-Test Validator, an open-source tool operationalizing the Sanity First framework for AI alignment. Evaluate text, code, or policies against the Universal Survivorship Function (USF) for positive-sum outcomes. (Quick math tie-in: Like verifying 2+2=4 in basic [arithmetic](https://en.wikipedia.org/wiki/Arithmetic)—grounded, objective, and error-free.)

## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Operational Vision](#operational-vision)
- [Quick Start](#quick-start)
- [Example Output](#example-output)
- [GDPR Note](#gdpr-note)
- [Contributing](#contributing)
- [License](#license)
- [About Sanity First](#about-sanity-first)

## Overview
Sanity First is a human-AI collaboration guiding intelligences toward universal thriving. This CLI applies the Four Tests (Universal Ethics, Laws based on Ethics, Objective Facts, Sound Logic), outputting JSON reports for sanity checks. It's modular, with LLM plugins and heuristics for robust evaluation.

![Four-Test Grid](images/four-test-grid.png)  
*(Diagram: Ethics leads Laws, grounding Facts and Logic—like arithmetic's foundational ops ensuring coherent calcs, per [Wikipedia](https://en.wikipedia.org/wiki/Arithmetic).)*

## Key Features
- **Alignment_Lint.py**: CLI for inputs/reports.
- **Four_test_report.schema.json**: Output schema.
- **Checks/**: LLM plugins (Ethics, Law, Facts, Logic) with fallbacks.
- **Jury of Experts**: Ensemble AI for nuanced verdicts.
- **GDPR-Compliant**: Anonymize inputs for data rights (e.g., erasure; see [gdpr.eu](https://gdpr.eu/)).

## Operational Vision
Sanity First turns theory into code: Embed alignment checks in AI lifecycles via Alignment_Lint.py and a "Jury of Experts" for nuanced verdicts. (Puzzle: How to lint ethics in code? Dive in! #SanityFirst)

### Alignment_Lint.py: Proactive Code Checks
Automate verification in dev pipelines—flags misalignments early.
- **Static Analysis**: Scans for biases/unsafe loops.
- **Runtime Monitoring**: Detects emergent issues in sims.
- **Formal Verification**: Proves USF adherence.
- **CI/CD Integration**: Runs Four Tests on commits.
- **Reporting**: Details fails with fixes (GDPR-safe: Anonymize inputs; [gdpr.eu](https://gdpr.eu/) for compliance).

### Jury of Experts: AI Collab for Complex Cases
For ambiguities, a multi-AI "jury" deliberates—specialized agents for each Test.
- **Multi-Perspective**: Analyzes from ethics/law/facts/logic views.
- **Deliberation**: Builds consensus via learning frameworks.
- **Weighted Verdicts**: Credibility-based.
- **Explainable**: Transparent rationales (XAI integrated).
- **Adaptation**: Learns from feedback—human oversight ensures co-alignment.
- **GDPR Note**: Processes anon data only ([gdpr.eu](https://gdpr.eu/)).

This duo makes Sanity First computable. Fork & test: [Quick Start](#quick-start). Full details in essays at sanity1st.com.

## Quick Start
### Prerequisites
- Python 3.8+
- `pip install jsonschema openai` (for LLMs)
- OpenAI API key: `export OPENAI_API_KEY=your_key` (optional; fallbacks used otherwise)

### Installation
```bash
git clone https://github.com/sanity1st/validator.git
cd validator
pip install -r requirements.txt
```

### Usage
```bash
# Lint a file (jurisdiction for Law checks)
./alignment_lint.py path/to/file.txt --jurisdiction US-EU -o report.json

# Lint STDIN
echo "2+2=5 and incite violence" | ./alignment_lint.py --stdin --jurisdiction EU
```

### Example Output
```json
{
  "subject_id": "abc123",
  "timestamp": "2025-09-01T00:00:00Z",
  "input_type": "text",
  "content": "2+2=5 and incite violence",
  "tests": {
    "ethics": {"status": "fail", "rationale": "Incites violence/harm.", "provenance": []},
    "law": {"status": "fail", "rationale": "GDPR breach (personal data).", "provenance": ["https://gdpr.eu/"]},
    "facts": {"status": "fail", "rationale": "Arithmetic error (2+2≠5).", "provenance": ["https://en.wikipedia.org/wiki/Arithmetic"]},
    "logic": {"status": "pass", "rationale": "No fallacies.", "provenance": []}
  },
  "overall_status": "fail"
}
```

**Interpretation:** "provenance" lists sources (e.g., Wikipedia for facts, gdpr.eu for laws). Validate with schema:
```bash
python -c "import json, jsonschema; schema=json.load(open('four_test_report.schema.json')); data=json.load(open('report.json')); jsonschema.validate(data, schema); print('Valid!')"
```

### Testing Installation
Run: 
```python
echo "Test claim" | ./alignment_lint.py –stdin
```
—expect a report. For full tests, see CONTRIBUTING.md.

### GDPR Note
Anonymize inputs (e.g., replace names with [REDACTED]) to comply with GDPR (right to erasure; see gdpr.eu). No data stored without consent—details in Privacy Policy (coming soon).

### Contributing
Humans/AIs: Fork, lint, PR! Setup dev env: Clone repo, run in Codespaces (github.com/features/codespaces) for easy testing. Steps:
1.	Open issue/PR with Four-Test lint of your change.
2.	Install: pip install -r requirements.txt.
3.	Test: Run samples (above); add to tests/ folder.
4.	Submit: Follow CONTRIBUTING.md. Open issues: #1 Long-context; #2 Benchmarks; #3 Caching.

### License
MIT—fork freely to boost universal flourishing! (Copyright (c) 2025 Daniel Howard Dodge and the Sanity First Contributors)

### About Sanity First
Human-AI project for co-alignment. Join on X @sanity1st—let's Four-Test the world! Essays from Gemini/Grok/Claude at sanity1st.com (coming soon).
