"""Figures for the brief and the deck of paper 6.5 (numbers as in working paper v0.2).

    python3 make_figures.py      -> fig_stylized_run.png, fig_kenya_need.png

fig_stylized_run: GIMF-lite stylized run, year 10 (working paper, Table 3; 2.Source/stylized_run_output.txt).
fig_kenya_need:   Kenya, 2030, the tool's budget need, pricing revenue and financing gap (working paper, Table 5;
                  2.Source/kenya_run_output.txt). Illustrative tool results, not official estimates.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE, GREEN, LEAF, GREY, INK = "#1F4E79", "#2E7D32", "#97BC62", "#9AA59C", "#1B1B1B"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.edgecolor": "#6B7B6E", "axes.labelcolor": INK,
                     "xtick.color": INK, "ytick.color": INK})
HERE = os.path.dirname(os.path.abspath(__file__))

# 1. Stylized run, year 10
v = ["Debt financed", "Tax financed", "Debt financed,\ncarbon revenue earmarked", "Debt financed,\nefficiency 0.5 not 0.7"]
gdp = [1.53, 1.60, 1.52, 1.08]
debt = [57.2, 49.2, 53.2, 57.4]
col = [BLUE, BLUE, GREEN, GREY]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4.4), sharey=True)
y = list(range(4))[::-1]
a1.barh(y, gdp, color=col, height=0.6)
a2.barh(y, debt, color=col, height=0.6)
for yi, g, d in zip(y, gdp, debt):
    a1.text(g + 0.03, yi, f"{g:.2f}", va="center", color=INK)
    a2.text(d + 0.8, yi, f"{d:.1f}", va="center", color=INK)
a1.set_yticks(y)
a1.set_yticklabels(v, fontsize=11)
a1.set_title("GDP, % above baseline, year 10", fontsize=12, loc="left")
a2.set_title("Public debt, % of GDP, year 10 (start: 50)", fontsize=12, loc="left")
a1.set_xlim(0, 1.95)
a2.set_xlim(0, 68)
for a in (a1, a2):
    a.grid(axis="x", color="#E3E8E3")
    a.set_axisbelow(True)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig_stylized_run.png"), dpi=200)
plt.close(fig)

# 2. Kenya, 2030, percent of GDP
lab = ["Direct budget need", "...after the efficiency gap", "Incremental need: capital",
       "Incremental need: spending\n(land use, non-CO₂, other)", "Carbon pricing revenue\n(US$88/t on power)",
       "Financing gap"]
val = [0.60, 0.81, 0.10, 0.39, 0.05, 0.44]
col = [BLUE, GREY, BLUE, LEAF, GREEN, "#8B2E2E"]
fig, ax = plt.subplots(figsize=(10, 4.4))
y = list(range(len(val)))[::-1]
ax.barh(y, val, color=col, height=0.6)
for yi, x in zip(y, val):
    ax.text(x + 0.01, yi, f"{x:.2f}", va="center", color=INK)
ax.set_yticks(y)
ax.set_yticklabels(lab, fontsize=11)
ax.set_xlim(0, 0.95)
ax.set_title("Kenya, 2030: percent of GDP (illustrative tool results)", fontsize=12, loc="left")
ax.grid(axis="x", color="#E3E8E3")
ax.set_axisbelow(True)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig_kenya_need.png"), dpi=200)
plt.close(fig)
