# Paper Outline: IJDL Special Section Submission
## "Scaffolding Without Replacing: A Design Case of Human Checkpoints and Verbalized Sampling in an AI Research Methodology Assistant"

**Target:** IJDL Special Section, "Learning Designs to Support and Improve Workplace Performance"
**Format:** Full design case
**Target word count:** ~5,000 words (text only, excluding figures, tables, and references)
**Authors:** Hosung You (first), Mohan Yang (second)
**Framing:** Learning design in disguise; first-person design case; EDR phases 1-2
**Revised:** 2026-03-21 (tailored to IJDL Special Section; 3 design decisions instead of 5)

---

## Framing Notes for This Outline

The IJDL Special Section explicitly welcomes artifacts "not originally framed as learning designs but that shape workplace performance." This paper leads with that framing from the abstract forward. Diverga is introduced as a research tool that functions as a learning design: it scaffolds the methodological reasoning of doctoral researchers, who are knowledge workers whose research design capability constitutes their primary workplace performance.

The paper is first-person. The designer narrates his own design process, including failures and unresolved tensions, following IJDL design case conventions (Boling, 2010; Smith, 2010). Dr. Yang's role as external collaborator is acknowledged as itself a design decision, compensating for the designer-as-evaluator position.

Design decisions have been reduced from five (in the original outline for Dr. Yang) to three, selected for their direct relevance to the special section theme and for their ability to illustrate learning design principles in an AI tool context.

---

## Section-by-Section Outline

---

### Abstract (~200 words, not counted in 5,000-word body)

Structure: IMRaD condensed.

- **Problem:** AI research tools converge on modal recommendations (mode collapse) and encourage uncritical acceptance (automation bias), undermining methodological reasoning in knowledge work.
- **Artifact:** Diverga, a 24-agent AI research methodology assistant designed to scaffold rather than replace researcher decision-making.
- **Design decisions:** Multi-agent architecture (44 to 24 agents); Verbalized Sampling with Typicality Scores; five required Human Checkpoints as cognitive forcing functions.
- **Frame:** Learning design in disguise for doctoral researcher workplace performance.
- **Genre:** First-person design case; EDR phases 1-2.

---

### Section 1: Introduction (~700 words)

**Purpose:** Establish the problem, introduce the design challenge, frame the paper as a learning design in disguise, and orient the reader to IJDL design case conventions.

**Key moves:**
1. Open with the workplace performance framing: research methodology decisions are consequential knowledge work tasks for doctoral students and early-career scholars. These decisions define epistemic character and professional reputation.
2. Introduce mode collapse as the design driver: AI tools converge on predictable recommendations regardless of research context. Concrete example: TAM for technology adoption, thematic analysis for qualitative work, random effects for meta-analysis.
3. Introduce automation bias as the compounding problem: 78% uncritical acceptance rate (Springer Nature, 2025); negative correlation with critical thinking (Microsoft Research, 2025).
4. State the design challenge: Can an AI research assistant be designed to scaffold methodological reasoning rather than replace it?
5. Introduce Diverga: 24-agent system, 57-day design period, 224 commits. First-person framing: the designer is a doctoral student simultaneously building the tool and studying research methodology.
6. State the "learning design in disguise" angle explicitly: Diverga was built as a research tool, but its architecture is organized around scaffolding epistemic agency. Its design decisions are learning design decisions, even when they look like engineering decisions.
7. Scope statement: This paper documents the design process, decisions, and rationale. Empirical evaluation is a companion paper. The design case follows EDR phases 1-2 (McKenney & Reeves, 2012).

**References:** Boling (2010); Smith (2010); McKenney & Reeves (2012); Springer Nature (2025); Microsoft Research (2025)

---

### Section 2: Design Context (~600 words)

**Purpose:** Situate the designer, the users, and the technical context. Establish credibility of the first-person perspective and acknowledge its limitations.

**Subsections:**

**2.1 The Designer and the Dual Role (~200 words)**
- Hosung You, Penn State doctoral student in education, simultaneously the builder and the researcher.
- The dual role is both an asset (insider tacit knowledge) and a limitation (evaluation bias).
- Dr. Yang's collaboration was sought as a structural compensation: external design case expertise and critical interrogation of design rationale.
- This collaboration structure is itself a design decision, documented here rather than buried in an acknowledgment.

**2.2 Target Users and Workplace Context (~200 words)**
- Social science doctoral students engaged in research design.
- Research methodology decisions as knowledge work: selecting theoretical frameworks, designing data collection, choosing analytical approaches.
- The gap between research methods coursework and actual research design practice: courses teach the logic of methods; they rarely scaffold the judgment required to select and adapt methods for a specific study.
- Diverga is designed for that gap.

**2.3 Technical Context (~200 words)**
- Model Context Protocol (MCP): the infrastructure standard that enables multi-agent coordination in Claude Code.
- Why a doctoral student could build this in 57 days: MCP abstracts the complexity of agent-to-agent communication; Claude Code provides the execution environment.
- Brief comparison with existing tools (Elicit, Consensus, SciSpace, ChatGPT): what they provide (information retrieval, summarization, general assistance) and what they do not provide (structured diversity, mandatory human oversight, typicality transparency).

**Figure placeholder:** Table 1. Diverga vs. existing AI research tools (4-column comparison: Diverga, Elicit, Consensus, ChatGPT). Placed at end of Section 2.

---

### Section 3: Design Problem in Detail (~600 words)

**Purpose:** Give the design problem enough specificity that readers understand why the three design decisions described in Section 4 were necessary.

**Subsections:**

**3.1 Mode Collapse in Research AI (~250 words)**
- Define mode collapse for a non-technical audience: AI systems trained to maximize prediction probability will consistently produce the most statistically common output, not the most contextually appropriate one.
- Analogy to instructional design: standardized curricula that reduce pedagogical diversity; one-size-fits-all LMS configurations that constrain instructional approaches.
- Concrete examples from research methodology: technology adoption (TAM dominance), qualitative design (thematic analysis default), sampling (convenience sampling recommendation).
- Citation: arXiv:2510.01171.

**3.2 Automation Bias in Knowledge Work (~200 words)**
- Automation bias: the tendency to accept AI recommendations without critical evaluation, especially under time pressure or when the AI presents recommendations with confidence.
- 78% uncritical acceptance rate in research contexts (Springer Nature, 2025).
- Negative correlation between AI tool use and critical thinking engagement (Microsoft Research, 2025).
- The compounding effect: mode collapse narrows the options presented; automation bias ensures the narrowed options are accepted without scrutiny.

**3.3 The Design Gap (~150 words)**
- No existing tool combines structured human oversight with diversity-generating mechanisms for research methodology guidance.
- The design challenge is not to build a better recommendation engine; it is to build a system that keeps the researcher's judgment in the loop while countering the homogenization pressure of the underlying model.

---

### Section 4: Design Decisions and Rationale (~2,400 words; core of the paper)

**Purpose:** Document three design decisions using the IJDL design case pattern: decision point, alternatives considered, rationale for chosen approach, evidence of implementation, and design tension carried forward.

Each subsection is approximately 800 words.

---

#### 4.1 Multi-Agent Architecture: From 44 to 24 Agents (~800 words)

**Decision point:** How many agents, organized how?

**The trajectory (200 words):**
- v1.0 (January 22, 2026): 20 agents in 5 categories. Core concept established.
- v6.7 (peak): 44 agents across 9 categories. Maximum specialization.
- v11.0 (current): 24 agents across 9 categories. Principled consolidation.
- The 44-to-24 reduction is the narrative center: not a failure, but a design lesson about the relationship between specialization and usability.

**Alternatives considered (150 words):**
- Single-agent with diverse prompting (simpler, but one agent cannot hold competing epistemological commitments simultaneously).
- Modular tool-use agent similar to Cline/Obra architecture (maximizes user adoption breadth, but sacrifices domain depth).
- Maintaining 44 agents (maximum specialization, but coordination overhead and user cognitive load scale superlinearly with agent count).

**Rationale for consolidation (250 words):**
- Functional overlap analysis: several v6.7 agents performed structurally identical tasks in different topical clothing.
- Usage patterns: many specialized agents were rarely invoked because users defaulted to broader-scope agents.
- Li et al. (2025) "more agents is less" finding: beyond a threshold, additional agents generate coordination noise that degrades output quality.
- Brooks' subsumption architecture principle: simpler subsystems with clean ownership boundaries outperform complex subsystems with overlapping responsibilities.
- The 9-category structure (A: Theory, B: Literature, C: Methodology, D: Data, E: Analysis, F: Quality, G: Publication, H: Ethics, I: Specialized) maps to the actual phases of research design, not to the internal logic of the AI system.

**Evidence of implementation (100 words):**
- Before/after architecture diagram (Figure 1).
- Agent consolidation table: which v10 agents merged, which v11 agent absorbed them, and the functional rationale for each merger (Table 2).

**Design tension carried forward:**
- Simplicity vs. specialization. 24 agents organized in 9 categories is still more complex than ChatGPT. Diverga remains a specialized tool with a learning curve. This is an unresolved tension, not a solved problem. The paper does not claim the current count is optimal; it claims it is more defensible than 44.

**Figures/tables for this subsection:**
- Figure 1: Architecture comparison (v10 44-agent map vs. v11 24-agent map). Side-by-side.
- Table 2: Agent consolidation table (columns: v10 agent name, v11 agent absorbed into, functional rationale).

---

#### 4.2 Verbalized Sampling and Typicality Scores: Structuring Diversity (~800 words)

**Decision point:** How does the system generate recommendations that escape modal convergence?

**The problem reframed (150 words):**
- Instructional analogy: asking a curriculum to "be diverse" does not produce diversity; structural requirements for diverse content do.
- Similarly, prompting an AI to "provide diverse recommendations" is an instruction it can partially satisfy while still defaulting to high-probability outputs.
- Diversity must be structurally enforced, not instructionally requested.

**Alternatives considered (150 words):**
- Standard prompting with diversity instructions ("give me three different options"): produces surface variation without genuine epistemic diversity.
- Retrieval-augmented generation from a curated methodology database: addresses gaps in training data but does not address distributional bias in the model itself.
- Random sampling with post-hoc filtering: introduces noise without principled diversity criteria.

**Rationale for Verbalized Sampling (250 words):**
- VS (Zhao et al., 2024) provides a principled framework for exploring the full typicality spectrum rather than the high-probability peak.
- T-Score (Typicality Score): a measure of how common a recommendation is relative to the model's training distribution. T > 0.8 is modal; T < 0.4 is genuinely unconventional.
- Critical design decision: surface the T-Score to the researcher, not just use it internally. A researcher who sees T = 0.82 knows they are receiving the expected recommendation. One who sees T = 0.31 knows they are in unconventional territory and can decide accordingly.
- The T-Score becomes a metacognitive tool: it prompts the researcher to ask "is this the common choice because it is the best choice for my context, or because it is statistically common?"
- VS Arena: five epistemological persona agents (post-positivist, interpretivist, critical theorist, pragmatist, transformative) with cannotRecommend constraint arrays. Each persona is structurally prohibited from recommending what the other personas are likely to recommend, enforcing genuine epistemic diversity rather than simulated variation.

**Evidence of implementation (100 words):**
- Example prompt-response pair showing VS output with T-Scores (Figure 2).
- VS Arena persona configuration, annotated (Figure 3): shows cannotRecommend arrays and the structural constraint mechanism.

**Design tension carried forward:**
- Diversity vs. coherence. The VS Arena generates five epistemologically divergent perspectives on a methodology question. Without synthesis, this can overwhelm a novice researcher. No arbitration mechanism currently exists in Diverga to help the researcher integrate competing recommendations. This is an acknowledged gap, documented as a future design problem rather than a current limitation to be minimized.

**Figures/tables for this subsection:**
- Figure 2: Example T-Score display as seen by the researcher. Annotated screenshot.
- Figure 3: VS Arena persona configuration excerpt (annotated YAML or schematic). Shows cannotRecommend arrays for two personas as illustration.

---

#### 4.3 Human Checkpoint System: Five Required Cognitive Forcing Functions (~800 words)

**Decision point:** Where does the human stay in the loop, and how?

**The problem reframed (100 words):**
- Automation bias is not primarily a knowledge problem; researchers often know they should evaluate AI recommendations critically. It is a cognitive habit problem: under time pressure and with confident-sounding AI output, critical evaluation is the path of most resistance.
- Cognitive forcing functions (Bucinca et al., 2021): deliberate design elements that interrupt automatic processing and require effortful evaluation. The checkpoint is the learning design equivalent of a Socratic pause.

**The trajectory (150 words):**
- Early versions (v3.0): checkpoint system formally specified; AskUserQuestion mechanism established.
- v6.0 (Clean Slate Edition, January 25, 2026): major philosophical pivot. Removed the Sisyphus Protocol and autonomous continuation modes. Strengthened mandatory checkpoints. Language shift from "I will proceed" to "May I proceed?" This is the moment the system's design philosophy crystallized.
- v11.0: checkpoint bug discovered. All checkpoints auto-approved because a conditional logic error caused the pause mechanism to always return {continue: true}. The bug was not detected through user testing; it was detected through architectural review. The system appeared to have checkpoints; it did not.
- v11.1: SQLite-based fix. Five REQUIRED checkpoint gates with verified halt behavior.

**Alternatives considered (150 words):**
- No checkpoints (full autonomy): maximizes workflow fluidity; eliminates checkpoint fatigue; eliminates genuine human oversight.
- Optional checkpoints (soft suggestions): preserves fluidity; but optional checkpoints are consistently skipped under time pressure, providing the appearance of oversight without its function.
- Checkpoints at every step (maximum oversight): cognitively burdensome; research by Bucinca et al. shows that excessive forcing functions produce reactance and tool abandonment.

**Rationale for five required checkpoints (200 words):**
- The five gate positions correspond to genuine cross-agent dependency points: decisions made at these points propagate through all subsequent agent outputs. A researcher who selects a post-positivist paradigm at Checkpoint 2 receives different outputs from the analysis agents than one who selects a critical theory paradigm. The checkpoint is where paradigmatic commitment becomes consequential.
- Five is a judgment call, not an empirically derived optimum. The design case documents this honestly: the number reflects the designer's best current assessment of where oversight adds more value than it subtracts in cognitive load.
- The checkpoint bug story is included not as a confession but as evidence: genuine human oversight in autonomous AI systems is difficult to implement and verify. Systems that appear to have checkpoints may not. This design lesson generalizes beyond Diverga.

**Evidence of implementation (100 words):**
- Checkpoint flow diagram showing the five REQUIRED gates and their positions in the workflow (Figure 4).
- Screenshot of a REQUIRED checkpoint as presented to the researcher (Figure 5).
- Brief description of the SQLite implementation and the architectural review process that detected the bug.

**Design tension carried forward:**
- Autonomy vs. oversight. Five REQUIRED checkpoints is a defensible position, not a proven optimum. Checkpoint fatigue is real; five interruptions in a research design session may still be too many for some users. The tension is documented as an open empirical question for the companion evaluation paper.

**Figures/tables for this subsection:**
- Figure 4: Checkpoint flow diagram. Shows 5 REQUIRED gates, their labels, and the workflow segments between them.
- Figure 5: Screenshot of a REQUIRED checkpoint interaction. Annotated to show the halt behavior and the researcher decision interface.

---

### Section 5: Design Tensions (~500 words)

**Purpose:** Frame the paper's three core tensions as inherent and unresolved, not as problems the design solved. This section gives the design case intellectual honesty and positions the unresolved tensions as hypotheses for the companion evaluation paper.

**Framing sentence:** Design cases in learning design often document what was built and why; the best ones also document what remains uncertain and why it matters. The following tensions are carried forward from Section 4 as open questions.

**Tension 1: Simplicity vs. Specialization (~150 words)**
- 24 agents in 9 categories is more principled than 44, but it is still more complex than a general-purpose tool.
- For novice researchers, the 9-category architecture may itself be a barrier: knowing which category of agent to invoke requires prior knowledge of the research design process.
- The design bets that the right users (doctoral students in research design contexts) have enough process knowledge to navigate the architecture. This bet has not been tested.

**Tension 2: Diversity vs. Coherence (~150 words)**
- The VS Arena generates five epistemologically divergent perspectives. For experienced researchers, this plurality is a resource. For novice researchers, it may be a source of confusion rather than illumination.
- No synthesis mechanism currently exists. The researcher must integrate competing perspectives without AI support.
- This is the most important unresolved design problem in Diverga's current state.

**Tension 3: Oversight Rigor vs. Workflow Fluidity (~150 words)**
- Five checkpoints interrupt cognitive flow. The design trades some fluidity for genuine oversight, but the exchange rate is unknown.
- Checkpoint fatigue is not hypothetical: in the pre-fix v11.0, the silent auto-approval behavior may have emerged partly because the original checkpoint count was too high and was quietly engineered around.
- The companion evaluation paper will investigate whether five REQUIRED checkpoints produce the intended deliberative behavior or whether they produce habituated click-through.

**Closing sentence for Section 5:** These tensions are not design failures; they are the honest boundary conditions of the current design. Naming them is a contribution to the field's understanding of what it means to design AI tools for epistemic support rather than mere efficiency.

---

### Section 6: Design Artifacts (~400 words + figures)

**Purpose:** Curate the primary design evidence in one place, following IJDL's multimedia-friendly conventions.

**Format:** Brief descriptive paragraph per artifact, with figure or table cross-reference.

| Artifact | Description | Figure/Table |
|---|---|---|
| Architecture comparison | v10 (44-agent) vs. v11 (24-agent) maps | Figure 1 |
| Agent consolidation table | Merger rationale for each v10-to-v11 transition | Table 2 |
| T-Score display example | Annotated screenshot of VS output as seen by researcher | Figure 2 |
| VS Arena persona configuration | Annotated excerpt showing cannotRecommend arrays | Figure 3 |
| Checkpoint flow diagram | Five REQUIRED gates and workflow segments | Figure 4 |
| Checkpoint interaction screenshot | Researcher-facing halt behavior at a REQUIRED gate | Figure 5 |
| Decision audit trail sample | Excerpt from decision-log showing researcher choices at checkpoints | Figure 6 |
| Design evolution timeline | Key milestones from v1.0 (Jan 22) to v11.1 (Mar 2026) | Figure 7 |

**Note on artifacts:** All screenshots and YAML excerpts are drawn from actual Diverga sessions and configurations. Prompts and outputs have been lightly edited for length but not for content.

---

### Section 7: Reflection and Future Directions (~400 words)

**Purpose:** Close the design case by connecting the design story to the broader field and to the companion papers.

**7.1 What This Design Story Reveals (~200 words)**
- Learning design principles are not limited to explicit instructional settings. The decisions documented in this paper (structural diversity enforcement, mandatory cognitive interruption, typicality transparency) are recognizable to instructional designers even when they appear in an AI tool's architecture.
- The "learning design in disguise" framing is not a rhetorical move; it is descriptive. Diverga shapes researcher behavior through its form, not through explicit instruction. This is analogous to how a well-designed PBL environment shapes student inquiry through task structure rather than direct teaching.
- The designer-as-researcher position, compensated by external collaboration, is a viable model for early-career researchers building the tools they study. The transparency required by design case conventions forces a discipline that purely engineering-oriented development does not.

**7.2 Transferable Design Principles (~100 words)**
- Structural enforcement over instructional exhortation: design diversity into the system's architecture, not into the system's instructions.
- Transparency as metacognitive prompt: surface the information the user needs to calibrate their reliance on the system.
- Checkpoints as cognitive forcing functions: design mandatory pause points at consequential decision nodes, not at every step.

**7.3 Connection to Companion Papers (~100 words)**
- This design case occupies EDR phases 1 and 2. The empirical evaluation of whether Diverga's design decisions produce the intended effects on researcher performance is Paper 3 (Computers & Education, targeted 2027).
- Paper 2 (BJET Special Issue, targeted 2026) will address methodological questions about how to study artificial agency in multi-agent AI systems, using Diverga as the exemplar case.
- The design case establishes the design rationale that Papers 2 and 3 can reference without re-documenting the full system.

---

### References

*Key references below; full formatted reference list to be prepared for submission.*

- Boling, E. (2010). The need for design cases: Disseminating design knowledge. *International Journal of Designs for Learning*, 1(1), 1-8.
- Bucinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision making. *CSCW*, 5, Article 188.
- Li, Z., et al. (2025). More agents is less: Scaling properties of multi-agent LLM systems. *arXiv:2602.03794*.
- McKenney, S., & Reeves, T. C. (2012). *Conducting educational design research*. Routledge.
- Smith, K. M. (2010). Producing the rigorous design case. *International Journal of Designs for Learning*, 1(1), 9-20.
- Wang, T., et al. (2024). Mixture-of-agents yields emergent collaborative intelligence. *Together AI Technical Report*.
- Yang, M., & Harbor, J. (2023). Authentic learning design failures: The need for learner and contextual analysis and participatory design. *International Journal of Designs for Learning*, 14(1), 88-105.
- Zhao, Y., et al. (2024). Verbalized sampling for language model selection. *arXiv:2510.01171*.

---

## Word Count Estimates by Section

| Section | Estimated Words |
|---|---|
| Abstract (not in body count) | ~200 |
| Section 1: Introduction | ~700 |
| Section 2: Design Context | ~600 |
| Section 3: Design Problem in Detail | ~600 |
| Section 4.1: Multi-Agent Architecture | ~800 |
| Section 4.2: Verbalized Sampling and T-Scores | ~800 |
| Section 4.3: Human Checkpoint System | ~800 |
| Section 5: Design Tensions | ~500 |
| Section 6: Design Artifacts | ~400 |
| Section 7: Reflection and Future Directions | ~400 |
| **Total (body text)** | **~5,600** |

*Note: Target is ~5,000 words. Approximately 600 words of flexibility; Section 3 and Section 6 are the most compressible without losing core argument. Figures and tables are not included in the word count.*

---

## Required Figures and Tables

| ID | Type | Description | Section | Status |
|---|---|---|---|---|
| Figure 1 | Diagram | Architecture comparison: v10 (44-agent) vs. v11 (24-agent). Side-by-side category maps. | 4.1 | Needs creation |
| Figure 2 | Screenshot | T-Score display as presented to researcher during a Diverga session. Annotated. | 4.2 | Needs capture |
| Figure 3 | YAML/schematic | VS Arena persona configuration excerpt. Annotated to show cannotRecommend constraint arrays. | 4.2 | Needs extraction |
| Figure 4 | Flow diagram | Checkpoint flow showing 5 REQUIRED gates, labels, and workflow segments between gates. | 4.3 | Needs creation |
| Figure 5 | Screenshot | REQUIRED checkpoint interaction as presented to researcher. Annotated to show halt behavior. | 4.3 | Needs capture |
| Figure 6 | Screenshot/excerpt | Decision audit trail (decision-log.yaml) showing researcher choices at checkpoints. | 6 | Needs capture |
| Figure 7 | Timeline | Design evolution from v1.0 (Jan 22) through v11.1 (Mar 2026). Key milestones. | 6 | Needs creation |
| Table 1 | Comparison table | Diverga vs. Elicit vs. Consensus vs. ChatGPT on 4-5 design-relevant dimensions. | 2 | Available in brainstorming doc |
| Table 2 | Consolidation table | v10 agent, v11 agent absorbed into, functional rationale. All mergers documented. | 4.1 | Partially available; needs formalization |

---

## Deferred from Original Outline (5 Decisions -> 3)

The following design decisions from the original five-subsection outline (outline_for_yang.md, Section 4) are deferred from this submission:

| Deferred Decision | Rationale for Deferral |
|---|---|
| **VS Arena Design** (4.4 in original) | Core VS and Arena content is folded into Decision 2 (Section 4.2 here). The detailed persona configuration and cannotRecommend mechanism is represented through Figure 3. Full treatment reserved for Paper 2. |
| **Decision Audit Trail** (4.5 in original) | Represented as a design artifact in Section 6 (Figure 6) rather than as a standalone design decision. The audit trail's metacognitive function is referenced in Section 4.3 as a complement to checkpoints. |

These decisions remain available for Paper 2 (methodological contribution) and Paper 3 (empirical evaluation), where they will be treated with the evidence base that the design case cannot yet provide.

---

## Key Framing Differences from Original Outline

| Dimension | Original Outline (for Yang) | This Revision (IJDL Special) |
|---|---|---|
| **Primary frame** | Design case for IJDL (general) | Learning design in disguise for workplace performance (special section) |
| **Number of design decisions** | 5 | 3 |
| **Workplace performance link** | Implicit (research methodology as skill) | Explicit (lead with knowledge worker framing in Introduction) |
| **Target word count** | 7,200 (estimated) | ~5,000 |
| **Theory burden** | Minimal (per Yang meeting) | Minimal; workplace framing handles positioning without heavy theoretical scaffolding |
| **First-person framing** | Named in scope statement | Named in first paragraph of Introduction; reinforced throughout |
