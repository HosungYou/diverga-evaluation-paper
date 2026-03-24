"""
generate_figures_paper3.py
Generates Figure 3 and Figure 4 for Paper 3 (ETR&D)

Figure 3: Study Session Protocol
  - Phase 0-4 timeline with data sources labeled per phase

Figure 4: Mixed Methods Data Integration Design
  - QUAN + QUAL strands → joint display → meta-inference + design principles
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

C_BLUE     = '#1a5276'
C_LBLUE    = '#2980b9'
C_GREEN    = '#1e8449'
C_LGREEN   = '#27ae60'
C_GRAY     = '#717d7e'
C_LGRAY    = '#d5d8dc'
C_WHITE    = '#ffffff'
C_ORANGE   = '#d35400'
C_PURPLE   = '#6c3483'
C_LPURPLE  = '#9b59b6'
C_BLUE_BG  = '#eaf2fb'
C_GREEN_BG = '#eafaf1'
C_PUR_BG   = '#f5eef8'
C_ORG_BG   = '#fdf2e9'


# ─────────────────────────────────────────────────────────────────────────────
# Figure 3: Study Session Protocol
# ─────────────────────────────────────────────────────────────────────────────
def fig3_study_protocol():
    fig, ax = plt.subplots(figsize=(16, 7.5))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 7.5)
    ax.axis('off')
    fig.patch.set_facecolor(C_WHITE)

    # ── Title ──
    ax.text(8.0, 7.25, 'Figure 3. Study Session Protocol',
            ha='center', va='top', fontsize=12, fontweight='bold', color=C_BLUE)
    ax.text(8.0, 6.85,
            'Single-session within-subject design (N = 5); approximate total duration: 2.5–3 hours',
            ha='center', va='top', fontsize=9, color=C_GRAY, style='italic')

    TL_Y = 4.35    # timeline center y

    phases = [
        # (label_lines, duration, width, fc, ec, note_lines)
        (['Phase 0', 'Pre-Task', 'Baseline'],
         '30 min', 2.4, C_BLUE_BG, C_BLUE,
         ['Pre-task artifact', '(Google Doc, no AI)', 'Scenario A, unaided']),

        (['Phase 1', 'Orientation'],
         '20 min', 2.0, '#eaf4fc', C_LBLUE,
         ['Diverga walkthrough:', 'checkpoint system,', 'VS/T-Score, practice']),

        (['Break'], '5 min', 0.8, '#f8f9f9', C_LGRAY, []),

        (['Phase 2', 'Diverga-Assisted', '(Scenario B)'],
         '60 min', 2.8, C_GREEN_BG, C_GREEN,
         ['decision-log.yaml', 'Think-aloud audio', 'Screen recording']),

        (['Break'], '5 min', 0.8, '#f8f9f9', C_LGRAY, []),

        (['Phase 3', 'Re-design', '(Scenario A)'],
         '40 min', 2.4, C_ORG_BG, C_ORANGE,
         ['decision-log.yaml', 'Think-aloud audio', 'Screen recording']),

        (['Phase 4', 'Interview'],
         '25 min', 2.0, C_PUR_BG, C_PURPLE,
         ['Interview audio', 'Researcher field notes']),
    ]

    box_h = 1.6    # height of phase box
    gap = 0.12
    x = 0.25

    for label_lines, dur, w, fc, ec, notes in phases:
        is_break = label_lines[0] == 'Break'

        rect = FancyBboxPatch((x, TL_Y - box_h / 2), w, box_h,
                              boxstyle='round,pad=0.1',
                              facecolor=fc, edgecolor=ec, linewidth=2.0 if not is_break else 0.8)
        ax.add_patch(rect)

        if is_break:
            ax.text(x + w / 2, TL_Y + 0.18, 'Break', ha='center', va='center',
                    fontsize=8, color=C_GRAY, fontweight='bold')
            ax.text(x + w / 2, TL_Y - 0.22, dur, ha='center', va='center',
                    fontsize=7.5, color=C_GRAY)
        else:
            n = len(label_lines)
            step = 0.32
            start_y = TL_Y + step * (n - 1) / 2
            for i, line in enumerate(label_lines):
                fw = 'bold' if i == 0 else 'normal'
                fs = 10 if i == 0 else 8.5
                ax.text(x + w / 2, start_y - i * step, line,
                        ha='center', va='center', fontsize=fs,
                        fontweight=fw, color=ec)
            # Duration badge bottom
            ax.text(x + w / 2, TL_Y - box_h / 2 + 0.2, dur,
                    ha='center', va='center', fontsize=7.5, color=C_WHITE,
                    bbox=dict(boxstyle='round,pad=0.18', facecolor=ec, edgecolor='none'))

        # Data source annotation above (skip break)
        if notes:
            note_y = TL_Y + box_h / 2 + 0.55
            ax.text(x + w / 2, note_y + 0.25 * (len(notes) - 1) / 2,
                    '\n'.join(notes),
                    ha='center', va='center', fontsize=7, color=ec,
                    linespacing=1.4,
                    bbox=dict(boxstyle='round,pad=0.2', facecolor=C_WHITE,
                              edgecolor=ec, linewidth=0.8))
            ax.annotate('', xy=(x + w / 2, TL_Y + box_h / 2 + 0.02),
                        xytext=(x + w / 2, TL_Y + box_h / 2 + 0.38),
                        arrowprops=dict(arrowstyle='->', color=ec, lw=0.9))

        # Connector arrow
        x += w
        if x < 16 - w:
            ax.annotate('', xy=(x + 0.02, TL_Y),
                        xytext=(x - 0.02, TL_Y),
                        arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=1.5))
        x += gap

    # ── Counterbalance note ──
    ax.text(8.0, 0.45,
            'Counterbalancing: 3 participants receive Scenario A (Phase 0 baseline) then Scenario B (Phase 2); '
            '2 receive Scenario B then Scenario A.\n'
            'All participants engage both scenarios: unaided (Phase 0) and Diverga-assisted (Phases 2–3).',
            ha='center', va='center', fontsize=8, color=C_GRAY, style='italic',
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#fbfcfc', edgecolor=C_LGRAY))

    plt.tight_layout(rect=[0, 0.04, 1, 1])
    out = os.path.join(OUT_DIR, 'figure3_study_protocol.png')
    plt.savefig(out, dpi=300, bbox_inches='tight', facecolor=C_WHITE)
    plt.close()
    print(f"Saved: {out}")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 4: Mixed Methods Data Integration Design
# ─────────────────────────────────────────────────────────────────────────────
def fig4_data_integration():
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis('off')
    fig.patch.set_facecolor(C_WHITE)

    # ── Title ──
    ax.text(7.0, 8.75, 'Figure 4. Mixed Methods Data Integration Design',
            ha='center', va='top', fontsize=12, fontweight='bold', color=C_BLUE)
    ax.text(7.0, 8.32,
            'Convergent design: QUAN and QUAL strands analyzed independently, integrated at meta-inference stage',
            ha='center', va='top', fontsize=9, color=C_GRAY, style='italic')

    # ── Strand headers ──
    for cx, label, color in [(2.5, 'QUANTITATIVE STRAND', C_GREEN), (11.5, 'QUALITATIVE STRAND', C_PURPLE)]:
        rect = FancyBboxPatch((cx - 2.1, 7.6), 4.2, 0.72,
                              boxstyle='round,pad=0.12', facecolor=color, edgecolor='none')
        ax.add_patch(rect)
        ax.text(cx, 7.96, label, ha='center', va='center',
                fontsize=10, fontweight='bold', color=C_WHITE)

    # ── QUAN data sources ──
    quan_items = [
        ('decision-log.yaml\n(all checkpoint records)',      6.55),
        ('T-Score selection patterns\n(modal vs. non-modal choices)', 5.45),
        ('Time-on-checkpoint\n(screen recording timestamps)',         4.35),
        ('Agent activation sequences\n(dependency graph traversal)',  3.25),
    ]
    for text, y in quan_items:
        rect = FancyBboxPatch((0.4, y - 0.48), 4.2, 0.88,
                              boxstyle='round,pad=0.1',
                              facecolor=C_GREEN_BG, edgecolor=C_LGREEN, linewidth=1.3)
        ax.add_patch(rect)
        ax.text(2.5, y - 0.02, text, ha='center', va='center',
                fontsize=8.5, color='#1a5c34', linespacing=1.35)

    # ── QUAN → analysis ──
    ax.annotate('', xy=(2.5, 2.25), xytext=(2.5, 2.8),
                arrowprops=dict(arrowstyle='->', color=C_GREEN, lw=2.0))
    rect = FancyBboxPatch((0.4, 1.35), 4.2, 0.85,
                          boxstyle='round,pad=0.12', facecolor=C_GREEN, edgecolor='none')
    ax.add_patch(rect)
    ax.text(2.5, 1.78, 'CMAA Analysis\n(PIR · SUD · DSE · GCA · CCI)',
            ha='center', va='center', fontsize=9, fontweight='bold',
            color=C_WHITE, linespacing=1.35)

    # ── QUAL data sources ──
    qual_items = [
        ('Think-aloud transcripts\n(concurrent, at checkpoints)',       6.55),
        ('Pre/post design artifacts\n(Google Doc vs. Diverga output)',   5.45),
        ('Semi-structured interviews\n(4 blocks, post-session)',         4.35),
        ('Researcher field notes\n(observations, technical incidents)',   3.25),
    ]
    for text, y in qual_items:
        rect = FancyBboxPatch((9.4, y - 0.48), 4.2, 0.88,
                              boxstyle='round,pad=0.1',
                              facecolor=C_PUR_BG, edgecolor=C_LPURPLE, linewidth=1.3)
        ax.add_patch(rect)
        ax.text(11.5, y - 0.02, text, ha='center', va='center',
                fontsize=8.5, color='#4a235a', linespacing=1.35)

    # ── QUAL → analysis ──
    ax.annotate('', xy=(11.5, 2.25), xytext=(11.5, 2.8),
                arrowprops=dict(arrowstyle='->', color=C_PURPLE, lw=2.0))
    rect = FancyBboxPatch((9.4, 1.35), 4.2, 0.85,
                          boxstyle='round,pad=0.12', facecolor=C_PURPLE, edgecolor='none')
    ax.add_patch(rect)
    ax.text(11.5, 1.78, 'AT Contradiction Analysis\n+ Within-Case Narrative',
            ha='center', va='center', fontsize=9, fontweight='bold',
            color=C_WHITE, linespacing=1.35)

    # ── Integration box (center) ──
    rect = FancyBboxPatch((4.9, 1.35), 4.2, 0.85,
                          boxstyle='round,pad=0.12', facecolor=C_BLUE, edgecolor='none')
    ax.add_patch(rect)
    ax.text(7.0, 1.78, 'Integration: Joint Display\n(Cross-case Meta-Inference)',
            ha='center', va='center', fontsize=9.5, fontweight='bold',
            color=C_WHITE, linespacing=1.35)

    # ── Arrows into integration box ──
    ax.annotate('', xy=(4.9, 1.78), xytext=(4.6, 1.78),
                arrowprops=dict(arrowstyle='->', color=C_BLUE, lw=2.0))
    ax.annotate('', xy=(9.1, 1.78), xytext=(9.4, 1.78),
                arrowprops=dict(arrowstyle='->', color=C_BLUE, lw=2.0))

    # ── Key integration point ──
    rect = FancyBboxPatch((4.9, 3.8), 4.2, 3.4,
                          boxstyle='round,pad=0.15',
                          facecolor='#d6eaf8', edgecolor=C_LBLUE, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(7.0, 6.95, 'Key Integration Point', ha='center', va='center',
            fontsize=10, fontweight='bold', color=C_BLUE)
    ax.text(7.0, 6.45,
            'High DSE (wide solution space presented)\n+\nModal selection (T-Score > 0.8 chosen)',
            ha='center', va='center', fontsize=8.5, color=C_BLUE, linespacing=1.4)
    ax.text(7.0, 5.65, '⬇', ha='center', va='center', fontsize=16, color=C_LBLUE)
    ax.text(7.0, 5.12,
            'Quantitative evidence of exposure\nto diverse alternatives',
            ha='center', va='center', fontsize=8, color=C_GRAY, linespacing=1.35)
    ax.text(7.0, 4.55, '+', ha='center', va='center', fontsize=14, color=C_GRAY)
    ax.text(7.0, 4.1,
            '"It just felt right" (think-aloud)\n→ Automation bias in action',
            ha='center', va='center', fontsize=8.5, color=C_BLUE,
            fontweight='bold', linespacing=1.4,
            bbox=dict(boxstyle='round,pad=0.2', facecolor=C_WHITE,
                      edgecolor=C_LBLUE, linewidth=1.0))

    # ── Output arrow ──
    ax.annotate('', xy=(7.0, 0.98), xytext=(7.0, 1.35),
                arrowprops=dict(arrowstyle='->', color=C_BLUE, lw=2.0))
    rect = FancyBboxPatch((3.5, 0.3), 7.0, 0.65,
                          boxstyle='round,pad=0.12', facecolor='#d6eaf8',
                          edgecolor=C_BLUE, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(7.0, 0.63, 'Design Principles (ETR&D output)  +  Empirical CMAA Validation (Paper 2)',
            ha='center', va='center', fontsize=9, fontweight='bold', color=C_BLUE)

    plt.tight_layout(rect=[0, 0.02, 1, 1])
    out = os.path.join(OUT_DIR, 'figure4_data_integration.png')
    plt.savefig(out, dpi=300, bbox_inches='tight', facecolor=C_WHITE)
    plt.close()
    print(f"Saved: {out}")


if __name__ == '__main__':
    fig3_study_protocol()
    fig4_data_integration()
    print("Paper 3 figures complete.")
