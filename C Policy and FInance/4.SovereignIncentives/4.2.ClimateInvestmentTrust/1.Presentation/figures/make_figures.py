"""Brief figure for Climate Fiscal Policy Brief No. 4.2. Uses the working-paper model in ../../2.Source.
python3 make_figures.py -> writes fig1-buffer-vs-payout.png beside this file."""
import os, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "2.Source"))
from model import BASE, buffer_ratio_mc, incentive_per_donor_dollar, capital_path

P = BASE
lam = P["p"] * P["L"]
b0 = buffer_ratio_mc(P["n"], P["p"], P["rho"], P["L"], P["alpha"])
plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False})
fig, (a1, a2) = plt.subplots(1, 2, figsize=(8, 3.4))
labels = ["Payout\nfund", "Buffer:\nstress", "Buffer:\nmiddle", "Buffer:\nMDB record"]
vals = [1.0, incentive_per_donor_dollar(P["s"], 0.03 * 0.37), incentive_per_donor_dollar(P["s"], 0.03 * 0.10),
        incentive_per_donor_dollar(P["s"], lam)]
bars = a1.bar(labels, vals, color=["#9a9a9a", "#7fa7c6", "#4f86b0", "#1f5f8b"])
for bar, v in zip(bars, vals):
    a1.text(bar.get_x() + bar.get_width() / 2, v * 1.12, f"{v:.0f}" if v >= 10 else f"{v:.1f}", ha="center")
a1.set_yscale("log"); a1.set_ylim(0.5, 200)
a1.set_yticks([1, 3, 10, 30, 100]); a1.set_yticklabels(["1", "3", "10", "30", "100"])
a1.set_ylabel("Spread savings per donor dollar (PV, log)")
a1.set_title("A. Holding beats spending", loc="left", fontsize=9)
for lab, E_p, f, col in (("$95bn private, fee = EL/2", 95, lam / 2, "#4a8c3f"),
                         ("$95bn private, no fee", 95, 0.0, "#1f5f8b"),
                         ("$10bn private, no fee", 10, 0.0, "#d1782a")):
    a2.plot(range(26), capital_path(T=25, E_p=E_p, lam=lam, f=f, b=b0), lw=2, color=col, label=lab)
a2.set_xlabel("Years from launch"); a2.set_ylabel("Trust capital, $bn")
a2.set_title("B. Growth needs fee income", loc="left", fontsize=9)
a2.legend(frameon=False, fontsize=7)
fig.tight_layout(); fig.savefig(os.path.join(HERE, "fig1-buffer-vs-payout.png"), dpi=200)
print("written")
