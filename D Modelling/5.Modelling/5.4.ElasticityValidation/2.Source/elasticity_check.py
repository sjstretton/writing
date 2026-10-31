"""Paper 5.4: "Are CPAT's Price Elasticities Right? A Check Against the Evidence".

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
   Total Effective Carbon Price (TECP) in the stylized economy of paper 6.1.

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
# Each entry: (label, value, bib key, independent). Values are long-run own-price
# elasticities as reported; every number was checked against the source named in
# the bib note (31 Oct 2026). independent=False marks CPAT's own calibration source:
# Labandeira et al. as reproduced in CPAT's documentation (Table A), which tests
# the calibration, not the targets. "Dahl and Roman (2004)" values are as reported
# in Huntington et al. (MPRA 87532, Table 13), for industrialized economies.
CAL = "CPAT Table A (Labandeira et al. as reproduced)"
GASOLINE = [(CAL + " mean", -0.53, "Labandeira2017", False),
            (CAL + " adjusted", -0.77, "Labandeira2017", False),
            ("Labandeira et al., global (authors' summary)", -0.72, "labandeira2016papeles", True),
            ("Labandeira et al., EU", -0.79, "labandeira2016papeles", True),
            ("Brons et al. mean", -0.84, "brons2008", True),
            ("Havranek et al. uncorrected", -0.69, "havranek2012", True),
            ("Huntington et al. developing, transport", -0.61, "huntington2019", True),
            ("Dahl and Roman via Huntington et al.", -0.61, "huntington2019", True),
            ("Arzaghi and Squalli, fuel-subsidizing", -0.25, "arzaghi2015", True)]
GASOLINE_BC = -0.31          # Havranek et al., corrected for publication bias
DIESEL = [(CAL + " mean", -0.39, "Labandeira2017", False),
          (CAL + " adjusted", -0.44, "Labandeira2017", False),
          ("Labandeira et al., global (authors' summary)", -0.60, "labandeira2016papeles", True),
          ("Labandeira et al., EU", -0.64, "labandeira2016papeles", True),
          ("Huntington et al. developing (two estimates)", -0.50, "huntington2019", True),
          ("Dahl and Roman via Huntington et al.", -0.67, "huntington2019", True)]
ELEC = [(CAL + " mean", -0.51, "Labandeira2017", False),
        (CAL + " adjusted", -0.37, "Labandeira2017", False),
        ("Labandeira et al., global (authors' summary)", -0.69, "labandeira2016papeles", True),
        ("Labandeira et al., EU", -0.60, "labandeira2016papeles", True),
        ("Huntington et al. developing, all", -0.46, "huntington2019", True),
        ("Dahl and Roman via Huntington et al.", -0.32, "huntington2019", True)]
ELEC_RES = ELEC + [("Huntington et al. developing, residential", -0.32, "huntington2019", True),
                   ("Dahl and Roman, residential, via Huntington et al.", -0.43, "huntington2019", True),
                   ("Espey and Espey, residential (mostly US)", -0.85, "espey2004", True),
                   ("Csereklyei, EU residential (low end)", -0.53, "csereklyei2020", True),
                   ("Csereklyei, EU residential (high end)", -0.56, "csereklyei2020", True)]
ELEC_IND = ELEC + [("Huntington et al. developing, industrial (Mexico)", -0.81, "huntington2019", True),
                   ("Csereklyei, EU industrial (low end)", -0.75, "csereklyei2020", True),
                   ("Csereklyei, EU industrial (high end)", -1.01, "csereklyei2020", True)]
GAS = [(CAL + " mean", -0.57, "Labandeira2017", False),
       (CAL + " adjusted", -0.68, "Labandeira2017", False),
       ("Labandeira et al., global (authors' summary)", -0.85, "labandeira2016papeles", True),
       ("Labandeira et al., EU", -0.78, "labandeira2016papeles", True),
       ("Burke and Yang, 44 countries", -1.25, "burke2016gas", True)]
GAS_RES = GAS + [("Dahl and Roman, residential, via Huntington et al.", -0.56, "huntington2019", True),
                 ("Huntington et al. developing, residential", -1.59, "huntington2019", True)]
GAS_IND = GAS + [("Dahl and Roman, industry, via Huntington et al.", -1.35, "huntington2019", True)]
COAL = [("Burke and Liao, China, low", -0.30, "burke2015coal", True),
        ("Burke and Liao, China, high", -0.70, "burke2015coal", True)]

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
    if any(v < hi for v in vals):
        return "Elastic edge"   # within the tolerance, but beyond the most elastic estimate
    return "In range"


def comparison():
    rows = []
    for f, s, label, ev, bc in PAIRS:
        c_dev, c_hic = total(f, s, "LMIC"), total(f, s, "HIC")
        vals = [v for _, v, _, _ in ev]
        ind = [v for _, v, _, i in ev if i]
        lo, hi = max(vals), min(vals)          # least / most elastic
        med = float(np.median(ind))
        rows.append(dict(pair=label, fuel=f, sector=s,
                         usage_dev=round(CPAT[("usg", f, s)]["LMIC"], 2), eff_dev=round(CPAT[("eff", f, s)]["LMIC"], 2),
                         cpat_dev=round(c_dev, 2), cpat_hic=round(c_hic, 2),
                         lit_least=lo, lit_most=hi, indep_least=max(ind), indep_most=min(ind),
                         indep_median=round(med, 2), cpat_over_median=round(c_dev / med, 2),
                         bias_corrected=bc, n=len(vals), n_indep=len(ind),
                         sources="; ".join(sorted({k for _, _, k, _ in ev})),
                         verdict=verdict(c_dev, c_hic, lo, hi),
                         verdict_indep=verdict(c_dev, c_hic, max(ind), min(ind))))
    with open(HERE / "table_comparison.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    return rows


# ---------------------------------------------------------- income elasticities
INC_LIT = {  # long run; label -> (value, key)
    ("gso", "tra"): [("Huntington et al. developing, transport", 0.94, "huntington2019"),
                     ("Dahl and Roman via Huntington et al.", 0.69, "huntington2019"),
                     ("Burke and Csereklyei, transport energy, 132 countries", 0.86, "burke2016"),
                     ("Havranek and Kokes, gasoline, uncorrected", 0.66, "havranek2015income"),
                     ("Havranek and Kokes, gasoline, bias-corrected", 0.23, "havranek2015income"),
                     ("Arzaghi and Squalli, fuel-subsidizing", 0.81, "arzaghi2015")],
    ("die", "tra"): [("Dahl and Roman via Huntington et al.", 1.13, "huntington2019"),
                     ("Burke and Csereklyei, transport energy, 132 countries", 0.86, "burke2016")],
    ("ecy", "res"): [("Huntington et al. developing, residential", 0.53, "huntington2019"),
                     ("Dahl and Roman, residential, via Huntington et al.", 0.60, "huntington2019"),
                     ("Burke and Csereklyei, residential electricity", 0.78, "burke2016"),
                     ("Csereklyei, EU residential", 0.61, "csereklyei2020")],
    ("ecy", "ind"): [("Huntington et al. developing, industrial", 0.76, "huntington2019"),
                     ("Csereklyei, EU industrial (low end)", 0.76, "csereklyei2020"),
                     ("Csereklyei, EU industrial (high end)", 1.08, "csereklyei2020")],
    ("nga", "ind"): [("Dahl and Roman, industry, via Huntington et al.", 1.39, "huntington2019"),
                     ("Burke and Csereklyei, industry energy, 132 countries", 0.88, "burke2016")],
    ("nga", "res"): [("Huntington et al. developing, residential", 0.85, "huntington2019"),
                     ("Dahl and Roman, residential, via Huntington et al.", 0.11, "huntington2019")],
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
# Share of each margin's long-run response achieved T years after a permanent
# price change: a(T) = 1 - (1 - lam)^T. Central speeds: usage 0.30 a year (within
# paper 6.1's 0.25-0.40 for the demand margin; Havranek et al.'s bias-corrected
# short-run/long-run ratio for gasoline is 0.09/0.31 = 0.29); efficiency 0.067 a
# year (vehicle fleet turnover, 15-year life: Black et al. 2022, Annex C).
# Bounds: usage instantaneous (lam_U = 1), and efficiency at building turnover
# (1.2-1.8 percent a year in Black et al. 2022; 0.02 used).
LAM_U = 0.30
LAM_F = 0.067
TIMING_CASES = [("central", 0.30, 0.067), ("usage instantaneous", 1.0, 0.067),
                ("slow capital (buildings)", 0.30, 0.02)]


def horizon_total(u, e, T, lam_u=LAM_U, lam_f=LAM_F):
    aU, aF = 1 - (1 - lam_u) ** T, 1 - (1 - lam_f) ** T
    return aU * u + aF * e + (aU * u) * (aF * e)


TIMING_PAIRS = [("gso", "tra", "Gasoline, transport"), ("die", "tra", "Diesel, transport"),
                ("ecy", "res", "Electricity, residential"), ("coa", "ind", "Coal, industry"),
                ("die", "ind", "Diesel, industry")]


def timing():
    rows = []
    for case, lu, lf in TIMING_CASES:
        for f, s, label in TIMING_PAIRS:
            u, e = CPAT[("usg", f, s)]["LMIC"], CPAT[("eff", f, s)]["LMIC"]
            lr = u + e + u * e
            for T in (1, 3, 5, 10, 20):
                ht = horizon_total(u, e, T, lu, lf)
                rows.append(dict(case=case, pair=label, year=T, cpat=round(lr, 3), partial=round(ht, 3),
                                 share=round(ht / lr, 3), cpat_overstatement=round(lr / ht - 1, 3)))
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
# Paper 6.1 central values; CPAT-implied (developing-country totals of the
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
    cases = [("Paper 6.1 central calibration", base),
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
        for _, v, _, ind in ev:
            ax.plot(v, yi, "|" if ind else "x", color=MUTED, ms=9 if ind else 5, mew=1.2, zorder=2)
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
         Line2D([], [], ls="", marker="|", color=MUTED, ms=9, label="Published estimate"),
         Line2D([], [], ls="", marker="x", color=MUTED, ms=5, label="CPAT's calibration source (its Table A)"),
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
        fast = [0.0] + [horizon_total(u, e, t, 1.0, LAM_F) for t in T[1:]]
        slow_f = 0.02 if s != "tra" else LAM_F     # building/industry capital turns over more slowly
        slow = [0.0] + [horizon_total(u, e, t, LAM_U, slow_f) for t in T[1:]]
        ax.fill_between(T, fast, slow, color=col, alpha=0.12, lw=0)
        ax.plot(T, ht, color=col, lw=2, label=f"{label}: partial adjustment (band: alternative speeds)")
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
    tc.check_against_brief()   # the copied model reproduces paper 6.1
    rows = comparison()
    for r in rows:
        print(f"{r['pair']:28s} CPAT {r['cpat_dev']:+.2f}/{r['cpat_hic']:+.2f}  "
              f"lit {r['lit_most']:+.2f}..{r['lit_least']:+.2f} indep {r['indep_most']:+.2f}..{r['indep_least']:+.2f} "
              f"med {r['indep_median']:+.2f} ratio {r['cpat_over_median']:.2f}  {r['verdict']} / {r['verdict_indep']}")
    for r in income_table():
        print(r)
    for r in timing():
        if r["year"] in (1, 5, 10):
            print(r["case"], r["pair"], r["year"], r["partial"], r["share"], r["cpat_overstatement"])
    print(cpat_eta())
    for r in tecp_table():
        print(r)
    fig_comparison(rows)
    fig_timing()
