"""Working-paper figures for the Climate Investment Trust. Run from anywhere:
python3 make_wp_figures.py  -> writes figures/fig1..fig3 PNGs beside this file."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from model import (BASE, CASES, buffer_ratio_mc, buffer_ratio_large, incentive_per_donor_dollar,
                   capital_path)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figures")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
COL = ["#1f5f8b", "#d1782a", "#4a8c3f", "#8b2f5c"]
P = BASE
lam = P["p"] * P["L"]
b0 = buffer_ratio_mc(P["n"], P["p"], P["rho"], P["L"], P["alpha"])

# Figure 1: buffer needed vs correlation, three loss cases
rhos = np.linspace(0.05, 0.40, 15)
fig, ax = plt.subplots(figsize=(6.2, 3.8))
labs = {"base (MDB record)": "Base: MDB record (0.77% calls, 4.9% loss)",
        "middle (3% x 10%)": "Middle: 3% calls, 10% loss",
        "stress (3% x 37%)": "Stress: 3% calls, 37% loss"}
for (name, (p, L)), col in zip(CASES.items(), COL):
    ax.plot(rhos, [100 * buffer_ratio_mc(20, p, r, L, 0.01, sims=200_000) for r in rhos],
            color=col, lw=2, label=labs[name] + ", 20 programs")
    ax.plot(rhos, [100 * buffer_ratio_large(p, r, L, 0.01) for r in rhos], color=col,
            ls="--", lw=1.0)
ax.plot([], [], color="grey", ls="--", lw=1.0, label="Many small programs (equation 1)")
ax.set_xlabel("Correlation of guarantee calls (one-factor asset correlation)")
ax.set_ylabel("Buffer, % of guarantee exposure")
ax.set_title("On the MDB record a buffer under 1% of exposure suffices; the stress case needs 7-13%",
             fontsize=9, loc="left")
ax.legend(frameon=False, fontsize=7.5)
fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig1_buffer_ratio.png"), dpi=200); plt.close(fig)

# Figure 2: incentive per donor dollar vs expected loss rate (log scales)
lams = np.geomspace(0.0002, 0.02, 200)
fig, ax = plt.subplots(figsize=(6.2, 3.8))
for share, col, lab in ((0.0, COL[0], "no guarantee fee"), (0.5, COL[2], "fee = half of expected loss")):
    ax.plot(lams * 100, [incentive_per_donor_dollar(P["s"], x, share * x) for x in lams],
            color=col, lw=2, label=f"Buffer fund, {lab}")
ax.axhline(1, color="grey", lw=1.5, ls="--", label="Payout fund")
for i, (name, (p, L)) in enumerate(CASES.items()):
    bL = buffer_ratio_mc(20, p, 0.2, L, 0.01)
    ax.plot(p * L * 100, incentive_per_donor_dollar(P["s"], p * L, carry=0.02, b=bL), "o", color=COL[3],
            ms=5, label="Each case's own buffer, 2% carry" if i == 0 else None)
for (name, (p, L)), short in zip(CASES.items(), ("Base\n(MDB record)\n80", "Middle\n10", "Stress\n2.7")):
    ax.axvline(p * L * 100, color="grey", lw=0.8, ls=":")
    ax.text(p * L * 100 * 1.07, 0.35, short, fontsize=7.5, color="#444444", va="bottom")
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xticks([0.02, 0.05, 0.1, 0.3, 1, 2]); ax.set_xticklabels(["0.02", "0.05", "0.1", "0.3", "1", "2"])
ax.set_yticks([1, 3, 10, 30, 100]); ax.set_yticklabels(["1", "3", "10", "30", "100"])
ax.set_ylim(0.3, 400)
ax.set_xlabel("Trust's expected loss, % of exposure a year (log scale)")
ax.set_ylabel("Spread savings per donor dollar (PV, log)")
ax.set_title("Held capital delivers 2.7-80 times what spent capital does", fontsize=10, loc="left")
ax.legend(frameon=False, fontsize=8, loc="upper right")
fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig2_incentive_per_dollar.png"), dpi=200); plt.close(fig)

# Figure 3: capital paths with the stress-case buffer held (the launch policy recommended in the paper)
T = 25
b_st = buffer_ratio_mc(20, 0.03, 0.2, 0.37, 0.01)
lam_st = 0.03 * 0.37
fig, ax = plt.subplots(figsize=(6.2, 3.8))
scen = [("Losses at MDB record, $95bn private co-investment", 95, lam),
        ("Losses at MDB record, insurance only", 0, lam),
        ("Stress losses, $95bn private co-investment", 95, lam_st),
        ("Stress losses, insurance only", 0, lam_st)]
for (lab, E_p, l), col in zip(scen, COL):
    ax.plot(range(T + 1), capital_path(T=T, E_p=E_p, lam=l, f=0.0, b=b_st), color=col, lw=2, label=lab)
ax.set_xlabel("Years from launch"); ax.set_ylabel("Trust capital, $bn")
ax.set_title("With the stress buffer held, the loss record decides whether the Trust grows", fontsize=10, loc="left")
ax.legend(frameon=False, fontsize=8)
fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig3_capital_paths.png"), dpi=200); plt.close(fig)
print("written to", OUT)
