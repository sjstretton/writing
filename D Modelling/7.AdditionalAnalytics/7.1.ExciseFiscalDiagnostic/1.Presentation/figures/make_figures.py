"""Figures for paper 7.1 (working paper v0.4, brief v1.0 and deck), with the numbers of the papers.

fig_corrective.png  Country A (stylized): the corrective rate for petrol and diesel split into carbon,
                    local air pollution and distance-related costs (after the mileage share), with the
                    low-high range and the current excise. Numbers: 2.Source/stylized_example.py.
fig_countries.png   Sierra Leone and Liberia: excise revenue on two definitions against the OECD African
                    mean, and petrol tax per liter against the spine's carbon component.
                    Sources: 2.Source/country_metrics_SLE_LBR.csv (the diagnostic; illustrative results,
                    not official estimates) and 2.Source/africa_excise_benchmark.csv (OECD 2025).
Run:  python3 make_figures.py
Palette validated with the dataviz validator (31 Oct 2026): green #2E7D32, blue #2F6DA8, amber #C9822B.
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

GREEN, BLUE, AMBER, GREY, INK, MUTED = "#2E7D32", "#2F6DA8", "#C9822B", "#9AA59C", "#1B1B1B", "#5B665E"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.edgecolor": "#8A968C", "axes.labelcolor": INK,
                     "xtick.color": INK, "ytick.color": INK})
HERE = os.path.dirname(os.path.abspath(__file__))

# ---- Figure 1: corrective benchmark, Country A (stylized) ------------------------------------
# central components, USD per liter (stylized_example.py, Table 4); distance-related = beta x (cong+acc+road)
comp = {"Petrol": (0.114, 0.04, 0.5 * 0.30), "Diesel": (0.134, 0.15, 0.5 * 0.30)}
rng = {"Petrol": (0.126, 0.673), "Diesel": (0.196, 0.912)}
current = {"Petrol": 0.30, "Diesel": 0.18}
labels = ["Carbon (USD 50/t)", "Local air pollution", "Congestion, accidents, road damage (x 0.5)"]
colors = [GREEN, BLUE, AMBER]
fig, ax = plt.subplots(figsize=(10, 4.8))
x = np.arange(2)
w = 0.42
for j, f in enumerate(("Petrol", "Diesel")):
    bottom = 0.0
    for k, v in enumerate(comp[f]):
        ax.bar(x[j], v - 0.003, w, bottom=bottom, color=colors[k], label=labels[k] if j == 0 else None,
               edgecolor="white", linewidth=2)
        bottom += v
    t = sum(comp[f])
    xr = x[j] + w / 2 + 0.10
    ax.errorbar(xr, t, yerr=[[t - rng[f][0]], [rng[f][1] - t]], fmt="o", color=MUTED, ecolor=MUTED,
                markersize=5, capsize=6, lw=1.4)
    ax.text(xr + 0.05, t, f"Corrective rate {t:.2f}\n(range {rng[f][0]:.2f}–{rng[f][1]:.2f})",
            va="center", ha="left", fontsize=10.5, color=INK)
    ax.plot([x[j] - w / 2 - 0.05, x[j] + w / 2 + 0.02], [current[f]] * 2, color=INK, lw=2.2, ls=(0, (4, 2)))
    ax.text(x[j] - w / 2 - 0.07, current[f], f"Current\nexcise {current[f]:.2f}", va="center", ha="right",
            fontsize=10.5, color=INK)
ax.set_xticks(x)
ax.set_xticklabels(["Petrol", "Diesel"])
ax.set_xlim(-0.85, 1.85)
ax.set_ylabel("US dollars per liter")
ax.set_ylim(0, 1.0)
ax.legend(frameon=False, loc="upper left", fontsize=10.5)
ax.grid(axis="y", color="#E6EAE6")
ax.set_axisbelow(True)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig_corrective.png"), dpi=200)
plt.close(fig)

# ---- Figure 2: Sierra Leone and Liberia ------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(11, 4.8))
ax = axes[0]
names = ["Sierra Leone\nreported by\nthe diagnostic\n2024–25", "Sierra Leone\nOECD data\n2023",
         "Liberia\nexcise law\nonly, FY2024", "Liberia\nwith fuel and\nroad levies,\nFY2024", "African\nmean, 37\ncountries\n2023"]
vals = [1.265, 0.57, 0.373, 1.254, 1.32]
txt = ["1.25–1.28", "0.57", "0.37", "1.25", "1.32"]
cols = [BLUE, GREY, BLUE, BLUE, GREY]
bars = ax.bar(range(5), vals, color=cols, width=0.62)
for b, t in zip(bars, txt):
    ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.03, t, ha="center", color=INK, fontsize=10.5)
ax.set_xticks(range(5))
ax.set_xticklabels(names, fontsize=9)
ax.set_ylim(0, 1.6)
ax.set_title("Excise revenue, percent of GDP", loc="left", fontsize=12.5, color=INK)
ax.grid(axis="y", color="#E6EAE6")
ax.set_axisbelow(True)

ax = axes[1]
names = ["Sierra Leone\npetrol excise", "Liberia\npetrol levies", "Carbon cost\nalone at\nUSD 50/t", "Carbon cost\nalone at\nUSD 185/t"]
vals = [0.23, 0.095, 0.114, 0.423]
txt = ["0.23", "0.095", "0.11", "0.42"]
cols = [BLUE, BLUE, GREEN, GREEN]
bars = ax.bar(range(4), vals, color=cols, width=0.62)
for b, t in zip(bars, txt):
    ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.01, t, ha="center", color=INK, fontsize=10.5)
ax.set_xticks(range(4))
ax.set_xticklabels(names, fontsize=9.5)
ax.set_ylim(0, 0.5)
ax.set_title("Petrol, US dollars per liter, 2026", loc="left", fontsize=12.5, color=INK)
ax.grid(axis="y", color="#E6EAE6")
ax.set_axisbelow(True)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig_countries.png"), dpi=200)
plt.close(fig)
print("wrote fig_corrective.png, fig_countries.png")
