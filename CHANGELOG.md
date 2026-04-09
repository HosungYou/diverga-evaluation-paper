# Changelog

All notable changes to the Diverga Evaluation Paper repository are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this repository follows a loose semantic versioning scheme for releases corresponding to major manuscript milestones.

---

## [0.4.0] - 2026-04-09

### Added

- **Paper 2 v3** (`Paper2_BJET_Methodological/Paper2_BJET_APA7_draft_v3.docx`) with Yang (2025) HALIE integration. CMAA reframed as an extension of Yang et al.'s (2025) HALIE application from standard generative AI to checkpoint-governed agentic AI, with two-tier measurement structure (Tier 1 HALIE-adapted metrics + Tier 2 CMAA indicators) foregrounded in the theoretical framework and methodology sections. Claude.ai baseline adopted, 2-day session split, partial Latin square counterbalancing. Agent count corrected from 24 to 29. Paper 3 cross-reference updated from ETR&D to Computers and Education: Artificial Intelligence.
- **Paper 3 v3** (`Paper3_Experimental/Paper3_CE_AI_APA7_draft_v3.docx`) with target journal changed from Educational Technology Research and Development to Computers and Education: Artificial Intelligence. Full multiple case study design with Activity Theory primary framework and HALIE/CMAA embedded as quantitative measurement stream. Independent performance evaluation protocol added following Yang et al. (2025) precedent. Yang (2025) Literature Review subsection added. References updated.
- **Instruments/ folder** containing six draft instrument adaptations for Principal Investigator review before pilot testing:
  - `01_self_efficacy_scale_draft.md`: Adapted 5-item AI self-efficacy scale (Avey et al., 2009 via Yang et al., 2025)
  - `02_engagement_composite_draft.md`: Adapted 8-item engagement composite (Skinner et al., 2009; Fredricks et al., 2004; Halverson & Graham, 2019 via Yang et al., 2025)
  - `03_performance_rubric_draft.md`: New 4-dimension research design quality rubric for independent performance evaluation
  - `04_dok_rubric_adapted.md`: Webb (2002) Depth of Knowledge rubric adapted for checkpoint selections
  - `05_prompt_relevance_rubric_adapted.md`: Yang et al. (2025, Appendix A) prompt relevance rubric adapted
  - `06_originality_rubric_adapted.md`: Yang et al. (2025, Appendix A) originality rubric adapted
- `Instruments/README.md` documenting the purpose, contents, and review process for all instrument adaptations.

### Changed

- Paper 2 and Paper 3 manuscripts now consistently reference the two-tier measurement structure and the shared Research Design IRB document in `Research_Design_IRB/`.
- Paper 2 abstract and introduction now position CMAA as an extension of Yang et al. (2025) HALIE application rather than as a standalone methodology.
- Paper 3 filename prefix changed from `Paper3_ETRnD` to `Paper3_CE_AI` to match the updated target journal.

### Deprecated

- `Paper2_BJET_Methodological/Paper2_BJET_APA7_draft_v2.docx` (retained for historical reference; superseded by v3)
- `Paper3_Experimental/Paper3_ETRnD_APA7_draft_v2.docx` (retained for historical reference; superseded by v3)

### Note on instrument finalization

The six instrument drafts in `Instruments/` are intended for Principal Investigator review before pilot testing. Pilot testing with two external methodologists will establish baseline inter-rater reliability (Cohen's kappa >= 0.70 target) before study artifacts are scored. Final instrument versions will be locked in the Open Science Framework pre-registration before data collection begins.

---

## [0.3.1] - 2026-04-09

### Changed

- **Paper 3 target journal finalized as Computers and Education: Artificial Intelligence (C&E:AI)**, replacing the earlier Computers & Education target. Rationale: C&E:AI is explicitly AI-focused, welcomes qualitative and case study methodology, has no minimum sample size norm, shares the publisher with Computers & Education, and was identified by the journal matching analysis as the highest-confidence venue for an N = 5 multiple case study of doctoral researchers' engagement with agentic AI.
- Research Design document updated throughout (abstract, Section 2.2 Paper 3 research questions, Section 9 Timeline, Section 10 Outstanding Items) to reflect the new target.
- Repository README, Research_Design_IRB README, and this CHANGELOG updated accordingly.

### Note on existing Paper 3 manuscripts

- Existing files in `Paper3_Experimental/` retain the ETR&D filenames and content from v0.2.0. These will be updated in the next release (v0.4.0) to reflect the C&E:AI target and the Yang (2025) HALIE integration introduced in v0.3.0.

---

## [0.3.0] - 2026-04-09

### Added

- **Research_Design_IRB/ folder** containing the unified research design document that supports the multi-site Institutional Review Board protocol for both Paper 2 (BJET methodology) and Paper 3 (Computers and Education: Artificial Intelligence empirical) from a single shared N = 5 dataset.
- `Research_Design_IRB/Research_Design_IRB_v1.docx` (APA 7 formatted, 9 tables, 19 references) specifying participants, recruitment, measurement, data collection, analysis plan, IRB protections, timeline, and outstanding items.
- `Research_Design_IRB/README.md` documenting the folder contents, key design decisions, and outstanding items.

### Measurement framework (new)

- **Two-tier measurement structure** introduced in Section 4.2 of the research design.
- **Tier 1** adapts four HALIE-based interaction metrics from Yang et al. (2025, BJET) Appendix A rubrics: prompt number, Depth of Knowledge (Webb, 2002), prompt relevance and evolution, and originality. Tier 1 also includes validated self-efficacy (Avey et al., 2009) and engagement composite (Skinner et al., 2009; Fredricks et al., 2004; Halverson & Graham, 2019) scales.
- **Tier 2** introduces five Checkpoint-Mediated Agency Analysis (CMAA) indicators specific to the Diverga checkpoint architecture: Proactive Intervention Rate, Decision Space Expansion, Governance Constraint Activation, State Utilization Depth, and Coordination Complexity Index.
- **HALIE dimension mapping** (Section 4.5, Table 4) structures both Tier 1 and Tier 2 indicators along the Targets, Perspectives, and Criteria dimensions from Lee et al. (2023), following Yang et al. (2025, Figure 3).

### Strategic reframing

- CMAA repositioned as an extension of Yang et al.'s (2025) HALIE application from standard generative AI to checkpoint-governed agentic AI, rather than as a standalone methodology. This strengthens continuity with prior BJET-published measurement work and the fit with the BJET Special Issue on Agentic AI in Education (SI-2026-000285).
- **Independent performance evaluation** by the Principal Investigator introduced following the bias mitigation precedent of Yang et al. (2025).
- **Anonymization** applied throughout for double-anonymous peer review: institutions referenced as Institution A and Institution B; authors as Principal Investigator and Co-Investigator.

### Design decisions confirmed

- Baseline condition set to **Claude.ai** (standard generative AI), not a no-AI condition, to preserve the answerability of Paper 2 RQ2.
- **Two-day session split** with concurrent think-aloud in Phases 0 and 2 and retrospective think-aloud via screen replay in Phases 3 and 4.
- **Partial Latin square counterbalancing** (3 participants receive Scenario A first, 2 receive Scenario B first), pre-registered on OSF.
- **Maximum-variation purposeful sampling** (N = 5) across four dimensions: AI knowledge level, methodology expertise, epistemological disposition, disciplinary identity.

### References added

- Avey, J. B., Luthans, F., & Jensen, S. M. (2009)
- Fredricks, J. A., Blumenfeld, P. C., & Paris, A. H. (2004)
- Halverson, L. R., & Graham, C. R. (2019)
- Lee, M., et al. (2023) [HALIE framework]
- Skinner, E. A., Kindermann, T. A., & Furrer, C. J. (2009)
- Webb, N. L. (2002)
- Yang, M., Jiang, S., Li, B., Herman, K., Luo, T., Moots, S. C., & Lovett, N. (2025) [BJET, 56(6), 1973-2000]

### Outstanding items

- Instrument adaptation and pilot testing (self-efficacy, engagement, performance rubric)
- First authorship decision for Paper 3
- Designation of neutral study coordinator
- SMART IRB reliance route confirmation
- Diverga instrumentation layer extensions (CMAA telemetry)
- Coordination with Yang et al. (2025) research team

---

## [0.2.0] - 2026-03-24

### Added

- **Paper 2 (BJET Methodological) manuscripts**: proposal draft v1 in Markdown and Word, APA 7 draft v2 in Word, conceptual framing document, and abstract draft.
- **Paper 3 (Experimental) manuscripts**: proposal draft v1 in Markdown and Word, APA 7 draft v2 in Word, experimental design v2, and interview purpose document.
- **Paper 1 (Design Case)**: IJDL proposal form draft, figures, and supporting materials.
- **DISCUSSION folder**: raw discussion logs, comparative analysis, and v11.0 architecture discussion.
- **You_Yang_2026_Research_Design_Draft.docx**: earlier research design draft (superseded in v0.3.0 by Research_Design_IRB).

### Infrastructure

- Three-paper folder structure established (Paper1_DesignCase, Paper2_BJET_Methodological, Paper3_Experimental).
- Supporting scripts folder added.

---

## [0.1.0] - 2026-03-10

### Added

- Initial repository structure
- `RESEARCH_PROPOSAL.md` (Korean, full research proposal)
- `README.md` with project overview
- Early v11.0 architecture discussion
- Comparative analysis of AI research tools

---

## Release Tag Scheme

- `v0.1.x` — Initial research proposal and discussion
- `v0.2.x` — Paper 2 and Paper 3 manuscript drafts
- `v0.3.x` — Research Design (For IRB) with Yang (2025) integration
- `v0.4.x` — (Planned) Paper 2 and Paper 3 manuscripts updated to reflect Yang (2025) integration
- `v0.5.x` — (Planned) OSF pre-registration and IRB submission
- `v1.0.0` — (Planned) Data collection complete; Paper 2 manuscript submitted to BJET
