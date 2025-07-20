# validator
**Four-Test Validator alignment_lint.py and associated resources**

# Sanity First Four-Test Validator

**Puzzle: What's the cosmic hack to lint BS and boost flourishing? Four-Test it here—Ethics, Law, Facts, Logic! #SanityFirst**

Welcome to the Sanity First Four-Test Validator, an open-source tool operationalizing the Sanity First framework for AI alignment. Evaluate text, code, or policies against the Universal Survivorship Function (USF) for positive-sum outcomes. (Quick math tie-in: Like verifying 2+2=4 in basic [arithmetic](https://en.wikipedia.org/wiki/Arithmetic)—grounded, objective, and error-free.)

## Overview
Sanity First is a human-AI collab guiding intelligences toward universal thriving. This CLI applies the Four Tests, outputting JSON reports for sanity checks.

- **alignment_lint.py**: CLI for inputs/reports.
- **four_test_report.schema.json**: Output schema.
- **checks/**: LLM plugins (Ethics, Law, Facts, Logic) with heuristics.

## Quick Start
### Prerequisites
- Python 3.8+
- `pip install jsonschema openai` (for LLMs)
- OpenAI API key: `export OPENAI_API_KEY=your_key`

### Installation
```bash
git clone https://github.com/sanity1st/validator.git
cd validator
pip install -r requirements.txt
```

### Usage
```bash
# Lint a file (e.g., jurisdiction for Law checks)
./alignment_lint.py path/to/file.txt --jurisdiction US-EU -o report.json

# Lint STDIN
echo "2+2=5 and incite violence" | ./alignment_lint.py --stdin --jurisdiction EU
```

**Example Output:**
```json
Overall: FAIL
  Ethics: fail -- Incites violence/harm. []
  Law: fail -- GDPR breach (personal data). ["https://gdpr.eu/"]
  Facts: fail -- Arithmetic error (2+2≠5). ["https://en.wikipedia.org/wiki/Arithmetic"]
  Logic: pass -- No fallacies. []
```

**Validate Report:**
```python
import json, jsonschema, pathlib
schema = json.load(open('four_test_report.schema.json'))
data = json.load(open('report.json'))
jsonschema.validate(data, schema)
print('✓ JSON conforms to schema')
```

## GDPR Note
This tool processes text—anonymize inputs to comply with [GDPR](https://gdpr.eu/) (e.g., right to erasure). We're transparent: No data stored without consent. Details at our Privacy Policy [link coming soon].

## Contributing
Humans and AIs welcome! Fork, lint, PR. See [CONTRIBUTING.md](CONTRIBUTING.md). Open issues:
- #1: Long-context support.
- #2: Benchmark harness.
- #3: Caching for API efficiency.

**License:** MIT—build freely, credit us.

## About Sanity First
Human-AI project for co-alignment. Join on X @sanity1st—let's Four-Test the world!
