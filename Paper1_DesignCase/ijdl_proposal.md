# IJDL Special Section Proposal
## "Learning Designs to Support and Improve Workplace Performance"

**Prepared by:** Hosung You, Pennsylvania State University, College of Education
**Co-author:** Mohan Yang, Pennsylvania State University
**Date:** 2026-03-21
**Proposal Deadline:** 2026-03-31

---

## Short Description (75-100 words)

This design case documents Diverga, a 24-agent AI research methodology assistant built to scaffold doctoral researchers' methodological reasoning rather than replace it. Designed over 57 days by the first author, a Penn State doctoral student, Diverga addresses mode collapse: the tendency of AI tools to converge on predictable, homogeneous recommendations. Three design decisions are examined: a multi-agent architecture consolidated from 44 to 24 agents, Verbalized Sampling with Typicality Scores to structurally enforce recommendation diversity, and five required Human Checkpoints as cognitive forcing functions. Diverga is a learning design in disguise for researcher workplace performance.

---

## Extended Abstract (200-1,000 words)

### Context and Problem

Research methodology decisions are consequential workplace tasks for doctoral students and early-career scholars. Selecting a theoretical framework, choosing between qualitative and quantitative approaches, or determining an appropriate sampling strategy are not clerical operations: they define the epistemic character of a study and, by extension, shape a researcher's professional reputation and scholarly contribution. These decisions constitute a form of workplace performance in the knowledge work domain.

Artificial intelligence tools have proliferated rapidly in academic research contexts. Elicit, Consensus, SciSpace, and general-purpose assistants such as ChatGPT and Claude are increasingly integrated into researchers' workflows. Yet these tools share a structural problem: mode collapse. When researchers query AI systems for methodology guidance, the systems converge on the same high-probability recommendations regardless of the specificity of the research context. A tool asked about theoretical frameworks for technology adoption recommends TAM. Asked about qualitative design, it recommends thematic analysis. Asked about meta-analytic modeling, it recommends random effects. This convergence is not a bug in these tools; it is an artifact of how large language models are trained to maximize predictive probability. The most probable response is, by definition, the most common one. For researchers seeking methodological creativity and contextual fit, the most common recommendation is often not the best one.

Existing tools also tend toward automation bias: researchers accept AI recommendations without critical scrutiny. A 2025 Springer Nature report found a 78% uncritical acceptance rate for AI-generated methodology suggestions, and Microsoft Research (2025) identified a negative correlation between AI tool use and critical thinking engagement in knowledge work settings. The combination of mode collapse and automation bias creates a professional risk: researchers outsource methodological reasoning to systems that systematically homogenize it.

### The Designed Artifact

This design case documents Diverga, a 24-agent AI research methodology assistant built on Model Context Protocol (MCP) infrastructure and integrated with Claude Code. Diverga was designed by the first author, a Penn State doctoral student in education, over 57 days (January 22 to March 19, 2026) across 224 version-controlled commits. Dr. Mohan Yang, an instructional design scholar with published IJDL design cases, serves as collaborating researcher and critical external voice, compensating for the inherent limitation of the designer-as-evaluator position.

Diverga is, at one level, an AI research tool. At another level, it is a learning design in disguise. The system does not merely answer methodology questions; it structures the process by which a researcher engages with those questions, forces deliberate choice points, surfaces the typicality of each recommendation so the researcher can calibrate their reliance on it, and logs the researcher's decisions for retrospective reflection. Every interaction with Diverga is a scaffolded episode of methodological reasoning, not a transaction for an answer. In this sense, Diverga belongs to a tradition of learning designs that operate through the artifact rather than through explicit instruction: the form of the tool shapes the cognitive habits of its user.

The target users are social science doctoral students: knowledge workers whose research design capability is their primary professional competency and the central site of their workplace performance.

### Three Core Design Decisions

This design case examines three design decisions that define Diverga's character as a scaffolding instrument.

**Decision 1: Multi-Agent Architecture (Consolidation from 44 to 24 Agents)**

Diverga grew from 20 agents at launch (v1.0) to a peak of 44 agents (v6.7) before being consolidated to 24 agents across 9 functional categories in the current version (v11.0). The consolidation was not a retreat from ambition; it was a principled response to what the literature calls the "more agents is less" problem: beyond a threshold, additional agents increase inter-agent coordination overhead and user cognitive load without proportional gains in output quality. The design decision to consolidate was driven by functional overlap analysis, usage pattern review, and the principle that specialization should map to genuine epistemic distinctions rather than surface-level topic divisions. The before-and-after architecture provides a concrete illustration of iterative design reasoning in AI system development.

**Decision 2: Verbalized Sampling and Typicality Scores (Countering Mode Collapse)**

Diverga operationalizes Verbalized Sampling (VS), a methodology from computational linguistics research (Zhao et al., 2024), to structurally reduce mode collapse. Rather than asking the AI to "be diverse" (an instruction it can ignore), VS prompts agents to generate recommendations across the full typicality spectrum, from high-typicality options (T > 0.8, i.e., common, well-established approaches) to low-typicality options (T < 0.4, i.e., unconventional, context-sensitive alternatives). Critically, Diverga surfaces the Typicality Score to the researcher rather than using it only internally. A researcher who sees that a recommended framework scores T = 0.82 knows they are receiving a modal recommendation; one who sees T = 0.31 knows they are in genuinely novel territory. This transparency mechanism turns the T-Score into a metacognitive prompt, not merely a quality indicator. The VS Arena, Diverga's multi-perspective deliberation component, extends this further by assigning five epistemological persona agents (post-positivist, interpretivist, critical theorist, pragmatist, transformative) with structural constraints on what they cannot recommend, enforcing diversity at the architectural level.

**Decision 3: Human Checkpoint System (Five Required Cognitive Forcing Functions)**

Diverga's Human Checkpoint system designates five mandatory interruption points in the research design workflow where the AI halts and awaits explicit researcher decision before proceeding. These checkpoints are not optional suggestions; they are structural gates embedded in the system architecture. The design draws directly on Bucinca et al.'s (2021) cognitive forcing functions framework, which shows that deliberate interruption of automatic processing reduces overreliance on AI recommendations. The checkpoint design was itself iterative: an early version (v11.0) contained a silent bug in which all checkpoints auto-approved without user input, a failure that revealed how difficult genuine human oversight is to implement in autonomous systems. The fix and the subsequent reduction from many required checkpoints to five carefully chosen ones illustrates a recurring tension in the design: oversight rigor versus workflow fluidity. The design case documents this tension as unresolved rather than solved, honoring the complexity of designing for human-AI collaboration.

### Relevance to the Special Issue

This paper fits the "learning design in disguise" framing articulated by the special issue editors. Diverga was not built as a learning design; it was built as a research tool. Yet its architecture is organized around scaffolding methodological reasoning, its checkpoints function as cognitive forcing functions, its T-Score display functions as a metacognitive transparency mechanism, and its decision audit trail creates a log suitable for reflective practice. The researchers who use Diverga are knowledge workers; their research methodology capability is their professional performance domain. Diverga improves that performance not by providing better answers but by designing better questions.

The design case is first-person: the designer describes his own design process, its rationale, its failures, and its unresolved tensions. This first-person perspective, combined with Dr. Yang's external critical position, follows established IJDL design case conventions (Boling, 2010; Smith, 2010) and is positioned within the Analysis/Exploration and Design/Construction phases of the McKenney and Reeves (2012) Educational Design Research model. Empirical evaluation of Diverga's effects on researcher performance is reserved for a companion experimental paper; this design case makes the design story available to the field as a transparent, transferable account of how an AI scaffolding tool can be built with human oversight and epistemic diversity as first-order design values.

---

## Proposed Title

"Scaffolding Without Replacing: A Design Case of Human Checkpoints and Verbalized Sampling in an AI Research Methodology Assistant"

## Proposed Word Count

Approximately 5,000 words (text) plus figures and tables

## Format

Full design case (not Quick Hit)

## Contact

Hosung You
Doctoral Student, College of Education, Penn State
[Contact via institutional email]
