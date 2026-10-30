"""Slide figure for the paper deck: fig_stylized_run.png (numbers as in the paper)."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
BLUE, GREEN, GREY, INK = "#1F4E79", "#2E7D32", "#9AA59C", "#1B1B1B"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.spines.top": False,
    "axes.spines.right": False, "axes.edgecolor": "#6B7B6E", "axes.labelcolor": INK,
    "xtick.color": INK, "ytick.color": INK})
HERE = os.path.dirname(os.path.abspath(__file__))

# GIMF-lite stylized run, year 10 (paper Table 3; efficiency-case debt from 2.Source/stylized_run_output.txt): GDP gain and public debt by variant
v = ["Debt financed", "Tax financed", "Debt financed,\ncarbon revenue earmarked", "Debt financed,\nefficiency 0.5"]
gdp = [1.53, 1.60, 1.52, 1.08]; debt = [57.2, 49.2, 53.2, 57.4]  # efficiency case from 2.Source/stylized_run_output.txt
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4.6), sharey=True)
y = list(range(4))[::-1]
a1.barh(y, gdp, color=[BLUE, BLUE, BLUE, GREEN], height=0.6)
a2.barh(y, debt, color=[BLUE, BLUE, BLUE, GREEN], height=0.6)
for yi, g, d in zip(y, gdp, debt):
    a1.text(g + 0.03, yi, f"{g:.2f}", va="center", color=INK)
    a2.text(d + 0.8, yi, f"{d:.1f}", va="center", color=INK)
a1.set_yticks(y); a1.set_yticklabels(v, fontsize=11)
a1.set_title("GDP, % above baseline, year 10", fontsize=12, loc="left")
a2.set_title("Public debt, % of GDP, year 10", fontsize=12, loc="left")
a1.set_xlim(0, 1.95); a2.set_xlim(0, 68)
for a in (a1, a2): a.grid(axis="x", color="#E3E8E3"); a.set_axisbelow(True)
fig.tight_layout(); fig.savefig(os.path.join(HERE, "fig_stylized_run.png"), dpi=200)
