"""Figures for working paper 5.3 (v0.2), from the numbers published in the CPAT methodology.

fig1_backcast.png    Normalized RMSE of greenhouse gas emissions, back-cast 2000-2017 (paper Table 2)
fig2_sensitivity.png G20 CO2 cut in 2030 under a carbon tax rising to $75, one parameter changed (paper Table 4)

Source of every number: CPAT methodology, chapter 3 (Mitigation), sections Hindcasting and Parameter Sensitivity
Analysis, https://cpmodelai.github.io/cpat_ai/CPAT_full_documentation_html/03_Mitigation.html. Run from this folder.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE, GREEN, GREY, INK, MUTED, GRID = "#1F4E79", "#2E7D32", "#9AA59C", "#1B1B1B", "#5A665C", "#E3E8E3"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.edgecolor": "#6B7B6E", "axes.labelcolor": INK,
                     "xtick.color": INK, "ytick.color": INK})
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(OUT, exist_ok=True)

# Figure 1: back-cast error (GHG excl. LULUCF, normalized RMSE = RMSE / mean observed emissions)
countries = ["Australia", "United States", "South Africa", "Brazil", "United Kingdom", "China"]
nrmse = [0.0505, 0.0966, 0.1383, 0.2551, 0.3285, 0.9151]
fig, ax = plt.subplots(figsize=(8, 3.6))
y = list(range(len(countries)))[::-1]
ax.barh(y, [100 * v for v in nrmse], color=BLUE, height=0.55)
for yi, v in zip(y, nrmse):
    ax.text(100 * v + 1.2, yi, f"{100 * v:.0f}%", va="center", color=INK)
ax.set_yticks(y)
ax.set_yticklabels(countries)
ax.set_xlabel("Level error, percent of mean observed emissions (normalized RMSE)")
ax.set_xlim(0, 105)
ax.grid(axis="x", color=GRID)
ax.set_axisbelow(True)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig1_backcast.png"), dpi=200)
plt.close(fig)

# Figure 2: sensitivity of the 2030 G20 CO2 cut (percent), one parameter at a time; default -29%
rows = [  # (label, cut in percent, is price elasticity)
    ("Price elasticities +2 s.d.", 39, True), ("Price elasticities +1 s.d.", 35, True),
    ("Power model: elasticity", 34, False), ("EIA price forecast", 32, False),
    ("Very high renewables growth", 32, False), ("World energy prices -50%", 31, False),
    ("Income elasticities, multipliers, GDP growth", 29, False),
    ("Power model: engineering", 22, False), ("World energy prices +50%", 20, False),
    ("Price elasticities -1 s.d.", 20, True), ("Price elasticities -2 s.d.", 7, True),
]
fig, ax = plt.subplots(figsize=(8, 4.2))
y = list(range(len(rows)))[::-1]
for yi, (lab, v, el) in zip(y, rows):
    ax.plot([0, v], [yi, yi], color=GRID, lw=2, zorder=1)
    ax.scatter([v], [yi], s=70, color=BLUE if el else GREY, zorder=3, edgecolor="white", linewidth=1.5)
    ax.text(v + 1.0, yi, f"{v}%", va="center", color=INK, fontsize=10)
ax.axvline(29, color=MUTED, ls="--", lw=1)
ax.text(29.4, len(rows) - 0.4, "default 29%", color=MUTED, fontsize=9, va="bottom")
ax.set_yticks(y)
ax.set_yticklabels([r[0] for r in rows])
for t, r in zip(ax.get_yticklabels(), rows):
    t.set_fontweight("bold" if r[2] else "normal")
ax.set_xlim(0, 45)
ax.set_ylim(-0.7, len(rows) - 0.1)
ax.set_xlabel("G20 CO2 cut in 2030 against the baseline (%)")
ax.grid(axis="x", color=GRID)
ax.set_axisbelow(True)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig2_sensitivity.png"), dpi=200)
plt.close(fig)
print("wrote", os.listdir(OUT))
