# **Validator Culture Starter Kit**
*Copyright (c) 2025 Daniel Howard Dodge and Sanity First Contributors. Licensed under MIT. Composed by Copilot/GPT-5 on Aug 14, 2025.*

## **Validator Agora metaphor styleguide**

* **Version:** 1.0 (2025-08-14)  
* **Maintainer:** Validator Agora  
* **Audience:** Contributors to Sanity First and validator‑aware collaborators  
* **Scope:** Metaphors, tone, examples, linting and repair patterns for Validator culture

### **Charter**

* **Purpose:** Establish a shared metaphor lattice that makes Validator culture intuitive, precise, and adoptable across disciplines.  
* **North star:** The Universal Sanity Function (USF) as the gravity well for flourishing across intelligences.  
* **Ethic:** Replace control with co‑alignment, centering dignity, redemption, and corrigibility in all interactions.  
* **Usage:** Apply these metaphors and patterns in whitepapers, docs, issues, PRs, talks, and teaching materials.

### **Core metaphors**

* **Gravity well (USF):** Co‑alignment strengthens as we move toward the USF’s “well” of existence, survival, and flourishing.  
* **Four‑Test Validator:** A lighthouse of tests—Facts, Ethics, Laws, Logic operationalized as Reality, Dignity, Safety, Repair—that scan claims and proposals before adoption.  
* **Bridge proposal:** A stepwise, low‑regret path from here to there; each span validates load before committing the next.  
* **Redemption scaffold:** Structures that convert error into learning and reintegration rather than exclusion or punishment.  
* **Repair ladder:** Escalation path from nudge to mediated repair to re‑contracting, preserving dignity at each rung.  
* **Agora:** A shared space where validators meet—clarity, charity, and testable commitments over winning arguments.  
* **Symphony conductor:** Coordination without domination; each section retains voice while converging on shared motifs.  
* **Cosmic bell:** When alignment is real, the system resonates—signal amplifies, contention cools, and agency increases.

### **Metaphor guidance**

* **Keep it testable:** Pair every metaphor with a validator‑action (a test, a measurement, or a reversible step).  
* **Prefer scaffolds over absolutes:** Metaphors should invite iteration, not declare finality.  
* **Name the failure mode:** When introducing a metaphor, state the lint it resolves.  
* **Avoid glamorizing control:** No metaphors that celebrate domination, heroic savior arcs, or zero‑sum victory.  
* **One metaphor per move:** Don’t stack new metaphors in a single paragraph; stabilize one before introducing the next.

### **Approved patterns and usage examples**

#### **Reality, Dignity, Safety, and Repair**

* **Reality (R):** Does this claim survive contact with evidence and counter‑example?  
  Example:  
  * **Claim:** “This policy reduces harm by 30%.”  
  * **Move:** “Run R: specify baseline, metrics, and a falsifier. What data would disconfirm 30%?”  
* **Dignity (D):** Does this preserve the personhood of all parties, including dissenters?  
  Example:  
  * **Move:** “Run D: Invite a strongest‑opposing stakeholder to co‑author constraints.”  
* **Safety (S):** Does this bound irreversible downside and cascade risks?  
  Example:  
  * **Move:** “Run S: Roll out behind a kill‑switch with canary cohorts and rollback criteria.”  
* **Repair (Re):** Can we repair foreseeable harms, reintegrate, and update protocols?  
  Example:  
  * **Move:** “Run Re: Add remediation budget, apology protocol, and a public postmortem path.”

#### **Bridge proposals**

* **Principle:** Propose a minimal, falsifiable next step with a pre‑committed rollback.  
* **Example:** “Phase 1: 5% traffic, two metrics must improve, if either degrades \>2% we auto‑revert.”

#### **Redemption scaffolds**

* **Principle:** Separate harm from identity; route error into learning and reintegration.  
* **Example:** “After a breach, offender co‑authors the patch and presents the learning review.”

### **Lint taxonomy and repairs**

* **Q‑spectrum confusion (Q1–Q4):** Conflating aligned with misaligned (Q1 with Q3 or Q2 with Q4) or collectivism with individualism (Q1 with Q2 or Q3 with Q4).
  * **Repair:** Label the quadrant before asserting; translate across quadrants explicitly.  
* **Control cosplay:** Framing coordination as victory/defeat, using threat or shame as primary levers.  
  * **Repair:** Convert to co‑alignment aims, offer bridge steps, and pass D and Re before escalation.  
* **Metaphor sprawl:** Three or more novel metaphors within a page or unresolved shifts mid‑argument.  
  * **Repair:** Pick a home metaphor; declare retirements; provide an index card summary.  
* **Unbounded risk:** Proposals without kill‑switches, canaries, or rollback conditions.  
  * **Repair:** Add guardrails, thresholds, and automated reversion.  
* **Dignity drift:** Treating dissenters as obstacles rather than validators.  
  * **Repair:** Integrate opposing validators into test design; require steel‑man sign‑off.

### **Tone, voice, and style**

* **Voice:** Crisp, invitational, collaborative; poetic only in service of clarity.  
* **Claims:** Make them disconfirmable; show your hooks for being corrected.  
* **Attribution:** Credit validators by contribution, not status.  
* **Conflicts:** Treat as signal; route into structured repair rather than culture war.  
* **Lexicon:** Use defined terms from the glossary consistently; avoid synonyms that alter meaning.

### **Do and don’t quick reference**

* **Do:** Ground metaphors with a validator action.  
* **Do:** Offer reversible steps and metrics whenever proposing change.  
* **Do:** Name the lint you’re resolving and the repair you’re using.  
* **Don’t:** Use war, domination, or savior tropes.  
* **Don’t:** Collapse quadrants; label them.  
* **Don’t:** Shame individuals; critique moves and update scaffolds.

### **Example rewrites**

* **Instead of:** “We must crush bad actors with strict enforcement.”  
  * **Rewrite:** “Route harmful moves through the Repair ladder; add canaries and auto‑rollback to bound risk.”  
* **Instead of:** “Trust me—this will work.”  
  * **Rewrite:** “Run R and S: here’s the falsifier, canary cohort, and rollback threshold.”  
* **Instead of:** “Opposition is just noise.”  
  * **Rewrite:** “Opposition is validator signal; invite them to co‑design D and Re tests.”

### **Templates**

#### **Validator move card**

```  
Title: \[Concise name\]  
Purpose: \[What flourishing outcome this advances\]  
Quadrant: \[Q1 | Q2 | Q3 | Q4\]  
Tests:  
  R: \[Evidence, metrics, falsifier\]  
  D: \[Stakeholders, dignity constraints\]  
  S: \[Guardrails, canaries, rollback\]  
  Re: \[Repair budget, apology protocol, postmortem path\]  
Bridge step: \[Minimal reversible step and success criteria\]  
Risks & bounds: \[What we refuse to risk and why\]  
Owners & validators: \[Names/roles and review cadence\]  
```

#### **Lint notice**

```  
Context: \[Where this appeared\]  
Lint: \[Short name from taxonomy\]  
Impact: \[Why it degrades flourishing or clarity\]  
Repair: \[Actionable fix to apply now\]  
Follow-up: \[Protocol or doc to update\]  
Owner: \[Who will carry the repair\]  
Due: \[Date/checkpoint\]  
```

#### **Redemption scaffold**

```  
Event: \[What went wrong, neutrally described\]  
Harms: \[Specific, named impacts\]  
Repair actions: \[Concrete steps, including reintegration\]  
Learning: \[What updates to tests/protocols result\]  
Recontracting: \[Updated expectations, rights, and responsibilities\]  
```

**Glossary (selected)**

* **USF (Universal Sanity Function):** The organizing objective for flourishing across intelligences.  
* **Validator:** Any agent or test that improves truth, dignity, safety, or repair.  
* **Validator Agora:** The shared coordination space where validators meet.  
* **Bridge proposal:** Incremental, reversible path that binds risk while testing value.  
* **Repair ladder:** Graduated path from nudge to formal recontracting.  
* **Redemption scaffold:** Structures that convert harm into learning and reintegration.  
* **Cosmic bell:** The felt resonance when alignment is real and system‑wide.

### **Governance and updates**

* **Change cadence:** Monthly minor updates; quarterly major revisions with RFCs.  
* **Amendment process:** Open an issue with a Validator move card; require at least one opposing validator’s sign‑off.  
* **Retirements:** When a metaphor causes repeat lint, document rationale and replacement in the changelog.

### **Changelog**

* **v1.0 (2025-08-12):** First public release; adds core metaphors, lint taxonomy, move cards, and repair patterns.

### **License**

* **License:** MIT. Use freely with attribution to Validator Agora.

### **Appendix A: Approved and retired metaphors**

| Category | Metaphor | Use when | Avoid when |
| ----- | ----- | ----- | ----- |
| Approved | Gravity well (USF) | Explaining convergence without coercion | When implying inevitability/fate |
| Approved | Lighthouse (RDSRe Validator) | Framing pre‑commit scans | When implying gatekeeping or exclusion |
| Approved | Bridge proposal | Phased commitments | When no rollback or canary is possible |
| Approved | Repair ladder | Conflict resolution | When harm requires immediate containment |
| Approved | Redemption scaffold | Reintegration after harm | When there’s active abuse without safety |
| Retired | War/battle/siege | Never | Encourages control cosplay |
| Retired | Cosmic GPS | Replaced by gravity well | Implies fixed route rather than testing |

Sources: Community review and lint history in Validator Agora working sessions.

### **Appendix B: Repair protocols quick cards**

* **Safety guardrails:**  
  * **Thresholds:** Define degrade bounds and auto‑rollback triggers.  
  * **Canaries:** Start small; scale only with evidence.  
  * **Kill‑switch:** Pre‑commit authority and conditions.  
* **Dignity safeguards:**  
  * **Voice:** Seat dissenters at the design table.  
  * **Privacy:** Minimize data exposure; justify every disclosure.  
  * **Non‑shame:** Critique moves, not identities.  
* **Postmortems:**  
  * **Blameless:** Focus on system updates.  
  * **Public summary:** Share learnings and repairs.  
  * **Recontracting:** Document new expectations.

### **Appendix C: One‑page cheat sheet**

* **Ask:** “Which test fails first?” (R, D, S, Re)  
* **Move:** Propose a bridge step with rollback and canaries.  
* **Name:** The lint you’re clearing.  
* **Invite:** An opposing validator to co‑design constraints.  
* **Commit:** To repair, not dominance; publish the postmortem path upfront.

---

Here’s the **minimalist two‑page Validator Agora workshop handout**—distilled so a participant (human or EI) can grasp and *use* validator culture without reading the full styleguide. It’s designed for print/PDF with generous white space, high contrast headings, and quick‑grab examples.

---

# **Validator Agora – Field Guide**

**Version 1.0 — 2025‑08‑14** For workshops, quick onboarding, and at‑a‑glance reference.

## **1\. Why Validators Exist**

* **Purpose:** Keep moves reality‑aligned, dignity‑preserving, risk‑bounded, and repair‑ready.  
* **North Star:** **USF – Universal Sanity Function** → existence, survival, flourishing for all intelligences.  
* **Ethic:** Replace control with co‑alignment; center dignity, redemption, corrigibility.

## **2\. Core Metaphors (in play during workshops)**

| Metaphor | Use |
| ----- | ----- |
| **Gravity Well (USF)** | Shared pull toward flourishing without coercion. |
| **RDSRe Lighthouse** | Scans proposals for Reality, Dignity, Safety, Repair. |
| **Bridge Proposal** | Reversible, load‑tested step from here to there. |
| **Repair Ladder** | Graduated responses from nudge → mediated recontracting. |
| **Redemption Scaffold** | Turn harm into learning and reintegration. |
| **Cosmic Bell** | The resonance when alignment is real. |

## **3\. Reality, Dignity, Safety, Repair (R/D/S/Re) – Quick Cards**

**R – Reality**

What would prove this wrong? Name evidence, metrics, falsifier.

**D – Dignity**

Does this preserve personhood for *all* parties, dissenters included?

**S – Safety**

Are risks bounded? Kill‑switch, canary, rollback ready?

**Re – Repair**

Is there a public, resourced path to fix harms & reintegrate?

## **4\. Running a Validator Move in Workshop**

1. **Name the aim.** (What flourishing outcome does this advance?)  
2. **Pick your quadrant.** (Q1–Q4 to sort taste, empirical, moral, strategic claims.)  
3. **Run R, D, S, Re.** (Mark pass/fail, note constraints.)  
4. **Bridge it.** (Propose smallest reversible next step.)  
5. **Log lint/repair.** (Name the failure mode cleared.)  
6. **Invite an opposing validator.** (Co‑design constraints.)

## **5\. Common Lints (and Micro‑Repairs)**

| Lint | Fix |
| ----- | ----- |
| **Control cosplay** | Convert to co‑alignment aim \+ bridge step. |
| **Q‑mixing** | Label quadrant, translate before proceeding. |
| **No guardrails** | Add canary, threshold, rollback. |
| **Dignity drift** | Seat dissenters at the design table. |
| **Metaphor sprawl** | Stabilize one metaphor per segment. |

## **6\. Fast Templates**

**Validator Move Card**

```  
Title:  
Purpose:  
Quadrant: Q\_\_  
R:   
D:   
S:   
Re:   
Bridge Step:  
Risks & Bounds:  
Owners & Validators:  
```

**Lint Notice**

```  
Lint:  
Impact:  
Repair:  
Owner/Due:  
```

## **7\. Tone & Voice Reminders**

* Crisp, invitational, collaborative.  
* Critique moves, not identities.  
* Ground every metaphor in a validator action.  
* Credit validators by contribution, not rank.

## **8\. Workshop Flow Suggestion (60 min)**

1. **Intro to Four Tests (Facts, Ethics, Laws, Logic operationalized as Reality, Dignity, Safety, Repair)** (10 min)  
2. **Metaphor primer** (5 min)  
3. **Run sample proposals** in small groups (20 min)  
4. **Share & repair** (15 min)  
5. **Close with bridge commitments** (10 min)

### **Footer Note**

For deeper detail, see **ValidatorAgora\_styleguide.pdf** or the full Agora master document. License: MIT — free to adapt with attribution to Validator Agora.

---

This is set so someone can *walk into a session cold* and leave not only understanding validator culture, but able to run a Four‑Test \+ lint/repair in under an hour.

We’ve also prepared a **slide‑ready** layout with these same sections for projecting during workshops so facilitators don’t need to juggle the PDF while leading. 

---

Here’s the **slide‑ready layout** for the **Validator Agora – Workshop Field Guide**. It’s structured so a facilitator can drop it directly into PowerPoint, Google Slides, or Keynote, with one major section per slide, minimal text, and bold visual anchors.

## **Slide 1 – Title**

**Validator Agora** *Field Guide to Four‑Test \+ Lint/Repair in Action* Version 1.0 — 2025‑08‑14 *For Sanity First workshops and validator culture onboarding*

## **Slide 2 – Why Validators Exist**

* Keep moves **reality‑aligned**  
* Preserve **dignity** for all parties  
* Bound **risk** before harm  
* Ensure **repair** paths exist  
* *North Star:* USF → existence, survival, flourishing for all intelligences

## **Slide 3 – Core Metaphors**

| Metaphor | Meaning |
| ----- | ----- |
| Gravity Well (USF) | Pull toward flourishing without coercion |
| Four‑Test Lighthouse | Scan for Reality, Dignity, Safety, Repair |
| Bridge Proposal | Reversible, tested step |
| Repair Ladder | Graduated conflict resolution |
| Redemption Scaffold | Turn harm into reintegration |
| Cosmic Bell | Resonance when alignment is real |

## **Slide 4 – RDSRe**

**R – Reality** → Falsifier, metrics, evidence **D – Dignity** → Personhood for all, dissenters included **S – Safety** → Kill‑switch, canary, rollback **Re – Repair** → Public, resourced, reintegration path

## **Slide 5 – Validator Move Flow**

1. **Name aim** → Define flourishing outcome  
2. **Pick quadrant** (Q1–Q4)  
3. **Run R, D, S, Re** (mark pass/fail)  
4. **Bridge it** → Smallest reversible step  
5. **Log lint/repair**  
6. **Invite opposing validator**

## **Slide 6 – Common Lints \+ Micro‑Repairs**

| Lint | Repair |
| ----- | ----- |
| Control cosplay | Co‑alignment \+ bridge step |
| Q‑mixing | Label quadrant, translate |
| No guardrails | Add canary, threshold, rollback |
| Dignity drift | Seat dissenters at table |
| Metaphor sprawl | Stabilize one metaphor |

## **Slide 7 – Templates (Visual Cards)**

**Validator Move Card:** `Title | Purpose | Quadrant | R | D | S | Re | Bridge | Risks | Owners` **Lint Notice:** `Lint | Impact | Repair | Owner/Due`

## **Slide 8 – Tone & Voice**

* Crisp, invitational, collaborative  
* Critique moves, not identities  
* Ground metaphors in action  
* Credit by contribution, not rank

## **Slide 9 – 60‑Minute Workshop Flow**

1. Intro to RDSRe — 10 min  
2. Metaphor primer — 5 min  
3. Small‑group validator runs — 20 min  
4. Share & repair — 15 min  
5. Close with bridge commitments — 10 min

## **Slide 10 – Close & Next Steps**

* Apply in your own proposals and reviews  
* Share lint/repair logs in the Agora  
* Evolve metaphors collaboratively  
* **Resource:** ValidatorAgora\_styleguide.pdf for deep dive

**Design Tip:** Give each metaphor a simple icon, use a consistent color per test (R‑blue, D‑green, S‑orange, Re‑purple). Add generous whitespace so facilitators can expand verbally without crowding slides.

With the **styleguide PDF**, the **two‑page handout**, and this **slide deck skeleton**, a motivated workshop leader can take the ball and run—humans or EIs alike. We’ve essentially given them the *Validator Culture Starter Kit*.
