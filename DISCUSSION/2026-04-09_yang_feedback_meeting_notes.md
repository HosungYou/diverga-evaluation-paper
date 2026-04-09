# Meeting Notes: Dr. Yang Feedback on Paper 2 Direction

**Date**: 2026-04-09
**Participants**: Co-Investigator (Hosung You), Principal Investigator (Mohan Yang)
**Context**: Follow-up meeting after the Research Design v1 and Paper 2/3 v3 drafts were shared for review (see v0.3.0 and v0.4.0 releases)
**Related documents**:
- `Research_Design_IRB/Research_Design_IRB_v1.docx`
- `Paper2_BJET_Methodological/Paper2_BJET_APA7_draft_v3.docx`
- `Paper3_Experimental/Paper3_CE_AI_APA7_draft_v3.docx`

---

## 1. Summary of Dr. Yang's Feedback

Dr. Yang reviewed the Paper 2 direction and provided six substantive critiques. These critiques collectively push the paper away from a purely conceptual contribution and toward a methodologically grounded, empirically situated, and practically relevant paper that BJET readers can use.

### 1.1 Include empirical studies that have measured Artificial Agency

Paper 2 currently presents CMAA as an extension of Yang et al. (2025) HALIE application, but the broader landscape of prior attempts to measure artificial agency (as distinct from generative AI interaction) is not adequately represented. Dr. Yang noted that the paper must engage with the empirical literature on artificial agency measurement, not only the philosophical (Floridi) and framework-level (HALIE) literature. Paper 2 should identify which published studies have actually collected data with the goal of measuring the agentic properties of AI systems and should position CMAA relative to those attempts.

### 1.2 Create a comparison table of Performance of AI Agency measurements

Beyond narrative literature review, Dr. Yang requested a comparison table that juxtaposes the measurement approaches used in prior empirical studies of AI agency performance. This table should display, at a minimum, the construct measured, the specific metrics used, the sample and setting, the type of evidence generated (quantitative telemetry vs. qualitative coding vs. self-report), and the practical implications drawn. The table is meant to make CMAA's distinctive contribution visible at a glance by showing what existing approaches do and do not capture.

### 1.3 A theoretical construct alone is not meaningful

Dr. Yang was explicit: presenting a theoretical construct (artificial agency) with a set of operationalized indicators (CMAA) is not by itself a publishable contribution. The paper must demonstrate that the construct and the indicators produce actionable understanding that readers can apply in their own work. A framework paper with no empirical bite, or with empirical bite that only validates the framework internally, will not satisfy BJET reviewers.

### 1.4 The paper must answer "why it matters to others"

A related critique: the paper must explicitly state and justify why its contribution matters to readers who are not already working on checkpoint-governed agentic AI. This audience includes instructional designers, learning analytics researchers, doctoral methods instructors, and educational technology practitioners. The argument cannot be "we built a new thing and measured it"; it must be "we built and measured a new thing, and here is what you can do with this knowledge in your own context."

### 1.5 Technical terms must be softened or explained

Paper 2 v3 uses terminology (PIR, DSE, GCA, SUD, CCI, Typicality Trajectory, governance constraint activation, state utilization depth, coordination complexity index, decision audit database) that is dense and unfamiliar to most BJET readers. Dr. Yang asked that the paper either soften the language or provide plain-language explanations adjacent to each technical term. BJET's readership spans educational researchers and practitioners who do not have agentic-AI engineering backgrounds; if the paper cannot be read without a glossary, it will not travel.

### 1.6 A solid theoretical framework is needed (added note)

In addition to the five points above, Dr. Yang emphasized that the paper needs a solid theoretical framework. This is a separate concern from the empirical comparison (point 1.1) and from the practical relevance argument (point 1.4). Paper 2 v3 invokes Floridi (2025) and HALIE (Lee et al., 2023) as anchors, and Fowler (2025) as a background analogue, but the integration among these sources is not tight enough to carry the paper's theoretical weight alone. A dedicated theoretical framework section should make explicit (a) which theoretical tradition the paper is extending, (b) what the relationships among Floridi, HALIE, and activity-theoretical work are, and (c) what theoretical contribution the paper makes beyond operationalizing an existing framework.

---

## 2. Literature Review: Papers Cited During the Discussion

Three papers were shared during the meeting as potentially relevant for expanding the Paper 2 literature review and for building the comparison table requested in point 1.2. Two of the three were accessible and reviewed; the third is behind a paywall and requires follow-up.

### 2.1 Jiang, T., Sun, Z., Fu, S., & Lv, Y. (2024)

**Citation**: Jiang, T., Sun, Z., Fu, S., & Lv, Y. (2024). Human-AI interaction research agenda: A user-centered perspective. *Data and Information Management, 8*(4), Article 100078. https://doi.org/10.1016/j.dim.2024.100078

**Construct measured**: Human-AI Interaction (HAII) as a multi-dimensional construct encompassing collaboration, competition, conflict, and symbiosis.

**Design**: Literature review with agenda-setting intent. Draws from communication, psychology, and sociology to identify research themes, theoretical foundations, and methodological frameworks for HAII research.

**Measurement approaches identified**: The authors characterize the existing HAII literature as dominated by self-reporting (surveys, scales, interview-based measures) and observational approaches (log analysis, behavior coding, interaction analytics). They do not introduce new metrics; instead they map existing ones into a taxonomy.

**Key recommendations**:
- Broaden HAII research beyond dyadic human-AI pairs to diverse user groups, AI roles, and tasks.
- Develop multi-disciplinary theories that integrate insights from communication, psychology, and sociology.
- Employ multi-level research methods that combine self-report and behavioral data.

**Relevance to Paper 2**:
- Useful as a framing reference in the literature review to establish that HAII measurement is an active research agenda with recognized gaps.
- The "collaboration, competition, conflict, symbiosis" taxonomy can be referenced to position checkpoint-governed agency as a form of structured collaboration.
- Does not itself provide empirical measurement of AI agency performance, so it supports the narrative review but not the comparison table directly.

### 2.2 Fragiadakis, G., Diou, C., Kousiouris, G., & Nikolaidou, M. (2024, revised 2025)

**Citation**: Fragiadakis, G., Diou, C., Kousiouris, G., & Nikolaidou, M. (2024). Evaluating human-AI collaboration: A review and methodological framework. *arXiv preprint arXiv:2407.19098*.

**Construct measured**: Human-AI Collaboration (HAIC) effectiveness across three collaboration modes (AI-centric, human-centric, symbiotic).

**Design**: Literature review followed by framework development. The authors propose a decision-tree-based framework that guides metric selection according to collaboration mode and application domain.

**Measurement approach**: The framework is meta-methodological, not a new instrument. It helps researchers select from existing metrics rather than introducing new ones. Key distinctions are made between quantitative metrics (task completion time, error rate, accuracy, system usability) and qualitative metrics (trust, satisfaction, perceived workload, perceived control).

**Three HAIC modes**:
- **AI-centric**: AI leads, human supervises. Metrics emphasize AI accuracy and human trust calibration.
- **Human-centric**: Human leads, AI supports. Metrics emphasize task completion time, user autonomy, and cognitive load.
- **Symbiotic**: Joint co-creation. Metrics emphasize coordination efficiency and shared decision quality.

**Practical implications**: The authors apply the framework to manufacturing, healthcare, finance, and education. Education application emphasizes learning outcomes and user engagement as symbiotic-mode metrics.

**Relevance to Paper 2**:
- Directly relevant because it defines HAIC and proposes a selection framework for metrics, making it a natural predecessor to CMAA.
- The three-mode taxonomy (AI-centric, human-centric, symbiotic) provides a useful reference for positioning checkpoint-governed agency as a structured symbiotic mode.
- Can be cited as evidence that the field recognizes the need for mode-specific metric selection; CMAA can be positioned as a concrete instantiation of symbiotic-mode metrics for an educational context.
- Would be a strong entry in the comparison table (Yang's point 1.2).

### 2.3 Bigman, Y. E., Briker, R., & Langer, M. (2026)

**Citation**: Bigman, Y. E., Briker, R., & Langer, M. (2026). Human-AI interaction research needs to be embedded in psychological theory. *Nature Reviews Psychology, 5*(April), 233-234. https://doi.org/10.1038/s44159-026-00551-4

**Article type**: Comment (two pages), published online 20 March 2026. Not an empirical study and not a full review; it is a short theoretical intervention by three researchers (Hebrew University of Jerusalem, Otto Beisheim School of Management, University of Freiburg) arguing for a programmatic shift in how Human-AI interaction research is conducted.

**Core argument**: Human-AI interaction research can become outdated quickly because AI technologies evolve faster than even fast-paced research can be published. To ensure cumulative insights that outlast the latest model release, research should meaningfully rely on psychological theory to explain, predict, and anticipate human-AI interaction. Without clear embedding in psychological theory, research carries the risk of generating findings that lack generalizability beyond a particular AI version, and the resulting insights can quickly lose relevance as the technology evolves.

**Two approaches to embedding research in theory**:

- **Approach 1: Apply or extend existing psychological theories.** Although cutting-edge AI systems are non-human, for many forms of interaction the type of agent one interacts with might not fundamentally matter. Humans might respond to friendly words or assistance from an AI in similar ways to how they respond to humans. The authors illustrate this with studies on social penalties of using generative AI that rely on attribution theory to predict whether and how people penalize users of AI.
- **Approach 2: Develop novel psychological theories.** For properties that have no clear human-human analogue, existing theories may create blind spots. The authors note that interaction between humans can be explained by perceptions of warmth and competence, but additional constructs might be necessary to explain and predict human-AI interaction, and such novel constructs would remain undetected under human-human theoretical lenses.

**Three practical recommendations for embedding research in theory**:

1. **Coherence**: Researchers should consider how or whether their research connects to existing theory. A researcher studying persuasion by AI should examine to what extent their findings support or challenge foundational theories of persuasion. Without coherence, new findings remain disconnected and fragmented. If findings are fully consistent with human-human psychology, researchers should adopt the approach of explaining human-AI interaction with existing human-human interaction theory; if existing theories fail to explain the new findings, researchers should develop novel theories to explain human-AI interaction.

2. **Distinctiveness from human-human interaction**: Researchers should consider how interacting with AI is similar to or distinct from interacting with humans. A researcher studying trust in AI should ask whether and how trust in AI is different from trust in humans. More specifically, research should aim to identify the psychological or interaction attributes that cause people to trust AIs in ways that overlap with or differ from how they trust humans. Without considering distinctiveness, research may unveil a new phenomenon while merely using "old wine in a new barrel."

3. **Generalizability**: Researchers should aim for and explicitly discuss generalizability. The key question is how much human-AI interaction research can generalize as technology has evolved and continues to evolve. A researcher studying reactions to empathy by AI using ChatGPT 5.2 should ask to what extent the findings and insights are relevant or generalizable to future LLMs or to entirely new technology.

**Key references cited by Bigman et al.**:

- Whetten, D. A. (1989). What constitutes a theoretical contribution? *Academy of Management Review, 14*, 490-495.
- Kuhn, T. S. (1962). *The structure of scientific revolutions*. University of Chicago Press.
- Vaccaro, M., Almaatouq, A., & Malone, T. (2024). When combinations of humans and AI are useful: A systematic review and meta-analysis. *Nature Human Behaviour, 8*, 2293-2303.
- Berente, N., Gu, B., Recker, J., & Santhanam, R. (2021). Managing artificial intelligence. *MIS Quarterly, 45*, 1433-1450.
- Reif, J. A. M., Larrick, R. P., & Soll, J. B. (2025). Evidence of a social evaluation penalty for using AI. *Proceedings of the National Academy of Sciences, 122*, e2426766122.
- De Freitas, J., et al. (2025). AI companions reduce loneliness. *Journal of Consumer Research*.
- Rahwan, I., Shariff, A., & Bonnefon, J. F. (2025). The science fiction science method. *Nature, 644*, 51-58.

**Relevance to Paper 2 and Dr. Yang's feedback**:

This Comment is the most directly relevant of the three papers reviewed at the meeting because it speaks to Dr. Yang's feedback point 1.6 on theoretical framework. Bigman and colleagues argue that Human-AI interaction research that is not embedded in psychological theory carries the risk of generating findings that lack generalizability beyond a particular AI version. Paper 2 v3 currently anchors CMAA in Floridi's philosophy of artificial agency and in HALIE as a methodological framework, but it does not make explicit connections to psychological constructs such as trust, attribution, self-regulation, automation bias, epistemic agency, or social cognition.

Three specific implications follow for Paper 2 v4:

1. **Coherence check**: Paper 2 v4 must explicitly state which psychological theories (or families of theories) CMAA connects to. Candidates include shared regulation of learning (Jarvela et al., 2023), automation bias and algorithm aversion (Bucinca et al., 2021), social cognition applied to AI (Bigman et al., 2019), and epistemic cognition (Chinn, Buckland, & Samarapungavan, 2011). Without at least one clearly articulated psychological theory as a coherence anchor, the paper's theoretical framework will remain primarily philosophical (Floridi) and methodological (HALIE), which is the weakness Dr. Yang identified.

2. **Distinctiveness argument**: Paper 2 v4 should include a paragraph on how engagement with checkpoint-governed agentic AI differs from engagement with human research advisors, human methodology peers, or static research methods references. The checkpoint is structurally a form of advisor intervention, and doctoral students have prior models for how to engage with advisor feedback. CMAA indicators should be positioned as capturing either (a) interaction attributes that map onto human-human advisor attributes (supporting distinction by degree) or (b) interaction attributes that have no human-human counterpart (supporting distinction by kind). This is a theoretical move, not just a rhetorical one, because it commits the paper to one side of the debate about whether AI agency is categorically different from or continuous with human agency.

3. **Generalizability statement**: Paper 2 v4 needs explicit language about how CMAA is designed to generalize. Bigman et al. warn that findings tied to a specific model version become outdated. CMAA can rebut this concern by being operationalized at the architectural level (checkpoints, alternative generation, enforcement mechanisms) rather than at the model-specific level (e.g., Claude 3.7 vs Claude 4.0). The architectural framing already exists in the v3 draft but needs to be made explicit as a generalizability argument.

**Action item**: The Bigman et al. (2026) paper should be added to the Paper 2 v4 reference list and cited in two places: (a) the theoretical framework section as the rationale for requiring coherence with psychological theory, and (b) the limitations or future directions section as the rationale for why CMAA's architectural framing is designed to outlast specific AI model versions.

---

## 2A. Additional Feedback on Paper 1 (Design Case for IJDL)

Dr. Yang also noted a concern about Paper 1 (the Design Case manuscript targeting International Journal of Designs for Learning). Paper 1 currently documents evaluation phases and the iterative modifications made across five design cycles, but the rationale for why each design choice was made is not yet robust enough.

### 2A.1 Verbatim feedback

The design cycles and iterations are present in the current Paper 1 draft, but the document does not yet make a sufficiently strong case for why the specific design decisions were made at each cycle. Design cases in the IJDL tradition require that every design choice be justified not only by reference to what was implemented but by reference to the design rationale: what problem was identified, what alternatives were considered, which alternative was selected and on what grounds, and how the selection was later evaluated for success or failure.

### 2A.2 Interpretation and implications

This feedback is aligned with the IJDL editorial norms for design case manuscripts, which are more stringent about design rationale than a typical empirical paper. The IJDL design case tradition (Boling, 2010; Smith, 2010; Howard et al., 2012) treats the design rationale as the scholarly contribution, not the artifact itself. A reader of a design case should be able to reconstruct the author's decision-making well enough to apply the same decision logic in their own context.

The current Paper 1 draft is structured around five design cycles with documented modifications (the 44-to-29 agent consolidation, the autonomous mode removal, the checkpoint bypass incident and governance tightening, the three-layer memory introduction, and the VS T-score formalization). Each of these is described in terms of what changed, but Dr. Yang's feedback implies that the paper needs to also include, for each cycle:

- What problem or design tension triggered the decision to modify.
- What alternatives were considered (including alternatives that were rejected and why).
- Which alternative was selected and on what grounds.
- What success criterion was defined at the time of the decision.
- How the subsequent cycle evaluated whether the decision succeeded, and what was learned.

This is a substantial addition to the existing draft and should be handled in a Paper 1 v3 revision. It is out of scope for the Paper 2 v4 work but should be logged as a separate workstream so that Paper 1 is not blocked by Paper 2.

### 2A.3 Action items for Paper 1

- Retrieve design cycle commit logs from the Diverga repository (the Co-Investigator already has 224 version-controlled commits spanning 57 days) and extract, for each of the five cycles, the problem statement that triggered the cycle.
- For each design decision documented in the current Paper 1 draft, add a "Decision Rationale" subsection with the four elements above: trigger problem, alternatives considered, selection grounds, success criterion.
- Revisit the figures in Paper 1 to ensure that each figure displays a decision rather than merely a final state.
- Plan a Paper 1 v3 draft following the Paper 2 v4 work, with target completion in late May 2026 if Paper 2 v4 is submitted by the August 1, 2026 BJET abstract deadline.

---

## 3. Synthesis: What Paper 2 v4 Will Need to Address

Dr. Yang's six feedback points can be consolidated into four structural changes for Paper 2 v4.

### 3.1 Expanded Literature Review with Comparison Table

A new subsection titled "Prior Approaches to Measuring Artificial Agency and Human-AI Interaction Performance" should be added between the existing theoretical framework and the CMAA framework sections. This subsection should contain:

- A narrative review of five to eight empirical studies that have measured AI agency, HAII, or HAIC performance. Candidates include Yang et al. (2025), Fragiadakis et al. (2024), Jiang et al. (2024), the Nature paper once accessible, and additional empirical studies to be identified. Acharya et al. (2025) and Hughes et al. (2025), already cited in Paper 2 v3, should be examined for whether they offer measurement data or only conceptual taxonomies.
- A table (proposed Table 2 in v4, replacing or preceding the current Tier 1 table) that displays one row per prior approach, with columns for: study, construct measured, measurement instruments or metrics, sample and setting, type of evidence produced (telemetry, qualitative coding, self-report, mixed), key findings, and gap or limitation that CMAA addresses. The last column is critical because it makes the paper's contribution visible at the level of the table alone.

### 3.2 Dedicated Theoretical Framework Section with Psychological Grounding

The current v3 collapses theoretical framework discussion into a single subsection within the broader "Theoretical Framework" chapter. Paper 2 v4 should elevate the theoretical framework to a more prominent position with four subsections, explicitly responding to Bigman et al.'s (2026) call for psychological theory embedding:

- **Artificial agency as defined by Floridi (2025)**: interactivity, bounded autonomy, adaptability. Present this as the philosophical foundation, but make explicit that philosophical definition alone is not sufficient grounding per Bigman et al. (2026).
- **Psychological theory embedding**: connect CMAA to at least one established psychological theory that explains why human researchers respond to checkpoint-mediated interaction the way they do. Candidates include automation bias and algorithm aversion (Bucinca et al., 2021; Dietvorst et al., 2015), shared regulation of learning (Jarvela et al., 2023), attribution theory applied to AI (Reif et al., 2025), or epistemic cognition (Chinn et al., 2011). Select one as the primary psychological anchor and articulate how CMAA indicators operationalize the psychological constructs that theory predicts will be consequential.
- **The HALIE framework (Lee et al., 2023) and its operationalization by Yang et al. (2025)**: present this as the methodological bridge that translates philosophical agency criteria into measurable educational outcomes.
- **Activity-theoretical situating of checkpoint-mediated scaffolding (Engestrom, 1987; Jarvela et al., 2023)**: present this as the sociocultural grounding that explains why the redistribution of epistemic labour at checkpoints matters for learning. Note that Paper 3 uses activity theory as its dominant frame; Paper 2 can reference it lightly without interleaving.
- **A concluding paragraph that names the theoretical contribution of Paper 2**: not merely operationalizing Floridi, not merely extending Yang et al., but integrating philosophical, psychological, methodological, and sociocultural levels into a single measurement framework for agentic AI in education. Explicitly cite Bigman et al. (2026) to frame this integration as a response to the call for psychologically grounded Human-AI interaction research.

### 3.3 "Why It Matters" Framing Throughout

Every section of Paper 2 v4 must include language that answers "why does this matter to me?" for the BJET reader. Specifically:

- The introduction should open with a concrete scenario that is recognizable to BJET readers (e.g., a doctoral student using Claude vs an agentic AI tool and what the educator would want to know about the interaction). Yang et al. (2025) opened with the nontraditional student digital divide; a similarly concrete opening would work for Paper 2.
- Each CMAA indicator should be accompanied by a "Why it matters" sentence that explains what the indicator tells an educator, designer, or researcher about the interaction, not just what it measures computationally.
- The discussion should include a subsection titled "Implications for Educational Practice" that translates the measurement framework into concrete questions educators can ask: "Is my students' interaction with this AI system producing the depth of engagement I want?" "Does this tool expand or narrow my students' methodological imagination?" "Which of my checkpoints are actually being respected?"

### 3.4 Accessibility Pass on Technical Language

A final editorial pass should review every technical term in Paper 2 v4 and either replace it with plain language, add a parenthetical gloss at first use, or move it to a definitions table. Target readers include BJET readers without an engineering background. Specific terms flagged:

- "Checkpoint-Mediated Agency Analysis" (CMAA) is defensible as a named methodology but should be glossed on first use as "a way to measure what happens at the structured decision points where an AI system pauses and asks the human researcher for input."
- "Proactive Intervention Rate" (PIR): gloss as "how often the AI system initiates the interaction compared to how often the user does."
- "Decision Space Expansion" (DSE): gloss as "whether the AI system broadens the set of options the user considers."
- "Governance Constraint Activation" (GCA): gloss as "how often the AI system's built-in rules stop the system from taking actions that would bypass human decisions." Currently the most obscure term.
- "State Utilization Depth" (SUD): gloss as "how much the AI system refers back to earlier parts of the project when making new recommendations."
- "Coordination Complexity Index" (CCI): gloss as "how many internal parts of the AI system work together to produce a given recommendation."
- "Typicality Trajectory": gloss as "the pattern of how novel or typical the user's choices become over the course of a session."
- "Decision audit database": gloss as "the record of every checkpoint decision, including what the user chose and what alternatives were presented."

---

## 4. Action Items

### Paper 2 workstream

| Action | Owner | Target Date |
|---|---|---|
| Nature Reviews Psychology Comment (Bigman, Briker, & Langer, 2026) already retrieved and reviewed | Co-I | Done (2026-04-09) |
| Identify three to five additional empirical studies of AI agency measurement for the comparison table | Co-I | 2026-04-13 |
| Draft the Prior Approaches comparison table with initial entries (Yang 2025, Fragiadakis 2024, Jiang 2024, Bigman 2026, Acharya 2025, Hughes 2025, and new entries) | Co-I | 2026-04-15 |
| Select the primary psychological theory anchor for Paper 2 v4 (automation bias, shared regulation, attribution, or epistemic cognition) | PI + Co-I | 2026-04-12 |
| Draft the expanded theoretical framework section with four subsections (Floridi, psychological anchor, HALIE/Yang, Engestrom), explicitly citing Bigman et al. (2026) | Co-I | 2026-04-16 |
| Draft "Why it matters" scenario-based opening paragraph for Paper 2 v4 | Co-I | 2026-04-15 |
| Add "Why it matters" sentences to each CMAA indicator definition | Co-I | 2026-04-15 |
| Draft "Implications for Educational Practice" discussion subsection | Co-I | 2026-04-18 |
| Technical language accessibility pass (gloss or replace all flagged terms) | Co-I | 2026-04-18 |
| Add distinctiveness paragraph comparing checkpoint engagement with human advisor engagement | Co-I | 2026-04-18 |
| Add generalizability statement framing CMAA as architecture-level rather than model-specific | Co-I | 2026-04-18 |
| PI review of Paper 2 v4 draft incorporating all feedback | PI | 2026-04-24 |
| Submit Paper 2 v4 abstract to BJET Special Issue by deadline | PI + Co-I | 2026-08-01 |

### Paper 1 workstream (separate from Paper 2 v4)

| Action | Owner | Target Date |
|---|---|---|
| Extract the design cycle commit logs from the Diverga repository and identify the trigger problem for each of the five design cycles | Co-I | 2026-04-20 |
| For each design decision in Paper 1 v2, add a Decision Rationale subsection with trigger problem, alternatives considered, selection grounds, and success criterion | Co-I | 2026-05-10 |
| Revise Paper 1 figures to display design decisions rather than final states | Co-I | 2026-05-15 |
| Draft Paper 1 v3 with the added design rationale throughout | Co-I | 2026-05-25 |
| PI review of Paper 1 v3 | PI | 2026-05-30 |
| Submit Paper 1 v3 to IJDL | PI + Co-I | 2026-06-15 |

---

## 5. Open Questions for Next Meeting

1. Is the six-point feedback above an exhaustive list of the concerns with Paper 2, or are there additional concerns that should be surfaced before v4 drafting begins? Clarifying this avoids a fourth round of revision.

2. Does the PI want the theoretical framework section to foreground Floridi (as in v3), foreground HALIE (which would tilt the paper toward Yang et al.'s methodological lineage), or foreground an integration of both? The three options have different reviewer resonances and different length budgets.

3. Should the comparison table include only studies that have measured artificial agency as a construct, or should it include adjacent studies that have measured related constructs (trust calibration, user autonomy, AI initiative) from which Paper 2 draws inspiration? The first option is more focused; the second is more comprehensive.

4. How should the "Why it matters" framing be balanced against the BJET Special Issue's methodological track requirement? The Special Issue explicitly welcomes methodological papers, and the risk of over-emphasizing practical relevance is that the paper reads as an applied paper rather than a methodological contribution. A middle path is needed.

5. Is it acceptable to add the phrase "and what practitioners should watch for" to several of the subsection headings as a rhetorical device, or does the PI prefer a more conservative section-heading style?

6. Does the PI want a new figure (conceptual diagram) that shows the relationship among Floridi, HALIE, activity theory, and CMAA in a single visual? This would address both the theoretical framework concern (1.6) and the accessibility concern (1.5) simultaneously, but it adds a figure budget to the manuscript.

---

## 6. Reference List for This Meeting

Acharya, D. B., Kuppan, K., & Divya, B. (2025). Agentic AI: Autonomous intelligence for complex goals: A comprehensive survey. *IEEE Access, 13*, 18912-18936.

Engestrom, Y. (1987). *Learning by expanding: An activity-theoretical approach to developmental research*. Orienta-Konsultit.

Floridi, L. (2025). AI as agency without intelligence: On artificial intelligence as a new form of artificial agency and the multiple realisability of agency thesis. *Philosophy & Technology, 38*, Article 30.

Fragiadakis, G., Diou, C., Kousiouris, G., & Nikolaidou, M. (2024). Evaluating human-AI collaboration: A review and methodological framework. *arXiv preprint arXiv:2407.19098*.

Hughes, L., Dwivedi, Y. K., Malik, T., Shawosh, M., Albashrawi, M. A., Jeon, I., & Walton, P. (2025). AI agents and agentic systems: A multi-expert analysis. *Journal of Computer Information Systems*, 1-29.

Jarvela, S., Nguyen, A., & Hadwin, A. (2023). Human and artificial intelligence collaboration for socially shared regulation in learning. *British Journal of Educational Technology, 54*(5), 1057-1076.

Jiang, T., Sun, Z., Fu, S., & Lv, Y. (2024). Human-AI interaction research agenda: A user-centered perspective. *Data and Information Management, 8*(4), Article 100078. https://doi.org/10.1016/j.dim.2024.100078

Lee, M., Srivastava, M., Hardy, A., Thickstun, J., Durmus, E., Paranjape, A., Gerard-Ursin, I., Li, X. L., Ladhak, F., Rong, F., Wang, R. E., Kwon, M., Park, J. S., Cao, H., Lee, T., Bommasani, R., Bernstein, M. S., & Liang, P. (2023). Evaluating human-language model interaction. *Transactions on Machine Learning Research*.

Bigman, Y. E., Briker, R., & Langer, M. (2026). Human-AI interaction research needs to be embedded in psychological theory. *Nature Reviews Psychology, 5*(April), 233-234. https://doi.org/10.1038/s44159-026-00551-4

Bucinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW1), Article 188.

Chinn, C. A., Buckland, L. A., & Samarapungavan, A. (2011). Expanding the dimensions of epistemic cognition: Arguments from philosophy and psychology. *Educational Psychologist, 46*(3), 141-167.

Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm aversion: People erroneously avoid algorithms after seeing them err. *Journal of Experimental Psychology: General, 144*(1), 114-126.

Reif, J. A. M., Larrick, R. P., & Soll, J. B. (2025). Evidence of a social evaluation penalty for using AI. *Proceedings of the National Academy of Sciences, 122*, e2426766122.

Whetten, D. A. (1989). What constitutes a theoretical contribution? *Academy of Management Review, 14*(4), 490-495.

Yang, M., Jiang, S., Li, B., Herman, K., Luo, T., Moots, S. C., & Lovett, N. (2025). Analysing nontraditional students' ChatGPT interaction, engagement, self-efficacy and performance: A mixed-methods approach. *British Journal of Educational Technology, 56*(6), 1973-2000. https://doi.org/10.1111/bjet.13588
