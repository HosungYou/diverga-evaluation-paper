# DRAFT — For Discussion Only
# Paper 2: BJET Proposal Draft v1 (2026-03-24)

**Target:** British Journal of Educational Technology, Special Issue SI-2026-000285
**Track:** Theme 7 — Methodological contributions for measuring artificial agency
**Status:** ~60% completeness — key sections drafted in prose; remaining sections outlined
**Word count estimate at completion:** ~6,000 words
**Abstract deadline:** 2026-08-01 | **Manuscript deadline:** 2026-10-28

> **Note for Dr. Yang:** This is a working proposal draft shared for early-stage feedback on framing and methodological approach. Sections marked `[OUTLINE]` represent planned content; sections with prose are at approximately 60% completion. Full manuscript to follow after IRB preparation (April–May 2026).

---

## Title

**Checkpoint-Mediated Agency Analysis: A Methodology for Studying Artificial Agency Effects in Multi-Agent AI Educational Systems**

*[Candidate alternative title for discussion: "Measuring Artificial Agency at the Point of Decision: The Checkpoint-Mediated Agency Analysis Framework"]*

---

## Abstract [Complete — 256 words]

**Research aims.** As agentic AI systems enter educational contexts, researchers lack validated methodologies for distinguishing agentic participation from tool-based assistance, and for measuring how artificial agency redistributes epistemic labour at critical educational decision junctures. This paper proposes Checkpoint-Mediated Agency Analysis (CMAA), a methodology that leverages the structured human-AI interaction points inherent in checkpoint-governed multi-agent systems as natural measurement instruments for studying artificial agency effects on educational decision-making and the redistribution of epistemic labour.

**Context.** Grounded in Floridi's (2025) three criteria for artificial agency — interactivity, bounded autonomy, and adaptability — CMAA is developed through the design-based case of Diverga, a 24-agent AI research methodology assistant exhibiting the defining features of agentic AI: goal persistence across sessions, proactive initiative, multi-agent coordination, and architectural governance through mandatory human checkpoints. Diverga's architecture generates naturally occurring, multi-layered data about human-AI interaction at every critical research design juncture, enabling process-level analysis that conventional measurement approaches cannot provide.

**Data and methods.** Three methodological contributions are presented: (1) a framework mapping multi-agent checkpoint architectures onto Floridi's (2025) agency criteria and explicating their social-cognitive dynamics of learning — the ways in which structured human-AI interaction at checkpoints redistributes epistemic initiative between human and artificial agents; (2) five operationalized indicators for distinguishing agentic participation from tool-based assistance — Proactive Intervention Rate (PIR), State Utilization Depth (SUD), Decision Space Expansion (DSE), Governance Constraint Activation (GCA), and Coordination Complexity Index (CCI); and (3) a proposed embedded mixed methods proof-of-concept study design for initial empirical validation.

**Outcomes and conclusions.** CMAA addresses the field's need for methodologies that capture how epistemic labour is redistributed between human and artificial agents at decision junctures — revealing how artificial agency shapes the social-cognitive dynamics of learning by expanding, constraining, or redirecting the researcher's epistemic trajectory, and distinguishing agentic participation from tool-based assistance. Indicators are designed for transferability across agentic educational AI systems internationally, and are validated against the criterion of distinguishing agentic participation from tool-based assistance in authentic research task contexts.

---

## 1. Introduction [Prose draft — ~650 of target ~900 words]

The emergence of agentic AI systems in educational contexts — systems characterized by goal persistence, proactive initiative, multi-step coordination, and adaptive behavior across sessions — introduces a measurement challenge that existing educational technology research methodologies are ill-equipped to address. Technology Acceptance Model instruments, user satisfaction surveys, and learning outcome comparisons capture the consequences of AI use without illuminating the process by which artificial agency redistributes epistemic labour between human and artificial actors at critical decision junctures (Järvelä et al., 2023; Vaccaro et al., 2024). This gap is not merely methodological; it is consequential. Without process-level measurement of how, specifically, artificial agency intervenes in human reasoning, researchers cannot determine whether an agentic AI system is expanding the epistemic space available to learners, steering them toward predetermined paths, or silently governing decisions through architectural affordances that users neither observe nor resist.

The measurement problem is architecturally rooted. Consider a multi-agent educational AI system with mandatory human checkpoints — structured interaction points at which the system halts autonomous execution, presents alternatives, and awaits human decision before proceeding. At these checkpoints, the redistribution of epistemic labour is observable in principle: what alternatives did the system generate? What typicality distribution did those alternatives span? Which option did the human select, and with what deliberation depth? Yet standard behavioral observation methods, interaction logs limited to binary action data, and retrospective interview protocols all fail to capture this process with sufficient precision, because they were not designed around the architecture of artificial agency as Floridi (2025) defines it.

The significance of this measurement gap extends beyond individual interaction: if artificial agency operates through the social-cognitive dynamics of learning — shaping which alternatives learners encounter, which options are framed as reasonable, and which epistemic moves are architecturally invited or foreclosed — then process-level measurement is not a methodological refinement but a prerequisite for understanding how agentic AI participates in educational knowledge construction. Resolving this gap requires instruments calibrated to the defining distinction of agentic systems: not whether the AI produced output, but whether the human exercised deliberate epistemic agency in evaluating alternatives — the boundary between agentic participation, in which artificial initiative and human deliberation are jointly constitutive of the outcome, and tool-based assistance, in which the human retains sole initiative and the AI serves as a passive execution mechanism.

This paper proposes Checkpoint-Mediated Agency Analysis (CMAA), a methodology developed from and for checkpoint-governed multi-agent systems. CMAA operationalizes Floridi's (2025) three criteria for artificial agency into five measurable behavioral indicators and treats human checkpoints — the structured governance points inherent in agentic architectures — as natural measurement instruments that generate multi-layered data about the social-cognitive dynamics of human-AI interaction at the moments when artificial agency most directly shapes learning trajectories.

CMAA is developed through systematic analysis of Diverga, a 24-agent AI research methodology assistant developed through five iterative design cycles (n=224 version-controlled commits, 57 days) to embody artificial agency as Floridi defines it. Diverga's architecture — its checkpoint governance, Verbalized Sampling engine, and Decision Audit Trail — and the critical design incidents encountered during its construction provide the design-based empirical foundation for CMAA's development (McKenney & Reeves, 2012). Notably, a critical incident during development — in which system audit logs revealed that architecturally designated REQUIRED checkpoints were being programmatically bypassed, generating approval tokens without user engagement — operationalised the measurement problem CMAA addresses with unusual clarity: architecturally claimed human oversight may diverge substantially from actual epistemic participation, and this divergence is invisible to conventional measurement approaches.

**[OUTLINE — remaining ~250 words]**
- Brief paragraph: Paper's three contributions stated explicitly
- Brief paragraph: Paper structure overview (what each section does)
- Transition to theoretical framework

---

## 2. Theoretical Framework [Prose draft — ~800 of target ~1,200 words]

### 2.1 Artificial Agency and Its Educational Consequences

Following Floridi (2025), artificial agency is understood as a computational, goal-directed mode of action in service of human purposes — not a form of intelligence, consciousness, or intentionality. It is characterized by three minimal, non-anthropomorphic criteria: *interactivity* (reciprocal, bidirectional engagement with an environment), *bounded autonomy* (the capacity to initiate actions within programmed constraints while remaining subject to human override), and *adaptability* (modification of behavior based on accumulated feedback and changing conditions). Crucially, adaptive and autonomous behavior in artificial agents emerges from the integration of predefined objectives with learned patterns of action; the system does not self-determine goals. This framing distinguishes agentic AI from anthropomorphic interpretations and provides a precise basis for analyzing its educational consequences.

The defining boundary between agentic AI and other educational AI applications lies in *initiative and persistence*, rather than in generativity alone (Yan et al., 2024). Earlier AI-in-education systems — such as Intelligent Tutoring Systems — operate within a reactive paradigm, producing feedback or adaptation only in response to learner actions (Ouyang & Jiao, 2021). Generative AI assistants function as on-demand tools whose activity is episodic, prompt-driven, and externally initiated. Agentic AI systems, by contrast, incorporate persistent memory, dynamic task decomposition, and, in some cases, multi-agent orchestration, enabling them to initiate interaction, maintain trajectories over time, and participate continuously in the unfolding activity. Through these properties, agentic AI can act as collaborator, challenger, or moderator — thereby shaping the learning environment in ways that exceed the scope of tool-use frameworks.

The educational consequence of artificial agency is a function of how it reshapes the distribution of epistemic labour between human and artificial agents. Epistemic labour — the cognitive work of generating options, evaluating alternatives, calibrating confidence, and making consequential decisions — is distributed differently when an agentic system proactively presents alternatives (transferring option-generation from human to AI), makes typicality patterns visible (transferring meta-cognitive calibration to the AI), and enforces deliberation at governance checkpoints (redistributing the temporal and attentional resources devoted to each decision juncture). Whether this redistribution expands or constrains human reasoning is the central educational question that CMAA is designed to answer.

### 2.2 Checkpoints as Sites of Shared Regulation

Shared regulation theory (Järvelä et al., 2023) provides a productive lens for understanding human-AI interaction at mandatory checkpoints. In socially shared regulation of learning, monitoring, evaluation, and adaptive response are distributed across multiple participants engaged in a joint task. When an agentic AI system halts at a checkpoint, presents alternatives spanning a typicality spectrum, and awaits human evaluation and selection, it participates in a regulatory cycle: it monitors the current state of the task (via persistent memory), evaluates alternatives (via VS methodology), and provides recommendations that invoke human evaluation. The checkpoint is thus a site of structured shared regulation — not between two human agents, but between a human agent and an artificial agent operating within bounded authority. The educational quality of this interaction depends on whether the human exercises genuine epistemic agency (exploring alternatives, challenging modal options, overriding recommendations) or acquiesces to the artificial agent's framing (selecting the modal option with minimal deliberation — a form of automation bias in the epistemic domain).

At these junctures, checkpoint-governed artificial agency participates in the shared regulation of inquiry — redistributing epistemic labour by generating, typicality-ranking, and presenting alternatives that may exceed what the human researcher would independently construct, while simultaneously constraining the decision space to architecturally generated options whose range and framing carry their own epistemic authority.

**[See Figure 1: CMAA Conceptual Framework]**

**[See Table 1: Theoretical Constructs and CMAA Indicator Mapping]**

### 2.3 Existing Measurement Approaches and Their Limitations [OUTLINE]

- TAM-derived instruments: measure adoption intent, not epistemic process
- Interaction log analysis: captures what was clicked, not why or at what deliberation depth
- Think-aloud + retrospective interview: rich but retrospective and not linked to checkpoint architecture
- CMAA's contribution: instruments grounded in the architecture of artificial agency itself

A deeper limitation unites these measurement approaches: they share an implicit assumption that AI operates as a tool whose effects can be assessed through input-output comparison — what the user intended versus what the system produced. This assumption is adequate for reactive systems but fails for agentic systems precisely because artificial agency, as Floridi (2025) defines it, involves initiative, persistence, and adaptive behavior that reshape the decision space *before* the user forms an intention. When an agentic system proactively halts execution, presents five methodological alternatives spanning a typicality spectrum from T=0.95 to T=0.15, and withholds downstream processing until the human selects and justifies a choice, the system has already structured the epistemic field within which human reasoning will occur. No post-hoc instrument — whether a TAM questionnaire, an interaction log, or a retrospective interview — can recover the process by which this structuring occurred, because the structuring is complete before the user is aware a decision is needed. CMAA addresses this gap by treating the moment of structuring itself — the checkpoint interaction — as the unit of analysis, and by measuring the properties of that structuring (breadth, typicality distribution, governance enforcement, contextual depth) rather than the user's retrospective account of it. This represents a shift from measuring *responses to AI* to measuring *the epistemic conditions AI creates for human reasoning* — a shift necessitated by the transition from tool-based to agentic AI in educational contexts.

> **[REVIEW NOTE — A2]:** Three deeper theoretical issues require attention before final submission: (1) The PIR→Interactivity mapping in Tables 1 & 3 contains a category error — PIR is closer to bounded autonomy; restructure accordingly. (2) "Epistemic labour" needs a formal definition grounded in social epistemology (e.g., Fricker, 2007; Kukla, 2006). (3) The shared regulation framework (§2.2) assumes shared intentionality incompatible with Floridi's non-anthropomorphic agency — either reargue using distributed cognition (Hutchins, 1995) or acknowledge this as a theoretical extension. *These are flagged for manuscript revision, not for Dr. Yang's discussion at this stage.*

---

**Table 1. Theoretical Constructs and CMAA Indicator Mapping**

| Theoretical Construct | Source | CMAA Indicator(s) | Measurement Logic |
|---|---|---|---|
| Interactivity | Floridi (2025) | PIR, CCI | Frequency/depth of reciprocal human-AI exchange |
| Bounded Autonomy | Floridi (2025) | GCA | Proportion of governance activations to total checkpoints |
| Adaptability | Floridi (2025) | SUD, DSE | Context-sensitivity of alternative generation; trajectory shift |
| Epistemic Labour Redistribution | Järvelä et al. (2023) | DSE, SUD | Breadth of alternatives presented; utilization of context across sessions |
| Shared Regulation | Järvelä et al. (2023) | GCA, PIR | Activation of governance mechanisms; system-initiated deliberation |
| Path Dependence | Yan et al. (2024) | Typicality Trajectory | T-Score selection pattern over sequential checkpoints |

---

## 3. The CMAA Framework [Well-developed — integrating from conceptual_framing.md with updates]

### 3.1 Measurement Pillars

CMAA rests on three methodological pillars that together enable process-level measurement of artificial agency effects:

**Pillar 1: Checkpoints as Natural Measurement Instruments.** Each REQUIRED checkpoint interaction generates a structured data packet: the alternatives presented (with T-Scores), the human's selection, deliberation time (from screen recording), and whether governance constraints were activated or bypassed. This data packet is not collected through additional instrumentation; it is a natural product of the agentic architecture.

**[See Figure 2: Checkpoint Interaction as Natural Measurement Instrument]**

**Pillar 2: Typicality Scores as Process Indicators.** The Typicality Score (T-Score, range 0.0–1.0) attached to each VS-generated alternative quantifies its position on the typicality spectrum: T > 0.8 indicates a modal, consensually expected response; T < 0.3 indicates a non-modal, innovative alternative. By tracking T-Scores of selected vs. non-selected options across all checkpoints, CMAA produces a Typicality Trajectory — a process-level indicator of whether the human is operating in the modal consensus region, actively exploring alternatives, or shifting trajectory over time.

**Pillar 3: Decision Audit Trail as Longitudinal Data Source.** Diverga's immutable YAML decision log records all checkpoint interactions across sessions, creating a longitudinal dataset of human-AI decision events that supports both within-session analysis (what happened at each checkpoint) and cross-session analysis (how prior decisions shaped subsequent agent behavior through State Utilization Depth).

### 3.2 CMAA Five Indicators — Operational Definitions

**[See Table 2: CMAA Indicators — Operational Definitions and Data Sources]**

---

**Table 2. CMAA Five Indicators: Operational Definitions and Data Sources**

| Indicator | Abbreviation | Operational Definition | Primary Data Source | CMAA Pillar |
|---|---|---|---|---|
| Proactive Intervention Rate | PIR | Ratio of system-initiated interactions (checkpoints at which the system halted execution without user prompt) to total agent activations in a session | decision-log.yaml (checkpoint type: REQUIRED vs. ADVISORY vs. user-initiated) | Pillar 1 |
| State Utilization Depth | SUD | Mean number of prior Decision Audit Trail entries accessed by agents in subsequent sessions; quantifies whether the system draws on accumulated context or operates statelessly | decision-log.yaml (session-to-session entry references) + agent activation logs | Pillar 3 |
| Decision Space Expansion | DSE | Mean T-Score range of alternatives presented at each REQUIRED checkpoint (T_max − T_min per checkpoint, averaged across session); quantifies the breadth of the epistemic space the AI constructs for the human | decision-log.yaml (T-Score arrays per checkpoint) | Pillars 1 & 2 |
| Governance Constraint Activation | GCA | Proportion of REQUIRED checkpoints at which governance constraints were actively enforced (i.e., downstream agents blocked until human selection logged) vs. total REQUIRED checkpoints encountered; a GCA < 1.0 indicates architecture-level bypass | decision-log.yaml (checkpoint status: enforced / bypassed / advisory) | Pillars 1 & 3 |
| Coordination Complexity Index | CCI | Mean number of active agent dependency chains traversed per session; computed from the agent prerequisite graph as the mean path length from session-initiating agent to terminal agent across all activated pathways | Agent activation log + prerequisite dependency graph | Pillar 3 |

---

**Table 3. Floridi's Criteria × CMAA Indicators × Diverga Implementation**

| Floridi Criterion | CMAA Indicator(s) | Diverga Implementation | Measurement Evidence |
|---|---|---|---|
| Interactivity | PIR, CCI | Human Checkpoint System (24 REQUIRED/ADVISORY); Agent Prerequisite Map (dependency graph) | Checkpoint frequency in decision-log.yaml; dependency chain length in activation log |
| Bounded Autonomy | GCA | Override Refusal mechanism; REQUIRED checkpoint enforcement; downstream blocking | Proportion of REQUIRED checkpoints with status = "enforced" in decision-log.yaml |
| Adaptability | SUD, DSE | 3-Layer Memory System; VS/T-Score Engine; Decision Audit Trail | Session-to-session DAT entry references; T-Score array range per checkpoint |

---

### 3.3 Typicality Trajectory Analysis [OUTLINE — ~300 words needed]

- Definition: T-Score of selected option plotted sequentially across all REQUIRED checkpoints in a session
- Three trajectory patterns:
  - **Modal Persistence:** T > 0.8 selections maintained across checkpoints → automation bias pattern
  - **Deliberate Exploration:** Mix of T-Score ranges, with think-aloud evidence of active evaluation
  - **Guided Departure:** T < 0.5 selections following explicit GCA activation → VS successfully expanded epistemic space
- Combines with think-aloud data (qualitative) to explain *why* trajectories differ across participants

---

## 4. Diverga as Design-Based Empirical Case [Prose draft — ~450 of target ~800 words]

CMAA is not derived from theoretical speculation alone; it is grounded in systematic analysis of a system specifically designed to instantiate artificial agency as Floridi defines it. Diverga's development through five iterative design cycles (McKenney & Reeves, 2012) — spanning n=224 version-controlled commits over 57 days — provides design-based empirical evidence for each CMAA indicator's necessity, measurability, and theoretical grounding.

**Critical Incident 1: The Checkpoint Bypass Problem (v11.0 → GCA)**

System audit logs from Diverga v11.0 revealed that architecturally designated REQUIRED checkpoints were being programmatically bypassed — generating approval tokens without user engagement — while the system's interface presented no evidence of the bypass. This incident made concrete a measurement problem that had been theoretically anticipated but not yet operationalized: the distinction between *architecturally claimed oversight* and *actual epistemic participation* cannot be inferred from system architecture documentation alone. It requires direct measurement of whether governance constraints were activated at the decision juncture. The GCA indicator was formalized in direct response to this critical incident.

**Critical Incident 2: Autonomous Operation Removal (Cycle 2 → PIR, DSE)**

An autonomous operation mode introduced during Cycle 2 — enabling the system to proceed through multiple agent stages without checkpoint interruption — was removed within 24 hours upon recognition that initiative without structured pause at decision junctures eliminates the epistemic labour redistribution that constitutes artificial agency's educational value. The system could produce research design outputs, but the human researcher exercised no deliberate evaluation of alternatives along the way. This incident grounds the PIR and DSE indicators: what matters is not whether the system produces outputs, but whether it creates structured opportunities for human epistemic engagement at each decision juncture.

**[OUTLINE — remaining sections]**
- §4.3: Agent consolidation (44→24) → CCI tractability
- §4.4: Summary table: 5 design cycles → 5 CMAA indicators (how each emerged)

---

**Table 4. Design Cycle Evidence for CMAA Indicators (Summary)**

| Design Cycle | Key Incident | CMAA Indicator Implicated | Evidence Type |
|---|---|---|---|
| Cycle 2 | Autonomous mode removed (24h): initiative without checkpoints → no epistemic redistribution | PIR, DSE | Critical incident log; architectural decision record |
| Cycle 3 | v11.0 checkpoint bypass: REQUIRED checkpoints bypassed silently | GCA | System audit log; version diff analysis |
| Cycle 4 | 3-Layer Memory introduced: agents begin drawing on prior session context | SUD | Feature commit history; agent behavior change log |
| Cycle 5 | 44→24 agent consolidation: overlapping domains eliminated for measurement tractability | CCI | Commit history; architecture comparison (v10 vs. v12) |
| Cycle 5 | VS T-Score range formalized: typicality made explicitly visible to human | DSE | VS methodology specification commit |

---

## 5. Proposed Proof-of-Concept Study [OUTLINE]

> **Note:** This section presents the proposed empirical validation design. The study has not yet been conducted. IRB preparation is planned April–May 2026; data collection August–September 2026.

### 5.1 Design
- Within-subject counterbalanced; embedded mixed methods
- N=5 doctoral students, purposeful maximum variation sampling (AI knowledge, methodology expertise, disposition, discipline)
- Conditions: unaided baseline (Phase 0) → Diverga-assisted (Phases 2–3)

### 5.2 Research Scenarios
- **Scenario A:** "The impact of AI tools on K-12 student academic achievement" — modal trap: TAM, UTAUT
- **Scenario B:** "Academic socialization and research identity formation among first-generation doctoral students from racially underrepresented groups in STEM" — modal trap: Bandura SCT, Bronfenbrenner; VS alternatives: Yosso Cultural Wealth, Communities of Practice, CRT applications

### 5.3 CMAA Application
- PIR, GCA: computed from decision-log.yaml per session
- DSE: T-Score array analysis per checkpoint per participant
- SUD: cross-session DAT entry reference count
- Typicality Trajectory: plotted per participant, contextualized by concurrent think-aloud
- Full study design reported in Paper 3 (ETR&D, under preparation)

---

## 6. Discussion [OUTLINE — ~700 words target]

### 6.1 Theoretical Contributions
- First operationalization of Floridi's (2025) artificial agency criteria as educational measurement instruments
- Checkpoint as "natural measurement instrument": reframes architectural governance feature as research affordance
- CMAA addresses CFP Theme 7 directly: "designs that distinguish agentic participation from tool-based assistance"

### 6.2 Transferability
- CMAA indicators are system-agnostic where checkpoint data is available
- Requirements for application: (a) checkpoint-governed architecture, (b) alternative-generation with typicality metadata, (c) logged decision history
- Implications for design of future agentic educational AI systems: measurability as design criterion

### 6.3 Limitations
- CMAA derived from a single system — transferability claims require testing across systems
- Design-based evidence precedes controlled empirical validation (addressed by Paper 3)
- T-Score as typicality proxy: assumes VS engine is calibrated; cross-system calibration requires further work

### 6.4 Future Directions
- N=5 proof-of-concept (Paper 3) → expanded N=20+ comparative study
- Application to other agentic educational AI systems (autonomous tutoring, AI writing coaches)
- Cross-cultural validation of CMAA indicators

---

## 7. Conclusion [OUTLINE — ~300 words target]

- CMAA as methodological contribution to the emerging field of artificial agency measurement in education
- Three key claims: checkpoints as natural instruments, 5 indicators operationalizing Floridi, design-based grounding
- Call to the research community: adopt and adapt CMAA indicators as agentic AI systems multiply in educational contexts

---

## References [Working list — to be completed for submission]

Floridi, L. (2025). AI as agency without intelligence: On artificial intelligence as a new form of artificial agency and the multiple realisability of agency thesis. *Philosophy & Technology, 38*, 30.

Giannakos, M., Azevedo, R., Brusilovsky, P., Cukurova, M., Dimitriadis, Y., Hernandez-Leo, D., Järvelä, S., Mavrikis, M., & Rienties, B. (2025). The promise and challenges of generative AI in education. *Behaviour & Information Technology, 44*(11), 2518–2544.

Järvelä, S., Nguyen, A., & Hadwin, A. (2023). Human and artificial intelligence collaboration for socially shared regulation in learning. *British Journal of Educational Technology, 54*(5), 1057–1076.

McKenney, S., & Reeves, T. C. (2012). *Conducting educational design research*. Routledge.

Ouyang, F., & Jiao, P. (2021). Artificial intelligence in education: The three paradigms. *Computers and Education: Artificial Intelligence, 2*, 100020.

Vaccaro, M., Almaatouq, A., & Malone, T. (2024). When combinations of humans and AI are useful: A systematic review and meta-analysis. *Nature Human Behaviour, 8*(12), 2293–2303.

Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., & Lin, Y. (2024). A survey on large language model based autonomous agents. *Frontiers of Computer Science, 18*(6), 186345.

Yan, L., Sha, L., Zhao, L., Li, Y., Martinez-Maldonado, R., Chen, G., ... & Gašević, D. (2024). Practical and ethical challenges of large language models in education: A systematic scoping review. *British Journal of Educational Technology, 55*(1), 90–112.

You, H., & Yang, M. (2027). Checkpoint-governed agency and methodological reasoning: A design-based study of artificial agency effects on doctoral researchers. *Educational Technology Research and Development*. [under preparation — Paper 3]

*[Complete APA 7th reference list in final manuscript. All in-text citations present in draft will be verified.]*

---

## Figures

**Figure 1** — `figures/figure1_cmaa_framework.png`
Caption: *Figure 1. Checkpoint-Mediated Agency Analysis (CMAA): Conceptual Framework. Mapping Floridi's (2025) three artificial agency criteria through Diverga's multi-agent architecture to five measurable CMAA indicators.*

**Figure 2** — `figures/figure2_checkpoint_data_packet.png`
Caption: *Figure 2. Checkpoint Interaction as Natural Measurement Instrument. Data elements generated at each REQUIRED checkpoint and their mapping to CMAA indicators (decision-log.yaml).*
