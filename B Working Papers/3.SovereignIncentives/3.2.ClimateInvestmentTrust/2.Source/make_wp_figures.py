"""Working-paper figures for the Climate Investment Trust. Run from anywhere:
python3 make_wp_figures.py  -> writes figures/fig1..fig3 PNGs beside this file."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from model import (BASE, buffer_ratio_mc, buffer_ratio_large, incentive_per_donor_dollar,
                   capital_path)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figures")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
COL = ["#1f5f8b", "#d1782a", "#4a8c3f", "#8b2f5c"]
P = BASE
lam = P["p"] * P["L"]
b0 = buffer_ratio_mc(P["n"], P["p"], P["rho"], P["L"], P["alpha"])

# Figure 1: buffer needed vs correlation
rhos = np.linspace(0.05, 0.40, 15)
fig, ax = plt.subplots(figsize=(6.2, 3.8))
for p, col in zip((0.01, 0.03, 0.05), COL):
    ax.plot(rhos, [100 * buffer_ratio_mc(20, p, r, P["L"], 0.01, sims=200_000) for r in rhos],
            color=col, lw=2, label=f"PD {p:.0%}, 20 countries")
ax.plot(rhos, [100 * buffer_ratio_large(0.03, r, P["L"], 0.01) for r in rhos], color=COL[1],
        ls="--", lw=1.5, label="PD 3%, many countries")
ax.set_xlabel("Correlation of guarantee calls (one-factor asset correlation)")
ax.set_ylabel("Buffer, % of guarantee exposure")
ax.set_title("Buffers of 4-17% of exposure keep the chance of exhaustion at 1% a year", fontsize=10, loc="left")
ax.legend(frameon=False, fontsize=8)
fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig1_buffer_ratio.png"), dpi=200); plt.close(fig)

# Figure 2: incentive per donor dollar vs loss given call
Ls = np.linspace(0.05, 0.6, 50)
fig, ax = plt.subplots(figsize=(6.2, 3.8))
for share, col, lab in ((0.0, COL[0], "no guarantee fee"), (0.5, COL[2], "fee = half of expected loss")):
    ax.plot(Ls, [incentive_per_donor_dollar(P["s"], P["p"] * L, share * P["p"] * L) for L in Ls],
            color=col, lw=2, label=f"Buffer fund, {lab}")
ax.axhline(1, color="grey", lw=1.5, ls="--", label="Payout fund")
ax.axvline(0.37, color="grey", lw=0.8, ls=":")
ax.text(0.375, 15, "average sovereign\nhaircut, 37%", fontsize=8, color="grey")
ax.set_ylim(0, 25)
ax.set_xlabel("Loss given call (share of a call the Trust never recovers)")
ax.set_ylabel("Spread savings per donor dollar (PV)")
ax.set_title("Held capital delivers 3-20 times what spent capital does", fontsize=10, loc="left")
ax.legend(frameon=False, fontsize=8)
fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig2_incentive_per_dollar.png"), dpi=200); plt.close(fig)

# Figure 3: capital paths
T = 25
fig, ax = plt.subplots(figsize=(6.2, 3.8))
scen = [("$95bn private co-investment, fee = half of expected loss", 95, lam / 2),
        ("$95bn private co-investment, no guarantee fee", 95, 0.0),
        ("$10bn private co-investment, no guarantee fee", 10, 0.0),
        ("Insurance only, fee = half of expected loss", 0, lam / 2)]
for (lab, E_p, f), col in zip(scen, COL):
    ax.plot(range(T + 1), capital_path(T=T, E_p=E_p, lam=lam, f=f, b=b0), color=col, lw=2, label=lab)
ax.set_xlabel("Years from launch"); ax.set_ylabel("Trust capital, $bn")
ax.set_title("Fees on private returns, not the buffer's yield, make the Trust grow", fontsize=10, loc="left")
ax.legend(frameon=False, fontsize=8)
fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig3_capital_paths.png"), dpi=200); plt.close(fig)
print("written to", OUT)
