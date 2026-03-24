# BJET Special Issue: Conceptual Framing

## "Agentic AI in Education: Artificial Agency and the Social-Cognitive Dynamics of Learning"

**Paper 2: Methodological Approaches for Studying Artificial Agency**

**Authors:** Hosung You (Pennsylvania State University), Mohan Yang (Texas A&M University)

**Target:** BJET Special Issue SI-2026-000285
**Abstract deadline:** 2026-08-01 | **Full manuscript:** 2026-10-28

---

## 1. Reframing Diverga as Artificial Agency

### 1.1 Mapping Diverga to Floridi's Three Criteria

Floridi (2025) defines artificial agency as a computational, goal-directed mode of action defined by human purposes, characterized by three minimal criteria: interactivity, bounded autonomy, and adaptability. Diverga's multi-agent checkpoint architecture maps onto each criterion with unusual precision, making it a strong case for operationalizing and measuring artificial agency in educational contexts.

#### Criterion 1: Interactivity

Interactivity refers to the capacity to perceive and respond to environmental states and inputs in a bidirectional manner, not merely to receive instructions and produce outputs.

Diverga exhibits interactivity at multiple levels:

- **Agent-to-user interaction.** The Human Checkpoint System creates structured bidirectional exchanges. At REQUIRED checkpoints (CP_RESEARCH_DIRECTION, CP_PARADIGM_SELECTION, CP_THEORY_SELECTION, CP_METHODOLOGY_APPROVAL), the system halts execution and presents VS-generated alternatives with Typicality Scores (T-Scores), then waits for the researcher's explicit selection before proceeding. This is not passive output delivery; it is a turn-taking dialogue where the system's next state is contingent on human input.
- **Agent-to-agent interaction.** Diverga's 24 agents operate within a dependency graph: upstream agents (e.g., A1: Research Question Refiner) generate outputs that downstream agents (e.g., A2: Theory Architect, C1/C2/C3: Design Consultants) consume as prerequisites. The Agent Prerequisite Map enforces sequential chains (A1 -> A2 -> C1/C2/C3 -> E1/E2) while allowing parallel execution among independent agents (e.g., B1 + B2 for literature tasks). This agent-to-agent coordination represents inter-component interactivity within the system.
- **Agent-to-environment interaction.** Through the 3-Layer Memory System and MCP tools, agents access and update project state (`.research/project-state.yaml`), read prior checkpoint decisions, and adapt their behavior based on accumulated context. The system "perceives" the evolving research design environment.

#### Criterion 2: Bounded Autonomy

Bounded autonomy means the capacity to act independently within defined constraints, without requiring continuous human direction for every step while remaining subject to human override and governance.

Diverga operationalizes bounded autonomy through a carefully engineered tension between agent independence and human control:

- **Autonomous within bounds.** Each of Diverga's 24 agents possesses specialized domain knowledge (e.g., A2 Theory & Critique Architect commands VS-enhanced theory selection across paradigms) and can independently generate multi-alternative recommendations, calculate T-Scores, identify modal patterns, and produce reasoned evaluations. Agents select appropriate analytical strategies, invoke parallel sub-tasks, and orchestrate complex pipelines (e.g., I0's 7-stage PRISMA pipeline) without step-by-step human instruction.
- **Bounded by checkpoints.** The autonomy is explicitly bounded: REQUIRED checkpoints function as hard governance boundaries where the system must halt and defer to human judgment. The Override Refusal mechanism prevents bypassing these boundaries. Downstream agents are blocked from execution until upstream checkpoints receive human approval, enforcing a "no decision without human consent" policy at critical junctures.
- **Bounded by architecture.** Model routing (Opus for HIGH-tier complex reasoning, Sonnet for MEDIUM-tier standard tasks, Haiku for LOW-tier validation) constrains the computational resources available to each agent. The dependency graph constrains execution order. These architectural boundaries define the operational envelope within which autonomy operates.

This is precisely the "bounded" quality Floridi emphasizes: Diverga acts autonomously in generating alternatives and analysis, but defers to humans for decisions that shape the research trajectory.

#### Criterion 3: Adaptability

Adaptability refers to the capacity to modify behavior based on accumulated experience and changing conditions, going beyond fixed input-output mappings.

Diverga exhibits adaptability through several mechanisms:

- **Verbalized Sampling (VS) as adaptive recommendation.** VS methodology actively adapts recommendations based on the researcher's context, prior decisions, and the identified modal landscape. Rather than producing fixed responses to fixed inputs, VS identifies the "obvious" recommendation (T > 0.8), then deliberately generates alternatives across the typicality spectrum (T ~ 0.6, T ~ 0.4, T < 0.3). The alternatives generated are context-sensitive; they depend on the research question, paradigm, and prior checkpoint selections.
- **3-Layer Context System.** Diverga's memory architecture allows agents to adapt across sessions. Layer 1 (natural language status queries), Layer 2 (auto-injected context for sub-agents), and Layer 3 (full detailed context on demand) create a persistent understanding of the research project's evolving state. An agent's behavior in session 5 is informed by decisions made in sessions 1 through 4.
- **Decision Audit Trail.** The immutable YAML log of all research decisions creates a feedback loop: agents can consult prior decisions to calibrate subsequent recommendations, avoiding redundancy and building on established choices.
- **VS Arena (V1-V5 Personas).** The five paradigm-specific personas (Post-Positivist, Critical Theorist, Pragmatist, Interpretivist, Transformative) represent an advanced form of adaptability: the system can adopt fundamentally different epistemological stances and generate recommendations aligned with each, adapting its evaluative framework rather than merely its content.

### 1.2 Positioning on the AI Spectrum

Floridi and the CFP distinguish three tiers of educational AI systems. Diverga can be positioned relative to each:

| Tier | Characteristics | Examples | Diverga Comparison |
|------|----------------|----------|-------------------|
| **Reactive AIED** | Fixed rules, no learning, predetermined responses | Intelligent tutoring systems with branching logic, automated quiz grading | Diverga is fundamentally different: it generates novel recommendations, adapts to context, and maintains state across sessions. |
| **Generative AI Assistants** | Produce content on demand, respond to prompts, but operate as single-turn or loosely connected multi-turn tools; user-initiated, user-directed | ChatGPT, Claude (standalone), Elicit, Consensus | Diverga shares the generative foundation (built on Claude) but differs structurally: it maintains persistent project state, enforces checkpoint governance, coordinates multiple specialized agents, and proactively shapes the interaction through forced pauses and alternative presentation. |
| **Agentic AI** | Goal-directed, multi-step, semi-autonomous, operating within bounded authority, adapting to feedback, coordinating sub-tasks | Multi-agent research pipelines, autonomous coding systems | Diverga occupies this tier. Its 24-agent architecture with prerequisite enforcement, parallel execution, persistent memory, and checkpoint governance constitutes a multi-agent system that pursues the user's research design goal through coordinated, adaptive, semi-autonomous action. |

**What makes Diverga distinctly agentic (rather than merely a sophisticated generative assistant)?**

1. **Goal persistence across sessions.** A generative assistant responds to each prompt in relative isolation. Diverga maintains a research project goal (defined at CP_RESEARCH_DIRECTION) and all subsequent agent actions are oriented toward that goal across multiple sessions, mediated by the 3-Layer Memory System.
2. **Proactive intervention.** Generative assistants produce output when asked. Diverga proactively halts at checkpoints, presents unsolicited alternatives, and flags when modal recommendations dominate (T > 0.8 flagged as "predictable"). It shapes the interaction trajectory rather than merely responding within it.
3. **Multi-agent coordination.** A generative assistant is a single entity. Diverga coordinates 24 specialized agents across a dependency graph, with different agents activated based on project state, paradigm detection, and prerequisite satisfaction. This distributed, coordinated action is a hallmark of agentic systems.
4. **Architectural governance.** The checkpoint system, prerequisite enforcement, and Override Refusal mechanism constitute a governance structure that constrains and directs the system's own behavior, a feature absent from standard generative assistants.

### 1.3 What Makes the Multi-Agent Checkpoint Architecture Distinctly "Agentic"

The distinctive agentic quality of Diverga lies in the integration of three design principles:

1. **Distributed expertise with coordinated action.** Twenty-four agents possess distinct knowledge domains, model allocations, and VS levels. They do not operate in isolation; the Agent Prerequisite Map creates a directed acyclic graph of dependencies, so the system coordinates action across agents toward the shared goal of a defensible research design.

2. **Checkpoint-mediated shared authority.** Authority over the research design is shared between the AI system and the human researcher, but the sharing is structured and asymmetric. The AI has authority to generate, evaluate, and recommend. The human has authority to decide. Checkpoints are the governance mechanism that enforces this division of labor, making the system's agency bounded and accountable.

3. **Adaptive diversity generation.** Through VS methodology, the system does not merely execute tasks; it actively shapes the space of possibilities available to the researcher. By generating alternatives across the typicality spectrum and making typicality visible (T-Scores), Diverga exercises a form of epistemic agency: it influences what the researcher considers, not just what the researcher receives.

This combination of distributed expertise, structured governance, and epistemic influence constitutes artificial agency as Floridi defines it: computational, goal-directed action in service of human purposes, operating with interactivity, bounded autonomy, and adaptability.

---

## 2. Methodological Contribution

### 2.1 Proposed Methodology: Checkpoint-Mediated Agency Analysis (CMAA)

This paper proposes **Checkpoint-Mediated Agency Analysis (CMAA)**, a methodology for studying artificial agency effects in educational contexts. CMAA leverages the structured interaction points inherent in agentic AI systems (such as Diverga's Human Checkpoints) as natural measurement sites for observing, recording, and analyzing the effects of artificial agency on human decision-making.

CMAA addresses a core methodological challenge identified in the CFP: the need for "designs that distinguish agentic participation from tool-based assistance." By instrumenting the checkpoint interactions between human and AI agent, CMAA produces multi-layered data that captures both the process and the outcomes of artificial agency in action.

**CMAA rests on three methodological pillars:**

#### Pillar 1: Human Checkpoints as Measurement Points

Each checkpoint interaction generates a naturally occurring data packet:

| Data Element | Source | Measurement Purpose |
|-------------|--------|-------------------|
| **Alternatives presented** | VS-generated options with T-Scores | Maps the solution space the AI agent constructs for the human |
| **Alternative selected** | Human checkpoint decision | Captures the human's response to AI agency |
| **Deliberation time** | Timestamp delta (presentation to selection) | Indexes cognitive engagement with AI-presented options |
| **Selection rationale** | Decision Audit Trail (YAML) | Externalizes human reasoning in response to AI agency |
| **T-Score of selection** | Typicality Score of chosen option | Measures whether AI agency expands or constrains human choices |
| **Deviation from modal** | Gap between modal recommendation and actual selection | Quantifies the "divergence effect" of agentic diversity generation |

This data structure is inherent to the checkpoint architecture, meaning it is generated as a natural byproduct of system use rather than through invasive research instrumentation. This minimizes observer effects and ecological validity threats.

**Key insight:** In agentic AI systems with checkpoint governance, the governance mechanism itself serves as a measurement instrument. Checkpoints are simultaneously (a) a design feature ensuring human authority, (b) a pedagogical feature promoting reflection, and (c) a research feature producing analyzable data about human-AI interaction.

#### Pillar 2: Decision Audit Trail for Process-Level Modelling

The Decision Audit Trail (immutable YAML log) enables a form of process-level modelling that the CFP identifies as a priority:

- **Sequential decision mapping.** The trail records every research decision in chronological order, creating a complete narrative of how a research design evolved through human-AI interaction. This enables process analysis (not just outcome analysis) of artificial agency effects.
- **Decision dependency analysis.** Because Diverga's agents operate in a prerequisite graph (A1 -> A2 -> C1/C2/C3 -> E1/E2), the audit trail reveals how early checkpoint decisions propagate through downstream design choices. This allows researchers to trace the causal chain of AI agency influence across the research design lifecycle.
- **Typicality trajectory analysis.** By plotting the T-Scores of selected options across sequential checkpoints, researchers can construct a "typicality trajectory" for each participant, revealing whether exposure to VS alternatives leads to increasingly divergent (lower T-Score) or increasingly conservative (higher T-Score) choices over time. This trajectory is a direct measure of how AI agency shapes human decision patterns.
- **Comparison with counterfactual baselines.** The modal recommendation (T > 0.8) at each checkpoint provides a built-in counterfactual: what a non-agentic, standard AI tool would have recommended. The gap between the modal recommendation and the researcher's actual selection (enabled by agentic diversity generation) quantifies the incremental effect of artificial agency.

#### Pillar 3: VS Methodology as Adaptability Operationalization

Verbalized Sampling directly operationalizes Floridi's "adaptability" criterion and provides measurable indicators:

- **Diversity of generated alternatives.** The number and typicality range of alternatives generated at each checkpoint measures the system's adaptive response to the specific research context.
- **Context-sensitivity of recommendations.** By comparing VS outputs across different research contexts (same agent, different projects), researchers can assess whether the system's recommendations genuinely adapt or merely recycle from a fixed repertoire.
- **T-Score calibration accuracy.** Comparing algorithmically assigned T-Scores with expert ratings of typicality measures the quality of the system's adaptability, specifically whether it accurately perceives the "landscape" of methodological options.
- **VS Arena engagement.** The five paradigm-specific personas (V1-V5) represent maximally adaptive behavior: the system adopts fundamentally different epistemological stances. Tracking which personas are activated and how their recommendations differ provides data on the range and depth of adaptability.

### 2.2 How CMAA Advances Existing Approaches

| Existing Approach | Limitation | CMAA Advancement |
|------------------|-----------|-----------------|
| Pre/post surveys of AI tool impact | Measures outcomes only; misses process | Process-level data from checkpoint interactions and audit trails |
| Think-aloud protocols with AI tools | Captures cognition but is invasive; changes behavior | Checkpoint data is non-invasive (generated by normal system use) |
| Log analysis of AI tool usage | Captures clicks/queries but not decision quality | T-Score selection data captures the quality and diversity of decisions |
| Experimental comparisons (AI vs. no-AI) | Treats AI as homogeneous; does not distinguish agentic from non-agentic | Checkpoint architecture enables within-system comparison (agentic features on/off) |
| Surveys of AI agency perceptions | Self-report bias; no behavioral data | Behavioral data (checkpoint selections, deliberation times) complemented by optional self-report |

---

## 3. Distinguishing Agentic Participation from Tool-Based Assistance

### 3.1 Operationalizing the Distinction

The CFP calls for "designs that distinguish agentic participation from tool-based assistance." Using Diverga as a case, we propose a framework for operationalizing this distinction along five dimensions:

| Dimension | Tool-Based Assistance | Agentic Participation | Diverga Evidence |
|-----------|----------------------|----------------------|-----------------|
| **Initiative** | Human initiates every action; AI responds | AI proactively intervenes (e.g., halting at checkpoints, presenting unsolicited alternatives) | REQUIRED checkpoints force system-initiated pauses; VS generates alternatives beyond what was requested |
| **State persistence** | Each interaction is independent or loosely connected | System maintains and acts upon a persistent model of the project | 3-Layer Memory System; `.research/project-state.yaml` updated across sessions |
| **Goal orientation** | Serves immediate user request | Pursues a sustained goal (research design completion) across multiple interactions | Agent Prerequisite Map enforces goal-directed sequencing; downstream agents are blocked until upstream goals are met |
| **Coordination** | Single-entity response | Multi-component coordination toward shared objective | 24 agents with dependency graph, parallel execution, and model routing |
| **Governance** | User controls all; no self-regulation | System has internal governance structures constraining its own behavior | Override Refusal mechanism; REQUIRED checkpoint enforcement; architectural model-tier constraints |

### 3.2 Proposed Measurable Indicators

Building on the five-dimension framework, we propose measurable indicators that researchers can use to empirically distinguish agentic participation from tool-based assistance in educational AI systems:

**Indicator 1: Proactive Intervention Rate (PIR)**
- *Definition:* The proportion of interaction episodes initiated by the AI system (e.g., checkpoint halts, unsolicited alternative presentation) relative to total interaction episodes.
- *Measurement:* Count of system-initiated pauses and presentations / Total interaction episodes.
- *Threshold:* A PIR near zero indicates tool-based assistance (human initiates everything). Agentic systems should show PIR > 0, with the specific value reflecting the degree of agentic intervention.
- *Diverga data source:* Checkpoint trigger log.

**Indicator 2: State Utilization Depth (SUD)**
- *Definition:* The extent to which the system's current outputs reference or build upon information from prior sessions or interactions.
- *Measurement:* Code system outputs for references to prior decisions, earlier checkpoint selections, or accumulated project context. Calculate the proportion of outputs that incorporate cross-session state.
- *Threshold:* Tool-based assistance shows SUD near zero (each interaction stands alone). Agentic systems show SUD > 0, increasing as the project progresses.
- *Diverga data source:* Layer 2 context injection logs; Decision Audit Trail cross-references.

**Indicator 3: Decision Space Expansion (DSE)**
- *Definition:* The degree to which the AI system expands the set of options the human considers beyond what the human requested or would have independently generated.
- *Measurement:* Compare the set of alternatives presented by the system (especially low-T-Score options) with the alternatives the human would have considered (measured via pre-task baseline or think-aloud).
- *Threshold:* Tool-based assistance provides what was asked for. Agentic systems expand the decision space by introducing unsolicited but relevant alternatives.
- *Diverga data source:* VS-generated alternatives at checkpoints vs. pre-task research designs (baseline).

**Indicator 4: Governance Constraint Activation (GCA)**
- *Definition:* The frequency with which internal governance mechanisms constrain or redirect the system's own behavior.
- *Measurement:* Count of prerequisite-blocked agent activations, Override Refusal triggers, and checkpoint enforcement events.
- *Threshold:* Tool-based assistance has no internal governance (user controls everything). Agentic systems show GCA > 0, indicating self-regulation.
- *Diverga data source:* MCP runtime logs; `diverga_check_prerequisites` call records.

**Indicator 5: Coordination Complexity Index (CCI)**
- *Definition:* The number and depth of inter-component interactions required to produce a given output.
- *Measurement:* For each user-facing output, trace the number of agents involved, the depth of the dependency chain, and the number of parallel execution groups activated.
- *Threshold:* Tool-based assistance shows CCI = 1 (single component). Agentic systems show CCI > 1 with increasing values indicating greater coordination complexity.
- *Diverga data source:* Agent activation logs; Task tool invocation records.

---

## 4. Research Questions

Aligned with the BJET Special Issue track "Methodological Approaches for Studying Artificial Agency," we propose the following research questions:

### RQ1: Methodological Framework Validation

**How can the structured interaction points (Human Checkpoints) in multi-agent AI systems be leveraged as measurement instruments for studying artificial agency effects on educational decision-making?**

*Rationale:* This question addresses the CFP's call for methodological contributions that advance the measurement of artificial agency. It tests the core premise of CMAA: that checkpoint governance structures in agentic AI systems generate naturally occurring, analyzable data about human-AI interaction that surpasses what conventional methods (surveys, experiments) can capture.

*Sub-questions:*
- RQ1a: What data dimensions does checkpoint-mediated measurement capture that conventional methods do not?
- RQ1b: How do checkpoint-generated data (deliberation time, T-Score selection patterns, rationale articulation) relate to established measures of critical thinking and decision quality?

### RQ2: Distinguishing Agency from Assistance

**What measurable indicators reliably distinguish agentic AI participation from tool-based AI assistance in research methodology learning contexts?**

*Rationale:* This question directly addresses the CFP's emphasis on "designs that distinguish agentic participation from tool-based assistance." Using the five proposed indicators (PIR, SUD, DSE, GCA, CCI), this question tests whether the conceptual distinction between agentic and tool-based AI can be empirically operationalized and validated.

*Sub-questions:*
- RQ2a: Which indicators show the greatest discriminant validity between agentic and tool-based conditions?
- RQ2b: How do researchers' perceptions of AI agency correlate with behavioral indicators of agentic participation?

### RQ3: Agency Effects on Methodological Reasoning

**How does exposure to agentic AI participation (as operationalized through Diverga's checkpoint-mediated VS alternatives) affect the diversity and quality of researchers' methodological reasoning over time?**

*Rationale:* This question connects the methodological contribution (CMAA) to substantive educational outcomes. By tracking typicality trajectories across sequential checkpoints and comparing pre/post research designs, it examines whether artificial agency produces measurably different learning effects than tool-based assistance.

*Sub-questions:*
- RQ3a: Do researchers' typicality trajectories (T-Score selections across checkpoints) show systematic patterns (e.g., increasing divergence, stabilization, reversion to modal)?
- RQ3b: How does the decision audit trail reveal the process by which artificial agency influences methodological reasoning?

---

## 5. Proposed Methodology Overview

### 5.1 Design: Embedded Mixed Methods with Within-Subject Comparison

The study employs an embedded mixed methods design (Creswell & Plano Clark, 2018) with a within-subject comparison that leverages Diverga's architecture to create naturally occurring contrasts between agentic and tool-based conditions.

**Phase 1: Baseline (Tool-Based Condition)**
- Participants use a standard generative AI assistant (Claude, standalone) to design a research study on a provided scenario.
- Data collected: Research design artifact, think-aloud recording, screen recording.
- This establishes the tool-based assistance baseline for each participant.

**Phase 2: Agentic Condition**
- Same participants use Diverga (full checkpoint and VS architecture) to design a research study on a parallel scenario (counterbalanced).
- Data collected: All checkpoint interaction data (via CMAA), research design artifact, think-aloud recording, screen recording, Decision Audit Trail.

**Phase 3: Reflective Interview**
- Semi-structured interview focused on perceived differences between the two conditions, experiences of AI agency, and checkpoint interactions.

### 5.2 Participants

| Element | Specification |
|---------|--------------|
| Population | Social science doctoral students (education, psychology, HRD) |
| N | 5 or fewer (following Dr. Yang's recommendation for depth over breadth) |
| Sampling | Purposeful; stratified by AI knowledge level and methodological experience |
| Sites | Penn State and/or Texas A&M |
| Inclusion | (1) Completed 1+ research methods course, (2) AI tool experience, (3) Basic CLI familiarity |
| Exclusion | Prior Diverga users; CS/Engineering majors |

### 5.3 Data Sources and Analysis

| Data Source | Method | Analysis | RQ Addressed |
|-------------|--------|----------|-------------|
| Checkpoint interaction data | CMAA extraction from Decision Audit Trail | Typicality trajectory analysis; deliberation time patterns; deviation-from-modal calculation | RQ1, RQ3 |
| Research design artifacts (both conditions) | Pre/post comparison | Framework diversity (Shannon Entropy Index); design quality rubric (expert-rated) | RQ2, RQ3 |
| Think-aloud protocols | Audio + screen recording | Thematic analysis using Floridi's three criteria as sensitizing concepts | RQ1, RQ2 |
| Semi-structured interviews | Post-session, 30 min | Deductive coding (agentic vs. tool-based perception) + inductive open coding | RQ2, RQ3 |
| System logs (MCP runtime) | Agent activation, prerequisite checks, parallel execution | Coordination Complexity Index; Governance Constraint Activation; Proactive Intervention Rate calculation | RQ2 |
| Behavioral data | Screen recording analysis | T-Score inspection frequency; navigation patterns; time-on-alternatives | RQ1, RQ3 |

### 5.4 Analytical Framework

**Quantitative strand:**
- Descriptive statistics for all five proposed indicators (PIR, SUD, DSE, GCA, CCI) across both conditions
- Typicality trajectory plotting (T-Score selections across sequential checkpoints)
- Shannon Entropy Index comparison for framework diversity (baseline vs. agentic condition)
- Deliberation time analysis at checkpoints

**Qualitative strand:**
- Thematic analysis of think-aloud data using Floridi's interactivity, bounded autonomy, and adaptability as sensitizing concepts
- Cross-case analysis across participants with different AI knowledge levels
- Narrative analysis of typicality trajectories (why did this participant's selections follow this pattern?)

**Integration:**
- Joint display: quantitative indicators alongside qualitative themes for each participant
- Convergence assessment: where do behavioral indicators and perceptual reports agree or diverge?
- Explanation building: using qualitative data to explain quantitative patterns in checkpoint interaction data

### 5.5 Ensuring International Relevance

The methodological contribution (CMAA) is designed to be transferable beyond the Diverga case:

- **Framework generalizability.** The five dimensions for distinguishing agentic from tool-based AI (Initiative, State Persistence, Goal Orientation, Coordination, Governance) and their measurable indicators are applicable to any educational AI system, not only Diverga.
- **Checkpoint-as-measurement-instrument principle.** Any agentic AI system with structured human-AI interaction points can apply the CMAA approach, making it relevant to the growing global population of checkpoint-enabled AI educational tools.
- **Cross-cultural applicability.** Research methodology education exists in all higher education contexts worldwide. The methodology does not assume a specific cultural or institutional context.
- **Open instrumentation.** The proposed indicators (PIR, SUD, DSE, GCA, CCI) are operationally defined with sufficient precision to be replicated by international research teams.

---

## 6. Key References (Preliminary)

- Floridi, L. (2025). *Artificial agency.* [As cited in CFP]
- McKenney, S., & Reeves, T. C. (2012; 2019). *Conducting educational design research.* Routledge.
- Sandoval, W. A. (2014). Conjecture mapping. *Journal of the Learning Sciences, 23*(1), 18-36.
- Creswell, J. W., & Plano Clark, V. L. (2018). *Designing and conducting mixed methods research* (3rd ed.). Sage.
- You, H. (2025). Verbalized Sampling for creative text generation. *arXiv:2510.01171*.
- Bucinca, Z., et al. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW1).
- Herrington, J., Reeves, T. C., & Oliver, R. (2010). *A guide to authentic e-learning.* Routledge.
- Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology, 3*(2), 77-101.
- Yang, M., et al. (2025). [BJET ChatGPT study]. *British Journal of Educational Technology.*

---

## 7. Working Notes

### Alignment with CFP Tracks

This paper targets the track "Methodological Approaches for Studying Artificial Agency," which calls for:

| CFP Requirement | How This Paper Addresses It |
|----------------|---------------------------|
| Methodological contributions that advance measurement of artificial agency | Proposes CMAA as a new methodology; defines five measurable indicators |
| Multimodal analyses | Combines checkpoint data, behavioral logs, think-aloud, interviews, and design artifacts |
| Process-level modelling | Decision Audit Trail enables sequential decision mapping and typicality trajectory analysis |
| Designs that distinguish agentic participation from tool-based assistance | Five-dimension framework with operationalized indicators; within-subject comparison design |

### Strengths for the Special Issue

1. **Theoretical grounding in Floridi.** The paper does not merely use Diverga as an example; it systematically maps Diverga's architecture to Floridi's three criteria, producing a transferable framework for analyzing any agentic AI system.
2. **Methodology as primary contribution.** Unlike a typical empirical paper, the primary contribution is CMAA itself, with the Diverga study serving as a proof-of-concept. This aligns with the track's emphasis on methodological advancement.
3. **Practitioner relevance.** The five indicators (PIR, SUD, DSE, GCA, CCI) are immediately usable by other researchers studying agentic AI in education.
4. **Non-anthropomorphic framing.** Following Floridi, the paper consistently frames Diverga's agency as computational and goal-directed, avoiding anthropomorphic language (no "thinking," "understanding," or "knowing").

### Potential Challenges

- **Small N.** The study uses 5 or fewer participants, which limits generalizability. Mitigated by positioning the paper as methodological (proof-of-concept for CMAA) rather than empirical (claims about population effects).
- **Developer-researcher dual role.** Hosung You is both Diverga's developer and a co-researcher. Mitigated by Dr. Yang's independent theoretical perspective and by the within-subject design (each participant serves as their own control).
- **Novelty of CMAA.** As a new methodology, CMAA has no precedent studies. Mitigated by grounding each component in established methods (log analysis, think-aloud, mixed methods) and by the transparent operationalization of indicators.
