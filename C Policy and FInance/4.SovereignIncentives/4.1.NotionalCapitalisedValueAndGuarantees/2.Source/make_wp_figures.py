"""Figures for working paper 4.1. Run: python3 make_wp_figures.py
Writes PNGs to ./figures/. All inputs come from model.py (stylized unless noted there).
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import model as M

HERE = Path(__file__).resolve().parent
OUT = HERE / "figures"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
BLUE, ORANGE, GREY = "#2a6fb0", "#d9822b", "#888888"


def fig_balance(path):
    Bb = M.balance_path(M.D_FOREST, M.P_E, M.A_PATH, M.E_BAU)
    Ba = M.balance_path(M.D_FOREST, M.P_E, M.A_PATH, M.E_ACT)
    yrs = np.append(M.YEARS, M.YEARS[-1] + 1)
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(yrs, Ba / 1e9, color=BLUE, lw=2, label="Acts now: emissions 15 → 3 Mt by 2037")
    ax.plot(yrs, Bb / 1e9, color=ORANGE, lw=2, label="Business as usual: 15 Mt a year")
    ax.axhline(M.D_FOREST / 1e9, color=GREY, ls="--", lw=1)
    ax.text(2050.8, M.D_FOREST / 1e9 - 0.38, "Eligible green borrowing (\\$5bn):\ncapacity above this line is unused",
            fontsize=8, color=GREY, ha="right", va="top")
    ax.set_ylabel("Balance = guarantee capacity, $bn")
    ax.set_ylim(0, 6)
    ax.set_title("A per-tonne debit drains the balance under business as usual", fontsize=10, loc="left")
    ax.legend(frameon=False, fontsize=8, loc="lower left")
    fig.text(0.01, 0.01, "Stylized forest country: opening balance \\$5bn, debit \\$50/tCO2 against an allowance "
             "falling from 12 Mt to zero in 2050.", fontsize=7, color=GREY)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(path, dpi=200)
    plt.close(fig)


def fig_ratio(path):
    el = np.geomspace(0.0002, 0.03, 300)
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    for ds, c in ((0.015, GREY), (0.03, BLUE), (0.045, ORANGE)):
        ax.plot(el * 100, [M.ratio(ds=ds, el=x, k=0.0) for x in el], color=c, lw=2,
                label=f"spread saved {ds*100:.1f} pp")
    ax.plot(el * 100, [min(M.econ_ratio(ds=0.03, el=x), M.ratio(ds=0.03, el=x, k=0.0)) for x in el], color=BLUE, lw=1.5, ls="--",
            label="3.0 pp, net of the default option")
    ax.axhline(1, color="black", lw=0.8)
    for x, lab in ((M.EL_GEMS, "Base: MDB record\n(0.77% × 4.9%)\nratio 80"),
                   (M.EL_MID, "Middle: 3% × 10%\nratio 10"),
                   (M.EL_SERIES, "Stress:\n3% × 37%\nratio 2.7")):
        ax.axvline(x * 100, color=GREY, ls=":", lw=1)
        ax.text(x * 100 * 1.08, 0.27, lab, fontsize=7, color="#444444", va="bottom")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xticks([0.02, 0.05, 0.1, 0.3, 1, 3])
    ax.set_xticklabels(["0.02", "0.05", "0.1", "0.3", "1", "3"])
    ax.set_yticks([1, 3, 10, 30, 100])
    ax.set_yticklabels(["1", "3", "10", "30", "100"])
    ax.set_ylim(0.25, 250)
    ax.set_xlabel("Guarantor's expected loss, % of exposure a year (log scale)")
    ax.set_ylabel("Incentive value ÷ guarantor cost (log)")
    ax.set_title("A guarantee is worth many times what it costs", fontsize=10, loc="left")
    ax.legend(frameon=False, fontsize=8, loc="upper right")
    fig.text(0.01, 0.01, "Cost = expected loss (buffer earns the discount rate). Dashed: risk premium (a third of a 3 pp spread) "
             "plus expected loss.", fontsize=7, color=GREY)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(path, dpi=200)
    plt.close(fig)


def fig_timing(path):
    K0, dE, g = 1e9, 5e6, 0.05
    m0 = (M.R + g) * K0 / dE
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    for share, c, lab in ((1.2, BLUE, "120% of minimum: act now"),
                          (0.6, ORANGE, "60% of minimum: delay always better"),
                          (0.0, GREY, "No incentive: never act")):
        t, W = M.early_action(K0, dE, g, m0 * share)
        ax.plot(t, W / 1e6, color=c, lw=2, label=lab)
    ax.axhline(0, color="black", lw=0.8)
    ax.set_xlabel("Year of adoption")
    ax.set_ylabel("Net present value of adopting, $m")
    ax.set_title("Below the minimum incentive, delay beats acting now", fontsize=10, loc="left")
    ax.legend(frameon=False, fontsize=8)
    fig.text(0.01, 0.01, "Stylized reform: \\$1bn up-front cost falling 5% a year; cuts 5 MtCO2 a year; "
             "incentive decays at 5% a year; discount rate 5%.", fontsize=7, color=GREY)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(path, dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    fig_balance(OUT / "fig1-balance-paths.png")
    fig_ratio(OUT / "fig2-incentive-cost-ratio.png")
    fig_timing(OUT / "fig3-early-action.png")
    print("written to", OUT)
