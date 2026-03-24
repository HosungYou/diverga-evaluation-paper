#!/usr/bin/env python3
"""
Generate academic figures for the Diverga Design Case paper.
Figures are saved to ./figures/ directory at 300 DPI.

Authors: Hosung You, Mohan Yang
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

# Output directory
FIGURES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)

# Academic style settings
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'serif'],
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.15,
    'text.color': '#1a1a1a',
    'axes.edgecolor': '#333333',
    'axes.labelcolor': '#1a1a1a',
})


def figure1_architecture():
    """
    Figure 1: Diverga System Architecture.
    Shows 9 categories (A-I, X) with their agents in a clean grid layout.
    """
    fig, ax = plt.subplots(figsize=(10, 7.5))
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-1.0, 9.5)
    ax.axis('off')

    # Title
    ax.text(5.0, 9.0, "Diverga v12.0: 24-Agent Architecture",
            ha='center', va='center', fontsize=14, fontweight='bold',
            fontfamily='serif')
    ax.text(5.0, 8.5, "9 Categories Covering the Complete Research Lifecycle",
            ha='center', va='center', fontsize=10, fontstyle='italic',
            color='#555555', fontfamily='serif')

    # Category data: (name, agents_list, color_shade)
    categories = [
        ("A: Research\nFoundation", ["A1: RQ Refiner", "A2: Theory Architect", "A5: Paradigm Advisor"], '#2c2c2c'),
        ("B: Literature\n& Evidence", ["B1: Literature Scout", "B2: Quality Appraiser"], '#3d3d3d'),
        ("C: Study\nDesign", ["C1: Quant Design", "C2: Qual Design", "C3: Mixed Methods", "C5: Meta-Analysis"], '#4e4e4e'),
        ("D: Data\nCollection", ["D2: Collection Spec.", "D4: Instrument Dev."], '#5f5f5f'),
        ("E: Analysis", ["E1: Quant Analysis", "E2: Qual Coding", "E3: Mixed Integration"], '#4e4e4e'),
        ("F: Quality &\nValidation", ["F5: Humanization\n     Verifier"], '#6a6a6a'),
        ("G: Publication &\nCommunication", ["G1: Journal Matcher", "G2: Publication Spec.", "G5: Style Auditor", "G6: Style Humanizer"], '#3d3d3d'),
        ("I: Systematic\nReview", ["I0: SR Orchestrator", "I1: Paper Retrieval", "I2: Screening Asst.", "I3: RAG Builder"], '#2c2c2c'),
        ("X: Cross-\nCutting", ["X1: Research\n     Guardian"], '#5f5f5f'),
    ]

    # Layout: 3 columns x 3 rows
    positions = [
        (0.3, 6.8),   # A
        (3.7, 6.8),   # B
        (7.1, 6.8),   # C
        (0.3, 4.2),   # D
        (3.7, 4.2),   # E
        (7.1, 4.2),   # F
        (0.3, 1.5),   # G
        (3.7, 1.5),   # I
        (7.1, 1.5),   # X
    ]

    box_w = 2.9
    header_h = 0.55

    for idx, ((name, agents, color), (px, py)) in enumerate(zip(categories, positions)):
        n_agents = len(agents)
        agent_h = 0.35
        total_agent_h = n_agents * agent_h + 0.15
        total_h = header_h + total_agent_h

        # Category header box
        header_box = FancyBboxPatch(
            (px, py), box_w, header_h,
            boxstyle="round,pad=0.05",
            facecolor=color, edgecolor='#1a1a1a', linewidth=1.2
        )
        ax.add_patch(header_box)
        ax.text(px + box_w / 2, py + header_h / 2, name,
                ha='center', va='center', fontsize=9, fontweight='bold',
                color='white', fontfamily='serif')

        # Agent list area
        agent_box = FancyBboxPatch(
            (px, py - total_agent_h), box_w, total_agent_h,
            boxstyle="round,pad=0.05",
            facecolor='#f5f5f5', edgecolor='#999999', linewidth=0.8,
            linestyle='-'
        )
        ax.add_patch(agent_box)

        # Individual agent labels
        for j, agent_name in enumerate(agents):
            y_pos = py - 0.12 - (j + 0.5) * agent_h
            ax.text(px + 0.15, y_pos, agent_name,
                    ha='left', va='center', fontsize=7.5,
                    fontfamily='serif', color='#2a2a2a')

    # Legend for model tiers
    legend_y = -0.5
    ax.text(1.0, legend_y, "Model Routing:",
            ha='left', va='center', fontsize=9, fontweight='bold', fontfamily='serif')

    tier_labels = [
        ("Opus (13 agents): High-stakes decisions", '#2c2c2c'),
        ("Sonnet (9 agents): Moderate complexity", '#666666'),
        ("Haiku (2 agents): Lightweight tasks", '#999999'),
    ]
    for i, (label, color) in enumerate(tier_labels):
        x_start = 3.5 + i * 2.5
        rect = plt.Rectangle((x_start, legend_y - 0.12), 0.25, 0.25,
                              facecolor=color, edgecolor='#333333', linewidth=0.6)
        ax.add_patch(rect)
        ax.text(x_start + 0.35, legend_y, label,
                ha='left', va='center', fontsize=7.5, fontfamily='serif')

    save_path = os.path.join(FIGURES_DIR, "figure1_architecture.png")
    fig.savefig(save_path, dpi=300, facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"Saved: {save_path}")


def figure2_checkpoint_flow():
    """
    Figure 2: Human Checkpoint Flow.
    Flowchart showing research workflow with 5 REQUIRED checkpoint positions
    and RECOMMENDED checkpoints distinguished by line style.
    """
    fig, ax = plt.subplots(figsize=(11, 6.5))
    ax.set_xlim(-0.5, 11)
    ax.set_ylim(-1.5, 6.5)
    ax.axis('off')

    # Title
    ax.text(5.25, 6.1, "Human Checkpoint System: Research Workflow with Decision Gates",
            ha='center', va='center', fontsize=13, fontweight='bold', fontfamily='serif')

    # Workflow stages (boxes) and checkpoints (diamonds/gates)
    # Layout: horizontal flow with checkpoints between stages

    # Stage definitions: (x, y, label, width)
    stages = [
        (0.2, 3.5, "Research\nQuestion\nFormulation", 1.5),
        (2.8, 3.5, "Paradigm &\nTheory\nSelection", 1.5),
        (5.4, 3.5, "Research\nDesign &\nMethodology", 1.5),
        (8.0, 3.5, "Data\nCollection\n& Analysis", 1.5),
        (10.0, 3.5, "Writing &\nPublication", 1.2),
    ]

    # Checkpoint definitions: (x, y, label, level)
    # level: 'required' or 'recommended'
    checkpoints = [
        (2.15, 3.8, "CP_RESEARCH\n_DIRECTION", "required"),
        (4.55, 4.5, "CP_PARADIGM\n_SELECTION", "required"),
        (4.55, 3.1, "CP_THEORY\n_SELECTION", "required"),
        (7.15, 3.8, "CP_METHOD\n_APPROVAL", "required"),
        (9.35, 3.8, "CP_ANALYSIS\n_PLAN", "recommended"),
    ]

    stage_h = 1.1

    # Draw stages
    for (sx, sy, label, sw) in stages:
        box = FancyBboxPatch(
            (sx, sy - stage_h / 2), sw, stage_h,
            boxstyle="round,pad=0.08",
            facecolor='#e8e8e8', edgecolor='#333333', linewidth=1.2
        )
        ax.add_patch(box)
        ax.text(sx + sw / 2, sy, label,
                ha='center', va='center', fontsize=8, fontweight='bold',
                fontfamily='serif', linespacing=1.3)

    # Draw checkpoints as diamond shapes
    def draw_diamond(cx, cy, label, level):
        diamond_size = 0.42
        if level == "required":
            fc = '#333333'
            ec = '#1a1a1a'
            tc = 'white'
            lw = 1.8
            ls = '-'
        else:
            fc = 'white'
            ec = '#555555'
            tc = '#333333'
            lw = 1.2
            ls = '--'

        diamond = plt.Polygon(
            [(cx, cy + diamond_size),
             (cx + diamond_size, cy),
             (cx, cy - diamond_size),
             (cx - diamond_size, cy)],
            closed=True, facecolor=fc, edgecolor=ec,
            linewidth=lw, linestyle=ls, zorder=5
        )
        ax.add_patch(diamond)

        # Label below diamond
        ax.text(cx, cy - diamond_size - 0.22, label,
                ha='center', va='top', fontsize=6.5,
                fontfamily='serif', fontweight='bold',
                color='#2a2a2a', linespacing=1.1)

    for cp in checkpoints:
        draw_diamond(*cp)

    # Draw arrows connecting stages
    arrow_props = dict(
        arrowstyle='->', color='#444444', linewidth=1.3,
        connectionstyle='arc3,rad=0.0', mutation_scale=12
    )

    # Stage 1 -> CP1 -> Stage 2
    ax.annotate('', xy=(2.15 - 0.42, 3.8), xytext=(1.7, 3.8), arrowprops=arrow_props)
    ax.annotate('', xy=(2.8, 3.8), xytext=(2.15 + 0.42, 3.8), arrowprops=arrow_props)

    # Stage 2 -> CP2 (up) and CP3 (down)
    ax.annotate('', xy=(4.55 - 0.42, 4.5), xytext=(4.3, 4.0),
                arrowprops=dict(arrowstyle='->', color='#444444', linewidth=1.0,
                                connectionstyle='arc3,rad=-0.2', mutation_scale=10))
    ax.annotate('', xy=(4.55 - 0.42, 3.1), xytext=(4.3, 3.5),
                arrowprops=dict(arrowstyle='->', color='#444444', linewidth=1.0,
                                connectionstyle='arc3,rad=0.2', mutation_scale=10))

    # CP2 and CP3 -> Stage 3
    ax.annotate('', xy=(5.4, 4.0), xytext=(4.55 + 0.42, 4.5),
                arrowprops=dict(arrowstyle='->', color='#444444', linewidth=1.0,
                                connectionstyle='arc3,rad=0.2', mutation_scale=10))
    ax.annotate('', xy=(5.4, 3.5), xytext=(4.55 + 0.42, 3.1),
                arrowprops=dict(arrowstyle='->', color='#444444', linewidth=1.0,
                                connectionstyle='arc3,rad=-0.2', mutation_scale=10))

    # Stage 3 -> CP4 -> Stage 4
    ax.annotate('', xy=(7.15 - 0.42, 3.8), xytext=(6.9, 3.8), arrowprops=arrow_props)
    ax.annotate('', xy=(8.0, 3.8), xytext=(7.15 + 0.42, 3.8), arrowprops=arrow_props)

    # Stage 4 -> CP5 -> Stage 5
    ax.annotate('', xy=(9.35 - 0.42, 3.8), xytext=(9.5, 3.8), arrowprops=arrow_props)
    ax.annotate('', xy=(10.0, 3.8), xytext=(9.35 + 0.42, 3.8), arrowprops=arrow_props)

    # Checkpoint behavior annotation
    behavior_y = 1.2
    ax.text(5.25, behavior_y + 0.6, "Checkpoint Behavior Protocol",
            ha='center', va='center', fontsize=10, fontweight='bold', fontfamily='serif')

    protocol_steps = [
        "1. STOP immediately at checkpoint",
        "2. Present options with VS alternatives and T-Scores",
        "3. WAIT for explicit human approval",
        "4. DO NOT proceed until approval is received",
    ]
    for i, step in enumerate(protocol_steps):
        ax.text(5.25, behavior_y - 0.05 - i * 0.32, step,
                ha='center', va='center', fontsize=8, fontfamily='serif',
                color='#333333')

    # Legend
    legend_y = -0.9

    # Required diamond
    d_size = 0.18
    lx = 2.0
    d1 = plt.Polygon(
        [(lx, legend_y + d_size), (lx + d_size, legend_y),
         (lx, legend_y - d_size), (lx - d_size, legend_y)],
        closed=True, facecolor='#333333', edgecolor='#1a1a1a', linewidth=1.5, zorder=5
    )
    ax.add_patch(d1)
    ax.text(lx + 0.35, legend_y, "REQUIRED checkpoint (system halts, must approve)",
            ha='left', va='center', fontsize=8, fontfamily='serif')

    # Recommended diamond
    lx2 = 7.0
    d2 = plt.Polygon(
        [(lx2, legend_y + d_size), (lx2 + d_size, legend_y),
         (lx2, legend_y - d_size), (lx2 - d_size, legend_y)],
        closed=True, facecolor='white', edgecolor='#555555',
        linewidth=1.2, linestyle='--', zorder=5
    )
    ax.add_patch(d2)
    ax.text(lx2 + 0.35, legend_y, "RECOMMENDED checkpoint (system pauses, suggests approval)",
            ha='left', va='center', fontsize=8, fontfamily='serif')

    save_path = os.path.join(FIGURES_DIR, "figure2_checkpoint_flow.png")
    fig.savefig(save_path, dpi=300, facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"Saved: {save_path}")


def figure3_evolution_timeline():
    """
    Figure 3: Design Evolution Timeline.
    Horizontal timeline from v1.0 to v12.0 with agent count overlay.
    """
    fig, ax1 = plt.subplots(figsize=(12, 5))

    # Version milestones with dates and agent counts
    versions = [
        ("v1.0", "Jan 22", 20, "Initial commit\n(Research Coordinator)"),
        ("v2.0", "Jan 22", 20, "VS integration"),
        ("v3.0", "Jan 23", 21, "Creativity Suite"),
        ("v4.0", "Jan 25", 21, "Architecture\nrestructure"),
        ("v5.0", "Jan 25", 33, "Sisyphus Edition\n(+12 agents)"),
        ("v6.0", "Jan 25", 27, "Renamed to Diverga;\nremoved Sisyphus"),
        ("v6.7", "Jan 30", 44, "Systematic Review\n(peak: 44 agents)"),
        ("v7.0", "Feb 3", 44, "Memory System"),
        ("v8.1", "Feb 9", 44, "Checkpoint\nenforcement fix"),
        ("v9.0", "Feb 15", 44, "SQLite + MCP\nserver split"),
        ("v10.0", "Feb 23", 44, "Discourse-level\ndetection"),
        ("v11.0", "Mar 10", 24, "Consolidation\n(44 to 24)"),
        ("v12.0", "Mar 19", 24, "Unified\norchestrator"),
    ]

    x_positions = np.arange(len(versions))
    labels = [v[0] for v in versions]
    dates = [v[1] for v in versions]
    agent_counts = [v[2] for v in versions]
    milestones = [v[3] for v in versions]

    # Plot agent count as area + line
    ax1.fill_between(x_positions, agent_counts, alpha=0.15, color='#333333', step='mid')
    ax1.plot(x_positions, agent_counts, 'o-', color='#333333', linewidth=2,
             markersize=6, markerfacecolor='#555555', markeredgecolor='#222222',
             markeredgewidth=1.0, zorder=5)

    # Annotate agent counts on the line
    for i, (x, y) in enumerate(zip(x_positions, agent_counts)):
        offset_y = 2.5 if i != 6 else 3.0  # Extra offset at peak
        ax1.annotate(str(y), (x, y), textcoords="offset points",
                     xytext=(0, 10), ha='center', fontsize=8,
                     fontweight='bold', fontfamily='serif', color='#222222')

    # Milestone labels (alternate above and below)
    for i, (x, milestone) in enumerate(zip(x_positions, milestones)):
        if i % 2 == 0:
            y_text = -8
            va = 'top'
        else:
            y_text = -5
            va = 'top'

        ax1.text(x, -2.5 - (i % 2) * 4, milestone,
                 ha='center', va='top', fontsize=6.5,
                 fontfamily='serif', color='#444444',
                 linespacing=1.2,
                 bbox=dict(boxstyle='round,pad=0.2', facecolor='#f0f0f0',
                           edgecolor='#cccccc', linewidth=0.5))

    # Key milestone highlights
    highlight_indices = [0, 5, 6, 8, 11]  # initial, naming, peak, checkpoint fix, consolidation
    for idx in highlight_indices:
        ax1.axvline(x=x_positions[idx], color='#aaaaaa', linewidth=0.6,
                    linestyle=':', alpha=0.7, zorder=1)

    # Axes configuration
    ax1.set_xticks(x_positions)
    ax1.set_xticklabels([f"{labels[i]}\n({dates[i]})" for i in range(len(labels))],
                         fontsize=7.5, fontfamily='serif', rotation=0)
    ax1.set_ylabel("Number of Agents", fontsize=11, fontfamily='serif')
    ax1.set_ylim(-12, 52)
    ax1.set_xlim(-0.5, len(versions) - 0.5)

    # Only show agent count ticks in positive range
    ax1.set_yticks([0, 10, 20, 30, 40, 50])
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['bottom'].set_position(('data', 0))
    ax1.tick_params(axis='y', labelsize=9)

    # Title
    ax1.set_title("Diverga Design Evolution: From Research Coordinator to v12.0\n"
                   "January 22 to March 19, 2026 (57 days, 224 commits)",
                   fontsize=12, fontweight='bold', fontfamily='serif', pad=15)

    # Phase annotations
    phase_specs = [
        (0, 3, "Phase 1:\nRapid Expansion", '#888888'),
        (4, 6, "Phase 2:\nPeak & Pivot", '#666666'),
        (7, 10, "Phase 3:\nInfrastructure", '#888888'),
        (11, 12, "Phase 4:\nConsolidation", '#666666'),
    ]
    for start, end, phase_label, color in phase_specs:
        mid = (x_positions[start] + x_positions[end]) / 2
        ax1.annotate(phase_label,
                     xy=(mid, 49), ha='center', va='top',
                     fontsize=7.5, fontfamily='serif', fontstyle='italic',
                     color=color)
        ax1.annotate('', xy=(x_positions[start], 47), xytext=(x_positions[end], 47),
                     arrowprops=dict(arrowstyle='<->', color=color,
                                     linewidth=0.8, linestyle='-'))

    plt.tight_layout()
    save_path = os.path.join(FIGURES_DIR, "figure3_evolution_timeline.png")
    fig.savefig(save_path, dpi=300, facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"Saved: {save_path}")


if __name__ == "__main__":
    print("Generating figures for Diverga Design Case paper...")
    print("=" * 55)

    figure1_architecture()
    figure2_checkpoint_flow()
    figure3_evolution_timeline()

    print("=" * 55)
    print("All figures generated successfully.")
    print(f"Output directory: {FIGURES_DIR}")
