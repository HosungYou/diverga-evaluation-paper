# EDR Cycle Analysis of Diverga Development

Based on complete git history analysis of `Diverga-core` (153 commits, 2026-01-22 to 2026-03-19).

Methodology: McKenney & Reeves (2012) Educational Design Research framework with three phases per cycle: Analysis/Exploration, Design/Construction, Evaluation/Reflection.

---

## 1. Five Design Cycles (with Commit Evidence)

### Cycle 1: Initial Agent Design and VS Integration (v1.0--v2.0)

**Period:** 2026-01-22 to 2026-01-23 (2 days)

**Analysis/Exploration:**
- Started from a need for a multi-agent research assistant system for social science researchers using Claude Code's Skills platform.
- Initial commit (`312bd97`, 2026-01-22) established 20 specialized research agents organized in 5 categories (A through E), with Korean/English documentation.
- Trigger: Recognition that LLM-based research assistants default to "modal" (most common) recommendations, lacking creative or divergent thinking.

**Design/Construction:**
- v1.0: 20 agents with master coordinator skill, auto-trigger system, parallel execution support (`312bd97`).
- v2.0: Integration of Verbalized Sampling (VS) methodology from arXiv:2510.01171 across all 20 agents (`6ab488e`, 2026-01-22).
  - Tiered VS application: Full VS (5 phases) for 5 agents, Enhanced VS (3 phases) for 6 agents, Light VS (modal awareness) for 9 agents.
  - T-Score (Typicality Score) system introduced for measuring recommendation diversity.
- Claude Code marketplace integration (`a6ea631`, `0a60be1`).

**Evaluation/Reflection:**
- Marketplace schema compatibility issues required fixes (`a6ea631`).
- Installation guide was overly complex; simplified in v2.1.0 (`50d4387`).
- Recognized need for deeper architectural foundations, including modular creativity mechanisms.

**Outcome leading to Cycle 2:** The monolithic VS integration lacked modularity. Creativity mechanisms were embedded but not independently activatable. The system needed a modular creativity suite and more sophisticated interaction patterns.

**Key commits:**
| Hash | Date | Description |
|------|------|-------------|
| `312bd97` | 2026-01-22 | Initial commit: 20 agents |
| `6ab488e` | 2026-01-22 | VS methodology integration (v2.0.0) |
| `a6ea631` | 2026-01-23 | Marketplace compatibility fix |
| `50d4387` | 2026-01-23 | Installation simplification |

---

### Cycle 2: Creativity Suite, Rapid Versioning, and Clean Slate Transition (v3.0--v6.0)

**Period:** 2026-01-23 to 2026-01-25 (3 days)

**Analysis/Exploration:**
- v3.0 design document and analysis report created (`e85e05d`, 2026-01-23), identifying the need for five discrete creativity mechanisms.
- Recognition that VS alone was insufficient; creativity needed to be modular and composable.

**Design/Construction (v3.0):**
- Modular creativity suite with 5 mechanisms (`dee6766` through `f7a49f8`, all 2026-01-23):
  - Forced Analogy (`dee6766`)
  - Iterative Divergent-Convergent Loop (`e4ecda9`)
  - Semantic Distance Scorer (`18c9732`)
  - Temporal Reframing (`4e312ba`)
  - Community Simulation (`f7a49f8`)
- VS Engine v3.0 with checkpoints and iteration (`4981c2a`).
- Dynamic T-Score system with API integration (`21899c3`).
- All 20 agents upgraded across three tiers: FULL (5), ENHANCED (6), LIGHT (9) (`28d188d`, `be95ce2`, `76328be`).
- Agent 21: Conceptual Framework Visualizer with Nanobanana (Gemini API) integration (`7caeda3`, `0ae63e6`).

**Design/Construction (v4.0):**
- Complete architecture restructure with context persistence (`91f77b0`, 2026-01-25).
- VS Engine simplified from 14 checkpoints to 3-stage process.
- Agents reorganized into 3-tier structure (Flagship/Core/Support).
- Language switched to English base with Korean input support.

**Design/Construction (v5.0, Sisyphus Edition):**
- Major expansion: 21 to 33 agents (`dd98cef`, 2026-01-25).
- New categories: D (Data Collection, D1-D4) and H (Specialized Approaches, H1-H2).
- **Sisyphus Protocol** introduced: continuation enforcement until verified completion.
- **Iron Law of Continuation**: "agent OR checkpoint" forced behavior.
- Paradigm Auto-Detection (quantitative/qualitative/mixed methods).

**Evaluation/Reflection:**
- The Sisyphus Protocol was immediately recognized as problematic: it removed human control, making AI autonomous between checkpoints.
- The project name was changed twice in rapid succession:
  - "Research Coordinator" to "NovaScholar" (`68951c0`) because VS methodology needed branding as core value.
  - "NovaScholar" to "Diverga" (`04724ba`) because "NovaScholar already exists."
- The OMC autonomous modes (ralph, ultrawork, autopilot, ecomode) and Sisyphus Protocol conflicted with the core design principle that humans should remain in control.

**Outcome leading to Cycle 3:** v6.0.0 "Clean Slate Edition" (`b443f53`, 2026-01-25) was a deliberate reset. It removed the Sisyphus Protocol, Iron Law of Continuation, and OMC autonomous modes while strengthening the human checkpoint system. This was the first major design failure and correction, establishing the principle: "AI works BETWEEN checkpoints, humans decide AT them."

**Key commits:**
| Hash | Date | Description |
|------|------|-------------|
| `e85e05d` | 2026-01-23 | v3.0 design document |
| `dee6766`--`f7a49f8` | 2026-01-23 | Five creativity mechanisms |
| `91f77b0` | 2026-01-25 | v4.0 architecture restructure |
| `dd98cef` | 2026-01-25 | v5.0 Sisyphus Edition (33 agents) |
| `68951c0` | 2026-01-25 | Rename to NovaScholar |
| `04724ba` | 2026-01-25 | Rename to Diverga |
| `b443f53` | 2026-01-25 | v6.0.0 Clean Slate (Sisyphus removed) |

---

### Cycle 3: Expansion to 44-Agent Peak (v6.0--v6.7)

**Period:** 2026-01-25 to 2026-02-04 (10 days)

**Analysis/Exploration:**
- After the Clean Slate reset, the system stabilized at 27 agents with a human-centered checkpoint philosophy.
- Category-based naming adopted (A1, B2, etc.) replacing numbered agents (`7311778`, v6.0.1).
- Identified domain-specific gaps: meta-analysis pipeline, humanization, systematic review automation.

**Design/Construction:**
- v6.2.0: Agent orchestration guide and B5 documentation (`426680c`, 2026-01-26).
- v6.3.0: Multi-Gate Validation Pipeline for meta-analysis; 3 new agents C5/C6/C7 bringing total to 40 (`d936617`, `e89dd1f`, 2026-01-26). Based on "V7 GenAI meta-analysis lessons learned."
- v6.4.0: Plugin Marketplace Edition with auto-trigger dispatch (`be23b5f`, 2026-01-27). Added `/diverga:setup` wizard and `/diverga:help`.
- v6.5.0: `/agents/` directory for Task tool parallel execution (`b23c80b`, 2026-01-27). 40 agent `.md` files for programmatic invocation.
- v6.6.0--6.6.3: Cross-platform support for Codex CLI and OpenCode (`546419f`, 2026-01-28). Model mapping (opus/sonnet/haiku to o1/gpt-4/gpt-3.5-turbo). Extensive QA testing (QUAL and QUANT scenarios).
- v6.7.0: Category I systematic review automation with 4 new agents (I0-I3), reaching **44 agents** (`0aa61f5`, 2026-01-30).
- v6.8.0--v6.9.x: DIVERGA Memory System for persistent context (`a24c5b7`, 2026-02-01). Multiple plugin discovery and compatibility fixes.

**Evaluation/Reflection:**
- Task tool agent recognition failed; required moving skills to root (`37ea4fe`, v6.5.2).
- ESM/CommonJS conflicts with Codex CLI (`b0eee65`).
- Plugin discovery was brittle: 8 consecutive fix commits on 2026-02-02 (`439619f` through `efc024a`) addressing skill names, paths, version fields, and orphaned directories.
- Marketplace cache synchronization issues (`f5d38bc`, v6.9.2).
- Agent count reached peak (44) but cross-platform maintenance burden became evident (Claude Code 100%, Codex CLI ~75%, OpenCode ~70% compatibility).

**Outcome leading to Cycle 4:** The 44-agent system worked but had significant maintenance overhead. Cross-platform support (3 platforms) multiplied complexity. Plugin/skill discovery was fragile. The memory system (v7.0, v8.0) added further complexity. This set the stage for the "great consolidation" in v11.0.

**Key commits:**
| Hash | Date | Description |
|------|------|-------------|
| `7311778` | 2026-01-25 | Category-based naming (v6.0.1) |
| `e89dd1f` | 2026-01-26 | C5/C6/C7 meta-analysis agents (40 total) |
| `be23b5f` | 2026-01-27 | Plugin Marketplace Edition (v6.4) |
| `546419f` | 2026-01-28 | Cross-platform support (v6.6.0) |
| `0aa61f5` | 2026-01-30 | Category I agents (44 total, v6.7.0) |
| `a24c5b7` | 2026-02-01 | Memory System (v6.8.0) |
| `439619f`--`efc024a` | 2026-02-02 | 8 plugin discovery fixes |

---

### Cycle 4: The Great Consolidation (v8.0--v11.0)

**Period:** 2026-02-04 to 2026-03-10 (34 days)

**Analysis/Exploration:**
- v8.0 through v10.3 represented infrastructure maturation: MCP checkpoint enforcement, SQLite backend, Agent Teams pilot, humanization pipeline.
- The system grew to 44 agents across 9 categories on 3 platforms, with a 59KB CLAUDE.md.
- Key insight: most agents were rarely used; some had overlapping responsibilities.
- Cross-platform parity was expensive: Codex CLI and OpenCode required constant adaptation work.
- Hardcoded user paths in hooks caused silent failures for other users (`c1c11f6`, v10.3.2).

**Design/Construction (Infrastructure, v8.0--v10.3):**
- v8.0: Project Visibility and HUD Enhancement (`a401d8f`, 2026-02-04).
- v8.1.0: Checkpoint Enforcement Strengthening with mandatory AskUserQuestion (`0de04a1`, 2026-02-09).
- v8.2.0: MCP Runtime Checkpoint Enforcement; 7 MCP tools; removed 104 unused Python files from lib/memory/ (`e10edc5`, 2026-02-12).
- v8.3.0: Cross-Platform Migration with 47 individual Codex CLI SKILL.md files (`3bd4a6d`, 2026-02-12).
- v8.5.0: Developer Experience and Agent Teams Pilot; agents.json as Single Source of Truth (`eefb04c`, 2026-02-15).
- v9.0: TDD-driven architecture rewrite (317/317 tests); SQLite + YAML dual backend; 16 MCP tools across 3 servers (`e1ae732`, `81f06bc`, `4c034ab`, 2026-02-15).
- v9.1--v9.2: Humanization Pipeline v2.0 with MCP tool integration; zero-setup MCP auto-registration (`8566955`, `d369f5b`, `3a7048c`, 2026-02-22--23).
- v10.0: Discourse-level detection and 4-layer humanization pipeline (`ad19875`, 2026-02-23).
- v10.1.1: Typographic enforcement; Zotero MCP removal (`c9c6b62`, 2026-02-23).
- v10.3.0: Journal Intelligence MCP with OpenAlex integration (`cac396d`, 2026-02-23).
- v10.3.1: Platform hook enforcement with PreToolUse hooks (`064c11a`, 2026-02-28).

**Design/Construction (The Consolidation, v11.0):**
- v11.0.0 (`73f0e92`, 2026-03-10): **Major simplification: 44 to 24 agents.**
  - Removed Codex CLI and OpenCode platform support entirely (Claude Code exclusive).
  - Removed YAML/JSON backend; SQLite WAL is the only backend.
  - CLAUDE.md reduced from 59KB to 12KB (79% reduction).
  - 20 agents removed via consolidation:
    - A3 (Devil's Advocate) + A6 (Visualizer) merged into A2
    - A4 (Ethics) + F4 (Bias Detection) merged into new X1 (Research Guardian)
    - B3 (Effect Size) + C6 (Data Guard) + C7 (Error Prevention) merged into C5
    - B4 (Research Radar) removed entirely (low value)
    - B5 (PDF Processor) merged into I3
    - C4 (Materials) + D1 (Sampling) merged into C1
    - D3 (Observation) merged into D2
    - E4 (Code Gen) merged into E1; E5 (Sensitivity) split into C5+E1
    - F1 (Consistency) + F2 (Checklist) + F3 (Reproducibility) merged into G2
    - G3 (Peer Review) + G4 (Pre-registration) merged into G2
    - H1 (Ethnography) + H2 (Action Research) merged into C2
  - Unified hooks: two separate enforcer scripts merged into one (prereq-enforcer.mjs).
  - MCP servers reduced: 4 to 3 (context7 moved to global config).

**Evaluation/Reflection:**
- Post-release fix for stale references (`a418bc8`, 2026-03-10).
- Hook matcher used wrong tool name ("Task" instead of "Agent") requiring fix (`6846b47`, 2026-03-12).
- T-Score calibration needed empirical grounding; added OpenAlex frequency lookup and feedback system (`4c0958f`, `6caeead`, 2026-03-10).
- Agent aliases (83 aliases in `agent-aliases.json`) added to maintain backward compatibility.
- Humanizer repositioned from "AI detection bypass" to "academic writing quality improvement" for ethical framing.

**Outcome leading to Cycle 5:** The consolidation successfully reduced complexity, but exposed new issues: the hook enforcement system was fragile, the VS Arena concept (multi-agent debate) was not yet integrated, and the setup wizard needed redesign.

**Key commits:**
| Hash | Date | Description |
|------|------|-------------|
| `e10edc5` | 2026-02-12 | MCP Runtime Checkpoint Enforcement |
| `e1ae732` | 2026-02-15 | v9.0 architecture (317 tests) |
| `ad19875` | 2026-02-23 | v10.0 discourse-level humanization |
| `064c11a` | 2026-02-28 | Platform hook enforcement |
| `73f0e92` | 2026-03-10 | v11.0.0: 44 to 24 agents |
| `6846b47` | 2026-03-12 | Hook matcher fix ("Task" to "Agent") |
| `4c0958f` | 2026-03-10 | Humanizer ethical repositioning |

---

### Cycle 5: Stabilization, VS Arena, and Architecture Slimming (v11.1--v12.0)

**Period:** 2026-03-12 to 2026-03-19 (7 days)

**Analysis/Exploration:**
- After the v11.0 consolidation, the system needed new features built on the simplified foundation.
- VS Arena (epistemological debate between methodology personas) was identified as a key differentiator.
- CLAUDE.md was still 16.8KB, loaded every session; token cost was a concern.
- Multiple orchestration skills (research-orchestrator, vs-arena) created redundancy.

**Design/Construction:**
- v11.1.0: VS Arena with 5 epistemological persona agents (V1-V5); deleted ~30 stale files; rewrote prereq-enforcer.mjs; 170 tests across 7 test files (`40d15f5`, 2026-03-12).
- v11.1.1: latex2omml integration for LaTeX-to-Word OMML conversion (`5083053`, 2026-03-13).
- v11.1.2: Setup wizard fix, first-run detection, symlink dev guide (`1d6f95d`, 2026-03-13).
- v11.3.0: Dev mode (selective symlinks), deploy pipeline, Agent Teams integration into VS Arena (`9b8e52e`, 2026-03-14). Three collaboration modes: Agent Teams + VS Arena / Subagents + Classic VS / Disabled.
- v12.0.0 (2026-03-19):
  - Extracted checkpoint rules, architecture, and MCP tools from CLAUDE.md (`e948e1d`); slimmed from 16.8KB to less than 5KB.
  - Deleted legacy routing.yaml (33-agent v6.0 era) and UPGRADE_ROADMAP.md (v8.0.1 era) (`da2c6f1`).
  - Created unified `/diverga:orchestrator` skill replacing both research-orchestrator and vs-arena (`cb3602e`).
  - Slimmed research-coordinator SKILL.md from 28KB to ~14KB (`35074f6`).
  - Removed research-orchestrator and vs-arena skills (`856af2b`); breaking change.
  - Merged Agent Teams + VS Arena into setup Step 4 (`935e726`).

**Evaluation/Reflection:**
- Hook portability issues fixed: `${CLAUDE_PLUGIN_ROOT}` for portable hook commands (`c677b4e`).
- Plugin hooks duplication and version sync issues resolved (`2a21214`).
- Deploy script ordering bug fixed: package.json must update before version sync (`6bbefd9`).
- The system reached a stable state with 24 core agents + 5 VS Arena agents = 29 total, 34 skills, and a lean CLAUDE.md (~1,250 tokens per session vs. ~4,200 previously).

**Outcome:** A stabilized, architecturally lean system with clear separation of concerns. The single orchestrator skill provides a unified entry point. Legacy artifacts have been removed. The system is ready for user evaluation studies.

**Key commits:**
| Hash | Date | Description |
|------|------|-------------|
| `40d15f5` | 2026-03-12 | v11.1.0: VS Arena + cleanup |
| `5083053` | 2026-03-13 | latex2omml integration |
| `9b8e52e` | 2026-03-14 | v11.3.0: dev mode, deploy, Agent Teams |
| `e948e1d` | 2026-03-19 | CLAUDE.md extraction (16.8KB to <5KB) |
| `cb3602e` | 2026-03-19 | Unified orchestrator skill |
| `856af2b` | 2026-03-19 | Remove redundant skills |
| `305ecc3` | 2026-03-19 | v12.0.0 version bump |

---

## 2. Design Failures and Removals (with Rationale)

### 2.1 Sisyphus Protocol and Iron Law of Continuation

| Aspect | Detail |
|--------|--------|
| **Feature** | Sisyphus Protocol: "work never stops until complete"; Iron Law of Continuation: "agent OR checkpoint" (AI must either invoke an agent or a checkpoint at every turn) |
| **Added** | `dd98cef`, 2026-01-25, v5.0.0 (Sisyphus Edition) |
| **Removed** | `b443f53`, 2026-01-25, v6.0.0 (Clean Slate Edition) -- same day |
| **Rationale** | Violated human-centered design principle. Removed human control over research process. The system proceeded autonomously between checkpoints without waiting for user confirmation. Commit message: "AI works BETWEEN checkpoints, humans decide AT them." |
| **Significance** | Fastest design failure in the project: added and removed within hours. Established the foundational design principle that guided all subsequent development. |

### 2.2 OMC Autonomous Modes

| Aspect | Detail |
|--------|--------|
| **Feature** | Four autonomous execution modes: ralph, ultrawork, autopilot, ecomode |
| **Added** | Pre-v5.0.0 (part of OMC, "Oh My ClaudeCode," framework integration) |
| **Removed** | `b443f53`, 2026-01-25, v6.0.0 |
| **Rationale** | Autonomous modes contradicted the checkpoint-based human control system. All modes removed in the Clean Slate reset. |

### 2.3 Project Name Changes

| Aspect | Detail |
|--------|--------|
| **Feature** | Project name: "Research Coordinator" then "NovaScholar" |
| **Renamed to NovaScholar** | `68951c0`, 2026-01-25 ("VS methodology as core value") |
| **Renamed to Diverga** | `04724ba`, 2026-01-25 ("NovaScholar already exists") |
| **Rationale** | The first rename aimed to brand VS as core innovation. The second was forced by name collision. Final name "Diverga" emphasizes "divergent thinking and breaking free from modal recommendations." |

### 2.4 Codex CLI and OpenCode Platform Support

| Aspect | Detail |
|--------|--------|
| **Feature** | Full cross-platform support for Codex CLI (OpenAI) and OpenCode, with model mapping, adapters, installers, and per-platform SKILL.md files |
| **Added** | `546419f`, 2026-01-28, v6.6.0. Expanded significantly in v8.3.0 (`3bd4a6d`, 2026-02-12) with 47 individual Codex CLI SKILL.md files |
| **Removed** | `73f0e92`, 2026-03-10, v11.0.0. Directories `.codex/`, `.opencode/`, `adapters/` entirely deleted |
| **Rationale** | Platform compatibility was 75% (Codex) and 70% (OpenCode) versus 100% for Claude Code. Maintaining three platforms multiplied maintenance burden. ESM/CommonJS conflicts required workarounds. The decision made Diverga "Claude Code exclusive." |
| **Duration** | 41 days (Jan 28 to Mar 10) |

### 2.5 Nanobanana (Gemini API) Integration

| Aspect | Detail |
|--------|--------|
| **Feature** | Agent 21 (Conceptual Framework Visualizer) used ASCII Blueprint to Nanobanana (Gemini API) workflow for framework visualization |
| **Added** | `0ae63e6`, 2026-01-25 |
| **Removed** | Effectively removed in v11.0.0 when A6 (Visualizer) was merged into A2 |
| **Rationale** | External API dependency for a niche use case. The visualizer functionality was consolidated rather than maintained as a standalone agent. |

### 2.6 Twenty Agents Removed in Great Consolidation

| Removed Agent(s) | Merged Into | Rationale |
|---|---|---|
| A3 (Devil's Advocate) + A6 (Visualizer) | A2 | Overlapping critical analysis functions |
| A4 (Ethics) + F4 (Bias Detection) | New X1 (Research Guardian) | Both serve research integrity; unified guardian role |
| B3 (Effect Size) + C6 (Data Guard) + C7 (Error Prevention) | C5 | All serve meta-analysis validation; C5 already orchestrated them |
| B4 (Research Radar) | Removed entirely | "Low value" per commit message |
| B5 (PDF Processor) | I3 | RAG builder already handles document ingestion |
| C4 (Materials) + D1 (Sampling) | C1 | Design-adjacent functions consolidated |
| D3 (Observation) | D2 | Data collection methods consolidated |
| E4 (Code Gen) | E1 | Analysis code is part of analysis |
| E5 (Sensitivity) | Split into C5 + E1 | Meta-analysis sensitivity in C5; general analysis in E1 |
| F1 (Consistency) + F2 (Checklist) + F3 (Reproducibility) | G2 | Quality assurance functions merged into publication specialist |
| G3 (Peer Review) + G4 (Pre-registration) | G2 | Publication workflow consolidated |
| H1 (Ethnography) + H2 (Action Research) | C2 | Qualitative methods consolidated |

All removals in commit `73f0e92`, 2026-03-10.

### 2.7 lib/memory/ Python Module (104 Files)

| Aspect | Detail |
|--------|--------|
| **Feature** | Python-based memory system with SQLite, embeddings, CLI, hooks |
| **Added** | `a24c5b7`, 2026-02-01, v6.8.0 (32 files initially, grew through v7.0/v8.0) |
| **Removed** | `e10edc5`, 2026-02-12, v8.2.0 (104 files removed) |
| **Rationale** | Replaced by MCP-based architecture. The Python code was "design reference only" per commit message. MCP tools provided the same functionality through standardized tool protocol. |
| **Duration** | 11 days |

### 2.8 YAML/JSON Backend

| Aspect | Detail |
|--------|--------|
| **Feature** | YAML-based state management; dual YAML + SQLite backend in v9.0 |
| **Added** | Original architecture (v1.0+); dual backend added `4c034ab`, 2026-02-15 |
| **Removed** | `73f0e92`, 2026-03-10, v11.0.0 (SQLite WAL is sole backend) |
| **Rationale** | Dual backends created synchronization complexity. SQLite WAL provided better concurrency, simpler state management, and was already the de facto primary. |

### 2.9 Zotero MCP Server

| Aspect | Detail |
|--------|--------|
| **Feature** | Zotero bibliography manager MCP integration |
| **Added** | Part of MCP server configuration (pre-v10.1.1) |
| **Removed** | `c9c6b62`, 2026-02-23, v10.1.1 |
| **Rationale** | Removed from `.mcp.json` (3 servers remain). Likely due to limited usage or reliability concerns. |

### 2.10 context7 MCP Server

| Aspect | Detail |
|--------|--------|
| **Feature** | context7 MCP server for plugin context |
| **Removed from plugin** | `73f0e92`, 2026-03-10, v11.0.0 |
| **Rationale** | Moved to user's global MCP configuration rather than removed entirely. Not plugin-specific. |

### 2.11 research-orchestrator and vs-arena Skills

| Aspect | Detail |
|--------|--------|
| **Feature** | Separate `/diverga:research-orchestrator` and `/diverga:vs-arena` skills |
| **Added** | research-orchestrator: original architecture; vs-arena: `40d15f5`, 2026-03-12, v11.1.0 |
| **Removed** | `856af2b`, 2026-03-19, v12.0.0 |
| **Rationale** | Replaced by unified `/diverga:orchestrator` (`cb3602e`) that handles both Agent Teams lifecycle and VS Arena debate. Eliminates redundancy. |
| **Duration** | vs-arena existed 7 days before consolidation |

### 2.12 Legacy routing.yaml and UPGRADE_ROADMAP.md

| Aspect | Detail |
|--------|--------|
| **Feature** | 33-agent routing configuration (v6.0 era); v8.0.1 upgrade roadmap |
| **Removed** | `da2c6f1`, 2026-03-19 |
| **Rationale** | routing.yaml referenced pre-consolidation 33 agents while agents.json was the SSoT since v11.0. UPGRADE_ROADMAP.md was a v8.0.1 era document referencing 44 agents for a "never-released v8.1.0" (the actual v8.1.0 was Checkpoint Enforcement, not the roadmap's planned release). |

### 2.13 Stale Files (~30 files deleted in v11.1.0)

| Aspect | Detail |
|--------|--------|
| **Feature** | Old SDDs, release notes, checkpoint templates, B5 docs, dist/, internal/ directories |
| **Removed** | `40d15f5`, 2026-03-12, v11.1.0 |
| **Rationale** | Accumulated documentation debt from rapid iteration. "Part 1: Cleanup" in commit message. |

### 2.14 Typographic Rules Reversal (Em Dash Enforcement then Prohibition)

| Aspect | Detail |
|--------|--------|
| **Feature** | v10.1.1 (`c9c6b62`, 2026-02-23) enforced Unicode em dashes and smart quotes across G5/G6/F5 humanization agents |
| **Reversed** | User preference established to *never* use em dashes (U+2014) in any output. The typographic rules in humanization agents were subsequently adjusted to match this preference. |
| **Significance** | Illustrates tension between "what makes text look polished" and "what the user/researcher actually wants." |

---

## 3. Platform-Design Co-evolution Events

### 3.1 Claude Code Skills System (v1.0, 2026-01-22)

- **Platform feature:** Claude Code Skills (SKILL.md files) for persistent agent instructions.
- **Design response:** Entire architecture built on SKILL.md as the agent definition format. Master coordinator skill with auto-trigger patterns.
- **Commits:** `312bd97`, `6ab488e`

### 3.2 Claude Code Marketplace (v2.0--v2.1, 2026-01-23)

- **Platform feature:** Claude Code plugin marketplace for distributing skill bundles.
- **Design response:** marketplace.json schema integration; single plugin install for all 21 skills.
- **Commits:** `a6ea631`, `0a60be1`
- **Friction:** Schema compatibility required fixes; installation guide had to be simplified.

### 3.3 Task Tool for Parallel Agent Execution (v6.5, 2026-01-27)

- **Platform feature:** Claude Code's Task tool (subagent invocation via `Task(subagent_type="diverga:a1")`).
- **Design response:** Created `/agents/` directory with 40 `.md` files for Task tool registration.
- **Commits:** `b23c80b`, `37ea4fe`
- **Friction:** Task tool could not auto-discover agents in `.claude/skills/`; required moving skills to root. Explicit `skills[]` key in marketplace.json prevented `/agents/` auto-scanning.

### 3.4 Codex CLI Compatibility (v6.6, 2026-01-28)

- **Platform feature:** OpenAI Codex CLI and OpenCode as alternative coding assistants.
- **Design response:** Shared core library, CLI adapters, model mapping (opus to o1), tool mapping (TodoWrite to update_plan).
- **Commits:** `546419f`, `b0eee65`, `2138224`
- **Friction:** ESM/CommonJS module conflicts. Platform parity was never achieved (75%/70%). Eventually abandoned in v11.0.

### 3.5 Plugin Discovery and Skill Loading (v6.8--v6.9, 2026-02-02)

- **Platform feature:** Claude Code's plugin.json-based skill discovery mechanism.
- **Design response:** 8 consecutive fix commits in one day trying to align with undocumented platform requirements.
- **Commits:** `439619f` through `f5d38bc`
- **Friction:** Version fields unsupported then required; skill names must match folder names; skills path format changed. This was the most intense platform-driven iteration in the project.

### 3.6 MCP (Model Context Protocol) Integration (v8.2--v9.0, 2026-02-12 to 2026-02-15)

- **Platform feature:** MCP server protocol for tool registration in Claude Code.
- **Design response:**
  - v8.2.0: MCP checkpoint server with 7 tools, replacing inline checkpoint logic (`e10edc5`).
  - v9.0: 16 MCP tools across 3 servers (checkpoint, memory, communication); SQLite backend (`81f06bc`, `4c034ab`).
  - v9.2.1: `.mcp.json` for zero-setup auto-registration of MCP servers (`c46fb35`, `85564c5`).
- **Significance:** MCP became the primary mechanism for checkpoint enforcement, state management, and inter-agent communication, replacing SKILL.md-embedded logic.

### 3.7 PreToolUse Hooks for Checkpoint Enforcement (v10.3.1, 2026-02-28)

- **Platform feature:** Claude Code's PreToolUse hook system (runs JavaScript before tool invocation).
- **Design response:** `checkpoint-enforcer.mjs` and `skill-interceptor.mjs` hooks that intercept every `diverga:*` agent call to verify checkpoint prerequisites.
- **Commits:** `064c11a`, `6846b47`
- **Friction:** Hook matcher initially used "Task" instead of "Agent" as the tool name. Hardcoded user paths caused silent failures for other users (`c1c11f6`). Required `${CLAUDE_PLUGIN_ROOT}` for portability (`c677b4e`).

### 3.8 Agent Teams (v8.5--v11.3, 2026-02-15 to 2026-03-14)

- **Platform feature:** Claude Code's experimental Agent Teams feature (multi-agent collaboration with TeamCreate/TaskCreate/SendMessage).
- **Design response:**
  - v8.5.0: Pilot with I0 Team Lead mode, 4 team patterns (`eefb04c`, 2026-02-15).
  - v11.1.0: VS Arena built on Agent Teams for multi-agent methodology debate (`40d15f5`, 2026-03-12).
  - v11.3.0: Graceful degradation (fallback to subagent mode when Agent Teams unavailable), setup wizard integration (`b6fbe3d`, `8f65452`, `b7545ad`, 2026-03-14).
  - v12.0.0: Unified orchestrator handles both Agent Teams and subagent modes (`cb3602e`, 2026-03-19).
- **Significance:** Agent Teams enabled the VS Arena concept (real cross-critique between epistemological personas), which was the project's key innovation for multi-perspective methodology debate. The feature's experimental status necessitated graceful degradation architecture.

### 3.9 Humanizer MCP Server (v9.2--v10.0, 2026-02-23)

- **Platform feature:** MCP servers can be distributed via `uvx` (Python package runner) and auto-registered via `.mcp.json`.
- **Design response:** Humanizer MCP server published to GitHub, auto-registered via `uvx` (`3a7048c`). All MCP servers auto-registered via plugin `.mcp.json` (`c46fb35`).
- **Commits:** `d369f5b`, `3a7048c`, `c46fb35`

---

## 4. Summary Timeline

```
Date        Version  Agents  Key Event
----------  -------  ------  -----------------------------------------
2026-01-22  v1.0.0   20      Initial commit: 20 research agents
2026-01-22  v2.0.0   20      VS methodology integration
2026-01-23  v3.0.0   21      Creativity suite (5 mechanisms)
2026-01-25  v4.0.0   21      Architecture restructure, context persistence
2026-01-25  v5.0.0   33      Sisyphus Edition: 12 new agents, Sisyphus Protocol
2026-01-25  v6.0.0   27      Clean Slate: Sisyphus REMOVED, human-centered reset
2026-01-25  v6.0.1   33      Category-based naming (A1-H2)
2026-01-26  v6.3.0   40      Meta-analysis agents (C5/C6/C7) + 4 more
2026-01-27  v6.4.0   40      Plugin Marketplace Edition
2026-01-27  v6.5.0   40      Task tool parallel execution
2026-01-28  v6.6.0   40      Cross-platform: Codex CLI + OpenCode
2026-01-30  v6.7.0   44      Category I (systematic review) -- PEAK
2026-02-01  v6.8.0   44      Memory System
2026-02-04  v8.0.0   44      Project Visibility + HUD
2026-02-09  v8.1.0   44      Checkpoint Enforcement Strengthening
2026-02-12  v8.2.0   44      MCP Runtime Enforcement; lib/memory/ removed
2026-02-15  v9.0.0   44      TDD architecture; SQLite + MCP; 317 tests
2026-02-23  v10.0.0  44      Discourse-level humanization pipeline
2026-02-28  v10.3.1  44      Platform hook enforcement
2026-03-10  v11.0.0  24      GREAT CONSOLIDATION: 44->24, Claude Code only
2026-03-12  v11.1.0  29      VS Arena (5 personas) + cleanup
2026-03-13  v11.1.1  29      latex2omml integration
2026-03-14  v11.3.0  29      Agent Teams integration, dev mode, deploy
2026-03-19  v12.0.0  29      Unified orchestrator; CLAUDE.md <5KB; stable
```

### Agent Count Trajectory

```
44 |                          **********************
   |                         *                      *
40 |              ***********                        *
   |             *                                    *
33 |      *  ****                                      *
   |     * **                                           *
27 |     *                                               *
   |    *                                                 *
24 |                                                       *****
   |
20 | ***
   +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
   v1  v2 v3 v4 v5 v6    v6.3 v6.7      v8-10              v11 v12
```

### Design Principle Evolution

1. **v1.0--v2.0:** "Multi-agent specialization with VS methodology"
2. **v3.0--v5.0:** "Maximize automation and agent coverage" (Sisyphus Protocol)
3. **v6.0:** "AI works BETWEEN checkpoints, humans decide AT them" (correction)
4. **v6.0--v10.3:** "Expand platform reach and feature depth" (44 agents, 3 platforms)
5. **v11.0--v12.0:** "Simplify ruthlessly; depth over breadth" (24 agents, 1 platform)

### Key Metrics

| Metric | Peak | Final (v12.0) |
|--------|------|---------------|
| Agents | 44 (v6.7--v10.3) | 24 core + 5 VS Arena = 29 |
| Platforms | 3 (v6.6--v10.3) | 1 (Claude Code) |
| CLAUDE.md size | 59KB (pre-v11.0) | <5KB |
| MCP servers | 4 (v10.3) | 3 |
| Test count | 317 (v9.0) | 170 (v11.1) |
| Skills | 51 (v7.0) | 34 (v12.0) |

---

*Analysis generated from 153 git commits spanning 2026-01-22 to 2026-03-19.*
*Framework: McKenney & Reeves (2012) Educational Design Research.*
