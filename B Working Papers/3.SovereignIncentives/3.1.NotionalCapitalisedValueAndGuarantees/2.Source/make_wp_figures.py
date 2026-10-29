"""Figures for working paper 3.1. Run: python3 make_wp_figures.py
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
    ax.text(2027.3, M.D_FOREST / 1e9 + 0.12, "Eligible green borrowing (\\$5bn): capacity above this is unused",
            fontsize=8, color=GREY)
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
    el = np.linspace(0.0005, 0.03, 300)
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    for ds, c in ((0.015, GREY), (0.03, BLUE), (0.045, ORANGE)):
        ax.plot(el * 100, [M.ratio(ds=ds, el=x) for x in el], color=c, lw=2,
                label=f"spread saved {ds*100:.1f} pp")
    ax.axhline(1, color="black", lw=0.8)
    for x, lab in ((M.EL_SERIES, "Series base case\n(3% calls × 37% loss)"),
                   (0.003, "10% loss\nper call")):
        ax.axvline(x * 100, color=GREY, ls=":", lw=1)
        ax.text(x * 100 + 0.06, 13.5, lab, fontsize=8, color=GREY, va="top")
    ax.set_xlabel("Guarantor's expected loss, % of exposure a year")
    ax.set_ylabel("Incentive value ÷ guarantor cost")
    ax.set_ylim(0, 15)
    ax.set_title("A guarantee is worth several times what it costs", fontsize=10, loc="left")
    ax.legend(frameon=False, fontsize=8, loc="upper right")
    fig.text(0.01, 0.01, "Buffer earns the discount rate, so cost = expected loss. "
             "MDB sovereign record (GEMs, 1984–2024): 0.04% a year, ratio about 80.", fontsize=7, color=GREY)
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
