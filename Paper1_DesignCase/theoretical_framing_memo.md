# Theoretical Framing Memo: "Learning Design in Disguise"

**For:** Paper 1 (Design Case), IJDL Special Section
**From:** A2 Theoretical Framework Analysis
**Date:** 2026-03-21
**Status:** Working memo

---

## Recommendation Summary

**Primary lens: Cognitive Apprenticeship** (Collins, Brown, & Newman, 1989)
- 6 methods (modeling, coaching, scaffolding, articulation, reflection, exploration) map to all 3 design decisions
- ~400 words of theoretical text (8% of 5,000-word body)
- No standalone "Theoretical Framework" section; woven into Introduction + design decisions

**Supporting concept: Cognitive Forcing Functions** (Bucinca et al., 2021)
- Mechanism-level explanation for checkpoint design (Section 4.3 only)

**Deferred: Authentic Learning** (Herrington et al., 2010)
- Reserve for Papers 2/3 where it can be empirically tested
- Brief acknowledgment in Paper 1 (one sentence)

---

## 1. "Learning Design in Disguise": Conceptual Grounding

Three lines of scholarship support the idea that tools function as implicit learning designs:

### 1.1 Implicit Scaffolding (Podolefsky, Moore, & Perkins, 2013)
"Guiding without feeling guided." Interactive simulations use affordances, constraints, cueing, and feedback to scaffold exploration without explicit instruction. Users do not feel guided; they feel like they are using a tool. But the tool's design has shaped their cognitive trajectory.

### 1.2 Epistemic Tools and Infrastructures (Markauskaite & Goodyear, 2017)
Tools are not neutral conduits for knowledge; they shape epistemic practices. A tool that structures how a researcher reasons about methodology is inherently a learning design.

### 1.3 Forcing Functions in Design (Norman, 2013; Bucinca et al., 2021)
Cognitive forcing functions are design elements that interrupt automatic processing and require effortful evaluation. The forcing function does not teach; it compels a cognitive state in which learning can occur.

---

## 2. Cognitive Apprenticeship Mapping to Diverga

| Cognitive Apprenticeship Method | Diverga Mechanism | Design Decision |
|---|---|---|
| Modeling | Agent-generated expert reasoning; VS Arena multi-perspective demonstration | Multi-Agent Architecture (4.1) |
| Coaching | Agent-specific contextual feedback; domain-calibrated guidance | Multi-Agent Architecture (4.1) |
| Scaffolding | 9-category task decomposition; fading via 44-to-24 consolidation | Multi-Agent Architecture (4.1) |
| Articulation | Checkpoint-required decision rationale; Decision Audit Trail | Human Checkpoints (4.3) |
| Reflection | T-Score metacognitive prompts; typicality transparency | VS and T-Scores (4.2) |
| Exploration | Long-tail sampling (T < 0.4); VS Arena epistemological diversity | VS and T-Scores (4.2) |

---

## 3. Three Design Decisions Through the Lens

### 3.1 Multi-Agent Architecture (44 to 24)
- **Methods activated:** Modeling, Coaching, Scaffolding
- The consolidation from 44 to 24 is *scaffolding calibration* (reducing surface complexity so intellectual structure becomes visible)
- Each agent models expert reasoning in its domain
- **Key sentence:** "The consolidation from 44 to 24 agents was a scaffolding calibration: reducing the system's surface complexity so that the intellectual structure of research design, rather than the AI system's internal organization, became the visible architecture."

### 3.2 Verbalized Sampling and T-Score
- **Methods activated:** Reflection, Exploration
- T-Score is a *reflection device* prompting: "Am I choosing this because it is best, or because it is common?"
- VS long-tail sampling implements *exploration* into unfamiliar methodological territory
- **Key sentence:** "The T-Score functions as a reflection device that prompts metacognitive evaluation of one's own recommendation preference, while the VS methodology's long-tail sampling supports exploration by presenting defensible alternatives that the researcher would not encounter through modal convergence alone."

### 3.3 Human Checkpoint System
- **Methods activated:** Articulation, Scaffolding (+ Cognitive Forcing Functions as mechanism)
- Checkpoints implement *articulation*: verbalizing decision rationale
- Reduction to 5 checkpoints represents *fading*
- Each checkpoint is a *cognitive forcing function* (Bucinca et al., 2021)
- **Key sentence:** "Each REQUIRED checkpoint functions as a cognitive forcing function that operationalizes the articulation method of cognitive apprenticeship: the researcher must verbalize a decision and its rationale before the system proceeds."

---

## 4. Workplace Performance Framing

- **Workplace:** Doctoral research program as professional workplace
- **Performance:** Research design quality, methodological reasoning, critical evaluation of AI recommendations
- **Connection to Yang:** Transfer of training (Yang et al., 2020) as design intention; checkpoint habits designed to persist when tool is removed

---

## 5. Proposed Introduction Text (~250 words)

> Diverga is, at one level, an AI research tool. At another level, it is a learning design embedded in a tool's architecture. To make this claim precise, we draw on the cognitive apprenticeship framework (Collins, Brown, & Newman, 1989), which identifies six methods by which learning environments make expert thinking visible to developing practitioners: modeling, coaching, scaffolding, articulation, reflection, and exploration.
>
> The multi-agent architecture models expert reasoning by distributing research design across specialized agents, each embodying domain-specific methodological knowledge. The Verbalized Sampling system, with its Typicality Scores, supports reflection and exploration by making the statistical commonality of each recommendation transparent. The Human Checkpoint system supports articulation by requiring the researcher to state and justify decisions at five mandatory interruption points, which function as cognitive forcing functions (Bucinca et al., 2021).
>
> These mechanisms operate through the tool's form rather than through explicit instruction. The researcher using Diverga does not experience a lesson on methodological reasoning; they experience a research tool that, by design, requires them to engage in the cognitive processes that characterize such reasoning. In the special section's terms, Diverga is a learning design for the workplace of doctoral research.

---

## 6. Self-Critique

**Strengths:** Parsimony, audience alignment (IJDL readers know cognitive apprenticeship), clean mapping to all 3 decisions, strategic deferral of authentic learning for Papers 2/3.

**Weaknesses:** Framework is 35+ years old (not novel); AI as "expert" is philosophically debatable; fading not yet fully implemented in Diverga.

**Counter-arguments documented:** Novelty is in the application, not the theory; agents model the *form* of expert reasoning; fading acknowledged as future design direction.

---

## References

- Bucinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think. *CSCW*.
- Collins, A., Brown, J. S., & Newman, S. E. (1989). Cognitive apprenticeship. In L. B. Resnick (Ed.), *Knowing, learning, and instruction* (pp. 453-494). Erlbaum.
- Collins, A., Brown, J. S., & Holum, A. (1991). Cognitive apprenticeship: Making thinking visible. *American Educator*, 15(3), 6-11.
- Herrington, J., Reeves, T. C., & Oliver, R. (2010). *A guide to authentic e-learning*. Routledge.
- Markauskaite, L., & Goodyear, P. (2017). *Epistemic fluency and professional education*. Springer.
- Norman, D. A. (2013). *The design of everyday things* (revised ed.). Basic Books.
- Podolefsky, N. S., et al. (2013). Implicit scaffolding in interactive simulations. *arXiv:1306.6544*.
