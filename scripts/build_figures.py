#!/usr/bin/env python3
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


ROOT = Path(__file__).resolve().parents[1]
OUTS = [ROOT / "figures", ROOT / "paperVII_submission_source" / "figures"]


def box(ax, xy, w, h, text, color):
    p = FancyBboxPatch(xy, w, h, boxstyle="round,pad=0.02,rounding_size=0.02",
                       linewidth=1.2, edgecolor="#20242a", facecolor=color)
    ax.add_patch(p)
    ax.text(xy[0] + w / 2, xy[1] + h / 2, text, ha="center", va="center", fontsize=9)


def arrow(ax, a, b):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=12,
                                 linewidth=1.2, color="#30343b"))


def main():
    fig, ax = plt.subplots(figsize=(10, 4.8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")
    box(ax, (0.3, 3.35), 2.0, 0.8, "base + universal seed", "#dce9f5")
    box(ax, (3.0, 3.35), 2.0, 0.8, "stabilized body\n$M_\\tau$", "#e5efd8")
    box(ax, (5.7, 3.1), 2.5, 1.3, "post-body functional\ngravity + gauge + matter\n+ quantum + counterterms", "#f8e7c6")
    box(ax, (6.0, 1.2), 2.0, 0.75, "stationary packet", "#f2d6d6")
    box(ax, (3.2, 0.45), 2.2, 0.75, "observer restriction", "#e6ddf2")
    box(ax, (0.3, 0.45), 2.0, 0.75, "terminal readouts", "#d8ece8")
    arrow(ax, (2.3, 3.75), (3.0, 3.75))
    arrow(ax, (5.0, 3.75), (5.7, 3.75))
    arrow(ax, (6.95, 3.1), (6.95, 1.95))
    arrow(ax, (6.0, 1.55), (5.4, 0.83))
    arrow(ax, (3.2, 0.83), (2.3, 0.83))
    ax.text(4.95, 4.45, "body freeze", ha="center", fontsize=9, color="#5b682f")
    ax.text(8.4, 2.45, "once-counted stress\nand current", fontsize=9, va="center")
    ax.text(4.9, 2.65, "conditioning", fontsize=8, rotation=90, va="center")
    ax.text(3.95, 2.45, "no terminal-to-body feedback", fontsize=8, rotation=90, va="center")
    fig.tight_layout()
    for out in OUTS:
        out.mkdir(parents=True, exist_ok=True)
        fig.savefig(out / "fig_joint_ledger.pdf", bbox_inches="tight")
    plt.close(fig)
    print("PAPER_VII_FIGURES_BUILT")


if __name__ == "__main__":
    main()
