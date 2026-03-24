# FINAL Integrated Outline v2: IJDL Design Case
## "Scaffolding Without Replacing: A Design Case of Human Checkpoints and Verbalized Sampling in an AI Research Methodology Assistant"

**Target:** IJDL Special Section, "Learning Designs to Support and Improve Workplace Performance"
**Format:** Full design case (first-person)
**Target word count:** ~5,000 words (body text, excluding abstract, figures, tables, references)
**Authors:** Hosung You (first), Mohan Yang (second)
**Framing:** Learning design in disguise; Cognitive Apprenticeship lens; EDR phases 1-2
**Version:** 2026-03-21 (FINAL integrated outline incorporating theoretical framing, EDR cycles, platform co-evolution, and design failures)
**Proposal deadline:** 2026-03-31
**Full manuscript deadline:** 2026-08-15

---

## Theoretical Foundation (woven throughout, not standalone section)

**Primary lens:** Cognitive Apprenticeship (Collins, Brown, & Newman, 1989)
- 6 methods: modeling, coaching, scaffolding, articulation, reflection, exploration
- All 6 map to the 3 design decisions (see Table 3)
- ~400 words total theoretical text distributed across Introduction and Section 5

**Supporting mechanism:** Cognitive Forcing Functions (Bucinca et al., 2021)
- Applied specifically to Section 5.3 (Human Checkpoints)

**Deferred:** Authentic Learning (Herrington et al., 2010) reserved for Papers 2 and 3

---

## Section-by-Section Outline

---

### Abstract (~200 words, not counted in body)

Structure: IMRaD condensed.

- **Problem:** AI research tools converge on modal recommendations (mode collapse) and encourage uncritical acceptance (automation bias), undermining methodological reasoning in knowledge work.
- **Artifact:** Diverga, a 24-agent AI research methodology assistant designed to scaffold rather than replace researcher decision-making.
- **Theoretical lens:** Cognitive apprenticeship (Collins et al., 1989) provides the framework: the system's architecture operationalizes modeling, coaching, scaffolding, articulation, reflection, and exploration through AI-mediated mechanisms.
- **Design decisions:** Multi-agent architecture (44 to 24 agents); Verbalized Sampling with Typicality Scores; five required Human Checkpoints as cognitive forcing functions.
- **Process:** Five iterative design cycles over 57 days (224 commits), co-evolving with the Claude Code platform.
- **Frame:** Learning design in disguise for doctoral researcher workplace performance.
- **Genre:** First-person design case; EDR phases 1-2.

---

### Section 1: Introduction (~600 words)

**Purpose:** Establish the problem, introduce the design challenge, frame the paper as a learning design in disguise with Cognitive Apprenticeship as the theoretical lens, and orient the reader to IJDL design case conventions.

**Key moves:**

1. **Workplace performance framing (80 words).** Research methodology decisions are consequential knowledge work tasks for doctoral students and early-career scholars. These decisions define epistemic character and professional reputation. Open with a concrete scenario: a doctoral student asks an AI tool for a theoretical framework and receives TAM regardless of context.

2. **Mode collapse as design driver (80 words).** AI tools converge on predictable recommendations regardless of research context. Define mode collapse for a non-technical audience: systems trained to maximize prediction probability will consistently produce the most statistically common output, not the most contextually appropriate one. Concrete examples: TAM for technology adoption, thematic analysis for qualitative work, random effects for meta-analysis.

3. **Automation bias as compounding problem (60 words).** 78% uncritical acceptance rate (Springer Nature, 2025); negative correlation with critical thinking (Microsoft Research, 2025). The combination narrows options and ensures the narrowed options go unscrutinized.

4. **Design challenge statement (40 words).** Can an AI research assistant be designed to scaffold methodological reasoning rather than replace it? This is a learning design problem disguised as an engineering problem.

5. **Cognitive Apprenticeship lens (paragraph 1 of 2, ~90 words).** Introduce the theoretical lens. Diverga is, at one level, an AI research tool. At another level, it is a learning design embedded in a tool's architecture. Drawing on the cognitive apprenticeship framework (Collins, Brown, & Newman, 1989), we identify six methods by which learning environments make expert thinking visible to developing practitioners: modeling, coaching, scaffolding, articulation, reflection, and exploration. Each of Diverga's three core design decisions operationalizes a subset of these methods through architectural mechanisms rather than explicit instruction.

   > **Key sentence:** "These mechanisms operate through the tool's form rather than through explicit instruction. The researcher using Diverga does not experience a lesson on methodological reasoning; they experience a research tool that, by design, requires them to engage in the cognitive processes that characterize such reasoning."

6. **Cognitive Apprenticeship lens (paragraph 2 of 2, ~80 words).** Preview the mapping briefly. The multi-agent architecture models expert reasoning and scaffolds the research design process. The Verbalized Sampling system, with its Typicality Scores, supports reflection and exploration by making the statistical commonality of each recommendation transparent. The Human Checkpoint system supports articulation by requiring the researcher to state and justify decisions at mandatory interruption points, which function as cognitive forcing functions (Bucinca et al., 2021). In the special section's terms, Diverga is a learning design for the workplace of doctoral research.

7. **Scope statement (70 words).** This paper documents the design process, decisions, and rationale across five iterative design cycles. Empirical evaluation is reserved for a companion experimental paper. The design case follows EDR phases 1-2 (McKenney & Reeves, 2012), and the first-person narrative follows IJDL design case conventions (Boling, 2010; Smith, 2010). Table 3 maps all six cognitive apprenticeship methods to specific Diverga mechanisms.

**References:** Collins, Brown, & Newman (1989); Bucinca et al. (2021); Boling (2010); Smith (2010); McKenney & Reeves (2012); Springer Nature (2025); Microsoft Research (2025)

**Table placed at end of Section 1:**
- **Table 3: Cognitive Apprenticeship Mapping** (6 CA methods to Diverga mechanisms and design decisions)

---

### Section 2: Design Context (~400 words)

**Purpose:** Situate the designer, the users, and the technical context. Establish credibility of the first-person perspective and acknowledge its limitations.

**Subsections:**

**2.1 The Designer and the Dual Role (~120 words)**
- Hosung You, Penn State doctoral student in education, simultaneously the builder and the researcher.
- The dual role is both an asset (insider tacit knowledge about research design challenges) and a limitation (evaluation bias).
- Dr. Yang's collaboration was sought as a structural compensation: external design case expertise, published IJDL design cases (Yang & Harbor, 2023), and critical interrogation of design rationale.
- This collaboration structure is itself a design decision.

**2.2 Target Users and Workplace Context (~120 words)**
- Social science doctoral students engaged in research design.
- Research methodology decisions as knowledge work: selecting theoretical frameworks, designing data collection, choosing analytical approaches.
- The gap between research methods coursework and actual research design practice.
- Diverga is designed for that gap.

**2.3 Technical Context (~160 words)**
- Model Context Protocol (MCP): the infrastructure standard that enables multi-agent coordination in Claude Code.
- Why a doctoral student could build this in 57 days: MCP abstracts agent-to-agent communication complexity; Claude Code provides the execution environment; the plugin ecosystem enables distribution.
- Brief comparison with existing tools (Table 1): Elicit, Consensus, SciSpace, ChatGPT provide information retrieval and summarization; none provides structured diversity, mandatory human oversight, or typicality transparency.

**Table at end of Section 2:**
- **Table 1: Diverga vs. Existing AI Research Tools** (5-column comparison: Feature dimension, Diverga, Elicit, Consensus, ChatGPT)

  | Dimension | Diverga | Elicit | Consensus | ChatGPT |
  |---|---|---|---|---|
  | Multi-agent architecture | 24 specialized agents in 9 categories | Single retrieval pipeline | Single retrieval pipeline | Single general-purpose agent |
  | Diversity mechanism | Verbalized Sampling with T-Scores across full typicality spectrum | None (retrieval-based) | None (retrieval-based) | Prompt-dependent ("give diverse options") |
  | Human oversight structure | 5 REQUIRED checkpoint gates; cognitive forcing functions | None (user-initiated) | None (user-initiated) | None (user-initiated) |
  | Typicality transparency | T-Score displayed to user for every recommendation | Not applicable | Not applicable | Not applicable |
  | Decision audit trail | SQLite-logged researcher decisions at each checkpoint | Not applicable | Not applicable | Conversation history only |

---

### Section 3: Design Process: Five Iterative Cycles (~600 words) [NEW SECTION]

**Purpose:** Tell the iterative design story. Position the development within the EDR model and show how the design evolved through analysis, construction, and reflection cycles. Integrate platform co-evolution as a narrative thread. Integrate design failures as evidence of genuine iterative reasoning.

**Opening paragraph (~80 words):**
Position the development within McKenney and Reeves (2012) EDR framework: three phases per cycle (Analysis/Exploration, Design/Construction, Evaluation/Reflection). The 57-day development period (January 22 to March 19, 2026; 224 commits) is organized into five identifiable cycles. These cycles were not pre-planned; they emerged from the interaction between design ambitions, evaluation feedback, and the evolving capabilities of the Claude Code platform. Figure 1 shows the conceptual framework; Figure 2 shows the five cycles mapped to the EDR model.

**Cycle 1: Foundation (v1.0-v2.0; Jan 22-23; 2 days) (~80 words)**
- Trigger: Recognition that LLM research assistants default to modal recommendations.
- Designed: 20 agents in 5 categories; Verbalized Sampling methodology integrated from arXiv:2510.01171; T-Score system introduced.
- Evaluated: Marketplace schema compatibility issues; installation guide was overly complex.
- Changed: Simplified installation; recognized need for modular creativity mechanisms.
- Agent count: 20.

**Cycle 2: Sisyphus and Clean Slate (v3.0-v6.0; Jan 23-25; 3 days) (~120 words)**
- Trigger: VS alone was insufficient; creativity needed to be modular and composable.
- Designed: Five creativity mechanisms (Forced Analogy, Divergent-Convergent Loop, Semantic Distance Scorer, Temporal Reframing, Community Simulation). Expanded to 33 agents. Introduced the Sisyphus Protocol: autonomous continuation until verified completion.
- **Design failure (Sisyphus Protocol):** Added in v5.0 and removed the same day in v6.0. The protocol removed human control, making AI autonomous between checkpoints. This was the fastest design failure in the project and established the foundational design principle: "AI works BETWEEN checkpoints, humans decide AT them."
- Changed: v6.0.0 "Clean Slate Edition" removed all autonomous modes. Strengthened mandatory checkpoints. Language shifted from "I will proceed" to "May I proceed?"
- Agent count: 20 to 33 to 27.

**Cycle 3: Expansion to Peak (v6.0-v6.7; Jan 25-Feb 4; 10 days) (~100 words)**
- Trigger: Identified domain gaps (meta-analysis pipeline, humanization, systematic review).
- Designed: Meta-analysis agents (C5/C6/C7), systematic review automation (I0-I3), Plugin Marketplace Edition, Task tool parallel execution, cross-platform support (Codex CLI + OpenCode).
- Evaluated: Task tool discovery failures; ESM/CommonJS conflicts; 8 consecutive plugin fix commits in one day; cross-platform parity never achieved (75%/70%).
- **Design failure (cross-platform support):** 41-day lifespan (Jan 28 to Mar 10). Platform compatibility was expensive and incomplete; eventually abandoned.
- Agent count: peaked at 44.

**Cycle 4: The Great Consolidation (v8.0-v11.0; Feb 4-Mar 10; 34 days) (~120 words)**
- Trigger: 44 agents across 3 platforms with a 59KB CLAUDE.md. Most agents were rarely used; some had overlapping responsibilities.
- Designed: MCP checkpoint enforcement, SQLite backend, Agent Teams pilot, humanization pipeline. Then the consolidation: 44 to 24 agents, Codex CLI and OpenCode support removed entirely, CLAUDE.md reduced from 59KB to 12KB (79% reduction).
- **Design failure (checkpoint bug):** v11.0 contained a silent bug in which all checkpoints auto-approved without user input. The system appeared to have checkpoints; it did not. Detected through architectural review, not user testing.
- **Design failure (lib/memory/):** 104-file Python module built over 11 days, then replaced entirely by MCP-based architecture.
- Changed: 20 agents removed via principled consolidation (see Table 2). Claude Code exclusive.
- **Platform co-evolution:** Hooks system (June 2025) enabled architectural enforcement of checkpoints, replacing behavioral instructions.

**Cycle 5: Stabilization (v11.1-v12.0; Mar 12-19; 7 days) (~100 words)**
- Trigger: Simplified foundation needed new capabilities; VS Arena concept required implementation.
- Designed: VS Arena with 5 epistemological persona agents; Agent Teams integration for genuine multi-agent debate; unified orchestrator replacing two redundant skills; CLAUDE.md extracted and slimmed from 16.8KB to less than 5KB.
- **Platform co-evolution:** Agent Teams (Feb 2026) enabled genuine multi-perspective debate. Before Agent Teams, VS Arena required simulated diversity through subagents; after Agent Teams, personas could cross-critique independently.
- Evaluated: Hook portability issues, deploy script ordering bugs.
- Agent count: 24 core + 5 VS Arena = 29.
- Outcome: Architecturally stable system ready for user evaluation studies.

**Closing paragraph (~50 words):**
Figure 3 shows the co-evolution of Claude Code platform features and Diverga design changes. Three platform capabilities were particularly consequential: hooks (enabling checkpoint enforcement at the architectural level), plugins (enabling marketplace distribution), and Agent Teams (enabling genuine multi-agent epistemological debate). Each triggered a design iteration.

**Figures and tables for Section 3:**
- **Figure 2: Five EDR Cycles** (horizontal timeline, agent count overlay, key events, platform milestones)
- **Figure 3: Platform-Design Co-evolution** (two parallel timelines with connecting arrows)

---

### Section 4: Design Problem (~400 words)

**Purpose:** Give the design problem enough specificity that readers understand why the three design decisions described in Section 5 were necessary. This section defines what needed to be solved; Section 5 documents the solutions.

**4.1 Mode Collapse in Research AI (~170 words)**
- Define mode collapse for a non-technical audience: AI systems trained to maximize prediction probability will consistently produce the most statistically common output, not the most contextually appropriate one.
- Analogy to instructional design: standardized curricula that reduce pedagogical diversity; one-size-fits-all LMS configurations that constrain instructional approaches.
- Concrete examples from research methodology: technology adoption (TAM dominance), qualitative design (thematic analysis default), sampling (convenience sampling recommendation).
- Citation: Zhao et al. (2024), arXiv:2510.01171.

**4.2 Automation Bias in Knowledge Work (~130 words)**
- Automation bias: the tendency to accept AI recommendations without critical evaluation, especially under time pressure or when the AI presents recommendations with confidence.
- 78% uncritical acceptance rate in research contexts (Springer Nature, 2025).
- Negative correlation between AI tool use and critical thinking engagement (Microsoft Research, 2025).
- The compounding effect: mode collapse narrows the options presented; automation bias ensures the narrowed options are accepted without scrutiny.

**4.3 The Design Gap (~100 words)**
- No existing tool combines structured human oversight with diversity-generating mechanisms for research methodology guidance.
- The design challenge is not to build a better recommendation engine; it is to build a system that keeps the researcher's judgment in the loop while countering the homogenization pressure of the underlying model.
- The cognitive apprenticeship framework clarifies the goal: the system should make expert methodological thinking visible and require the researcher to engage with it, not merely consume it.

---

### Section 5: Design Decisions and Rationale (~2,000 words)

**Purpose:** Document three design decisions using the IJDL design case pattern: decision point, alternatives considered, rationale, evidence, and design tension carried forward. Each decision is connected to the cognitive apprenticeship methods it operationalizes.

---

#### 5.1 Multi-Agent Architecture: From 44 to 24 Agents (~700 words)

**CA methods activated:** Modeling, Coaching, Scaffolding

**Opening frame (~50 words):**
In cognitive apprenticeship terms, the multi-agent architecture operationalizes three methods. Each agent models expert reasoning in its domain. Domain-specific feedback constitutes coaching. The 9-category task decomposition provides scaffolding. The consolidation from 44 to 24 is scaffolding calibration: reducing surface complexity so intellectual structure becomes visible.

**The trajectory (~120 words):**
- v1.0 (January 22, 2026): 20 agents in 5 categories. Core concept.
- v6.7 (peak): 44 agents across 9 categories. Maximum specialization.
- v11.0 (current): 24 agents across 9 categories. Principled consolidation.
- The 44-to-24 reduction is the narrative center: not a failure, but a design lesson about the relationship between specialization and usability.
- **Design failure integrated:** The journey to 44 included rapid expansion driven by domain-specific gaps (meta-analysis, systematic review, humanization), cross-platform support that multiplied complexity, and a 104-file Python memory module (built over 11 days, replaced by MCP). These expansions were not wasted; they revealed the thresholds at which complexity becomes counterproductive.

**Alternatives considered (~100 words):**
- Single-agent with diverse prompting: simpler, but one agent cannot hold competing epistemological commitments simultaneously.
- Modular tool-use agent similar to Cline/Obra architecture: maximizes user adoption breadth but sacrifices domain depth.
- Maintaining 44 agents: maximum specialization, but coordination overhead and user cognitive load scale superlinearly with agent count.

**Rationale for consolidation (~200 words):**
- Functional overlap analysis: several v6.7 agents performed structurally identical tasks in different topical clothing.
- Usage patterns: many specialized agents were rarely invoked because users defaulted to broader-scope agents.
- Li et al. (2025) "more agents is less" finding: beyond a threshold, additional agents generate coordination noise that degrades output quality.
- Brooks' subsumption architecture principle: simpler subsystems with clean ownership boundaries outperform complex subsystems with overlapping responsibilities.
- The 9-category structure (A: Theory, B: Literature, C: Methodology, D: Data, E: Analysis, F: Quality, G: Publication, H: Ethics, I: Specialized) maps to the actual phases of research design, not to the internal logic of the AI system.
- **Key sentence (CA):** "The consolidation from 44 to 24 agents was a scaffolding calibration: reducing the system's surface complexity so that the intellectual structure of research design, rather than the AI system's internal organization, became the visible architecture."

**Evidence of implementation (~60 words):**
- Architecture comparison diagram (Figure 4): v10 (44 agents) vs. v11 (24 agents), side by side.
- Agent consolidation table (Table 2): which v10 agents merged, which v11 agent absorbed them, and the functional rationale for each merger.

**Design tension carried forward (~70 words):**
Simplicity vs. specialization. 24 agents in 9 categories is more principled than 44, but still more complex than ChatGPT. For novice researchers, the 9-category architecture may itself be a barrier: knowing which agent to invoke requires prior knowledge of the research design process. This bet has not been tested.

**Table 2: Agent Consolidation** (abridged version for outline; full table for manuscript)

| Removed Agent(s) | Merged Into | Rationale |
|---|---|---|
| A3 (Devil's Advocate) + A6 (Visualizer) | A2 | Overlapping critical analysis functions |
| A4 (Ethics) + F4 (Bias Detection) | X1 (Research Guardian) | Both serve research integrity |
| B3 (Effect Size) + C6 (Data Guard) + C7 (Error Prevention) | C5 | All serve meta-analysis validation |
| B4 (Research Radar) | Removed entirely | Low usage |
| C4 (Materials) + D1 (Sampling) | C1 | Design-adjacent functions |
| F1 + F2 + F3 (Quality Assurance) | G2 | Quality checks consolidated into publication |
| G3 (Peer Review) + G4 (Pre-registration) | G2 | Publication workflow consolidated |
| H1 (Ethnography) + H2 (Action Research) | C2 | Qualitative methods consolidated |

---

#### 5.2 Verbalized Sampling and Typicality Scores: Structuring Diversity (~650 words)

**CA methods activated:** Reflection, Exploration

**Opening frame (~50 words):**
In cognitive apprenticeship terms, the T-Score is a reflection device that prompts metacognitive evaluation: "Am I choosing this because it is best, or because it is common?" The VS methodology's long-tail sampling supports exploration by presenting defensible alternatives the researcher would not encounter through modal convergence alone.

**The problem reframed (~100 words):**
- Instructional analogy: asking a curriculum to "be diverse" does not produce diversity; structural requirements for diverse content do.
- Similarly, prompting an AI to "provide diverse recommendations" is an instruction it can partially satisfy while still defaulting to high-probability outputs.
- Diversity must be structurally enforced, not instructionally requested.

**Alternatives considered (~100 words):**
- Standard prompting with diversity instructions: produces surface variation without genuine epistemic diversity.
- Retrieval-augmented generation from a curated methodology database: addresses gaps in training data but does not address distributional bias in the model itself.
- Random sampling with post-hoc filtering: introduces noise without principled diversity criteria.

**Rationale for Verbalized Sampling (~200 words):**
- VS (Zhao et al., 2024) provides a principled framework for exploring the full typicality spectrum rather than the high-probability peak.
- T-Score (Typicality Score): a measure of how common a recommendation is relative to the model's training distribution. T > 0.8 is modal; T < 0.4 is genuinely unconventional.
- Critical design decision: surface the T-Score to the researcher, not just use it internally. A researcher who sees T = 0.82 knows they are receiving the expected recommendation. One who sees T = 0.31 knows they are in unconventional territory and can decide accordingly.
- The T-Score becomes a metacognitive tool: it prompts the researcher to ask "is this the common choice because it is the best choice for my context, or because it is statistically common?"
- VS Arena: five epistemological persona agents (post-positivist, interpretivist, critical theorist, pragmatist, transformative) with cannotRecommend constraint arrays. Each persona is structurally prohibited from recommending what the other personas are likely to recommend, enforcing genuine epistemic diversity rather than simulated variation.
- **Platform co-evolution integrated:** Before Agent Teams (Feb 2026), the VS Arena required simulated diversity through subagent calls where all personas ran in the same context window. After Agent Teams, each persona agent operates in its own independent context window with genuine cross-critique, producing substantively different debate dynamics.
- **Key sentence (CA):** "The T-Score functions as a reflection device that prompts metacognitive evaluation of one's own recommendation preference, while the VS methodology's long-tail sampling supports exploration by presenting defensible alternatives that the researcher would not encounter through modal convergence alone."

**Evidence of implementation (~50 words):**
- T-Score calibration now uses OpenAlex frequency lookup for empirical grounding (v11.0).
- VS Arena persona configuration with cannotRecommend arrays enforces structural diversity.

**Design tension carried forward (~80 words):**
Diversity vs. coherence. The VS Arena generates five epistemologically divergent perspectives on a methodology question. Without synthesis, this can overwhelm a novice researcher. No arbitration mechanism currently exists in Diverga to help the researcher integrate competing recommendations. This is the most important unresolved design problem in Diverga's current state.

---

#### 5.3 Human Checkpoint System: Five Required Cognitive Forcing Functions (~650 words)

**CA methods activated:** Articulation + Cognitive Forcing Functions (Bucinca et al., 2021)

**Opening frame (~50 words):**
Each REQUIRED checkpoint functions as a cognitive forcing function that operationalizes the articulation method of cognitive apprenticeship: the researcher must verbalize a decision and its rationale before the system proceeds. The reduction from many checkpoints to five represents fading, a deliberate reduction of support as the researcher moves through the workflow.

**The problem reframed (~70 words):**
- Automation bias is not primarily a knowledge problem; researchers often know they should evaluate AI recommendations critically. It is a cognitive habit problem: under time pressure and with confident-sounding AI output, critical evaluation is the path of most resistance.
- Cognitive forcing functions (Bucinca et al., 2021): deliberate design elements that interrupt automatic processing and require effortful evaluation. The checkpoint is the learning design equivalent of a Socratic pause.

**The trajectory, with design failures integrated (~150 words):**
- v3.0 (Jan 23): Checkpoint system formally specified; AskUserQuestion mechanism established.
- v5.0 (Jan 25): Sisyphus Protocol introduced. AI proceeds autonomously between checkpoints. Added and removed the same day.
- v6.0 (Jan 25, Clean Slate): Sisyphus removed. Language shift from "I will proceed" to "May I proceed?" This is the moment the design philosophy crystallized.
- v8.1-v8.2 (Feb 9-12): Checkpoint enforcement strengthened via MCP. Before hooks (June 2025), checkpoints were behavioral instructions only; after hooks, they became architectural enforcement through PreToolUse interception of every agent call.
- **Checkpoint bug (v11.0):** All checkpoints auto-approved because a conditional logic error caused the pause mechanism to always return `{continue: true}`. The bug was not detected through user testing; it was detected through architectural review. The system appeared to have checkpoints; it did not. This failure illustrates how difficult genuine human oversight is to implement in autonomous AI systems.
- v11.1: SQLite-based fix. Five REQUIRED checkpoint gates with verified halt behavior.

**Alternatives considered (~100 words):**
- No checkpoints (full autonomy): maximizes workflow fluidity; eliminates genuine human oversight.
- Optional checkpoints (soft suggestions): preserves fluidity; but optional checkpoints are consistently skipped under time pressure, providing the appearance of oversight without its function.
- Checkpoints at every step (maximum oversight): cognitively burdensome; Bucinca et al. show that excessive forcing functions produce reactance and tool abandonment.

**Rationale for five required checkpoints (~130 words):**
- The five gate positions correspond to genuine cross-agent dependency points: decisions made at these points propagate through all subsequent agent outputs. A researcher who selects a post-positivist paradigm at Checkpoint 2 receives different outputs from the analysis agents than one who selects a critical theory paradigm.
- Five is a judgment call, not an empirically derived optimum. The design case documents this honestly: the number reflects the designer's best current assessment of where oversight adds more value than it subtracts in cognitive load.
- The checkpoint bug story is included not as a confession but as evidence: genuine human oversight in autonomous AI systems is difficult to implement and verify. This design lesson generalizes beyond Diverga.

**Evidence of implementation (~50 words):**
- Checkpoint flow diagram (Figure 5) showing the five REQUIRED gates and their positions in the workflow.
- Each checkpoint is labeled with the CA method it activates (Articulation).
- SQLite backend records researcher decisions for retrospective reflection.

**Design tension carried forward (~70 words):**
Autonomy vs. oversight. Five REQUIRED checkpoints is a defensible position, not a proven optimum. Checkpoint fatigue is real; five interruptions in a research design session may still be too many for some users. In the pre-fix v11.0, the silent auto-approval behavior may have emerged partly because the original checkpoint count was too high and was quietly engineered around. This tension is an open empirical question for the companion evaluation paper.

---

### Section 6: Design Tensions (~400 words)

**Purpose:** Frame the paper's three core tensions as inherent and unresolved, not as problems the design solved. This section gives the design case intellectual honesty and positions the tensions as hypotheses for the companion evaluation paper.

**Opening sentence:** Design cases in learning design often document what was built and why; the best ones also document what remains uncertain and why it matters. The following tensions are carried forward from Section 5 as open questions.

**Tension 1: Simplicity vs. Specialization (~120 words)**
- 24 agents in 9 categories is more principled than 44, but still more complex than a general-purpose tool.
- For novice researchers, the 9-category architecture may itself be a barrier: knowing which category of agent to invoke requires prior knowledge of the research design process.
- The design bets that the right users (doctoral students in research design contexts) have enough process knowledge to navigate the architecture. This bet has not been tested.

**Tension 2: Diversity vs. Coherence (~120 words)**
- The VS Arena generates five epistemologically divergent perspectives. For experienced researchers, this plurality is a resource. For novice researchers, it may be a source of confusion rather than illumination.
- No synthesis mechanism currently exists. The researcher must integrate competing perspectives without AI support.
- This is the most important unresolved design problem in Diverga's current state.

**Tension 3: Oversight Rigor vs. Workflow Fluidity (~120 words)**
- Five checkpoints interrupt cognitive flow. The design trades fluidity for genuine oversight, but the exchange rate is unknown.
- Checkpoint fatigue is not hypothetical: in the pre-fix v11.0, the silent auto-approval behavior may have emerged partly because the original checkpoint count was too high and was quietly engineered around.
- The companion evaluation paper will investigate whether five REQUIRED checkpoints produce the intended deliberative behavior or whether they produce habituated click-through.

**Closing sentence:** These tensions are not design failures; they are the honest boundary conditions of the current design. Naming them is a contribution to the field's understanding of what it means to design AI tools for epistemic support rather than mere efficiency.

**Table at end of Section 6:**
- **Table 4: Design Tensions Summary**

  | Tension | Design Decision | What Was Traded | Open Question |
  |---|---|---|---|
  | Simplicity vs. Specialization | Multi-Agent Architecture | User simplicity for domain coverage | Is 24 agents still too many for novice researchers? |
  | Diversity vs. Coherence | VS and T-Score | Recommendation convergence for epistemic plurality | Do novice researchers need synthesis support? |
  | Oversight Rigor vs. Workflow Fluidity | Human Checkpoints | Workflow fluidity for genuine human control | Do 5 checkpoints produce deliberation or click-through? |

---

### Section 7: Reflection and Future Directions (~400 words)

**Purpose:** Close the design case by connecting the design story to the broader field and to the companion papers.

**7.1 What This Design Story Reveals (~150 words)**
- Learning design principles are not limited to explicit instructional settings. The decisions documented in this paper (structural diversity enforcement, mandatory cognitive interruption, typicality transparency) are recognizable to instructional designers even when they appear in an AI tool's architecture.
- The "learning design in disguise" framing is descriptive, not rhetorical. Diverga shapes researcher behavior through its form, not through explicit instruction. This is analogous to how a well-designed PBL environment shapes student inquiry through task structure rather than direct teaching.
- The designer-as-researcher position, compensated by external collaboration, is a viable model for early-career researchers building the tools they study.
- The co-evolution with the Claude Code platform illustrates a broader phenomenon: AI tool designers are not designing on stable ground. Platform capabilities emerge and disappear; designs must adapt or become obsolete.

**7.2 Transferable Design Principles (~100 words)**
Three principles transfer to other AI tool designs for knowledge work:
1. **Structural enforcement over instructional exhortation:** Design diversity into the system's architecture, not into the system's instructions.
2. **Transparency as metacognitive prompt:** Surface the information the user needs to calibrate their reliance on the system.
3. **Checkpoints as cognitive forcing functions:** Design mandatory pause points at consequential decision nodes, not at every step.

**7.3 Connection to Companion Papers (~100 words)**
- This design case occupies EDR phases 1 and 2. The empirical evaluation of whether Diverga's design decisions produce the intended effects on researcher performance is Paper 3 (Computers & Education, targeted 2027).
- Paper 2 (BJET Special Issue on Artificial Agency, abstract due August 1, 2026) will address methodological questions about how to study artificial agency in multi-agent AI systems, using Diverga as the exemplar case. Authentic Learning (Herrington et al., 2010) will serve as the primary theoretical framework for Papers 2 and 3.
- The design case establishes the design rationale that Papers 2 and 3 can reference without re-documenting the full system.

---

### References

*Key references below; full formatted reference list to be prepared for submission.*

- Boling, E. (2010). The need for design cases: Disseminating design knowledge. *International Journal of Designs for Learning*, 1(1), 1-8.
- Bucinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision making. *CSCW*, 5, Article 188.
- Collins, A., Brown, J. S., & Newman, S. E. (1989). Cognitive apprenticeship: Teaching the crafts of reading, writing, and mathematics. In L. B. Resnick (Ed.), *Knowing, learning, and instruction: Essays in honor of Robert Glaser* (pp. 453-494). Erlbaum.
- Collins, A., Brown, J. S., & Holum, A. (1991). Cognitive apprenticeship: Making thinking visible. *American Educator*, 15(3), 6-11.
- Herrington, J., Reeves, T. C., & Oliver, R. (2010). *A guide to authentic e-learning*. Routledge.
- Li, Z., et al. (2025). More agents is less: Scaling properties of multi-agent LLM systems. *arXiv:2602.03794*.
- Markauskaite, L., & Goodyear, P. (2017). *Epistemic fluency and professional education*. Springer.
- McKenney, S., & Reeves, T. C. (2012). *Conducting educational design research*. Routledge.
- Microsoft Research. (2025). *AI tools and critical thinking in knowledge work*. [Citation details TBD].
- Norman, D. A. (2013). *The design of everyday things* (revised ed.). Basic Books.
- Podolefsky, N. S., Moore, E. B., & Perkins, K. K. (2013). Implicit scaffolding in interactive simulations: Design, learner use, and affective responses. *arXiv:1306.6544*.
- Smith, K. M. (2010). Producing the rigorous design case. *International Journal of Designs for Learning*, 1(1), 9-20.
- Springer Nature. (2025). *AI use in academic research*. [Citation details TBD].
- Wang, T., et al. (2024). Mixture-of-agents yields emergent collaborative intelligence. *Together AI Technical Report*.
- Yang, M., & Harbor, J. (2023). Authentic learning design failures: The need for learner and contextual analysis and participatory design. *International Journal of Designs for Learning*, 14(1), 88-105.
- Zhao, Y., et al. (2024). Verbalized sampling for language model selection. *arXiv:2510.01171*.

---

## Word Count Estimates by Section

| Section | Estimated Words |
|---|---|
| Abstract (not in body count) | ~200 |
| Section 1: Introduction (with CA lens) | ~600 |
| Section 2: Design Context | ~400 |
| Section 3: Design Process: Five Iterative Cycles [NEW] | ~600 |
| Section 4: Design Problem | ~400 |
| Section 5.1: Multi-Agent Architecture | ~700 |
| Section 5.2: Verbalized Sampling and T-Scores | ~650 |
| Section 5.3: Human Checkpoint System | ~650 |
| Section 6: Design Tensions | ~400 |
| Section 7: Reflection and Future Directions | ~400 |
| **Total (body text)** | **~4,800** |

*200 words of flexibility remain under the ~5,000-word target.*

---

## Complete Figure and Table Inventory

| ID | Type | Content | Section | Status |
|---|---|---|---|---|
| Figure 1 | Conceptual Framework | EDR model (outer) + Cognitive Apprenticeship 6 methods (middle) + 3 Diverga Design Decisions (inner) + Platform Evolution bar (bottom) | 1 or 3 | Generate (v2) |
| Figure 2 | EDR Cycles | 5 cycles mapped to horizontal timeline with agent count overlay, key events, and platform milestones | 3 | Generate (v2) |
| Figure 3 | Platform-Design Co-evolution | Two parallel timelines: Claude Code features (top) and Diverga design changes (bottom) with connecting arrows | 3 | Generate (v2) |
| Figure 4 | Architecture Comparison | v10 (44 agents, 9 categories) vs. v11 (24 agents, 9 categories) side by side | 5.1 | Generate (v2) |
| Figure 5 | Checkpoint Flow | 5 REQUIRED checkpoint gates in research workflow with CA method labels | 5.3 | Generate (v2) |
| Table 1 | Comparison | Diverga vs. Elicit vs. Consensus vs. ChatGPT on 5 dimensions | 2 | Draft above |
| Table 2 | Agent Consolidation | Removed agents, merged-into target, functional rationale | 5.1 | Draft above |
| Table 3 | CA Mapping | 6 CA methods mapped to Diverga mechanisms and design decisions | 1 | Draft below |
| Table 4 | Design Tensions | 3 tensions with traded values and open questions | 6 | Draft above |

### Table 3: Cognitive Apprenticeship Mapping (Full Draft)

| CA Method | Diverga Mechanism | Design Decision | How It Works |
|---|---|---|---|
| Modeling | Agent-generated expert reasoning; VS Arena multi-perspective demonstration | Multi-Agent Architecture (5.1) | Each agent models domain-specific expert thinking; VS Arena models how experts from different paradigms reason about the same problem |
| Coaching | Agent-specific contextual feedback; domain-calibrated guidance | Multi-Agent Architecture (5.1) | Agents provide feedback tailored to the researcher's specific study context, not generic advice |
| Scaffolding | 9-category task decomposition; fading via 44-to-24 consolidation | Multi-Agent Architecture (5.1) | The category structure decomposes research design into manageable phases; consolidation reduces scaffolding complexity |
| Reflection | T-Score metacognitive prompts; typicality transparency | VS and T-Scores (5.2) | T-Score makes the commonality of each recommendation visible, prompting the researcher to evaluate their own preference |
| Exploration | Long-tail sampling (T < 0.4); VS Arena epistemological diversity | VS and T-Scores (5.2) | VS samples across the full typicality spectrum; low-T recommendations push researchers into unfamiliar methodological territory |
| Articulation | Checkpoint-required decision rationale; Decision Audit Trail | Human Checkpoints (5.3) | Checkpoints require the researcher to state and justify a decision before the system proceeds |

---

## Design Failures Integrated into Sections (Cross-Reference)

| Failure | Where Integrated | Purpose in Narrative |
|---|---|---|
| Sisyphus Protocol (added and removed same day) | Section 3 (Cycle 2), Section 5.3 (trajectory) | Establishes foundational design principle; fastest failure = strongest lesson |
| Cross-platform support (41-day lifespan) | Section 3 (Cycle 3), Section 5.1 (trajectory) | Illustrates expansion-contraction pattern; platform dependency decisions |
| Checkpoint bug (silent auto-approval) | Section 3 (Cycle 4), Section 5.3 (trajectory) | Core evidence for difficulty of genuine human oversight in AI systems |
| lib/memory Python module (104 files, 11 days) | Section 3 (Cycle 4), Section 5.1 (trajectory) | Illustrates how MCP replaced bespoke infrastructure |
| Typographic rules reversal (em dash enforcement then prohibition) | Not included (too minor for word count) | Reserved for extended version if needed |

---

## Platform Co-evolution Key Examples (Cross-Reference)

| Platform Feature | Date | Design Impact | Where Integrated |
|---|---|---|---|
| Hooks system | June 2025 | Before: checkpoints were behavioral instructions only; After: architectural enforcement via PreToolUse interception | Section 3 (closing), Section 5.3 |
| Skills system | October 2025 | Enabled SKILL.md as agent definition format; entire architecture built on this primitive | Section 3 (Cycle 1) |
| Plugins system | October 2025 | Before: manual setup required; After: marketplace distribution; 8 plugin discovery fix commits in one day | Section 3 (Cycle 3) |
| Agent Teams | February 2026 | Before: VS Arena required simulated diversity via subagents; After: genuine multi-agent debate with independent context windows | Section 3 (Cycle 5), Section 5.2 |
| 1M context window | March 2026 | Reduced compaction pressure; enabled larger agent instructions | Section 2 (technical context) |

---

## Key Narrative Threads

1. **The consolidation arc:** 20 to 44 to 24. Expansion was not failure; it was necessary exploration that revealed the thresholds at which complexity becomes counterproductive. The consolidation is the design lesson.

2. **The checkpoint arc:** Sisyphus Protocol (autonomy) to Clean Slate (human control) to checkpoint bug (false oversight) to SQLite fix (verified oversight). Each failure deepened the understanding of what genuine human oversight requires.

3. **The platform dependency arc:** Claude Code's evolving capabilities (hooks, skills, plugins, Agent Teams) both enabled and constrained design choices. The designer was not building on stable ground; they were building on a platform that changed 176 times in 2025 alone.

4. **The learning design arc:** What looks like an engineering story is a learning design story. The cognitive apprenticeship mapping makes this visible: every architectural decision can be read as a pedagogical decision about how to make expert methodological thinking visible to developing researchers.
