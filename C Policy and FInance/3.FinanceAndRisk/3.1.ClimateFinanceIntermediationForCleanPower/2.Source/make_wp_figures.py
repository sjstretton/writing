"""Figures for the working paper. Run: python3 make_wp_figures.py (writes figures/*.png)."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import model as M

OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(exist_ok=True)
BLUE, ORANGE, AQUA, GREY, INK, INK2 = "#2a78d6", "#eb6834", "#1baf7a", "#c3c2b7", "#0b0b0b", "#52514e"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.edgecolor": INK2, "axes.labelcolor": INK, "xtick.color": INK2,
                     "ytick.color": INK2, "axes.grid": True, "grid.color": "#e6e5e0",
                     "grid.linewidth": 0.6, "figure.dpi": 150, "savefig.bbox": "tight"})


def fig_lcoe():
    rs = [x / 1000 for x in range(30, 161, 2)]
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot([r * 100 for r in rs], [M.lcoe(r) for r in rs], color=BLUE, lw=2)
    for r in [0.05, 0.08, 0.12]:
        ax.plot(r * 100, M.lcoe(r), "o", ms=7, color=BLUE, mec="white", mew=2)
        ax.annotate(f"{r:.0%}: {M.lcoe(r):.1f}¢", (r * 100, M.lcoe(r)), xytext=(6, -14),
                    textcoords="offset points", color=INK, fontsize=9)
    t = M.tariff_no_guarantee()
    ax.axhspan(M.lcoe(M.R0), t, color=ORANGE, alpha=0.18, lw=0)
    ax.text(3.2, (M.lcoe(M.R0) + t) / 2, "offtaker premium, central case\n(stylized): +%.1f¢" % (t - M.lcoe(M.R0)),
            va="center", fontsize=8.5, color=INK2)
    ax.set_xlabel("Weighted average cost of capital, real (%)")
    ax.set_ylabel("Levelized cost (US cents/kWh)")
    ax.set_ylim(3, 8.2)
    fig.savefig(OUT / "fig1_lcoe_wacc.png")
    plt.close(fig)


def fig_premium():
    lams = [x / 100 for x in range(0, 31)]
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    for R, c in [(0.3, ORANGE), (0.6, BLUE), (0.9, AQUA)]:
        ys = [(M.wacc_equivalent(M.tariff_with_risk(l, R, M.DELAY, M.R0, M.MPR)) - M.R0) * 100 if l > 0 else 0
              for l in lams]
        ax.plot([l * 100 for l in lams], ys, color=c, lw=2, label=f"{R:.0%} of arrears recovered")
        ax.text(30.4, ys[-1], f"R = {R:.0%}", va="center", fontsize=9, color=INK)
    ax.set_xlabel("Default episodes per 100 offtaker-years (one-year episodes)")
    ax.set_ylabel("Offtaker premium in WACC (pp)")
    ax.legend(frameon=False, fontsize=8.5, loc="upper left")
    ax.set_xlim(0, 34)
    fig.savefig(OUT / "fig2_offtaker_premium.png")
    plt.close(fig)


def fig_guarantees():
    t0, tc, td = M.tariff_no_guarantee(), M.tariff_contract_guarantee(), M.tariff_debt_guarantee()
    sc = M.annual_revenue_musd(t0) - M.annual_revenue_musd(tc)
    sd = M.annual_revenue_musd(t0) - M.annual_revenue_musd(td)
    gc = M.guarantor_cost_contract()
    go, gx, debt, _ = M.guarantor_cost_debt()
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.2), sharey=True)
    labels = ["Contract\nguarantee", "Debt\nguarantee"]
    ax = axes[0]
    ax.bar([0, 1], [sc, sd], color=BLUE, width=0.55)
    for i, v in enumerate([sc, sd]):
        ax.text(i, v + 0.02, f"${v:.2f}m", ha="center", fontsize=9, color=INK)
    ax.set_xticks([0, 1], labels)
    ax.set_title("Saving to offtaker ($m/yr)", fontsize=10, color=INK)
    ax = axes[1]
    ax.bar([0, 1], [gc, go], color=ORANGE, width=0.55, label="Offtaker risk")
    ax.bar([1], [gx], bottom=[go], color=GREY, width=0.55, label="Other risks (debt only)")
    for i, v in enumerate([gc, go + gx]):
        ax.text(i, v + 0.01, f"${v:.2f}m", ha="center", fontsize=9, color=INK)
    ax.set_xticks([0, 1], labels)
    ax.set_title("Expected cost to guarantors ($m/yr)", fontsize=10, color=INK)
    ax.legend(frameon=False, fontsize=8, loc="upper right")
    ax.set_ylim(0, sc * 1.15)
    for a in axes:
        a.grid(axis="x", visible=False)
    fig.tight_layout()
    fig.savefig(OUT / "fig3_contract_vs_debt.png")
    plt.close(fig)


def fig_waterfall():
    annual = M.REG_MW * 1000 * M.KWH_PER_KW * M.lcoe(M.R0) / 100 / 1e6
    qs = [q for _, q in M.LAYERS[1:]]
    costs, _ = M.waterfall_expected_costs(M.LAM, annual, M.REC_F, M.DELAY, M.R0, qs)
    arrears = M.phi(M.LAM, M.DELAY) * annual
    recovered = arrears * M.rtilde(M.REC_F, M.DELAY, M.R0)
    names = ["Offtaker repays (value)"] + [n for n, _ in M.LAYERS[1:]]
    vals = [recovered] + costs
    fig, ax = plt.subplots(figsize=(6.4, 3.2))
    y = list(range(len(names)))[::-1]
    ax.barh(y, vals, color=[AQUA] + [BLUE] * 4, height=0.55)
    for yi, v in zip(y, vals):
        ax.text(v + 0.2, yi, f"${v:.1f}m", va="center", fontsize=9, color=INK)
    ax.set_yticks(y, names)
    ax.set_xlabel("Expected value per year ($m), regional facility, 2 GW (stylized)")
    ax.grid(axis="y", visible=False)
    ax.set_xlim(0, max(vals) * 1.2)
    fig.savefig(OUT / "fig4_waterfall.png")
    plt.close(fig)


if __name__ == "__main__":
    fig_lcoe(); fig_premium(); fig_guarantees(); fig_waterfall()
    print("written:", sorted(p.name for p in OUT.glob("*.png")))
