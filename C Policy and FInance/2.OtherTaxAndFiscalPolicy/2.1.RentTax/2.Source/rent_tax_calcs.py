"""Calculations for paper 2.1, Taxing Rent, Not Effort (working paper v0.2, brief v1.0).

Writes, into this folder:
  archetypes.csv          the five worked firms (Table 2 of the working paper; the brief's table; the deck)
  revenue.csv             the order-of-magnitude revenue arithmetic (Appendix D)
  figures/fig1_effective_rates.png   effective tax rate on rent, current tax against the design

Every parameter is either the paper's stated design parameter or an assumption labelled as such.
Sourced inputs: Eurostat nama_10_nfa_bs and nama_10_gdp (land value, 2023); OECD Revenue Statistics
(corporate income tax and recurrent property tax as a share of GDP, 2023); Beer, de Mooij and Liu (2020)
(semi-elasticity of reported profit); Torslov, Wier and Zucman (2023) (profit shifted out of high-tax EU countries).
Run from any folder: python3 rent_tax_calcs.py
"""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ---------------------------------------------------------------- design parameters (the paper's)
TAU_1 = 0.50        # Layer One: rate on profit above the normal-return allowance, groups above EUR 750m
TAU_0 = 0.25        # conventional corporate tax rate (the comparison, and the rate below the threshold)
R_ALLOW = 0.03      # allowance rate on equity (illustrative)
T_2 = 0.22          # Layer Two: sectoral destination-based cash-flow tax
TAU_S, D_K, D_W = 0.04, 0.08, 0.25   # Layer Three: sales rate and presence credits (assets ex land, payroll)


def liability(f):
    """Tax under the design for one firm (EUR m, in-country figures)."""
    S, K, W = f["sales"], f["assets"], f["payroll"]
    l1 = f["rate1"] * max(0.0, f["profit"] - R_ALLOW * f["equity"])
    l2 = T_2 * max(0.0, S - f["local_costs"]) if f["designated"] else 0.0
    l3 = max(0.0, TAU_S * S - D_K * K - D_W * W)
    top_up = max(0.0, l2 - l1) + l3                       # Layer Two credited against Layer One
    cap = f["rate1"] * f["global_rent_margin"] * S         # rate on sales-apportioned global rent
    total = max(l1, min(l1 + top_up, cap))
    return dict(L1=l1, L2=l2, L3=l3, cap=cap, total=total)


# ---------------------------------------------------------------- five illustrative firms (stylized)
# global_rent_margin = (global profit - allowance on global equity) / global sales
FIRMS = [
    dict(name="A. Foreign platform, designated sector", short="Foreign platform",
         sales=1000, assets=50, payroll=60, local_costs=100, profit=20, equity=100,
         global_margin=0.35, global_equity_to_sales=0.5, designated=True, rate1=TAU_1),
    dict(name="B. Foreign seller, not designated", short="Foreign seller",
         sales=1000, assets=50, payroll=100, local_costs=150, profit=30, equity=150,
         global_margin=0.20, global_equity_to_sales=0.5, designated=False, rate1=TAU_1),
    dict(name="C. Domestic manufacturer", short="Domestic manufacturer",
         sales=1000, assets=800, payroll=250, local_costs=900, profit=90, equity=600,
         global_margin=0.09, global_equity_to_sales=0.6, designated=False, rate1=TAU_1),
    dict(name="D. Low-margin distributor", short="Low-margin distributor",
         sales=10000, assets=1000, payroll=500, local_costs=9800, profit=200, equity=1000,
         global_margin=0.02, global_equity_to_sales=0.1, designated=False, rate1=TAU_1),
    dict(name="E. Scale-driven manufacturer (carve-out)", short="Scale-driven (carve-out)",
         sales=1000, assets=900, payroll=300, local_costs=920, profit=80, equity=800,
         global_margin=0.08, global_equity_to_sales=0.8, designated=False, rate1=TAU_0),
]


def archetypes():
    rows = []
    for f in FIRMS:
        f["global_rent_margin"] = f["global_margin"] - R_ALLOW * f["global_equity_to_sales"]
        rent_local = f["global_rent_margin"] * f["sales"]          # rent earned from in-country customers
        normal = R_ALLOW * f["global_equity_to_sales"] * f["sales"]
        d = liability(f)
        d3 = max(0.0, TAU_S * f["sales"] - D_K * f["assets"] - D_W * f["payroll"])
        rows.append({
            "firm": f["name"], "short": f["short"],
            "in-country sales": f["sales"], "declared profit": f["profit"],
            "rent from in-country customers": round(rent_local, 1),
            "current tax (25% of declared profit)": round(TAU_0 * f["profit"], 1),
            "Layer One": round(d["L1"], 1), "Layer Two": round(d["L2"], 1),
            "Layer Three before cap": round(d3, 1), "cap": round(d["cap"], 1),
            "total under design": round(d["total"], 1),
            "current rate on rent %": round(100 * TAU_0 * f["profit"] / rent_local),
            "design rate on rent %": round(100 * d["total"] / rent_local),
            "normal return": round(normal, 1),
        })
    return rows


# ---------------------------------------------------------------- revenue arithmetic (Appendix D)
LAND = {"Germany": (1.63, 0.68, 0.20), "France": (3.06, 0.57, 0.28)}   # land/GDP; household share; non-fin. corp. share
TAU_L = 0.025          # land value tax rate (the paper's midpoint)
I_LAND = 0.04          # pre-tax yield used to capitalize land rents (assumption)
ABOVE = (0.3, 0.5)     # share of household land value above the allowance (assumption)
CIT_GDP = 3.75         # OECD average CIT revenue, % of GDP, 2023
RENT_SHARE = (0.5, 0.7)  # share of the declared CIT base that is above a normal return (assumption)
SEMI = (0.75, 1.5)     # semi-elasticity of reported profit to the rate gap, % per point (1.5: Beer et al. 2020)
SHIFTED = 0.20         # profit recoverable in high-tax EU countries (Torslov et al. 2023)


def revenue():
    out = []
    cap_factor = I_LAND / (I_LAND + TAU_L)        # land values fall when the tax is announced
    lo = LAND["Germany"]; hi = LAND["France"]
    land_lo = 100 * TAU_L * lo[0] * (lo[1] * ABOVE[0] + lo[2]) * cap_factor
    land_hi = 100 * TAU_L * hi[0] * (hi[1] * ABOVE[1] + hi[2]) * cap_factor
    out.append(("Land value tax above the household allowance", land_lo, land_hi))
    base = CIT_GDP / TAU_0                          # declared base at the conventional rate, % of GDP
    gap = 100 * (TAU_1 - TAU_0)
    l1_lo = TAU_1 * base * RENT_SHARE[0] * (1 - SEMI[1] * gap / 100)
    l1_hi = TAU_1 * base * RENT_SHARE[1] * (1 - SEMI[0] * gap / 100)
    out.append(("Layer One alone, after profit shifting", l1_lo, l1_hi))
    full_lo = TAU_1 * base * RENT_SHARE[0] * (1 + SHIFTED)
    full_hi = TAU_1 * base * RENT_SHARE[1] * (1 + SHIFTED)
    out.append(("Layers One to Three if the destination layers recapture shifted rent", full_lo, full_hi))
    out.append(("Memo: current corporate income tax (OECD average, 2023)", CIT_GDP, CIT_GDP))
    out.append(("Memo: current recurrent property taxes (OECD average, 2023)", 0.95, 0.95))
    return [(a, round(b, 2) if a.startswith("Memo") else round(b, 1), round(c, 2) if a.startswith("Memo") else round(c, 1)) for a, b, c in out], cap_factor


def figure(rows):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    labels = [r["short"] for r in rows]
    cur = [r["current rate on rent %"] for r in rows]
    des = [r["design rate on rent %"] for r in rows]
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=200)
    y = range(len(rows))
    h = 0.36
    ax.barh([i - h / 2 - 0.01 for i in y], cur, height=h, color="#3B7FC4", label="Current tax (25% of declared profit)")
    ax.barh([i + h / 2 + 0.01 for i in y], des, height=h, color="#2E7D32", label="Proposed design")
    for i, v in zip(y, des):
        ax.text(v + 1, i + h / 2 + 0.01, f"{v}%", va="center", fontsize=9, color="#1B1B1B")
    for i, v in zip(y, cur):
        ax.text(v + 1, i - h / 2 - 0.01, f"{v}%", va="center", fontsize=9, color="#555555")
    ax.set_yticks(list(y)); ax.set_yticklabels(labels, fontsize=10)
    ax.invert_yaxis()
    ax.set_xlim(0, 60)
    ax.set_xlabel("Tax as a percent of the rent the firm earns from in-country customers", fontsize=9)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_color("#999999"); ax.spines["bottom"].set_color("#999999")
    ax.xaxis.grid(True, color="#E5E5E5", linewidth=0.6); ax.set_axisbelow(True)
    ax.legend(loc="lower left", bbox_to_anchor=(0, 1.0), ncol=2, frameon=False, fontsize=9)
    fig.tight_layout()
    (HERE / "figures").mkdir(exist_ok=True)
    fig.savefig(HERE / "figures" / "fig1_effective_rates.png")
    print("wrote figures/fig1_effective_rates.png")


if __name__ == "__main__":
    rows = archetypes()
    with open(HERE / "archetypes.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    for r in rows:
        print(r)
    rev, cf = revenue()
    with open(HERE / "revenue.csv", "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["item", "low % of GDP", "high % of GDP"]); w.writerows(rev)
    print("capitalization factor", round(cf, 3))
    for r in rev:
        print(r)
    figure(rows)
