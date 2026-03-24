# Semi-Structured Interview: Purpose Clarification

## Paper 3 Experimental Study
**Date:** 2026-03-21
**Context:** Dr. Yang requested that the purpose of the semi-structured interview be clearly defined, specifying what data gap it fills that other collection methods cannot address.

---

## 1. Why Semi-Structured Interviews Are Needed Beyond Think-Aloud and Screen Recording

The study already collects three rich data streams during the task phases: (a) think-aloud verbal protocols, (b) screen recordings of participant behavior, and (c) Diverga's decision-log.yaml checkpoint data. A natural question arises: what does the interview add that these concurrent methods do not already capture?

The answer lies in three fundamental limitations of concurrent data collection methods.

### 1.1 Think-Aloud Captures Process, Not Interpretation

Think-aloud protocols capture what participants are thinking *in the moment* of action. They excel at revealing cognitive processes (e.g., "I see T-Score 0.3, that seems unusual, let me look at this option"). However, think-aloud data is inherently fragmented, task-bound, and lacking in reflective depth. Participants rarely step back during a task to articulate *why* a pattern matters to them, how it connects to their broader research identity, or whether the experience changed their thinking. The interview provides a dedicated space for this reflective layer.

### 1.2 Screen Recording Captures Behavior, Not Meaning

Screen recordings reveal what participants did (clicked, scrolled, hesitated, revisited). Combined with timestamps from decision-log.yaml, they provide precise behavioral data. However, behavioral data alone is ambiguous. A 45-second pause at a checkpoint could indicate deep deliberation, confusion, distraction, or technical difficulty. The interview allows participants to attribute meaning to their own behaviors retrospectively, resolving ambiguities that behavioral data alone cannot.

### 1.3 Decision Logs Capture Outcomes, Not Rationale

Diverga's decision-log.yaml records which options participants selected, their T-Scores, and the sequence of selections. This is valuable quantitative data. But it captures the *what*, not the *why*. Two participants might both select a low-T-Score (non-modal) option; one might do so out of genuine intellectual curiosity, the other because they misunderstood the T-Score scale. Only the interview can systematically surface these underlying rationales across all checkpoint interactions.

### 1.4 Summary: The Interview's Unique Contribution

| Data Source | Captures | Cannot Capture |
|---|---|---|
| Think-aloud | In-the-moment cognitive processes | Reflective interpretation; identity-level meaning |
| Screen recording | Observable behavior and timing | Participant's own meaning-making about that behavior |
| Decision-log.yaml | Selection outcomes and sequences | Rationale, values, and contextual reasoning behind selections |
| **Semi-structured interview** | **Reflective interpretation, retrospective sense-making, perceived value, identity implications, design tensions** | **Cannot capture in-the-moment cognition (that is what think-aloud is for)** |

The interview is the only method that accesses the participant's *reflective, integrative* understanding of their own experience with Diverga. It converts fragmented process data into coherent narratives about scaffolding, autonomy, trust, and methodological growth.

---

## 2. Specific Data the Interview Captures That Other Methods Cannot

### 2.1 Perceived Scaffolding Value

Did the participant experience the checkpoints as helpful scaffolds or as interruptions? This is a subjective evaluation that only emerges through direct inquiry. A participant who dutifully engaged with every checkpoint (observable in screen recording) might privately view them as bureaucratic friction. Only the interview reveals this.

### 2.2 Trust Calibration

How much did participants trust Diverga's recommendations, and did that trust change over the course of the session? Trust is an internal state that is partially visible in behavior (e.g., accepting vs. overriding recommendations) but requires interview probing to understand its nuances (e.g., "I trusted it for theory suggestions but not for sampling decisions").

### 2.3 Automation Bias Awareness

Were participants aware of moments when they might have uncritically accepted AI suggestions? Self-awareness of automation bias is, by definition, not accessible through behavioral observation alone. The interview can surface both recognized and (through careful probing) partially recognized instances.

### 2.4 Design Tensions

What tensions did participants experience between their own methodological preferences and Diverga's suggestions? Tensions may be partially visible in think-aloud data (e.g., "Hmm, I wouldn't normally choose this"), but their full significance only emerges when participants reflect on them holistically.

### 2.5 Identity and Disciplinary Norms

How did participants' disciplinary identities shape their interaction with Diverga? A sociology student and an educational psychology student may engage with the same checkpoint differently because of disciplinary norms about acceptable methods. The interview is the primary venue for surfacing these identity-level influences.

### 2.6 Comparative Reflection (Pre-task vs. Post-task)

How do participants perceive the difference between their unassisted research design (Phase 0) and their Diverga-assisted design (Phases 2-3)? This comparison requires metacognitive reflection that is not accessible during the tasks themselves.

---

## 3. Proposed Interview Guide

**Duration:** 25-30 minutes
**Format:** Semi-structured; questions serve as prompts with flexibility for follow-up
**Timing:** Immediately after the re-design task (Phase 3), while the experience is fresh

### Structure: Four Blocks

The interview is organized into four blocks, each targeting a distinct data gap. Questions are numbered for reference; the interviewer should prioritize depth over coverage if time is limited.

---

#### Block A: Overall Experience and Perceived Value (5-7 min)

**Data gap addressed:** Holistic interpretation of the Diverga experience that cannot emerge from fragmented think-aloud data.

**Q1.** "Looking back at your entire session with Diverga, what stands out to you most?"
- *Rationale:* Open-ended entry point; reveals what the participant considers most salient, which may differ from what the researcher observed. Allows the participant to frame the experience in their own terms before targeted questions.

**Q2.** "How would you compare the research design you created without Diverga [Phase 0] to the ones you created with it [Phases 2-3]? What changed, if anything?"
- *Rationale:* Captures the participant's metacognitive assessment of scaffolding effects. This comparison is impossible to make during the tasks themselves because the participant is immersed in the task at that point.

---

#### Block B: Checkpoint Interactions and Decision-Making (8-10 min)

**Data gap addressed:** Retrospective rationale for specific checkpoint decisions; meaning attribution to behaviors observed in screen recording.

**Q3.** "During the checkpoints, Diverga presented multiple options with T-Scores. Can you walk me through how you decided which option to choose? Was there a moment where the decision felt particularly difficult or surprising?"
- *Rationale:* Elicits decision-making rationale at a level of specificity that think-aloud often misses (participants tend to narrate actions rather than justify them during concurrent verbalization). The "difficult or surprising" probe targets moments of cognitive conflict, which are theoretically important for understanding scaffolding.

**Q4.** "Were there moments where you felt like you were just going along with what Diverga suggested, rather than making an independent choice? If so, can you describe what was happening?"
- *Rationale:* Directly probes automation bias awareness. This question asks participants to reflect on their own susceptibility to AI influence, which is not accessible through behavioral observation. Phrased non-judgmentally ("going along with" rather than "blindly accepting") to reduce social desirability bias.

---

#### Block C: Trust, Autonomy, and Tensions (7-8 min)

**Data gap addressed:** Internal states (trust, autonomy, tension) that are only partially visible in behavioral data.

**Q5.** "How much did you trust the suggestions Diverga provided? Did your level of trust change as you used the tool more?"
- *Rationale:* Trust calibration is central to the automation bias question. Trust dynamics over time are especially important because they may reveal whether checkpoint interactions build appropriate trust or erode it. This temporal dimension is difficult to reconstruct from think-aloud data alone.

**Q6.** "Was there a point where Diverga's suggestion conflicted with what you would have chosen on your own? How did you handle that?"
- *Rationale:* Probes design tensions between AI scaffolding and researcher autonomy. While such conflicts may appear in think-aloud data, the interview allows participants to reflect on how they resolved them and what that resolution meant for their sense of agency as a researcher.

---

#### Block D: Broader Implications and Identity (5 min)

**Data gap addressed:** Identity-level and future-oriented reflections that are entirely outside the scope of task-concurrent data.

**Q7.** "After today's experience, how do you think a tool like Diverga might (or might not) fit into your own research practice going forward? Is there anything about it that connects to, or conflicts with, how you see yourself as a researcher?"
- *Rationale:* Captures the intersection of tool experience and researcher identity, which is a key dimension in Paper 2's framework. Also surfaces forward-looking attitudes (adoption likelihood, conditions for use) that are inaccessible through behavioral observation. The identity probe ("how you see yourself as a researcher") connects to the disciplinary identity dimension in the participant profiling matrix.

---

### Optional Follow-Up Probes (used as needed)

- "Can you say more about that?"
- "You mentioned [X] during the think-aloud; can you elaborate on what you were thinking at that point?"
- "If you could change one thing about how the checkpoints work, what would it be?"

---

## 4. How Interview Data Integrates with Other Data Sources

### 4.1 Integration Logic

The interview does not stand alone; it functions as an interpretive layer that enriches and disambiguates data from other sources. The integration follows a **convergence and complementarity** model (Greene, Caracelli, & Graham, 1989).

### 4.2 Source-by-Source Integration

| Interview Data | Integrates With | Integration Purpose |
|---|---|---|
| Q1-Q2 (overall experience, pre/post comparison) | Pre-task and post-task artifacts | Participant's perceived change is compared against observable changes in artifact quality and diversity |
| Q3 (checkpoint decision rationale) | decision-log.yaml + screen recording timestamps | Retrospective rationale is layered onto behavioral data; resolves ambiguity in observed hesitations or quick selections |
| Q4 (automation bias awareness) | Think-aloud moments of acceptance/override | Identifies whether acceptance of AI suggestions was reflective or unreflective; tests whether think-aloud silence at checkpoints masked uncritical acceptance |
| Q5 (trust calibration) | Behavioral patterns across session (screen recording) | Trust trajectory is compared against behavioral trajectory; e.g., does increasing trust correlate with faster checkpoint decisions? |
| Q6 (conflict and tension) | Think-aloud conflict moments | Interview provides resolution narrative for tensions that were only partially articulated during the task |
| Q7 (identity and future use) | Participant profiling matrix (disciplinary identity, disposition) | Connects pre-session profile to post-session reflection; examines whether challenge-seeking participants respond differently than conservative ones |

### 4.3 Analytic Procedure for Integration

1. **Within-case integration:** For each participant, create a case portrait that weaves together all data sources. Interview data serves as the participant's own interpretive voice within the portrait.
2. **Cross-source triangulation:** For each key finding (e.g., "Participant 3 explored low-T-Score options more than others"), check whether the finding is supported by at least two independent data sources. Use the interview to confirm, enrich, or challenge patterns from behavioral data.
3. **Discrepancy analysis:** When interview self-reports conflict with observed behavior (e.g., a participant claims they carefully evaluated all options but screen recording shows rapid selection), treat the discrepancy as analytically productive rather than as a validity threat. Such discrepancies reveal gaps between perceived and actual engagement with scaffolding.

### 4.4 Role in Cross-Case Analysis

In the cross-case analysis phase, interview data contributes to pattern identification by providing:
- **Participant-generated categories:** Labels and metaphors participants use to describe their experience (e.g., "It felt like having a second advisor" vs. "It felt like a quiz")
- **Explanatory accounts:** Why certain patterns emerged for some participants but not others
- **Confirming/disconfirming evidence:** When a behavioral pattern is ambiguous, interview data from multiple participants can strengthen or weaken the interpretation
