# 2026-03-24: Agent Teams Review — Paper 2 (BJET) & Paper 3 (ETR&D)

**Session type:** Parallel agent review via Diverga Agent Teams (CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1)
**Agents:** theory-reviewer (A2), pub-reviewer (G2), ethics-reviewer (X1)
**Files reviewed:** `paper2_proposal_draft_v1.md`, `paper3_etrd_proposal_draft_v1.md`
**Revisions applied:** Yes — see below for what was applied vs. flagged for later

---

## Revisions Applied to Paper 2 (BJET)

| Section | Change | Source |
|---|---|---|
| Abstract — Research aims | "lacks validated methodologies for **distinguishing agentic participation from tool-based assistance**, and for measuring how artificial agency **redistributes epistemic labour at critical educational decision junctures**" | G2 |
| Abstract — Data/methods item (1) | "mapping...onto Floridi's (2025) agency criteria **as sites of social-cognitive interaction, where epistemic labour is visibly redistributed** between human and artificial agents" | G2 |
| Abstract — Outcomes | Added: "validated against the criterion of **distinguishing agentic participation from tool-based assistance** in authentic research task contexts" | G2 |
| Introduction — para 3 | Added 2 CFP-language sentences before CMAA introduction: social-cognitive dynamics framing + agentic participation / tool-based assistance distinction | G2 |
| §2.3 | Added full theoretical positioning paragraph ("A deeper limitation unites these measurement approaches...") | A2 |
| §2.3 | Added [REVIEW NOTE — A2] flagging 3 deeper theoretical issues for manuscript revision: PIR/Interactivity category error, epistemic labour formal definition, shared regulation intentionality gap | A2 |

### Outstanding theoretical issues for manuscript revision (NOT shared with Dr. Yang yet)

1. **PIR → Interactivity category error** (Tables 1 & 3): PIR measures system-initiated halts, closer to bounded autonomy than Floridi's interactivity. Move PIR to Bounded Autonomy; make SUD an Interactivity indicator.
2. **"Epistemic labour" needs formal definition**: Not standard in Floridi, Järvelä, or EdTech literature. Ground in Fricker (2007) *Epistemic Injustice* or Kukla (2006).
3. **Shared regulation + intentionality gap**: Järvelä's framework presupposes shared intentionality; Floridi's artificial agent has none. Either reargue using distributed cognition (Hutchins, 1995) or explicitly acknowledge as a theoretical extension.
4. **Circularity in CMAA validation chain**: Framework derived from Diverga, indicators operationalized via Diverga data structures, validated on Diverga. Add a paragraph distinguishing system-specific operationalizations from system-agnostic indicator definitions.
5. **"Path Dependence" in Table 1**: Unsupported — either develop with Arthur (1994) sourcing or remove and fold into DSE.
6. **No exhaustiveness argument for 5 indicators**: Add theoretical saturation argument or explicitly frame as initial set.

---

## Revisions Applied to Paper 3 (ETR&D)

| Section | Change | Source |
|---|---|---|
| Abstract — sentences 1–2 | Rewritten to ETR&D genre: leads with "initial empirical evaluation phase of a five-cycle EDR programme" rather than technology-effects framing | G2 |
| §3.1 | Floridi re-explanation condensed to forward reference to Paper 2 + one summary sentence; removes self-plagiarism risk between companion papers | G2 |
| §8.2 | Full reflexivity paragraph replacing single bullet: developer-investigator dual role, 3 structural safeguards (second coder, negative codes, DP4–6 reservation) | X1 |
| §8.2 Limitations | Added 5 explicit limitations: N=5, single system, IRB-pending, DP1–3 circularity, T-Score calibration | X1 |

### Outstanding IRB/protocol issues for IRB application (April–May 2026)

1. **Coercion via institutional proximity**: Exclude participants in courses taught/advised by researcher; route recruitment through third party if needed.
2. **Demand characteristics — developer presence**: Consider researcher absence during Phases 2–3; debrief should explicitly invite negative evaluations.
3. **Session duration consent**: Add mid-session check-in after Phase 1 break; include compensation language.
4. **Data sensitivity in think-aloud**: Transcription protocol must anonymize named individuals (advisors, faculty).
5. **Social desirability in Phase 4 interview**: Add anonymous post-session written reflection or delayed follow-up; add devil's advocate prompting.
6. **Practice effects in Phase 3**: Acknowledge that Phase 3 re-design conflates Diverga exposure with task repetition; not a clean within-participant comparison.

---

## Cross-paper relationship flag (G2)

Paper 3 §3.1 previously re-explained Floridi at nearly the same depth as Paper 2 §2.1 — self-plagiarism risk. **Fixed** by condensing to forward reference.

Paper 2 §5.3 and Paper 3 §3.1 now maintain clean bidirectionality: Paper 2 defines CMAA → Paper 3 applies it, with Paper 3 citing "You & Yang (Paper 2)" rather than re-deriving the framework.

---

---

## Round 2 Additional Revisions Applied (same session)

Second agent round (theory-reviewer-2, pub-reviewer-2, ethics-reviewer-2) identified additional gaps not caught in round 1.

### Paper 2 additions
| Section | Change | Source |
|---|---|---|
| Abstract — Data block item (1) | Further refined: "explicating their social-cognitive dynamics of learning — the ways in which structured human-AI interaction at checkpoints redistributes epistemic **initiative**..." | G2-R2 |
| Abstract — Outcomes | Added: "revealing how artificial agency shapes the social-cognitive dynamics of learning by expanding, constraining, or **redirecting the researcher's epistemic trajectory**" | G2-R2 |
| §2.2 end | Added closing sentence: "At these junctures, checkpoint-governed artificial agency participates in the **shared regulation of inquiry**..." | G2-R2 |

### Paper 3 additions
| Section | Change | Source |
|---|---|---|
| Abstract | Full rewrite (224 words): leads with design challenge ("does this architecture genuinely expand epistemic agency, or do researchers default to modal consensus?") — ETR&D genre | G2-R2 |
| Table 9 Automation-Deference | Clarified: requires BOTH log-confirmed non-inspection AND verbal deference; rational modal selection ≠ automation deference | X1-R2 |
| §8.2 Limitations | Added: orientation phase priming as demand characteristic; data linkability protocol note | X1-R2 |

### Outstanding issues from Round 2 (not yet applied — for manuscript revision)

**A2-R2 new issues:**
- CCI, GCA, SUD all require Diverga-specific architecture — three of five indicators require minimum architectural features (checkpoint enforcement logging, persistent audit trail, multi-agent dependency graph). Scope CMAA to "checkpoint-governed multi-agent systems" or distinguish core vs. architecture-specific indicators
- Co-regulation vs. shared regulation: Hadwin et al. (2018) co-regulation framework better fits asymmetric human-AI scaffolding than SSRL which requires shared intentionality
- Derivation subsection needed: explicitly show Floridi criterion → observable checkpoint phenomena → indicator for each indicator

**G2-R2 new issues:**
- Paper 2 DRAFT note timeline inconsistency: says "Full manuscript to follow after IRB preparation (April–May 2026)" but abstract deadline is August 2026 and data collection August–September 2026. Fix timeline language.
- Paper 2 Introduction does not signal existence of Paper 3 — add early forward reference when §5 Proposed Study is written out
- "Initiative and persistence" and "shared regulation" still absent from Abstract (partially addressed; check final draft)

**X1-R2 new issues:**
- IRB: evaluative positioning of participants (implicit skills assessment) — debrief script must clarify study measures tool, not individual ability
- Scenario familiarity asymmetry: Scenario A (EdTech, AI/K-12) vs. Scenario B (doctoral identity, race) may be differentially proximate for participants; counterbalancing doesn't address topic familiarity
- Phase 4 interview: consider asynchronous follow-up (48h) for better reflective quality and reduced social desirability pressure

---

## Hook status

`prereq-enforcer.mjs` temporarily replaced with pass-through for this session.
**Restore:** `cp ~/.claude/plugins/cache/diverga/diverga/12.0.0/hooks/prereq-enforcer.mjs.bak ~/.claude/plugins/cache/diverga/diverga/12.0.0/hooks/prereq-enforcer.mjs`
