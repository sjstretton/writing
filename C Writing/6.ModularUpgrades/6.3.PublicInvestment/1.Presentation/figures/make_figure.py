"""Slide figure for the paper deck: fig_lenses.png (numbers as in the paper)."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
BLUE, GREEN, GREY, INK = "#1F4E79", "#2E7D32", "#9AA59C", "#1B1B1B"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.spines.top": False,
    "axes.spines.right": False, "axes.edgecolor": "#6B7B6E", "axes.labelcolor": INK,
    "xtick.color": INK, "ytick.color": INK})
HERE = os.path.dirname(os.path.abspath(__file__))

# Net annual benefit of one year's 2030 investment, US$ billion (paper Table 1)
g = ["Advanced economies", "China", "Developing,\nexcluding China"]
mkt = [161, 74, 45]; six = [151, 74, 131]
import numpy as np
x = np.arange(len(g)); w = 0.36
fig, ax = plt.subplots(figsize=(10, 4.6))
b1 = ax.bar(x - w/2 - 0.01, mkt, w, color=BLUE, label="At market cost of capital")
b2 = ax.bar(x + w/2 + 0.01, six, w, color=GREEN, label="At a 6% social rate")
for bars in (b1, b2):
    for b in bars:
        ax.text(b.get_x() + b.get_width()/2, b.get_height() + 3, f"{b.get_height():.0f}", ha="center", color=INK)
ax.set_xticks(x); ax.set_xticklabels(g)
ax.set_ylabel("Savings less capital charge, US$ bn a year")
ax.set_ylim(0, 185); ax.legend(frameon=False, loc="upper right")
ax.grid(axis="y", color="#E3E8E3"); ax.set_axisbelow(True)
fig.tight_layout(); fig.savefig(os.path.join(HERE, "fig_lenses.png"), dpi=200)
