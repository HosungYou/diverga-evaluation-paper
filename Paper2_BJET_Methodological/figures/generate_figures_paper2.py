"""
generate_figures_paper2.py
Generates Figure 1 and Figure 2 for Paper 2 (BJET SI-2026-000285)

Figure 1: CMAA Conceptual Framework
  - Floridi (2025) 3 criteria → Diverga architecture → CMAA 5 indicators

Figure 2: Checkpoint Interaction as Natural Measurement Instrument
  - Single REQUIRED checkpoint → data packet elements mapped to CMAA indicators
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Palette
C_BLUE      = '#1a5276'
C_LBLUE     = '#2980b9'
C_GREEN     = '#1e8449'
C_LGREEN    = '#27ae60'
C_GRAY      = '#717d7e'
C_LGRAY     = '#d5d8dc'
C_WHITE     = '#ffffff'
C_RED       = '#c0392b'
C_ORANGE    = '#d35400'
C_YELLOW_BG = '#fef9e7'
C_BLUE_BG   = '#eaf2fb'
C_GREEN_BG  = '#eafaf1'
C_PURPLE    = '#6c3483'


# ─────────────────────────────────────────────────────────────────────────────
# Figure 1: CMAA Conceptual Framework
# ─────────────────────────────────────────────────────────────────────────────
def fig1_cmaa_framework():
    fig, ax = plt.subplots(figsize=(15, 9))
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 9)
    ax.axis('off')
    fig.patch.set_facecolor(C_WHITE)

    # ── Title ──
    ax.text(7.5, 8.7, 'Figure 1. Checkpoint-Mediated Agency Analysis (CMAA): Conceptual Framework',
            ha='center', va='top', fontsize=12, fontweight='bold', color=C_BLUE)
    ax.text(7.5, 8.25,
            "Mapping Floridi's (2025) Artificial Agency Criteria through Diverga's Architecture to Measurable CMAA Indicators",
            ha='center', va='top', fontsize=9, color=C_GRAY, style='italic')

    # ── Column header boxes ──
    col_cx = [2.2, 7.5, 12.8]
    col_labels = [
        "Floridi's (2025)\nArtificial Agency Criteria",
        "Diverga's\nMulti-Agent Architecture",
        "CMAA\nIndicators",
    ]
    col_colors = [C_BLUE, C_LBLUE, C_GREEN]

    for cx, label, color in zip(col_cx, col_labels, col_colors):
        rect = FancyBboxPatch((cx - 1.9, 7.1), 3.8, 0.85,
                              boxstyle='round,pad=0.12',
                              facecolor=color, edgecolor='none')
        ax.add_patch(rect)
        ax.text(cx, 7.53, label, ha='center', va='center',
                fontsize=10, fontweight='bold', color=C_WHITE, linespacing=1.4)

    # ── Col 1: Floridi criteria ──
    criteria = [
        ('Interactivity',          'Reciprocal engagement\nwith an environment', 5.85),
        ('Bounded Autonomy',       'Action within constraints;\nhuman override preserved', 3.95),
        ('Adaptability',           'Behavior modification\nbased on feedback', 2.05),
    ]
    for name, desc, y in criteria:
        rect = FancyBboxPatch((0.3, y - 0.72), 3.8, 1.35,
                              boxstyle='round,pad=0.12',
                              facecolor=C_BLUE_BG, edgecolor=C_BLUE, linewidth=1.6)
        ax.add_patch(rect)
        ax.text(2.2, y + 0.28, name, ha='center', va='center',
                fontsize=10, fontweight='bold', color=C_BLUE)
        ax.text(2.2, y - 0.24, desc, ha='center', va='center',
                fontsize=8, color=C_GRAY, linespacing=1.35)

    # ── Col 2: Diverga architecture ──
    arch = [
        ('Human Checkpoint System',          'REQUIRED checkpoints halt execution;\nhalt-and-defer at critical junctures', 5.85),
        ('VS + T-Score Engine',              'Verbalized Sampling generates options\nspanning T: 0.0 (novel) → 1.0 (modal)', 3.95),
        ('3-Layer Memory +\nDecision Audit Trail',
                                              'Persistent project state;\nimmutable YAML checkpoint log', 2.05),
    ]
    for name, desc, y in arch:
        rect = FancyBboxPatch((5.6, y - 0.72), 3.8, 1.35,
                              boxstyle='round,pad=0.12',
                              facecolor='#eaf4fc', edgecolor=C_LBLUE, linewidth=1.6)
        ax.add_patch(rect)
        ax.text(7.5, y + 0.28, name, ha='center', va='center',
                fontsize=9.5, fontweight='bold', color=C_LBLUE, linespacing=1.3)
        ax.text(7.5, y - 0.24, desc, ha='center', va='center',
                fontsize=8, color=C_GRAY, linespacing=1.35)

    # ── Arrows col 1 → col 2 ──
    for y in [5.85, 3.95, 2.05]:
        ax.annotate('', xy=(5.6, y), xytext=(4.1, y),
                    arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=1.6))

    # ── Col 3: CMAA indicators ──
    indicators = [
        ('PIR',   'Proactive Intervention Rate',     6.55),
        ('GCA',   'Governance Constraint Activation', 5.35),
        ('DSE',   'Decision Space Expansion',         4.15),
        ('SUD',   'State Utilization Depth',          2.95),
        ('CCI',   'Coordination Complexity Index',    1.75),
    ]
    for abbr, name, y in indicators:
        rect = FancyBboxPatch((10.9, y - 0.55), 3.8, 1.0,
                              boxstyle='round,pad=0.12',
                              facecolor=C_GREEN_BG, edgecolor=C_GREEN, linewidth=1.6)
        ax.add_patch(rect)
        ax.text(12.8, y + 0.12, abbr, ha='center', va='center',
                fontsize=11, fontweight='bold', color=C_GREEN)
        ax.text(12.8, y - 0.28, name, ha='center', va='center',
                fontsize=8, color=C_GRAY)

    # ── Arrows col 2 → col 3 (with connections) ──
    connections = [
        # (from_y, to_y, rad)
        (5.85, 6.55, -0.15),   # Interactivity → PIR
        (5.85, 1.75, -0.3),    # Interactivity → CCI
        (3.95, 5.35, -0.2),    # Bounded Auto → GCA
        (3.95, 4.15,  0.0),    # VS → DSE
        (2.05, 2.95,  0.15),   # Memory → SUD
    ]
    for fy, ty, rad in connections:
        ax.annotate('', xy=(10.9, ty), xytext=(9.4, fy),
                    arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=1.2,
                                   connectionstyle=f'arc3,rad={rad}'))

    # ── Bottom note ──
    ax.text(7.5, 0.55,
            'Each CMAA indicator is measurable from checkpoint interaction data (decision-log.yaml) '
            'and linked to a specific criterion of artificial agency (Floridi, 2025).',
            ha='center', va='center', fontsize=8, color=C_GRAY, style='italic',
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#fbfcfc', edgecolor=C_LGRAY))

    plt.tight_layout(rect=[0, 0.04, 1, 1])
    out = os.path.join(OUT_DIR, 'figure1_cmaa_framework.png')
    plt.savefig(out, dpi=300, bbox_inches='tight', facecolor=C_WHITE)
    plt.close()
    print(f"Saved: {out}")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 2: Checkpoint Interaction as Natural Measurement Instrument
# ─────────────────────────────────────────────────────────────────────────────
def fig2_checkpoint_data_packet():
    fig, ax = plt.subplots(figsize=(14, 8.5))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8.5)
    ax.axis('off')
    fig.patch.set_facecolor(C_WHITE)

    # ── Title ──
    ax.text(7.0, 8.2, 'Figure 2. Checkpoint Interaction as Natural Measurement Instrument',
            ha='center', va='top', fontsize=12, fontweight='bold', color=C_BLUE)
    ax.text(7.0, 7.78,
            'Data elements generated at each REQUIRED checkpoint and their mapping to CMAA indicators',
            ha='center', va='top', fontsize=9, color=C_GRAY, style='italic')

    # ── Central checkpoint box ──
    cx, cy = 7.0, 4.1
    rect = FancyBboxPatch((cx - 1.9, cy - 0.95), 3.8, 1.85,
                          boxstyle='round,pad=0.15',
                          facecolor=C_BLUE, edgecolor='none')
    ax.add_patch(rect)
    ax.text(cx, cy + 0.52, 'REQUIRED', ha='center', va='center',
            fontsize=8.5, color='#aed6f1', fontweight='bold', style='italic')
    ax.text(cx, cy + 0.05, 'CHECKPOINT', ha='center', va='center',
            fontsize=14, color=C_WHITE, fontweight='bold')
    ax.text(cx, cy - 0.52, 'e.g., CP_THEORY_SELECTION', ha='center', va='center',
            fontsize=8, color='#aed6f1')

    # ── Human decision label ──
    ax.text(cx, cy - 1.45, '⬆  Human evaluates and selects', ha='center', va='center',
            fontsize=9, color=C_BLUE, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#d6eaf8', edgecolor=C_LBLUE, linewidth=1.2))

    # ── LEFT: VS-generated alternatives ──
    ax.text(2.3, 7.25, 'VS-Generated Alternatives', ha='center', va='center',
            fontsize=10, fontweight='bold', color=C_LBLUE)
    ax.text(2.3, 6.88, '(Verbalized Sampling Engine)', ha='center', va='center',
            fontsize=8, color=C_GRAY, style='italic')

    options = [
        ('Modal Option',     'T-Score > 0.8  (predictable)', '#fdedec', C_RED,    6.2),
        ('Mid-Range Alt.',   'T-Score ~ 0.5  (contextual)',  C_YELLOW_BG, '#b7950b', 4.7),
        ('Non-Modal Alt.',   'T-Score < 0.3  (innovative)',  C_GREEN_BG,  C_LGREEN, 3.2),
    ]
    for label, desc, fc, ec, y in options:
        rect = FancyBboxPatch((0.3, y - 0.58), 4.0, 1.05,
                              boxstyle='round,pad=0.1', facecolor=fc,
                              edgecolor=ec, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(2.3, y + 0.15, label, ha='center', va='center',
                fontsize=9.5, fontweight='bold', color=ec)
        ax.text(2.3, y - 0.28, desc, ha='center', va='center',
                fontsize=8.5, color=C_GRAY)
        ax.annotate('', xy=(cx - 1.9, cy), xytext=(4.3, y),
                    arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=1.3,
                                   connectionstyle='arc3,rad=0'))

    # ── RIGHT: Measurement data logged ──
    ax.text(11.7, 7.25, 'decision-log.yaml', ha='center', va='center',
            fontsize=10, fontweight='bold', color=C_GREEN)
    ax.text(11.7, 6.88, '(Immutable Decision Audit Trail)', ha='center', va='center',
            fontsize=8, color=C_GRAY, style='italic')

    outputs = [
        ('Selection Record',    'Option chosen + T-Score\n→ PIR, DSE measurement',      C_GREEN_BG, C_GREEN,  6.2),
        ('Deliberation Log',    'Time-on-checkpoint\n→ SUD, engagement depth',           C_BLUE_BG,  C_LBLUE,  4.7),
        ('Governance Record',   'REQUIRED bypass? Y/N\n→ GCA measurement',               '#fdf2e9',  C_ORANGE, 3.2),
    ]
    for label, desc, fc, ec, y in outputs:
        rect = FancyBboxPatch((9.7, y - 0.58), 4.0, 1.05,
                              boxstyle='round,pad=0.1', facecolor=fc,
                              edgecolor=ec, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(11.7, y + 0.15, label, ha='center', va='center',
                fontsize=9.5, fontweight='bold', color=ec)
        ax.text(11.7, y - 0.28, desc, ha='center', va='center',
                fontsize=8, color=C_GRAY, linespacing=1.3)
        ax.annotate('', xy=(9.7, y), xytext=(cx + 1.9, cy),
                    arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=1.3,
                                   connectionstyle='arc3,rad=0'))

    # ── Bottom note ──
    ax.text(7.0, 0.48,
            'Each checkpoint yields a structured data packet: alternatives presented × T-scores × '
            'human selection × deliberation time → CMAA quantitative input. '
            'N alternatives presented per checkpoint = Decision Space Expansion (DSE) raw data.',
            ha='center', va='center', fontsize=8, color=C_GRAY, style='italic',
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#fbfcfc', edgecolor=C_LGRAY))

    plt.tight_layout(rect=[0, 0.04, 1, 1])
    out = os.path.join(OUT_DIR, 'figure2_checkpoint_data_packet.png')
    plt.savefig(out, dpi=300, bbox_inches='tight', facecolor=C_WHITE)
    plt.close()
    print(f"Saved: {out}")


if __name__ == '__main__':
    fig1_cmaa_framework()
    fig2_checkpoint_data_packet()
    print("Paper 2 figures complete.")
