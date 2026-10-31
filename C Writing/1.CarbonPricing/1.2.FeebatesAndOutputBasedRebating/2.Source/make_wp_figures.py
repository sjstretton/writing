"""Calibration, tables and figures for working paper 1.2 (feebates), v0.3.

Run from any directory:  python3 make_wp_figures.py
Reads  ember_yearly_2024_IND_IDN_ZAF.csv  (beside this script)
Writes figures/fig3_price_effects.png, figures/fig4_fiscal_flows.png,
       figures/fig1_investment_logit.png, figures/fig2_benchmark_dynamics.png,
       table_country_cases.csv, and prints every number quoted in the paper.

Data
  Generation mix and capacity, 2024: Ember, Yearly Electricity Data (global CSV,
  downloaded 29 October 2026, CC-BY-4.0). Extract saved beside this script.
  Emission factors: IPCC (2006) Guidelines, Vol. 2, ch. 1, Table 1.4 defaults:
  other bituminous coal 94.6 kgCO2/GJ, natural gas 56.1, gas/diesel oil 74.1.

Stylized (labelled so in the paper)
  Heat rates, fuel prices and non-fuel variable costs, common to all three
  countries; the gas headroom limit; investment costs, financing costs and the
  logit sensitivity; the capital-stock simulation.
"""
import csv
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

HERE = Path(__file__).resolve().parent
FIG = HERE / "figures"
FIG.mkdir(exist_ok=True)
plt.rcParams["axes.unicode_minus"] = True

# ---- palette (reference categorical slots, light mode) and ink -------------
SURF, INK, INK2, GRID = "#ffffff", "#0b0b0b", "#52514e", "#d9d8d4"
BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"

T = 50.0  # central carbon price, $/tCO2

# ---- technologies (stylized costs; IPCC 2006 emission factors) -------------
TECH = {
    #            heat GJ/MWh, tCO2/GJ, fuel $/GJ, other variable $/MWh
    "coal":  dict(heat=10.0, ef=0.0946, fuel=2.5,  other=5.0),
    "gas":   dict(heat=6.5,  ef=0.0561, fuel=8.0,  other=3.0),
    "oil":   dict(heat=10.0, ef=0.0741, fuel=15.0, other=5.0),
    "clean": dict(heat=0.0,  ef=0.0,    fuel=0.0,  other=0.0),
}
for p in TECH.values():
    p["e"] = p["heat"] * p["ef"]                 # tCO2/MWh
    p["c"] = p["heat"] * p["fuel"] + p["other"]  # variable cost, $/MWh

GAS_MAX_CF = 0.60  # stylized: fuel-limited ceiling on gas capacity factor
# Ember records no gas-fired generation in South Africa in 2024; we assume no
# gas fuel is available for switching there.
NO_GAS_FUEL = {"South Africa"}

# ---- Ember 2024 data --------------------------------------------------------
EMBER_MAP = {"Coal": "coal", "Gas": "gas", "Other Fossil": "oil",
             "Bioenergy": "clean", "Hydro": "clean", "Nuclear": "clean",
             "Solar": "clean", "Wind": "clean", "Other Renewables": "clean"}
COUNTRIES = ["India", "Indonesia", "South Africa"]
# Largest generator's share of national generation (sources in the paper):
# NTPC 24% (company website); Eskom "over 86%" of national needs (company website).
DOMINANT = {"India": ("NTPC", 0.24), "South Africa": ("Eskom", 0.86)}


def load():
    gen = {c: {k: 0.0 for k in TECH} for c in COUNTRIES}
    cap = {c: {k: 0.0 for k in TECH} for c in COUNTRIES}
    total, lifecycle = {}, {}
    with open(HERE / "ember_yearly_2024_IND_IDN_ZAF.csv") as f:
        for r in csv.DictReader(f):
            c, v, val = r["Area"], r["Variable"], float(r["Value"])
            if r["Category"] == "Electricity generation":
                if v == "Total Generation":
                    total[c] = val
                elif v in EMBER_MAP:
                    gen[c][EMBER_MAP[v]] += val
            elif r["Category"] == "Capacity" and v in EMBER_MAP:
                cap[c][EMBER_MAP[v]] += val
            elif r["Category"] == "Power sector emissions" and v == "CO2 intensity":
                lifecycle[c] = val
    return gen, cap, total, lifecycle


GEN, CAP, TOTAL, LIFE = load()


def intensity(q):
    D = sum(q.values())
    return sum(q[k] * TECH[k]["e"] for k in q) / D


def redispatch(c, t):
    """Short-run merit order at fixed capacity and demand. Clean is must-run.
    Gas displaces coal up to its headroom if gas is cheaper than coal at
    carbon cost t*e (identical ranking under tax and feebate: Proposition 1)."""
    q = dict(GEN[c])
    cg = TECH["gas"]["c"] + t * TECH["gas"]["e"]
    cc = TECH["coal"]["c"] + t * TECH["coal"]["e"]
    if cg < cc and c not in NO_GAS_FUEL:
        head = max(CAP[c]["gas"] * 8.76 * GAS_MAX_CF - q["gas"], 0.0)
        shift = min(head, q["coal"])
        q["gas"] += shift
        q["coal"] -= shift
    return q


def case(c, t=T):
    q0 = GEN[c]
    D = sum(q0.values())
    q = redispatch(c, t)
    e0, et = intensity(q0), intensity(q)
    R = sum((q[k] - q0[k]) * TECH[k]["c"] for k in q) / D  # resource cost, $/MWh
    ec = TECH["coal"]["e"]
    shares = {k: q[k] / D for k in q}
    fee_only = t * sum(shares[k] * (TECH[k]["e"] - et) for k in q if TECH[k]["e"] > et)
    flows = {k: t * (TECH[k]["e"] - et) * q[k] / 1000 for k in q}  # $bn (TWh*$/MWh/1000)
    out = dict(
        D=D, e0=e0, et=et, R=R,
        coal_share=q0["coal"] / D, gas_share=q0["gas"] / D,
        oil_share=q0["oil"] / D, clean_share=q0["clean"] / D,
        shift=q["gas"] - q0["gas"],
        dE=sum((q0[k] - q[k]) * TECH[k]["e"] for k in q),  # MtCO2 cut by re-dispatch
        E0=sum(q0[k] * TECH[k]["e"] for k in q0),
        tax_sb=R + t * et,                 # single buyer, tax
        tax_mkt=t * ec,                    # market, coal marginal before and after
        fb_sb=R,                           # single buyer, feebate netted in the pool
        fb_sb_feeonly=R + fee_only,        # single buyer, fees passed through, rebates kept
        fb_mkt=t * (ec - et),              # market, coal marginal
        fb_mkt_gas=t * (TECH["gas"]["e"] - et),  # market, gas marginal
        fb_mkt_oil=t * (TECH["oil"]["e"] - et),  # market, oil/diesel marginal
        flows=flows,
        tax_rev=t * sum(q[k] * TECH[k]["e"] for k in q) / 1000,
        coal_fee=t * (ec - et),
        clean_rebate=t * et,
        life=LIFE[c],
    )
    return out


def t_bound(r, t=T):
    return t * (r["e0"] - r["et"])


def report():
    print("Technologies:")
    for k, p in TECH.items():
        print(f"  {k:5s} e={p['e']:.3f} tCO2/MWh  variable cost={p['c']:.1f} $/MWh")
    sw = (TECH["gas"]["c"] - TECH["coal"]["c"]) / (TECH["coal"]["e"] - TECH["gas"]["e"])
    print(f"  coal-to-gas switching price = {sw:.1f} $/tCO2")
    rows = []
    for c in COUNTRIES:
        r = case(c)
        print(f"\n{c}: D={r['D']:.1f} TWh coal {100*r['coal_share']:.1f}% gas {100*r['gas_share']:.1f}% "
              f"oil {100*r['oil_share']:.1f}% clean {100*r['clean_share']:.1f}%")
        print(f"  Prop 2 bound t(e0-et) = {t_bound(r):.2f} $/MWh")
        print(f"  e_bar (direct, IPCC) {r['e0']:.3f} -> {r['et']:.3f} after re-dispatch; "
              f"Ember lifecycle {r['life']:.0f} g/kWh; direct emissions {r['E0']:.0f} Mt")
        print(f"  re-dispatch: {r['shift']:.1f} TWh coal->gas, cut {r['dE']:.1f} Mt "
              f"({100*r['dE']/r['E0']:.1f}%), resource cost R={r['R']:.2f} $/MWh")
        for k in ["tax_sb", "tax_mkt", "fb_sb", "fb_sb_feeonly", "fb_mkt", "fb_mkt_gas", "fb_mkt_oil"]:
            print(f"  {k:14s} {r[k]:+.1f} $/MWh")
        print("  flows $bn/yr: " + ", ".join(f"{k} {v:+.2f}" for k, v in r["flows"].items())
              + f"; tax revenue {r['tax_rev']:.1f}")
        print(f"  coal net fee {r['coal_fee']:.1f} $/MWh = {r['coal_fee']/TECH['coal']['heat']:.2f} $/GJ "
              f"({100*r['coal_fee']/TECH['coal']['heat']/TECH['coal']['fuel']:.0f}% of coal price); "
              f"clean rebate {r['clean_rebate']:.1f} $/MWh")
        rows.append([c, f"{r['D']:.0f}", f"{100*r['coal_share']:.1f}", f"{100*r['gas_share']:.1f}",
                     f"{100*r['oil_share']:.1f}", f"{100*r['clean_share']:.1f}", f"{r['e0']:.3f}",
                     f"{r['et']:.3f}", f"{r['life']:.0f}", f"{r['tax_sb']:.1f}", f"{r['tax_mkt']:.1f}",
                     f"{r['fb_sb']:.1f}", f"{r['fb_sb_feeonly']:.1f}", f"{r['fb_mkt']:.1f}",
                     f"{r['tax_rev']:.1f}", f"{r['flows']['coal']:.1f}", f"{-r['flows']['clean']:.1f}",
                     f"{-r['flows']['gas']:.1f}", f"{r['dE']:.0f}"])
        for t in (25, 100):
            rr = case(c, t)
            print(f"  at ${t}: tax_sb {rr['tax_sb']:.1f} tax_mkt {rr['tax_mkt']:.1f} "
                  f"fb_sb {rr['fb_sb']:.2f} fb_mkt {rr['fb_mkt']:.1f}")
    with open(HERE / "table_country_cases.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["country", "generation_TWh", "coal_pct", "gas_pct", "oil_pct", "clean_pct",
                    "ebar_direct", "ebar_after_redispatch", "ember_lifecycle_g_per_kWh",
                    "tax_single_buyer", "tax_market", "feebate_single_buyer",
                    "feebate_single_buyer_fees_only", "feebate_market_coal_marginal",
                    "tax_revenue_bn", "coal_fees_bn", "clean_rebates_bn", "gas_rebates_bn",
                    "redispatch_cut_Mt"])
        w.writerows(rows)


# ---- Figure 1: price effects under the two market designs -------------------
def style(ax):
    ax.set_facecolor(SURF)
    ax.grid(axis="y", color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_color(GRID)
    ax.spines["bottom"].set_color(GRID)
    ax.tick_params(colors=INK2, labelsize=8)


def fig1():
    fig, ax = plt.subplots(figsize=(6.8, 3.8), dpi=200)
    fig.patch.set_facecolor(SURF)
    style(ax)
    series = [("tax_sb", "Tax, single buyer", ORANGE), ("tax_mkt", "Tax, wholesale market", "#b84a1f"),
              ("fb_sb", "Feebate, single buyer", BLUE), ("fb_mkt", "Feebate, wholesale market", AQUA)]
    w = 0.19
    for i, c in enumerate(COUNTRIES):
        r = case(c)
        for j, (k, lab, col) in enumerate(series):
            x = i + (j - 1.5) * (w + 0.015)
            ax.bar(x, r[k], width=w, color=col, edgecolor=SURF, linewidth=1)
            ax.text(x, r[k] + 0.8, f"{r[k]:.0f}", ha="center", va="bottom", fontsize=7, color=INK)
    ax.set_xticks(range(len(COUNTRIES)))
    ax.set_xticklabels(COUNTRIES, fontsize=9, color=INK)
    ax.set_ylabel("Change in price, US\\$/MWh", fontsize=8, color=INK2)
    ax.set_ylim(0, 55)
    ax.legend(handles=[Patch(color=col, label=lab) for _, lab, col in series], ncol=2, fontsize=7.5,
              frameon=False, loc="upper center", bbox_to_anchor=(0.5, 1.16))
    fig.tight_layout()
    fig.savefig(FIG / "fig3_price_effects.png", facecolor=SURF)
    plt.close(fig)


# ---- Figure 2: fiscal flows by plant type -----------------------------------
def fig2():
    fig, ax = plt.subplots(figsize=(6.8, 3.6), dpi=200)
    fig.patch.set_facecolor(SURF)
    style(ax)
    kinds = [("coal", "Coal (pays fee)", ORANGE), ("oil", "Oil and diesel", YELLOW),
             ("gas", "Gas", AQUA), ("clean", "Clean (receives rebate)", BLUE)]
    w = 0.18
    for i, c in enumerate(COUNTRIES):
        r = case(c)
        for j, (k, lab, col) in enumerate(kinds):
            v = r["flows"][k]
            x = i + (j - 1.5) * (w + 0.015)
            ax.bar(x, v, width=w, color=col, edgecolor=SURF, linewidth=1)
            if abs(v) >= 0.05:
                ax.text(x, v + (0.3 if v >= 0 else -0.3), f"{v:+.1f}".replace("-", "\u2212"),
                        ha="center", va="bottom" if v >= 0 else "top", fontsize=7, color=INK)
        ax.text(i, -19.5, f"Tax revenue: \\${r['tax_rev']:.0f}bn", ha="center", fontsize=7, color=INK2)
    ax.axhline(0, color=INK2, linewidth=0.8)
    ax.set_xticks(range(len(COUNTRIES)))
    ax.set_xticklabels(COUNTRIES, fontsize=9, color=INK)
    ax.set_ylabel("Net feebate payment, US\\$ bn a year", fontsize=8, color=INK2)
    ax.set_ylim(-21, 21)
    ax.legend(handles=[Patch(color=col, label=lab) for _, lab, col in kinds], ncol=4, fontsize=7,
              frameon=False, loc="upper center", bbox_to_anchor=(0.5, 1.13))
    fig.tight_layout()
    fig.savefig(FIG / "fig4_fiscal_flows.png", facecolor=SURF)
    plt.close(fig)


# ---- Investment: logit share of clean in new capacity (stylized) ------------
def annuity(r, n):
    return r / (1 - (1 + r) ** -n)


INV = {  # stylized: overnight cost $/kW, capacity factor, life, O&M+fuel $/MWh, intensity
    "clean": dict(K=1500.0, cf=0.28, life=25, var=12.0, e=0.0),
    "coal": dict(K=1200.0, cf=0.70, life=30, var=8.0 + TECH["coal"]["c"], e=TECH["coal"]["e"]),
}
BETA = 0.05  # stylized logit sensitivity, per $/MWh


def lcoe(tech, r, kclean_mult=1.0):
    p = INV[tech]
    K = p["K"] * (kclean_mult if tech == "clean" else 1.0)
    return K * 1000 * annuity(r, p["life"]) / (p["cf"] * 8760) + p["var"]


def gap(r, t, instrument="tax", ebar=0.6, kclean_mult=1.0):
    """Clean minus coal levelized cost including the carbon instrument."""
    if instrument == "tax":
        cc = lcoe("clean", r, kclean_mult) + t * INV["clean"]["e"]
        cd = lcoe("coal", r) + t * INV["coal"]["e"]
    else:  # feebate against any common benchmark ebar
        cc = lcoe("clean", r, kclean_mult) + t * (INV["clean"]["e"] - ebar)
        cd = lcoe("coal", r) + t * (INV["coal"]["e"] - ebar)
    return cc - cd


def phi(r, t, instrument="tax", ebar=0.6, kclean_mult=1.0):
    return 1 / (1 + np.exp(BETA * gap(r, t, instrument, ebar, kclean_mult)))


def fig3():
    ts = np.linspace(0, 100, 201)
    fig, ax = plt.subplots(figsize=(6.5, 3.6), dpi=200)
    fig.patch.set_facecolor(SURF)
    style(ax)
    for r, col in [(0.06, BLUE), (0.12, ORANGE)]:
        tax = phi(r, ts, "tax")
        fb = phi(r, ts, "feebate", ebar=0.7)
        assert np.allclose(tax, fb)  # Proposition 4: the benchmark cancels
        ax.plot(ts, 100 * tax, color=col, linewidth=2)
        t_par = (lcoe("clean", r) - lcoe("coal", r)) / INV["coal"]["e"]
        ax.plot([t_par], [50], "o", color=col, markersize=5, markeredgecolor=SURF)
        ax.text(t_par + 2, 46, f"parity \\${t_par:.0f}/t", fontsize=7, color=INK2, va="top")
        i45 = np.searchsorted(ts, 45)
        ax.text(45, 100 * tax[i45] + (3 if r < 0.1 else -3),
                f"financing cost {int(r*100)}%", fontsize=8, color=INK,
                ha="right" if r < 0.1 else "left", va="bottom" if r < 0.1 else "top")
    ax.set_xlim(0, 112)
    ax.set_ylim(0, 102)
    ax.set_xlabel("Carbon price or feebate rate, US\\$/tCO$_2$", fontsize=8, color=INK2)
    ax.set_ylabel("Clean share of new capacity, %", fontsize=8, color=INK2)
    fig.tight_layout()
    fig.savefig(FIG / "fig1_investment_logit.png", facecolor=SURF)
    plt.close(fig)
    for r in (0.06, 0.08, 0.12):
        print(f"r={r:.2f}: LCOE clean {lcoe('clean', r):.1f}, coal {lcoe('coal', r):.1f}, "
              f"parity price {(lcoe('clean', r) - lcoe('coal', r)) / INV['coal']['e']:.1f} $/t, "
              f"phi(0)={phi(r, 0):.2f}, phi(25)={phi(r, 25):.2f}, phi(50)={phi(r, 50):.2f}")


# ---- Capital turnover and the benchmark (stylized, India-like start) --------
def simulate(t=T, r=0.08, years=26, growth=0.05, ret_coal=1 / 35, ret_clean=1 / 25,
             learn=0.02):
    """Generation-equivalent capital stocks; clean share of new investment from
    the logit; the feebate benchmark is last year's realized average."""
    D = GEN["India"]["clean"] + GEN["India"]["coal"]  # two-type stylized grid
    C, Dt = GEN["India"]["clean"], GEN["India"]["coal"]
    ec = TECH["coal"]["e"]
    out = []
    for y in range(years):
        ebar = ec * Dt / (C + Dt)
        out.append(dict(year=2024 + y, w=C / (C + Dt), ebar=ebar,
                        coal_fee=t * (ec - ebar), rebate=t * ebar))
        Dn = D * (1 + growth)
        I = (Dn - D) + ret_coal * Dt + ret_clean * C
        f = float(phi(r, t, "feebate", ebar, kclean_mult=(1 - learn) ** y))
        C = (1 - ret_clean) * C + f * I
        Dt = (1 - ret_coal) * Dt + (1 - f) * I
        D = Dn
    return out


def fig4():
    sim = simulate()
    yrs = [s["year"] for s in sim]
    fig, (a, b) = plt.subplots(1, 2, figsize=(7.0, 3.4), dpi=200)
    fig.patch.set_facecolor(SURF)
    for ax in (a, b):
        style(ax)
    ec = TECH["coal"]["e"]
    a.plot(yrs, [T * ec] * len(yrs), color=ORANGE, linewidth=2, linestyle="--")
    a.plot(yrs, [s["coal_fee"] for s in sim], color=ORANGE, linewidth=2)
    a.plot(yrs, [s["rebate"] for s in sim], color=BLUE, linewidth=2)
    a.text(yrs[-1], T * ec + 1.5, "Tax on coal", fontsize=7, color=INK, ha="right", va="bottom")
    a.text(yrs[-1], sim[-1]["coal_fee"] - 9, "Feebate: net fee on coal\n= market price effect",
           fontsize=7, color=INK, ha="right", va="top")
    a.text(yrs[-1], sim[-1]["rebate"] + 2, "Rebate to clean", fontsize=7, color=INK, ha="right",
           va="bottom")
    a.set_ylim(0, 55)
    a.set_ylabel("US\\$/MWh at \\$50/tCO$_2$", fontsize=8, color=INK2)
    a.set_title("A. The feebate converges on the tax", fontsize=8.5, color=INK, loc="left")
    s = np.linspace(0, 1, 101)
    b.plot(100 * s, T * (1 - s), color=BLUE, linewidth=2, label="Benchmark this year's average")
    b.plot(100 * s, T * (1 - s / 1.08), color=BLUE, linewidth=2, linestyle="--",
           label="Benchmark last year's average\n(8% discount, permanent cut)")
    b.legend(fontsize=6.5, frameon=False, loc="upper right")
    for name, (firm, sh) in DOMINANT.items():
        b.plot([100 * sh], [T * (1 - sh)], "o", color=ORANGE, markersize=6, markeredgecolor=SURF)
        if sh < 0.5:
            b.text(100 * sh + 3, T * (1 - sh) + 3, f"{firm} ({name})", fontsize=7,
                   color=INK, ha="left", va="bottom")
        else:
            b.text(100 * sh - 4, T * (1 - sh) - 1, f"{firm} ({name})", fontsize=7,
                   color=INK, ha="right", va="top")
    b.set_xlabel("Firm's share of sector output, %", fontsize=8, color=INK2)
    b.set_ylabel("Incentive per tonne, US\\$", fontsize=8, color=INK2)
    b.set_ylim(0, 55)
    b.set_title("B. Dominant firms see less of the rate", fontsize=8.5, color=INK, loc="left")
    fig.tight_layout()
    fig.savefig(FIG / "fig2_benchmark_dynamics.png", facecolor=SURF)
    plt.close(fig)
    for a_, b_ in zip(sim[:10], sim[1:11]):
        print(f"  true-up {b_['year']}: benchmark fall {a_['ebar'] - b_['ebar']:.3f}, "
              f"deficit {T * (a_['ebar'] - b_['ebar']):.2f} $/MWh, "
              f"{T * (a_['ebar'] - b_['ebar']) * sum(GEN['India'].values()) / 1000:.1f} $bn at India 2024 output")
    for s_ in sim[::5]:
        print(f"  {s_['year']}: clean share {100*s_['w']:.0f}% ebar {s_['ebar']:.3f} "
              f"coal fee {s_['coal_fee']:.1f} rebate {s_['rebate']:.1f}")


if __name__ == "__main__":
    report()
    fig1()
    fig2()
    print("\nInvestment (stylized):")
    fig3()
    print("\nSimulation (stylized, India-like start, $50/t, r=8%):")
    fig4()
    for c, (firm, sh) in DOMINANT.items():
        print(f"{firm}: t(1-s)={T*(1-sh):.1f}, lagged t(1-s/1.08)={T*(1-sh/1.08):.1f}, "
              f"leave-one-out scale 1/(1-s)={1/(1-sh):.2f}")
    print("wrote figures to", FIG)
