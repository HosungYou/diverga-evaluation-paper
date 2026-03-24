# Diverga v11.0 Architecture Discussion

**From 44 Agents to 24: Consolidation, Arena Design, and the Pursuit of Genuine Methodological Diversity**

*Discussion Document for Diverga Evaluation Paper*
*March 10, 2026*

---

## 1. v11.0 Consolidation: From 44 Agents to 24

The transition from Diverga v10 to v11.0 represents a fundamental architectural rethinking rather than an incremental update. The original 44-agent system, while theoretically comprehensive, suffered from three interrelated problems: excessive cognitive load on users navigating the agent landscape, substantial inter-agent coordination overhead that degraded system responsiveness, and a steep learning curve that undermined adoption among the target population of social science researchers.

The consolidation reduced the agent count to 24 by systematically merging agents with overlapping functional boundaries. Several merges illustrate the logic. The A3 Devil's Advocate agent, A4 Ethics agent, and A6 Visualization agent were consolidated into a single A2 agent, reflecting the recognition that ethical scrutiny, adversarial critique, and visual representation of methodological trade-offs share a common epistemic function: helping the researcher interrogate assumptions. Similarly, the B4 Research Radar agent and B5 Parallel Processing agent were merged into B1, acknowledging that literature surveillance and parallel search execution are operationally inseparable in practice. These merges were not arbitrary reductions but principled consolidations guided by usage pattern analysis and functional overlap assessment.

The resulting 24 agents are organized across 9 categories (A through G, I, and X), each with clear ownership boundaries. Category A handles methodology critique and evaluation, Category B manages literature and knowledge retrieval, and so forth. The critical design principle is that no two agents should need to negotiate over who owns a particular subtask. Ownership boundaries are drawn such that any given user action maps unambiguously to a single responsible agent.

This consolidation aligns with broader findings in multi-agent system design. Brooks (1991) argued in subsumption architecture that behavioral competence emerges not from adding more specialized modules but from careful layering of fewer, well-integrated ones. The v11.0 consolidation applies this insight to AI-assisted research methodology: fewer agents with broader but well-defined responsibilities outperform a larger number of narrowly specialized agents that must constantly coordinate.

The practical consequences are significant. System latency decreased because fewer inter-agent messages are required for common workflows. The onboarding experience improved because users can form a mental model of 24 agents organized in 9 categories far more readily than 44 agents with ambiguous boundaries. And maintenance burden decreased because each agent's prompt engineering, testing, and checkpoint configuration is simpler when the agent count is lower.

---

## 2. Obra/Superpowers Comparison: Breadth vs. Depth

Obra (formerly known as "superpowers," with over 76,000 GitHub stars at the time of writing) represents the polar opposite of Diverga's architectural philosophy. Obra is a single-agent, tool-use framework with no domain specialization. It provides a general-purpose AI coding assistant that can invoke external tools, read files, and execute commands, but it makes no assumptions about the user's domain, workflow, or epistemic commitments.

Obra's popularity is instructive. Its 76,000 GitHub stars demonstrate a clear market signal: simplicity wins for adoption. A tool that requires no configuration, no domain knowledge, and no understanding of multi-agent architectures has an inherently lower barrier to entry. Developers can install Obra, point it at a codebase, and begin productive work within minutes. The cognitive overhead is minimal because there is only one agent to understand.

Diverga takes the opposite approach: deep domain specialization for social science research methodology. Each of its 24 agents encodes specific knowledge about research design paradigms, sampling strategies, validity frameworks, and ethical considerations that are unique to the social sciences. This specialization enables Diverga to provide guidance that a general-purpose tool cannot — for instance, recognizing when a researcher's stated epistemological commitments conflict with their proposed methodology, or suggesting alternative sampling strategies that align with a specific theoretical framework.

The comparison reveals a fundamental tension in AI-assisted tools that extends beyond the specific case of Diverga and Obra. General-purpose tools optimize for breadth of applicability and ease of adoption. Domain-specific tools optimize for depth of assistance and quality of output within their target domain. Neither approach dominates the other in all contexts. A researcher who needs help with both coding and methodology might prefer Obra's breadth, while a researcher who needs sophisticated methodological guidance will find Diverga's depth indispensable.

This tension is not unique to AI systems. It echoes longstanding debates in software engineering between frameworks and libraries (Tulach, 2008), between integrated development environments and text editors, and between enterprise platforms and point solutions. The resolution is typically not a winner-take-all outcome but a recognition that different tools serve different user needs at different stages of expertise and workflow maturity.

For the purposes of this evaluation study, the comparison with Obra establishes Diverga's design rationale: the system deliberately sacrifices generality and ease of adoption in exchange for domain-specific depth that cannot be replicated by a general-purpose single-agent framework.

---

## 3. Agent Arena and Emergent Behavior

The theoretical foundation for Diverga's multi-agent architecture draws on two lines of research: the Erdos minimum-overlap principle from combinatorial mathematics and the Mixture of Agents (MoA) architecture developed by Together AI.

The Erdos minimum-overlap principle, originally formulated in the context of set intersection problems in graph theory, provides a useful analogy for multi-agent system design. The principle suggests that a collection of sets (or, by analogy, agents) with minimal pairwise overlap covers more total ground than the same number of sets with high overlap. Applied to AI-assisted research methodology, this means that diverse agents with minimal capability overlap produce better collective outcomes — measured in terms of the breadth and novelty of methodological suggestions — than homogeneous agents that largely replicate each other's capabilities.

Together AI's Mixture of Agents architecture (Wang et al., 2024) provides empirical support for this principle in the LLM domain. MoA demonstrates that layered aggregation of diverse LLM outputs consistently outperforms individual models, even when some of the individual models in the mixture are weaker than the best single model. The key mechanism is that diverse models make uncorrelated errors: where one model exhibits a blind spot, another model's different training or prompting compensates. The aggregation layer then synthesizes the diverse outputs into a response that exceeds any individual model's capability.

These findings provide theoretical and empirical support for Diverga's evolution from a single-agent Verbalized Sampling (VS) approach to a multi-agent VS Arena design. In the original VS implementation, a single agent generates multiple methodology options. In the VS Arena design, multiple agents with distinct epistemological commitments independently generate methodology options, and an aggregation mechanism presents the researcher with a genuinely diverse set of choices.

The expected emergent behavior of the Arena design is that the collective output exhibits properties that no individual agent would produce alone: unexpected methodology combinations, novel applications of established methods to new problem types, and creative integrations of methods from different research traditions. This emergence is not mystical; it is the predictable consequence of combining diverse perspectives with minimal overlap, as both the Erdos principle and MoA architecture suggest.

---

## 4. VS Simulated vs. Genuine Diversity

The current Verbalized Sampling implementation in Diverga has a fundamental limitation that motivates the Arena redesign. In the current system, a single agent generates three methodology options in response to a researcher's problem description. The agent is explicitly instructed to "avoid the modal response" — that is, to avoid defaulting to the most common or expected methodology for the given research question. Despite this instruction, the agent's training distribution still biases its outputs toward common methodologies.

This is simulated diversity, not genuine diversity. The single agent is, in effect, sampling from a single distribution and attempting to spread its samples across that distribution's support. But the distribution itself is shaped by the agent's training data, which over-represents certain methodological approaches (e.g., surveys and experiments in education research) and under-represents others (e.g., arts-based research, participatory action research, indigenous methodologies). No amount of prompting can fully counteract this distributional bias because the bias is embedded in the model's weights, not in its instructions.

The VS Arena design addresses this limitation by using physically separate agents, each with a distinct epistemological persona. The five personas — post-positivist, critical theorist, pragmatist, interpretivist, and transformative — represent fundamentally different ontological and epistemological commitments. Each persona agent has a `cannotRecommend` constraint array that explicitly excludes specific methodologies from its recommendation space. For example, a post-positivist agent cannot recommend narrative inquiry, and a critical theorist agent cannot recommend randomized controlled trials.

The `cannotRecommend` mechanism is critical because it enforces diversity structurally rather than relying on the agent's willingness to comply with diversity instructions. When an agent is prohibited from recommending the three most common methodologies for a given research question, it is forced to explore less common alternatives. This is not a soft nudge; it is a hard constraint that reshapes the agent's effective search space.

The distinction between simulated and genuine diversity has important implications for the evaluation study. If the VS Arena produces methodology suggestions that differ more substantially across agents than the current single-agent VS produces across its three options, this would constitute evidence that structural diversity (via distinct personas and constraints) outperforms instructional diversity (via prompting a single agent to be diverse).

---

## 5. Academic Evidence

Several recent papers provide the theoretical and empirical foundation for the VS Arena design.

The original Verbalized Sampling paper (Zhao et al., 2024) introduced the VS methodology and demonstrated that explicit typicality scoring — asking the model to rate how "typical" each generated response is — reduces mode collapse in LLM outputs. By making the model aware of its own tendency toward modal responses, VS enables more diverse sampling from the model's output distribution. This finding directly informs Diverga's VS implementation: each methodology option is accompanied by a typicality score that helps the researcher understand whether the suggestion represents a conventional or unconventional approach.

The agent scaling literature provides a counterintuitive but important insight. Research on multi-agent scaling (Li et al., 2025) demonstrates that "more agents is less" — that is, adding more agents beyond a small optimal number degrades rather than improves collective performance, unless the additional agents contribute genuinely diverse perspectives. Specifically, two diverse agents outperform sixteen homogeneous agents across a range of benchmarks. This finding validates Diverga's v11.0 consolidation from 44 to 24 agents and supports the VS Arena design principle that diversity of agent perspectives matters more than agent count.

Research on diversity of thought in LLM ensembles (Wang et al., 2024) demonstrates that persona-based differentiation — assigning distinct identities or perspectives to different agents — improves collective problem-solving quality. When agents are prompted to adopt different viewpoints, their collective outputs cover more of the solution space and include more creative or unconventional proposals. This finding supports the VS Arena's use of epistemological personas.

However, research on persona-induced bias (Chen et al., 2025) introduces an important caveat. Persona injection — telling an agent to "think like" a particular type of expert — can introduce systematic biases that distort the agent's outputs in unpredictable ways. An agent told to think like a critical theorist may over-apply power analysis frameworks even when they are irrelevant to the research question. This finding motivates the VS Arena's preference for constraint-based differentiation (via `cannotRecommend` arrays) over positive persona framing. Rather than telling an agent what to be, the system tells the agent what it cannot recommend, allowing the agent's natural capabilities to fill the remaining search space without the distortions introduced by persona injection.

---

## 6. Claude Code Agent Teams Infrastructure

The practical implementation of the VS Arena design is facilitated by Claude Code's native Agent Teams infrastructure. This infrastructure, configured via YAML frontmatter files in the `.claude/agents/` directory, provides built-in support for several capabilities that the Arena design requires.

First, Agent Teams supports multi-agent dispatch with model routing. Each persona agent can be configured to use a specific model (e.g., Sonnet for standard methodology generation, Opus for complex interdisciplinary cases), enabling cost-performance optimization across the agent ensemble. The model routing is specified declaratively in the agent's YAML configuration, eliminating the need for custom orchestration code.

Second, Agent Teams provides tool access control at the agent level. Each persona agent can be granted access to specific tools (e.g., literature search, methodology database queries) while being denied access to others. This enables the enforcement of epistemic boundaries: a post-positivist agent might have access to quantitative methodology databases but not to qualitative coding tools, reinforcing its paradigmatic orientation.

Third, and most relevant to the Arena design, Agent Teams supports background execution via the `background: true` flag. This enables concurrent execution of all five persona agents, which is essential for the Arena's design goal of presenting the researcher with simultaneously generated, independently produced methodology suggestions. Without background execution, the persona agents would need to run sequentially, which would both increase latency and potentially allow later agents to be influenced by earlier agents' outputs (violating the independence assumption).

The alignment between Claude Code's Agent Teams infrastructure and the VS Arena's architectural requirements is not coincidental. The Arena design was informed by the capabilities of the target implementation platform. This is a pragmatic design decision: rather than designing an ideal architecture and then struggling to implement it on available infrastructure, the Arena design leverages the specific affordances of Claude Code's agent system to achieve its goals with minimal custom engineering.

---

## 7. Checkpoint System Design

The checkpoint system is a critical component of Diverga's architecture, serving as the mechanism through which human oversight is maintained in an otherwise autonomous multi-agent workflow. The v11.0 checkpoint system had a critical bug that undermined this function: the checkpoint hook always returned `{continue: true}`, implementing only a soft block that logged warnings but never actually prevented an agent from proceeding without prerequisite completion.

The root cause was an impedance mismatch between the checkpoint configuration format and the runtime state storage. The YAML-based prerequisite checker attempted to read checkpoint completion status from flat files that did not exist in the expected locations. The actual checkpoint state was stored in SQLite, but the hook's file-reading logic never consulted the database. As a result, the prerequisite check always failed silently and defaulted to allowing continuation.

The v11.1 fix addresses this at two levels. First, the hook was rewritten to read checkpoint state directly from SQLite, eliminating the impedance mismatch. When the hook needs to verify that a prerequisite checkpoint has been completed, it queries the SQLite database for the checkpoint's status rather than looking for a nonexistent file. Second, the hook now implements hard blocking (`continue: false`) for REQUIRED prerequisites, meaning that an agent cannot proceed past a checkpoint until all of its REQUIRED prerequisites are verified as complete in the database.

In addition to fixing the bug, v11.1 undertook a principled review of which checkpoints should be classified as REQUIRED versus RECOMMENDED. Four checkpoints were downgraded from REQUIRED to RECOMMENDED: CP_VS_001 (VS initialization), CP_VS_003 (VS option generation), CP_THEORY_SELECTION (theoretical framework selection), and SCH_API_KEY_VALIDATION (ScholarAI API key validation). The rationale for each downgrade was the same: these checkpoints are internal to their owning agents and should not gate other agents' progress. CP_VS_001 and CP_VS_003, for example, are internal to the VS agent's workflow; whether the VS agent has completed its initialization should not prevent the literature review agent from beginning its work.

After the downgrade, only 5 checkpoints remain REQUIRED, all of which represent genuinely cross-agent dependencies: cases where one agent's output is a necessary input to another agent's work. This reduction addresses the tension between oversight rigor and workflow fluidity. Too many required checkpoints create bottlenecks that slow the research process and frustrate users; too few remove the human-in-the-loop safeguards that distinguish Diverga from fully autonomous systems.

---

## 8. Persona Injection and Constraint-Based Differentiation

The VS Arena's approach to creating diverse persona agents merits detailed discussion because it represents a deliberate departure from the most common approach in the multi-agent LLM literature. The standard approach to persona creation is positive persona framing: instructing the agent to "think like a critical theorist" or "adopt the perspective of an interpretivist researcher." This approach is intuitive and easy to implement, but it has well-documented limitations.

Positive persona framing relies on the model's ability and willingness to maintain a consistent persona across an extended interaction. Research on persona stability in LLMs suggests that persona adherence degrades over long conversations, particularly when the persona conflicts with the model's training distribution (Chen et al., 2025). An agent instructed to think like a critical theorist may begin with power-analysis-inflected recommendations but gradually drift back toward its default (typically post-positivist) methodological preferences as the conversation progresses.

The VS Arena uses constraint-based differentiation as its primary mechanism for creating diverse personas. Each persona agent has a `cannotRecommend` array that specifies methodologies the agent is prohibited from suggesting. This is a negative constraint rather than a positive instruction: instead of telling the agent what to think, the system tells the agent what it cannot recommend. The constraint is enforced programmatically — recommendations that appear in the `cannotRecommend` array are filtered from the agent's output — making it robust against persona drift.

The `cannotRecommend` mechanism is complemented by two additional design elements. First, each persona agent has explicitly stated epistemological commitments covering ontology (what exists), epistemology (how we know), and axiology (what is valued). These commitments provide a coherent intellectual framework that guides the agent's reasoning without prescribing specific recommendations. A critical theorist agent, for example, has ontological commitments to social constructionism and axiological commitments to emancipation, which naturally orient its methodology suggestions toward participatory and action-oriented approaches.

Second, each persona agent receives perspective-taking instructions that encourage differentiation: "Consider what other agents in the Arena might recommend and ensure your recommendations are distinct." This instruction leverages the model's theory-of-mind capabilities to promote diversity. By reasoning about what a post-positivist or pragmatist agent would likely suggest, a critical theorist agent can identify and avoid overlapping recommendations, further increasing the collective diversity of the Arena's output.

The combination of `cannotRecommend` constraints, epistemological commitments, and perspective-taking instructions creates a multi-layered differentiation system. No single layer is sufficient on its own: constraints without commitments would produce arbitrary exclusions, commitments without constraints would be vulnerable to persona drift, and perspective-taking without either would have no structural foundation. Together, the three layers create genuine methodological diversity that is both robust and principled.

---

## 9. Critique and Limitations

Despite the principled design of the v11.0 architecture and VS Arena, several significant limitations warrant acknowledgment and future attention.

**MCP Complexity and Setup Friction.** The current Diverga system requires three MCP (Model Context Protocol) servers to operate: the core Diverga MCP server, the Humanizer MCP server (which manages researcher-facing language and tone), and the Journal MCP server (which handles publication-specific formatting and requirements). This three-server requirement creates substantial setup friction for new users. Each server must be independently installed, configured, and maintained, and version incompatibilities between servers can produce subtle and difficult-to-diagnose errors. For an academic tool whose target users are social science researchers — not software engineers — this level of infrastructure complexity is a significant adoption barrier. Future versions should explore server consolidation or a unified installer that abstracts the multi-server architecture from the user.

**Checkpoint Fatigue.** The v11.1 reduction from numerous REQUIRED checkpoints to 5 represents meaningful progress, but checkpoint fatigue remains a concern. In long research sessions — which are typical for doctoral students developing dissertation proposals — even 5 required checkpoints can create decision fatigue if they are clustered in time or if their questions require substantial deliberation. The current checkpoint design does not account for temporal spacing or cognitive load management. A more sophisticated approach might adapt checkpoint frequency based on session duration, user response patterns (e.g., reducing checkpoint frequency when the user consistently approves without modification), or the complexity of the decision being gated.

**Absence of a CSO (Chief Scientific Officer) Principle.** The current multi-agent architecture distributes authority equally among agents within their domains. No single agent has the authority to override or veto another agent's methodology recommendation. This flat authority structure is democratic but potentially problematic. In cases where one agent's recommendation conflicts with another's — for example, when the VS Arena produces five methodology suggestions that are individually coherent but collectively incompatible — there is no arbitration mechanism. A CSO principle would designate a meta-agent with the authority to evaluate the collective output for coherence, identify conflicts, and either resolve them or escalate them to the human researcher with a clear explanation of the conflict. The absence of such a principle means that the researcher bears the full burden of cross-methodology coherence assessment, which may be beyond the capability of novice researchers.

**Persona Bias Risk Within Allowed Search Spaces.** The `cannotRecommend` constraint mechanism prevents persona agents from suggesting excluded methodologies, but it does not address biases within the allowed search space. A critical theorist agent that cannot recommend surveys or experiments may still exhibit a training-distribution bias toward the most common critical methodologies (e.g., critical discourse analysis, critical ethnography) while neglecting less common approaches (e.g., critical systems heuristics, critical realism-informed mixed methods). The constraint mechanism reshapes the search space boundary but does not ensure uniform exploration within that boundary. Addressing this limitation may require combining `cannotRecommend` constraints with within-space diversity mechanisms such as the original VS typicality scoring.

**Evaluation Gap.** Perhaps the most significant limitation is the absence of empirical evaluation data for the VS Arena design. The architectural decisions described in this document are theory-driven, drawing on established principles from multi-agent systems, LLM ensemble research, and research methodology. However, the specific claim that the VS Arena produces genuinely more diverse and higher-quality methodology suggestions than the single-agent VS implementation has not been empirically tested. The evaluation study described in the accompanying research proposal aims to address this gap, but until data is collected and analyzed, the Arena design remains a theoretically motivated but empirically unvalidated architectural hypothesis.

---

## Synthesis: Design Tensions in AI-Mediated Research Methodology

The v11.0 architecture and VS Arena design exist at the intersection of several fundamental design tensions that are unlikely to be fully resolved by any single system.

The first tension is between **simplicity and specialization**. The Obra comparison demonstrates that simpler systems achieve wider adoption, while Diverga's design philosophy holds that domain-specific depth is necessary for meaningful research methodology assistance. The v11.0 consolidation from 44 to 24 agents represents an attempt to move toward simplicity without sacrificing specialization, but the system remains substantially more complex than single-agent alternatives.

The second tension is between **diversity and coherence**. The VS Arena is designed to maximize methodological diversity through distinct epistemological personas and constraint-based differentiation. But greater diversity increases the burden on the researcher (or a future CSO agent) to synthesize diverse suggestions into a coherent research design. Diversity without coherence is noise; coherence without diversity is mode collapse.

The third tension is between **autonomy and oversight**. The checkpoint system exists to maintain human oversight in an otherwise autonomous workflow, but every checkpoint interrupts the workflow and imposes cognitive load. The v11.1 reduction to 5 REQUIRED checkpoints reflects a judgment about where this tension should be balanced, but the optimal balance likely varies across users, research contexts, and stages of expertise.

The fourth tension is between **theoretical elegance and practical implementation**. The VS Arena's combination of `cannotRecommend` constraints, epistemological commitments, and perspective-taking instructions is theoretically well-motivated, but its practical effectiveness depends on implementation details — prompt engineering quality, model capability, constraint enforcement reliability — that can only be validated through empirical evaluation.

These tensions are not flaws to be eliminated but inherent characteristics of the design space. The contribution of the v11.0 architecture is not to resolve them but to make them explicit, to propose principled positions within each tension, and to create an evaluation framework through which those positions can be empirically assessed. The forthcoming evaluation study will provide the first empirical evidence on whether Diverga's particular resolution of these tensions produces meaningful benefits for social science researchers navigating the complex landscape of research methodology selection.

---

## References

Brooks, R. A. (1991). Intelligence without representation. *Artificial Intelligence*, 47(1-3), 139-159.

Chen, Y., et al. (2025). Persona-induced bias in large language model ensembles. *arXiv preprint*, arXiv:2511.11789.

Li, Z., et al. (2025). More agents is less: Scaling properties of multi-agent LLM systems. *arXiv preprint*, arXiv:2602.03794.

Tulach, J. (2008). *Practical API design: Confessions of a Java framework architect*. Apress.

Wang, J., et al. (2024). Diversity of thought improves reasoning in large language model ensembles. *arXiv preprint*, arXiv:2410.12853.

Wang, T., et al. (2024). Mixture-of-Agents yields emergent collaborative intelligence. *Together AI Technical Report*.

Zhao, Y., et al. (2024). Verbalized sampling for language model selection. *arXiv preprint*, arXiv:2510.01171.
