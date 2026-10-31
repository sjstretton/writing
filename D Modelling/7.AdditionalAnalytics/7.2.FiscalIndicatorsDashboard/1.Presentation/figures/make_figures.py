"""Figures for paper 7.2 (working paper v0.2, brief v1.0 and deck), 31 Oct 2026. Run: python3 make_figures.py

fig_profiles.png    Four economies, 2024: tax revenue, net interest over revenue, fossil fuel subsidies (Table 2 values,
                    as compiled by the dashboard from IMF WoRLD, WEO and the IMF's 2025 subsidy update).
fig_renewables.png  Renewable share of electricity generation, 2024: the dashboard's panel against Ember's observed
                    shares (2.Source/check_public_sources_output.txt).
Numbers are typed here from Table 2 and the check output, so that the figures and the papers carry one set of numbers.
Palette validated with the dataviz validator (#2F6DB5, #C8742A: all checks pass, light mode).
"""
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
BLUE, ORANGE, INK, MUTED, GRID = "#2F6DB5", "#C8742A", "#1B1B1B", "#5E6B60", "#E3E8E3"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.spines.left": False, "axes.edgecolor": "#9AA59C",
                     "xtick.color": MUTED, "ytick.color": INK, "axes.titlesize": 11.5})

C = ["Colombia", "Indonesia", "Morocco", "South Africa"]
TAX = [23.0, 10.1, 20.8, 25.2]          # % of GDP, WoRLD taxes, 2024
NETINT = [13.5, 15.1, 7.9, 18.9]        # net interest, % of revenue, WEO, 2024
EXPL = [0.4, 3.0, 1.9, 0.0]             # explicit fossil fuel subsidies, % of GDP, 2024
IMPL = [5.4, 9.2, 5.0, 12.9]            # implicit, % of GDP, 2024
PANEL_RE = [79.9, 28.0, 29.5, 7.0]      # dashboard panel, renewable share of generation, %, 2024
EMBER_RE = [61.4, 18.1, 24.4, 12.5]     # Ember yearly electricity data, %, 2024


def bars(ax, vals, title, xmax, fmt="{:.1f}"):
    y = list(range(len(C)))[::-1]
    ax.barh(y, vals, color=BLUE, height=0.56)
    for yi, v in zip(y, vals):
        ax.text(v + xmax * 0.015, yi, fmt.format(v), va="center", color=INK, fontsize=10.5)
    ax.set_yticks(y)
    ax.set_yticklabels(C)
    ax.set_xlim(0, xmax)
    ax.set_title(title, loc="left", color=INK)
    ax.grid(axis="x", color=GRID)
    ax.set_axisbelow(True)
    ax.tick_params(axis="y", length=0)


fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(11, 3.7), sharey=True)
bars(a1, TAX, "Tax revenue, % of GDP", 31)
bars(a2, NETINT, "Net interest, % of revenue", 23)
y = list(range(len(C)))[::-1]
a3.barh(y, EXPL, color=ORANGE, height=0.56, label="Explicit", edgecolor="white", linewidth=1.5)
a3.barh(y, IMPL, left=EXPL, color=BLUE, height=0.56, label="Implicit", edgecolor="white", linewidth=1.5)
for yi, e, i in zip(y, EXPL, IMPL):
    a3.text(e + i + 0.3, yi, f"{e:.1f} + {i:.1f}", va="center", color=INK, fontsize=10)
a3.set_xlim(0, 19)
a3.set_title("Fossil fuel subsidies, % of GDP", loc="left", color=INK)
a3.grid(axis="x", color=GRID)
a3.set_axisbelow(True)
a3.tick_params(axis="y", length=0)
a3.legend(frameon=False, loc="upper right", fontsize=9.5)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig_profiles.png"), dpi=200)
plt.close(fig)

fig, ax = plt.subplots(figsize=(7.5, 3.4))
for yi, p, e in zip(y, PANEL_RE, EMBER_RE):
    ax.plot([min(p, e), max(p, e)], [yi, yi], color="#B8C2BA", linewidth=2, zorder=1)
ax.scatter(PANEL_RE, y, s=70, color=ORANGE, label="Dashboard panel (modeled, IMF CPAT-based)", zorder=2,
           edgecolor="white", linewidth=1.5)
ax.scatter(EMBER_RE, y, s=70, color=BLUE, label="Ember (observed generation)", zorder=3, edgecolor="white",
           linewidth=1.5)
for yi, p, e in zip(y, PANEL_RE, EMBER_RE):
    ax.text(p + (2 if p > e else -2), yi + 0.22, f"{p:.1f}", ha="left" if p > e else "right", color=INK, fontsize=9.5)
    ax.text(e + (2 if e > p else -2), yi + 0.22, f"{e:.1f}", ha="left" if e > p else "right", color=INK, fontsize=9.5)
ax.set_yticks(y)
ax.set_yticklabels(C)
ax.set_ylim(-0.6, 3.8)
ax.set_xlim(0, 90)
ax.set_xlabel("Renewable share of electricity generation, 2024, %", color=MUTED)
ax.grid(axis="x", color=GRID)
ax.set_axisbelow(True)
ax.tick_params(axis="y", length=0)
ax.legend(frameon=False, loc="upper center", bbox_to_anchor=(0.5, 1.2), ncol=2, fontsize=9.5)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig_renewables.png"), dpi=200)
plt.close(fig)
print("wrote fig_profiles.png, fig_renewables.png")
