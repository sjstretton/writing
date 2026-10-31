"""Brief figure for Climate Fiscal Policy Brief No. 5.1 (The CPAT Mitigation Module).

Draws the brief's figure from the same functions and numbers as the working paper's Table 2 and
Figure 2 (../../2.Source/worked_examples.py): shares of new power investment under CPAT's logit
rule and under the proposed quadratic-penalty ("velocity") rule, with no carbon price and at
75 US dollars per tonne of CO2. Stylized costs.

Run: python3 make_figures.py   (writes fig1_investment_shares.png beside this script)
"""
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "2.Source"))
from worked_examples import TECH, costs, logit_shares, velocity_shares  # noqa: E402

INK, MUTED, GRID = "#1f1f1e", "#6b6a63", "#d9d8d2"
LOGIT, VELOCITY = "#2a78d6", "#eb6834"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "text.color": INK,
                     "axes.edgecolor": MUTED, "axes.labelcolor": INK,
                     "xtick.color": INK, "ytick.color": MUTED})


def main():
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.0), sharey=True)
    for ax, cp, title in [(axes[0], 0.0, "No carbon price"), (axes[1], 75.0, "Carbon price of 75 USD/tCO2")]:
        c = costs(cp)
        lg = [100 * x for x in logit_shares(c)]
        vl = [100 * x for x in velocity_shares(c)]
        xs = range(len(TECH))
        w = 0.38
        ax.bar([x - w / 2 for x in xs], lg, w, color=LOGIT, label="CPAT logit rule")
        ax.bar([x + w / 2 for x in xs], vl, w, color=VELOCITY, label="Quadratic-penalty rule")
        for x, a, b in zip(xs, lg, vl):
            ax.text(x - w / 2, a + 1, "%.1f" % a, ha="center", fontsize=6.5, color=INK)
            ax.text(x + w / 2, b + 1, "%.1f" % b, ha="center", fontsize=6.5, color=INK)
        ax.set_xticks(list(xs))
        ax.set_xticklabels(TECH)
        ax.set_title(title, fontsize=9, loc="left")
        ax.grid(axis="y", color=GRID, lw=0.6)
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_ylim(0, 62)
    axes[0].set_ylabel("Share of new investment (%)")
    axes[0].legend(frameon=False, fontsize=7.5, loc="upper right")
    fig.tight_layout()
    out = os.path.join(HERE, "fig1_investment_shares.png")
    fig.savefig(out, dpi=220, bbox_inches="tight")
    print("written", out)


if __name__ == "__main__":
    main()
