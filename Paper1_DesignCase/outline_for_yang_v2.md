# Design Case Outline: Diverga
## For IJDL Submission (Regular or Special Section)

**Target:** International Journal of Designs for Learning
**Format:** First-person design case (~5,000 words)
**Genre conventions:** Boling (2010); Smith (2010)

---

## Proposed Title

"Scaffolding Without Replacing: A Design Case of Human Checkpoints and Verbalized Sampling in an AI Research Methodology Assistant"

---

## Structure

### 1. Introduction
- AI research tools exhibit mode collapse (convergence on predictable recommendations) and encourage automation bias
- Design challenge: scaffold methodological reasoning rather than replace it
- Cognitive Apprenticeship (Collins et al., 1989) as lightweight theoretical lens; 6 methods map to 3 design decisions
- Scope: design story only; empirical evaluation reserved for companion paper

### 2. Design Context
- Designer: doctoral student, dual role (builder + researcher)
- External collaborator provides critical distance and design case expertise
- Target users: social science doctoral students
- Technical platform: MCP + Claude Code

### 3. Design Process
- 57 days, 224 commits, 5 iterative cycles (EDR; McKenney & Reeves, 2012)
- Key trajectory: 20 agents (v1) to 44 (peak) to 24 (consolidated)
- Platform co-evolution: Claude Code capabilities (hooks, Agent Teams) triggered design iterations
- Design failures documented: Sisyphus Protocol (same-day reversal), checkpoint bug (silent auto-approval), cross-platform support (abandoned after 41 days)

### 4. Design Problem
- Mode collapse: AI converges on modal recommendations regardless of context
- Automation bias: 78% uncritical acceptance rate
- No existing tool combines structured oversight with diversity-generating mechanisms

### 5. Design Decisions (core of the paper)

**5.1 Multi-Agent Architecture (44 to 24)**
- Alternatives: single-agent, modular tool-use, maintain 44
- Rationale: functional overlap, "more agents is less" scaling, epistemic rather than topical boundaries
- Evidence: architecture diagram, consolidation table

**5.2 Verbalized Sampling and T-Score**
- Alternatives: prompt-based diversity, RAG, random sampling
- Rationale: structural enforcement of diversity; T-Score as metacognitive transparency; VS Arena for epistemological plurality
- Evidence: T-Score examples, persona configuration

**5.3 Human Checkpoint System (5 REQUIRED)**
- Alternatives: no checkpoints, optional, every step
- Rationale: cognitive forcing functions (Bucinca et al., 2021); gates at cross-agent dependency points
- Evidence: checkpoint flow diagram, bug documentation

### 6. Design Tensions (unresolved)
- Simplicity vs. Specialization
- Diversity vs. Coherence
- Oversight Rigor vs. Workflow Fluidity

### 7. Reflection
- Transferable design principles: structural enforcement, transparency as metacognition, checkpoints as forcing functions
- Connection to companion papers (BJET methodological; experimental evaluation)

---

## Figures and Tables

| ID | Content | Status |
|---|---|---|
| Figure 1 | Conceptual Framework (EDR + CA + Design Decisions) | Generated |
| Figure 2 | 5 EDR Cycles timeline with agent count | Generated |
| Figure 3 | Platform-Design co-evolution | Generated |
| Figure 4 | Architecture comparison (v10 vs. v11) | Generated |
| Figure 5 | Checkpoint flow with CA labels | Generated |
| Table 1 | Diverga vs. existing tools | Draft ready |
| Table 2 | Agent consolidation summary | Draft ready |
| Table 3 | CA methods to Diverga mapping | Draft ready |
| Table 4 | Design tensions summary | Draft ready |

---

## Role Distribution (Proposed)

| Task | Lead | Support |
|---|---|---|
| Design case structure and IJDL framing | Yang | You |
| Design rationale documentation | You | Yang |
| Architecture and technical descriptions | You | Yang |
| Design tension analysis | Joint | Joint |
| Artifact curation (figures, diagrams) | You | Yang |
| Introduction, Design Context writing | Yang | You |
| Design Decisions writing | You | Yang |
| Reflection, final review | Joint | Joint |

---

## Key References

- Boling, E. (2010). The need for design cases. *IJDL*, 1(1), 1-8.
- Bucinca, Z., et al. (2021). Cognitive forcing functions. *CSCW*.
- Collins, A., Brown, J. S., & Newman, S. E. (1989). Cognitive apprenticeship. In Resnick (Ed.), *Knowing, learning, and instruction*.
- McKenney, S., & Reeves, T. C. (2012). *Conducting educational design research*. Routledge.
- Smith, K. M. (2010). Producing the rigorous design case. *IJDL*, 1(1), 9-20.
- Yang, M., & Harbor, J. (2023). Authentic learning design failures. *IJDL*, 14(1), 88-105.
- Zhao, Y., et al. (2024). Verbalized sampling. arXiv:2510.01171.

---

## Accompanying Materials

A detailed draft (~4,800 words with all figures/tables embedded) is available as a companion document for reference during writing.
