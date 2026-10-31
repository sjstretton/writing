"""Slide figure for the paper deck: fig_profiles.png (numbers as in the paper)."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
BLUE, GREEN, GREY, INK = "#1F4E79", "#2E7D32", "#9AA59C", "#1B1B1B"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.spines.top": False,
    "axes.spines.right": False, "axes.edgecolor": "#6B7B6E", "axes.labelcolor": INK,
    "xtick.color": INK, "ytick.color": INK})
HERE = os.path.dirname(os.path.abspath(__file__))

# Four economies, 2024 (paper Table 2, from IMF WoRLD and WEO via the pipeline)
c = ["Colombia", "Indonesia", "Morocco", "South Africa"]
tax = [23.0, 10.1, 20.8, 25.2]; itr = [13.5, 15.1, 7.9, 18.9]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4.6), sharey=True)
y = list(range(4))[::-1]
a1.barh(y, tax, color=[BLUE, GREEN, BLUE, BLUE], height=0.6)
a2.barh(y, itr, color=[BLUE, BLUE, BLUE, GREEN], height=0.6)
for yi, t, i in zip(y, tax, itr):
    a1.text(t + 0.4, yi, f"{t:.1f}", va="center", color=INK)
    a2.text(i + 0.3, yi, f"{i:.1f}", va="center", color=INK)
a1.set_yticks(y); a1.set_yticklabels(c)
a1.set_title("Tax revenue, % of GDP", fontsize=12, loc="left")
a2.set_title("Interest, % of revenue", fontsize=12, loc="left")
a1.set_xlim(0, 30); a2.set_xlim(0, 23)
for a in (a1, a2): a.grid(axis="x", color="#E3E8E3"); a.set_axisbelow(True)
fig.tight_layout(); fig.savefig(os.path.join(HERE, "fig_profiles.png"), dpi=200)
