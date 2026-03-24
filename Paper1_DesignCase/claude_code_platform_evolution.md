# Claude Code Platform Evolution Timeline

A chronological record of major Claude Code capabilities and milestones, compiled for the Diverga design case paper. Dates sourced from Anthropic announcements, the official changelog, and developer coverage.

---

## 2024

### November 25, 2024 -- Model Context Protocol (MCP) Announced
Anthropic publicly introduced MCP as an open standard for connecting AI assistants to external data sources, tools, and systems. The initial specification (2024-11-05) defined JSON-RPC 2.0 messaging, stdio and SSE transports, and three primitives (tools, resources, prompts). SDKs shipped for Python, TypeScript, C#, and Java.
- Source: [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)
- Source: [MCP History](https://www.mcpserverspot.com/learn/fundamentals/mcp-history)
- Source: [Model Context Protocol (Wikipedia)](https://en.wikipedia.org/wiki/Model_Context_Protocol)

---

## 2025

### February 2025 -- Claude Code Research Preview
Anthropic released Claude Code as a limited research preview: an agentic CLI tool enabling developers to delegate coding tasks directly from the terminal, billed per API token.
- Source: [Claude Code overview](https://code.claude.com/docs/en/overview)
- Source: [Claude (language model) (Wikipedia)](https://en.wikipedia.org/wiki/Claude_(language_model))

### March 26, 2025 -- MCP Spec Update (Streamable HTTP, OAuth 2.1)
The March 2025 MCP specification revision added Streamable HTTP transport, OAuth 2.1 authentication, and tool annotations, laying the groundwork for authenticated MCP servers in Claude Code.
- Source: [MCP Specification](https://modelcontextprotocol.io/specification/2025-03-26)

### May 1, 2025 -- Claude Max Plan; Claude Code Widely Available
Claude Code became available through the Claude Max subscription ($100/month), removing pay-per-token friction and enabling broader adoption.
- Source: [Reflections of Claude Code from CHANGELOG](https://dev.to/oikon/reflections-of-claude-code-from-changelog-833)

### May 22, 2025 -- Claude 4 Launch; Claude Code GA
Anthropic released Claude Sonnet 4 and Claude Opus 4. Claude Code reached general availability after positive reception during the research preview.
- Source: [Introducing Claude 4](https://www.anthropic.com/news/claude-4)
- Source: [Claude (language model) (Wikipedia)](https://en.wikipedia.org/wiki/Claude_(language_model))

### June 12, 2025 -- Plan Mode
Plan mode added, allowing users to preview execution steps via `Shift + Tab` or `/config` settings before Claude executes tool calls.
- Source: [Reflections of Claude Code from CHANGELOG](https://dev.to/oikon/reflections-of-claude-code-from-changelog-833)

### June 18, 2025 -- MCP Spec Update (Elicitation, Structured Output)
The June 2025 MCP specification revision added elicitation (servers requesting information from users), structured output, and audio content support.
- Source: [MCP Next Version Update](https://modelcontextprotocol.info/blog/mcp-next-version-update/)

### June 30, 2025 -- Hooks System Introduced (v1.0.38)
The initial hooks system shipped with four event types: `PreToolUse`, `PostToolUse`, `Stop`, and `SessionEnd`. `PreToolUse` is the only hook that can block actions (approve or deny tool execution), enabling security gates and file protection. `PostToolUse` fires after successful tool execution with both the input and response available for inspection.
- Source: [Hooks reference](https://code.claude.com/docs/en/hooks)
- Source: [Claude Code Hooks guide](https://www.eesel.ai/blog/hooks-in-claude-code)
- Source: [GitButler: Automate Your AI Workflows with Claude Code Hooks](https://blog.gitbutler.com/automate-your-ai-workflows-with-claude-code-hooks)

### August 20, 2025 -- /context Command
The `/context` command introduced, letting users visualize the system prompt, tools, MCP integrations, custom agents, memory files, and message history.
- Source: [Reflections of Claude Code from CHANGELOG](https://dev.to/oikon/reflections-of-claude-code-from-changelog-833)

### September 29, 2025 -- Claude Code 2.0; Claude Sonnet 4.5; Claude Agent SDK; GitHub Actions
A major release day with several announcements:
- **Claude Code 2.0** shipped with a native VS Code extension (beta), a checkpoint/rewind system (auto-saves before each change, rewindable for 30 days), and an updated terminal interface with searchable prompt history (`Ctrl+R`).
- **Claude Sonnet 4.5** set as the default model.
- **Claude Agent SDK** released (formerly the Claude Code SDK), allowing developers to build general-purpose AI agents beyond coding.
- **GitHub Actions integration** (`claude-code-action`) launched, enabling AI-assisted PR review, issue triage, and automated code changes triggered by `@claude` mentions.
- Source: [Claude Code 2.0 (SmartScope)](https://smartscope.blog/en/generative-ai/claude/claude-code-2-0-release/)
- Source: [Claude Agent SDK overview](https://platform.claude.com/docs/en/agent-sdk/overview)
- Source: [anthropics/claude-code-action (GitHub)](https://github.com/anthropics/claude-code-action)

### October 16, 2025 -- Skills System (v2.0.22)
Claude Code Skills launched, allowing users to package domain knowledge, processes, and executable code into `.claude/skills/` folders. Skills auto-activate based on conversation context. Each skill uses a `SKILL.md` file with YAML frontmatter. Skills follow the Agent Skills open standard, enabling cross-platform compatibility.
- Source: [Extend Claude with skills](https://code.claude.com/docs/en/skills)
- Source: [Simon Willison: Claude Skills are awesome](https://simonwillison.net/2025/Oct/16/claude-skills/)
- Source: [Claude Agent Skills deep dive](https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/)

### October 2025 -- Plugins System (Public Beta)
Claude Code plugins launched in public beta, introducing installable extensions that bundle agents, hooks, skills, slash commands, and MCP servers. The official Anthropic plugin marketplace became automatically available in Claude Code.
- Source: [Create plugins](https://code.claude.com/docs/en/plugins)
- Source: [Discover and install plugins](https://code.claude.com/docs/en/discover-plugins)

### October 20, 2025 -- Claude Code on the Web
Claude Code launched as a web application at claude.ai (under the "Code" tab), enabling browser-based access with parallel job execution. Available to Pro, Max, Team, and Enterprise subscribers. Claude Code had grown 10x in users since May and reached over $500M in annualized revenue.
- Source: [TechCrunch: Anthropic brings Claude Code to the web](https://techcrunch.com/2025/10/20/anthropic-brings-claude-code-to-the-web/)
- Source: [MLQ: Anthropic Launches Claude Code on the Web](https://mlq.ai/news/anthropic-launches-claude-code-on-the-web/)

### November 24, 2025 -- Claude Opus 4.5
Claude Opus 4.5 released, showing strong affinity with the Claude Code harness and driving user migration back from competing tools.
- Source: [Reflections of Claude Code from CHANGELOG](https://dev.to/oikon/reflections-of-claude-code-from-changelog-833)

### November 25, 2025 -- MCP Spec v2025-11-25
The November 2025 MCP specification released, becoming the primary production standard heading into 2026.
- Source: [MCP Specification 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25)

### December 2025 -- Background Agents, Named Sessions, Dynamic MCP
Key features shipped in the v2.0.x line during December:
- **Background agents** (v2.0.60): sub-agents can run in the background while the main session continues; press `Ctrl+B` to background a running sub-agent.
- **Named sessions**: `/rename` to name sessions, then `claude --resume session-name` to resume.
- **`.claude/rules/`** directory for project rules.
- **Dynamic MCP tool loading** beta tested, addressing context window consumption.
- Source: [Claude Code Changelog](https://code.claude.com/docs/en/changelog)
- Source: [Reflections of Claude Code from CHANGELOG](https://dev.to/oikon/reflections-of-claude-code-from-changelog-833)

---

## 2026

### January 2026 -- SKILL.md, Session Forking, Cloud Handoff, --from-pr
January updates in the v2.1.x line included:
- **SKILL.md support** with frontmatter (effort, description, paths).
- **Session forking** with `/resume` grouping of forks.
- **Cloud handoff** for handing sessions from terminal to web.
- **`--from-pr` flag** for PR-linked sessions that auto-link to GitHub PRs.
- **Customizable keybindings** (`/keybindings` command, v2.1.18).
- **Task management system** with dependency tracking (v2.1.17).
- **Structured outputs in `-p` mode** (v2.1.22).
- **Bash history autocomplete** with Tab (v2.1.14).
- Source: [Claude Code Changelog](https://code.claude.com/docs/en/changelog)
- Source: [Releases (GitHub)](https://github.com/anthropics/claude-code/releases)

### February 5, 2026 -- Claude Opus 4.6; Agent Teams Research Preview (v2.1.32)
Major release day:
- **Claude Opus 4.6** launched.
- **Agent Teams** (research preview): multi-agent collaboration where one session acts as team lead, coordinating teammate sessions that work independently in their own context windows and communicate directly with each other. Distinct from subagents, which can only report back to the main agent. Enabled via `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`.
- **Auto-memory** recording system introduced.
- Source: [Orchestrate teams of Claude Code sessions](https://code.claude.com/docs/en/agent-teams)
- Source: [Claude Code Agent Teams guide](https://claudefa.st/blog/guide/agents/agent-teams)

### February 17, 2026 -- Claude Sonnet 4.6; Agent Teams on Bedrock/Vertex (v2.1.45)
Claude Sonnet 4.6 support added. Agent Teams expanded to Bedrock, Vertex, and Foundry providers. SDK rate limit info types introduced.
- Source: [Claude Code Changelog](https://code.claude.com/docs/en/changelog)

### February 19, 2026 -- Git Worktree Isolation (v2.1.49)
The `--worktree` (`-w`) flag shipped, enabling isolated git worktrees for subagents and agents. Subagents can declare `isolation: "worktree"` for sandboxed parallel work.
- Source: [Claude Code Changelog](https://code.claude.com/docs/en/changelog)

### February 26, 2026 -- Auto-Memory; /copy Command (v2.1.59)
Auto-memory system shipped, where Claude saves useful context automatically during sessions. The `/copy` command introduced with an interactive picker for code blocks.
- Source: [Claude Code Changelog](https://code.claude.com/docs/en/changelog)

### February 28, 2026 -- HTTP Hooks; /simplify and /batch (v2.1.63)
**HTTP hooks** introduced, allowing hooks to POST JSON to URLs as an alternative to shell commands. Project configs and auto-memory now shared across git worktrees. Bundled `/simplify` and `/batch` slash commands added.
- Source: [Claude Code Changelog](https://code.claude.com/docs/en/changelog)

### March 3, 2026 -- Voice Mode
Voice mode shipped (`/voice` to toggle), using a push-to-talk approach (hold space bar). Initially rolled out to ~5% of users with broader rollout through March. Available to Pro, Max, Team, and Enterprise users.
- Source: [TechCrunch: Claude Code rolls out a voice mode](https://techcrunch.com/2026/03/03/claude-code-rolls-out-a-voice-mode-capability/)

### March 7, 2026 -- /loop Command; Cron Scheduling (v2.1.71)
The `/loop` command for recurring prompts/slash commands shipped alongside cron scheduling tools. Voice mode expanded to 20 languages.
- Source: [Claude Code Changelog](https://code.claude.com/docs/en/changelog)

### March 13, 2026 -- 1M Context Window for Opus 4.6 (v2.1.75)
Opus 4.6 context window expanded to 1M tokens for Max, Team, and Enterprise plans.
- Source: [Claude Code Changelog](https://code.claude.com/docs/en/changelog)

### March 14, 2026 -- MCP Elicitation Support; PostCompact Hook (v2.1.76)
MCP Elicitation support landed in Claude Code, enabling interactive dialogs mid-task. New `Elicitation`, `ElicitationResult`, and `PostCompact` hook events added. The `/effort` slash command introduced.
- Source: [Claude Code Changelog](https://code.claude.com/docs/en/changelog)

### March 20, 2026 -- Bare Mode; Channels (v2.1.81)
`--bare` flag for scripted `-p` calls (skips hooks, LSP, plugin sync). `--channels` permission relay for pushing approvals to mobile (research preview).
- Source: [Claude Code Changelog](https://code.claude.com/docs/en/changelog)

---

## Summary of Hook Event Types (Cumulative as of March 2026)

| Hook Event | Purpose | Introduced |
|---|---|---|
| `PreToolUse` | Block/approve tool calls before execution | June 2025 |
| `PostToolUse` | Inspect tool results after execution | June 2025 |
| `Stop` | Fires when agent stops | June 2025 |
| `SessionEnd` | Fires at session end | June 2025 |
| `SessionStart` | Fires at session start | ~Late 2025 |
| `Notification` | Custom notifications | ~Late 2025 |
| `StopFailure` | Fires when agent fails to stop | March 2026 |
| `InstructionsLoaded` | Fires when CLAUDE.md loaded | ~Early 2026 |
| `TeammateIdle` | Agent Teams: teammate idle | February 2026 |
| `TaskCompleted` | Agent Teams: task finished | February 2026 |
| `ConfigChange` | Settings changed (audit) | February 2026 |
| `WorktreeCreate` | Git worktree created | February 2026 |
| `WorktreeRemove` | Git worktree removed | February 2026 |
| `PostCompact` | Context compaction completed | March 2026 |
| `Elicitation` | MCP elicitation request | March 2026 |
| `ElicitationResult` | MCP elicitation response | March 2026 |

---

## Growth Metrics

| Date | Metric |
|---|---|
| May 2025 | GA launch; pay-per-token and Max subscription |
| October 2025 | 10x user growth since May; $500M+ annualized revenue |
| November 2025 | $1B+ annualized revenue |
| February 2026 | ~4% of all public GitHub commits (~135K/day) |
| 2025 total | 176 shipped updates |

---

## Key Source URLs

- Official Changelog: https://code.claude.com/docs/en/changelog
- GitHub Releases: https://github.com/anthropics/claude-code/releases
- GitHub CHANGELOG.md: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- Hooks Reference: https://code.claude.com/docs/en/hooks
- Agent Teams Docs: https://code.claude.com/docs/en/agent-teams
- MCP Docs: https://code.claude.com/docs/en/mcp
- Skills Docs: https://code.claude.com/docs/en/skills
- Plugins Docs: https://code.claude.com/docs/en/plugins
- MCP Specification: https://modelcontextprotocol.io/
