"""Figures for the working paper. Run from anywhere: python3 make_wp_figures.py"""
import os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import model as M

OUT = os.path.join(HERE, "figures")
os.makedirs(OUT, exist_ok=True)
C = ["#1f4e79", "#c55a11", "#548235", "#7f7f7f"]


def fig_subordination(path, title=True):
    rho = np.linspace(0.01, 0.40, 80)
    fig, ax = plt.subplots(figsize=(7, 4.2))
    for (name, t), c in zip(M.TARGETS, C):
        ax.plot(rho, [100 * M.subordination(0.05, r, 0.20, t) for r in rho], color=c,
                label=f"{name} (senior 10-yr PD {t:.1%})")
        ax.plot(rho, [100 * M.subordination(0.05, r, 0.40, t) for r in rho], color=c, ls="--", lw=1)
    ax.axhline(100 * 0.05 * 0.20, color="black", lw=0.8, ls=":")
    ax.text(0.30, 1.3, "expected pool loss (1%)", fontsize=8)
    ax.set_xlabel("Default correlation between plants, ρ")
    ax.set_ylabel("Subordination needed, % of pool")
    ax.set_xlim(0, 0.40); ax.set_ylim(0, 25)
    ax.legend(fontsize=8, frameon=False, loc="upper left")
    ax.text(0.22, 21.5, "dashed: recovery 60% instead of 80%", fontsize=8)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(path, dpi=200); plt.close(fig)


def fig_lcoe(path):
    w = M.structure_wacc(*M.capital_structure()[:2], M.R_E, M.R_M, M.R_S)
    cases = [("Single-stage\n12%", M.lcoe_staged(0.12, 0.12)),
             ("Single-stage\n10%", M.lcoe_staged(0.10, 0.10)),
             ("Two-stage,\nproject bond 8%", M.lcoe_staged(0.12, 0.08)),
             (f"Two-stage,\npooled {100*w:.1f}%", M.lcoe_staged(0.12, w))]
    fig, ax = plt.subplots(figsize=(7, 3.8))
    bars = ax.bar([c[0] for c in cases], [c[1] for c in cases], color=[C[3], C[3], C[1], C[0]])
    for b, (_, v) in zip(bars, cases):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.08, f"{v:.2f}", ha="center", fontsize=9)
    ax.set_ylabel("LCOE, US cents per kWh")
    ax.set_ylim(0, 8)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(path, dpi=200); plt.close(fig)


def fig_countries(path):
    ns = [1, 2, 3, 5, 10, 20]
    ks = [100 * M.mc_subordination(0.05, 0.10, 0.15, 0.20, 0.001, n, sims=300_000) for n in ns]
    fig, ax = plt.subplots(figsize=(7, 3.8))
    ax.plot(ns, ks, marker="o", color=C[0], label="pool spread over N host countries")
    lim = 100 * M.subordination(0.05, 0.10, 0.20, 0.001)
    ax.axhline(lim, color=C[1], ls="--", label="limit: global factor only (ρ = 0.10)")
    ax.set_xscale("log"); ax.set_xticks(ns); ax.set_xticklabels(ns)
    ax.set_xlabel("Number of host countries in the pool, N")
    ax.set_ylabel("Subordination for senior\n10-yr PD of 0.1%, % of pool")
    ax.set_ylim(0, 11)
    ax.legend(fontsize=8, frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); fig.savefig(path, dpi=200); plt.close(fig)


if __name__ == "__main__":
    fig_subordination(os.path.join(OUT, "fig1-subordination.png"))
    fig_lcoe(os.path.join(OUT, "fig2-lcoe-two-stage.png"))
    fig_countries(os.path.join(OUT, "fig3-host-countries.png"))
    print("written to", OUT)
