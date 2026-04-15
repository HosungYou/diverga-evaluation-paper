# Paper 2 v4 Direction: Measurement Pivot Final Decision

**Date**: 2026-04-15
**Status**: Decisions confirmed; ready for Paper 2 v4 drafting
**Related files**:
- `2026-04-09_yang_feedback_meeting_notes.md`
- `2026-04-09_paper2_v4_planning_from_agent_team.md`
- `2026-04-09_measurement_pivot_multi_agent_deliberation.md`

---

## 1. Problem Statement

Paper 2 v3 proposed five invented indicators under the name Checkpoint-Mediated Agency Analysis (CMAA): PIR, DSE, GCA, SUD, CCI. Dr. Yang's feedback identified six concerns with this approach, and the doctoral candidate raised an additional concern about the accessibility of technical terminology. The central issue is that inventing novel measurement terms when established alternatives exist undermines both reader accessibility and the paper's theoretical coherence.

The team conducted two rounds of multi-agent deliberation (eight agent invocations total) to determine which CMAA indicators should be replaced with established validated scales and which should be retained as genuinely novel contributions.

---

## 2. Governing Constraint

Agent A2 (Theoretical Framework Architect) identified the decisive constraint: **replacement scales must come from traditions compatible with the Paper 2 theoretical framework** (Floridi philosophical agency + Chinn epistemic cognition + Jarvela shared regulation + Engestrom activity theory + HALIE methodological bridge).

**Accepted traditions**: Self-regulated learning (SRL), epistemic cognition, distributed cognition, collaborative regulation, metacognitive monitoring.

**Rejected traditions** (even if psychometrically strong): Trust in automation (Jian et al., 2000), algorithm aversion/appreciation (Dietvorst et al., 2015; Logg et al., 2019), general HCI usability scales (SUS, UEQ), technology acceptance models.

**Rationale**: Engineering psychology traditions treat the human as a supervisory controller and the AI as a tool. This ontology is incompatible with Floridi's agency criteria and Chinn's epistemic cognition, both of which frame the AI-human pair as an epistemic encounter. Importing scales from incompatible traditions would fragment the theoretical framework and weaken the paper's response to Bigman, Briker, and Langer's (2026) call for psychological theory embedding.

---

## 3. Final Measurement Battery

### Tier 1: HALIE-Adapted Metrics (unchanged)

Borrowed from Yang et al. (2025, BJET) and original sources. Applied to both the Claude baseline and the agentic AI conditions.

| Metric | Source | Format |
|---|---|---|
| Prompt number | Yang et al. (2025) | Count |
| Depth of Knowledge | Webb (2002); Yang et al. (2025, Appendix A) | 4-level rubric, 2 coders |
| Prompt relevance and evolution | Yang et al. (2025, Appendix A) | 4-level rubric, 2 coders |
| Originality | Yang et al. (2025, Appendix A) | 4-level rubric, 2 coders |
| Self-efficacy | Avey, Luthans, and Jensen (2009) | 5 items, 5-point Likert, post-session |
| Engagement composite | Skinner et al. (2009); Fredricks et al. (2004); Halverson and Graham (2019) | 8 items, composite score, post-session |

### Tier 2: SRL and Epistemic Cognition Scales (newly borrowed)

Three established scales replacing three CMAA indicators, drawn from SRL-compatible traditions per the governing constraint.

| New Name | Replaces | Primary Source | Theoretical Family | What It Measures (plain language) |
|---|---|---|---|---|
| **AI-Initiated Support Frequency** | PIR | Karabenick and Berger (2013) self-regulated help-seeking; Horvitz (1999) mixed-initiative coding as architectural supplement | Self-regulated learning | How often the AI system acts on the task without being asked, compared with how often the user initiates |
| **Cross-Session Context Retention** | SUD | Wegner (1987) and Lewis (2003) Transactive Memory Systems; log-based continuity measurement | Distributed cognition | How much earlier context (prior sessions, prior decisions) the AI system actually uses when making new recommendations |
| **Human-AI Coregulation Depth** | CCI (human-AI dimension) | Hadwin, Jarvela, and Miller (2018) socially shared regulation of learning process metrics | Collaborative regulation | How deeply the human and the AI system share the work of planning, monitoring, and evaluating the research design |

### Tier 3: Agentic-Irreducible Indicators (retained, renamed)

Two indicators plus one log-derived architectural metric. These measure phenomena that did not exist before checkpoint-governed agentic AI and have no established counterpart.

| New Name | Was | Theoretical Anchor | What It Measures (plain language) | Why It Cannot Be Replaced |
|---|---|---|---|---|
| **Override Activation Rate** | GCA | Floridi (2025) bounded autonomy | How often the AI system's built-in rules stop it from taking actions that would bypass human decisions | This measures an AI vetoing itself, a phenomenon that did not exist in pre-agentic systems. No pre-2023 scale captures it. |
| **Epistemic Alternative Exposure** | DSE | Chinn, Buckland, and Samarapungavan (2011) evaluativist stance; Bucinca, Malaya, and Gajos (2021) cognitive forcing functions as empirical precedent | Whether the AI system broadens the range of theoretical and methodological options the researcher considers, or narrows them toward the most common answer | Chinn's epistemic cognition framework requires measuring option-set expansion. Existing consideration-set scales from consumer psychology are ontologically mismatched. |
| **Agent-to-Agent Interdependence** (log metric only) | CCI (agent-to-agent dimension) | Malone and Crowston (1994) coordination theory; Thompson (1967) interdependence typology | How many internal AI agents and how many dependency links are activated to produce a single recommendation | This is a log-derived architectural descriptor, not a participant-measured construct. No human-team coordination scale applies to LLM-to-LLM coordination. |

### Tier 4: Cross-Cutting Controls (optional)

| Scale | Source | Purpose |
|---|---|---|
| NASA-TLX (6 dimensions) | Hart and Staveland (1988) | Cognitive workload control: does checkpoint interaction increase mental demand? |
| AI Literacy Scale | Ng, Leung, Chu, and Qiao (2021) | Individual difference control: does prior AI literacy moderate engagement patterns? |

---

## 4. Summary of Changes

| Before (5 invented) | After | Status |
|---|---|---|
| PIR (Proactive Intervention Rate) | AI-Initiated Support Frequency (Karabenick + Horvitz) | **Replaced** |
| DSE (Decision Space Expansion) | Epistemic Alternative Exposure (Chinn + Bucinca) | **Renamed, retained** |
| GCA (Governance Constraint Activation) | Override Activation Rate (Floridi) | **Renamed, retained** |
| SUD (State Utilization Depth) | Cross-Session Context Retention (transactive memory) | **Replaced** |
| CCI (Coordination Complexity Index) | Split into Human-AI Coregulation Depth (Hadwin/Jarvela, **replaced**) + Agent-to-Agent Interdependence (log metric, **retained**) | **Split** |

**Net**: 5 invented indicators become 2 renamed retained + 1 log metric + 3 borrowed validated scales.

---

## 5. Revised Research Questions

**RQ1**: How can a measurement battery composed primarily of established validated scales, adapted and integrated for checkpoint-governed multi-agent AI environments, capture artificial agency effects on educational decision-making that single-scale or single-tier approaches fail to detect?

**RQ2**: To what extent does a tiered battery combining HALIE-adapted metrics (Yang et al., 2025), established validated scales for agency, self-efficacy, and epistemic engagement, and a minimal set of checkpoint-architectural indicators reliably distinguish agentic AI participation from standard generative AI assistance in research methodology learning?

**RQ3**: How do researchers' typicality trajectories (T-Score selections across sequential checkpoints) evolve under exposure to checkpoint-governed agency, and what process-level patterns distinguish emerging inquirer profiles relative to the strategic-inquirer and exploratory-inquirer archetypes identified by Yang et al. (2025)?

**RQ4** (new): Do the borrowed validated scales and the retained checkpoint-architectural indicators exhibit convergent validity in predicting learning outcomes and decision-quality markers, and where they diverge, what does that divergence reveal about the unique measurement affordances of checkpoint architectures?

---

## 6. Theoretical Framework Structure for Paper 2 v4

Five subsections, integrating four analytic levels per Bigman, Briker, and Langer (2026):

1. **Artificial Agency as Interactivity, Bounded Autonomy, and Adaptability** (Floridi, 2025). Philosophical foundation. Primary anchor for Override Activation Rate.

2. **Epistemic Cognition and the Reception of Checkpoint-Mediated Alternatives** (Chinn, Buckland, and Samarapungavan, 2011). Primary psychological anchor. Dualist/multiplist/evaluativist schema as moderator of checkpoint uptake. Primary anchor for Epistemic Alternative Exposure.

3. **Shared Regulation of Learning and the Redistribution of Regulatory Labour** (Jarvela, Nguyen, and Hadwin, 2023; Hadwin, Jarvela, and Miller, 2018). Secondary psychological anchor. Primary anchor for Human-AI Coregulation Depth.

4. **HALIE as a Methodological Bridge** (Lee et al., 2023; Yang et al., 2025). Translates philosophical and psychological constructs into observable traces at the checkpoint level. Primary anchor for AI-Initiated Support Frequency and Cross-Session Context Retention.

5. **Activity-Theoretical Situating** (Engestrom, 1987). Sociocultural container. Primary anchor for Agent-to-Agent Interdependence. Paper 3 foregrounds this; Paper 2 references it lightly.

Integration paragraph (from A2):

> Paper 2's theoretical contribution is the vertical integration of four analytic levels into a single measurement framework for artificial agency in education. Floridi (2025) supplies the philosophical warrant; Chinn et al. (2011) supply the psychological mechanism; Jarvela et al. (2023) and Hadwin et al. (2018) supply the sociocognitive account of regulation redistribution; HALIE as extended by Yang et al. (2025) supplies the methodological bridge; and Engestrom (1987) supplies the sociocultural container. This integration directly answers Bigman, Briker, and Langer's (2026) call for human-AI interaction research to be embedded in psychological theory.

---

## 7. Paper 2 v4 Positioning Statement

> We integrate validated instruments from self-regulated learning, epistemic cognition, distributed cognition, and collaborative regulation traditions with two architectural indicators (Override Activation Rate, Epistemic Alternative Exposure) that measure phenomena with no established counterpart in pre-agentic AI literature. The resulting three-tier measurement battery is the first designed specifically for checkpoint-governed multi-agent AI in educational contexts and directly responds to Bigman, Briker, and Langer's (2026) call for human-AI interaction research to be embedded in psychological theory.

---

## 8. "Why It Matters" Framing (from G2)

### Opening scenario (ready for Paper 2 v4 introduction)

A second-year doctoral student in an instructional design program opens a multi-agent AI platform to help her plan a mixed-methods dissertation study on undergraduate help-seeking behavior. Within four minutes, the system has drafted a literature review outline, proposed three research questions, and recommended a survey instrument adapted from prior BJET publications. She accepts the suggestions and moves on. Two weeks later, her advisor asks how she chose that particular instrument over the alternatives, why the research questions are framed in that direction rather than another, and whether the AI recommended a design that matched her epistemological commitments or simply the one it had most frequently generated before. She cannot answer any of these questions, because she never saw them as questions; the AI moved through those decisions faster than deliberation could catch them. This scenario is not a cautionary tale about AI overreach; it is a description of the current state of agentic AI in educational research contexts. The measurement battery proposed in this paper was developed to give researchers, instructors, and tool designers a structured method for answering exactly the question her advisor posed: at each decision point in an AI-assisted workflow, who held agency, on what basis, and to what effect?

### What each measure tells a BJET reader

| Measure | What It Reveals | Decision It Supports |
|---|---|---|
| AI-Initiated Support Frequency | How often the AI acted on the student's task without being asked; whether the tool augments judgment or substitutes for it | Instructor: set threshold policies for how much unsolicited AI action is appropriate |
| Epistemic Alternative Exposure | Whether the AI broadens options or narrows toward a single pathway; implications for critical thinking | Curriculum designer: select tools that preserve deliberate choice-making |
| Override Activation Rate | How often built-in guardrails triggered; whether the AI encountered contested territory | Program director: identify assignments where AI constraints conflict with disciplinary norms |
| Cross-Session Context Retention | Whether the AI actually uses the context the student provided or produces generic responses | Methods instructor: evaluate whether a tool genuinely personalizes guidance |
| Human-AI Coregulation Depth | How deeply the human and AI share regulatory work (planning, monitoring, evaluating) | Researcher: compare collaborative AI designs to understand regulation redistribution |
| Agent-to-Agent Interdependence | Whether agents coordinate or conflict internally | Technology director: compare multi-agent platforms for coherence |

### Implications for Educational Practice (discussion outline)

- For doctoral methods instructors: use AI-Initiated Support Frequency benchmarks to establish transparent policies on AI involvement at each dissertation design stage.
- For instructional designers: use Epistemic Alternative Exposure scores to select AI tools that expand rather than narrow student options.
- For AI tool designers: use Override Activation Rate logs to identify task types where governance constraints need revision to accommodate disciplinary variation.
- For faculty coordinators assessing equity: use Cross-Session Context Retention across student subgroups to detect personalization failures.
- For educational technology researchers: use Human-AI Coregulation Depth and Agent-to-Agent Interdependence in comparative studies across settings, including under-resourced Global South contexts.

---

## 9. Technical Term Accessibility (from G5)

All terms in Paper 2 v4 must be glossed at first use. The following classification governs the manuscript:

**Keep as named concepts** (5 terms): The paper's three-tier battery name, Typicality Trajectory, Override Activation Rate, Epistemic Alternative Exposure, Verbalized Sampling.

**Gloss at first use** (11 terms): Agent-to-Agent Interdependence, AI-Initiated Support Frequency, Cross-Session Context Retention, Human-AI Coregulation Depth, T-score, bounded autonomy, checkpoint architecture, multi-agent orchestration, agentic AI, dependency graph, dynamic task decomposition.

**Replace with plain language** (6 terms): modal recommendation becomes "most common recommendation"; override refusal becomes "the system's decision to reject an instruction"; prerequisite enforcement becomes "requiring earlier conditions be met"; persistent memory becomes "information retained across sessions"; cross-session state becomes "information carried forward between sessions"; inter-component dependencies becomes "how parts of the system rely on each other."

---

## 10. Comparison Table for Prior Empirical Studies (Paper 2 v4 Table 2)

This table juxtaposes prior empirical approaches to measuring AI agency or human-AI interaction performance with the present study's battery.

| Study | Construct | Instrument Type | Sample | Evidence Type | Gap Our Battery Addresses |
|---|---|---|---|---|---|
| Yang et al. (2025) BJET | ChatGPT interaction metrics | DoK rubric, relevance rubric, originality rubric, self-efficacy/engagement scales | N = 73, undergrad + grad | Mixed (log + scale + interview) | Designed for standard generative AI; no checkpoint-specific measures |
| Fragiadakis et al. (2024) arXiv | HAIC evaluation framework | Decision-tree for metric selection across 3 modes | Literature review | Meta-methodological | No education-specific operationalization; no empirical application |
| Edwards et al. (2025) BJET | Agent initiative in collaborative learning | Lexical metric + PMQ + interview | Empirical, mixed methods | Mixed | Initiative measured but not at architectural checkpoint level |
| Shang et al. (2024) arXiv | Affective/cognitive AI trust | 27-item semantic differential | Multi-wave instrument validation | Self-report | Trust is measured but governance activation (override behavior) is not |
| Dang et al. (2025) BJET | Cognitive + socio-emotional HAIC | Behavioral coding + self-report | Empirical, mixed reality | Mixed | Measures interaction but not checkpoint-mediated regulation redistribution |
| Cihon et al. (2025) arXiv | Structural agent autonomy | Code inspection rubric | Scalable agent evaluation | Code review | Architectural-level measurement supports our design but not applied to education |
| Jafari Meimandi et al. (2025) arXiv | Evaluation coverage imbalance | Systematic review coding | Meta-analysis of evaluations | Review | Identifies the gap our Tier 3 fills: persistent memory and coordination are under-measured |
| Zhang, Muller, and Shami (2024) CHI EA | Researcher-AI coordination | Think-aloud + behavioral log | Small N, qualitative | Qualitative | Closest to our setting but no defined checkpoints; CMAA provides structured measurement |
| **Present study** | **Checkpoint-governed agency in doctoral research** | **3-tier battery: HALIE-adapted + SRL/epistemic cognition + architectural indicators** | **N = 5, within-subject** | **Mixed** | **First battery combining validated scales with checkpoint-specific indicators for agentic AI in education** |

---

## 11. Paper 1 Feedback (Separate Workstream)

Dr. Yang also provided feedback on Paper 1 (Design Case for IJDL): the evaluation phases and design cycle iterations are documented, but a robust explanation of **why each design choice was made** must be included. Each of the five design cycles must contain:

1. Trigger problem that prompted the cycle
2. Alternatives considered (including rejected ones)
3. Grounds for selection
4. Success criterion defined at the time

This workstream proceeds in parallel with Paper 2 v4 but does not block it.

---

## 12. Additional References (from 3 papers reviewed during discussion)

Three papers were shared during the Dr. Yang meeting and have been reviewed:

1. **Jiang, T., Sun, Z., Fu, S., and Lv, Y. (2024)**. Human-AI interaction research agenda: A user-centered perspective. *Data and Information Management, 8*(4), Article 100078. Provides HAII taxonomy (collaboration, competition, conflict, symbiosis) and calls for multi-disciplinary theories.

2. **Fragiadakis, G., Diou, C., Kousiouris, G., and Nikolaidou, M. (2024)**. Evaluating human-AI collaboration: A review and methodological framework. *arXiv preprint arXiv:2407.19098*. Decision-tree framework for HAIC metric selection across AI-centric, human-centric, and symbiotic modes.

3. **Bigman, Y. E., Briker, R., and Langer, M. (2026)**. Human-AI interaction research needs to be embedded in psychological theory. *Nature Reviews Psychology, 5*(April), 233-234. The most important reference for Paper 2 v4. Argues that HAI research not grounded in psychological theory risks becoming obsolete with each AI model release. Three recommendations: coherence with existing theory, distinctiveness from human-human interaction, and explicit generalizability. Paper 2 v4 cites this Comment as the rationale for its psychological theory embedding.

---

## 13. Next Steps

| Action | Owner | Target |
|---|---|---|
| Paper 2 v4 drafting following the four-tier battery and four research questions specified in this document | Co-I | 2026-04-20 |
| Instruments/ folder update with draft adaptations of Tier 2 borrowed scales (Karabenick help-seeking, transactive memory, Hadwin coregulation) | Co-I | 2026-04-18 |
| Chinn et al. reference verification (2011 vs. later works) | Co-I | 2026-04-16 |
| PI review of Paper 2 v4 draft | PI | 2026-04-28 |
| Paper 2 BJET abstract submission | PI + Co-I | 2026-08-01 |
| Paper 1 v3 (Design Case) with decision rationale additions | Co-I | 2026-05-25 |
