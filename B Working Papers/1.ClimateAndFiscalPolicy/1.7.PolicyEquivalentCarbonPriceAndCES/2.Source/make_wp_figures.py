"""Figures and tables for working paper 1.7 (v0.3), "Measure Carbon Pricing by
the Emissions It Cuts: The Total Effective Carbon Price".

Run from this folder:   python make_wp_figures.py
Writes to figures/:
  fig1_weights.png        abatement weights vs emission shares, by sector and margin
  fig2_accuracy.png       first-order, second-order and exact TECP as policies scale up
  fig3_uncertainty.png    Monte Carlo distribution of the TECP (long and short run)
  fig4_horizon.png        TECP by horizon under partial adjustment
  wp_numbers.md           every number quoted in the paper, with the table rows
All numbers are for the stylized economy of tecp_model.py (the brief's economy).
"""

import copy
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

import tecp_model as M

HERE = Path(__file__).resolve().parent
OUT = HERE / "figures"
OUT.mkdir(exist_ok=True)

# Reference palette (dataviz skill), light mode; static figures for Word.
BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
INK, INK2, GRID, GRAY = "#0b0b0b", "#52514e", "#e4e3df", "#a3a29d"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9,
                     "axes.edgecolor": INK2, "axes.labelcolor": INK2,
                     "xtick.color": INK2, "ytick.color": INK2,
                     "axes.spines.top": False, "axes.spines.right": False})

# --------------------------------------------------------------------------
# Calibration ranges (Table 2 of the paper). Long-run sigma and |eta|;
# adjustment speeds per year. Uniform draws, independent across parameters.
# --------------------------------------------------------------------------
RANGES_LR = {
    "Power": {"sigma": (1.5, 3.0), "eta": (0.2, 0.5)},
    "Road transport": {"sigma": (0.5, 1.5), "eta": (0.3, 0.8)},
    "Industry": {"sigma": (0.5, 1.5), "eta": (0.3, 0.7)},
}
LAMBDA_INT = (0.04, 0.10)    # switching: capital turnover, per year
LAMBDA_EXT = (0.25, 0.40)    # demand: short-run / long-run elasticity ratio
CENTRAL_SPEEDS = (0.07, 0.35)
N_DRAWS = 2000
SEED = 20261029


def econ_with(params):
    econ = copy.deepcopy(M.ECON)
    for s, d in params.items():
        econ[s]["sigma"], econ[s]["eta"] = d["sigma"], d["eta"]
    return econ


def evaluate(econ, a_int=1.0, a_ext=1.0):
    """Credit price, and per-instrument and mix TECPs (first order and exact)."""
    kw = dict(a_int=a_int, a_ext=a_ext)
    # The standard enters through its long-run credit price at every horizon: a -2%
    # standard cannot bind within one year in this model at any price below the
    # level that drives the biofuel price to zero.
    lam = M.solve_lcfs_lambda(econ)
    out = {"lambda": lam}
    for k in M.INSTRUMENTS + ("mix",):
        keys = M.INSTRUMENTS if k == "mix" else (k,)
        dps = M.package_dp(lam, keys, econ=econ)
        out[k + "_lin"] = M.tecp_horizon_linear(dps, a_int, a_ext, econ)
        out[k + "_exact"] = M.tecp_exact_from_cut(M.exact_cut(dps, econ, **kw), econ, **kw)
    return out


def monte_carlo(short_run=False):
    rng = np.random.default_rng(SEED + int(short_run))
    rows = []
    for _ in range(N_DRAWS):
        params = {s: {k: rng.uniform(*v) for k, v in d.items()} for s, d in RANGES_LR.items()}
        a_int = a_ext = 1.0
        if short_run:
            a_int, a_ext = rng.uniform(*LAMBDA_INT), rng.uniform(*LAMBDA_EXT)
        rows.append(evaluate(econ_with(params), a_int, a_ext))
    return {k: np.array([r[k] for r in rows]) for k in rows[0]}


def pct(a, q):
    return float(np.percentile(a, q))


def main():
    lines = []
    lam = M.solve_lcfs_lambda()
    L, parts = M.Lambda(parts=True)
    E0 = {s: M.base_emissions(s) for s in M.SECTORS}
    Etot = sum(E0.values())
    lines.append(f"Baseline emissions {Etot:.1f} Mt; Lambda {L:.4f} Mt per $/t ({100 * L / Etot:.3f}% per $/t)")
    lines.append(f"Gamma (second derivative of uniform-tax cut) {M.Gamma():.5f}")
    for s in M.SECTORS:
        a, b = parts[s]
        st = M.stats(s)
        lines.append(f"{s}: emission share {E0[s] / Etot:.3f}; weight switching {a / L:.3f}, demand {b / L:.3f}; "
                     f"kappa {st['kappa']:.5f} t/$; X {st['X']:.0f} $m; omega_int_s {a / (a + b):.3f}")
    a_tot = sum(a for a, _ in parts.values())
    lines.append(f"Economy: switching share of Lambda {a_tot / L:.3f}")

    # ---------------- per-instrument numbers (Table 3) -----------------
    explicit = M.explicit_price_metric()
    rows = {}
    for k in M.INSTRUMENTS + ("mix",):
        keys = M.INSTRUMENTS if k == "mix" else (k,)
        dps = M.package_dp(lam, keys)
        sw = sum(M.linear_cut(s, dps[s])[0] for s in M.SECTORS) / L
        dm = sum(M.linear_cut(s, dps[s])[1] for s in M.SECTORS) / L
        rows[k] = dict(sw=sw, dm=dm, lin=sw + dm, sec=M.tecp_second_order(dps), ex=M.tecp_exact(dps),
                       cut=M.exact_cut(dps),
                       cut_lin=sum(sum(M.linear_cut(s, dps[s])) for s in M.SECTORS),
                       cut_sec=sum(sum(M.linear_cut(s, dps[s])) + M.second_order_term(s, dps[s]) for s in M.SECTORS))
    # explicit-price metric and shadow-price variants
    rows["tax"]["explicit"], rows["subsidy"]["explicit"], rows["standard"]["explicit"] = explicit, 0.0, 0.0
    rows["mix"]["explicit"] = explicit
    shadow_std = lam * E0["Road transport"] / Etot
    rows["tax"]["shadow"], rows["subsidy"]["shadow"], rows["standard"]["shadow"] = explicit, 0.0, shadow_std
    rows["mix"]["shadow"] = explicit + shadow_std
    qn = M.exact_quantities("Power", M.dp_instrument("subsidy", "Power"))
    spend = qn[2] * M.SUBSIDY  # $m: TWh x $/MWh
    avgcost = spend / rows["subsidy"]["cut"]
    lines.append(f"LCFS credit price {lam:.1f} $/t; renewable output with subsidy {qn[2]:.1f} TWh; "
                 f"subsidy spending {spend:.0f} $m; budgetary cost per tonne {avgcost:.1f} $/t")
    lines.append(f"Covered-emissions-weighted shadow price of the standard {shadow_std:.1f} $/t")
    lines.append("")
    lines.append("| Instrument | TECP switching | TECP demand | TECP first order | TECP second order | TECP exact | "
                 "cut exact Mt | cut linear | cut 2nd | explicit | explicit+shadow |")
    lines.append("|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|")
    for k, r in rows.items():
        lines.append(f"| {k} | {r['sw']:.2f} | {r['dm']:.2f} | {r['lin']:.2f} | {r['sec']:.2f} | {r['ex']:.2f} | "
                     f"{r['cut']:.2f} | {r['cut_lin']:.2f} | {r['cut_sec']:.2f} | {r['explicit']:.1f} | {r['shadow']:.1f} |")
    lines.append(f"Sum of stand-alone exact TECPs {sum(rows[k]['ex'] for k in M.INSTRUMENTS):.2f}; "
                 f"sum of stand-alone exact cuts {sum(rows[k]['cut'] for k in M.INSTRUMENTS):.2f}")

    # old (1 - w) form, as in the brief's check
    num = den = 0.0
    dps = M.package_dp(lam)
    for s in M.SECTORS:
        ei, ee, w, eb, C = M.semi_elasticities_old(s)
        _, q, p, e = M.arrays(s)
        Ef = q * e
        den += np.sum(Ef * (ei + ee))
        dp = dps[s]
        mean_dp = np.sum(w * dp)
        tau_ext = mean_dp / eb
        with np.errstate(divide="ignore", invalid="ignore"):
            prod = np.where(np.abs(e - eb) > 1e-12, ei * (dp - mean_dp) / (e - eb), 0.0)
        num += np.sum(Ef * (prod + ee * tau_ext))
    lines.append(f"Old (1 - w) form TECP of the mix: {num / den:.2f}")

    # ---------------- accuracy (Figure 2) -------------------------------
    ks = np.linspace(0.0, 3.0, 31)
    acc = {"lin": [], "sec": [], "ex": []}
    for k in ks:
        d = M.package_dp(lam, scale=k)
        acc["lin"].append(M.tecp_linear(d))
        acc["sec"].append(M.tecp_second_order(d))
        acc["ex"].append(M.tecp_exact(d))
    rates = np.linspace(0, 150, 31)
    acct = {"lin": [], "sec": [], "ex": []}
    for r in rates:
        d = {s: (M.dp_uniform(s, r) if s in M.TAX_SECTORS else np.zeros(3)) for s in M.SECTORS}
        acct["lin"].append(M.tecp_linear(d))
        acct["sec"].append(M.tecp_second_order(d))
        acct["ex"].append(M.tecp_exact(d))
    lines.append("")
    lines.append("Accuracy, mix scaled by k: k, linear, second, exact, err lin %, err 2nd %")
    for k, a, b, c in zip(ks, acc["lin"], acc["sec"], acc["ex"]):
        if k in (0.5, 1.0, 1.5, 2.0, 3.0):
            lines.append(f"  {k:.1f}: {a:.2f}, {b:.2f}, {c:.2f}, {100 * (a / c - 1):+.1f}, {100 * (b / c - 1):+.1f}")
    lines.append("Accuracy, tax on power+industry at rate r: r, linear, second, exact, err lin %, err 2nd %")
    for r, a, b, c in zip(rates, acct["lin"], acct["sec"], acct["ex"]):
        if r in (30, 60, 100, 150):
            lines.append(f"  {r:.0f}: {a:.2f}, {b:.2f}, {c:.2f}, {100 * (a / c - 1):+.1f}, {100 * (b / c - 1):+.1f}")
    # threshold: largest scale with linear error under 5 percent
    err = np.abs(np.array(acc["lin"][1:]) / np.array(acc["ex"][1:]) - 1)
    k5 = ks[1:][err < 0.05].max()
    lines.append(f"Linear error below 5% for mix scale k <= {k5:.1f} (exact TECP {acc['ex'][list(ks).index(k5)]:.1f})")

    # ---------------- horizon (Figure 4) --------------------------------
    li, lx = CENTRAL_SPEEDS
    Ts = np.arange(0, 31)
    hz = {k: {"lin": [], "ex": []} for k in M.INSTRUMENTS + ("mix",)}
    for T in Ts:
        aI, aX = 1 - (1 - li) ** max(T, 1e-9), 1 - (1 - lx) ** max(T, 1e-9)
        if T == 0:
            aI, aX = 1e-6 * li, 1e-6 * lx
        for k in hz:
            keys = M.INSTRUMENTS if k == "mix" else (k,)
            d = M.package_dp(lam, keys)
            hz[k]["lin"].append(M.tecp_horizon_linear(d, aI, aX))
            hz[k]["ex"].append(M.tecp_exact_from_cut(M.exact_cut(d, a_int=aI, a_ext=aX), a_int=aI, a_ext=aX))
    lines.append("")
    lines.append(f"Horizon TECP (lambda_int {li}, lambda_ext {lx}; credit price held at its long-run value):")
    for T in (1, 5, 10, 20, 30):
        lines.append("  T=%d: " % T + "; ".join(f"{k} lin {hz[k]['lin'][T]:.2f} exact {hz[k]['ex'][T]:.2f}" for k in hz))
    om = a_tot / L
    lines.append(f"  omega (LR switching share) {om:.3f}; omega_1 {(li * om) / (li * om + lx * (1 - om)):.3f}")

    # ---------------- Monte Carlo (Figure 3) ----------------------------
    mc = monte_carlo(False)
    mcs = monte_carlo(True)
    lines.append("")
    lines.append(f"Monte Carlo, {N_DRAWS} draws, seed {SEED}. Long run:")
    for key in ("mix_lin", "mix_exact", "tax_exact", "subsidy_exact", "standard_exact", "lambda"):
        a = mc[key]
        lines.append(f"  {key}: median {pct(a, 50):.1f}, 5th {pct(a, 5):.1f}, 95th {pct(a, 95):.1f}")
    lines.append("Short run (one year; adjustment speeds drawn):")
    for key in ("mix_lin", "mix_exact", "tax_exact", "subsidy_exact", "standard_exact"):
        a = mcs[key]
        lines.append(f"  {key}: median {pct(a, 50):.1f}, 5th {pct(a, 5):.1f}, 95th {pct(a, 95):.1f}")
    lines.append(f"  share of LR draws with mix TECP > explicit metric: {np.mean(mc['mix_exact'] > explicit):.3f}")
    lines.append(f"  LR ratio exact/linear: median {pct(mc['mix_exact'] / mc['mix_lin'], 50):.3f}, "
                 f"5th {pct(mc['mix_exact'] / mc['mix_lin'], 5):.3f}, 95th {pct(mc['mix_exact'] / mc['mix_lin'], 95):.3f}")
    # central short run at central speeds
    cs = evaluate(M.ECON, 1 - (1 - li), 1 - (1 - lx))
    lines.append(f"Central case, one year: mix lin {cs['mix_lin']:.2f}, exact {cs['mix_exact']:.2f}; tax {cs['tax_exact']:.2f}; "
                 f"subsidy {cs['subsidy_exact']:.2f}; standard {cs['standard_exact']:.2f} (credit price held at {cs['lambda']:.0f})")

    (OUT / "wp_numbers.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))

    # ======================= FIGURES =====================================
    # Figure 1: emission shares vs abatement weights
    fig, ax = plt.subplots(figsize=(7.0, 2.9), dpi=200)
    y = np.arange(len(M.SECTORS))[::-1].astype(float)
    h = 0.36
    for i, s in enumerate(M.SECTORS):
        a, b = parts[s][0] / L, parts[s][1] / L
        ax.barh(y[i] + h / 2 + 0.02, a, height=h, color=BLUE, edgecolor="white", linewidth=1.0)
        ax.barh(y[i] + h / 2 + 0.02, b, height=h, left=a, color=ORANGE, edgecolor="white", linewidth=1.0)
        ax.text(a + b + 0.01, y[i] + h / 2 + 0.02, f"{100 * (a + b):.0f}% of abatement weight", va="center",
                fontsize=8.5, color=INK)
        es = E0[s] / Etot
        ax.barh(y[i] - h / 2 - 0.02, es, height=h, color=GRAY, edgecolor="white", linewidth=1.0)
        ax.text(es + 0.01, y[i] - h / 2 - 0.02, f"{100 * es:.0f}% of emissions", va="center", fontsize=8.5, color=INK2)
    ax.set_yticks(y)
    ax.set_yticklabels(M.SECTORS)
    ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)
    ax.set_xlim(0, 0.95)
    ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    ax.xaxis.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=BLUE, label="Abatement weight: fuel switching"),
                       Patch(color=ORANGE, label="Abatement weight: demand"),
                       Patch(color=GRAY, label="Share of baseline emissions")],
              loc="lower center", bbox_to_anchor=(0.45, -0.38), ncol=3, frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(OUT / "fig1_weights.png", bbox_inches="tight", facecolor="white")
    plt.close(fig)

    # Figure 2: accuracy
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.0), dpi=200)
    for ax, xs, data, xlabel, title in (
            (axes[0], ks, acc, "Policy mix scaled by k (k = 1 is the example)", "A. The policy mix"),
            (axes[1], rates, acct, "Carbon tax on power and industry ($/tCO₂)", "B. The carbon tax alone")):
        ax.plot(xs, data["ex"], color=INK, linewidth=2, label="Exact (iterative)")
        ax.plot(xs, data["sec"], color=BLUE, linewidth=2, linestyle="--", label="Second order")
        ax.plot(xs, data["lin"], color=ORANGE, linewidth=2, linestyle=":", label="First order")
        ax.set_xlabel(xlabel, fontsize=8.5)
        ax.set_title(title, fontsize=9, loc="left", color=INK)
        ax.grid(True, color=GRID, linewidth=0.8)
        ax.set_axisbelow(True)
    axes[0].set_ylabel("TECP ($/tCO₂)")
    axes[0].axvline(1.0, color=GRAY, linewidth=0.8)
    axes[1].axvline(30.0, color=GRAY, linewidth=0.8)
    axes[0].legend(frameon=False, fontsize=8, loc="upper left")
    fig.tight_layout()
    fig.savefig(OUT / "fig2_accuracy.png", bbox_inches="tight", facecolor="white")
    plt.close(fig)

    # Figure 3: Monte Carlo
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.0), dpi=200, gridspec_kw={"width_ratios": [1.3, 1]})
    ax = axes[0]
    bins = np.linspace(min(mcs["mix_exact"].min(), mc["mix_exact"].min()) - 1,
                       max(mcs["mix_exact"].max(), mc["mix_exact"].max()) + 1, 50)
    ax.hist(mc["mix_exact"], bins=bins, color=BLUE, alpha=0.85, label="Long run", edgecolor="white", linewidth=0.5)
    ax.hist(mcs["mix_exact"], bins=bins, color=ORANGE, alpha=0.75, label="One year", edgecolor="white", linewidth=0.5)
    ax.set_xlim(explicit - 2, bins[-1])
    ax.axvline(explicit, color=INK2, linewidth=1.2, linestyle="--")
    ax.text(explicit + 0.4, ax.get_ylim()[1] * 0.55, f"Explicit-price\nmetric ${explicit:.1f}", fontsize=7.5,
            color=INK2, va="top")
    ax.axvline(rows["mix"]["ex"], color=INK, linewidth=1.2)
    ax.text(rows["mix"]["ex"] + 0.4, ax.get_ylim()[1] * 0.62, f"Central\ncase ${rows['mix']['ex']:.1f}", fontsize=7.5,
            color=INK, va="top")
    ax.set_xlabel("Exact TECP of the policy mix ($/tCO₂)", fontsize=8.5)
    ax.set_ylabel("Draws", fontsize=8.5)
    ax.set_title("A. Policy mix", fontsize=9, loc="left", color=INK)
    ax.legend(frameon=False, fontsize=8, loc="upper left")
    ax.grid(True, axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax = axes[1]
    names = [("tax", "Carbon tax"), ("subsidy", "Renewable\nsubsidy"), ("standard", "Fuel standard")]
    for j, (k, lab) in enumerate(names):
        for off, data, col in ((-0.13, mc, BLUE), (0.13, mcs, ORANGE)):
            a = data[k + "_exact"]
            ax.plot([pct(a, 5), pct(a, 95)], [j + off] * 2, color=col, linewidth=2.2, solid_capstyle="round")
            ax.plot(pct(a, 50), j + off, "o", color=col, markersize=6, markeredgecolor="white", markeredgewidth=1.2)
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels([n[1] for n in names], fontsize=8)
    ax.invert_yaxis()
    ax.tick_params(axis="y", length=0)
    ax.set_xlabel("Exact TECP, 5th–95th percentile ($/tCO₂)", fontsize=8.5)
    ax.set_title("B. By instrument", fontsize=9, loc="left", color=INK)
    ax.grid(True, axis="x", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    fig.tight_layout()
    fig.savefig(OUT / "fig3_uncertainty.png", bbox_inches="tight", facecolor="white")
    plt.close(fig)

    # Figure 4: horizon
    fig, ax = plt.subplots(figsize=(7.0, 3.0), dpi=200)
    for k, col, lab in (("mix", INK, "Policy mix"), ("tax", BLUE, "Carbon tax"),
                        ("subsidy", ORANGE, "Renewable subsidy"), ("standard", AQUA, "Fuel standard")):
        ax.plot(Ts[1:], np.array(hz[k]["ex"])[1:], color=col, linewidth=2)
        ax.plot(Ts[1:], np.array(hz[k]["lin"])[1:], color=col, linewidth=1.2, linestyle=":")
        ax.text(Ts[-1] + 0.4, hz[k]["ex"][-1], lab, va="center", fontsize=8, color=INK)
    ax.set_xlim(0, 36)
    ax.set_xlabel("Years after the policy starts", fontsize=8.5)
    ax.set_ylabel("TECP ($/tCO₂)", fontsize=8.5)
    ax.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    from matplotlib.lines import Line2D
    ax.legend(handles=[Line2D([0], [0], color=INK2, linewidth=2, label="Exact"),
                       Line2D([0], [0], color=INK2, linewidth=1.2, linestyle=":", label="First order")],
              frameon=False, fontsize=8, loc="center right", bbox_to_anchor=(0.86, 0.55))
    fig.tight_layout()
    fig.savefig(OUT / "fig4_horizon.png", bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("figures written to", OUT)


if __name__ == "__main__":
    main()
