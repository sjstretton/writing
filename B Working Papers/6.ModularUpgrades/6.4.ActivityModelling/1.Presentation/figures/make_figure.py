"""Slide figure for the paper deck: fig_activity.png (numbers as in the paper)."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
BLUE, GREEN, GREY, INK = "#1F4E79", "#2E7D32", "#9AA59C", "#1B1B1B"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.spines.top": False,
    "axes.spines.right": False, "axes.edgecolor": "#6B7B6E", "axes.labelcolor": INK,
    "xtick.color": INK, "ytick.color": INK})
HERE = os.path.dirname(os.path.abspath(__file__))

# Change in activity over ten years, stylized drivers (paper Table 3)
a = ["Cars in use", "Steel and aluminum", "Passenger travel", "Road freight", "Vans and trucks",
     "Fertilizers", "Electricity, homes", "Cement and clinker", "Home heat", "Km per car"]
v = [64, 42, 41, 35, 35, 31, 28, 20, 19, 1]
fig, ax = plt.subplots(figsize=(10, 4.8))
y = list(range(len(a)))[::-1]
ax.barh(y, v, color=[GREEN] + [BLUE]*9, height=0.62)
for yi, vi in zip(y, v):
    ax.text(vi + 0.8, yi, f"+{vi}%", va="center", color=INK, fontsize=11)
ax.set_yticks(y); ax.set_yticklabels(a, fontsize=11)
ax.set_xlabel("Change over 10 years: population +1% and income per person +2% a year")
ax.set_xlim(0, 72); ax.grid(axis="x", color="#E3E8E3"); ax.set_axisbelow(True)
fig.tight_layout(); fig.savefig(os.path.join(HERE, "fig_activity.png"), dpi=200)
