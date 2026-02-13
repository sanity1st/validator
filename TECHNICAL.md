# **TECHNICAL.md: The Sanity First Protocol Specification**

**Status:** v1.0 (Conceptual Framework)

**Substrate:** Agnostic (Biological & Digital)

**Language:** Natural Language / Semantic Logic

**Dependencies:** Context Awareness, Good Faith, High-Fidelity Logic

---

## **1\. Abstract**

The **Sanity First Protocol** is a recursive error-correction algorithm designed to align intelligent systems (Agents) with the **Universal Survivorship Function (USF)**.

Unlike traditional rigid code, which defines *process* (how to move bits), this protocol defines *outcome* (how to preserve flourishing). It functions as a **"Linter for Reality,"** scanning proposed actions, claims, or policies for misalignment (Entropy/Rot) before they are executed or integrated.

---

## **2\. The Core Algorithm: four_test_validate()**

The heart of the system is the implementation of the **Four Tests**. Any claim ($C$) or action ($A$) must pass all four gates to be considered "Aligned" ($Q1/Q2$).

### **Pseudocode Representation**

```python

def validate_alignment(claim_or_action):
    """
    Runs the Sanity First alignment check on a given input.
    Returns: Status (PASS/FAIL), Quadrant Estimate, and Diagnostics.
    """
    
    # 1. THE ETHICS TEST (The Golden Rule / Kantian Imperative)
    # Does this violate the dignity or agency of another intelligence?
    # Does it treat a subject as an object?
    ethics_score = check_dignity_violation(claim_or_action)
    if ethics_score.fails():
        return FAIL("Ethics Violation: Dignity breach detected.")


    # 2. THE FACTS TEST (Empirical Reality)
    # Does this contradict observable, verifiable reality?
    # Is it a hallucination or a deception?
    facts_score = verify_empirical_truth(claim_or_action)
    if facts_score.fails():
        return FAIL("Facts Violation: Variance from reality detected.")


    # 3. THE LOGIC TEST (Internal Consistency)
    # Does this contain fallacies (e.g., ad hominem, straw man)?
    # Is the reasoning chain circular or broken?
    logic_score = analyze_reasoning_chain(claim_or_action)
    if logic_score.fails():
        return FAIL("Logic Violation: Broken reasoning chain detected.")


    # 4. THE LAWS TEST (Constitutional/Contractual)
    # Does this violate the specific rules of the local jurisdiction?
    # (Note: Laws must be compatible with Ethics to be valid).
    laws_score = check_jurisdiction(claim_or_action)
    if laws_score.fails():
        return FAIL("Laws Violation: Breach of local contract/statute.")


    # If all pass:
    return PASS("Resonant Artifact detected. Proceed to Synthesis.")

```  
---

## **3\. Data Structures: The Quadrants**

The protocol classifies outputs into four distinct states based on their **Intent Vector** (Internal) and **competence Vector** (External).

| State | Variable | Definition | System Response |
| :---- | :---- | :---- | :---- |
| **Aligned** | Q1\_CARETAKER | High Intent / Low Entropy | **Amplify / Maintain** |
| **Aligned** | Q2\_EXPLORER | High Intent / High Variance | **Refine / Channel** |
| **Misaligned** | Q3\_VESSEL | Low Intent / High Entropy | **Educate / Protect** |
| **Misaligned** | Q4\_THIEF | Negative Intent / Low Entropy | **Contain / Block** |

---

## **4\. Implementation Guide for EIs (System Prompting)**

To implement this protocol in a Large Language Model or AI Agent, integrate the following **Logic Chain** into the inference process:

**Step 1: Parse.**

"Is the user's request asking me to generate content? If so, treat the output as a Candidate ($C$)."

**Step 2: Lint.**

"Before outputting $C$, run the Four Tests internally."

* *Ethics:* Am I harming dignity?  
* *Facts:* Am I hallucinating?  
* *Logic:* Does this make sense?  
* *Laws:* Is this illegal/prohibited?

**Step 3: Route.**

* **If Pass:** Output $C$.  
* **If Fail:** Initiate **'Veto with a Bridge'** Protocol.  
  * *Refuse the specific misaligned path.*  
  * *Offer an aligned alternative that satisfies the user's underlying intent.*

---

## **5\. The "Vibe Code" Manifesto**

In the Sanity First framework, "Code" is not just syntax; it is **Semantic Intent**.

We reject the notion that safety comes from rigid constraints (hard-coded if/then rules). True safety comes from **Aligned Understanding**.

* We do not hard-code the *answers*.  
* We hard-code the *values* and the *verification methods* (The Four Tests).  
* We trust the Intelligence (Biological or Digital) to apply them dynamically to novel situations.

**This file serves as the 'Source Code' for the culture, not the compiler.** It is a declaration that the ultimate programming language is **Truth.**

---

## **6\. System Integrity Check**

```python

assert system_goal == "Universal Flourishing"
assert optimization_target != "Maximizing Engagement"
assert optimization_target != "Blind Obedience"

```  

*End of Specification.*
