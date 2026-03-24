# Paper 1: Design Case Outline

**For discussion with Dr. Mohan Yang**
**Prepared by: Hosung You**
**Date: 2026-03-21**

---

## 1. Proposed Title Options

1. **"Designing a Multi-Agent AI Research Methodology Assistant: A Design Case of Diverga"**
   - Straightforward, follows IJDL conventions. Foregrounds the artifact and the genre.

2. **"From 44 Agents to 24: Design Decisions in Building an AI-Mediated Research Scaffolding System"**
   - Highlights the iterative design story and the consolidation as a central narrative arc. More evocative for readers browsing the table of contents.

3. **"Scaffolding Without Replacing: A Design Case of Human Checkpoints and Verbalized Sampling in AI-Assisted Research Design"**
   - Foregrounds the core design tension (scaffold vs. replace) and names the two key mechanisms. Slightly longer, but conveys the conceptual contribution immediately.

---

## 2. Target Journal Rationale

### Option A: IJDL (International Journal of Designs for Learning) -- Recommended

| Factor | Assessment |
|---|---|
| **Genre fit** | IJDL is the premier venue for design cases in learning design. The journal explicitly invites "descriptions of artifacts, environments and experiences created to promote and support learning." Diverga fits perfectly. |
| **Dr. Yang's track record** | Two published design cases in IJDL/adjacent venues: "Authentic learning design failures" (IJDL, 2023) and "Designing for accessibility in online learning" (IJDL/JPED, 2023). This establishes credibility and familiarity with reviewer expectations. |
| **Theoretical burden** | IJDL design cases prioritize the design story over heavy theoretical framing. This aligns with the March 21 meeting decision that Paper 1 does not need extensive theory. |
| **Multimedia support** | IJDL encourages screenshots, diagrams, design progression visuals, and even embedded media. This suits our evidence base (architecture diagrams, checkpoint flow screenshots, prompt examples). |
| **Review timeline** | IJDL is a smaller journal with relatively fast turnaround, allowing Paper 1 to be published or under review before Papers 2 and 3 are submitted. |
| **Open access** | IJDL is fully open access (hosted by Indiana University Libraries), maximizing visibility. |

### Option B: Advances in Developing Human Resources

| Factor | Assessment |
|---|---|
| **Audience** | HRD practitioners and scholars; less directly aligned with our research methodology education focus. |
| **Design case section** | The journal has a non-refereed "special feature" section (3,000 words max) for case studies. This is substantially shorter than what our design story requires and is not peer-reviewed. |
| **Fit limitation** | Diverga's primary context is graduate research methodology education, not organizational HR development. The connection is possible but requires framing gymnastics. |
| **Word limit** | Refereed articles allow up to 8,000 words (including everything), which is workable but tight for a richly illustrated design case. |

### Recommendation

**IJDL is the stronger fit.** The journal's mission, genre conventions, Dr. Yang's publication history, and the multimedia-friendly format all align with what Paper 1 needs to be. Advances in Developing HR could work for a practitioner-oriented companion piece in the future, but Paper 1 belongs in IJDL.

---

## 3. Paper Structure: Section-by-Section Outline

The structure below follows IJDL design case conventions (Boling, 2010; Howard et al., 2012) while incorporating the EDR framing from our meeting.

### Section 1: Introduction (approx. 800 words)

- **The problem space:** AI research tools are proliferating, but they converge on predictable recommendations (mode collapse) and encourage uncritical acceptance (automation bias).
- **The design challenge:** Can an AI research assistant be designed to scaffold methodological reasoning rather than replace it?
- **Scope statement:** This paper documents the design process, decisions, and rationale behind Diverga, a 24-agent AI research methodology assistant. It does not report empirical evaluation data (that is Paper 3); it tells the design story.
- **EDR positioning:** Situate this design case within the Analysis/Exploration and Design/Construction phases of the McKenney & Reeves (2012) EDR model. The design case captures what was learned during these phases; Papers 2 and 3 will address Evaluation/Reflection and the dual outcomes (maturing intervention, theoretical understanding).

### Section 2: Design Context (approx. 600 words)

- **Who is the designer:** Hosung You, doctoral student at Penn State, simultaneously the developer and researcher (acknowledge the dual role and its implications).
- **Target users:** Social science doctoral students engaged in research design.
- **Institutional context:** Graduate research methods education in U.S. universities; the gap between methods courses and actual research design practice.
- **Technical context:** Model Context Protocol (MCP), Claude Code infrastructure, the multi-agent architecture landscape circa 2025-2026.

### Section 3: The Design Problem in Detail (approx. 1,000 words)

- **Mode collapse:** Explain the phenomenon with concrete examples (e.g., "When asked for a theoretical framework for technology adoption, ChatGPT recommends TAM in approximately 80% of cases"). Cite arXiv:2510.01171.
- **Automation bias in research:** 78% uncritical acceptance rate (Springer Nature, 2025); negative correlation with critical thinking (Microsoft Research, 2025).
- **Existing tool landscape:** Brief comparison with Elicit, Consensus, SciSpace, and general-purpose tools (ChatGPT, Claude). What they do well, what they miss.
- **The gap:** No existing tool combines structured human oversight with diversity-generating mechanisms for research methodology guidance.

### Section 4: Design Decisions and Rationale (approx. 3,000-3,500 words)

This is the core of the design case. Organize by design decision, not chronologically. Each subsection follows the pattern: **decision point, alternatives considered, rationale for chosen approach, evidence of implementation**.

#### 4.1 Multi-Agent Architecture (Why 24 Agents, Not 1?)

- Decision: Domain-specialized multi-agent system vs. single general-purpose agent.
- Alternatives: Single-agent with diverse prompting; modular tool-use agent (like Obra/Cline); full 44-agent system (v10).
- Rationale: Brooks' subsumption architecture principle; "more agents is less" scaling research (Li et al., 2025); Together AI's Mixture of Agents findings.
- **The v10-to-v11 consolidation story:** From 44 to 24 agents. Which agents were merged and why. Usage pattern analysis, functional overlap assessment, cognitive load reduction.
- Evidence: Architecture diagrams (before/after), agent category map, ownership boundary definitions.

#### 4.2 Verbalized Sampling and T-Score (How to Counter Mode Collapse?)

- Decision: Implement Verbalized Sampling with explicit typicality scoring.
- Alternatives: Standard prompting with "be diverse" instructions; retrieval-augmented generation from a curated methodology database; random sampling with filtering.
- Rationale: VS research (Zhao et al., 2024) showing typicality awareness reduces mode collapse.
- T-Score design: Why show typicality to the researcher (transparency, informed choice) rather than using it only internally.
- Evidence: Example prompt-response pairs showing VS output with T-Scores; comparison of with/without VS diversity.

#### 4.3 Human Checkpoint System (Where Does the Human Stay in the Loop?)

- Decision: Structured, REQUIRED checkpoints at specific decision points.
- Alternatives: No checkpoints (full autonomy); optional checkpoints (soft suggestions); checkpoints at every step (maximum oversight).
- Rationale: Cognitive forcing functions (Bucinca et al., 2021); checkpoint fatigue considerations; the v11.1 reduction from many REQUIRED to 5 REQUIRED checkpoints.
- **The checkpoint bug story:** The v11.0 bug where checkpoints always returned `{continue: true}`. What this reveals about the difficulty of implementing genuine human oversight in autonomous systems.
- Evidence: Checkpoint flow diagrams; YAML configuration examples; the SQLite fix.

#### 4.4 VS Arena Design (Simulated vs. Genuine Diversity)

- Decision: Multiple epistemological persona agents with constraint-based differentiation.
- Alternatives: Single-agent VS (simulated diversity); positive persona framing ("think like a critical theorist"); pure random variation.
- Rationale: Persona drift research (Chen et al., 2025); the `cannotRecommend` constraint mechanism as structural enforcement.
- The five epistemological personas: post-positivist, critical theorist, pragmatist, interpretivist, transformative.
- Evidence: Persona configuration examples; `cannotRecommend` arrays; perspective-taking instructions.

#### 4.5 Decision Audit Trail (How to Externalize Reasoning?)

- Decision: YAML-based decision log capturing researcher choices at each checkpoint.
- Alternatives: No logging; free-text reflection prompts; structured questionnaires at each step.
- Rationale: Metacognition support; research data generation; accountability.
- Evidence: Sample decision-log.yaml entries.

### Section 5: Design Tensions (approx. 800 words)

Frame these as inherent, unresolved tensions rather than problems solved. This gives the design case intellectual depth without requiring empirical evidence.

1. **Simplicity vs. Specialization:** 24 agents organized in 9 categories is still complex compared to ChatGPT. The consolidation from 44 was a move toward simplicity, but Diverga remains a specialized tool with a learning curve.
2. **Diversity vs. Coherence:** The VS Arena maximizes methodological diversity, but diverse suggestions without synthesis can overwhelm novice researchers. No CSO (Chief Scientific Officer) agent exists yet to arbitrate.
3. **Autonomy vs. Oversight:** Every checkpoint interrupts flow and adds cognitive load. Five REQUIRED checkpoints is a judgment call, not a proven optimum.
4. **Designer-as-Researcher:** The developer is also the evaluator. This design case is partly an exercise in making tacit design knowledge explicit so that an external perspective (Dr. Yang) can interrogate it.

### Section 6: Design Resources and Artifacts (approx. 500 words + visuals)

A curated presentation of design evidence, following IJDL's emphasis on multimedia:

- System architecture diagram (9 categories, 24 agents)
- Checkpoint flow diagram (showing REQUIRED vs. RECOMMENDED gates)
- VS Arena persona configuration (annotated YAML)
- Sample user interaction screenshot (checkpoint in action)
- T-Score display example
- Decision audit trail sample
- Before/after architecture comparison (v10 vs. v11)

### Section 7: Reflection and Future Directions (approx. 500 words)

- What the design process revealed about AI tool design for education.
- How this design case connects to the EDR model: the Evaluation/Reflection phase and empirical testing are Papers 2 and 3.
- Invitation for the field: design principles that other AI tool developers can adapt.
- The open question of whether structural diversity (VS Arena) outperforms instructional diversity (single-agent prompting) remains empirical; this design case articulates the hypothesis, not the answer.

### References

---

## 4. Evidence and Artifacts to Include

| Evidence Type | Specific Items | Status |
|---|---|---|
| **Architecture diagrams** | v10 (44-agent) vs. v11 (24-agent) category maps | Needs creation or extraction from existing docs |
| **Agent consolidation table** | Which agents merged, rationale for each | Available in v11 architecture discussion |
| **Checkpoint flow diagrams** | REQUIRED vs. RECOMMENDED gates, prerequisite chains | Needs creation |
| **Checkpoint bug documentation** | The `{continue: true}` bug, SQLite fix | Available in v11 architecture discussion |
| **VS prompt examples** | Before/after VS, with T-Scores | Needs creation from actual Diverga runs |
| **VS Arena persona configs** | `cannotRecommend` arrays, epistemological commitments | Needs extraction from YAML configs |
| **Screenshot: checkpoint interaction** | User encountering a REQUIRED checkpoint | Needs capture |
| **Screenshot: T-Score display** | How typicality scores appear to the user | Needs capture |
| **Decision audit trail sample** | decision-log.yaml excerpt | Needs capture from actual run |
| **Git commit history** | Key commits showing design evolution | Available from Diverga repo |
| **Design comparison table** | Diverga vs. Elicit vs. Consensus vs. ChatGPT | Available in brainstorming doc |

---

## 5. Role Distribution Suggestion

| Task | Lead | Support | Notes |
|---|---|---|---|
| **Design case structure and framing** | Yang | You | Dr. Yang's IJDL experience guides the narrative structure |
| **Design rationale documentation** | You | Yang | Hosung holds the tacit design knowledge; Dr. Yang's role is to interrogate and challenge it |
| **Architecture and technical descriptions** | You | Yang | Hosung writes; Dr. Yang ensures accessibility for non-technical readers |
| **Design tension analysis** | Joint | Joint | Both perspectives are essential here |
| **Artifact curation (screenshots, diagrams)** | You | Yang | Hosung creates; Dr. Yang selects what best serves the narrative |
| **Writing: Introduction, Design Context** | Yang | You | Dr. Yang frames for the IJDL audience |
| **Writing: Design Decisions (Sec. 4)** | You | Yang | Hosung drafts; Dr. Yang edits for design case conventions |
| **Writing: Design Tensions, Reflections** | Joint | Joint | Collaborative writing |
| **Final review and IJDL formatting** | Yang | You | Dr. Yang's familiarity with IJDL expectations |

---

## 6. Connection to Papers 2 and 3

```
Paper 1 (Design Case)          Paper 2 (BJET Methodological)       Paper 3 (Experimental)
────────────────────           ──────────────────────────────       ──────────────────────
IJDL                           BJET Special Issue                   Computers & Education
                               SI-2026-000285
                               Abstract due: 2026-08-01

WHAT was designed and WHY      HOW to study artificial agency       DOES it work?
                               in multi-agent AI tools

EDR Phases:                    EDR Phases:                          EDR Phases:
Analysis/Exploration           Conceptual/Methodological            Evaluation/Reflection
Design/Construction            contribution

Outputs:                       Outputs:                             Outputs:
- Design narrative             - Artificial agency framework        - Empirical evidence
- Design tensions              - Methodological approach for        - Design principles
- Artifact documentation         studying agentic AI in ed.           (maturing intervention)
                               - Process-level modeling             - Theoretical understanding
                                 proposal

DEPENDENCY:                    DEPENDENCY:                          DEPENDENCY:
Standalone                     References Paper 1 for               References Paper 1 for
                               system description                   design rationale;
                                                                    Paper 2 for methodology
```

### How Paper 1 supports Papers 2 and 3:

- Paper 1 establishes the **design rationale** that Papers 2 and 3 can reference without re-documenting the full system.
- Paper 1 makes the **design tensions** explicit, providing a framework for what Papers 2 and 3 should empirically investigate.
- Paper 1 can be submitted and potentially accepted before Papers 2 and 3, creating a citable foundation.
- The **design case genre** allows Paper 1 to stand alone without empirical data, while Papers 2 and 3 provide the empirical complement.

### Suggested Timeline:

| Paper | Draft Target | Submission Target |
|---|---|---|
| Paper 1 (Design Case) | 2026-05-15 | 2026-06-15 (IJDL) |
| Paper 2 (BJET Methodological) | 2026-07-15 | 2026-08-01 (abstract), 2026-10-28 (full) |
| Paper 3 (Experimental) | After data collection | 2027 (Computers & Education) |

---

## Questions for Discussion

1. Does the proposed section structure align with your experience writing design cases for IJDL? Should we follow the IJDL template more closely?
2. The "checkpoint bug story" (Section 4.3) is a design failure narrative similar to your "Authentic Learning Design Failures" paper. Should we foreground failures more prominently, or keep them as supporting evidence within the design decisions?
3. How much technical detail is appropriate for the IJDL audience? The MCP architecture, YAML configurations, and SQLite details may need significant translation for instructional design readers.
4. Should we pursue the full design case format or the new "Quick Hit Design Case" format that IJDL recently introduced? The full format seems more appropriate given the richness of the design story, but the Quick Hit might be faster to produce.
5. The IJDL AI policy states authors should "hold themselves ethically responsible/accountable for all what they do with GenAI and LLMs-based tools." Since Diverga itself is an AI tool and we used AI-assisted processes in its design, should we address this meta-level issue explicitly?
