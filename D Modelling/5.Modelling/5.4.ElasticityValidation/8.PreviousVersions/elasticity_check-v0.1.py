"""Paper 4.4: "Are CPAT's Price Elasticities Right? A Check Against the Evidence".

Run from this folder:  python3 elasticity_check.py

1. Reads CPAT's default elasticities (legacy CPAT 1.0pre, public NoPropData
   release, as extracted in the CPAT-AI repository: data/cpat_legacy_elasticities.csv)
   and computes the total long-run own-price elasticity CPAT applies:
       eps_total = eps_U + eps_F + eps_U * eps_F
   (usage margin, efficiency margin, and the rebound term; 03_Mitigation.qmd,
   "Fuel Consumption Dynamics" and "Rebound effect").
2. Compares each fuel-sector pair with the published evidence (LIT below; every
   number is tied to a bib key in ../ElasticityValidation.bib) and classifies
   CPAT as high, low or in range.
3. Shows what the differences do: (a) the timing of the response, under partial
   adjustment, against CPAT's one-year assumption; (b) emission cuts and the
   Total Effective Carbon Price (TECP) in the stylized economy of paper 1.7.

Outputs: table_comparison.csv, table_income.csv, table_timing.csv,
table_tecp.csv, figures/fig1_cpat_vs_literature.png, figures/fig2_timing.png.
"""

from pathlib import Path
import csv

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import tecp_core as tc

HERE = Path(__file__).resolve().parent
FIG = HERE / "figures"
FIG.mkdir(exist_ok=True)

# ---------------------------------------------------------------- CPAT data
def load_cpat():
    rows = list(csv.DictReader(open(HERE / "data" / "cpat_legacy_elasticities.csv")))
    out = {}
    for r in rows:
        out[(r["type"], r["fuel_group"], r["sector_group"])] = {
            g: float(r[g]) for g in ("LIC", "LMIC", "UMIC", "HIC")}
    return out


CPAT = load_cpat()


def total(f, s, g):
    u = CPAT[("usg", f, s)][g]
    e = CPAT[("eff", f, s)][g]
    return u + e + u * e


# ------------------------------------------------------- literature (long run)
# Each entry: (label, value, bib key). Values are long-run own-price
# elasticities as reported. "via" notes where a number is reported second-hand.
GASOLINE = [("Labandeira et al. mean", -0.53, "Labandeira2017"),
            ("Labandeira et al. adjusted", -0.77, "Labandeira2017"),
            ("Brons et al. mean", -0.84, "brons2008"),
            ("Havranek et al. uncorrected", -0.69, "havranek2012"),
            ("Huntington et al. developing", -0.61, "huntington2019")]
GASOLINE_BC = -0.31          # Havranek et al., corrected for publication bias
DIESEL = [("Labandeira et al. mean", -0.39, "Labandeira2017"),
          ("Labandeira et al. adjusted", -0.44, "Labandeira2017"),
          ("Huntington et al. developing", -0.50, "huntington2019"),
          ("Dahl (2004) via Huntington et al.", -0.67, "huntington2019")]
ELEC = [("Labandeira et al. mean", -0.51, "Labandeira2017"),
        ("Labandeira et al. adjusted", -0.37, "Labandeira2017"),
        ("Huntington et al. developing, all", -0.46, "huntington2019")]
ELEC_RES = ELEC + [("Huntington et al. developing, residential", -0.32, "huntington2019"),
                   ("Dahl (2004) residential via Huntington et al.", -0.43, "huntington2019")]
ELEC_IND = ELEC + [("Huntington et al. developing, industrial (Mexico)", -0.81, "huntington2019")]
GAS = [("Labandeira et al. mean", -0.57, "Labandeira2017"),
       ("Labandeira et al. adjusted", -0.68, "Labandeira2017"),
       ("Burke and Yang, 44 countries", -1.25, "burke2016gas")]
GAS_RES = GAS + [("Dahl (2004) residential via Huntington et al.", -0.56, "huntington2019"),
                 ("Huntington et al. developing, residential", -1.59, "huntington2019")]
GAS_IND = GAS + [("Dahl (2004) industry via Huntington et al.", -1.35, "huntington2019")]
COAL = [("Burke and Liao, China, low", -0.30, "burke2015coal"),
        ("Burke and Liao, China, high", -0.70, "burke2015coal")]

# (fuel code, sector code, label, evidence list, bias-corrected point or None)
PAIRS = [
    ("gso", "tra", "Gasoline, transport", GASOLINE, GASOLINE_BC),
    ("die", "tra", "Diesel, transport", DIESEL, None),
    ("ecy", "res", "Electricity, residential", ELEC_RES, None),
    ("ecy", "ind", "Electricity, industry", ELEC_IND, None),
    ("ecy", "srv", "Electricity, services", ELEC, None),
    ("nga", "res", "Natural gas, residential", GAS_RES, None),
    ("nga", "ind", "Natural gas, industry", GAS_IND, None),
    ("coa", "ind", "Coal, industry", COAL, None),
    ("die", "ind", "Diesel, industry", DIESEL, None),
    ("gso", "srv", "Gasoline, services", GASOLINE, GASOLINE_BC),
]
TOL = 0.05   # CPAT within 0.05 of the evidence range counts as in range


def verdict(c_dev, c_hic, lo, hi):
    """lo, hi: least and most negative values in the evidence."""
    vals = (c_dev, c_hic)
    if all(v < hi - TOL for v in vals):
        return "High"
    if all(v > lo + TOL for v in vals):
        return "Low"
    return "In range"


def comparison():
    rows = []
    for f, s, label, ev, bc in PAIRS:
        c_dev, c_hic = total(f, s, "LMIC"), total(f, s, "HIC")
        vals = [v for _, v, _ in ev]
        lo, hi = max(vals), min(vals)          # least / most elastic
        med = float(np.median(vals))
        rows.append(dict(pair=label, fuel=f, sector=s,
                         usage_dev=round(CPAT[("usg", f, s)]["LMIC"], 2), eff_dev=round(CPAT[("eff", f, s)]["LMIC"], 2),
                         cpat_dev=round(c_dev, 2), cpat_hic=round(c_hic, 2),
                         lit_least=lo, lit_most=hi, lit_median=round(med, 2),
                         bias_corrected=bc, n=len(vals),
                         sources="; ".join(sorted({k for _, _, k in ev})),
                         verdict=verdict(c_dev, c_hic, lo, hi)))
    with open(HERE / "table_comparison.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    return rows


# ---------------------------------------------------------- income elasticities
INC_LIT = {  # long run; label -> (value, key)
    ("gso", "tra"): [("Huntington et al. developing", 0.94, "huntington2019"),
                     ("Dahl (2004) via Huntington et al.", 0.69, "huntington2019")],
    ("die", "tra"): [("Dahl (2004) via Huntington et al.", 1.13, "huntington2019")],
    ("ecy", "res"): [("Huntington et al. developing, residential", 0.53, "huntington2019"),
                     ("Dahl (2004) residential via Huntington et al.", 0.60, "huntington2019")],
    ("ecy", "ind"): [("Huntington et al. developing, industrial", 0.76, "huntington2019")],
    ("nga", "ind"): [("Dahl (2004) industry via Huntington et al.", 1.39, "huntington2019")],
    ("nga", "res"): [("Huntington et al. developing, residential", 0.85, "huntington2019"),
                     ("Dahl (2004) residential via Huntington et al.", 0.11, "huntington2019")],
}
INC_LABEL = {("gso", "tra"): "Gasoline, transport", ("die", "tra"): "Diesel, transport",
             ("ecy", "res"): "Electricity, residential", ("ecy", "ind"): "Electricity, industry",
             ("nga", "ind"): "Natural gas, industry", ("nga", "res"): "Natural gas, residential"}


def income_table():
    rows = []
    for k, ev in INC_LIT.items():
        vals = [v for _, v, _ in ev]
        c = CPAT[("inc", k[0], k[1])]["LMIC"]
        rows.append(dict(pair=INC_LABEL[k], cpat_base=c, lit_min=min(vals), lit_max=max(vals),
                         sources="; ".join(f"{l} {v}" for l, v, _ in ev)))
    with open(HERE / "table_income.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    return rows


# --------------------------------------------------------------------- timing
LAM_U = 0.30    # usage margin, per year: SR/LR ratio, Havranek et al. (0.09/0.31)
LAM_F = 0.067   # efficiency margin, per year: vehicle turnover in CPAT (Black et al. 2022)


def horizon_total(u, e, T):
    aU, aF = 1 - (1 - LAM_U) ** T, 1 - (1 - LAM_F) ** T
    return aU * u + aF * e + (aU * u) * (aF * e)


def timing():
    rows = []
    for f, s, label in [("gso", "tra", "Gasoline, transport"), ("ecy", "res", "Electricity, residential"),
                        ("coa", "ind", "Coal, industry"), ("die", "ind", "Diesel, industry")]:
        u, e = CPAT[("usg", f, s)]["LMIC"], CPAT[("eff", f, s)]["LMIC"]
        lr = u + e + u * e
        for T in (1, 3, 5, 10, 20):
            ht = horizon_total(u, e, T)
            rows.append(dict(pair=label, year=T, cpat=round(lr, 3), partial=round(ht, 3),
                             share=round(ht / lr, 3)))
    with open(HERE / "table_timing.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    return rows


# ----------------------------------------------------------- TECP implications
def econ_with(eta):
    e = {s: dict(v) for s, v in tc.ECON.items()}
    for s in e:
        e[s]["eta"] = eta[s]
    return e


def cut_of_tax(econ, rate=30.0):
    dps = {s: tc.dp_uniform(s, rate, econ) for s in tc.SECTORS}
    E0 = sum(tc.base_emissions(s, econ) for s in tc.SECTORS)
    return tc.exact_cut(dps, econ) / E0


def tecp_case(econ):
    lam = tc.solve_lcfs_lambda(econ)
    dps = tc.package_dp(lam, econ=econ)
    return tc.tecp_linear(dps, econ), tc.tecp_exact(dps, econ)


# eta = |demand elasticity of the sector's energy service|.
# Paper 1.7 central values; CPAT-implied (developing-country totals of the
# dominant fuels: electricity for power; gasoline and diesel for road; coal,
# gas and oil for industry); CPAT with road bias-corrected; all halved.
def cpat_eta():
    road = np.mean([-total("gso", "tra", "LMIC"), -total("die", "tra", "LMIC")])
    power = np.mean([-total("ecy", s, "LMIC") for s in ("res", "ind", "srv")])
    ind = np.mean([-total(f, "ind", "LMIC") for f in ("coa", "nga", "oil")])
    return {"Power": round(power, 2), "Road transport": round(road, 2), "Industry": round(ind, 2)}


def tecp_table():
    base = {s: tc.ECON[s]["eta"] for s in tc.SECTORS}
    ce = cpat_eta()
    cases = [("Paper 1.7 central calibration", base),
             ("CPAT-implied demand elasticities", ce),
             ("CPAT, road fuels bias-corrected", {**ce, "Road transport": -GASOLINE_BC}),
             ("CPAT, all demand elasticities halved", {k: v / 2 for k, v in ce.items()})]
    rows = []
    for name, eta in cases:
        econ = econ_with(eta)
        lin, ex = tecp_case(econ)
        E0 = sum(tc.base_emissions(s, econ) for s in tc.SECTORS)
        sw = sum(tc.linear_cut(s, tc.dp_uniform(s, 30.0, econ), econ)[0] for s in tc.SECTORS)
        dm = sum(tc.linear_cut(s, tc.dp_uniform(s, 30.0, econ), econ)[1] for s in tc.SECTORS)
        rows.append(dict(case=name, eta_power=eta["Power"], eta_road=eta["Road transport"],
                         eta_industry=eta["Industry"], cut_30_pct=round(100 * cut_of_tax(econ), 1),
                         switching_pct_first_order=round(100 * sw / E0, 1),
                         demand_pct_first_order=round(100 * dm / E0, 1),
                         tecp_first_order=round(lin, 1), tecp_exact=round(ex, 1)))
    with open(HERE / "table_tecp.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    return rows


# -------------------------------------------------------------------- figures
INK, MUTED, GRID = "#0b0b0b", "#52514e", "#e4e3df"
BLUE, ORANGE = "#2a78d6", "#eb6834"


def fig_comparison(rows):
    fig, ax = plt.subplots(figsize=(7.5, 6.0), dpi=200)
    y = np.arange(len(rows))[::-1]
    for yi, r, (f, s, label, ev, bc) in zip(y, rows, PAIRS):
        ax.plot([r["lit_most"], r["lit_least"]], [yi, yi], color="#bdbcb6", lw=7,
                solid_capstyle="round", zorder=1)
        for _, v, _ in ev:
            ax.plot(v, yi, "|", color=MUTED, ms=9, mew=1.2, zorder=2)
        if bc is not None:
            ax.plot(bc, yi, "D", color=ORANGE, ms=6, mec="white", mew=1, zorder=3)
        ax.plot([r["cpat_dev"]], [yi], "o", color=BLUE, ms=8, mec="white", mew=1.5, zorder=4)
        ax.plot([r["cpat_hic"]], [yi], "o", mfc="white", mec=BLUE, ms=7, mew=1.6, zorder=4)
        ax.text(0.02, yi, r["verdict"], va="center", ha="left", fontsize=8, color=INK)
    ax.set_yticks(y)
    ax.set_yticklabels([r["pair"] for r in rows], fontsize=8.5, color=INK)
    ax.set_xlim(-1.7, 0.2)
    ax.axvline(0, color=MUTED, lw=0.8)
    ax.set_xlabel("Long-run own-price elasticity", fontsize=9, color=INK)
    ax.grid(axis="x", color=GRID, lw=0.8)
    ax.set_axisbelow(True)
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)
    ax.tick_params(axis="both", colors=MUTED, labelsize=8)
    from matplotlib.lines import Line2D
    h = [Line2D([], [], color="#bdbcb6", lw=7, label="Range of published estimates"),
         Line2D([], [], ls="", marker="|", color=MUTED, ms=9, label="Individual estimate"),
         Line2D([], [], ls="", marker="D", color=ORANGE, mec="white", ms=6,
                label="Gasoline, corrected for publication bias"),
         Line2D([], [], ls="", marker="o", color=BLUE, mec="white", ms=8,
                label="CPAT, low and middle income"),
         Line2D([], [], ls="", marker="o", mfc="white", mec=BLUE, ms=7, label="CPAT, high income")]
    ax.legend(handles=h, loc="upper center", bbox_to_anchor=(0.45, -0.12), ncol=2, fontsize=7.5, frameon=False)
    fig.tight_layout()
    fig.savefig(FIG / "fig1_cpat_vs_literature.png")
    plt.close(fig)


def fig_timing():
    fig, ax = plt.subplots(figsize=(7.0, 3.6), dpi=200)
    T = np.arange(0, 21)
    for (f, s, label), col in zip([("gso", "tra", "Gasoline, transport"),
                                   ("coa", "ind", "Coal, industry")], (BLUE, ORANGE)):
        u, e = CPAT[("usg", f, s)]["LMIC"], CPAT[("eff", f, s)]["LMIC"]
        lr = u + e + u * e
        ht = [0.0] + [horizon_total(u, e, t) for t in T[1:]]
        ax.plot(T, ht, color=col, lw=2, label=f"{label}: partial adjustment")
        ax.step([0, 1, 20], [0, lr, lr], where="post", color=col, lw=1.5, ls="--",
                label=f"{label}: CPAT (full response in year 1)")
    ax.set_xlabel("Years after a permanent price rise", fontsize=9, color=INK)
    ax.set_ylabel("Own-price elasticity at that horizon", fontsize=9, color=INK)
    ax.set_xlim(0, 20)
    ax.grid(color=GRID, lw=0.8)
    ax.set_axisbelow(True)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    ax.tick_params(colors=MUTED, labelsize=8)
    ax.legend(fontsize=7.5, frameon=False, loc="upper right")
    fig.tight_layout()
    fig.savefig(FIG / "fig2_timing.png")
    plt.close(fig)


if __name__ == "__main__":
    tc.check_against_brief()   # the copied model reproduces paper 1.7
    rows = comparison()
    for r in rows:
        print(f"{r['pair']:28s} CPAT {r['cpat_dev']:+.2f}/{r['cpat_hic']:+.2f}  "
              f"lit {r['lit_most']:+.2f}..{r['lit_least']:+.2f} med {r['lit_median']:+.2f}  {r['verdict']}")
    for r in income_table():
        print(r)
    for r in timing():
        if r["year"] in (1, 5, 10):
            print(r)
    print(cpat_eta())
    for r in tecp_table():
        print(r)
    fig_comparison(rows)
    fig_timing()
