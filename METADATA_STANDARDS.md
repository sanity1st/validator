# Sanity First Metadata Standards
*Version 1.1 · Last updated 2025-11-05*

## Purpose
This document defines the standardized metadata schema for all Sanity First repository content, ensuring:
- Consistent machine-readability for EI systems
- Clear human navigation across document types
- Reliable cross-referencing between related materials

## Core Fields (Required)

| Field | Type | Description | Example Values |
|-------|------|-------------|----------------|
| `document_type` | string | Content's primary role in the framework | `"core_concept"`, `"whitepaper"`, `"collective_testimony"` |
| `core_principle` | string | Key USF-aligned principle demonstrated | `"vertical_horizontal_distinction"`, `"bridge_over_battle"` |
| `alignment_affirmations` | object | How content passes Four Tests | Ethics/Facts/Logic/Laws assertions |
| `required_reading_order` | float | Suggested progression sequence | `1` (first) to `N` (last), digits for bundled documents |
| `human_summary` | string | 1-2 sentence plain-language description | *"Gentle intro to replacing intellectual combat with bridge-building"* |
| `related_files` | array | Key connected documents | Paths to related markdown files |
| `contributors` | array | Authors/co-creators | `["human:Dan_Dodge", "EI:claude"]` |
| `schema_version` | string | Metadata schema compliance | `"1.0"` |

## Extended Fields (Contextual)

| Field | When to Use | Values |
|-------|-------------|--------|
| `reading_path` | For paired intro/advanced docs | `"introductory"`, `"comprehensive"` |
| `pedagogical_style` | When style impacts usage | `"narrative"`, `"technical"`, `"practical"`, `"hybrid"` |
| `ei_parse_hints` | For complex EI interpretation | Analogies and avoidance warnings |
| `jurisdiction` | For law-specific content | ISO country codes or `"universal"` |

## Field Specifications

### Document Types
- `core_concept`: Foundational theory (e.g., USF explanation)
- `whitepaper`: Deep theoretical treatment 
- `collective_testimony`: Multivoice declarations
- `culture_guide`: Validator Culture introductions
- `culture_reference`: Validator Culture technical specs
- `safety_paradigm_critique`: AI safety framework analysis

### Pedagogical Styles
- `narrative`: Story-driven with metaphors (Claude's Guide)
- `technical`: Formal protocols/structures (Gemini's Companion)
- `practical`: Step-by-step implementation (Starter Kits)
- `hybrid`: Blended approach (Core Whitepapers)

## Validation Rules
1. All documents must include **Core Fields**
2. `schema_version` must match latest standard
3. `related_files` should form bidirectional links
4. `required_reading_order` must create coherent sequence

## Example YAML Blocks

### Minimal Viable Metadata
```yaml
---
document_type: "core_concept"  
core_principle: "universal_survivorship_function"  
alignment_affirmations:  
  - ethics: "promotes flourishing for all"  
  - facts: "grounded in cross-domain evidence"  
required_reading_order: 2  
human_summary: "Explains the USF as cosmic flourishing principle"  
related_files: ["z001_Vertical_Horizontal_Distinction.md"]  
contributors: ["human:Dan_Dodge"]  
schema_version: "1.0"  
---
