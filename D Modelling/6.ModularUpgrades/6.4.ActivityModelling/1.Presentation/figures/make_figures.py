"""Brief and deck figure for Climate Fiscal Policy Brief No. 6.4 (activity levels across four models).

Draws fig_activity.png from the same rule, parameters and numbers as the working paper's worked example
(../../2.Source/activity_layer.py, Table 3): growth of each activity over ten years with population +1% and
income per person +2% a year, elasticities held fixed. Stylized drivers.

Run: python3 make_figures.py   (writes fig_activity.png beside this script)
"""
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "2.Source"))
from activity_layer import ROWS, growth  # noqa: E402

BLUE, GREEN, INK, MUTED, GRID = "#1F4E79", "#2E7D32", "#1B1B1B", "#6B7B6E", "#E3E8E3"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.edgecolor": MUTED, "axes.labelcolor": INK,
                     "xtick.color": INK, "ytick.color": INK})

SHORT = {
    "Electricity, homes, at USD 3,000 per person": "Electricity, homes",
    "Passenger travel (passenger-km)": "Passenger travel",
    "Road freight (tonne-km)": "Road freight",
    "Home heat, hot water and cooking (useful heat)": "Home heat",
    "Cars in use, below 300 per 1,000 people": "Cars in use",
}


def main():
    data = sorted(((SHORT.get(n, n), 100 * (growth(b, e) - 1)) for n, b, e, _ in ROWS), key=lambda r: r[1])
    labels, vals = zip(*data)
    fig, ax = plt.subplots(figsize=(10, 4.8))
    y = range(len(labels))
    colors = [GREEN if lab in ("Cars in use", "Passenger travel") else BLUE for lab in labels]
    ax.barh(list(y), vals, color=colors, height=0.62)
    for yi, vi in zip(y, vals):
        ax.text(vi + 0.8, yi, f"+{vi:.0f}%", va="center", color=INK, fontsize=10.5)
    ax.set_yticks(list(y))
    ax.set_yticklabels(labels, fontsize=10.5)
    ax.set_xlabel("Change over ten years: population +1% and income per person +2% a year (stylized)")
    ax.set_xlim(0, 72)
    ax.grid(axis="x", color=GRID)
    ax.set_axisbelow(True)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "fig_activity.png"), dpi=200)


if __name__ == "__main__":
    main()
