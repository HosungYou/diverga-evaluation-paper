# Paper 3: Experimental Study Design (v2)

## Updated Following Yang Meeting, 2026-03-21

**Authors:** Hosung You (Pennsylvania State University) & Mohan Yang (Texas A&M University)
**Target Journal:** Educational Technology Research and Development (ETR&D)
**Status:** Design v2, 2026-03-21
**Relationship to Other Papers:** Paper 2 (BJET) provides the theoretical/methodological framework; this paper focuses on empirical results.

---

## 1. Participant Design

Two design options are presented below for discussion. Both reflect the reduced sample size (N <= 5) and the decision to layer participants by AI knowledge level.

### Option A: Purposeful Sampling (Maximum Variation)

**Logic:** Select 4-5 participants who collectively maximize variation across key dimensions, treating the study as a multiple case study rather than a group comparison.

| Dimension | Variation Sought |
|---|---|
| AI knowledge | Range from novice to experienced |
| Research methodology expertise | Early-stage to advanced candidacy |
| Disposition | Challenge-seeking to conservative |
| Disciplinary identity | At least 2 distinct social science fields |

**Selection Criteria:**
- Social science doctoral students (excluding CS/Engineering)
- Completed at least one research methods course
- No prior Diverga experience
- Basic CLI familiarity (or willingness to learn in orientation)

**Recruitment Strategy:**
- Screening survey distributed through Penn State College of Education doctoral listservs and research methods courses
- Survey captures AI knowledge, methodology background, self-reported disposition, and disciplinary area
- Select 4-5 participants who together cover the widest range across all four dimensions
- Over-recruit by 2-3 to account for attrition

**Strengths:**
- Rich, diverse data from a small N
- Each case contributes unique analytic value
- Aligns well with case study logic (Stake, 2006; Yin, 2018)
- Does not require balanced groups, reducing recruitment pressure

**Limitations:**
- Cannot make direct between-group comparisons
- Findings are illustrative, not comparative
- Selection requires careful screening and may be difficult if the applicant pool is small

---

### Option B: Comparative Design (AI-Knowledgeable vs. AI-Novice)

**Logic:** Create two layers based on AI knowledge level to enable structured cross-case comparison. The primary analytic interest is how prior AI experience shapes interaction with Diverga's checkpoint system.

| Layer | Description | N |
|---|---|---|
| AI-Knowledgeable | Regular AI tool users (e.g., ChatGPT, Elicit, Consensus); can articulate AI strengths/limitations | 2 |
| AI-Novice | Minimal or no AI tool experience for research purposes | 2 |

**Selection Criteria (same as Option A, plus):**
- AI-Knowledgeable: Self-report using AI research tools at least weekly for 3+ months; can describe specific use cases
- AI-Novice: Self-report using AI research tools rarely or never; limited to basic queries (e.g., grammar checking)

**Recruitment Strategy:**
- Same screening survey as Option A
- Classify respondents into two pools based on AI knowledge cutoff
- Select 2 from each pool, maximizing within-layer variation on other dimensions (methodology expertise, disposition, discipline)
- Over-recruit by 1-2 per layer

**Strengths:**
- Enables structured comparison: "How does AI background shape checkpoint interaction?"
- Cleaner analytic narrative for journal reviewers
- Layers align directly with a key theoretical question (automation bias may manifest differently by AI experience)

**Limitations:**
- N=2 per group is extremely small; patterns may reflect individual idiosyncrasy rather than group-level phenomena
- Binary classification of AI knowledge oversimplifies a continuous dimension
- Harder to recruit balanced groups, especially if one pool is underrepresented

---

### Recommendation

**Option A (Purposeful Sampling, Maximum Variation) with systematic attention to AI knowledge as a primary analytic dimension.**

Rationale:
1. With N <= 5, the study is fundamentally a multiple case study regardless of design choice. Forcing a comparative structure onto 2+2 risks overstating group-level claims that the data cannot support.
2. Maximum variation sampling preserves the analytic flexibility to examine AI knowledge as one dimension among several, rather than privileging it as the sole organizing variable.
3. If, upon analysis, AI knowledge emerges as the most salient differentiator, the cross-case analysis can foreground that finding without having pre-committed to a binary framework.
4. This approach aligns with the case study methodology appropriate for the sample size and with Paper 2's methodological framework.

**Suggested N = 5:** Select participants who, as a set, cover the four-dimensional variation space. Ensure that at least 2 have strong AI knowledge and at least 2 have minimal AI knowledge; the fifth participant can fill whichever gap remains on other dimensions.

---

## 2. Participant Profiling Matrix

Each participant will be profiled across four dimensions prior to data collection. The screening instrument (administered during recruitment) captures these dimensions.

### 2.1 Profiling Dimensions

| Dimension | Definition | Measurement Approach | Classification |
|---|---|---|---|
| **AI Knowledge Level** | Familiarity with and experience using AI tools for research purposes | Self-report frequency + specificity probe: "Which AI tools have you used for research? Describe a specific instance." | High / Moderate / Low |
| **Research Methodology Expertise** | Depth of training and experience in research design and methods | Number of methods courses completed + stage in program + independent research experience (e.g., publications, conference papers) | Advanced / Intermediate / Novice |
| **Disposition** | Tendency toward challenge-seeking vs. conservative approaches in research and tool use | Adapted items from Need for Cognition Scale (Cacioppo & Petty, 1982) + scenario-based question: "When an AI tool suggests an unfamiliar methodology, how do you typically respond?" | Challenge-seeking / Balanced / Conservative |
| **Disciplinary Identity** | Primary academic discipline and its epistemological norms | Self-identified field + brief description of dominant research paradigms in that field | Categorized by field (e.g., Education, Psychology, Sociology, Communication) |

### 2.2 Screening Instrument Structure

The screening survey (estimated 10-15 minutes) includes:

1. **Demographics:** Program, year, advisor (optional), prior methods courses (list)
2. **AI Experience Block (5 items):**
   - Frequency of AI tool use for research (Likert)
   - Tools used (checklist + open response)
   - Specific use case description (open response)
   - Self-rated AI proficiency (Likert)
   - Comfort with CLI/terminal (Yes/No + brief description)
3. **Research Experience Block (4 items):**
   - Methods courses completed (list)
   - Stage in program (pre-quals, post-quals, ABD)
   - Independent research outputs (publications, conference presentations)
   - Self-rated methodology confidence (Likert)
4. **Disposition Block (4 items):**
   - 3 adapted Need for Cognition items (Likert)
   - 1 scenario-based question (open response)
5. **Disciplinary Identity Block (2 items):**
   - Primary field
   - Dominant research paradigm in their field (selected from options + open response)

### 2.3 Sample Profiling Matrix (Illustrative)

| Participant | AI Knowledge | Methodology Expertise | Disposition | Discipline |
|---|---|---|---|---|
| P1 | High | Advanced | Challenge-seeking | Educational Psychology |
| P2 | Low | Intermediate | Conservative | Curriculum & Instruction |
| P3 | High | Novice | Balanced | Communication |
| P4 | Low | Advanced | Challenge-seeking | Sociology |
| P5 | Moderate | Intermediate | Conservative | Higher Education |

---

## 3. Data Collection Protocol (Updated)

### 3.1 Session Format

**1:1 Zoom sessions** (not breakout rooms)

Rationale for format change:
- Zoom breakout rooms only support local recording (cloud recording unavailable in breakout rooms)
- Breakout rooms require assigning recording permissions individually and rely on participants to manage local recording
- With N <= 5, 1:1 sessions are logistically feasible and methodologically superior
- 1:1 format allows the researcher to observe in real time and prompt think-aloud when participants fall silent

**Technical Setup:**
- Zoom meeting with screen sharing by participant
- Host (researcher) enables cloud recording (screen + audio)
- Participant shares their screen showing Diverga terminal
- Researcher's camera off; participant's camera optional
- Backup: local recording on researcher's machine
- Duration: approximately 2.5 hours per session (with breaks)

### 3.2 Think-Aloud Protocol

**Protocol type:** Concurrent think-aloud (Ericsson & Simon, 1993), with retrospective probes at natural stopping points.

**Warm-up:** 5-minute think-aloud practice using a non-research task (e.g., planning a weekend trip) to familiarize participants with verbalizing thought processes.

**During tasks:**
- Participants are instructed: "Please think out loud as you work. Tell me what you are looking at, what you are thinking, and why you are making each decision."
- Researcher prompts if silence exceeds 15 seconds: "What are you thinking right now?"
- At checkpoints, researcher may ask brief clarifying questions: "Can you tell me more about why you chose that option?"

**Documentation:** Each session produces (a) screen recording with audio, (b) Diverga's decision-log.yaml, (c) researcher field notes.

### 3.3 Task Design

| Phase | Task | Duration | Data Collected |
|---|---|---|---|
| **Phase 0: Pre-task** | Design a study on "The impact of AI tools on K-12 student academic achievement." Include theoretical framework, methods, and data collection plan. Written in Google Doc, no AI tools. | 30 min | Pre-task artifact (Google Doc) |
| **Phase 1: Orientation** | Diverga features walkthrough: checkpoint system, VS/T-Score explanation, agent categories. Hands-on practice with a non-scored scenario. | 20 min | (No formal data; orientation log) |
| **Break** | | 5 min | |
| **Phase 2: Post-task** | Design a study on "What factors shape academic socialization and research identity formation among first-generation doctoral students from racially underrepresented groups in STEM fields?" Use Diverga with think-aloud protocol. | 60 min | Screen recording, think-aloud audio, decision-log.yaml, post-task artifact |
| **Break** | | 5 min | |
| **Phase 3: Re-design** | Revisit Phase 0 scenario using Diverga. Think-aloud protocol. Focus: how does the participant's approach change with Diverga? | 40 min | Screen recording, think-aloud audio, decision-log.yaml, re-design artifact |
| **Phase 4: Interview** | Semi-structured interview (see Document 2 for full rationale and guide) | 25-30 min | Interview audio recording |

**Total session time:** Approximately 2.5-3 hours (including breaks)

### 3.4 Data Sources Summary

| Data Source | Collection Method | Primary Analysis Purpose | Type |
|---|---|---|---|
| Pre-task artifact | Google Doc (no AI) | Baseline: methodological reasoning without AI scaffolding | QUAL |
| Checkpoint logs | Diverga decision-log.yaml | Selection patterns, deliberation indicators, T-Score choices | QUAN + QUAL |
| Think-aloud transcripts | Screen + audio recording during Phases 2-3 | Cognitive processes at checkpoints; reasoning about alternatives | QUAL |
| Screen recordings | Zoom cloud recording | Behavioral patterns: T-Score inspection, navigation, time-on-task | QUAN + QUAL |
| Post-task artifact | Generated through Diverga | Framework diversity, design quality, comparison with pre-task | QUAL |
| Re-design artifact | Generated through Diverga | Change patterns when revisiting same scenario with scaffolding | QUAL |
| Semi-structured interview | Post-session audio recording | Reflective interpretation, perceived value, design tensions (see interview_purpose.md) | QUAL |
| Researcher field notes | During and immediately after session | Contextual observations, nonverbal cues, technical issues | QUAL |

---

## 4. Analysis Plan

### 4.1 Analytic Approach

Given N <= 5, the study adopts a **multiple case study** analysis framework (Stake, 2006; Yin, 2018) rather than statistical comparison. Each participant constitutes an individual case; cross-case analysis identifies patterns and divergences.

### 4.2 Within-Case Analysis

For each participant:

1. **Chronological narrative:** Reconstruct the participant's journey through all four task phases, integrating think-aloud data, screen recording, checkpoint logs, and artifacts.
2. **Checkpoint interaction analysis:** For each checkpoint encountered, document:
   - What alternatives were presented (from decision-log.yaml)
   - T-Score of selected vs. non-selected options
   - Think-aloud data at the moment of selection
   - Time spent at checkpoint (from screen recording)
   - Whether the participant explored non-modal options
3. **Artifact comparison:** Compare pre-task and re-design artifacts on:
   - Theoretical framework diversity (number and novelty of frameworks considered)
   - Methodological reasoning depth (justification quality)
   - Design coherence (alignment between RQ, theory, and methods)
4. **Interview integration:** Layer interview reflections onto the behavioral and cognitive data to build an interpretive case portrait.

### 4.3 Cross-Case Analysis

**Framework:** Adapted from Miles, Huberman, & Saldana (2020) cross-case analysis procedures.

**Step 1: Case-ordered descriptive matrix**
- Rows = participants (ordered by AI knowledge level)
- Columns = key analytic dimensions (checkpoint behavior, T-Score exploration, framework diversity change, reasoning quality change, perceived value)

**Step 2: Pattern identification**
- Identify clusters, contrasts, and outliers across cases
- Pay particular attention to whether AI knowledge level differentiates interaction patterns (this addresses the comparative question without requiring a formal group design)

**Step 3: Thematic synthesis**
- Themes derived through a hybrid approach: deductive codes from Paper 2's framework (authentic learning elements, VS mechanisms, checkpoint-as-scaffold) combined with inductive codes emerging from the data
- Coding process: independent coding by both authors, followed by reconciliation sessions

### 4.4 Integration with Paper 2's Methodological Framework

Paper 2 establishes the theoretical/methodological architecture. Paper 3's analysis directly operationalizes that framework:

| Paper 2 Concept | Paper 3 Operationalization |
|---|---|
| Checkpoint-as-scaffold | Checkpoint interaction analysis (4.2, item 2) |
| VS-based diversity generation | T-Score selection patterns + framework diversity in artifacts |
| Automation bias mitigation | Cases where participants override modal recommendations vs. accept them |
| Authentic learning elements | Deductive coding categories for think-aloud and interview data |
| Decision Audit Trail | decision-log.yaml as behavioral data source |

### 4.5 Quality Criteria

| Criterion | Strategy |
|---|---|
| Credibility | Triangulation across data sources; member checking (participants review case portraits) |
| Transferability | Thick description of each case; participant profiling matrix enables readers to assess applicability |
| Dependability | Audit trail of analytic decisions; inter-coder agreement on initial coding round |
| Confirmability | Raw data preserved; coding framework documented; negative case analysis |

---

## 5. Timeline

| Period | Phase | Activities |
|---|---|---|
| **Weeks 1-2** (Apr 2026) | Design Finalization | Finalize participant design (Option A vs. B); develop screening instrument; prepare Diverga session environment |
| **Weeks 3-4** (Apr-May 2026) | IRB & Recruitment Prep | IRB application (Penn State); draft recruitment materials; pilot screening survey |
| **Weeks 5-6** (May 2026) | Pilot Testing | Conduct 1-2 pilot sessions; refine task design, think-aloud prompts, and interview guide; test Zoom recording setup |
| **Weeks 7-8** (Jun 2026) | Recruitment & Screening | Distribute screening survey; select 5 participants (+ 2-3 alternates); schedule sessions |
| **Weeks 9-11** (Jun-Jul 2026) | Data Collection | Conduct 5 individual 1:1 Zoom sessions (1-2 per week) |
| **Weeks 12-14** (Jul-Aug 2026) | Transcription & Preparation | Transcribe think-aloud and interview recordings; organize decision-log.yaml files; compile artifacts |
| **Weeks 15-18** (Aug-Sep 2026) | Analysis | Within-case analysis; cross-case analysis; joint coding sessions (You & Yang) |
| **Weeks 19-22** (Oct-Nov 2026) | Writing | Draft Paper 3 manuscript; internal review cycles |
| **Weeks 23-24** (Nov-Dec 2026) | Submission | Final revisions; submit to ETR&D |

**Note:** This timeline runs in parallel with Paper 2 (BJET Special Issue, abstract due 2026-08-01, full manuscript due 2026-10-28). Paper 2's theoretical framework will be substantially developed by the time Paper 3 data collection begins, ensuring analytic coherence. Journal changed from C&E to ETR&D (2026-03-24): design-based research focus and N=5 intensive methodology norms are a better fit.

---

## 6. Open Questions for Dr. Yang

1. Does Option A (maximum variation with systematic attention to AI knowledge) satisfy the comparative interest, or is a formal two-group structure (Option B) preferred?
2. Should the screening instrument include a brief task-based AI knowledge assessment (e.g., "Given this research question, which AI tool would you use and how?") in addition to self-report items?
3. Is 2.5-3 hours too long for a single session? Should we consider splitting into two sessions per participant (Day 1: Pre-task + Orientation + Post-task; Day 2: Re-design + Interview)?
4. For the re-design task (Phase 3), should participants see their original pre-task artifact, or work from memory?
5. Compensation structure for participants (given the 2.5-3 hour commitment)?
