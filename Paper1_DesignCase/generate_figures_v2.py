"""
Generate academic figures for IJDL Design Case Paper (v2).
Diverga: Scaffolding Without Replacing.

Figures:
  1. Conceptual Framework (EDR + CA + Design Decisions + Platform)
  2. Five EDR Cycles (timeline + agent count overlay)
  3. Platform-Design Co-evolution (dual timeline with arrows)
  4. Architecture Comparison (v10 44 agents vs v11 24 agents)
  5. Checkpoint Flow (5 REQUIRED gates + CA method labels)

All figures: 300 DPI, academic grayscale style, matplotlib.
Output: figures/ directory.
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
import numpy as np
from datetime import datetime, timedelta

# Output directory
OUTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(OUTDIR, exist_ok=True)

# Common style
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
    "font.size": 9,
    "axes.linewidth": 0.8,
    "axes.edgecolor": "#333333",
    "text.color": "#222222",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.3,
})

# Color palette (grayscale-friendly with subtle tones)
GRAY_DARK = "#333333"
GRAY_MED = "#666666"
GRAY_LIGHT = "#999999"
GRAY_VLIGHT = "#CCCCCC"
GRAY_BG = "#F0F0F0"
ACCENT1 = "#4A7C9B"  # Steel blue (prints well in grayscale)
ACCENT2 = "#7B9E6B"  # Sage green
ACCENT3 = "#C4785B"  # Terracotta
ACCENT4 = "#8B7BAE"  # Muted purple
ACCENT5 = "#B8963E"  # Ochre

CYCLE_COLORS = ["#D4E4F0", "#D4ECD0", "#F5E0D0", "#E0D8EE", "#F0E8C8"]
CYCLE_BORDERS = [ACCENT1, ACCENT2, ACCENT3, ACCENT4, ACCENT5]


def add_rounded_box(ax, xy, width, height, text, facecolor="white",
                    edgecolor=GRAY_DARK, fontsize=8, fontweight="normal",
                    text_color=GRAY_DARK, linewidth=1.0, pad=0.02,
                    boxstyle="round,pad=0.02", zorder=2, ha="center",
                    va="center", wrap=False):
    """Add a rounded rectangle with centered text."""
    box = FancyBboxPatch(
        xy, width, height,
        boxstyle=boxstyle,
        facecolor=facecolor,
        edgecolor=edgecolor,
        linewidth=linewidth,
        zorder=zorder,
    )
    ax.add_patch(box)
    cx = xy[0] + width / 2
    cy = xy[1] + height / 2
    ax.text(cx, cy, text, ha=ha, va=va, fontsize=fontsize,
            fontweight=fontweight, color=text_color, zorder=zorder + 1,
            wrap=wrap)
    return box


# ============================================================
# FIGURE 1: Conceptual Framework Diagram
# ============================================================

def figure1_conceptual_framework():
    fig, ax = plt.subplots(figsize=(10, 8.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.3, 8)
    ax.axis("off")

    # Title
    ax.text(5, 7.7, "Conceptual Framework: Diverga as Learning Design in Disguise",
            ha="center", va="center", fontsize=12, fontweight="bold", color=GRAY_DARK)

    # --- Outer Layer: EDR Model ---
    edr_box = FancyBboxPatch(
        (0.3, 1.6), 9.4, 5.8,
        boxstyle="round,pad=0.15",
        facecolor="#F8F8F8", edgecolor=GRAY_DARK,
        linewidth=2.0, linestyle="--", zorder=1
    )
    ax.add_patch(edr_box)
    ax.text(5, 7.15, "Educational Design Research Model (McKenney & Reeves, 2012)",
            ha="center", va="center", fontsize=9, fontstyle="italic",
            color=GRAY_MED, zorder=2)

    # EDR phases as curved arrows at top
    phases = [
        ("Analysis /\nExploration", 1.8, 6.65),
        ("Design /\nConstruction", 5.0, 6.65),
        ("Evaluation /\nReflection", 8.2, 6.65),
    ]
    for label, x, y in phases:
        add_rounded_box(ax, (x - 0.9, y - 0.35), 1.8, 0.7, label,
                        facecolor=GRAY_BG, edgecolor=GRAY_MED,
                        fontsize=7.5, linewidth=0.8)

    # Arrows between EDR phases
    for x1, x2 in [(2.7, 4.1), (5.9, 7.3)]:
        ax.annotate("", xy=(x2, 6.65), xytext=(x1, 6.65),
                    arrowprops=dict(arrowstyle="->", color=GRAY_LIGHT,
                                    lw=1.2, connectionstyle="arc3,rad=0.0"))
    # Return arrow (iteration)
    ax.annotate("", xy=(1.8, 6.15), xytext=(8.2, 6.15),
                arrowprops=dict(arrowstyle="->", color=GRAY_LIGHT,
                                lw=1.0, connectionstyle="arc3,rad=-0.15",
                                linestyle="dashed"))
    ax.text(5.0, 5.85, "5 iterative cycles", ha="center", fontsize=7,
            color=GRAY_LIGHT, fontstyle="italic")

    # --- Middle Layer: Cognitive Apprenticeship Methods ---
    ca_label_y = 5.35
    ax.text(5, ca_label_y, "Cognitive Apprenticeship Methods (Collins et al., 1989)",
            ha="center", va="center", fontsize=9, fontweight="bold",
            color=GRAY_DARK)

    # Group 1: Modeling, Coaching, Scaffolding -> DD1
    ca_group1 = [("Modeling", 1.0), ("Coaching", 2.5), ("Scaffolding", 4.0)]
    for label, x in ca_group1:
        add_rounded_box(ax, (x - 0.55, 4.55), 1.1, 0.5, label,
                        facecolor="#D4E4F0", edgecolor=ACCENT1,
                        fontsize=7.5, linewidth=0.8)

    # Group 2: Reflection, Exploration -> DD2
    ca_group2 = [("Reflection", 5.8), ("Exploration", 7.3)]
    for label, x in ca_group2:
        add_rounded_box(ax, (x - 0.55, 4.55), 1.1, 0.5, label,
                        facecolor="#D4ECD0", edgecolor=ACCENT2,
                        fontsize=7.5, linewidth=0.8)

    # Group 3: Articulation -> DD3
    ca_group3 = [("Articulation", 9.0)]
    for label, x in ca_group3:
        add_rounded_box(ax, (x - 0.55, 4.55), 1.1, 0.5, label,
                        facecolor="#F5E0D0", edgecolor=ACCENT3,
                        fontsize=7.5, linewidth=0.8)

    # --- Inner Layer: 3 Diverga Design Decisions ---
    dd_y = 3.2
    dd_h = 0.9
    dd_data = [
        ("Design Decision 1\nMulti-Agent Architecture\n(44 to 24 agents)",
         1.0, 2.8, ACCENT1, "#D4E4F0"),
        ("Design Decision 2\nVS and T-Score\n(Structuring Diversity)",
         4.5, 2.3, ACCENT2, "#D4ECD0"),
        ("Design Decision 3\nHuman Checkpoints\n(Cognitive Forcing Functions)",
         7.5, 2.3, ACCENT3, "#F5E0D0"),
    ]
    for label, x, w, ec, fc in dd_data:
        add_rounded_box(ax, (x - w / 2, dd_y - dd_h / 2), w, dd_h, label,
                        facecolor=fc, edgecolor=ec, fontsize=7.5,
                        fontweight="bold", linewidth=1.5)

    # Arrows from CA methods to Design Decisions
    # Group 1 -> DD1
    for x in [1.0, 2.5, 4.0]:
        ax.annotate("", xy=(2.3, dd_y + dd_h / 2), xytext=(x, 4.55),
                    arrowprops=dict(arrowstyle="->", color=ACCENT1,
                                    lw=0.7, alpha=0.5))
    # Group 2 -> DD2
    for x in [5.8, 7.3]:
        ax.annotate("", xy=(5.65, dd_y + dd_h / 2), xytext=(x, 4.55),
                    arrowprops=dict(arrowstyle="->", color=ACCENT2,
                                    lw=0.7, alpha=0.5))
    # Group 3 -> DD3
    ax.annotate("", xy=(8.5, dd_y + dd_h / 2), xytext=(9.0, 4.55),
                arrowprops=dict(arrowstyle="->", color=ACCENT3,
                                lw=0.7, alpha=0.5))

    # --- Bottom Bar: Platform Evolution ---
    bar_y = 0.9
    bar_h = 0.08
    # Horizontal line instead of box
    ax.plot([0.8, 9.4], [bar_y, bar_y], color=GRAY_MED, linewidth=1.5, zorder=1)
    ax.text(5, bar_y + 0.3,
            "Claude Code Platform Evolution",
            ha="center", va="center", fontsize=8, fontweight="bold",
            color=GRAY_DARK)

    milestones = [
        ("MCP", "(Nov 2024)", 1.3),
        ("Hooks", "(Jun 2025)", 3.0),
        ("Skills", "(Oct 2025)", 4.7),
        ("Plugins", "(Oct 2025)", 6.0),
        ("Agent Teams", "(Feb 2026)", 7.8),
        ("1M Context", "(Mar 2026)", 9.1),
    ]
    for name, date_str, x in milestones:
        ax.plot(x, bar_y, "o", color=GRAY_DARK, markersize=6, zorder=3)
        ax.text(x, bar_y - 0.15, name, ha="center", va="top",
                fontsize=6.5, color=GRAY_DARK, zorder=3, fontweight="bold")
        ax.text(x, bar_y - 0.35, date_str, ha="center", va="top",
                fontsize=5.5, color=GRAY_MED, zorder=3)

    # Dashed arrows from platform bar up to design decisions
    ax.annotate("", xy=(2.3, dd_y - dd_h / 2), xytext=(3.0, bar_y + 0.1),
                arrowprops=dict(arrowstyle="->", color=GRAY_LIGHT,
                                lw=0.8, linestyle="dashed"))
    ax.annotate("", xy=(5.65, dd_y - dd_h / 2), xytext=(6.0, bar_y + 0.1),
                arrowprops=dict(arrowstyle="->", color=GRAY_LIGHT,
                                lw=0.8, linestyle="dashed"))
    ax.annotate("", xy=(8.5, dd_y - dd_h / 2), xytext=(7.8, bar_y + 0.1),
                arrowprops=dict(arrowstyle="->", color=GRAY_LIGHT,
                                lw=0.8, linestyle="dashed"))

    fig.savefig(os.path.join(OUTDIR, "figure1_conceptual_framework.png"))
    plt.close(fig)
    print("  Saved figure1_conceptual_framework.png")


# ============================================================
# FIGURE 2: Five EDR Cycles
# ============================================================

def figure2_edr_cycles():
    fig, ax = plt.subplots(figsize=(12, 6))

    # Date range
    start = datetime(2026, 1, 22)
    end = datetime(2026, 3, 19)
    total_days = (end - start).days

    def date_to_x(d):
        return (d - start).days / total_days * 10 + 0.5

    # Cycle definitions
    cycles = [
        ("Cycle 1:\nFoundation",
         datetime(2026, 1, 22), datetime(2026, 1, 23), "v1.0-v2.0"),
        ("Cycle 2:\nSisyphus &\nClean Slate",
         datetime(2026, 1, 23), datetime(2026, 1, 25), "v3.0-v6.0"),
        ("Cycle 3:\nExpansion\nto 44",
         datetime(2026, 1, 25), datetime(2026, 2, 4), "v6.0-v6.7"),
        ("Cycle 4:\nGreat\nConsolidation",
         datetime(2026, 2, 4), datetime(2026, 3, 10), "v8.0-v11.0"),
        ("Cycle 5:\nStabilization",
         datetime(2026, 3, 12), datetime(2026, 3, 19), "v11.1-v12.0"),
    ]

    # Draw cycle bands
    for i, (label, d_start, d_end, versions) in enumerate(cycles):
        x1 = date_to_x(d_start)
        x2 = date_to_x(d_end)
        ax.axvspan(x1, x2, ymin=0.0, ymax=0.85,
                   facecolor=CYCLE_COLORS[i], edgecolor=CYCLE_BORDERS[i],
                   linewidth=1.0, alpha=0.7, zorder=1)
        mid_x = (x1 + x2) / 2
        ax.text(mid_x, 46.5, label, ha="center", va="bottom",
                fontsize=7, fontweight="bold", color=CYCLE_BORDERS[i],
                zorder=5)
        ax.text(mid_x, 45, versions, ha="center", va="bottom",
                fontsize=6, color=GRAY_MED, fontstyle="italic", zorder=5)

    # Agent count line
    agent_data = [
        (datetime(2026, 1, 22), 20),
        (datetime(2026, 1, 22), 20),  # v1.0
        (datetime(2026, 1, 23), 21),  # v3.0
        (datetime(2026, 1, 25), 33),  # v5.0 Sisyphus
        (datetime(2026, 1, 25), 27),  # v6.0 Clean Slate
        (datetime(2026, 1, 26), 40),  # v6.3
        (datetime(2026, 1, 30), 44),  # v6.7 peak
        (datetime(2026, 2, 4), 44),   # maintained
        (datetime(2026, 2, 28), 44),  # maintained through Cycle 4
        (datetime(2026, 3, 10), 24),  # v11.0 consolidation
        (datetime(2026, 3, 12), 29),  # v11.1 VS Arena
        (datetime(2026, 3, 19), 29),  # v12.0
    ]
    dates = [date_to_x(d) for d, _ in agent_data]
    agents = [a for _, a in agent_data]

    ax.plot(dates, agents, "o-", color=GRAY_DARK, linewidth=2.0,
            markersize=4, zorder=4, label="Agent count")

    # Key events
    events = [
        (datetime(2026, 1, 25), 33, "Sisyphus\nadded", "above"),
        (datetime(2026, 1, 25), 27, "Clean Slate\n(removed)", "below"),
        (datetime(2026, 1, 30), 44, "44 agents\n(PEAK)", "above"),
        (datetime(2026, 3, 10), 24, "Consolidation\n44 to 24", "below"),
        (datetime(2026, 3, 12), 29, "VS Arena\n(+5 personas)", "above"),
    ]
    for d, y_val, label, pos in events:
        x = date_to_x(d)
        offset = 4 if pos == "above" else -5
        va = "bottom" if pos == "above" else "top"
        ax.annotate(label, xy=(x, y_val), xytext=(x, y_val + offset),
                    fontsize=6, ha="center", va=va, color=GRAY_DARK,
                    arrowprops=dict(arrowstyle="-", color=GRAY_LIGHT,
                                    lw=0.6), zorder=5)

    # Platform milestones on bottom
    platform_y = 12
    ax.axhline(y=14, color=GRAY_VLIGHT, linewidth=0.5, linestyle=":", zorder=1)
    ax.text(0.5, 14.5, "Platform Milestones", fontsize=7, fontweight="bold",
            color=GRAY_MED, va="bottom")

    platform_events = [
        (datetime(2026, 1, 22), "Skills\n(Oct 2025)"),
        (datetime(2026, 1, 27), "Plugins\n(Oct 2025)"),
        (datetime(2026, 2, 5), "Agent Teams\n(Feb 5)"),
        (datetime(2026, 2, 28), "Hooks\nEnforcement"),
        (datetime(2026, 3, 13), "1M Context\n(Mar 13)"),
    ]
    for d, label in platform_events:
        x = date_to_x(d)
        ax.plot(x, platform_y, "s", color=ACCENT1, markersize=5, zorder=4)
        ax.text(x, platform_y - 1.5, label, ha="center", va="top",
                fontsize=5.5, color=ACCENT1, zorder=5)

    # Formatting
    ax.set_xlim(0.2, 10.8)
    ax.set_ylim(5, 52)
    ax.set_ylabel("Agent Count", fontsize=9, fontweight="bold")
    ax.set_xlabel("Development Timeline (January 22 - March 19, 2026)", fontsize=9)

    # X-axis date labels
    date_ticks = [
        datetime(2026, 1, 22), datetime(2026, 1, 27),
        datetime(2026, 2, 1), datetime(2026, 2, 8),
        datetime(2026, 2, 15), datetime(2026, 2, 22),
        datetime(2026, 3, 1), datetime(2026, 3, 8),
        datetime(2026, 3, 15), datetime(2026, 3, 19),
    ]
    ax.set_xticks([date_to_x(d) for d in date_ticks])
    ax.set_xticklabels([d.strftime("%b %d") for d in date_ticks],
                       fontsize=7, rotation=30, ha="right")

    ax.set_title("Figure 2: Five EDR Iterative Design Cycles with Agent Count Trajectory",
                 fontsize=11, fontweight="bold", pad=15)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.savefig(os.path.join(OUTDIR, "figure2_edr_cycles.png"))
    plt.close(fig)
    print("  Saved figure2_edr_cycles.png")


# ============================================================
# FIGURE 3: Platform-Design Co-evolution
# ============================================================

def figure3_platform_coevolution():
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")

    ax.text(6, 6.7, "Figure 3: Platform-Design Co-evolution",
            ha="center", fontsize=12, fontweight="bold", color=GRAY_DARK)

    # Top track: Claude Code features
    top_y = 5.2
    ax.text(0.3, top_y + 0.9, "Claude Code Platform Features",
            fontsize=9, fontweight="bold", color=ACCENT1)
    ax.plot([0.5, 11.5], [top_y + 0.5, top_y + 0.5],
            color=ACCENT1, linewidth=2, zorder=2)

    platform_features = [
        (1.2, "MCP Announced\n(Nov 2024)", "Enabled multi-agent\ncoordination protocol"),
        (3.0, "Hooks System\n(Jun 2025)", "PreToolUse can block\ntool execution"),
        (5.0, "Skills System\n(Oct 2025)", "SKILL.md agent\ndefinition format"),
        (6.5, "Plugins\n(Oct 2025)", "Marketplace distribution;\nbundled extensions"),
        (8.5, "Agent Teams\n(Feb 2026)", "Independent multi-agent\ncollaboration"),
        (10.5, "1M Context\n(Mar 2026)", "Reduced compaction;\nlarger agent instructions"),
    ]
    for x, title, desc in platform_features:
        ax.plot(x, top_y + 0.5, "o", color=ACCENT1, markersize=8, zorder=3)
        ax.text(x, top_y + 0.7, title, ha="center", va="bottom",
                fontsize=6.5, fontweight="bold", color=ACCENT1)
        ax.text(x, top_y + 0.1, desc, ha="center", va="top",
                fontsize=5.5, color=GRAY_MED, linespacing=1.3)

    # Bottom track: Diverga design changes
    bot_y = 1.8
    ax.text(0.3, bot_y + 0.9, "Diverga Design Changes",
            fontsize=9, fontweight="bold", color=ACCENT3)
    ax.plot([0.5, 11.5], [bot_y + 0.5, bot_y + 0.5],
            color=ACCENT3, linewidth=2, zorder=2)

    design_changes = [
        (1.2, "Architecture built\non MCP", "All agent communication\nvia MCP protocol"),
        (3.0, "Checkpoint\nenforcement", "Behavioral instructions\nto architectural gates"),
        (5.0, "Agent definitions\nas SKILL.md", "20 agents defined as\nskill files (v1.0)"),
        (6.5, "Marketplace\ndistribution", "Single-click install;\n8 fix commits in 1 day"),
        (8.5, "VS Arena with\ngenuine debate", "Simulated diversity to\nindependent personas"),
        (10.5, "CLAUDE.md\nslimmed to <5KB", "Larger context enables\nricher agent instructions"),
    ]
    for x, title, desc in design_changes:
        ax.plot(x, bot_y + 0.5, "s", color=ACCENT3, markersize=7, zorder=3)
        ax.text(x, bot_y + 0.7, title, ha="center", va="bottom",
                fontsize=6.5, fontweight="bold", color=ACCENT3)
        ax.text(x, bot_y + 0.1, desc, ha="center", va="top",
                fontsize=5.5, color=GRAY_MED, linespacing=1.3)

    # Connecting arrows
    for x, _, _ in platform_features:
        ax.annotate(
            "", xy=(x, bot_y + 0.85), xytext=(x, top_y + 0.05),
            arrowprops=dict(
                arrowstyle="->", color=GRAY_VLIGHT,
                lw=1.2, linestyle="dashed",
                connectionstyle="arc3,rad=0.0"
            ), zorder=1
        )

    # Before/After annotations
    annotations = [
        (3.0, 3.6, "Before: instructions only\nAfter: architectural enforcement"),
        (8.5, 3.6, "Before: simulated diversity\nAfter: genuine multi-agent debate"),
        (6.5, 3.6, "Before: manual setup\nAfter: marketplace install"),
    ]
    for x, y, text in annotations:
        ax.text(x, y, text, ha="center", va="center",
                fontsize=5.5, color=GRAY_DARK, fontstyle="italic",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#FAFAFA",
                          edgecolor=GRAY_VLIGHT, linewidth=0.5))

    fig.savefig(os.path.join(OUTDIR, "figure3_platform_coevolution.png"))
    plt.close(fig)
    print("  Saved figure3_platform_coevolution.png")


# ============================================================
# FIGURE 4: Architecture Comparison (v10 vs v11)
# ============================================================

def figure4_architecture_comparison():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 12))

    for ax in (ax1, ax2):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 16)
        ax.axis("off")

    # Category data
    categories_v10 = {
        "A: Theory &\nFramework": ["A1 Paradigm", "A2 Framework", "A3 Devil's Adv.",
                                    "A4 Ethics", "A5 Gap", "A6 Visualizer"],
        "B: Literature": ["B1 Review", "B2 Search", "B3 Effect Size",
                          "B4 Radar", "B5 PDF"],
        "C: Methodology": ["C1 Design", "C2 Qualitative", "C3 Quantitative",
                           "C4 Materials", "C5 Meta-Anlys",
                           "C6 Data Guard", "C7 Error Prev"],
        "D: Data": ["D1 Sampling", "D2 Survey", "D3 Observation", "D4 Interview"],
        "E: Analysis": ["E1 Qual Anlys", "E2 Quant Anlys",
                        "E3 Mixed", "E4 Code Gen", "E5 Sensitivity"],
        "F: Quality": ["F1 Consistency", "F2 Checklist",
                       "F3 Reproducibility", "F4 Bias Detect"],
        "G: Publication": ["G1 Writing", "G2 Formatting",
                           "G3 Peer Review", "G4 Pre-reg"],
        "H: Specialized": ["H1 Ethnography", "H2 Action Res"],
        "I: Systematic\nReview": ["I0 Team Lead", "I1 Screening",
                                   "I2 Extraction", "I3 RAG Builder"],
    }

    categories_v11 = {
        "A: Theory &\nFramework": ["A1 Paradigm", "A2 Framework", "A5 Gap"],
        "B: Literature": ["B1 Review", "B2 Search"],
        "C: Methodology": ["C1 Design", "C2 Qualitative", "C3 Quantitative",
                           "C5 Meta-Anlys"],
        "D: Data": ["D2 Survey", "D4 Interview"],
        "E: Analysis": ["E1 Qual Anlys", "E2 Quant Anlys", "E3 Mixed"],
        "F: Quality": ["(merged into G2)"],
        "G: Publication": ["G1 Writing", "G2 Specialist"],
        "X: Research\nIntegrity": ["X1 Guardian"],
        "I: Systematic\nReview": ["I0 Team Lead", "I1 Screening",
                                   "I2 Extraction", "I3 RAG Builder"],
    }

    # Removed agents for highlighting
    removed_agents = {
        "A3 Devil's Adv.", "A4 Ethics", "A6 Visualizer",
        "B3 Effect Size", "B4 Radar", "B5 PDF",
        "C4 Materials", "C6 Data Guard", "C7 Error Prev",
        "D1 Sampling", "D3 Observation",
        "E4 Code Gen", "E5 Sensitivity",
        "F1 Consistency", "F2 Checklist", "F3 Reproducibility", "F4 Bias Detect",
        "G3 Peer Review", "G4 Pre-reg",
        "H1 Ethnography", "H2 Action Res",
    }

    # "Ghost" entries in v11 to show what was merged
    ghost_agents = {"(merged into G2)"}

    def draw_architecture(ax, categories, title, subtitle, is_v10=False):
        ax.text(5, 15.5, title, ha="center", fontsize=13, fontweight="bold",
                color=GRAY_DARK)
        ax.text(5, 14.9, subtitle, ha="center", fontsize=9, color=GRAY_MED)

        cat_list = list(categories.items())
        n_cats = len(cat_list)
        cat_h = 14.0 / max(n_cats, 1)
        y_start = 14.3

        for i, (cat_name, agents) in enumerate(cat_list):
            y = y_start - i * cat_h
            # Category header
            ax.add_patch(FancyBboxPatch(
                (0.2, y - cat_h + 0.25), 2.3, cat_h - 0.35,
                boxstyle="round,pad=0.05",
                facecolor=GRAY_BG, edgecolor=GRAY_MED,
                linewidth=0.8
            ))
            ax.text(1.35, y - cat_h / 2 + 0.1, cat_name,
                    ha="center", va="center", fontsize=6.5,
                    fontweight="bold", color=GRAY_DARK)

            # Agent boxes with wrapping for large rows
            if agents:
                max_per_row = 4
                agent_w = 1.35
                agent_h_single = cat_h - 0.45
                x_start = 2.8
                x_gap = 0.12

                n_agents = len(agents)
                n_rows = (n_agents + max_per_row - 1) // max_per_row
                row_h = agent_h_single / max(n_rows, 1)

                for j, agent in enumerate(agents):
                    row = j // max_per_row
                    col = j % max_per_row
                    x = x_start + col * (agent_w + x_gap)
                    ay = y - cat_h + 0.3 + (n_rows - 1 - row) * row_h

                    is_removed = is_v10 and agent in removed_agents
                    is_ghost = agent in ghost_agents

                    if is_ghost:
                        fc = "#F5F5F5"
                        ec = GRAY_VLIGHT
                        lw = 0.5
                        tc = GRAY_LIGHT
                        fs = "italic"
                    elif is_removed:
                        fc = "#FFE0E0"
                        ec = "#CC6666"
                        lw = 1.2
                        tc = GRAY_DARK
                        fs = "normal"
                    else:
                        fc = "white"
                        ec = GRAY_MED
                        lw = 0.6
                        tc = GRAY_DARK
                        fs = "normal"

                    ax.add_patch(FancyBboxPatch(
                        (x, ay), agent_w, row_h - 0.06,
                        boxstyle="round,pad=0.03",
                        facecolor=fc, edgecolor=ec, linewidth=lw
                    ))
                    ax.text(x + agent_w / 2, ay + (row_h - 0.06) / 2,
                            agent, ha="center", va="center",
                            fontsize=5.5, color=tc, fontstyle=fs)

    draw_architecture(ax1, categories_v10,
                      "v10 Architecture", "44 agents, 9 categories",
                      is_v10=True)
    draw_architecture(ax2, categories_v11,
                      "v11 Architecture", "24 agents, 9 categories",
                      is_v10=False)

    # Legend
    legend_elements = [
        mpatches.Patch(facecolor="#FFE0E0", edgecolor="#CC6666",
                       linewidth=1.2, label="Removed / merged (20 agents)"),
        mpatches.Patch(facecolor="white", edgecolor=GRAY_MED,
                       linewidth=0.6, label="Retained agent"),
    ]
    fig.legend(handles=legend_elements, loc="lower center", ncol=2,
               fontsize=9, frameon=True, edgecolor=GRAY_VLIGHT)

    fig.suptitle("Figure 4: Architecture Comparison",
                 fontsize=14, fontweight="bold", y=0.99)
    plt.subplots_adjust(wspace=0.12, bottom=0.05, top=0.95)

    fig.savefig(os.path.join(OUTDIR, "figure4_architecture_comparison.png"))
    plt.close(fig)
    print("  Saved figure4_architecture_comparison.png")


# ============================================================
# FIGURE 5: Checkpoint Flow
# ============================================================

def figure5_checkpoint_flow():
    fig, ax = plt.subplots(figsize=(13, 5))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 5)
    ax.axis("off")

    ax.text(6.5, 4.7, "Figure 5: Five REQUIRED Human Checkpoints in Diverga Research Workflow",
            ha="center", fontsize=11, fontweight="bold", color=GRAY_DARK)

    # Workflow stages (between checkpoints)
    stages = [
        "Problem\nDefinition",
        "Paradigm\nSelection",
        "Methodology\nDesign",
        "Data\nCollection Plan",
        "Analysis\nStrategy",
        "Final\nReview",
    ]

    # Checkpoint labels
    checkpoints = [
        "CP1: Problem\nScope",
        "CP2: Paradigm\nCommitment",
        "CP3: Method\nSelection",
        "CP4: Data\nPlan",
        "CP5: Analysis\nApproval",
    ]

    # CA method labels for each checkpoint
    ca_labels = [
        "Articulation",
        "Articulation",
        "Articulation",
        "Articulation",
        "Articulation",
    ]

    # Positions
    stage_w = 1.4
    cp_w = 0.6
    gap = 0.15
    total_w = len(stages) * stage_w + len(checkpoints) * cp_w + (len(stages) + len(checkpoints) - 1) * gap
    x_start = (13 - total_w) / 2

    x = x_start
    y_center = 2.5
    stage_h = 1.4
    cp_h = 1.8

    for i in range(len(stages)):
        # Draw stage
        add_rounded_box(ax, (x, y_center - stage_h / 2), stage_w, stage_h,
                        stages[i], facecolor="#F0F4F8", edgecolor=ACCENT1,
                        fontsize=7, linewidth=0.8)
        x += stage_w + gap

        # Draw checkpoint (if not last stage)
        if i < len(checkpoints):
            # Checkpoint gate
            ax.add_patch(FancyBboxPatch(
                (x, y_center - cp_h / 2), cp_w, cp_h,
                boxstyle="round,pad=0.03",
                facecolor="#FDEEEE", edgecolor="#CC4444",
                linewidth=2.0, zorder=3
            ))
            # REQUIRED label
            ax.text(x + cp_w / 2, y_center + cp_h / 2 + 0.15,
                    "REQUIRED", ha="center", va="bottom",
                    fontsize=5, fontweight="bold", color="#CC4444")
            # Checkpoint label
            ax.text(x + cp_w / 2, y_center + 0.1,
                    checkpoints[i], ha="center", va="center",
                    fontsize=5.5, fontweight="bold", color="#993333",
                    linespacing=1.2)
            # CA method label below
            ax.text(x + cp_w / 2, y_center - cp_h / 2 - 0.2,
                    f"CA: {ca_labels[i]}",
                    ha="center", va="top", fontsize=5.5,
                    color=ACCENT3, fontstyle="italic")
            # Gate icon (horizontal bars)
            bar_x1 = x + 0.05
            bar_x2 = x + cp_w - 0.05
            for bar_y in [y_center - 0.45, y_center - 0.55]:
                ax.plot([bar_x1, bar_x2], [bar_y, bar_y],
                        color="#CC4444", linewidth=1.5, zorder=4)

            # Arrow from stage to checkpoint
            if i > 0:
                pass  # arrows drawn below

            x += cp_w + gap

    # Draw flow arrows
    x = x_start
    for i in range(len(stages)):
        if i > 0:
            ax.annotate("", xy=(x, y_center),
                        xytext=(x - gap, y_center),
                        arrowprops=dict(arrowstyle="->", color=GRAY_MED,
                                        lw=1.5))
        x += stage_w + gap
        if i < len(checkpoints):
            # Stage to checkpoint
            ax.annotate("", xy=(x, y_center),
                        xytext=(x - gap, y_center),
                        arrowprops=dict(arrowstyle="->", color=GRAY_MED,
                                        lw=1.5))
            x += cp_w + gap

    # Bottom annotation
    ax.text(6.5, 0.4,
            "Each checkpoint halts the AI system and requires the researcher to state and justify\n"
            "a decision before proceeding. Decisions propagate to all subsequent agent outputs.",
            ha="center", va="center", fontsize=7.5, color=GRAY_MED,
            fontstyle="italic",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#FAFAFA",
                      edgecolor=GRAY_VLIGHT, linewidth=0.5))

    # CFF label
    ax.text(6.5, 4.25,
            "Cognitive Forcing Functions (Bucinca et al., 2021)",
            ha="center", va="center", fontsize=8, color=ACCENT3,
            fontstyle="italic")

    fig.savefig(os.path.join(OUTDIR, "figure5_checkpoint_flow.png"))
    plt.close(fig)
    print("  Saved figure5_checkpoint_flow.png")


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    print("Generating figures for IJDL Design Case (v2)...")
    print(f"Output directory: {OUTDIR}")
    print()

    figure1_conceptual_framework()
    figure2_edr_cycles()
    figure3_platform_coevolution()
    figure4_architecture_comparison()
    figure5_checkpoint_flow()

    print()
    print("All 5 figures generated successfully.")
    print(f"Files saved to: {OUTDIR}")
