# Research Design (For IRB)

Unified research design document supporting the multi-site Institutional Review Board (IRB) protocol for the Diverga evaluation study. This single document covers both Paper 2 (BJET methodology) and Paper 3 (Computers and Education: Artificial Intelligence empirical) because they share the same N = 5 within-subject dataset.

---

## Contents

| File | Description | Status |
|---|---|---|
| `Research_Design_IRB_v1.docx` | APA 7 formatted unified research design specifying participants, measurement, procedures, and IRB protections | v1, 2026-04-09 |

---

## Purpose

The document serves three overlapping functions:

1. **IRB protocol source text.** The sections on participants, recruitment, data collection, consent language, and risk mitigation are written as drop-in content for the institutional IRB application forms.
2. **Pre-registration source text.** The research questions, sampling criteria, measurement definitions, scenario assignment, and inference criteria are written to be copied directly into the Open Science Framework pre-registration template before data collection begins.
3. **Internal design specification.** The document records the rationale for every design decision (baseline choice, session split, sampling logic, measurement tier structure) so that both investigators and the neutral study coordinator share the same authoritative reference.

---

## Key Design Decisions

### Baseline condition

The baseline condition is **Claude.ai** (standard generative AI), not Google Doc with no AI. This decision was made to preserve the answerability of Paper 2 RQ2, which asks how agentic AI participation can be distinguished from standard generative AI assistance. A no-AI baseline would reduce the comparison to AI presence versus absence, which is not the research question and does not reflect the ecological reality of doctoral research practice in 2026.

### Session structure

Data collection uses a two-day within-subject split, with Day 1 covering the Claude baseline (Phase 0), Diverga orientation (Phase 1), and Diverga novel task (Phase 2), and Day 2 covering the Diverga re-design of the Phase 0 scenario (Phase 3) and the semi-structured interview (Phase 4). The inter-session gap of 1 to 7 days reduces rote recall of the Phase 0 design. Concurrent think-aloud is used in Phases 0 and 2; retrospective think-aloud via screen replay is used in Phases 3 and 4.

### Sampling

N = 5 doctoral students in social sciences, recruited using maximum-variation purposeful sampling across four dimensions (AI knowledge level, methodology expertise, epistemological disposition, disciplinary identity). Scenario counterbalancing uses a partial Latin square with 3 participants receiving Scenario A first and 2 receiving Scenario B first, pre-registered on the Open Science Framework before data collection.

### Measurement structure (two tiers)

**Tier 1** adapts four HALIE-based interaction metrics from Yang et al. (2025, BJET) Appendix A rubrics (prompt number, Depth of Knowledge, prompt relevance and evolution, originality) plus validated self-efficacy (Avey et al., 2009) and engagement (Skinner et al., 2009) scales. Tier 1 metrics apply to both the Claude and Diverga conditions, enabling direct contrast.

**Tier 2** introduces five Checkpoint-Mediated Agency Analysis (CMAA) indicators specific to the Diverga checkpoint architecture: Proactive Intervention Rate, Decision Space Expansion, Governance Constraint Activation, State Utilization Depth, and Coordination Complexity Index. Three indicators (PIR, DSE, GCA) yield between-condition contrasts under architectural assumptions; two (SUD, CCI) are reported as Diverga-only descriptors.

### Theoretical framing

Paper 2 anchors the CMAA extension in Floridi's (2025) three criteria for artificial agency (interactivity, bounded autonomy, adaptability) and positions the measurement approach as a direct extension of Yang et al.'s (2025) HALIE application from standard generative AI to checkpoint-governed agentic AI. Paper 3 uses cultural-historical activity theory (Engestrom, 1987) as its dominant analytic frame, with CMAA indicators treated as one quantitative data stream among several qualitative sources.

### Independent performance evaluation

The Principal Investigator, who did not develop Diverga, serves as an independent blind evaluator of research design quality using a four-dimension rubric (research question clarity, theoretical grounding, method-question alignment, ethical consideration). This follows the bias mitigation precedent of Yang et al. (2025), where one co-author conducted the performance evaluation specifically for research purposes. Inter-rater reliability is established during pilot with one external methodologist before study artifacts are scored.

---

## Relationship to Other Documents in the Repository

| Related path | Relationship |
|---|---|
| `Paper2_BJET_Methodological/` | Paper 2 manuscript drafts. Needs updating to reflect Yang (2025) HALIE integration and two-tier measurement structure. |
| `Paper3_Experimental/` | Paper 3 manuscript drafts. Target journal finalized as Computers and Education: Artificial Intelligence (C&E:AI) on 2026-04-09. Existing files in this folder still use the earlier ETR&D filenames and content; they will be updated in the next release to reflect the C&E:AI target and Yang (2025) HALIE integration. |
| `RESEARCH_PROPOSAL.md` | Earlier proposal in Korean. Superseded by this English research design for IRB purposes. |
| `You_Yang_2026_Research_Design_Draft.docx` | Earlier research design draft (Paper 1 design case). Different scope and purpose. Retained for historical reference. |

---

## Outstanding Items Requiring Confirmation

Six items must be resolved before IRB submission. These are listed in detail in Section 10 of the document:

1. Instrument adaptation and pilot testing for the adapted self-efficacy scale, engagement composite scale, and the four-dimension performance evaluation rubric.
2. First authorship decision for Paper 3, with the publication strategy recommending that the Principal Investigator serve as first author to strengthen credibility given the Co-Investigator's dual role.
3. Designation of a specific neutral study coordinator with no collaborative relationship with either investigator.
4. Confirmation that both institutions participate in SMART IRB for educational research protocols and designation of the reviewing institution.
5. Implementation of the Diverga instrumentation layer extensions (governance event logging, agent activation logging, automatic alternatives capture at checkpoints) before the June 2026 pilot sessions.
6. Coordination with the Yang et al. (2025) research team regarding the adapted rubrics and scale items to ensure consistency with the original published operationalization.

---

## Version History

| Version | Date | Key Changes |
|---|---|---|
| v1 | 2026-04-09 | Initial commit. APA 7 formatted. Yang et al. (2025) HALIE integration with two-tier measurement structure. Anonymized for double-anonymous peer review. |

---

## Citation

If referencing this design document in related manuscripts, cite as:

> Research Design (For IRB). (2026). Checkpoint-Mediated Agency Analysis and Its Application to Doctoral Researchers' Methodological Reasoning: A Multi-Site Design-Based Study. Internal document, Diverga Evaluation Paper repository. https://github.com/HosungYou/diverga-evaluation-paper/tree/main/Research_Design_IRB
