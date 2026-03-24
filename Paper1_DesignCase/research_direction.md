# Paper 1: Research Direction Memo

**Internal working document**
**Author: Hosung You**
**Date: 2026-03-21**

---

## 1. How This Design Case Fits Within the EDR Methodology

The McKenney & Reeves (2012) EDR model describes three iterative phases that produce two outcomes:

```
Analysis/Exploration  <-->  Design/Construction  <-->  Evaluation/Reflection
                              |                            |
                              v                            v
                    Maturing Intervention          Theoretical Understanding
```

Paper 1 (this design case) occupies the **first two phases**: Analysis/Exploration and Design/Construction. It documents what was analyzed (the mode collapse problem, the automation bias literature, the existing tool landscape), what design decisions emerged from that analysis, and how those decisions were constructed into a working system.

Critically, the design case does **not** claim to occupy the Evaluation/Reflection phase. It documents design rationale, not empirical evidence of effectiveness. This is both a genre requirement (design cases describe artifacts and their creation, not their outcomes) and a strategic choice (evaluation is Paper 3's territory).

However, the design case is not purely descriptive. It captures **embedded micro-evaluations**: the v10-to-v11 consolidation was informed by usage pattern analysis; the checkpoint reduction from many REQUIRED to 5 was informed by checkpoint fatigue observations; the VS Arena design was motivated by recognizing the limitations of single-agent simulated diversity. These are formative evaluations within the design process, not summative evaluations of the finished product. The design case can report them as part of the design story without trespassing on Paper 3's territory.

### EDR Positioning for the Three-Paper Series

| EDR Phase | Paper 1 (Design Case) | Paper 2 (BJET Methodological) | Paper 3 (Experimental) |
|---|---|---|---|
| Analysis/Exploration | Primary focus: problem analysis, literature landscape, design space mapping | References Paper 1 | References Paper 1 |
| Design/Construction | Primary focus: design decisions, rationale, iterations | Proposes methodology for studying artificial agency | References Paper 1 |
| Evaluation/Reflection | Formative only (within-design micro-evaluations) | Conceptual framework for evaluation | Primary focus: empirical evaluation |
| Maturing Intervention | Documents the current state of the intervention | N/A | Reports refined design principles |
| Theoretical Understanding | Articulates design tensions (pre-theoretical) | Proposes artificial agency framework | Reports empirical theoretical contributions |

This positioning allows each paper to have a clear, non-overlapping contribution while collectively telling the full EDR story.

---

## 2. What Makes Diverga's Design Story Unique and Publishable

### 2.1 A Novel Design Space

No published design case documents the creation of a multi-agent AI system for research methodology scaffolding. Design cases in IJDL have covered e-learning modules, virtual learning environments, PBL curricula, and accessibility interventions. An AI multi-agent system is a genuinely new type of designed artifact for this journal.

### 2.2 The Mode Collapse Problem as a Design Driver

Most AI tool design focuses on accuracy, efficiency, or user satisfaction. Diverga's design is driven by a different problem: the tendency of AI systems to homogenize the recommendations they provide. This is an unusual and intellectually compelling design driver. The paper can position mode collapse as analogous to problems in other design domains (e.g., standardized curricula that reduce pedagogical diversity, one-size-fits-all LMS configurations that constrain instructional approaches).

### 2.3 A Rich Iteration Story

The trajectory from v10 (44 agents) to v11 (24 agents) to v11.1 (checkpoint fix) provides a concrete, well-documented iteration narrative. This is exactly what design cases need: evidence of design evolution, not just a polished final product. The consolidation story demonstrates principled design reasoning (not arbitrary reduction), and the checkpoint bug story demonstrates learning from implementation failure.

### 2.4 Structural Diversity as a Design Principle

The VS Arena's `cannotRecommend` mechanism represents a genuinely novel approach to AI diversity. Rather than asking a system to "be diverse" (which is an instruction that can be ignored), Diverga constrains what the system cannot recommend, forcing structural diversity. This is a design principle that generalizes beyond Diverga to any AI system where output diversity matters.

### 2.5 The Designer-Researcher Tension

The paper can be transparent about the fact that the designer and the evaluator are the same person, and that the collaboration with Dr. Yang was explicitly sought to address this limitation. This meta-level honesty is itself a design decision worth documenting: the decision to design a collaboration structure that compensates for a known bias.

### 2.6 Checkpoint Design as Cognitive Forcing Function

The Human Checkpoint system is not merely a UI feature; it is a deliberate cognitive intervention designed to interrupt automated acceptance. Framing checkpoints through the lens of cognitive forcing functions (Bucinca et al., 2021) connects Diverga's design to broader HCI and judgment-under-uncertainty literature, giving the design case theoretical resonance without requiring heavy theoretical framing.

---

## 3. Key Design Tensions and Decisions to Highlight

The design case should be organized around tensions rather than chronology. Each tension represents a genuine design dilemma where reasonable designers might have chosen differently.

### Tension 1: Agent Count (More vs. Fewer)

- **The pull toward more:** Each specialized agent can encode deeper domain knowledge. 44 agents provided fine-grained coverage of research methodology subtopics.
- **The pull toward fewer:** Cognitive load on users, inter-agent coordination overhead, maintenance burden, and the "more agents is less" scaling finding.
- **The decision:** Consolidate to 24 through principled merging based on functional overlap and shared epistemic functions.
- **What this reveals:** Design for AI systems involves a fundamentally different set of tradeoffs than design for traditional learning environments. The "agents" are not merely interface elements; they are reasoning entities whose number affects system behavior in nonlinear ways.

### Tension 2: Simulated vs. Genuine Diversity

- **The pull toward simulated diversity:** Simpler to implement; single-agent VS already improves upon standard prompting; fewer infrastructure requirements.
- **The pull toward genuine diversity:** Single-agent diversity is constrained by the model's training distribution; no amount of prompting can fully counteract distributional bias; persona-based multi-agent diversity produces structurally different outputs.
- **The decision:** VS Arena with five epistemological personas and `cannotRecommend` constraints.
- **What this reveals:** "Be diverse" is not a design solution; diversity must be structurally enforced. This parallels instructional design insights about the difference between encouraging student participation (exhortation) and designing activities that require participation (structure).

### Tension 3: Oversight Rigor vs. Workflow Fluidity

- **The pull toward more checkpoints:** Every AI decision is a potential point of automation bias; maximum oversight maximizes researcher autonomy.
- **The pull toward fewer checkpoints:** Checkpoint fatigue degrades decision quality; frequent interruptions disrupt cognitive flow; overly cautious systems get abandoned.
- **The decision:** Reduce to 5 REQUIRED checkpoints at genuine cross-agent dependency points; downgrade internal checkpoints to RECOMMENDED.
- **The checkpoint bug as evidence:** The v11.0 bug where all checkpoints auto-approved illustrates how even well-designed oversight mechanisms can fail silently. The bug was not detected through testing but through architectural review, suggesting that checkpoint systems require dedicated verification.

### Tension 4: Transparency vs. Complexity

- **The pull toward full transparency:** Show the user everything (T-Scores, agent reasoning, alternative methodologies, confidence intervals). Informed users make better decisions.
- **The pull toward simplicity:** Too much information overwhelms novice researchers; decision paralysis; the system becomes harder to learn.
- **The decision:** Show T-Scores (a single transparency mechanism) and provide the Decision Audit Trail (logging, not display), but do not expose the full inter-agent communication or Arena deliberation process.
- **What this reveals:** Transparency in AI systems is not binary. Design must determine *which* information to surface and *when*, not simply whether to be transparent.

### Tension 5: Domain Specificity vs. Transferability

- **The pull toward deep specialization:** Social science research methodology has domain-specific nuances (epistemological paradigms, validity frameworks, sampling logic) that a generic tool cannot capture.
- **The pull toward generality:** A more general system reaches more users, accumulates more usage data, and iterates faster. The Obra comparison (76,000 GitHub stars) demonstrates the adoption advantage of generality.
- **The decision:** Deep specialization for social science research methodology, with the 9-category agent structure reflecting the actual workflow of research design.
- **What this reveals:** This tension connects to Dr. Yang's authentic learning framework. Authentic context requires domain specificity; generic AI tools provide inauthentic contexts that may scaffold surface-level task completion without supporting deep methodological reasoning.

---

## 4. Gaps That Need to Be Filled

### 4.1 Missing Documentation

| Gap | Description | Priority | Action Needed |
|---|---|---|---|
| **Design timeline reconstruction** | A chronological record of when key design decisions were made, ideally with git commit references. | High | Extract from Diverga git history; create a design evolution timeline. |
| **Alternatives-considered documentation** | For each major design decision, what alternatives were explicitly considered and why they were rejected. Some of this exists in discussion logs; much is tacit knowledge. | High | Hosung needs to write retrospective memos for each design decision; Dr. Yang can then probe for completeness. |
| **User-facing screenshots** | Current screenshots of Diverga in action: checkpoint interaction, T-Score display, agent selection, decision log output. | High | Capture from a fresh Diverga session. |
| **v10 documentation** | Description and screenshots of the 44-agent system (v10) for before/after comparison. | Medium | May need to reconstruct from git history or old screenshots. |
| **Agent consolidation rationale table** | A systematic table showing each v10 agent, which v11 agent it was merged into, and the specific rationale. | Medium | Partially available in the architecture discussion doc; needs formalization. |
| **Prompt engineering examples** | Annotated examples of agent system prompts showing how design decisions are operationalized in actual prompts. | Medium | Extract from current Diverga agent configurations. |

### 4.2 Missing Conceptual Work

| Gap | Description | Priority | Action Needed |
|---|---|---|---|
| **Design case framing** | The current documentation tells the design story from a developer perspective. It needs to be reframed through the design case genre conventions (Boling, 2010; Howard et al., 2012). | High | Dr. Yang's expertise is essential here. |
| **Authentic learning mapping** | The brainstorming doc maps Diverga features to Herrington's 9 elements, but this mapping needs to be refined and validated. Should it be included in Paper 1, or reserved for Papers 2/3? | Medium | Discuss with Dr. Yang. Including a light version in Paper 1 provides theoretical grounding without heavy framing. |
| **Comparison with published design cases** | How does Diverga's design case differ in structure and scope from Dr. Yang's previous design cases? Understanding this will help position the paper appropriately. | Medium | Read Yang & Lowell (2023) and Yang & Harbor (2023) carefully; identify structural parallels and departures. |
| **IJDL template compliance** | IJDL provides a Word template for design case submissions. The outline needs to be checked against this template. | Medium | Download and review the IJDL design case template. |

### 4.3 Missing Artifacts

| Artifact | Description | Priority |
|---|---|---|
| **Architecture diagram (v11)** | Clean visual showing 9 categories, 24 agents, their relationships | High |
| **Architecture diagram (v10)** | Clean visual showing the 44-agent structure for comparison | Medium |
| **Checkpoint flow diagram** | Visual showing the 5 REQUIRED checkpoints, their positions in the workflow, and prerequisite chains | High |
| **VS Arena interaction diagram** | Visual showing how 5 persona agents generate independent recommendations and how they are aggregated | High |
| **T-Score example display** | Annotated screenshot showing how T-Scores appear to the user | High |
| **Design evolution timeline** | Visual timeline showing major design milestones (v1 through v11.1) | Medium |

---

## 5. Questions for Dr. Yang

### Genre and Structure Questions

1. **Design case scope:** In your experience, how much contextual/theoretical framing is expected in an IJDL design case? The March 21 meeting established that Paper 1 should minimize theory, but IJDL design cases do typically situate the design within a body of knowledge. Where is the line?

2. **Failure narratives:** Your "Authentic Learning Design Failures" paper (IJDL, 2023) centered on design failures. Should Paper 1 foreground Diverga's design failures (the checkpoint bug, the v10 complexity problem, the simulated-vs.-genuine diversity limitation) as a primary narrative, or treat them as supporting evidence within a broader design story?

3. **Design case length:** What is the typical word count for a full IJDL design case? The outline above estimates approximately 7,200 words of text plus visuals. Is this within the expected range?

4. **Quick Hit vs. full design case:** IJDL recently introduced "Quick Hit Design Cases" as a shorter format. Given the richness of the Diverga design story, the full format seems more appropriate. Do you agree, or do you see value in the shorter format?

### Content Questions

5. **Technical detail calibration:** How much technical detail (MCP architecture, YAML configurations, SQLite implementation) is appropriate for IJDL readers? Your previous design cases were in educational program design and accessibility, which are less technically dense. What translation strategies worked for you?

6. **Authentic learning framework:** The brainstorming document maps Diverga to Herrington's 9 elements of authentic learning. Should we include this mapping in Paper 1 as a light analytical framework, or reserve it entirely for Papers 2 and 3? Including it would strengthen Paper 1's theoretical contribution but risks front-loading content that belongs in later papers.

7. **The designer-researcher dual role:** This is both a limitation and a feature of the design case. Having the designer write the case provides insider knowledge; having an external collaborator (you) provides critical distance. How should we frame this collaboration structure in the paper itself?

### Strategic Questions

8. **Submission timing:** If we target a draft by May 15 and submission by June 15 (2026), does this timeline work with your other commitments? Paper 2's BJET abstract is due August 1, so Paper 1 should ideally be submitted before that.

9. **Authorship order:** For a design case about a system that Hosung designed and built, with Dr. Yang providing the design case expertise and critical external perspective, what authorship order feels right? First instinct: You (Hosung) as first author, Yang as second. But if Dr. Yang leads the framing and narrative structure, the order could be discussed.

10. **Review of prior design cases:** Would you be willing to share drafts or pre-prints of your 2023 IJDL and accessibility design cases so I can study the structure, tone, and level of detail? This would help me align Paper 1 with genre expectations.

---

## Appendix: Key References for the Design Case

### Design Case Methodology
- Boling, E. (2010). The need for design cases: Disseminating design knowledge. *International Journal of Designs for Learning*, 1(1), 1-8.
- Howard, C. D., Boling, E., Rowland, G., & Smith, K. M. (2012). Instructional design cases and why we need them. *Educational Technology*, 52(3), 34-38.
- Smith, K. M. (2010). Producing the rigorous design case. *International Journal of Designs for Learning*, 1(1), 9-20.

### EDR Framework
- McKenney, S., & Reeves, T. C. (2012). *Conducting educational design research*. Routledge.

### Diverga's Theoretical Foundations
- Zhao, Y., et al. (2024). Verbalized sampling for language model selection. *arXiv:2510.01171*.
- Bucinca, Z., et al. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. *CSCW*.
- Wang, T., et al. (2024). Mixture-of-Agents yields emergent collaborative intelligence. *Together AI Technical Report*.
- Li, Z., et al. (2025). More agents is less: Scaling properties of multi-agent LLM systems. *arXiv:2602.03794*.

### Dr. Yang's Relevant Publications
- Yang, M., & Harbor, J. (2023). Authentic learning design failures: The need for learner and contextual analysis and participatory design. *International Journal of Designs for Learning*, 14(1), 88-105.
- Yang, M., Lowell, V., et al. (2023). Designing for accessibility in online learning: A design case. *JPED*.
- Yang, M. (2025). Towards dynamic learner state: Orchestrating AI agents and workplace performance via MCP. *Education Sciences*.
- Yang, M., et al. (2025). Analysing nontraditional students' ChatGPT interaction, engagement, self-efficacy and performance. *BJET*.
