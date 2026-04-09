# Multi-Agent Deliberation: Measurement Pivot to Established Scales

**Date**: 2026-04-09
**Context**: The doctoral candidate requested a pivot of Paper 2's measurement approach away from invented CMAA terminology toward maximally borrowed, established, psychometrically validated scales. Four Diverga agents (D4, B1, A2, A1) were dispatched in parallel with `DIVERGA_TEAM_DISPATCH=1` markers to debate and recommend the optimal pivot strategy.

**Prior state**: Paper 2 v3 contains five invented Tier 2 indicators under the CMAA name: PIR (Proactive Intervention Rate), DSE (Decision Space Expansion), GCA (Governance Constraint Activation), SUD (State Utilization Depth), and CCI (Coordination Complexity Index). Tier 1 already borrows from Yang et al. (2025) HALIE application.

**User's core request**: "These terms are technical and not easily understood in one pass. I want to borrow from existing research that has measured performance, borrow terms from existing academic disciplines where possible, and develop academically established scales."

---

## Agent Outputs Summary

### D4 (Measurement Instrument Developer) primary recommendation

D4 conducted a psychometric replacement analysis for each CMAA indicator and produced a three-tier measurement battery.

- **PIR**: Partial replacement with **Mixed-Initiative Interaction** (Horvitz, 1999; Allen, Guinn, & Horvitz, 1999) for the behavioral count, supplemented by **Perceived Agency Subscale** from the Godspeed Questionnaire (Bartneck et al., 2009; alpha .70 to .85).
- **DSE**: Full replacement with **Consideration Set Size** (Hauser & Wernerfelt, 1990) combined with **Cognitive Forcing Functions** operationalization (Bucinca, Malaya, & Gajos, 2021). Supplementary: Decision Self-Efficacy Scale (O'Connor, 1995; alpha .92).
- **GCA**: Partial replacement. Replace user-facing dimension with **Trust in Automation Scale** (Jian, Bisantz, & Drury, 2000; 12 items, alpha .85 to .94). Retain the log-based constraint-activation count as the irreducible architectural measure.
- **SUD**: Full replacement with **Perceived Personalization Scale** (Komiak & Benbasat, 2006; 4 items, alpha .89). Behavioral side: Context Retention Rate adapted from Bordes, Boureau, and Weston (2017).
- **CCI**: Retain as invented (reframed via **Thompson 1967** task interdependence typology and **Malone and Crowston 1994** coordination theory). Rename as Inter-Agent Interdependence Depth.

Cross-cutting additions proposed by D4:
- NASA-TLX (Hart & Staveland, 1988) for cognitive workload
- SUS (Brooke, 1996) for usability baseline

D4's verdict: Move from 5 invented indicators to effectively 1.5 (CCI retained, GCA-architectural retained as log event). Contribution reframes as "the first measurement battery specifically calibrated to checkpoint-mediated agentic AI systems in educational contexts."

### B1 (Literature Review Strategist) replacement landscape

B1 provided 21 candidate instruments with citations, reliability evidence, and CMAA-indicator mappings.

- **PIR**: Strongest candidate Amershi et al. (2014) 4-level mixed-initiative coding scheme (Cohen's kappa .78 to .84).
- **DSE**: Strongest candidate Brodbeck et al. (2007) group information sampling paradigm (ratio-based).
- **GCA**: Strongest candidate **Logg, Minson, and Moore (2019) algorithm appreciation measure** (6-item scale, alpha .82). Also strong: Dietvorst, Simmons, and Massey (2015) algorithm aversion.
- **SUD**: Strongest candidate Knijnenburg et al. (2012) 28-item recommender system experience scale (alpha .80 to .91). Weakest coverage area.
- **CCI**: No adequate replacement. Closest candidates (Marks, Mathieu, & Zaccaro, 2001; Cooke et al., 2013) measure human team processes, not AI component coordination. B1 recommends retention.

General scales B1 identified for cross-cutting use:
- Trust in Automation (Jian et al., 2000; alpha .94)
- Propensity to Trust in Machines (Merritt et al., 2013; alpha .78)
- AI Literacy Scale (Ng et al., 2021; alpha .91)
- NASA-TLX (Hart & Staveland, 1988; test-retest r = .83)
- User Experience Questionnaire (Laugwitz, Held, & Schrepp, 2008; alpha .87 to .93)
- Subjective Fit Perception Scale (Shin, 2020; alpha .88)

B1's verdict: GCA has the strongest replacement landscape; SUD has the weakest; CCI should remain invented.

### A2 (Theoretical Framework Architect) coherence constraint

**A2 raised the most important constraint in the deliberation and partially disagreed with D4 and B1.**

A2's rule for borrowing: Any replacement scale must come from traditions that treat cognition as situated, regulated, or epistemically constructed. **Acceptable sources**: self-regulated learning (SRL, SSRL), epistemic cognition, metacognitive monitoring, collaborative regulation, achievement emotions. **Unacceptable sources even if psychometrically strong**: trust-in-automation (Jian), technology acceptance, algorithm aversion (Dietvorst, Logg), automation reliance, general HCI scales.

A2's rationale: "The Floridi + Chinn + Jarvela + HALIE + Engestrom stack is a psychological-philosophical-sociocultural hybrid, not an HCI stack. Pulling Trust in Automation or algorithm aversion would import engineering psychology assumptions that treat the human as a supervisory controller and the AI as a tool. That ontology is incompatible with Floridi's agency criteria and with Chinn's epistemic cognition framing, both of which treat the AI-human pair as an epistemic encounter, not a control loop."

A2's indicator-level recommendations:

- **PIR**: Replaceable with SRL help-seeking (Karabenick & Berger, 2013). Theoretically coherent.
- **DSE**: **Retain as invented**, reframed as "Epistemic Alternative Exposure" grounded in Chinn (2011) and Barzilai epistemic cognition. Carries part of the distinctiveness claim.
- **GCA**: **Must remain invented**. This is the irreducible contribution because it measures human veto/override of an AI capable of unilateral action, a phenomenon that literally did not exist before agentic AI. No pre-2023 scale can capture it. **Reframe as "Override Activation Rate."**
- **SUD**: Partially replaceable with transactive memory systems (Wegner 1987; Lewis, 2003) or distributed cognition measures.
- **CCI**: **Most replaceable of the five** via coregulation process metrics from Hadwin, Jarvela, and Miller (2018) SSRL coding schemes.

**A2 directly contradicts D4 and B1 on GCA replacement**: D4 proposed Jian Trust in Automation; B1 proposed Logg algorithm appreciation. A2 argues both would fragment the theoretical framework.

A2 also contradicts D4 on CCI retention: D4 and B1 want to keep CCI; A2 says CCI is the most replaceable because coregulation literature captures it.

A2's verdict: The pivot is theoretically sound IF executed surgically. Blanket replacement fragments the framework. Disciplined replacement from the SRL/epistemic cognition family strengthens it.

### A1 (Research Question Refiner) reformulation

A1 produced revised research questions reflecting the pivot.

- **RQ1 (revised)**: "How can a measurement battery composed primarily of established validated scales, adapted and integrated for checkpoint-governed multi-agent AI environments, capture artificial agency effects on educational decision-making that single-scale or single-tier approaches fail to detect?"
- **RQ2 (revised)**: "To what extent does a tiered battery combining HALIE-adapted metrics (Yang et al., 2025), established validated scales for agency, self-efficacy, and epistemic engagement, and a minimal set of checkpoint-architectural indicators reliably distinguish agentic AI participation from standard generative AI assistance in research methodology learning?"
- **RQ3**: Kept with minor adjustment (Typicality Trajectory analysis is method-agnostic and survives the pivot).
- **RQ4 (new, recommended)**: "Do the borrowed validated scales and the retained checkpoint-architectural indicators exhibit convergent validity in predicting learning outcomes and decision-quality markers, and where they diverge, what does that divergence reveal about the unique measurement affordances of checkpoint architectures?"

A1's verdict: RQ1 (revised) is the most publishable as the primary contribution claim, landing squarely in the BJET Special Issue's Methodological Approaches strand. RQ4 is strongly recommended because it converts the borrowing decision into an empirical claim with theoretical payoff, justifying the retained invented indicators.

---

## Critical Disagreements

Three substantive disagreements must be resolved before Paper 2 v4 drafting can begin.

### Disagreement 1: GCA replacement

**D4 and B1**: Replace GCA user-facing dimension with Trust in Automation (Jian) or Algorithm Aversion/Appreciation (Dietvorst, Logg). These are psychometrically strong and widely used.

**A2**: Absolutely not. These scales come from engineering psychology traditions that treat the human as a supervisory controller. They fragment the Floridi + Chinn + Jarvela theoretical framework. GCA must remain invented because it measures a phenomenon that did not exist pre-agentic AI.

**Resolution rule**: A2's coherence constraint wins. The user's request was to borrow from existing literature in a way that strengthens the framework, not to import scales that would fragment it. Trust in Automation and algorithm aversion scales are rejected for GCA. Retain GCA as invented, reframed as "Override Activation Rate" (A2's proposed accessible name) or similar.

### Disagreement 2: CCI retention vs. replacement

**D4**: Retain CCI (Inter-Agent Interdependence Depth) as invented because human team coordination scales are not directly transferable to LLM-to-LLM coordination.

**B1**: Retain CCI because genuinely novel; no established counterpart.

**A2**: Replace CCI with coregulation process metrics from Hadwin, Jarvela, and Miller (2018) SSRL coding schemes. CCI is the most replaceable.

**Resolution rule**: This is a genuine tension. D4 and B1 are correct that the agent-to-agent (machine-to-machine) coordination dimension is novel. A2 is correct that the human-AI coordination dimension can be captured by coregulation literature. The resolution is to split CCI into two measures: one log-derived architectural metric (retained, agent-to-agent coordination depth) and one borrowed measure (Hadwin et al., 2018 coregulation process metric applied to the human-AI pair). This dual approach preserves the novel agent-to-agent dimension while borrowing the human-AI dimension from the coherent SRL tradition.

### Disagreement 3: DSE replacement vs. retention

**D4**: Full replacement with Consideration Set Size (Hauser & Wernerfelt, 1990) plus Bucinca et al. (2021) cognitive forcing functions. Consumer psychology tradition is neutral on coherence.

**A2**: Retain as invented, reframed as "Epistemic Alternative Exposure." Chinn's evaluativist stance requires encountering genuine alternatives; measuring how the AI expands the human's considered option set has no clean existing analog.

**B1**: Hybrid needed; partial coverage from cognitive forcing function literature.

**Resolution rule**: A2's position is closer to the theoretical framework because DSE operationalizes Chinn's epistemic cognition. However, Bucinca et al. (2021) cognitive forcing functions literature is directly relevant and comes from a learning sciences (not engineering) tradition. Retain DSE as invented with the "Epistemic Alternative Exposure" rename, but explicitly ground it in Bucinca et al. (2021) cognitive forcing functions as the nearest empirical precedent in the educational AI literature.

---

## Synthesized Three-Tier Measurement Battery (Team Consensus)

Applying A2's coherence constraint as the governing rule, and resolving the three disagreements, the team's consensus measurement battery for Paper 2 v4 is as follows.

### Tier 1: HALIE-Adapted Metrics (unchanged from v3)

Borrowed from Yang et al. (2025) and the original sources cited there.

| Metric | Source | Items or Levels |
|---|---|---|
| Prompt number | Yang et al. (2025) | Count |
| Depth of Knowledge | Webb (2002); Yang et al. (2025, Appendix A) | 4-level rubric |
| Prompt relevance and evolution | Yang et al. (2025, Appendix A) | 4-level rubric |
| Originality | Yang et al. (2025, Appendix A) | 4-level rubric |
| Self-efficacy | Avey, Luthans, and Jensen (2009) via Yang et al. (2025) | 5 items, 5-point Likert |
| Engagement composite | Skinner, Kindermann, and Furrer (2009); Fredricks, Blumenfeld, and Paris (2004); Halverson and Graham (2019) via Yang et al. (2025) | 8 items, composite score |

### Tier 2: SRL and Epistemic Cognition Scales (borrowed, coherence-constrained)

Replacing three CMAA indicators with established scales from traditions compatible with the Floridi + Chinn + Jarvela theoretical framework.

| Replacement | Primary Source | Replaces | Theoretical Family |
|---|---|---|---|
| **AI-Initiated Support Frequency** | Karabenick and Berger (2013) self-regulated help-seeking; supplemented by Horvitz (1999) Mixed-Initiative coding for architectural behavior | **PIR** | Self-regulated learning |
| **Cross-Session Context Retention** | Adapted from Wegner (1987) and Lewis (2003) Transactive Memory Systems; log-based continuity measurement | **SUD** | Distributed cognition |
| **Human-AI Coregulation Depth** | Hadwin, Jarvela, and Miller (2018) socially shared regulation of learning process metrics | **CCI (human-AI dimension only)** | Collaborative regulation |

### Tier 3: Agentic-Irreducible Indicators (retained as invented, renamed for accessibility)

Two indicators plus one log-derived architectural metric, retained because they measure phenomena with no established counterpart in pre-agentic AI literature.

| Retained Indicator | New Accessible Name | Original CMAA Name | Theoretical Anchor | Rationale for Retention |
|---|---|---|---|---|
| Override activation rate | **Override Activation Rate** | GCA | Floridi (2025) bounded autonomy; A2 direct endorsement | Measures human veto of AI that could act unilaterally, a phenomenon that did not exist pre-2023. No pre-agentic scale captures this. |
| Epistemic alternative exposure | **Epistemic Alternative Exposure** | DSE | Chinn, Buckland, and Samarapungavan (2011) evaluativist stance; Bucinca et al. (2021) as empirical precedent | Measures whether the AI expands the human's epistemic option set. Chinn framework requires this measure. |
| Agent-to-agent interdependence (log only) | **Agent-to-Agent Interdependence** | CCI (agent-to-agent dimension only) | Malone and Crowston (1994); Thompson (1967) interdependence typology | Descriptive log metric of inter-agent coordination. Not a participant-measured construct. |

### Tier 4 (new, optional): Cross-Cutting Validated Scales

Added to strengthen the battery with established human-AI interaction measures, drawn from SRL-compatible traditions only.

| Scale | Source | Purpose | Coherence Notes |
|---|---|---|---|
| NASA-TLX (cognitive workload, 6 dimensions) | Hart and Staveland (1988) | Control for cognitive burden induced by checkpoint interaction | Acceptable: workload is orthogonal to the theoretical framework |
| AI Literacy Scale (control variable) | Ng, Leung, Chu, and Qiao (2021) | Control for AI literacy confounds in agency perception | Acceptable: literacy is an individual difference measure |

**Explicitly excluded** despite psychometric strength:
- Trust in Automation Scale (Jian et al., 2000) - rejected by A2 coherence constraint
- Algorithm Aversion / Appreciation (Dietvorst 2015, Logg 2019) - rejected by A2 coherence constraint
- System Usability Scale (Brooke, 1996) - generic HCI, does not strengthen psychological theory embedding
- User Experience Questionnaire (Laugwitz et al., 2008) - generic HCI, same issue

---

## Net Change Summary

| Metric | Before (CMAA v3) | After (Pivot) | Status |
|---|---|---|---|
| PIR | Invented | Replaced by AI-Initiated Support Frequency (Karabenick + Horvitz) | Borrowed |
| DSE | Invented | Retained, renamed Epistemic Alternative Exposure (Chinn + Bucinca) | Retained, renamed |
| GCA | Invented | Retained, renamed Override Activation Rate (Floridi bounded autonomy) | Retained, renamed |
| SUD | Invented | Replaced by Cross-Session Context Retention (transactive memory) | Borrowed |
| CCI | Invented | Split: Agent-to-Agent Interdependence (log metric, retained) + Human-AI Coregulation Depth (borrowed from Hadwin/Jarvela) | Split |

Net result: **From 5 invented indicators to 2 invented (renamed for accessibility) plus 1 log-derived architectural metric plus 3 borrowed scales**. The paper now draws on 5 distinct borrowed instruments plus 2 retained novel indicators, satisfying both the user's borrowing request and A2's distinctiveness requirement.

---

## Revised Research Questions (Adopted from A1)

The team adopts A1's revised RQs with no modifications.

- **RQ1**: How can a measurement battery composed primarily of established validated scales, adapted and integrated for checkpoint-governed multi-agent AI environments, capture artificial agency effects on educational decision-making that single-scale or single-tier approaches fail to detect?

- **RQ2**: To what extent does a tiered battery combining HALIE-adapted metrics (Yang et al., 2025), established validated scales for agency, self-efficacy, and epistemic engagement, and a minimal set of checkpoint-architectural indicators reliably distinguish agentic AI participation from standard generative AI assistance in research methodology learning?

- **RQ3**: How do researchers' typicality trajectories (T-Score selections across sequential checkpoints) evolve under exposure to checkpoint-governed agency, and what process-level patterns distinguish emerging inquirer profiles relative to the strategic-inquirer and exploratory-inquirer archetypes identified by Yang et al. (2025)?

- **RQ4 (new)**: Do the borrowed validated scales and the retained checkpoint-architectural indicators exhibit convergent validity in predicting learning outcomes and decision-quality markers, and where they diverge, what does that divergence reveal about the unique measurement affordances of checkpoint architectures?

---

## Revised Paper 2 Positioning (Team Consensus)

The methodological contribution of Paper 2 v4 is:

> **We integrate validated instruments from self-regulated learning, epistemic cognition, distributed cognition, and collaborative regulation traditions with two architectural indicators (Override Activation Rate, Epistemic Alternative Exposure) that measure phenomena with no established counterpart in pre-agentic AI literature. The resulting three-tier measurement battery is the first designed specifically for checkpoint-governed multi-agent AI in educational contexts and directly responds to Bigman, Briker, and Langer's (2026) call for human-AI interaction research to be embedded in psychological theory.**

This positioning:

- Satisfies the user's request to maximize borrowing from existing literature
- Preserves A2's coherence constraint (all borrowed scales come from SRL-compatible traditions)
- Retains distinctiveness through the two remaining invented indicators
- Addresses Bigman et al. (2026) by demonstrating psychological theory embedding
- Strengthens reader accessibility by using established academic vocabulary (self-regulated help-seeking, transactive memory, socially shared regulation of learning) alongside two renamed indicators (Override Activation Rate, Epistemic Alternative Exposure)
- Preserves the methodological contribution claim required for BJET Methodological Approaches strand

---

## Critical Uncertainties and Next Decisions

### Decisions the user must make before Paper 2 v4 drafting begins

1. **Accept A2's coherence constraint?** The team recommends accepting A2's rule that replacements come only from SRL, epistemic cognition, distributed cognition, and collaborative regulation traditions. This rules out Trust in Automation, algorithm aversion, and general HCI scales even though they are psychometrically strong. The user should confirm this constraint before locking the battery.

2. **Override Activation Rate as the primary retained novel indicator?** Both D4 (partial) and A2 (strong) endorse retention of GCA as the irreducible contribution. The user should confirm the renamed term is acceptable.

3. **Split CCI into architectural log metric + borrowed human-AI coregulation measure?** This resolves the D4/B1 vs A2 disagreement by preserving both claims. The user should confirm the split is acceptable, or choose one side.

4. **Add RQ4 on convergent validity?** A1 strongly recommends adding RQ4 to convert the borrowing decision into an empirical claim. The user should confirm.

5. **Karabenick help-seeking scale adaptation for PIR replacement?** The team recommends adapting Karabenick's self-regulated help-seeking items for the AI context. Alternative: use Amershi et al. (2014) mixed-initiative coding scheme directly, which is closer to the original PIR but comes from HCI rather than SRL. The user should choose.

6. **Do we need to pilot the SRL-adapted scales in the Instruments/ pipeline?** Since the borrowed scales will be adapted (item rewording for AI context, session-level vs course-level referent), the Instruments/ folder should be expanded to include draft adaptations of the four new borrowed scales plus the two renamed invented indicators. The Principal Investigator should review before pilot testing.

---

## Action Items

| Action | Owner | Target Date |
|---|---|---|
| Confirm A2's coherence constraint and accept or reject the trust-in-automation exclusion | Co-I + PI | 2026-04-11 |
| Confirm the two retained invented indicators (Override Activation Rate, Epistemic Alternative Exposure) by name | PI | 2026-04-11 |
| Confirm the CCI split (architectural log metric + borrowed human-AI coregulation) | PI | 2026-04-11 |
| Add the 5 new borrowed scales to the Instruments/ folder as draft adaptations | Co-I | 2026-04-13 |
| Verify Chinn et al. (2011) vs. later Chinn works for Epistemic Alternative Exposure theoretical grounding | Co-I | 2026-04-13 |
| Verify Hadwin, Jarvela, and Miller (2018) is the best SRL source for Human-AI Coregulation Depth; alternative Hadwin citations exist | Co-I | 2026-04-13 |
| Draft Paper 2 v4 with revised three-tier battery and four research questions | Co-I | 2026-04-20 |
| PI review of Paper 2 v4 draft | PI | 2026-04-24 |

---

## Reference Additions for Paper 2 v4

Based on the team deliberation, the following references should be added to Paper 2 v4 (beyond those already in v3):

- Amershi, S., Cakmak, M., Knox, W. B., & Kollar, T. (2014). Power to the people: The role of humans in interactive machine learning. *AI Magazine, 35*(4), 105-120.
- Bucinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW1), Article 188.
- Chinn, C. A., Buckland, L. A., & Samarapungavan, A. (2011). Expanding the dimensions of epistemic cognition: Arguments from philosophy and psychology. *Educational Psychologist, 46*(3), 141-167.
- Hadwin, A. F., Jarvela, S., & Miller, M. (2018). Self-regulation, co-regulation, and shared regulation in collaborative learning environments. In D. H. Schunk & J. A. Greene (Eds.), *Handbook of self-regulation of learning and performance* (2nd ed., pp. 83-106). Routledge.
- Hart, S. G., & Staveland, L. E. (1988). Development of NASA-TLX (Task Load Index): Results of empirical and theoretical research. *Advances in Psychology, 52*, 139-183.
- Horvitz, E. (1999). Principles of mixed-initiative user interfaces. In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems* (pp. 159-166). ACM.
- Karabenick, S. A., & Berger, J.-L. (2013). Help seeking as a self-regulated learning strategy. In H. Bembenutty, T. J. Cleary, & A. Kitsantas (Eds.), *Applications of self-regulated learning across diverse disciplines* (pp. 237-261). Information Age Publishing.
- Lewis, K. (2003). Measuring transactive memory systems in the field: Scale development and validation. *Journal of Applied Psychology, 88*(4), 587-604.
- Malone, T. W., & Crowston, K. (1994). The interdisciplinary study of coordination. *ACM Computing Surveys, 26*(1), 87-119.
- Ng, D. T. K., Leung, J. K. L., Chu, S. K. W., & Qiao, M. S. (2021). Conceptualizing AI literacy: An exploratory review. *Computers and Education: Artificial Intelligence, 2*, 100041.
- Thompson, J. D. (1967). *Organizations in action: Social science bases of administrative theory*. McGraw-Hill.
- Wegner, D. M. (1987). Transactive memory: A contemporary analysis of the group mind. In B. Mullen & G. R. Goethals (Eds.), *Theories of group behavior* (pp. 185-208). Springer-Verlag.

Total new references: 12. Combined with the existing Paper 2 v3 reference list, Paper 2 v4 will have approximately 36 references, within the typical range for a BJET methodology paper.
