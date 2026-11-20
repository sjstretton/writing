"""Figures for paper 3.4. Reads the CSVs written by egypt_estimates.py. Run: python3 make_figures.py

fig1-net-cost-by-sector.png   Net cost by sector in 2035 at the local and the de-risked cost of capital
fig2-time-path.png            Investment arrives first, fuel savings later (% of GDP, 2025-2040)
fig3-power-unit-costs.png     Solar, wind and solar with storage against the fuel cost of gas power

Colors: the house palette (blue, orange, aqua; one-hue light-to-dark pair for local and de-risked),
checked with the palette validator: three-slot categorical set passes; the two blues pass as an ordinal pair.
"""
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
OUT = HERE / "figures"
OUT.mkdir(exist_ok=True)

BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
LIGHT, DARK = "#86b6ef", "#184f95"          # local (light) and de-risked (dark): one hue, two steps
INK, INK2, GRID, SURFACE, GAS = "#0b0b0b", "#52514e", "#e6e5e0", "#fcfcfb", "#f0efec"
plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans", "axes.spines.top": False,
                     "axes.spines.right": False, "axes.edgecolor": "#c3c2b7", "axes.linewidth": 0.6,
                     "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6, "axes.axisbelow": True,
                     "xtick.color": INK2, "ytick.color": INK2, "axes.labelcolor": INK2,
                     "figure.dpi": 200, "savefig.bbox": "tight", "figure.facecolor": "white",
                     "axes.facecolor": "white"})


def read(name):
    with open(HERE / name) as f:
        return list(csv.DictReader(f))


def dumbbell(ax, rows, lo_key, hi_key, labels, fmt="{:+.1f}", pad=0.35):
    """One row per item: light dot = local cost of capital, dark dot = de-risked, joined by a hairline."""
    n = len(rows)
    for i, r in enumerate(rows):
        y = n - 1 - i
        a, b = float(r[lo_key]), float(r[hi_key])
        ax.plot([a, b], [y, y], color="#c3c2b7", lw=2, solid_capstyle="round", zorder=2)
        ax.scatter([a], [y], s=70, color=LIGHT, edgecolor="white", linewidth=1.5, zorder=3)
        ax.scatter([b], [y], s=70, color=DARK, edgecolor="white", linewidth=1.5, zorder=3)
        left, right = (b, a) if b <= a else (a, b)
        gap = abs(a - b)
        if gap < 1e-9:
            ax.text(a + pad, y, fmt.format(a), va="center", ha="left", fontsize=9, color=INK)
        else:
            ax.text(left - pad, y, fmt.format(left), va="center", ha="right", fontsize=9, color=INK)
            ax.text(right + pad, y, fmt.format(right), va="center", ha="left", fontsize=9, color=INK)
    ax.set_yticks(range(n), list(reversed(labels)))
    ax.tick_params(axis="y", length=0, labelcolor=INK)
    ax.grid(axis="y", visible=False)
    ax.set_ylim(-0.7, n - 0.3)


def legend_pair(ax, loc="lower right"):
    h = [plt.Line2D([], [], marker="o", ls="", color=LIGHT, markersize=8, label="Local cost of capital, 10.3%"),
         plt.Line2D([], [], marker="o", ls="", color=DARK, markersize=8, label="De-risked, 6%")]
    ax.legend(handles=h, frameon=False, fontsize=8.5, loc=loc, handletextpad=0.3, borderaxespad=0.2)


# ---- Figure 1: net cost by sector, 2035 ------------------------------------------------------------
rows = [r for r in read("egypt_sector_table.csv") if r["year"] == "2035"]
short = {"Power generation, grids and storage": "Power, grids\nand storage", "Transport": "Transport",
         "Buildings": "Buildings", "Industry": "Industry", "Methane, land use and other": "Methane, land\nuse and other"}
tot = {"sector": "All sectors", "net_local": sum(float(r["net_local"]) for r in rows),
       "net_derisked": sum(float(r["net_derisked"]) for r in rows)}
fig, ax = plt.subplots(figsize=(6.6, 3.7))
dumbbell(ax, rows + [tot], "net_local", "net_derisked", [short[r["sector"]] for r in rows] + ["All sectors"])
ax.axvline(0, color=INK2, lw=0.8, zorder=1)
ax.axhline(0.5, color=GRID, lw=0.8)
ax.set_xlim(-8, 10.5)
ax.set_xlabel("Net cost in 2035, US\\$ billion a year (2024 prices). Left of zero: the sector pays for itself")
legend_pair(ax, loc="upper right")
fig.savefig(OUT / "fig1-net-cost-by-sector.png")
plt.close(fig)

# ---- Figure 2: the time path -----------------------------------------------------------------------
p = [r for r in read("egypt_paths.csv") if 2025 <= int(r["year"]) <= 2040]
yrs = [int(r["year"]) for r in p]
pct = lambda k: [100 * float(r[k]) / float(r["gdp"]) for r in p]
series = [("incremental_investment", "Extra investment", BLUE), ("imported_equipment", "of which imported\nequipment (half)", ORANGE),
          ("fuel_saved", "Fuel saved", AQUA)]
fig, ax = plt.subplots(figsize=(6.6, 3.5))
for k, lab, col in series:
    ys = pct(k)
    ax.plot(yrs, ys, color=col, lw=2, solid_capstyle="round", label=lab.replace("\n", " "))
    ax.scatter([yrs[-1]], [ys[-1]], s=40, color=col, edgecolor="white", linewidth=1.5, zorder=3)
    dy = {"incremental_investment": 0.45, "fuel_saved": -0.45, "imported_equipment": 0.0}[k]
    ax.text(yrs[-1] + 0.35, ys[-1] + dy, f"{lab}\n{ys[-1]:.1f}%", va="center", ha="left", fontsize=8.5, color=INK,
            linespacing=1.15)
ax.set_xlim(2025, 2040)
ax.set_ylim(0, 6.2)
ax.set_xticks([2025, 2030, 2035, 2040])
ax.set_ylabel("Percent of GDP")
ax.grid(axis="x", visible=False)
ax.legend(frameon=False, fontsize=8.5, loc="upper left", ncol=3, columnspacing=1.2, handlelength=1.4,
          bbox_to_anchor=(0.0, 1.12))
fig.savefig(OUT / "fig2-time-path.png")
plt.close(fig)

# ---- Figure 3: unit costs in power -----------------------------------------------------------------
u = read("egypt_power_unit_costs.csv")
loc = next(r for r in u if r["lens"].startswith("(a) local"))
der = next(r for r in u if r["lens"].startswith("(b)"))
items = [("Solar", "solar"), ("Wind", "wind"), ("Solar, half its output\nstored (battery \\$125/kWh)", "solar_plus_storage_low"),
         ("Solar, half its output\nstored (battery \\$250/kWh)", "solar_plus_storage_high")]
rows3 = [{"lo": loc[k], "hi": der[k]} for _, k in items]
gas = float(loc["gas_fuel_only"])
fig, ax = plt.subplots(figsize=(6.6, 3.3))
ax.axvspan(gas, gas * 12 / 8.8, color=GAS, zorder=0)
ax.axvline(gas, color=INK2, lw=0.8, zorder=1)
dumbbell(ax, rows3, "lo", "hi", [lab for lab, _ in items], fmt="{:.0f}", pad=2.2)
ax.text(gas + 1.2, 3.42, f"Gas power, fuel alone:\n\\${gas:.0f} at \\$8.8/MMBtu,\n\\${gas * 12 / 8.8:.0f} at \\$12 (LNG)", va="top", ha="left",
        fontsize=8.5, color=INK2, linespacing=1.2)
ax.set_xlim(0, 112)
ax.set_xlabel("US\\$ per MWh (2024 prices)")
legend_pair(ax, loc="lower left")
fig.savefig(OUT / "fig3-power-unit-costs.png")
plt.close(fig)
print("written:", ", ".join(sorted(x.name for x in OUT.glob("*.png"))))
