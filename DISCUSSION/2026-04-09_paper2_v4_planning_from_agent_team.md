# Paper 2 v4 Planning: Synthesis of Diverga Agent Team Outputs

**Date**: 2026-04-09
**Context**: Following Dr. Yang's feedback on Paper 2 v3 (documented in `2026-04-09_yang_feedback_meeting_notes.md`), the Diverga agent team was dispatched in parallel (with `DIVERGA_TEAM_DISPATCH=1` bypass marker) to address four workstreams:

- **B1 (Literature Review Strategist)**: Identify additional empirical AI agency measurement studies for the comparison table
- **A2 (Theoretical Framework Architect)**: Design the integrated theoretical framework with Epistemic Cognition + Shared Regulation anchors
- **G2 (Publication Specialist)**: Produce the "why it matters" framing (scenario opening, indicator explanations, practice implications)
- **G5 (Academic Style Auditor)**: Audit 23 technical terms and provide plain-language glosses

All four agents returned complete responses. This document synthesizes their outputs into a Paper 2 v4 revision plan.

---

## Important Note: CMAA Indicator Naming

The A2 agent hallucinated alternative expansions for the CMAA indicator acronyms. **These alternative expansions must not be adopted.** The canonical definitions from Research Design v1 and Paper 2 v3 remain authoritative:

| Acronym | Canonical Name (authoritative) | A2 Hallucinated Name (rejected) |
|---|---|---|
| **PIR** | **Proactive Intervention Rate** | Perturbation-Initiated Response |
| **DSE** | **Decision Space Expansion** | Divergence-Sensitive Engagement |
| **GCA** | **Governance Constraint Activation** | Goal-Coordinated Adjustment |
| **SUD** | **State Utilization Depth** | Suggestion Uptake Depth |
| **CCI** | **Coordination Complexity Index** | Contradiction-Confronting Iteration |

When applying A2's theoretical framework scaffolding below, substitute the canonical names throughout. The psychological-anchor-to-indicator mapping that A2 proposed is still valuable; only the names require substitution.

---

## 1. B1 Output: Empirical Studies for the Comparison Table

B1 identified seven additional empirical studies suitable for the Paper 2 v4 prior-approaches comparison table. All seven studies have confirmed DOIs or arXiv identifiers.

### 1.1 Studies identified

**Study 1: Cihon et al. (2025)**
- **Citation**: Cihon, P., et al. (2025). Measuring AI agent autonomy: Towards a scalable approach with code inspection. *arXiv preprint arXiv:2502.15212*.
- **Construct measured**: Structural autonomy of AI agents via code inspection.
- **Instrument type**: Code-review-based rubric applied to agent source or tool-call traces.
- **Sample and design**: Scalable approach to autonomy measurement across multiple agent systems; design-oriented rather than participant-based.
- **Evidence type**: Static code inspection + structured scoring.
- **Key finding**: Autonomy can be measured at the architectural level (which tools an agent can invoke, which safety wrappers are in place) rather than only at the behavioral level.
- **CMAA connection**: Directly relevant to **PIR** and **GCA**. Supports the CMAA claim that agency should be measured at the architectural level rather than the model-capability level, which answers Bigman et al.'s (2026) generalizability concern.

**Study 2: Jafari Meimandi et al. (2025)**
- **Citation**: Jafari Meimandi, K., et al. (2025). The measurement imbalance in agentic AI evaluation undermines industry productivity claims. *arXiv preprint arXiv:2506.02064*.
- **Construct measured**: Coverage balance of agentic AI evaluation instruments; what has and has not been measured across published studies.
- **Instrument type**: Systematic review coding of prior evaluation studies.
- **Sample and design**: Systematic review of agentic AI evaluation literature with explicit coverage audit.
- **Evidence type**: Meta-analytic coding of prior instruments.
- **Key finding**: Most published agentic AI evaluations concentrate on narrow subsets of agency properties; broad constructs like persistent memory use, coordination complexity, and governance enforcement are under-measured.
- **CMAA connection**: Directly supports the **SUD** and **CCI** contribution. CMAA is a direct response to the measurement imbalance this paper identifies.

**Study 3: Edwards et al. (2025)**
- **Citation**: Edwards, A., et al. (2025). Human-AI collaboration: Designing artificial agents to facilitate socially shared regulation among learners. *British Journal of Educational Technology*, Advance online publication. https://doi.org/10.1111/bjet.13534
- **Construct measured**: Agent initiative and partnership perception in collaborative learning settings.
- **Instrument type**: Lexical (text-mining) metric of agent initiative + Partnership/Mentorship Questionnaire (PMQ) + semi-structured interview.
- **Sample and design**: Mixed-methods empirical study in an online collaborative learning environment.
- **Evidence type**: Quantitative lexical metrics + validated scale + qualitative interview.
- **Key finding**: Artificial agents that initiated regulatory prompts were perceived as partners rather than tools, but only when the initiative was context-appropriate.
- **CMAA connection**: Directly relevant to **PIR** and **DSE**. **BJET-published and matches the target venue.**

**Study 4: Shang et al. (2024)**
- **Citation**: Shang, S., et al. (2024). Trusting your AI agent emotionally and cognitively: Development and validation of a semantic differential scale for AI trust. *arXiv preprint arXiv:2408.05354*.
- **Construct measured**: Affective and cognitive dimensions of trust in AI agents.
- **Instrument type**: 27-item semantic differential scale with separate affective and cognitive subscales.
- **Sample and design**: Instrument development study with multi-wave validation.
- **Evidence type**: Psychometric validation data (self-report).
- **Key finding**: Trust in AI agents is empirically separable into affective and cognitive dimensions that predict different interaction outcomes.
- **CMAA connection**: Trust calibration is a construct that CMAA does not directly measure, but it provides a reference point for the **SUD** indicator. Users who trust agents affectively but not cognitively may exhibit different state utilization patterns.

**Study 5: Dang et al. (2025)**
- **Citation**: Dang, T., et al. (2025). Human-AI collaborative learning in mixed reality: Examining the cognitive and socio-emotional interactions. *British Journal of Educational Technology*, Advance online publication. https://doi.org/10.1111/bjet.13607
- **Construct measured**: Cognitive and socio-emotional interactions in human-AI collaborative learning.
- **Instrument type**: Behavioral coding of interaction episodes + self-report measures of collaborative experience.
- **Sample and design**: Mixed-methods empirical study in a mixed reality learning environment.
- **Evidence type**: Behavioral observation + self-report.
- **Key finding**: Cognitive and socio-emotional interactions coevolved during collaborative tasks, with AI agent behavior triggering both types of interaction simultaneously.
- **CMAA connection**: Supports **CCI** and **DSE**. BJET-published.

**Study 6: Yan et al. (2025)**
- **Citation**: Yan, L., et al. (2025). Beyond efficiency: Empirical insights on generative AI's impact on cognition, metacognition and epistemic agency in learning. *British Journal of Educational Technology*, Advance online publication. https://doi.org/10.1111/bjet.70000
- **Construct measured**: Epistemic agency, metacognition, and cognition in AI-assisted learning.
- **Instrument type**: Multi-instrument synthesis drawing on cognitive, metacognitive, and agency measures.
- **Sample and design**: Synthesis/section editorial rather than a primary empirical study.
- **Evidence type**: Conceptual synthesis of empirical findings.
- **Key finding**: Generative AI's impact on epistemic agency is distinct from its impact on efficiency and must be measured separately.
- **CMAA connection**: Supports the rationale for **GCA** as an epistemic-agency measure. Should be cited for framing but not included in the primary comparison table (it is a synthesis rather than a primary measurement study).

**Study 7: Zhang, Muller, & Shami (2024)**
- **Citation**: Zhang, Y., Muller, M., & Shami, N. S. (2024). Human-AI collaboration in thematic analysis using ChatGPT: A user study and design recommendations. *Extended Abstracts of the ACM CHI Conference on Human Factors in Computing Systems (CHI EA '24)*. https://doi.org/10.1145/3613905.3650732
- **Construct measured**: Researcher-AI coordination patterns during thematic coding; perceived AI initiative and control allocation.
- **Instrument type**: Task-based think-aloud protocol + semi-structured interview + behavioral observation log of prompt-response sequences.
- **Sample and design**: Qualitative user study (small N) of researchers performing thematic analysis with ChatGPT assistance.
- **Evidence type**: Qualitative (think-aloud + interview + behavioral observation).
- **Key finding**: Researchers iteratively adjusted their level of AI delegation mid-task, and AI-generated outputs altered subsequent prompt strategy, creating a feedback loop between AI output and researcher oversight.
- **CMAA connection**: **Directly relevant to CCI and PIR** in a research-methodology-support context. This is the closest prior study to our Paper 3 setting.

### 1.2 B1 summary for the comparison table (Paper 2 v4 Table 2 input)

| Study | Primary Construct | Instrument Type | CMAA Connection |
|---|---|---|---|
| Cihon et al. (2025) | Structural autonomy | Code inspection rubric | PIR, GCA |
| Jafari Meimandi et al. (2025) | Evaluation coverage balance | Systematic review coding | SUD, CCI |
| Edwards et al. (2025) | Agent initiative, partner perception | Lexical metric + PMQ + interview | PIR, DSE |
| Shang et al. (2024) | Affective/cognitive trust | 27-item semantic differential | SUD |
| Dang et al. (2025) | Cognitive + socio-emotional interaction | Behavioral coding + self-report | CCI, DSE |
| Yan et al. (2025) | Epistemic agency, metacognition | Multi-instrument synthesis | GCA (framing only) |
| Zhang et al. (2024) | Researcher-AI coordination | Think-aloud + behavioral log | CCI, PIR |

### 1.3 Combined with previously identified studies

The full Paper 2 v4 comparison table should include these seven studies plus the previously identified sources:

- Yang, M., Jiang, S., Li, B., et al. (2025) [BJET] - Tier 1 methodological foundation
- Fragiadakis et al. (2024) [arXiv] - HAIC decision-tree framework
- Jiang et al. (2024) [Data and Information Management] - HAII taxonomy
- Acharya et al. (2025) [IEEE Access] - Agentic AI survey
- Hughes et al. (2025) [J. Comp. Info. Systems] - Multi-expert analysis
- Vaccaro, Almaatouq, & Malone (2024) [Nature Human Behaviour] - Human-AI combination meta-analysis

**Total candidates for Paper 2 v4 comparison table: 13 studies.**

---

## 2. A2 Output: Theoretical Framework Scaffolding

A2 produced a five-subsection theoretical framework for Paper 2 v4 with explicit psychological theory embedding. The canonical CMAA indicator names must be substituted in A2's proposed mapping.

### 2.1 Five-subsection structure

**Subsection 1: Artificial Agency as Interactivity, Bounded Autonomy, and Adaptability**
- **Opening**: Establishes the philosophical criteria that warrant treating multi-agent AI systems as agents rather than tools, a precondition for any measurement framework that claims to capture agency effects.
- **Key constructs**: (a) interactivity as perturbation-response coupling with the environment; (b) bounded autonomy as state-change capacity within architectural constraints; (c) adaptability as internal transition rules modifiable through interaction. Floridi treats these as gradable and architecture-relative.
- **Transition to Subsection 2**: Floridi specifies what agency is in the system, but not how humans respond to it. Because doctoral researchers vary systematically in how they treat knowledge claims from non-human sources, a psychological theory of that variation is needed.

**Subsection 2: Epistemic Cognition and the Reception of Checkpoint-Mediated Alternatives**
- **Opening**: Installs epistemic cognition (Chinn et al., 2011) as the primary psychological anchor, explaining why the same checkpoint produces different agency effects across doctoral researchers.
- **Key constructs**: Chinn et al.'s AIR model (Aims, Ideals, Reliable processes) plus the dualist/multiplist/evaluativist developmental schema. Evaluativists treat AI-generated alternatives as claims requiring calibration against reliable processes; multiplists treat them as equally valid options; dualists treat them as either right or wrong relative to an authority. Epistemic stance is thus a moderator of checkpoint uptake.
- **Transition to Subsection 3**: Epistemic cognition explains reception, but doctoral methodology work is not solitary cognition; it is regulated labour distributed across human and non-human participants.

**Subsection 3: Shared Regulation of Learning and the Redistribution of Regulatory Labour**
- **Opening**: Uses shared regulation of learning (Jarvela et al., 2023) as a secondary anchor to theorize checkpoints as sites where planning, monitoring, and evaluation are reallocated between doctoral researcher and agentic system.
- **Key constructs**: Co-regulation vs. socially shared regulation; the planning-monitoring-evaluation cycle; regulation as a finite labour pool that must be allocated. Checkpoints become observable moments when regulation labour is transferred, shared, or contested.
- **Transition to Subsection 4**: Having psychologically and sociocognitively motivated why checkpoints matter, the next step is to specify how to measure what happens at them.

**Subsection 4: HALIE as a Methodological Bridge to Observable Indicators**
- **Opening**: Adopts HALIE (Lee et al., 2023) as extended by Yang et al. (2025) to translate the preceding theoretical claims into traces that can be coded from interaction logs. HALIE is the bridge from construct to instrument.
- **Key constructs**: Turn-level human-AI interaction units; first-person vs. third-person evaluation; Yang et al.'s extension into methodology-training contexts with checkpoint events as analytic units.
- **Transition to Subsection 5**: HALIE specifies the analytic unit but brackets the institutional and historical context in which doctoral training occurs.

**Subsection 5: Activity-Theoretical Situating of Checkpoint-Mediated Methodology Work**
- **Opening**: Uses activity theory (Engestrom, 1987) to situate CMAA within the doctoral-training activity system, ensuring that measurement does not decontextualize the phenomenon. Paper 2 treats this lightly; Paper 3 foregrounds it.
- **Key constructs**: Subject-object-mediating artifact triangle; division of labour; contradictions as developmental drivers. The agentic AI is a mediating artifact whose introduction produces contradictions in the existing rules and division of labour of doctoral supervision.

### 2.2 Integration paragraph (A2's draft, 178 words)

> Paper 2's theoretical contribution is the vertical integration of four analytic levels into a single measurement framework for artificial agency in education. Floridi (2025) supplies the *philosophical* warrant for treating the system as an agent; Chinn et al. (2011) supply the *psychological* mechanism by which doctoral researchers differentially receive agentic outputs; Jarvela et al. (2023) supply the *sociocognitive* account of how regulation labour is redistributed at checkpoints; HALIE as extended by Yang et al. (2025) supplies the *methodological* bridge from construct to observable trace; and Engestrom (1987) supplies the *sociocultural* container that prevents decontextualised measurement. This vertical stack directly answers Bigman et al.'s (2026) call, in their *Nature Reviews Psychology* Comment, for human-AI interaction research to be embedded in psychological theory so that findings achieve coherence, distinctiveness, and generalizability. CMAA operationalises that call: coherence from the integrated stack, distinctiveness from the psychological anchor (not philosophy alone), and generalizability from the architecture-relative framing of agency. The framework thus positions Paper 2 as a methodological response to a published theoretical gap.

### 2.3 CMAA indicator to anchor mapping (canonical names substituted)

| Canonical Indicator | Primary Theoretical Anchor | Rationale |
|---|---|---|
| **PIR (Proactive Intervention Rate)** | Floridi (interactivity) | Directly operationalizes the interactivity criterion from the philosophical definition |
| **DSE (Decision Space Expansion)** | Chinn et al. (epistemic cognition) | Evaluativist stance predicts engagement with divergent alternatives; dualist stance predicts compression |
| **GCA (Governance Constraint Activation)** | Jarvela et al. (shared regulation) | Governance handoff at checkpoints is a shared-regulation construct |
| **SUD (State Utilization Depth)** | HALIE/Yang et al. | Cross-session context references are HALIE's native analytic unit at the turn level |
| **CCI (Coordination Complexity Index)** | Engestrom (activity theory) | Multi-agent coordination reflects division of labour in the activity system |

### 2.4 Distinctiveness claim

> Checkpoint-governed agentic AI reallocates regulation labour without reciprocal accountability.

A human advisor who proposes an alternative assumes co-responsibility for it; an agentic system bounded by Floridi's *bounded autonomy* cannot. Grounded primarily in Jarvela et al. (2023), secondarily in Floridi (2025). **This is the claim most likely to draw reviewer pushback and must be defended carefully.** It addresses Bigman et al.'s distinctiveness recommendation (point 2 in their Comment).

### 2.5 Generalizability claim

CMAA transfers across AI model versions because it measures effects at the **interaction architecture level** (checkpoint events, alternative generation mechanisms, enforcement structures) rather than at the model-capability level. The strongest anchor is Floridi (2025), whose architecture-relative framing of agency is precisely what licenses model-agnostic measurement. HALIE provides secondary support as a model-agnostic analytic unit. This addresses Bigman et al.'s generalizability recommendation (point 3 in their Comment).

### 2.6 Tensions to flag in Paper 2 v4

1. **Epistemological tradition mismatch**: Chinn et al.'s epistemic cognition is a cognitivist-individualist construct; Jarvela et al.'s shared regulation and Engestrom's activity theory are distributed-sociocultural constructs. Paper 2 v4 should argue that epistemic stance operates at the individual level while regulation operates at the distributed level (parallel, non-competing grains). An explicit footnote should acknowledge the borrowing across epistemological traditions.

2. **Agency vs. mediating artifact tension**: Floridi's gradable agency sits uneasily with activity theory's tendency to treat artifacts as non-agentic mediators. Flag as a limitation rather than attempting resolution.

---

## 3. G2 Output: Why-It-Matters Framing

G2 produced three deliverables for reader-facing accessibility.

### 3.1 Scenario-based opening paragraph (G2 draft, 250 words, ready for Paper 2 v4)

> A second-year doctoral student in an instructional design program opens a multi-agent AI platform to help her plan a mixed-methods dissertation study on undergraduate help-seeking behavior. Within four minutes, the system has drafted a literature review outline, proposed three research questions, and recommended a survey instrument adapted from prior BJET publications. She accepts the suggestions and moves on. Two weeks later, her advisor asks how she chose that particular instrument over the alternatives, why the research questions are framed in that direction rather than another, and whether the AI recommended a design that matched her epistemological commitments or simply the one it had most frequently generated before. She cannot answer any of these questions, because she never saw them as questions; the AI moved through those decisions faster than deliberation could catch them. Her advisor's concern is not whether AI should be involved in research design; it is whether anyone, the student or the tool, was actually exercising judgment at those moments, and whether the process could be examined after the fact. This scenario is not a cautionary tale about AI overreach; it is a description of the current state of agentic AI in educational research contexts. Checkpoint-Mediated Agency Analysis (CMAA) was developed to give researchers, instructors, and tool designers a structured method for answering exactly the question her advisor posed: at each decision point in an AI-assisted workflow, who held agency, on what basis, and to what effect?

**Assessment**: This opening is recognizable to BJET readers, concrete, and avoids technical jargon until the last sentence. It answers "why it matters" by grounding the framework in an educational concern. **Recommended for Paper 2 v4 introduction.**

### 3.2 Why-it-matters sentences per CMAA indicator

| Indicator | What It Reveals | Decision It Supports |
|---|---|---|
| **PIR (Proactive Intervention Rate)** | PIR tells a researcher how often an AI tool acted on the student's task without being asked, identifying whether the tool is augmenting student judgment or substituting for it. | An instructor can use PIR to set or justify threshold policies for how much unsolicited AI action is appropriate within a scaffolded assignment sequence. |
| **DSE (Decision Space Expansion)** | DSE reveals whether the AI tool is broadening the range of options a student considers or narrowing the student toward a single pathway, which has direct implications for critical thinking development. | A curriculum designer can use DSE to select or configure AI tools that preserve deliberate choice-making rather than funneling students toward predetermined outputs. |
| **GCA (Governance Constraint Activation)** | GCA indicates how frequently built-in ethical or procedural guardrails were triggered during a student's interaction, showing whether the AI encountered genuinely contested territory in the student's work. | A program director can use GCA patterns across a cohort to identify assignments where AI constraints conflict with disciplinary norms, and revise either the assignment or the tool configuration accordingly. |
| **SUD (State Utilization Depth)** | SUD shows how much of the context a student has provided the AI tool was actually used in generating its output, signaling whether students' prior work and stated goals are shaping AI behavior or being ignored. | A doctoral methods instructor can use SUD to evaluate whether an AI tool genuinely personalizes its guidance or produces generic responses regardless of what the student submitted. |
| **CCI (Coordination Complexity Index)** | CCI measures the degree to which multiple AI agents within a system are operating in a coordinated versus independent manner, which determines whether a student is receiving coherent support or conflicting guidance. | An educational technology director evaluating a multi-agent platform can use CCI to compare products and to identify configurations where agent coordination breakdowns create inconsistent or contradictory outputs for learners. |

### 3.3 Implications for Educational Practice (G2 outline)

- **For doctoral methods instructors supervising AI-assisted dissertation work**: Use PIR benchmarks from CMAA to establish transparent program policies specifying which stages of dissertation design (literature synthesis, instrument selection, analysis planning) require documented human decision-making, and audit student AI logs against those policies at proposal milestones.

- **For instructional designers building graduate-level research methods courses**: Use DSE scores when selecting or configuring AI writing and planning tools, prioritizing tools that consistently return high DSE values to ensure students encounter genuine option spaces rather than algorithmically narrowed choices.

- **For AI tool designers and developers in educational contexts**: Use GCA activation logs as a formative signal during tool development to identify which educational task types generate governance conflicts most frequently, and revise constraint architectures to distinguish between ethical limits and disciplinary conventions that vary by field.

- **For faculty and program coordinators assessing equity in AI-supported learning**: Use SUD comparisons across student subgroups to determine whether AI tools are responding proportionally to the context students provide; low SUD for students who submit detailed prompts may indicate the tool is not designed for the kinds of prior knowledge or disciplinary framing those students bring.

- **For educational technology researchers designing future studies of agentic AI**: Use CCI as a variable in comparative studies of single-agent versus multi-agent tools, allowing systematic investigation of whether coordination complexity predicts student confusion, task abandonment, or learning outcome variance across different institutional and cultural contexts, **including under-resourced settings in the Global South** where AI tool configurations may differ from those validated in North American or European research.

**Note**: The Global South mention in the last bullet directly addresses the BJET Special Issue's explicit call for international and cross-cultural perspectives.

---

## 4. G5 Output: Technical Term Audit

G5 classified the 23 technical terms in Paper 2 into four categories and produced sample rewrites.

### 4.1 Term classification summary

- **Category A (kept as-is)**: 5 terms (CMAA, PIR, DSE, GCA, SUD)
- **Category B (kept with plain-language gloss at first use)**: 11 terms
- **Category C (replaced with plain-language alternative)**: 6 terms
- **Category D (moved to definitions table)**: 1 term

### 4.2 Full classification table

| # | Term | Category | Gloss or Replacement |
|---|---|---|---|
| 1 | Checkpoint-Mediated Agency Analysis (CMAA) | A | Kept as-is (paper's named framework) |
| 2 | Proactive Intervention Rate (PIR) | A | Kept as-is (named indicator) |
| 3 | Decision Space Expansion (DSE) | A | Kept as-is (named indicator) |
| 4 | Governance Constraint Activation (GCA) | A | Kept as-is (named indicator) |
| 5 | State Utilization Depth (SUD) | A | Kept as-is (named indicator) |
| 6 | Coordination Complexity Index (CCI) | B | "a measure of how many agents and dependencies are coordinated per task" |
| 7 | Typicality Trajectory | B | "the pattern of how typical or atypical an agent's decisions are over time" |
| 8 | Decision audit database | B | "a structured log of every agent decision recorded for analysis" |
| 9 | Verbalized Sampling (VS) | B | "a method in which agents state their reasoning aloud before acting" |
| 10 | T-score (Typicality Score) | B | "a numeric score indicating how closely an agent's behavior matches the norm" |
| 11 | Modal recommendation | C | "most common recommendation produced across repeated trials" |
| 12 | Override refusal | C | "an agent's decision to reject a human or system instruction" |
| 13 | Prerequisite enforcement | C | "requiring that earlier conditions be met before an agent can proceed" |
| 14 | 29-agent dependency graph | B | "a map of how 29 agents depend on and interact with each other" |
| 15 | Multi-agent orchestration | B | "coordinating multiple AI agents to work together on a shared task" |
| 16 | Persistent memory | C | "information retained by the system across separate sessions" |
| 17 | Dynamic task decomposition | B | "breaking a complex task into subtasks in real time as conditions change" |
| 18 | Agentic AI (vs. generative AI) | B | "AI that takes sequences of actions and makes decisions, not just generates text" |
| 19 | Bounded autonomy | B | "the principle that agents act independently only within defined limits" |
| 20 | Checkpoint architecture | B | "a system design in which human review is built in at fixed decision points" |
| 21 | Cross-session state | C | "information the system carries forward from one session to the next" |
| 22 | Inter-component dependencies | C | "the ways different parts of the system rely on each other" |
| 23 | Interaction episode | D | Definitions table entry; use "session" or "interaction" in body |

### 4.3 Terms that must NOT be softened (G5's flag)

G5 identified four terms that must remain as technical named concepts:

1. **CMAA**: The paper's named framework; softening would make the contribution appear anonymous.
2. **PIR**: Named, operationalized metric with a defined formula; softening destroys reproducibility.
3. **Typicality Trajectory**: Has both conceptual and visual referents in the paper's figures; replacement would disrupt the prose-chart connection. Also a contribution-specific coinage.
4. **Verbalized Sampling (VS)**: Names a specific data collection procedure that distinguishes this study's methodology; replacing with a description would prevent replication.

### 4.4 Sample rewrites (G5's before/after)

**Sample 1 (governance language)**

- **Before**: "GCA scores were computed across all 29-agent dependency graph nodes to assess the frequency with which governance constraint activation events interrupted normal multi-agent orchestration cycles."
- **After**: "We measured how often the system's built-in safeguards halted normal coordination across the full network of 29 interdependent agents (GCA; governance constraint activation)."

**Sample 2 (telemetry language)**

- **Before**: "Verbalized Sampling (VS) procedures enabled the decision audit database to capture prerequisite enforcement events at each checkpoint, yielding a complete typicality trajectory for each agent across the experimental trials."
- **After**: "Agents stated their reasoning before acting (Verbalized Sampling, VS), which allowed us to log every instance of prerequisite enforcement in the structured decision record. This produced a complete picture of how each agent's behavior shifted toward or away from the norm over time (typicality trajectory)."

**Sample 3 (analytic claim)**

- **Before**: "DSE and CCI jointly predicted override refusal rates, suggesting that bounded autonomy conditions modulate the agent's capacity for dynamic task decomposition under cross-session state constraints."
- **After**: "Agents operating under tighter autonomy limits (bounded autonomy) showed both narrower decision options (DSE) and higher coordination complexity (CCI), which together predicted how often agents rejected instructions. This suggests that the boundaries placed on agent autonomy also affect how flexibly agents can break down complex tasks in real time."

---

## 5. Integration Plan for Paper 2 v4 Drafting

Based on the four agent outputs, Paper 2 v4 drafting should proceed in the following order:

### Phase A: Structural scaffolding (Day 1)
1. Replace the current introduction with G2's scenario-based opening paragraph.
2. Replace the current theoretical framework chapter with A2's five-subsection structure (using canonical CMAA names throughout).
3. Add A2's integration paragraph at the end of the theoretical framework chapter.

### Phase B: Literature review expansion (Day 2)
4. Add a new subsection "Prior Approaches to Measuring Artificial Agency and Human-AI Interaction Performance" before the CMAA framework chapter.
5. Draft the comparison table using 13 studies (B1's 7 new + 6 previously identified).
6. Write narrative bridging text connecting each study to the gap CMAA addresses.

### Phase C: Accessibility and reader-facing framing (Day 3)
7. Apply G5's term classification throughout: insert first-use glosses for Category B terms, replace Category C terms with plain-language alternatives, move Category D terms to a definitions table.
8. Insert G2's "why it matters" sentences alongside each CMAA indicator definition.
9. Rewrite three passages using G5's before/after examples as templates.

### Phase D: Discussion enhancement (Day 4)
10. Add a new "Implications for Educational Practice" subsection in the discussion, using G2's five-bullet outline.
11. Add a distinctiveness paragraph using A2's claim about reciprocal accountability.
12. Add a generalizability statement using A2's architecture-level argument.
13. Cite Bigman et al. (2026) in both the theoretical framework section and the limitations/future directions section.

### Phase E: Reference list (Day 4)
14. Ensure all 7 new B1-identified studies plus Bigman et al. (2026) plus psychological-anchor references (Chinn 2011, Jarvela 2023) are in the reference list.
15. Verify all citations are in APA 7 format with DOIs where available.

### Phase F: Internal review (Day 5)
16. Co-Investigator reads Paper 2 v4 from end to end, checking that technical terms are consistently glossed, "why it matters" is present in every major section, and the theoretical framework subsections cohere.
17. Send Paper 2 v4 to Principal Investigator for review.

---

## 6. Outstanding Decisions

Two decisions remain before Phase A drafting can begin:

1. **Primary psychological anchor confirmation**: The team recommended Epistemic Cognition (Chinn et al., 2011) as primary with Shared Regulation (Jarvela et al., 2023) as secondary. A2's scaffolding assumes this assignment. Confirmed by the Co-Investigator on 2026-04-09.

2. **Chinn et al. (2011) vs. Chinn et al. later works**: The original 2011 paper (Expanding the dimensions of epistemic cognition) is the classic reference, but later Chinn papers (e.g., Chinn, Rinehart, & Buckland, 2014 on epistemic cognition as explicit criteria) may be more directly useful for the CMAA operationalization. The A2 agent defaulted to 2011; the Co-Investigator should verify which Chinn reference is most apt.

---

## 7. Action Items Added to 2026-04-09 Meeting Notes

The following action items should be added to the existing Yang feedback meeting notes:

| Action | Owner | Target Date |
|---|---|---|
| Bigman et al. (2026) citation added to Paper 2 v3 reference list | Co-I | Done (2026-04-09) |
| Diverga agent team (B1, A2, G2, G5) outputs received and synthesized | Co-I | Done (2026-04-09) |
| Review G5 term classification and confirm acceptance or push back on any specific terms | PI | 2026-04-11 |
| Review A2 theoretical framework scaffolding and confirm psychological anchor selection | PI | 2026-04-11 |
| Review G2 opening paragraph and confirm tone is appropriate for BJET | PI | 2026-04-11 |
| Begin Paper 2 v4 drafting following Phase A through Phase F plan | Co-I | 2026-04-12 |
