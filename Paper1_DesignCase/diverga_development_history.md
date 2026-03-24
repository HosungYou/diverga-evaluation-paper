# Diverga Development History: A Design Case Documentation

**Prepared for:** Design Case Research Paper
**Repository:** https://github.com/HosungYou/Diverga
**Development Period:** January 22, 2026 -- March 19, 2026 (57 days)
**Total Commits:** 224
**Developer:** Hosung You, Pennsylvania State University, College of Education

---

## 1. Origin and Motivation

### 1.1 The Problem: Mode Collapse in Research AI

Diverga was created to solve a specific, well-documented problem in AI-assisted research: **mode collapse**. When researchers use general-purpose AI assistants for methodology decisions, the AI consistently recommends the same predictable, "safe" options:

> "For technology adoption, I recommend TAM." (every single time)
> "For your meta-analysis, use random effects model." (always)
> "Try thematic analysis for your qualitative study." (the obvious choice)

This convergence on modal (most common) recommendations undermines the exploratory nature of research, particularly in social science disciplines such as Education, Psychology, Management, Sociology, HRD, and Communication.

### 1.2 The Founding Insight: Verbalized Sampling

The project was grounded in the **Verbalized Sampling (VS) methodology** published on arXiv (arXiv:2510.01171). VS provides a theoretical framework for preventing mode collapse by exploring the "long tail of intellectual possibility" through Typicality Scores (T-Scores). Instead of always recommending the highest-probability option (T > 0.8), VS encourages exploration across the full typicality spectrum.

The project's tagline captures this philosophy:

> "When AI recommendations converge on the modal, Diverga helps you explore the exceptional."

### 1.3 Initial Commit (January 22, 2026)

The project began under the name **"Research Coordinator"** with 20 specialized research agents organized into 5 categories:

- **Category A**: Theory & Research Design (agents 01--04)
- **Category B**: Literature & Evidence (agents 05--08)
- **Category C**: Methodology & Analysis (agents 09--12)
- **Category D**: Quality & Validation (agents 13--16)
- **Category E**: Publication & Communication (agents 17--20)

Commit `312bd97` (2026-01-22):
> "Add 20 specialized research agents for social science researchers integrated with Claude Code Skills system."

The system was built as a **Claude Code plugin** from day one, using the Claude Code Skills system for agent registration and the `Task` tool for parallel agent execution.

---

## 2. Version Evolution Timeline

### 2.1 v1.0.0 -- Research Coordinator (January 22, 2026)

**Commit:** `312bd97` | **Date:** 2026-01-22

The initial release established the core concept: a master coordinator skill with 20 individual agent skills covering the complete social science research lifecycle. Key features included:

- Master coordinator with auto-trigger system (Korean + English keywords)
- Parallel execution support via `Task` tool
- Installation/uninstallation scripts
- Bilingual documentation (Korean/English)

**Agent count:** 20 | **Categories:** 5 (A--E)

### 2.2 v2.0.0 -- VS Integration (January 22, 2026)

**Commit:** `6ab488e` | **Date:** 2026-01-22 (same day as v1.0)

The VS methodology was integrated across all 20 agents within hours of the initial commit, indicating that VS was always the planned core differentiator. This release introduced:

- **Tiered VS application** (a key design decision):
  - **Full VS** (5 phases): agents 02, 03, 05, 10, 16 (highest-stakes decisions)
  - **Enhanced VS** (3 phases): agents 01, 04, 06, 07, 08, 09
  - **Light VS** (modal awareness only): agents 11--15, 17--20
- **T-Score (Typicality Score) system** for recommendation diversity
- VS-Research-Framework.md reference document
- Claude Code marketplace registration

### 2.3 v2.1.0 -- Plugin Marketplace (January 23, 2026)

**Commits:** `2bef67b` through `50d4387` | **Date:** 2026-01-23

Focused on distribution: single plugin install now included all 21 skills. Marketplace.json schema compatibility fixes.

### 2.4 v3.0.0 -- Creativity Enhancement Suite (January 23--24, 2026)

**Commits:** `e85e05d` through `8ada0f8` | **Dates:** 2026-01-23 to 2026-01-24

A major architectural expansion built on a formal analysis of VS methodology limitations. The v3.0 design document identified that VS alone was insufficient for truly creative research assistance, proposing 5 creative mechanisms:

1. **Forced Analogy Mechanism** -- cross-domain idea transfer
2. **Iterative Divergent-Convergent Loop** -- alternating expansion/contraction
3. **Semantic Distance Scorer** -- measuring conceptual novelty
4. **Temporal Reframing Mechanism** -- shifting temporal perspectives
5. **Community Simulation Mechanism** -- simulating research community reactions

The system introduced a modular architecture with `core/`, `creativity/`, and `interaction/` modules. Agents were upgraded in tiers: 5 FULL VS, 6 ENHANCED VS, 9 LIGHT VS.

**Key design decision:** The checkpoint system using `AskUserQuestion` was formally specified here, establishing the pattern that would become central to Diverga's identity.

### 2.5 v3.1.0 -- Conceptual Framework Visualizer (January 24--25, 2026)

**Commit:** `7caeda3` | **Date:** 2026-01-24

Added Agent 21 (Conceptual-Framework-Visualizer) with **Nanobanana** integration (Gemini API) for diagram generation. Introduced a novel ASCII Blueprint to Nanobanana pipeline, demonstrating early interest in visual output capabilities.

### 2.6 v4.0.0 -- Architecture Restructure (January 25, 2026)

**Commits:** `91f77b0` through `265062d` | **Date:** 2026-01-25

A complete architectural overhaul focused on making the system accessible to non-technical researchers:

- **Context persistence** across research lifecycle sessions
- **Pipeline templates** (PRISMA 2020 8-stage workflow)
- **Integration Hub** for Excel, PowerPoint, Word, R, Semantic Scholar
- **Guided Wizard** using AskUserQuestion-based UX
- **Auto-Documentation** for decision logs and PRISMA checklists

**Key design decisions:**
- VS Engine simplified from 14 checkpoints to 3-stage process
- All agents converted from Korean to English base (with Korean input support retained)
- Agents reorganized into 3-tier structure: Flagship/Core/Support
- Design principle established: *"Human decisions remain with humans (checkpoints preserved)"*

### 2.7 v5.0.0 -- Sisyphus Edition (January 25, 2026)

**Commit:** `dd98cef` | **Date:** 2026-01-25

A major expansion from 21 to 33 agents, adding complete qualitative research support:

- 12 new agents: A5, C2, C3, C4, D1--D4, E2, E3, H1, H2
- New categories: D (Data Collection), H (Specialized Approaches)
- **Sisyphus Protocol**: Continuation enforcement until verified completion
- **Paradigm Auto-Detection**: Quantitative/Qualitative/Mixed methods
- Full qualitative support: phenomenology, grounded theory, case study, ethnography, action research
- Mixed methods integration (joint displays, meta-inference)

**Agent count:** 33 | **Categories:** 8 (A--H)

The name "Sisyphus Edition" reflected the protocol's philosophy that the system should persistently work toward completion, never giving up on a research task.

### 2.8 Naming Journey: Research Coordinator -> NovaScholar -> Diverga (January 25, 2026)

Three name changes occurred on the same day, reflecting the project's search for identity:

1. **Research Coordinator** (v1.0--v5.0): Descriptive but generic
2. **NovaScholar** (`68951c0`): "VS methodology as core value; Beyond Modal: AI Research Assistant That Thinks Creatively." Abandoned because "NovaScholar already exists."
3. **Diverga** (`04724ba`): Final name. "Emphasizes divergent thinking and breaking free from modal recommendations." A portmanteau of "diverge" and the feminine suffix "-a," carrying the meaning: *"Diverge from the Modal, Discover the Exceptional."*

**Notable bug:** The automated rename script caused the word "innovation" to be corrupted to "indivergation" (sed replacement side effect), requiring a fix.

### 2.9 v6.0.0 -- Clean Slate Edition (January 25, 2026)

**Commit:** `b443f53` | **Date:** 2026-01-25

A pivotal philosophical turning point. This release **removed** several v5.0 features that prioritized AI autonomy over human control:

**Removed:**
- Sisyphus Protocol ("work never stops until complete")
- Iron Law of Continuation ("agent OR checkpoint")
- OMC autonomous modes (ralph, ultrawork, autopilot, ecomode)

**Strengthened:**
- Human checkpoint system (now mandatory)
- All REQUIRED checkpoints must HALT and WAIT
- Language shift: "진행하겠습니다" ("I will proceed") changed to "진행해도 될까요?" ("May I proceed?")

**New design principle:**
> "AI works BETWEEN checkpoints, humans decide AT them."

This version reduced from 33 to 27 agents through consolidation, introduced category-based naming (A1, A2, B1 instead of numbered agents 01--20), and restructured to the `.claude` directory convention.

**Agent count:** 27 | **Categories:** 8 (A--H, reduced agents per category)

### 2.10 v6.2.0--6.3.0 -- Meta-Analysis Specialization (January 26, 2026)

**Commits:** `426680c` through `b3e73c4` | **Date:** 2026-01-26

- B5 (ParallelDocumentProcessor) added
- Multi-Gate Validation Pipeline for meta-analysis
- C5/C6/C7 Meta-Analysis Agent System
- Universal Meta-Analysis Codebook v2.1--v2.2

### 2.11 v6.4.0 -- Plugin Marketplace Edition (January 27, 2026)

**Commit:** `be23b5f` | **Date:** 2026-01-27

Transformed Diverga into a proper Claude Code marketplace plugin:
- `/diverga:setup` wizard skill
- `/diverga:help` reference skill
- Auto-trigger dispatch patterns for all 40 agents
- Model routing: opus/sonnet/haiku per agent

**Agent count:** 40 | Installation simplified to 3 steps.

### 2.12 v6.5.0 -- HAVS Methodology & Task Tool (January 27--28, 2026)

**Commits:** `0d13485`, `b23c80b`, `37ea4fe` | **Dates:** 2026-01-27 to 2026-01-28

Two significant additions:

1. **HAVS (Humanization-Adapted VS)** methodology for G6-AcademicStyleHumanizer:
   - 3-phase VS specialization for text transformation (vs. standard 5 phases)
   - Three differentiated directions: A (conservative), B (balanced), C (aggressive)
   - Modal transformation warnings (T > 0.7) to avoid detectable AI patterns
   - Discipline-specific writing styles (Education, Psychology, Management, Health Sciences, Social Sciences)

2. **Task tool parallel execution** via `/agents/` directory:
   - 40 agent .md files registered for Task tool
   - oh-my-claudecode compatible invocation pattern
   - Skills directory moved to root level for auto-scanning (v6.5.2)

### 2.13 v6.6.0--6.6.2 -- Cross-Platform Support (January 28--30, 2026)

**Commits:** `546419f` through `e4bf261` | **Dates:** 2026-01-28 to 2026-01-30

Ambitious expansion to three platforms:
- **Claude Code** (primary): Full feature set
- **Codex CLI** (OpenAI): AGENTS.md bootstrap, CLI wrapper, GPT model routing
- **OpenCode** (open-source): Plugin hooks, checkpoint enforcer

Model mapping: opus/sonnet/haiku mapped to o1/gpt-4/gpt-3.5-turbo for Codex.

**Agent count:** 40 | **Categories:** 8 (A--H)

This period also included a comprehensive QA Protocol (v1.0 through v3.2), with real conversation testing scenarios (QUAL-001 through QUANT-005).

### 2.14 v6.7.0 -- Systematic Review Automation (January 30, 2026)

**Commit:** `d0dd5e3` area | **Date:** 2026-01-30

Added **Category I: Systematic Review Automation** with 4 new agents:
- I0: ReviewPipelineOrchestrator (Opus)
- I1: PaperRetrievalAgent (Sonnet) -- multi-database fetching
- I2: ScreeningAssistant (Sonnet) -- AI-PRISMA 6-dimension screening
- I3: RAGBuilder (Haiku) -- zero-cost vector database construction

New checkpoints: SCH_DATABASE_SELECTION (REQUIRED), SCH_SCREENING_CRITERIA (REQUIRED), SCH_RAG_READINESS (RECOMMENDED), SCH_PRISMA_GENERATION (OPTIONAL).

**Agent count:** 44 | **Categories:** 9 (A--I)

### 2.15 v6.9.1--6.9.2 -- Plugin Discovery Crisis (February 2--3, 2026)

**Commits:** `efc024a`, `f5b38bc` | **Dates:** 2026-02-02 to 2026-02-03

A critical debugging episode spanning 6+ hours:

```
Phase 1: Plugin shows installed, skills listed, but /diverga:help -> "Unknown skill"
Phase 2: Discovered undocumented SKILL.md `version` field requirement
Phase 3: Symlink workaround (hyphen prefix works, colon prefix fails)
Phase 4: Root cause: marketplace cache pulled old version without version field
```

**Key learnings documented:**
1. SKILL.md requires a `version` field (undocumented Claude Code requirement)
2. Marketplace has cache lag (10--15 minutes after push)
3. Plugin (colon) vs Local (hyphen) skill loading use different paths

150 files changed, 48 insertions(+), 50,430 deletions(-) from orphaned directory cleanup.

### 2.16 v7.0.0 -- Memory System (February 3, 2026)

**Commit:** `c07d180` | **Date:** 2026-02-03

Complete research context persistence system:

- **3-Layer Context System:**
  - Layer 1: Keyword-triggered ("my research," "연구 진행")
  - Layer 2: Task interceptor (context injected into agent prompts)
  - Layer 3: CLI explicit access

- **Checkpoint Auto-Trigger System** with 17 standard checkpoints
- **Dual-Tree Filesystem**: `.research/baselines/` (verified) + `.research/changes/` (in-progress)
- **Decision Audit Trail**: append-only, immutable log with versioning
- **Python library** (`lib/memory/`): 15 modules, 23 API methods
- **Migration support** from v6.8 format

### 2.17 v8.0.0 -- Project Visibility & HUD (February 4, 2026)

**Commits:** `c82c36f`, `a401d8f` | **Date:** 2026-02-04

- Independent HUD statusline (4 presets: research, checkpoint, memory, minimal)
- Setup wizard simplified from 9 steps to 3
- Natural language project initialization ("I want to conduct a systematic review on AI")
- Bilingual intent detection with confidence scoring
- Auto-generated research documentation (`docs/` directory with 7 files)

### 2.18 v8.1.0 -- Checkpoint Enforcement Strengthening (February 9, 2026)

**Commit:** `0de04a1` | **Date:** 2026-02-09

A critical enforcement overhaul ensuring `AskUserQuestion` tool is called at every human decision point:

- Text-based questions no longer count as checkpoint compliance
- Agent Prerequisite Map with dependency ordering
- No-skip policy for REQUIRED checkpoints
- Multi-agent checkpoint coordination (union of prerequisites)
- 120 TDD tests added

### 2.19 v8.2.0 -- MCP Runtime Checkpoint Enforcement (February 12, 2026)

**Commit:** `e10edc5` | **Date:** 2026-02-12

The introduction of the **MCP (Model Context Protocol) checkpoint server**, a major architectural shift:

- **7 MCP tools** for runtime verification
- SKILL.md checkpoint sections simplified from 35 lines to 8 lines per agent (675 lines saved across 28 agents)
- State path unification under `.research/` directory
- Priority Context (500-char compression-resilient summary)
- **104 unused Python files removed**, replaced by 3-file MCP server (~200 lines)

**Key insight:** Moving from prompt-level enforcement (SKILL.md instructions) to runtime enforcement (MCP tools) dramatically reduced token overhead while improving reliability.

### 2.20 v8.3.0 -- Cross-Platform Migration (February 12, 2026)

**Commit:** `3bd4a6d` | **Date:** 2026-02-12

Brought Codex CLI and OpenCode up to feature parity:
- 47 individual SKILL.md files for Codex CLI
- GPT-5.3-Codex model routing
- Platform compatibility: Claude Code 100%, Codex CLI ~75%, OpenCode ~70%

### 2.21 v8.5.0 -- Developer Experience (February 15, 2026)

**Commit:** `eefb04c` | **Date:** 2026-02-15

- **Single Source of Truth**: `config/agents.json` (44 agents) drives all derived files
- **Version sync**: `scripts/sync-version.js` propagates version across 100+ files
- **Release automation**: one-command version bump, sync, generate, changelog, git tag
- **Diagnostics**: `scripts/doctor.js` with 9 automated checks
- **Agent Teams pilot**: I0 Team Lead mode with parallel database fetching
- **Pre-commit hooks**: husky enforces consistency

### 2.22 v9.0.0 -- SQLite + MCP Server Split (February 15--16, 2026)

**Commits:** `eacb628` through `090a318` | **Date:** 2026-02-15

Major architecture release:
- Monolithic `checkpoint-server.js` (7 tools) split into modular `diverga-server.js` (16 tools)
- Three server domains: checkpoint, memory, comm (agent messaging)
- **SQLite backend** (WAL mode) for ACID-safe parallel agent execution
- Dual backend: SQLite opt-in, YAML default for backward compatibility
- Auto-migration from YAML/JSON to SQLite
- **464 tests** across 9 test suites

### 2.23 v9.1.0--9.2.1 -- Humanization Pipeline & MCP Integration (February 22--23, 2026)

**Commits:** `8566955` through `85564c5` | **Dates:** 2026-02-22 to 2026-02-23

Rapid-fire releases building the humanization pipeline:

- **v9.1.0**: Humanization Pipeline v2.0 with 3-layer transformation
- **v9.2.0**: Humanizer MCP server (4 tools) providing exact stylometric computation
  - Replaced LLM estimation with algorithmic precision for burstiness CV, MTLD, Fano Factor
  - 120 tests (84 pipeline + 36 MCP server)
- **v9.2.1**: Zero-setup MCP via plugin `.mcp.json` auto-registration
  - Adopted oh-my-claudecode distribution strategy: `uvx` for Python, `npx` for Node.js, `${CLAUDE_PLUGIN_ROOT}` for bundled

### 2.24 v10.0.0--10.3.2 -- Discourse-Level Detection & Journal Intelligence (February 23 -- March 5, 2026)

**Commits:** `ad19875` through `c1c11f6` | **Dates:** 2026-02-23 to 2026-03-05

- **v10.0.0**: 4-layer humanization pipeline with discourse-level AI detection (DT1--DT4), 13 quantitative metrics, 6-component composite scoring, 7 discipline profiles
- **v10.1.0**: `/diverga:humanize` orchestration skill (545 lines) enforcing sequential G5->G6->F5 with mandatory human checkpoints between passes
- **v10.2.0**: Rich Checkpoint v2.0 with section-level score tables, Balanced (Fast) mode, parallel G5+F5 execution, target score auto-stop
- **v10.3.0**: Journal Intelligence MCP server (6 tools) powered by OpenAlex and Crossref APIs; G1 Journal Matcher overhauled to checkpoint-based pipeline
- **v10.3.1**: Platform-level hook enforcement via `hooks/hooks.json` (PreToolUse hooks); OpenCode full feature parity with 44 agents
- **v10.3.2**: Portability fix replacing hardcoded `/Users/hosung/` paths with `$HOME/`

### 2.25 v11.0.0 -- Major Simplification (March 10, 2026)

**Commit:** `73f0e92` | **Date:** 2026-03-10

A dramatic consolidation release:

- **44 agents reduced to 24** through intelligent merging
- **Claude Code exclusive** (removed Codex CLI and OpenCode support)
- **SQLite-only backend** (removed YAML/JSON)
- **CLAUDE.md reduced from 59KB to 12KB** (79% reduction)

Agent consolidation logic:
- A3 (Devil's Advocate) + A6 (Visualizer) merged into A2
- A4 (Ethics) + F4 (Bias Detection) created new X1 (Research Guardian)
- B3, C6, C7 merged into C5 (meta-analysis pipeline)
- F1, F2, F3 merged into G2 (Publication Specialist)
- H1, H2 merged into C2 (Qualitative Designer)
- New **Category X**: Cross-Cutting (Research Guardian agent)

### 2.26 v11.1.0 -- VS Arena (March 12, 2026)

**Commit:** `40d15f5` | **Date:** 2026-03-12

- **VS Arena**: 5 epistemological persona agents (V1--V5) for multi-agent methodology debate
- Hard-block enforcement for 5 REQUIRED checkpoints via rewritten `prereq-enforcer.mjs`
- ~30 stale files deleted
- 170 tests updated for v11.1 architecture (24 core + 5 VS Arena = 29 agents)

### 2.27 v11.1.1--11.3.1 -- Tooling & Infrastructure (March 13--14, 2026)

- **v11.1.1**: `latex2omml` integration (LaTeX to Word OMML converter)
- **v11.1.2**: Setup wizard fix, first-run detection, developer guide
- **v11.3.0**: Selective symlink dev mode, one-command deploy pipeline, Agent Teams integration, setup wizard redesigned as researcher profile interview
- **v11.3.1**: Plugin hooks duplication fix, version drift fix, deploy pipeline bug fixes

### 2.28 v12.0.0 -- Unified Orchestrator (March 19, 2026)

**Commits:** `e948e1d` through `305ecc3` | **Date:** 2026-03-19

The current version, focused on architectural clarity:

- **Unified `/diverga:orchestrator` skill** replacing `research-orchestrator` + `vs-arena`
- **CLAUDE.md slimmed from 16.8KB to <5KB** (reducing per-session token load from ~4,200 to ~1,250)
- Content extracted to `docs/CHECKPOINT-RULES.md`, `docs/ARCHITECTURE.md`, `docs/MCP-TOOLS.md`
- Research-coordinator slimmed from 28KB to ~14KB
- Agent Teams + VS Arena merged into setup Step 4
- Legacy `routing.yaml` (33-agent v6.0 era) deleted

**Agent count:** 24 core + 5 VS Arena = 29 | **Categories:** 9 (A, B, C, D, E, F, G, I, X) + V

---

## 3. Key Design Decisions

### 3.1 Tiered VS Application (v2.0, January 22)

Rather than applying VS uniformly, agents were categorized by how much creative divergence their role warranted:

- **Full VS** (5 phases): For high-stakes methodological decisions (theory selection, paradigm choice)
- **Enhanced VS** (3 phases): For decisions with moderate impact
- **Light VS** (modal awareness): For operational tasks where creativity matters less

**Rationale:** Not every research step benefits from divergent thinking. A literature search agent needs thoroughness more than creativity; a theory selection agent needs maximum divergence.

### 3.2 Removing Sisyphus Protocol (v6.0, January 25)

The v5.0 "Sisyphus Protocol" enforced continuous AI operation until task completion. V6.0 deliberately removed it along with all autonomous continuation modes.

**Before (v5.0):** The system would keep working autonomously, only pausing at checkpoints.
**After (v6.0):** The system works *between* checkpoints but always defers to human judgment *at* them.

This was a philosophical pivot from "AI-driven with human oversight" to "human-driven with AI assistance."

### 3.3 Category-Based Agent Naming (v6.0.1, January 25)

Switched from sequential numbering (01--20) to category-letter + number (A1, B2, C5):
- More intuitive for researchers
- Enables category-level operations (e.g., "run all Category B agents")
- Scales better when adding agents

### 3.4 HAVS as a Separate Methodology (v6.5, January 27)

Rather than applying standard VS to text humanization, a specialized 3-phase variant (HAVS) was created:
- Standard VS uses 5 phases suited for recommendation generation
- HAVS uses 3 phases suited for text transformation
- Three directions (A/B/C) map to humanization intensity rather than typicality

### 3.5 MCP Over Python for State Management (v8.2, February 12)

The Python memory system (104 files in `lib/memory/`) was replaced by a 3-file Node.js MCP server:
- **Before:** Python library required separate installation, PYTHONPATH management, and import resolution
- **After:** MCP server runs as a subprocess, communicates via stdio, no dependency management
- 104 files removed, ~27,000 lines deleted, replaced by ~200 lines

### 3.6 Soft Block vs. Hard Block Enforcement (v10.3.1, February 28)

A deliberate choice to use **soft blocks** (always `continue: true` with warning injection) rather than hard blocks:
- Hard blocks would prevent agent execution entirely
- Soft blocks inject warning messages but allow the LLM to comply voluntarily
- This preserves the "AI assistant" relationship rather than creating an "AI gatekeeper"
- Later revised in v11.1.0 to use hard blocks for REQUIRED checkpoints only

### 3.7 Agent Consolidation from 44 to 24 (v11.0, March 10)

The most aggressive architectural decision. Rationale:
- Many agents had overlapping responsibilities
- Token overhead of 44 agent definitions exceeded practical limits
- Platform fragmentation (Codex/OpenCode support) was not delivering value
- 24 well-defined agents serve researchers better than 44 with fuzzy boundaries

Consolidation followed a principle of merging agents that naturally co-occur (e.g., ethics oversight + bias detection = Research Guardian).

### 3.8 CLAUDE.md Token Budget (v12.0, March 19)

CLAUDE.md is loaded into every Claude Code session. Reducing it from 16.8KB (~4,200 tokens) to <5KB (~1,250 tokens) saved ~3,000 tokens per session. Content was moved to reference documents loaded on demand.

---

## 4. Architecture Evolution

### 4.1 Phase 1: Skills-Only Architecture (v1.0--v3.1, Jan 22--25)

```
Claude Code
  └── .claude/skills/
       ├── research-coordinator/SKILL.md  (master)
       └── research-agents/
            ├── 01-research-question-refiner/SKILL.md
            ├── 02-theoretical-framework-architect/SKILL.md
            └── ... (20 agents)
```

All intelligence lived in SKILL.md files. No runtime state, no MCP, no backend.

### 4.2 Phase 2: Modular Core with Creativity Suite (v3.0--v4.0, Jan 23--25)

```
core/
  ├── vs-engine.md          (VS methodology)
  ├── dynamic-t-score.md    (T-Score system)
  └── checkpoint-system.md  (user interaction)
creativity/
  ├── forced-analogy.md
  ├── divergent-convergent-loop.md
  ├── semantic-distance-scorer.md
  ├── temporal-reframing.md
  └── community-simulation.md
interaction/
  └── comprehensive-checkpoint.md
```

Added context persistence, pipeline templates, and a guided wizard.

### 4.3 Phase 3: Plugin Architecture with Agent Registry (v5.0--v6.5, Jan 25--28)

```
.claude-plugin/
  └── marketplace.json
skills/
  ├── research-coordinator/SKILL.md
  ├── a1/SKILL.md
  ├── a2/SKILL.md
  └── ... (40+ agent skills)
agents/
  ├── a1.md  (Task tool registration)
  └── ... (40 agent definitions)
```

Separated skill definitions (for `/diverga:a1` invocation) from agent definitions (for `Task(subagent_type="diverga:a1")` invocation).

### 4.4 Phase 4: Memory System + HUD (v7.0--v8.0, Feb 3--4)

```
lib/
  ├── memory/src/         (15 Python modules)
  └── hud/                (TypeScript HUD system)
.research/
  ├── project-state.yaml
  ├── decision-log.yaml
  ├── checkpoints.yaml
  ├── baselines/
  └── changes/
```

Added persistent state management and a visual progress display.

### 4.5 Phase 5: MCP-First Architecture (v8.2--v9.0, Feb 12--16)

```
mcp/
  ├── diverga-server.js        (unified entry, 16 tools)
  ├── lib/
  │    ├── tool-registry.js    (tool dispatch)
  │    ├── checkpoint-logic.js (core logic)
  │    ├── sqlite-state.js     (SQLite backend)
  │    ├── messaging.js        (agent-to-agent)
  │    └── prereq-checker.mjs  (shared prerequisites)
  ├── servers/
  │    ├── checkpoint-server.js
  │    ├── memory-server.js
  │    └── comm-server.js
  └── journal-server.js        (OpenAlex/Crossref, 6 tools)
hooks/
  ├── hooks.json               (PreToolUse configuration)
  ├── checkpoint-enforcer.mjs  (Task interceptor)
  └── skill-interceptor.mjs    (Skill interceptor)
```

The Python memory system was entirely replaced by MCP servers. State moved to SQLite (WAL mode) for ACID-safe parallel operations.

### 4.6 Phase 6: Consolidated Architecture (v11.0--v12.0, Mar 10--19)

```
skills/                        (24 core + 5 arena + utilities)
agents/                        (24 agent definitions)
mcp/
  ├── diverga-server.js       (16 tools, SQLite-only)
  └── journal-server.js       (6 tools)
hooks/
  └── prereq-enforcer.mjs     (unified hook)
config/
  └── agents.json             (SSoT for all agents)
docs/
  ├── CHECKPOINT-RULES.md     (extracted from CLAUDE.md)
  ├── ARCHITECTURE.md
  └── MCP-TOOLS.md
CLAUDE.md                     (<5KB, minimal per-session load)
```

Removed Codex CLI, OpenCode, YAML backend, and redundant skill layers. Single platform, single backend, minimal token overhead.

---

## 5. Human Checkpoint System Evolution

### 5.1 v1.0--v2.0: Behavioral Checkpoints (January 22)

Checkpoints existed only as instructions in SKILL.md files. The LLM was *told* to pause, but nothing enforced it. Compliance depended entirely on the model following instructions.

### 5.2 v3.0: AskUserQuestion Pattern (January 23)

Formalized the use of Claude Code's `AskUserQuestion` tool for checkpoints. This provided structured UI elements (clickable options) rather than free-text questions, making checkpoints more reliable.

### 5.3 v6.0: Mandatory Halt (January 25)

The Clean Slate Edition made all REQUIRED checkpoints mandatory halts. The language shifted from declarative ("I will proceed") to interrogative ("May I proceed?"). This was a philosophical commitment, not a technical enforcement.

### 5.4 v7.0: Checkpoint Auto-Trigger + Persistence (February 3)

Three-tier checkpoint levels introduced:
- RED (REQUIRED): Must complete before proceeding
- ORANGE (RECOMMENDED): Strongly suggested
- YELLOW (OPTIONAL): Can skip with defaults

17 standard checkpoints defined. Checkpoint state persisted to YAML files across sessions.

### 5.5 v8.1: Enforcement Strengthening (February 9)

- Text-based questions no longer counted as checkpoint compliance
- Agent Prerequisite Map established with dependency ordering
- No-skip policy for REQUIRED checkpoints
- Multi-agent coordination: parallel agents must clear all prerequisites first

### 5.6 v8.2: MCP Runtime Enforcement (February 12)

Shift from prompt-level to runtime enforcement:
- `diverga_check_prerequisites(agent_id)` called before agent execution
- Override Refusal template presented instead of text refusal
- Fallback to `.research/decision-log.yaml` if MCP unavailable
- 56 unit tests for enforcement

### 5.7 v10.1.0: Humanization Pipeline Checkpoints (February 23)

Specialized checkpoints for the humanization workflow:
- CP_HUMANIZATION_REVIEW, CP_PASS1_REVIEW, CP_PASS2_REVIEW, CP_PASS3_REVIEW, CP_FINAL_REVIEW
- Rich Checkpoint v2.0 with section-level score tables and 6 response options
- OMC autonomous mode defense (ignores ralph/ultrawork/autopilot hooks during checkpoints)

### 5.8 v10.3.1: Platform Hook Enforcement (February 28)

PreToolUse hooks intercept *every* agent call at the Claude Code platform level:
- `checkpoint-enforcer.mjs` intercepts `Task` tool calls
- `skill-interceptor.mjs` intercepts `Skill` tool calls
- Soft block pattern: always `continue: true` with warning injection
- Shared prereq checker used by both Claude Code and OpenCode hooks

### 5.9 v11.1.0: Hard Block for REQUIRED (March 12)

Reversed the soft-block-only policy for the 5 most critical checkpoints:
- REQUIRED checkpoints: hard block (prevents agent execution)
- RECOMMENDED checkpoints: soft block (warning injection only)
- Debug mode via `DIVERGA_HOOK_DEBUG=1`

---

## 6. VS Methodology Integration

### 6.1 Core VS Framework

Based on arXiv:2510.01171, the Verbalized Sampling methodology assigns **Typicality Scores (T-Scores)** to all recommendations:

| T-Score Range | Interpretation | Diverga Behavior |
|---------------|----------------|-------------------|
| T > 0.8 | Modal (most common) | Flags as "predictable" |
| T 0.5--0.8 | Established alternative | Suggests as balanced choice |
| T 0.3--0.5 | Emerging approach | Recommends for innovation |
| T < 0.3 | Novel/creative | Presents with strong rationale |

### 6.2 Tiered Application (v2.0)

The system implemented three tiers of VS intensity:
- **Full VS (5 phases):** Complete divergent exploration with all creativity mechanisms
- **Enhanced VS (3 phases):** Abbreviated exploration for moderate-stakes decisions
- **Light VS (modal awareness):** Simple flagging of modal recommendations

### 6.3 Creativity Mechanisms (v3.0)

Five mechanisms augmented the base VS methodology:
1. Forced Analogy: cross-domain idea transfer
2. Divergent-Convergent Loop: iterative expansion/contraction
3. Semantic Distance Scorer: quantifying conceptual novelty
4. Temporal Reframing: shifting temporal perspectives
5. Community Simulation: modeling research community reactions

### 6.4 HAVS: Humanization-Adapted VS (v6.5)

A 3-phase specialization for text transformation:
- **Phase 1 (Analysis):** G5 scans text, identifies AI-detectable patterns, assigns T-Scores
- **Phase 2 (Transformation):** G6 applies HAVS with three directions (A/B/C intensity)
- **Phase 3 (Verification):** F5 verifies transformation quality and checks for regression

### 6.5 VS Arena (v11.1.0)

Five epistemological persona agents (V1--V5) engage in multi-agent methodology debate:
- Each persona represents a different epistemological stance
- Agents critique each other's recommendations
- Researcher observes the debate and selects their preferred approach
- Agent Teams enable parallel execution when available

### 6.6 T-Score Calibration (v11.0.0)

Post-consolidation refinements:
- T-Score feedback system for iterative calibration
- Social science database integration for empirical T-Score grounding
- Agent aliases for natural language invocation

---

## 7. Critical Turning Points

### 7.1 The Clean Slate Decision (v6.0, January 25)

The single most important design decision in the project's history. After implementing the Sisyphus Protocol in v5.0, the developer immediately reversed course, stripping out all AI-autonomous behaviors and establishing the foundational principle: "AI works BETWEEN checkpoints, humans decide AT them."

**Evidence:** Commits `dd98cef` (v5.0 Sisyphus) and `b443f53` (v6.0 Clean Slate) occurred on the same day (January 25), suggesting rapid recognition that autonomous AI behavior conflicted with the project's core values.

### 7.2 The Naming Resolution (January 25)

Three name changes in one day (Research Coordinator -> NovaScholar -> Diverga) reflected the project crystallizing its identity. The final name "Diverga" perfectly encodes the VS methodology's purpose: diverging from modal recommendations.

### 7.3 MCP Adoption (v8.2, February 12)

Moving checkpoint enforcement from SKILL.md instructions (prompt-level) to MCP tools (runtime-level) was a paradigm shift. It reduced prompt token overhead by thousands of tokens per agent while providing actual programmatic enforcement instead of relying on LLM compliance.

### 7.4 Plugin Discovery Crisis (v6.9.1, February 2--3)

A 6+ hour debugging session revealed undocumented Claude Code plugin requirements and marketplace caching behaviors. This experience led to the creation of comprehensive installation diagnostics (`/diverga:doctor`) and ultimately influenced the decision to prioritize the Claude Code platform exclusively.

### 7.5 The Great Simplification (v11.0, March 10)

Reducing 44 agents to 24 and dropping cross-platform support was a maturity decision:
- Codex CLI had reached ~75% parity but maintaining it cost significant development effort
- OpenCode had reached ~70% parity but the user base was minimal
- 44 agents with fuzzy boundaries confused researchers more than they helped
- The principle: "Do one thing well" (Claude Code with 24 focused agents) over "do everything adequately" (3 platforms with 44 overlapping agents)

### 7.6 Token Budget Awareness (v12.0, March 19)

The realization that CLAUDE.md's 16.8KB was loaded into *every* Claude Code session, consuming ~4,200 tokens before any work began. This led to aggressive content extraction, reducing the per-session overhead to ~1,250 tokens. A lesson in the hidden costs of context injection.

---

## 8. Current State (v12.0)

### 8.1 Architecture Summary

Diverga v12.0 is a **Claude Code plugin** providing 24 specialized research agents orchestrated by a unified system:

- **24 core agents** in 9 categories (A, B, C, D, E, F, G, I, X)
- **5 VS Arena persona agents** (V1--V5) for epistemological debate
- **MCP server stack**: diverga-server (16 tools), journal-server (6 tools), humanizer (4+ tools)
- **SQLite backend** (WAL mode) for all state management
- **PreToolUse hooks** for checkpoint enforcement
- **Bilingual support** (English + Korean)

### 8.2 Key Metrics

| Metric | Value |
|--------|-------|
| Total agents | 24 core + 5 arena = 29 |
| MCP tools | 26+ (16 diverga + 6 journal + 4+ humanizer) |
| Checkpoints | 17 standard + 5 SCH + 5 humanization |
| Test count | 170+ (v11.1.0 architecture) |
| CLAUDE.md size | <5KB (~1,250 tokens) |
| Development span | 57 days (Jan 22 -- Mar 19, 2026) |
| Total commits | 224 |

### 8.3 Design Principles (Evolved)

1. **Human decisions remain with humans.** AI handles what is beyond human scope.
2. **Diverge from the modal.** VS methodology ensures creative, defensible alternatives.
3. **Enforce, don't suggest.** REQUIRED checkpoints physically prevent agent execution.
4. **Minimize token overhead.** Only essential context loaded per session; reference docs on demand.
5. **Single platform excellence over multi-platform mediocrity.**

### 8.4 Target Domains

Education, Psychology, Management, Sociology, HRD, Communication, and other social science disciplines where research methodology decisions benefit from creative divergence and rigorous human oversight.

---

## Appendix A: Version-Date-Commit Reference

| Version | Date | Key Commit | Summary |
|---------|------|------------|---------|
| v1.0.0 | 2026-01-22 | `312bd97` | Initial 20 agents |
| v2.0.0 | 2026-01-22 | `6ab488e` | VS methodology integration |
| v3.0.0 | 2026-01-23 | `4981c2a` | Creativity suite, modular architecture |
| v4.0.0 | 2026-01-25 | `91f77b0` | Context persistence, wizard, English base |
| v5.0.0 | 2026-01-25 | `dd98cef` | Sisyphus Edition, 33 agents, qualitative |
| v6.0.0 | 2026-01-25 | `b443f53` | Clean Slate, human-centered redesign |
| v6.4.0 | 2026-01-27 | `be23b5f` | Plugin Marketplace, 40 agents |
| v6.7.0 | 2026-01-30 | (area) | Category I, 44 agents |
| v7.0.0 | 2026-02-03 | `c07d180` | Memory system, 3-layer context |
| v8.0.0 | 2026-02-04 | `a401d8f` | HUD, natural language init |
| v8.2.0 | 2026-02-12 | `e10edc5` | MCP checkpoint enforcement |
| v9.0.0 | 2026-02-16 | `b0eb4dd` | SQLite + 3-server split |
| v10.0.0 | 2026-02-23 | `ad19875` | Discourse-level detection |
| v10.3.1 | 2026-02-28 | `064c11a` | Platform hook enforcement |
| v11.0.0 | 2026-03-10 | `73f0e92` | 44->24 agents, Claude Code exclusive |
| v11.1.0 | 2026-03-12 | `40d15f5` | VS Arena, hard block enforcement |
| v12.0.0 | 2026-03-19 | `305ecc3` | Unified orchestrator, slim CLAUDE.md |

## Appendix B: Agent Count Evolution

```
v1.0  (Jan 22): 20 agents, 5 categories (A-E)
v2.0  (Jan 22): 20 agents, 5 categories (A-E) + VS tiers
v3.0  (Jan 23): 20 agents + creativity mechanisms
v3.1  (Jan 24): 21 agents (+ Visualizer)
v5.0  (Jan 25): 33 agents, 8 categories (A-H)
v6.0  (Jan 25): 27 agents, 8 categories (A-H, consolidated)
v6.4  (Jan 27): 40 agents, 8 categories (A-H, expanded)
v6.7  (Jan 30): 44 agents, 9 categories (A-I)
v11.0 (Mar 10): 24 agents, 9 categories (A-I + X)
v11.1 (Mar 12): 24 core + 5 arena (V1-V5) = 29
v12.0 (Mar 19): 24 core + 5 arena = 29 (unified orchestrator)
```

## Appendix C: Name Evolution

| Date | Name | Rationale | Commit |
|------|------|-----------|--------|
| Jan 22 | Research Coordinator | Descriptive of function | `312bd97` |
| Jan 25 | NovaScholar | VS as core value; "Beyond Modal" | `68951c0` |
| Jan 25 | Diverga | Divergent thinking identity; prior name taken | `04724ba` |

---

*Document generated from 224 commits spanning January 22 -- March 19, 2026. All commit hashes, dates, and quotes are sourced directly from the Git repository at `/Volumes/External SSD/Projects/Diverga/Diverga-core`.*
