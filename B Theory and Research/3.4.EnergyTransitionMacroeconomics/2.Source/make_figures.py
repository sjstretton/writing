"""Figures for paper 3.4. Reads the CSVs written by egypt_estimates.py. Run: python3 make_figures.py

fig1-returns.png              The price needed for a further cut rises; the cost of clean equipment falls with deployment
fig2-net-cost-by-sector.png   Net cost by sector in 2035 at the local and the de-risked cost of capital
fig3-time-path.png            Investment first, fuel savings later; the external balance traces a J (% of GDP)
fig4-power-unit-costs.png     Solar, wind and solar with storage against the fuel cost of gas power

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
BOX = dict(facecolor="white", edgecolor="none", pad=1.2, alpha=0.9)
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
            ax.text(a + pad, y, fmt.format(a).replace("-", "\u2212"), va="center", ha="left", fontsize=9, color=INK, bbox=BOX)
        else:
            ax.text(left - pad, y, fmt.format(left).replace("-", "\u2212"), va="center", ha="right", fontsize=9, color=INK, bbox=BOX)
            ax.text(right + pad, y, fmt.format(right).replace("-", "\u2212"), va="center", ha="left", fontsize=9, color=INK, bbox=BOX)
    ax.set_yticks(range(n), list(reversed(labels)))
    ax.tick_params(axis="y", length=0, labelcolor=INK)
    ax.grid(axis="y", visible=False)
    ax.set_ylim(-0.7, n - 0.3)


def legend_pair(ax, loc="lower right"):
    h = [plt.Line2D([], [], marker="o", ls="", color=LIGHT, markersize=8, label="Local cost of capital, 8.2% real"),
         plt.Line2D([], [], marker="o", ls="", color=DARK, markersize=8, label="De-risked, 3.9% real")]
    ax.legend(handles=h, frameon=False, fontsize=8.5, loc=loc, handletextpad=0.3, borderaxespad=0.2)


# ---- Figure 1: the price needed rises with the cut; the cost of equipment falls with deployment -------
rr = read("returns_illustration.csv")
mac = [r for r in rr if r["kind"] == "mac"]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.8, 2.9), gridspec_kw={"wspace": 0.36})
xs = [float(r["x"]) for r in mac]
ys = [float(r["value"]) for r in mac]
a1.plot(xs, ys, color=BLUE, lw=2, solid_capstyle="round")
for x_ in (10, 20, 30):
    y_ = ys[xs.index(float(x_))]
    a1.scatter([x_], [y_], s=40, color=BLUE, edgecolor="white", linewidth=1.5, zorder=3)
    a1.text(x_ - 1.0, y_ + 14, f"\\${y_:.0f}", ha="right", va="bottom", fontsize=8.5, color=INK)
a1.set_xlim(0, 31.5)
a1.set_ylim(0, 400)
a1.set_xticks([0, 10, 20, 30], ["0", "10%", "20%", "30%"])
a1.set_xlabel("Cut in road fuel use from the price alone", fontsize=9)
a1.set_ylabel("Carbon price needed,\nUS\\$ per tonne of CO$_2$", fontsize=9)
a1.grid(axis="x", visible=False)
a1.set_title("Price: each further cut needs\na higher price", fontsize=9.5, color=INK, loc="left")
for kind, lab, col, dy in (("learning_wind", "Onshore wind", ORANGE, 7), ("learning_solar", "Solar", BLUE, -9)):
    lr = [r for r in rr if r["kind"] == kind]
    ns = [int(r["x"]) for r in lr]
    vs = [float(r["value"]) for r in lr]
    a2.plot(ns, vs, color=col, lw=2, solid_capstyle="round")
    a2.scatter([ns[-1]], [vs[-1]], s=40, color=col, edgecolor="white", linewidth=1.5, zorder=3)
    a2.text(ns[-1] + 0.2, vs[-1] + (5 if kind == "learning_wind" else 1), f"{lab}, {vs[-1]:.0f}", va="center", ha="left",
            fontsize=8.5, color=INK)
a2.set_xlim(0, 9.4)
a2.set_xticks(range(0, 7))
a2.set_xlabel("Doublings of cumulative capacity", fontsize=9)
a2.set_ylabel("Installed cost, start = 100", fontsize=9)
a2.set_ylim(0, 105)
a2.grid(axis="x", visible=False)
a2.set_title("Deployment: each doubling makes\nthe next plant cheaper", fontsize=9.5, color=INK, loc="left")
fig.savefig(OUT / "fig1-returns.png")
plt.close(fig)


# ---- Figure 2: net cost by sector, 2035 ------------------------------------------------------------
rows = [r for r in read("egypt_sector_table.csv") if r["year"] == "2035"]
short = {"Power generation, grids and storage": "Power, grids\nand storage", "Transport": "Transport",
         "Buildings": "Buildings", "Industry": "Industry", "Methane, land use and other": "Methane, land\nuse and other"}
tot = {"sector": "All sectors", "net_local": sum(float(r["net_local"]) for r in rows),
       "net_derisked": sum(float(r["net_derisked"]) for r in rows)}
fig, ax = plt.subplots(figsize=(6.6, 3.7))
dumbbell(ax, rows + [tot], "net_local", "net_derisked", [short[r["sector"]] for r in rows] + ["All sectors"])
ax.axvline(0, color=INK2, lw=0.8, zorder=1)
ax.axhline(0.5, color=GRID, lw=0.8)
ax.set_xlim(-8.6, 8.6)
ax.set_xlabel("Net cost in 2035, US\\$ billion a year (2024 prices). Left of zero: the sector pays for itself")
legend_pair(ax, loc="upper right")
fig.savefig(OUT / "fig2-net-cost-by-sector.png")
plt.close(fig)

# ---- Figure 3: the time path and the J in the external balance --------------------------------------
p = [r for r in read("egypt_paths.csv") if 2025 <= int(r["year"]) <= 2040]
yrs = [int(r["year"]) for r in p]
pct = lambda k: [100 * float(r[k]) / float(r["gdp"]) for r in p]
series = [("incremental_investment", "Extra\ninvestment", BLUE, 0.0), ("imported_equipment", "Imported\nequipment", ORANGE, 0.0),
          ("fuel_saved", "Fuel saved", AQUA, 0.0)]
fig, (ax, bx) = plt.subplots(1, 2, figsize=(7.0, 3.0), gridspec_kw={"wspace": 0.8, "width_ratios": [1.0, 1.0]})
for k, lab, col, dy in series:
    ys = pct(k)
    ax.plot(yrs, ys, color=col, lw=2, solid_capstyle="round")
    ax.scatter([yrs[-1]], [ys[-1]], s=40, color=col, edgecolor="white", linewidth=1.5, zorder=3)
    dy = {"incremental_investment": 0.45, "fuel_saved": -0.75, "imported_equipment": 0.0}[k]
    ax.text(yrs[-1] + 0.5, ys[-1] + dy, f"{lab}, {ys[-1]:.1f}", va="center", ha="left", fontsize=8, color=INK, linespacing=1.15)
ax.set_xlim(2025, 2040)
ax.set_ylim(0, 7.6)
ax.set_xticks([2025, 2030, 2035, 2040])
ax.set_ylabel("Percent of GDP", fontsize=9)
ax.grid(axis="x", visible=False)
ax.set_title("Spending first, savings later", fontsize=9.5, color=INK, loc="left")
bx.axhline(0, color=INK2, lw=0.8, zorder=1)
for k, lab, col, xy, ha in (("external_effect_local", "Local cost\nof capital", LIGHT, (2034.6, -0.75), "left"),
                            ("external_effect_derisked", "De-risked", DARK, (2031.2, 0.75), "right")):
    ys = pct(k)
    bx.plot(yrs, ys, color=col, lw=2, solid_capstyle="round")
    bx.text(xy[0], xy[1], lab, va="center", ha=ha, fontsize=8, color=INK, linespacing=1.15)
bx.scatter([yrs[-1]], [ys[-1]], s=40, color=DARK, edgecolor="white", linewidth=1.5, zorder=3)
bx.text(yrs[-1] + 0.5, ys[-1], f"{ys[-1]:+.1f}", va="center", ha="left", fontsize=8, color=INK)
bx.text(2025.4, pct("external_effect_derisked")[0] + 0.42, f'{pct("external_effect_derisked")[0]:+.1f}'.replace("-", "\u2212"), va="center", ha="left",
        fontsize=8, color=INK)
bx.set_xlim(2025, 2040)
bx.set_xticks([2025, 2030, 2035, 2040])
bx.set_ylabel("Percent of GDP", fontsize=9)
bx.grid(axis="x", visible=False)
bx.set_title("Effect on the external balance", fontsize=9.5, color=INK, loc="left")
fig.savefig(OUT / "fig3-time-path.png")
plt.close(fig)

# ---- Figure 4: unit costs in power -----------------------------------------------------------------
u = read("egypt_power_unit_costs.csv")
loc = next(r for r in u if r["lens"].startswith("(a) local"))
der = next(r for r in u if r["lens"].startswith("(b)"))
items = [("Solar", "solar"), ("Wind", "wind"), ("Solar, half its output\nstored (battery \\$125/kWh)", "solar_plus_storage_low"),
         ("Solar, half its output\nstored (battery \\$250/kWh)", "solar_plus_storage_high")]
rows3 = [{"lo": loc[k], "hi": der[k]} for _, k in items]
gas = float(loc["gas_fuel_only"])
fig, ax = plt.subplots(figsize=(6.6, 3.3))
ax.axvspan(gas * 8.8 / 12, gas, color=GAS, zorder=0)
ax.axvline(gas, color=INK2, lw=0.8, zorder=1)
dumbbell(ax, rows3, "lo", "hi", [lab for lab, _ in items], fmt="{:.0f}", pad=2.2)
ax.text(gas + 1.5, 3.42, f"Gas power, fuel alone:\n\\${gas:.0f} at the import price\nof \\$12/MMBtu;\n\\${gas * 8.8 / 12:.0f} at \\$8.8", va="top", ha="left",
        fontsize=8.5, color=INK2, linespacing=1.2)
ax.set_xlim(0, 128)
ax.set_xlabel("US\\$ per MWh (2024 prices)")
legend_pair(ax, loc="lower left")
fig.savefig(OUT / "fig4-power-unit-costs.png")
plt.close(fig)
print("written:", ", ".join(sorted(x.name for x in OUT.glob("*.png"))))
