# DRAFT — For Discussion Only
# Paper 3: ETR&D Proposal Draft v1 (2026-03-24)

**Target:** Educational Technology Research and Development (ETR&D)
**Relationship:** Paper 2 (BJET) provides the CMAA methodological framework; this paper is its first empirical application
**Status:** ~60% completeness — key sections drafted in prose; remaining sections outlined
**Word count estimate at completion:** ~8,000 words
**IRB status:** Preparation planned April–May 2026
**Data collection planned:** August–September 2026

> **Note for Dr. Yang:** This is a working proposal draft shared for early-stage feedback. Sections marked `[OUTLINE]` are planned content. The study has not yet been conducted; IRB preparation begins April 2026. Journal changed from C&E to ETR&D: ETR&D's design-based research focus and N=5 intensive methodology norms are a better fit for this study's phase. Full manuscript to follow after data collection.

---

## Title

**Checkpoint-Governed Agency and Methodological Reasoning: A Design-Based Study of Artificial Agency Effects on Doctoral Researchers**

*[Candidate alternative: "Does Agentic AI Expand or Constrain Methodological Thinking? A Multiple-Case Study of Checkpoint-Mediated Scaffolding"]*

---

## Abstract [Draft — 224 words]

Checkpoint-governed agentic AI systems present a distinctive design challenge: when an AI system presents multiple alternatives across a typicality spectrum and enforces human selection at mandatory decision junctures, does this architecture genuinely expand epistemic agency, or do researchers default to modal consensus regardless? This paper reports a design-based study examining how Diverga, a 24-agent checkpoint-governed AI research methodology assistant, affects the methodological reasoning processes of doctoral students in social science fields. Using a multiple case study design (N=5, purposeful maximum variation sampling), participants engaged in two research design tasks in a single structured session: an unassisted baseline condition and a Diverga-assisted condition with concurrent think-aloud protocol. Data sources include checkpoint interaction logs, think-aloud transcripts, screen recordings, pre/post design artifacts, and semi-structured interviews. Analysis integrates Checkpoint-Mediated Agency Analysis (CMAA; You & Yang, forthcoming) indicators to quantify epistemic labour redistribution at checkpoints with Activity Theory contradiction analysis to explain when and why deliberative scaffolding fails to activate genuine epistemic engagement. Six design principles are derived for checkpoint-governed agentic AI in educational research contexts, addressing mandatory enforcement, typicality visibility, and upstream-downstream architectural coupling. Findings contribute both empirical grounding for the CMAA framework and actionable design principles for researchers and developers building agentic AI systems intended to support — rather than replace — human epistemic agency.

**Keywords:** agentic AI, artificial agency, doctoral education, research methodology, checkpoint-mediated scaffolding, design-based research, mixed methods

---

## 1. Introduction [Prose draft — ~650 of target ~900 words]

Research methodology education occupies an unusual position in doctoral training: it is simultaneously the most discipline-generalizable skill doctoral students develop and the one most vulnerable to intellectual conformity. The pressure to adopt recognizable theoretical frameworks — frameworks that advisors, reviewers, and funding bodies recognize — produces a systematic pull toward modal consensus in research design. A doctoral student studying AI adoption reaches for Technology Acceptance Model; a student studying identity formation reaches for Social Cognitive Theory; a student studying community dynamics reaches for Communities of Practice. These frameworks are not wrong; they are simply predictable, and predictability forecloses the disciplinary creativity that genuine scholarly contribution requires.

This tendency toward modal consensus is observable in AI-assisted research tool use. Querying three widely used AI research assistants — a major large language model, a systematic review tool, and a citation-based exploration platform — with the question "What theoretical framework should I use to study research identity formation among doctoral students?" yields a consistent pattern: Bandura's (1986) Social Cognitive Theory and Bronfenbrenner's (1979) ecological systems model are recommended by all three tools within the first response. This is not incidental; it is a structural feature of large language model-based recommendation systems. Statistical patterns in training corpora produce statistically probable outputs; tools optimized for helpfulness converge on the most frequently cited, most broadly recognized frameworks. The result — mode collapse, in which AI recommendations cluster at the modal consensus regardless of contextual nuance — is precisely the epistemic condition that careful doctoral training is designed to counteract.

Whether checkpoint-governed agentic AI systems, architecturally designed to generate and present alternatives across a typicality spectrum rather than defaulting to modal consensus, can mitigate this tendency is an open and important empirical question. Diverga is a 24-agent AI research methodology assistant built on the Model Context Protocol, designed to operationalize artificial agency (Floridi, 2025) through three mechanisms: (1) Verbalized Sampling (VS), which generates recommendations distributed across a typicality spectrum (T-Score: 0.0 novel → 1.0 modal); (2) mandatory human checkpoints at epistemically critical decision junctures, enforcing human evaluation of alternatives before proceeding; and (3) an immutable Decision Audit Trail recording all checkpoint interactions. These mechanisms constitute a deliberate architectural response to mode collapse — but whether they succeed in supporting authentic methodological reasoning, or whether researchers select the modal option regardless of the alternatives presented, is an empirical question that this study is designed to address.

This paper presents the design, protocol, and analysis plan for a multiple case study (N=5) examining how interaction with Diverga's checkpoint system affects doctoral students' methodological reasoning diversity. Three research questions organize the inquiry:

**RQ1.** How does interaction with Diverga's checkpoint system affect the diversity of theoretical frameworks and methodological approaches considered by doctoral students in research design tasks?

**RQ2.** What patterns of epistemic labour redistribution — as measured by CMAA indicators — characterize doctoral students' interaction with checkpoint-governed agentic AI during research design?

**RQ3.** What tensions emerge between the scaffolding intent of checkpoint-governed artificial agency and participants' actual epistemic engagement at checkpoints, and what design principles can be derived from these tensions?

**[OUTLINE — remaining ~250 words]**
- Paper structure overview
- Relationship to Paper 2 (BJET CMAA framework): this paper provides the empirical application

---

## 2. Literature Review [OUTLINE — ~900 words target]

### 2.1 Agentic AI in Education: From Tool to Participant
- Reactive AIED → generative AI assistants → agentic AI: initiative and persistence as defining features (Ouyang & Jiao, 2021; Yan et al., 2024)
- Multi-agent coordination in educational contexts (Wang et al., 2024; Hughes et al., 2025)
- Current knowledge gap: empirical studies of how agentic AI changes reasoning processes

### 2.2 Research Methodology Education at the Doctoral Level
- Challenges in doctoral methodology training: limited exposure to paradigm diversity, advisor influence, disciplinary norms
- AI tools in research education: emerging use cases, early findings (TAM-centered studies predominate)
- Mode collapse as structural risk: when AI recommendations replicate training data distributions

### 2.3 Measurement Approaches for AI-Mediated Reasoning
- Think-aloud as process data (Ericsson & Simon, 1993)
- Interaction log analysis: affordances and limitations
- Prior design-based studies of AI scaffolding: what was measured and what was missed
- CMAA (You & Yang, forthcoming) as the measurement framework for this study

---

## 3. Theoretical Framework [Prose draft — ~600 of target ~1,000 words]

### 3.1 Artificial Agency and Epistemic Labour Redistribution

This study adopts You and Yang's (Paper 2) operationalization of Floridi's (2025) artificial agency criteria as its foundational frame, in which interactivity, bounded autonomy, and adaptability are treated as measurable properties of checkpoint-governed AI architectures rather than anthropomorphic attributes. In the context of doctoral research methodology education, the educational consequence of artificial agency is not primarily a function of AI output quality, but of how checkpoint interactions redistribute epistemic labour — the cognitive work of generating options, evaluating alternatives, calibrating confidence, and making consequential decisions — at moments when research design decisions are made.

Diverga's checkpoint system creates structured sites where this redistribution becomes observable: whether the human engages in genuine deliberation across VS-generated alternatives — one modal (T > 0.8), one contextually appropriate (T ~ 0.5), and one non-modal but theoretically defensible (T < 0.3) — or defaults to the modal option without inspection, determines whether the redistribution resulted in expanded or constrained epistemic agency. This distinction — between deliberate engagement and automation deference at the checkpoint — is the central empirical question the study is designed to answer.

### 3.2 Authentic Learning as Evaluative Standard

Herrington et al.'s (2010) Authentic Learning framework provides the normative standard against which Diverga's effects are evaluated. Authentic learning involves: ill-defined, complex tasks; multiple perspectives; collaborative knowledge construction; reflection and metacognition; and articulation that renders tacit knowledge explicit. Diverga's design is explicitly informed by these features: VS methodology surfaces multiple perspectives (alternatives across paradigms); T-Score visibility makes implicit typicality judgments explicit (supporting metacognition); forced deliberation at checkpoints creates natural articulation moments. Whether the system succeeds in producing these effects — or whether participants bypass the deliberation the architecture invites — is what the study examines.

**[See Table 5: Authentic Learning Characteristics × Diverga Mechanisms × Study Observation Points]**

### 3.3 Activity Theory and Contradiction Analysis

Activity Theory (Engeström, 1987) provides the analytical lens for identifying tensions within the human-Diverga research design activity system. The primary contradiction under investigation is between *tool mediation* (checkpoint as epistemic scaffold, extending the researcher's methodological reach) and *normative constraint* (checkpoint as governance mechanism, limiting exploration to system-generated alternatives). Secondary contradictions are examined between the community of practice norms of the participant's discipline (established methodological expectations) and the VS recommendations that may challenge those norms. These contradictions surface in think-aloud data at checkpoints and in interview reflections on perceived vs. actual agency.

---

**Table 5. Authentic Learning Characteristics × Diverga Mechanisms × Study Observation Points**

| AL Characteristic (Herrington et al., 2010) | Diverga Mechanism | Study Observation Point |
|---|---|---|
| Ill-defined complex tasks | Research design scenarios (Scenarios A and B) | Pre-task artifact complexity assessment |
| Multiple perspectives | VS T-Score alternatives (5 paradigm personas) | DSE measurement; think-aloud at checkpoints |
| Reflection and metacognition | T-Score visibility; forced checkpoint pause | Think-aloud during checkpoint deliberation |
| Articulation (tacit → explicit) | REQUIRED checkpoint: must select and proceed | Interview: "Why did you choose that option?" |
| Authentic assessment | Comparison of pre-task vs. re-design artifact | Artifact analysis: framework diversity, coherence |

---

## 4. Design Research Methodology [Prose draft — ~350 of target ~600 words]

This study employs a design-based research approach (McKenney & Reeves, 2012) in which Diverga is the designed intervention under evaluation, and the research contributes both empirical findings and design principles for the broader field. The study constitutes Phase 2 of a broader EDR cycle: Phase 1 (design and construction of Diverga through five iterative cycles, n=224 commits) is reported in You & Yang (Paper 1, under review at IJDL). The present study reports the initial evaluation phase, contributing design knowledge that will inform subsequent design iteration.

The design-based framing is appropriate for three reasons. First, Diverga's architecture embodies design decisions — the checkpoint-enforcement mechanism, the T-Score typicality scale, the VS methodology — that are themselves theoretical claims about how artificial agency can support authentic learning. The study tests these claims in a naturalistic task context. Second, the small N (5 participants) is appropriate for an initial evaluation phase: the goal is to generate rich, process-level data sufficient to derive design principles and identify critical tensions for subsequent iteration, not to achieve statistical generalization. Third, ETR&D's design-based research genre supports the publication of evaluation studies before large-scale empirical replication, recognizing that design knowledge requires iterative refinement rather than single-study validation.

---

## 5. Study Design [Integrating from experimental_design_v2.md]

### 5.1 Research Context

Penn State College of Education doctoral students in social science fields. Diverga was developed at Penn State; the researcher is the developer (reflexivity addressed in §8.2). Recruitment through doctoral listservs and research methods courses.

### 5.2 Participants

N=5, purposeful maximum variation sampling across four dimensions (see Table 6). Selection ensures the sample covers AI knowledge × methodology expertise × disposition × disciplinary identity variation space. Minimum 2 participants with high AI knowledge; minimum 2 with low AI knowledge.

**IRB status:** Application preparation planned April–May 2026. Data collection planned August–September 2026.

**[See Table 6: Sample Profiling Matrix (Illustrative)]**

---

**Table 6. Sample Profiling Matrix (Illustrative — Actual Participants TBD Post-IRB)**

| Participant | AI Knowledge | Methodology Expertise | Disposition | Discipline |
|---|---|---|---|---|
| P1 | High | Advanced | Challenge-seeking | Educational Psychology |
| P2 | Low | Intermediate | Conservative | Curriculum & Instruction |
| P3 | High | Novice | Balanced | Communication |
| P4 | Low | Advanced | Challenge-seeking | Sociology of Education |
| P5 | Moderate | Intermediate | Conservative | Higher Education |

*Note: Maximum variation sampling; actual participants selected based on screening instrument.*

---

### 5.3 Research Scenarios

**Scenario A:** "The impact of AI tools on K-12 student academic achievement"
- *Primary modal trap:* Davis (1989) Technology Acceptance Model; UTAUT variants
- *VS-generatable alternatives:* Sociocultural perspectives on technology (Vygotsky-derived), sociotechnical systems theory, critical platform studies lens, learning analytics-oriented frameworks

**Scenario B:** "What factors shape academic socialization and research identity formation among first-generation doctoral students from racially underrepresented groups in STEM fields?"
- *Primary modal trap:* Bandura's (1986) Social Cognitive Theory; Bronfenbrenner's (1979) ecological systems model
- *VS-generatable alternatives:* Yosso's (2005) Cultural Wealth Model, Communities of Practice (Wenger, 1998), Critical Race Theory applied to higher education, intersectionality frameworks, TrioEd-informed models, funds of knowledge framework

*Counterbalancing:* 3 participants receive Scenario A → B order; 2 receive B → A.

**[See Figure 3: Study Session Protocol]**

### 5.4 Session Protocol Summary

**[See Table 7: Session Protocol Summary]**

---

**Table 7. Session Protocol Summary**

| Phase | Task | Duration | Data Collected |
|---|---|---|---|
| **Phase 0: Baseline** | Design a study on Scenario A (counterbalanced: some B). Written in Google Doc. No AI tools. | 30 min | Pre-task artifact (Google Doc) |
| **Phase 1: Orientation** | Diverga walkthrough: checkpoint system, VS/T-Score, practice with neutral scenario. | 20 min | Orientation log (informal) |
| *Break* | | 5 min | — |
| **Phase 2: Diverga-Assisted** | Design a study on Scenario B (counterbalanced). Diverga + concurrent think-aloud. | 60 min | decision-log.yaml, think-aloud audio, screen recording |
| *Break* | | 5 min | — |
| **Phase 3: Re-design** | Revisit Scenario A with Diverga. Think-aloud. How does approach change? | 40 min | decision-log.yaml, think-aloud audio, screen recording, re-design artifact |
| **Phase 4: Interview** | Semi-structured interview. 4 blocks (see §5.5). | 25–30 min | Interview audio, researcher field notes |

*Total session: approximately 2.5–3 hours including breaks.*

### 5.5 Data Sources

**[See Figure 4: Mixed Methods Data Integration Design]**

**[See Table 8: Data Sources and Analysis Purposes]**

---

**Table 8. Data Sources and Analysis Purposes**

| Data Source | Collection Method | Primary Analysis Purpose | Strand |
|---|---|---|---|
| Pre-task artifact | Google Doc (unaided) | Baseline: methodological reasoning without AI scaffolding | QUAL |
| Checkpoint logs | decision-log.yaml | Selection patterns, T-Score choices, deliberation indicators | QUAN + QUAL |
| Think-aloud transcripts | Screen + audio recording | Cognitive processes at checkpoints; reasoning about alternatives | QUAL |
| Screen recordings | Zoom cloud recording | Behavioral patterns: T-Score inspection, navigation, time-on-task | QUAN + QUAL |
| Post-task artifact | Diverga-assisted output | Framework diversity, design quality, comparison with pre-task | QUAL |
| Re-design artifact | Diverga-assisted output | Change patterns when revisiting unaided scenario with Diverga | QUAL |
| Semi-structured interview | Post-session audio recording | Reflective interpretation, perceived vs. actual agency | QUAL |
| Researcher field notes | During + immediately post-session | Contextual observations, nonverbal cues, technical incidents | QUAL |

---

## 6. Analysis Plan [OUTLINE — ~800 words target]

### 6.1 CMAA Application (Quantitative Strand)

Per participant, per session:
- **PIR:** Checkpoint interactions / total agent activations (decision-log.yaml, checkpoint_type field)
- **DSE:** Mean T-Score range per REQUIRED checkpoint (T_max − T_min, averaged across session)
- **GCA:** REQUIRED checkpoint status = "enforced" count / total REQUIRED checkpoints encountered
- **SUD:** Session-to-session DAT entry reference count (cross-session analysis only for multi-session participants)
- **CCI:** Mean dependency chain length per session (agent activation log + prerequisite graph)
- **Typicality Trajectory:** T-Score of selected option plotted sequentially across REQUIRED checkpoints per session

### 6.2 Activity Theory Contradiction Analysis (Qualitative Strand)

**Coding unit:** Think-aloud utterances at or immediately surrounding checkpoints; interview reflections on specific checkpoint decisions
**[See Table 9: AT Contradiction Coding Scheme (Preliminary)]**

### 6.3 Mixed Methods Integration

**Joint display design:** Cross-participant matrix — rows = participants, columns = CMAA indicator values + AT contradiction type. Integration question: Where do high DSE scores (wide alternative space presented) co-occur with modal T-Score selection (T > 0.8 chosen)? This intersection — the participant saw diverse alternatives and selected the predictable one anyway — is the primary evidence signature for automation bias in the epistemic domain, and requires think-aloud data to explain *why*.

---

**Table 9. AT Contradiction Coding Scheme (Preliminary)**

| Code | Definition | Example Indicator |
|---|---|---|
| Tool-Scaffold | Checkpoint functions as epistemic scaffold; participant engages deliberatively with alternatives | "Oh, I hadn't considered Yosso — that actually fits better because..." |
| Tool-Constrain | Checkpoint constrains exploration; participant selects from presented options without generating own alternatives | "I'll just go with that one" [selects without reviewing T-Score] |
| Norm-Conflict | Participant's disciplinary community norms conflict with VS recommendation | "My advisor would never accept that framework in my field" |
| Override-Explicit | Participant explicitly overrides or rejects system recommendation with articulated reasoning | "The system suggests TAM but that's not appropriate here because..." |
| Automation-Deference | Participant defers to system recommendation with minimal deliberation AND without inspecting alternative T-Scores (confirmed by log data showing negligible deliberation time); *note: a participant who reviews alternatives and reasonably selects the modal option is NOT coded here — the code requires both behavioral evidence of non-inspection and verbal deference* | "I'll just go with that one" [selects without scrolling to T-Score; log confirms < 5s at checkpoint] |

---

## 7. Design Principles [Preliminary — ETR&D Required Section]

> **Note:** Preliminary principles derived from Diverga's design phase. To be refined from empirical findings after data collection.

**DP1 — Mandatory checkpoint architecture:** Checkpoints must be architecturally enforced (not advisory) to function as meaningful epistemic redistribution points. Advisory checkpoints are routinely bypassed; only REQUIRED checkpoints generate the deliberation that makes epistemic labour redistribution observable and educationally meaningful.

**DP2 — Typicality visibility is necessary but insufficient:** Presenting T-Scores to users increases deliberation time at checkpoints but does not alone prevent modal selection. Typicality visibility requires accompanying deliberation scaffolding (e.g., prompt: "The most novel option has T=0.2 — what would it mean for your research to choose this?") to activate genuine epistemic engagement.

**DP3 — Upstream decision openness:** Agentic AI systems should be designed so that downstream agents do not constrain the option space available at upstream checkpoints. If the theory-selection agent (upstream) implicitly forecloses methodological options for the design-methods agent (downstream), the epistemic redistribution at the upstream checkpoint is undermined by architectural coupling.

**DP4, DP5, DP6 — [TBD from empirical findings]**

---

## 8. Discussion [OUTLINE — ~700 words target]

### 8.1 Theoretical Contributions
- First empirical application of CMAA (You & Yang, Paper 2)
- Evidence base for artificial agency effects on doctoral research methodology reasoning
- Activity Theory contradiction analysis as complement to CMAA quantitative indicators

### 8.2 Reflexivity and Limitations

The researcher occupies a dual role in this study as both system developer and primary investigator — a position that introduces layered reflexivity obligations beyond what a standard researcher positionality statement addresses. As developer, the researcher possesses architectural knowledge of Diverga that participants do not share: specifically, knowledge of what T-Score distributions each checkpoint is designed to present and which selection patterns the system is designed to encourage. This foreknowledge creates a risk that data interpretation will be shaped by confirmation of design intent rather than open-ended analysis of participant experience. Three structural safeguards are employed. First, Activity Theory contradiction coding (Table 9) is conducted by a second coder working from transcripts alone, without access to the checkpoint log data, before cross-analyst reconciliation — ensuring that qualitative interpretation is not anchored to quantitative patterns the developer can read in the logs. Second, the AT coding scheme includes codes explicitly designed to capture cases where Diverga constrains rather than supports epistemic agency (Tool-Constrain, Automation-Deference), providing an analytic pathway for negative findings that is structurally equivalent to codes capturing positive effects. Third, design principles DP4–DP6 are explicitly reserved for post-data-collection derivation and are not pre-specified, ensuring that the study can generate findings that contradict or qualify the design principles embedded in DP1–DP3. The researcher acknowledges that these safeguards reduce but do not eliminate the interpretive risks inherent in developer-investigator dual roles; readers should weigh findings accordingly and treat them as design-phase evidence informing subsequent independent replication rather than confirmatory findings.

Additional limitations:

- **N=5:** Findings are illustrative, not generalizable; statistical comparison is not attempted; patterns reflect individual cases and are reported as such.
- **Single system:** All findings are bounded to Diverga's implementation of checkpoint-governed agency; transferability requires testing across systems with different checkpoint architectures.
- **IRB-pending:** All participant protections to be formalized before data collection; protocol recommendations include third-party recruitment routing and researcher absence during Phases 2–3 to reduce coercion risk.
- **DP1–DP3 circularity:** Design principles DP1–DP3 are derived from Diverga's design phase and are instantiated in the system before the empirical evaluation begins. The study cannot provide an independent test of whether these principles are effective, because the system participants interact with has already been built to embody them. ETR&D readers should interpret DP1–DP3 as design-phase hypotheses — supported by design-based evidence (Paper 1) and theoretically grounded, but not independently validated by this study — and DP4–DP6 as empirically derived principles whose derivation this study enables. Subsequent work replicating the study with a system designed by independent developers would be required to test DP1–DP3 without the circularity inherent in developer-evaluation designs.
- **T-Score calibration:** DSE indicator values depend on T-Scores generated by Diverga's VS engine, which is not independently validated. A participant selecting a T=0.25 option may be selecting a genuinely non-modal framework or whatever the VS engine labeled as novel; these are not equivalent, and the study has no mechanism to distinguish them. This limits the interpretability of DSE as an objective typicality measure.
- **Orientation phase priming:** Phase 1 teaches the VS/T-Score typicality logic before data collection. Participants primed to understand that "non-modal options have lower T-Scores" may select lower T-Score alternatives not because the system genuinely expanded their epistemic space, but because the orientation established that doing so is evaluatively correct in this context. This procedural demand characteristic is embedded in the study design and limits causal attribution of low T-Score selections to the checkpoint architecture's independent effect.
- **Data linkability:** Checkpoint interaction logs (decision-log.yaml) are generated by Diverga, to which the researcher has administrative access. Session log files may in principle be linked to participant identity via timestamps or session IDs. Prior to IRB submission, a data de-identification protocol will be established: participant IDs assigned at consent, linkage map held separately, and raw log file access restricted to the research team.

### 8.3 Implications for Practice
- Design guidance for researchers and developers building agentic AI for research education
- Implications for doctoral program design: when and how to introduce AI-assisted methodology tools
- Checkpoint-governed AI as complement (not replacement) for advisor mentorship in methodology learning

---

## 9. Conclusion [OUTLINE — ~300 words target]

- Study contribution: first empirical application of CMAA in a naturalistic doctoral research design context
- Design-based research contribution: 6 design principles for checkpoint-governed agentic AI in education
- Limitation and future directions: N=20+ replication study planned; cross-institutional validation

---

## References [Working list]

Bandura, A. (1986). *Social foundations of thought and action: A social cognitive theory*. Prentice-Hall.

Bronfenbrenner, U. (1979). *The ecology of human development*. Harvard University Press.

Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. *MIS Quarterly, 13*(3), 319–340.

Engeström, Y. (1987). *Learning by expanding*. Orienta-Konsultit.

Ericsson, K. A., & Simon, H. A. (1993). *Protocol analysis: Verbal reports as data* (rev. ed.). MIT Press.

Floridi, L. (2025). AI as agency without intelligence: On artificial intelligence as a new form of artificial agency. *Philosophy & Technology, 38*, 30.

Herrington, J., Reeves, T. C., & Oliver, R. (2010). *A guide to authentic e-learning*. Routledge.

Hughes, L., Dwivedi, Y. K., Malik, T., Shawosh, M., Albashrawi, M. A., Jeon, I., ... & Walton, P. (2025). AI agents and agentic systems: A multi-expert analysis. *Journal of Computer Information Systems*, 1–29.

Järvelä, S., Nguyen, A., & Hadwin, A. (2023). Human and artificial intelligence collaboration for socially shared regulation in learning. *British Journal of Educational Technology, 54*(5), 1057–1076.

McKenney, S., & Reeves, T. C. (2012). *Conducting educational design research*. Routledge.

Ouyang, F., & Jiao, P. (2021). Artificial intelligence in education: The three paradigms. *Computers and Education: Artificial Intelligence, 2*, 100020.

Stake, R. E. (2006). *Multiple case study analysis*. Guilford.

Vaccaro, M., Almaatouq, A., & Malone, T. (2024). When combinations of humans and AI are useful: A systematic review and meta-analysis. *Nature Human Behaviour, 8*(12), 2293–2303.

Wenger, E. (1998). *Communities of practice: Learning, meaning, and identity*. Cambridge University Press.

Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., & Lin, Y. (2024). A survey on large language model based autonomous agents. *Frontiers of Computer Science, 18*(6), 186345.

Yan, L., Sha, L., Zhao, L., Li, Y., Martinez-Maldonado, R., Chen, G., ... & Gašević, D. (2024). Practical and ethical challenges of large language models in education. *British Journal of Educational Technology, 55*(1), 90–112.

Yin, R. K. (2018). *Case study research and design* (6th ed.). Sage.

Yosso, T. J. (2005). Whose culture has capital? A critical race theory discussion of community cultural wealth. *Race, Ethnicity and Education, 8*(1), 69–91.

You, H., & Yang, M. (2027a). [Paper 1 — design case title TBD]. *International Journal of Designs for Learning*. [under review]

You, H., & Yang, M. (2027b). Checkpoint-Mediated Agency Analysis: A methodology for studying artificial agency effects in multi-agent AI educational systems. *British Journal of Educational Technology*. [under preparation — Paper 2]

*[Complete APA 7th reference list in final manuscript.]*

---

## Figures

**Figure 3** — `figures/figure3_study_protocol.png`
Caption: *Figure 3. Study Session Protocol. Single-session within-subject design (N=5); approximate total duration 2.5–3 hours. Counterbalancing: 3 participants receive Scenario A first; 2 receive Scenario B first.*

**Figure 4** — `figures/figure4_data_integration.png`
Caption: *Figure 4. Mixed Methods Data Integration Design. Convergent design: QUAN (CMAA) and QUAL (AT contradiction analysis) strands analyzed independently and integrated at meta-inference stage via joint display.*
