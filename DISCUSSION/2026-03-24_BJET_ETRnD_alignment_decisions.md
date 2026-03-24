# 2026-03-24: BJET / ETR&D Alignment Decision Log

**Session type:** Solo research planning (Hosung You)
**Purpose:** Align Paper 2 (BJET SI-2026-000285) and Paper 3 (journal redirect to ETR&D) to target journal requirements; finalize task scenarios; document development story conversion rules
**Status:** Decisions finalized; implementation in progress

---

## 1. BJET CFP Analysis Results

### 1.1 CFP Confirmed Details

- **Special Issue title:** "Agentic AI in Education: Artificial Agency and the Social-Cognitive Dynamics of Learning"
- **Guest Editors:** Lixiang Yan (Tsinghua), Yizhou Fan (Peking University), Yueqiao Jin (Monash), Nancy Law (HKU), Yu Zhang (Tsinghua), Xibin Han (Tsinghua)
- **Paper 2 target track:** Theme 7 — "Methodological contributions that advance the measurement of artificial agency and its effects, including multimodal analyses, process-level modelling, and designs that distinguish agentic participation from tool-based assistance"
- **CFP theoretical anchor:** Floridi (2025) three criteria — interactivity, bounded autonomy, adaptability
- **Accepted paper types:** Empirical (experimental, longitudinal, design-based, multimodal) AND conceptually grounded papers that "build directly on empirical findings"
- **Word limit:** ~6,000 words (references excluded)
- **Abstract deadline:** 2026-08-01
- **Full manuscript deadline:** 2026-10-28
- **Final acceptance:** 2027-03-15 | **Publication:** 2027-05

### 1.2 BJET Alignment Gap Analysis

| Requirement | Current Paper 2 Status | Action Required |
|---|---|---|
| Floridi (2025) as primary framework | ✅ Present and detailed | — |
| "Social-cognitive dynamics" language | ❌ Absent | Add to Introduction and Discussion |
| "Epistemic labour redistribution" framing | ❌ Absent | Link DSE indicator explicitly |
| "Initiative and persistence" (beyond bounded autonomy) | ❌ Weak | Strengthen in §1.2 Positioning table |
| "Shared regulation" at checkpoints | ❌ Absent | Add to CMAA Framework §3 |
| "Path-dependent steering of inquiry" | ❌ Partial (Audit Trail mentioned) | Link to Typicality Trajectory analysis |
| Design-based empirical grounding | ⚠️ "Proof-of-concept planned" framing | Reframe: Diverga dev cycles as design-based evidence |
| Structured abstract (aims/context/data/outcomes) | ✅ Present, ~248 words | Minor language updates (add "social-cognitive dynamics") |
| ~6,000 word limit | ❌ Likely over if all sections written | Compress §5 Proposed Study; cut §1 to 900 words |
| Double-anonymous (no author names in manuscript) | ⚠️ Not yet prepared | Remove before submission |
| Non-anthropomorphic AI language | ✅ Present | — |
| International relevance | ✅ Present | — |

### 1.3 Development Story → BJET Formal Language Conversion Rules

**Principle:** Diverga's development history constitutes design-based empirical evidence — NOT personal narrative. Frame as "systematic analysis of n=5 iterative design cycles (n=224 commits, 57 days)."

**Rule: Never use 1st person narrative for development events in BJET.**

| Paper 1 / Internal narrative style | BJET-appropriate formal language |
|---|---|
| "Sisyphus Protocol 도입 후 같은 날 철회" | "An autonomous operation mode introduced during Cycle 2 was removed within 24 hours upon identification of a critical design tension: unrestricted agent initiative without checkpoint-mediated boundaries eliminates the epistemic labour redistribution that constitutes the core educational value of artificial agency." |
| "체크포인트가 자동 승인되는 버그 발견 (v11.0)" | "System audit logs from v11.0 revealed that architecturally designated REQUIRED checkpoints were programmatically bypassed, generating approval tokens without user engagement — operationalising the measurement problem that CMAA addresses: architecturally claimed oversight may diverge substantially from actual epistemic participation." |
| "44개에서 24개 에이전트로 통합" | "Through five iterative design cycles (n=224 commits, 57 days), agent proliferation from 44 to 24 was driven by epistemic boundary analysis — consolidating agents whose operational domains overlapped to ensure each checkpoint represented a distinguishable and irreducible decision juncture." |
| "VS Arena 5개 페르소나 설계" | "The system's five paradigm-specific evaluation personas (Post-Positivist, Critical Theorist, Pragmatist, Interpretivist, Transformative) operationalize adaptability by enabling the system to adopt fundamentally different epistemological stances at the researcher's directive." |

---

## 2. Task Scenario Decisions

### 2.1 Scenario A (Unchanged)

> "The impact of AI tools on K-12 student academic achievement"

**Rationale:** Well-suited for mode collapse detection — LLMs immediately and consistently recommend Davis (1989) TAM or UTAUT variants. VS T-Score diversity contrast is maximally observable against this baseline.

### 2.2 Scenario B (Replaced)

**Previous:** "The impact of AI-based collaboration tools on team creativity in remote work"

**Problem:** Requires HRD/organizational psychology domain knowledge foreign to most social science education doctoral students; the modal framework trap (organizational creativity theory) is unfamiliar to the target participant population, reducing ecological validity.

**Replacement:**
> "What factors shape academic socialization and research identity formation among first-generation doctoral students from racially underrepresented groups in STEM fields?"

**Rationale:**
- Familiar domain for social science education doctoral students
- Clear, observable modal framework trap: ChatGPT → Bandura's Social Cognitive Theory or Bronfenbrenner's ecological model (predictable, T > 0.8)
- Rich VS-generatable alternatives: Yosso's Cultural Wealth Model, Communities of Practice (Wenger, 1998), Critical Race Theory applied to higher education, intersectionality frameworks, TrioEd/TRIO-informed models
- Counterbalances Scenario A well: A is quantitative-leaning (achievement outcomes, TAM-typical), B is qualitative-leaning (identity, socialization) — minimizes transfer effect while preserving task difficulty equivalence
- Sufficient disciplinary breadth and international relevance for BJET audience

**Files to update:** `Paper3_Experimental/experimental_design_v2.md` Phase 2 task description, Phase 3 cross-reference

---

## 3. Paper 3 Journal Change Decision

### 3.1 Decision

| | Previous Target | New Target |
|---|---|---|
| **Journal** | Computers & Education (C&E) | Educational Technology Research and Development (ETR&D) |
| **Impact Factor** | 11.5 | 4.8 |
| **Acceptance strategy** | High IF, high competition, N=5 risky | Design-based focus, N=5 acceptable, first application of CMAA |

### 3.2 Rationale

| Factor | C&E | ETR&D |
|---|---|---|
| Typical N (mixed methods) | 30–100 | 10–20 |
| Design-based research | Possible but rare | Core genre |
| Design Principles section | Optional | Required/expected |
| Phase 1 + Phase 2 structure | Not standard | Standard |
| N=5 intensive case study | High rejection risk | Appropriate |
| Pre-data design papers | Requires data | Design-sharing accepted |
| CMAA first empirical application | Hard to justify without larger N | Natural fit for "design + evaluate" track |

### 3.3 Framing for Dr. Yang

> "ETR&D was identified as the more appropriate target journal given the design-based research nature of the study and the small-N intensive methodology. The study's design phase (Diverga's 5 EDR cycles) and evaluation phase (N=5 empirical study) map directly onto ETR&D's core publication track. C&E remains a target if the study expands to N=20+ in future iterations."

### 3.4 ETR&D-Specific Requirements Added to Paper 3

| Requirement | Status |
|---|---|
| 150–250 word abstract (non-structured) | To be written |
| Separate Literature Review section | To be added |
| Design Principles section (4–6 principles) | Preliminary principles drafted; empirical refinement pending |
| Practical implications | To be added to Discussion |
| ~8,000 word limit | Adequate — current content ~4,000; expansion needed |

---

## 4. Figures Plan

### Paper 2 (BJET) — New figures specific to Paper 2

| Figure | Description | File |
|---|---|---|
| Figure 1 | CMAA Conceptual Framework: Floridi 3 criteria → Diverga architecture → CMAA 5 indicators | `Paper2_BJET_Methodological/figures/figure1_cmaa_framework.png` |
| Figure 2 | Checkpoint Interaction as Natural Measurement Instrument: Single checkpoint → data packet elements | `Paper2_BJET_Methodological/figures/figure2_checkpoint_data_packet.png` |

### Paper 3 (ETR&D) — New figures specific to Paper 3

| Figure | Description | File |
|---|---|---|
| Figure 3 | Study Session Protocol: Phase 0–4 timeline with data sources labeled | `Paper3_Experimental/figures/figure3_study_protocol.png` |
| Figure 4 | Mixed Methods Data Integration: QUAN + QUAL strands → joint display → meta-inference | `Paper3_Experimental/figures/figure4_data_integration.png` |

---

## 5. Action Items

- [x] CFP alignment gap analysis complete
- [x] Task Scenario B replacement confirmed and rationale documented
- [x] Paper 3 journal change to ETR&D confirmed and rationale documented
- [x] Development story → BJET conversion rules documented
- [x] Figure 1: CMAA Framework (Paper 2) — `figures/figure1_cmaa_framework.png` generated
- [x] Figure 2: Checkpoint Data Packet (Paper 2) — `figures/figure2_checkpoint_data_packet.png` generated
- [x] Figure 3: Study Protocol (Paper 3) — `figures/figure3_study_protocol.png` generated
- [x] Figure 4: Data Integration (Paper 3) — `figures/figure4_data_integration.png` generated
- [x] Paper 2: `paper2_proposal_draft_v1.md` — 60% completeness, proposal feel
- [x] Paper 3: `paper3_etrd_proposal_draft_v1.md` — 60% completeness, ETR&D target
- [x] Update `experimental_design_v2.md` Scenario B text
- [ ] Agent Teams review (via /diverga agent teams) — in progress
- [ ] Commit & push all files to GitHub
- [ ] Share with Dr. Yang after agent review

---

## 6. Relationship Between Papers (Confirmed)

| Paper | Journal | Role | Status |
|---|---|---|---|
| Paper 1 | IJDL | Design case narrative (1st person, EDR story) | Outline + draft complete |
| Paper 2 | BJET SI-2026-000285 | CMAA methodology proposal (formal, design-based) | Proposal draft v1 in progress |
| Paper 3 | ETR&D | Empirical application of CMAA, N=5 case study | Proposal draft v1 in progress |

**Dependency chain:** Paper 1 (design story) → Paper 2 (method framework) → Paper 3 (empirical application)

Paper 2 is readable independently; Paper 3 references Paper 2 for CMAA. Paper 1 provides narrative context that Papers 2/3 render in formal academic language.
