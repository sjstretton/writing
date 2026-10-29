"""Figures for the working paper. Run from any folder: python3 make_wp_figures.py"""
import os
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import model as m  # noqa: E402


def fig_size(path):
    """Present value of each reward against the cost of a stylized reform."""
    u = m.uruguay_summary()
    c = m.coal_reform()
    gstar = c['pv_cost'] / (0.03 * m.annuity(m.R, 10))
    g = m.guarantee(gstar, 300, 0.01, 0.4, 0.10, 0.02, 10)
    labels = ["Uruguay 2023 loan:\nmaximum step-down (actual)",
              "Step-down of 100 bp\non a $1bn loan",
              "Entire interest waived\non a $1bn loan (6%)",
              f"Guarantee capacity of ${gstar/1000:.1f}bn\n(300 bp spread saved)",
              "Cost of the reform\n(stylized)"]
    vals = [u['pv'], m.rebate_value(1000, 100, 10), m.rebate_value(1000, 600, 10),
            g['incentive'], c['pv_cost']]
    cost = [u['pv'], m.rebate_value(1000, 100, 10), m.rebate_value(1000, 600, 10),
            g['cost'], None]
    fig, ax = plt.subplots(figsize=(8, 4.2))
    y = range(len(labels))[::-1]
    ax.barh(list(y), vals, color=["#1f6f8b", "#1f6f8b", "#1f6f8b", "#2a9d5c", "#b23a48"],
            label="Value to the government")
    for yi, cv in zip(y, cost):
        if cv is not None:
            ax.barh(yi, cv, height=0.35, color="none", edgecolor="black", hatch="///",
                    label=None)
    for yi, v in zip(y, vals):
        ax.text(v * 1.08, yi, f"${v:,.0f}m", va="center", fontsize=9)
    ax.set_xscale("log")
    ax.set_xlim(3, 4000)
    ax.set_yticks(list(y))
    ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlabel("Present value, US$ million (log scale), 5% discount rate, 10 years")
    ax.barh([-5], [1], color="none", edgecolor="black", hatch="///", label="Cost to the funder")
    ax.set_ylim(-0.6, len(labels) - 0.4)
    ax.legend(loc="upper right", fontsize=8, frameon=False)
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:,.0f}"))
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)


def fig_leverage(path):
    """Incentive value per dollar of funder cost, guarantee capacity vs cash rebate."""
    import numpy as np
    pds = np.linspace(0.0025, 0.03, 50)
    fig, ax = plt.subplots(figsize=(7, 3.8))
    for s, ls in ((150, ":"), (300, "-"), (450, "--")):
        ax.plot(pds * 100, [m.guarantee(1, s, p, 0.4, 0.10, 0.02, 10)['ratio'] for p in pds],
                ls, color="#2a9d5c", label=f"Guarantee capacity, {s} bp spread saved")
    ax.axhline(1, color="#1f6f8b", lw=2, label="Interest rebate or cash (ratio 1)")
    ax.set_xlabel("Annual probability of default on guaranteed debt (%), loss given default 40%")
    ax.set_ylabel("Incentive value per $1 of funder cost")
    ax.legend(fontsize=8, frameon=False)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    out = os.path.join(HERE, "figures")
    os.makedirs(out, exist_ok=True)
    fig_size(os.path.join(out, "fig1-size-problem.png"))
    fig_leverage(os.path.join(out, "fig2-leverage.png"))
    print("written to", out)
