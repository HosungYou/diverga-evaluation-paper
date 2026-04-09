# Diverga Evaluation Paper

**Human Checkpoints as Epistemic Scaffolds: An Educational Design Research Study of AI-Mediated Research Methodology Assistance Using Diverga**

---

## Overview

This repository contains the research proposal, discussion logs, and supporting materials for the pilot evaluation study of [Diverga](https://github.com/HosungYou/Diverga) — a 24-agent AI research methodology assistant built on Verbalized Sampling (VS) methodology.

## Research Focus

- **Theoretical Framework:** Activity Theory (Engeström) + Educational Design Research (McKenney & Reeves)
- **Core Question:** How do Human Checkpoints function as epistemic scaffolds in AI-mediated research design?
- **Key Constructs:** Mode collapse prevention, automation bias mitigation, researcher decision autonomy

## Repository Structure

```
diverga-evaluation-paper/
├── README.md                           # This file
├── CHANGELOG.md                        # Version history
├── RESEARCH_PROPOSAL.md                # Earlier research proposal (Korean)
├── Research_Design_IRB/                # Unified IRB research design (v1, 2026-04-09)
│   ├── README.md                       # Design overview and key decisions
│   └── Research_Design_IRB_v1.docx     # APA 7 document covering Paper 2 + Paper 3 shared protocol
├── Paper1_DesignCase/                  # Paper 1: Design case for IJDL
├── Paper2_BJET_Methodological/         # Paper 2: Methodology paper for BJET Special Issue
│   ├── Paper2_BJET_APA7_draft_v2.docx  # v2 (historical; no HALIE integration)
│   └── Paper2_BJET_APA7_draft_v3.docx  # v3 with Yang (2025) HALIE integration
├── Paper3_Experimental/                # Paper 3: Empirical study for Computers and Education: Artificial Intelligence
│   ├── Paper3_ETRnD_APA7_draft_v2.docx # v2 (historical; ETR&D target, no HALIE)
│   └── Paper3_CE_AI_APA7_draft_v3.docx # v3 with C&E:AI target + Yang (2025) HALIE integration
├── Instruments/                        # Draft adaptations of measurement instruments
│   ├── README.md
│   ├── 01_self_efficacy_scale_draft.md
│   ├── 02_engagement_composite_draft.md
│   ├── 03_performance_rubric_draft.md
│   ├── 04_dok_rubric_adapted.md
│   ├── 05_prompt_relevance_rubric_adapted.md
│   └── 06_originality_rubric_adapted.md
├── DISCUSSION/                         # Raw discussion and review logs
└── scripts/                            # Supporting analysis scripts
```

## Three-Paper Publication Strategy

| Paper | Type | Target Journal | Status |
|---|---|---|---|
| Paper 1 | Design case | International Journal of Designs for Learning (IJDL) | Draft submitted via IJDL_Proposal_Form |
| Paper 2 | Methodology | British Journal of Educational Technology, Special Issue on Agentic AI in Education (SI-2026-000285) | Draft v2 (APA 7); IRB pending |
| Paper 3 | Empirical | Computers and Education: Artificial Intelligence | Draft v2 (APA 7); IRB pending |

Papers 2 and 3 share a single N = 5 within-subject dataset collected under the protocol in `Research_Design_IRB/`. The partition between them is by unit of analysis (indicator-centric vs case-centric), not by data subset.

## Key References

- Verbalized Sampling: [arXiv:2510.01171](https://arxiv.org/abs/2510.01171)
- Diverga: [GitHub](https://github.com/HosungYou/Diverga)
- Conjecture Mapping: [Sandoval, 2014](https://doi.org/10.1080/10508406.2013.778204)

## Status

- [x] Initial research design discussion
- [x] Comparative analysis of AI research tools
- [x] Research proposal draft
- [x] v11.0 architecture discussion (consolidation, VS Arena, checkpoint design)
- [x] Paper 2 (BJET) and Paper 3 (C&E) proposal drafts v1
- [x] Paper 2 and Paper 3 APA 7 drafts v2
- [x] Research Design (For IRB) v1 with Yang et al. (2025) HALIE integration
- [ ] Instrument adaptation and pilot testing (self-efficacy, engagement, performance rubric)
- [ ] Diverga instrumentation layer extensions (CMAA telemetry)
- [ ] OSF pre-registration
- [ ] IRB submission (SMART IRB multi-site reliance)
- [ ] Pilot sessions
- [ ] Main data collection
- [ ] Paper 2 BJET submission (abstract 2026-08-01; full manuscript 2026-10-28)
- [ ] Paper 3 Computers and Education: Artificial Intelligence submission (December 2026)

## License

MIT
