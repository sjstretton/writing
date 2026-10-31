"""Slide figure for the paper deck: fig_backcast.png (numbers as in the paper)."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
BLUE, GREEN, GREY, INK = "#1F4E79", "#2E7D32", "#9AA59C", "#1B1B1B"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.spines.top": False,
    "axes.spines.right": False, "axes.edgecolor": "#6B7B6E", "axes.labelcolor": INK,
    "xtick.color": INK, "ytick.color": INK})
HERE = os.path.dirname(os.path.abspath(__file__))

# Back-cast from 2000, normalized RMSE of GHG excl. LULUCF (paper Table 2, from the CPAT documentation)
c = ["Australia", "United States", "South Africa", "Brazil", "United Kingdom", "China"]
v = [0.05, 0.10, 0.14, 0.26, 0.33, 0.92]
fig, ax = plt.subplots(figsize=(10, 4.6))
y = list(range(len(c)))[::-1]
ax.barh(y, v, color=[BLUE]*5 + [GREY], height=0.6)
for yi, vi in zip(y, v):
    ax.text(vi + 0.015, yi, f"{vi:.2f}", va="center", color=INK)
ax.set_yticks(y); ax.set_yticklabels(c)
ax.set_xlabel("Normalized RMSE of greenhouse gas emissions, back-cast 2000-2017")
ax.set_xlim(0, 1.05); ax.grid(axis="x", color="#E3E8E3"); ax.set_axisbelow(True)
fig.tight_layout(); fig.savefig(os.path.join(HERE, "fig_backcast.png"), dpi=200)
