"""Worked example and figure for Climate Fiscal Policy Brief No. 1.7,
"The Total Effective Carbon Price".

A stylized three-sector economy (power, road transport, industry) with a
nested CES energy demand in each sector. Three instruments:
  1. a carbon tax of $30/tCO2 on power and industry fuels (explicit price);
  2. a renewable power subsidy of $10/MWh (price-based subsidy);
  3. a tradable low-carbon fuel standard on road fuels (non-price).

The script computes, for each instrument and for the package:
  - the first-order Total Effective Carbon Price (TECP), split into the
    fuel-switching (intensive) and demand (extensive) margins;
  - the exact uniform tax that matches the package's emission cut in the full
    nonlinear CES model (a check on the linear formula);
  - an explicit-price metric of the effective-carbon-rate type (emissions-
    weighted average of explicit carbon prices), for comparison;
  - for the standard, both the shadow-price route and the back-out route.

All numbers are stylized. Run:  python make_figures.py
Outputs (beside this script): tecp_example.png, tecp_example_table.md
"""

from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent

# --------------------------------------------------------------------------
# Stylized economy. Quantities: power in TWh (prices $/MWh, emission factors
# tCO2/MWh); transport and industry in PJ ($/GJ, tCO2/GJ). In both cases
# quantity x emission factor gives MtCO2. Prices are delivered prices
# including existing taxes; power prices are levelized costs per MWh.
# sigma: within-sector substitution elasticity; eta: |service demand
# elasticity|. Both lie within the sector ranges given in the working paper.
# --------------------------------------------------------------------------
ECON = {
    "Power": {
        "sigma": 2.0, "eta": 0.2,
        "fuels": {  # name: (quantity, price, emission factor)
            "Coal": (100.0, 70.0, 0.95),
            "Gas": (60.0, 80.0, 0.40),
            "Renewables": (40.0, 70.0, 0.0),
        },
    },
    "Road transport": {
        "sigma": 1.5, "eta": 0.4,
        "fuels": {
            "Gasoline": (600.0, 30.0, 0.069),
            "Diesel": (500.0, 28.0, 0.074),
            "Biofuel": (80.0, 34.0, 0.025),
        },
    },
    "Industry": {
        "sigma": 0.8, "eta": 0.3,
        "fuels": {
            "Coal": (300.0, 4.0, 0.095),
            "Oil": (150.0, 18.0, 0.074),
            "Gas": (400.0, 10.0, 0.056),
        },
    },
}

TAX = 30.0            # $/tCO2 on power and industry
TAX_SECTORS = ("Power", "Industry")
SUBSIDY = 10.0        # $/MWh paid to renewable generation
LCFS_CUT = 0.02       # standard: road-fuel carbon intensity 2% below baseline


def arrays(sector):
    d = ECON[sector]["fuels"]
    names = list(d)
    q, p, e = (np.array([d[n][i] for n in names]) for i in range(3))
    return names, q, p, e


def cost_shares(sector):
    _, q, p, _ = arrays(sector)
    return q * p / np.sum(q * p)


# ---------------- first-order (linear) emission cut -----------------------
def linear_cut(sector, dp):
    """Emission reduction (MtCO2) to first order, split (intensive, extensive).

    Exact first-order derivative of the CES system:
      dln q_f = -sigma (pi_f - pibar) - eta * pibar,
      pi_f = dp_f / p_f,  pibar = sum_g s_g pi_g  (= dln C, the cost index).
    """
    sig, eta = ECON[sector]["sigma"], ECON[sector]["eta"]
    _, q, p, e = arrays(sector)
    E = q * e
    pi = dp / p
    pibar = np.sum(cost_shares(sector) * pi)
    intensive = np.sum(E * sig * (pi - pibar))
    extensive = np.sum(E) * eta * pibar
    return intensive, extensive


def semi_elasticities(sector):
    """eps_int_f = sigma (e_f/p_f - kappa); eps_ext = eta kappa,
    kappa = sum_f s_f e_f / p_f (emissions per dollar of energy spending)."""
    sig, eta = ECON[sector]["sigma"], ECON[sector]["eta"]
    _, q, p, e = arrays(sector)
    kappa = np.sum(cost_shares(sector) * e / p)
    return sig * (e / p - kappa), eta * kappa, kappa


# ---------------- exact nonlinear CES ------------------------------------
def exact_emissions(sector, dp):
    sig, eta = ECON[sector]["sigma"], ECON[sector]["eta"]
    _, q, p, e = arrays(sector)
    s = cost_shares(sector)
    P = (p + dp) / p
    if abs(sig - 1.0) < 1e-9:
        C = np.prod(P ** s)
    else:
        C = np.sum(s * P ** (1 - sig)) ** (1 / (1 - sig))
    qn = q * P ** (-sig) * C ** (sig - eta)
    return qn, np.sum(qn * e)


def base_emissions(sector):
    _, q, _, e = arrays(sector)
    return np.sum(q * e)


def bisect(f, lo, hi, n=200):
    flo = f(lo)
    for _ in range(n):
        mid = 0.5 * (lo + hi)
        fm = f(mid)
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ---------------- instruments as price changes ---------------------------
def dp_tax(sector, rate):
    _, _, _, e = arrays(sector)
    return rate * e


def dp_instrument(name, sector, lcfs_lambda=None):
    names, q, p, e = arrays(sector)
    dp = np.zeros_like(p)
    if name == "tax" and sector in TAX_SECTORS:
        dp = TAX * e
    elif name == "subsidy" and sector == "Power":
        dp = np.array([-SUBSIDY if n == "Renewables" else 0.0 for n in names])
    elif name == "standard" and sector == "Road transport":
        dp = lcfs_lambda * (e - lcfs_target())
    return dp


def lcfs_target():
    _, q, _, e = arrays("Road transport")
    return (1 - LCFS_CUT) * np.sum(q * e) / np.sum(q)


def solve_lcfs_lambda():
    """Credit price at which the standard just binds in the exact CES model."""
    sector = "Road transport"
    _, q, _, e = arrays(sector)
    target = lcfs_target()

    def gap(lam):
        qn, en = exact_emissions(sector, lam * (e - target))
        return en / np.sum(qn) - target

    return bisect(gap, 0.0, 600.0)


def exact_uniform_equivalent(sectors, E0, cut):
    """Back-out route: the uniform tax whose cut in the full CES model equals `cut`."""
    def gap(t):
        return sum(E0[s] - exact_emissions(s, dp_tax(s, t))[1] for s in sectors) - cut
    return bisect(gap, 0.0, 200.0)


def main():
    sectors = list(ECON)
    E0 = {s: base_emissions(s) for s in sectors}
    E_total = sum(E0.values())

    # Normalization: first-order cut from a $1/tCO2 uniform tax.
    lam_parts = {s: linear_cut(s, dp_tax(s, 1.0)) for s in sectors}
    LAMBDA = sum(a + b for a, b in lam_parts.values())

    lcfs_lambda = solve_lcfs_lambda()

    instruments = [
        ("tax", f"Carbon tax, ${TAX:.0f}/tCO2 (power, industry)",
         f"${TAX:.0f}/t"),
        ("subsidy", f"Renewable subsidy, ${SUBSIDY:.0f}/MWh (power)",
         f"${SUBSIDY:.0f}/MWh"),
        ("standard", f"Low-carbon fuel standard, -{LCFS_CUT:.0%} intensity (road)",
         f"${lcfs_lambda:.0f}/t (credit price)"),
    ]

    rows = []
    pkg_dp = {s: np.zeros(len(ECON[s]["fuels"])) for s in sectors}
    for key, label, nominal in instruments:
        inten = exten = 0.0
        exact_cut = 0.0
        for s in sectors:
            dp = dp_instrument(key, s, lcfs_lambda)
            pkg_dp[s] = pkg_dp[s] + dp
            a, b = linear_cut(s, dp)
            inten += a
            exten += b
            exact_cut += E0[s] - exact_emissions(s, dp)[1]
        explicit = 0.0
        if key == "tax":
            explicit = TAX * sum(E0[s] for s in TAX_SECTORS) / E_total
        rows.append(dict(key=key, label=label, nominal=nominal,
                         cut_lin=inten + exten, cut_exact=exact_cut,
                         t_int=inten / LAMBDA, t_ext=exten / LAMBDA,
                         tecp=(inten + exten) / LAMBDA,
                         tecp_backout=exact_uniform_equivalent(sectors, E0, exact_cut),
                         explicit=explicit))

    # Package: linear sum, and exact check.
    pkg_lin = sum(r["cut_lin"] for r in rows)
    pkg_exact_cut = sum(E0[s] - exact_emissions(s, pkg_dp[s])[1] for s in sectors)

    tecp_exact = exact_uniform_equivalent(sectors, E0, pkg_exact_cut)
    tecp_lin = pkg_lin / LAMBDA
    explicit_total = sum(r["explicit"] for r in rows)

    # Shares of Lambda by margin and sector (the abatement weights).
    weights = {s: (a / LAMBDA, b / LAMBDA) for s, (a, b) in lam_parts.items()}

    # ---------------- console report -----------------------------------
    print(f"Baseline emissions: {E_total:.1f} MtCO2 "
          + ", ".join(f"{s} {E0[s]:.1f}" for s in sectors))
    print(f"Lambda (cut from $1/t uniform tax): {LAMBDA:.4f} MtCO2 per $/t "
          f"({LAMBDA / E_total * 100:.3f}% of emissions per $/t)")
    for s in sectors:
        ei, ee, kappa = semi_elasticities(s)
        print(f"  {s:15s} weight: switching {weights[s][0]:.3f}, demand {weights[s][1]:.3f}; "
              f"kappa={kappa:.5f} t/$; eps_int={np.round(ei, 5)}; eps_ext={ee:.5f}")
    print(f"LCFS: target {lcfs_target():.5f} t/GJ, credit price {lcfs_lambda:.1f} $/t")
    for r in rows:
        print(f"{r['label']:55s} cut lin {r['cut_lin']:6.2f} exact {r['cut_exact']:6.2f} Mt | "
              f"TECP {r['tecp']:6.2f} (switch {r['t_int']:6.2f}, demand {r['t_ext']:6.2f}) "
              f"full-model {r['tecp_backout']:6.2f} | explicit {r['explicit']:5.2f}")
    print(f"Package: linear cut {pkg_lin:.2f} Mt, exact cut {pkg_exact_cut:.2f} Mt "
          f"({pkg_exact_cut / E_total * 100:.1f}% of baseline)")
    print(f"TECP linear {tecp_lin:.2f} $/t; exact uniform-tax equivalent {tecp_exact:.2f} $/t; "
          f"explicit-price metric {explicit_total:.2f} $/t")

    # Comparison: source formula with the (1 - w) factor and energy shares.
    src_num = src_den = 0.0
    for s in sectors:
        sig, eta = ECON[s]["sigma"], ECON[s]["eta"]
        _, q, p, e = arrays(s)
        w = q / q.sum()
        ebar = np.sum(w * e)
        Cs = np.sum(w * p)
        E = q * e
        eint = sig * (1 - w) * (e - ebar) / p
        eext = eta * ebar / Cs
        src_den += np.sum(E * (eint + eext))
        dp = pkg_dp[s]
        mean_dp = np.sum(w * dp)
        tau_ext = mean_dp / ebar
        with np.errstate(divide="ignore", invalid="ignore"):
            prod_int = np.where(np.abs(e - ebar) > 1e-12,
                                eint * (dp - mean_dp) / (e - ebar), 0.0)
        src_num += np.sum(E * (prod_int + eext * tau_ext))
    print(f"[check] working-paper semi-elasticities with (1-w) factor give TECP "
          f"{src_num / src_den:.2f} $/t")

    # ---------------- markdown table for the brief ----------------------
    lines = [
        "| Instrument | Rate or shadow price | Explicit-price metric ($/t) "
        "| Emission cut, full model (MtCO₂) | TECP: switching ($/t) | TECP: demand ($/t) | TECP ($/t) |",
        "|---|---|--:|--:|--:|--:|--:|",
    ]
    for r in rows:
        lines.append(f"| {r['label']} | {r['nominal']} | {r['explicit']:.1f} | "
                     f"{r['cut_exact']:.1f} | {r['t_int']:.1f} | {r['t_ext']:.1f} | {r['tecp']:.1f} |")
    lines.append(f"| **Policy mix** | | **{explicit_total:.1f}** | **{pkg_exact_cut:.1f}** | "
                 f"**{sum(r['t_int'] for r in rows):.1f}** | **{sum(r['t_ext'] for r in rows):.1f}** | "
                 f"**{tecp_lin:.1f}** |")
    (HERE / "tecp_example_table.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))

    # ---------------- figure ------------------------------------------
    BLUE, ORANGE = "#2a78d6", "#eb6834"
    INK, INK2, GRID = "#0b0b0b", "#52514e", "#e4e3df"
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9.5,
                         "axes.edgecolor": INK2, "axes.labelcolor": INK2,
                         "xtick.color": INK2, "ytick.color": INK})

    labels = [f"Carbon tax\n${TAX:.0f}/t, power + industry",
              f"Renewable subsidy\n${SUBSIDY:.0f}/MWh, power",
              f"Low-carbon fuel standard\ncredit price ${lcfs_lambda:.0f}/t, road",
              "Policy mix"]
    t_int = [r["t_int"] for r in rows] + [sum(r["t_int"] for r in rows)]
    t_ext = [r["t_ext"] for r in rows] + [sum(r["t_ext"] for r in rows)]
    expl = [r["explicit"] for r in rows] + [explicit_total]
    tecp = [r["tecp"] for r in rows] + [tecp_lin]

    fig, ax = plt.subplots(figsize=(7.2, 3.9), dpi=200)
    y = np.arange(len(labels))[::-1].astype(float)
    y[-1] -= 0.0
    h = 0.34
    for i in range(len(labels)):
        yi = y[i]
        # TECP bar (upper) stacked by margin; negatives drawn left of zero.
        pos_left = 0.0
        neg_left = 0.0
        for val, col in ((t_int[i], BLUE), (t_ext[i], ORANGE)):
            if val >= 0:
                ax.barh(yi + h / 2 + 0.02, val, height=h, left=pos_left, color=col,
                        edgecolor="white", linewidth=1.0)
                pos_left += val
            else:
                ax.barh(yi + h / 2 + 0.02, val, height=h, left=neg_left, color=col,
                        edgecolor="white", linewidth=1.0)
                neg_left += val
        extra = f"  (full model {tecp_exact:.1f})" if i == len(labels) - 1 else ""
        ax.text(max(pos_left, 0) + 0.6, yi + h / 2 + 0.02, f"TECP {tecp[i]:.1f}{extra}",
                va="center", ha="left", color=INK, fontsize=9)
        # Explicit-price metric bar (lower), neutral gray.
        ax.barh(yi - h / 2 - 0.02, expl[i], height=h, color="#a3a29d",
                edgecolor="white", linewidth=1.0)
        ax.text(max(expl[i], 0) + 0.6, yi - h / 2 - 0.02,
                f"explicit {expl[i]:.1f}", va="center", ha="left", color=INK2, fontsize=9)

    ax.axvline(0, color=INK2, linewidth=0.8)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.set_xlabel("$/tCO₂ (stylized economy)")
    ax.set_xlim(min(-2, min(t_ext) - 1), max(max(tecp), max(expl)) + 14)
    ax.xaxis.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.tick_params(axis="y", length=0)
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=BLUE, label="TECP: fuel-switching margin"),
                       Patch(color=ORANGE, label="TECP: demand margin"),
                       Patch(color="#a3a29d", label="Explicit-price metric (ECR type)")],
              loc="lower center", bbox_to_anchor=(0.42, -0.30), ncol=3, frameon=False,
              fontsize=8.5)
    fig.tight_layout()
    out = HERE / "tecp_example.png"
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
