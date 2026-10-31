"""Figures for Climate Fiscal Policy Brief No. 1.2 (feebates).

Run from any directory:  python3 make_figures.py
Writes fig1-power-tax-vs-feebate.png beside this script.

All numbers are stylized, chosen to be round and plausible, not calibrated to a
country. Emission factors are IPCC (2006) defaults (Vol. 2, ch. 1, Table 1.4):
other bituminous coal 94.6 kgCO2/GJ, natural gas 56.1 kgCO2/GJ.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["axes.unicode_minus"] = True

HERE = Path(__file__).resolve().parent

# --- Stylized power system -------------------------------------------------
T = 50.0  # carbon price, $/tCO2

# heat rate (GJ fuel per MWh), emission factor (tCO2/GJ), fuel price ($/GJ),
# non-fuel cost ($/MWh), share of output
PLANTS = {
    "Coal":  dict(heat=10.0, ef=0.0946, fuel=2.5, other=5.0,  share=0.6),
    "Gas":   dict(heat=6.5,  ef=0.0561, fuel=8.0, other=3.0,  share=0.2),
    "Solar": dict(heat=0.0,  ef=0.0,    fuel=0.0, other=40.0, share=0.2),
}

for p in PLANTS.values():
    p["e"] = p["heat"] * p["ef"]                    # tCO2/MWh
    p["cost"] = p["heat"] * p["fuel"] + p["other"]  # $/MWh before policy

e_bar = sum(p["share"] * p["e"] for p in PLANTS.values())  # benchmark = average

tax = {k: T * p["e"] for k, p in PLANTS.items()}
feebate = {k: T * (p["e"] - e_bar) for k, p in PLANTS.items()}
tax["System average"] = T * e_bar
feebate["System average"] = sum(PLANTS[k]["share"] * feebate[k] for k in PLANTS)


def report():
    print(f"benchmark e_bar = {e_bar:.3f} tCO2/MWh")
    avg_cost = sum(p["share"] * p["cost"] for p in PLANTS.values())
    print(f"average generation cost before policy = {avg_cost:.1f} $/MWh")
    for k, p in PLANTS.items():
        print(f"{k:6s} e={p['e']:.3f} cost={p['cost']:.1f} "
              f"tax={tax[k]:+.1f} feebate={feebate[k]:+.1f} "
              f"after tax={p['cost'] + tax[k]:.1f} after feebate={p['cost'] + feebate[k]:.1f}")
    print(f"System average: tax {tax['System average']:+.1f}, feebate {feebate['System average']:+.1f}")
    # fuel price multipliers under the tax
    for name, ef, price in [("coal", 0.0946, 2.5), ("gas", 0.0561, 8.0)]:
        print(f"{name}: +{T * ef:.2f} $/GJ on {price} $/GJ = +{100 * T * ef / price:.0f}%")
    diesel_ef = 0.0741 * 0.036  # tCO2/GJ * GJ/litre
    print(f"diesel: +{T * diesel_ef:.3f} $/l on 1.00 $/l = +{100 * T * diesel_ef:.0f}%")


def fig1():
    surface, ink, ink2, grid = "#ffffff", "#0b0b0b", "#52514e", "#d9d8d4"
    c_tax, c_fee = "#eb6834", "#2a78d6"

    cats = ["Coal", "Gas", "Solar", "System average"]
    fig, ax = plt.subplots(figsize=(6.5, 3.6), dpi=200)
    fig.patch.set_facecolor(surface)
    ax.set_facecolor(surface)

    h = 0.36
    y = range(len(cats))
    for i, c in enumerate(cats):
        for val, off, col in [(tax[c], -h / 2 - 0.02, c_tax), (feebate[c], h / 2 + 0.02, c_fee)]:
            ax.barh(i + off, val, height=h, color=col, edgecolor=surface, linewidth=1)
            if abs(val) < 0.5:
                val = 0.0
            lab = f"{val:+.0f}".replace("-", "\u2212") if val else "0"
            pad = 1.2 if val >= 0 else -1.2
            ax.text(val + pad, i + off, lab, va="center",
                    ha="left" if val >= 0 else "right", fontsize=8, color=ink)

    ax.axvline(0, color=ink2, linewidth=0.8)
    ax.set_yticks(list(y))
    ax.set_yticklabels(cats, fontsize=9, color=ink)
    ax.invert_yaxis()
    ax.set_xlim(-45, 60)
    ax.set_xlabel(r"Change in generation cost at \$50/tCO$_2$, US\$ per MWh (stylized)",
                  fontsize=9, color=ink2)
    ax.tick_params(axis="x", labelsize=8, colors=ink2)
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="x", color=grid, linewidth=0.6)
    ax.set_axisbelow(True)
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(grid)

    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=c_tax, label="Carbon tax"),
                       Patch(color=c_fee, label="Revenue-neutral feebate")],
              loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2, fontsize=8, frameon=False)
    fig.tight_layout()
    out = HERE / "fig1-power-tax-vs-feebate.png"
    fig.savefig(out, facecolor=surface)
    print("wrote", out)


if __name__ == "__main__":
    report()
    fig1()
