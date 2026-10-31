"""Slide figure for the paper deck: fig_register.png (numbers as in the paper)."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
BLUE, GREEN, GREY, INK = "#1F4E79", "#2E7D32", "#9AA59C", "#1B1B1B"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.spines.top": False,
    "axes.spines.right": False, "axes.edgecolor": "#6B7B6E", "axes.labelcolor": INK,
    "xtick.color": INK, "ytick.color": INK})
HERE = os.path.dirname(os.path.abspath(__file__))

# Register counts at release 1.0.2 (paper Table 1; excel_ai/BUGS.md and ISSUES.md)
labels = ["Legacy bugs", "Issues", "Departures", "Prototype bugs", "Documentation bugs", "Upgrades"]
vals = [228, 135, 35, 22, 20, 14]
fig, ax = plt.subplots(figsize=(10, 4.6))
y = range(len(labels))[::-1]
ax.barh(list(y), vals, color=BLUE, height=0.6)
ax.barh([y[0]], [24], color=GREEN, height=0.6)
for yi, v in zip(y, vals):
    ax.text(v + 3, yi, str(v), va="center", color=INK)
ax.text(12, y[0], "24 high", va="center", ha="center", color="white", fontsize=11, fontweight="bold")
ax.set_yticks(list(y)); ax.set_yticklabels(labels)
ax.set_xlabel("Entries in the CPAT-AI register, release 1.0.2")
ax.set_xlim(0, 255); ax.grid(axis="x", color="#E3E8E3"); ax.set_axisbelow(True)
fig.tight_layout(); fig.savefig(os.path.join(HERE, "fig_register.png"), dpi=200)
