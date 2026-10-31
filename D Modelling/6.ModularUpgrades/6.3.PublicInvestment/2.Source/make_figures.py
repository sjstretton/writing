"""Figures for working paper 6.3 (v0.2) and its brief. Run from this folder: python3 make_figures.py

fig_breakeven.png  Net saving per $1,000 of capital against the cost of capital (Proposition 1), with the
                   break-even rate and CPAT's optional income-group rates marked.
fig_island.png     Year-1 net cash to the budget and the liability each route creates, worked example (Table 2),
                   read from sids_worked_example_results.csv (run sids_worked_example.py first).
fig_lenses.png     Net benefit of one year's 2030 investment at market rates and at 6 percent (Table 1).
All numbers are recomputed here or read from the scripts' output; nothing is typed in by hand except Table 1's
inputs, which are the same as in investment_lenses.py.
"""
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / "figures"
OUT.mkdir(exist_ok=True)
BLUE, GREEN, GREY, INK, RED = "#1F4E79", "#2E7D32", "#9AA59C", "#1B1B1B", "#B23A3A"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.edgecolor": "#6B7B6E", "axes.labelcolor": INK,
                     "xtick.color": INK, "ytick.color": INK})


def crf(r, n=25):
    return r / (1 - (1 + r) ** -n)


B = 0.133

# --- Figure 1: break-even ------------------------------------------------------------
r = np.linspace(0.03, 0.18, 300)
net = 1000 * (B - crf(r))
lo, hi = 0.0001, 0.5
for _ in range(100):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if crf(mid) < B else (lo, mid)
rstar = mid
fig, ax = plt.subplots(figsize=(10, 4.6))
ax.axhline(0, color="#6B7B6E", lw=1)
ax.plot(100 * r, net, color=BLUE, lw=2.5)
ax.axvline(100 * rstar, color=RED, ls="--", lw=1.5)
ax.text(100 * rstar + 0.2, 60, f"break-even {100*rstar:.1f}%", color=RED)
ax.text(3.2, -40, "Dots: CPAT's optional income-group rates", color=GREEN, fontsize=11)
for lab, rr in [("HIC 7.5%", 0.075), ("UMIC 10%", 0.10), ("LMIC 12.5%", 0.125), ("LIC 15%", 0.15)]:
    y = 1000 * (B - crf(rr))
    ax.plot(100 * rr, y, "o", color=GREEN, ms=8)
    ax.annotate(f"{lab}: {y:+.0f}", (100 * rr, y), textcoords="offset points", xytext=(6, 8), color=INK, fontsize=11)
ax.set_xlabel("Cost of capital, percent a year")
ax.set_ylabel("Saving less capital charge,\nUS\\$ a year per US\\$1,000")
ax.grid(axis="y", color="#E3E8E3")
ax.set_axisbelow(True)
fig.tight_layout()
fig.savefig(OUT / "fig_breakeven.png", dpi=200)
plt.close(fig)
print("wrote fig_breakeven.png; r* =", round(100 * rstar, 2))

# --- Figure 2: island routes -----------------------------------------------------------
rows = {d["route"]: d for d in csv.DictReader(open(HERE / "sids_worked_example_results.csv"))}
routes = ["R1a", "R2", "R3", "R4"]
labels = ["Loan 8%,\n7 years", "Concessional\n1.5%, 30 years", "PPA,\nWACC 11%", "PPA, guaranteed,\nWACC 8.5%"]
cash = [float(rows[k]["net_cash_y1_musd"]) for k in routes]
gdp_m = 2000.0
liab = [float(rows[k]["headline_debt_added_pct_gdp"]) + float(rows[k]["ppa_pv8_pct_gdp"]) for k in routes]
is_ppa = [float(rows[k]["ppa_pv8_pct_gdp"]) > 0 for k in routes]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.6))
x = np.arange(len(routes))
b = a1.bar(x, cash, color=[RED if c < 0 else GREEN for c in cash], width=0.6)
a1.axhline(0, color="#6B7B6E", lw=1)
for i, c in enumerate(cash):
    a1.text(i, c + (0.6 if c >= 0 else -1.6), f"{c:+.1f}", ha="center", color=INK)
a1.set_xticks(x)
a1.set_xticklabels(labels, fontsize=10)
a1.set_ylabel("US\\$ million, year 1")
a1.set_title("Net cash to the budget", fontsize=12, color=INK)
a1.set_ylim(-18, 10)
b2 = a2.bar(x, liab, color=[BLUE if p else GREY for p in is_ppa], width=0.6)
for i, v in enumerate(liab):
    a2.text(i, v + 0.2, f"{v:.1f}", ha="center", color=INK)
a2.set_xticks(x)
a2.set_xticklabels(labels, fontsize=10)
a2.set_ylabel("Percent of GDP")
a2.set_title("Debt (grey) or PPA commitment at 8% (blue)", fontsize=12, color=INK)
a2.set_ylim(0, 11)
for a in (a1, a2):
    a.grid(axis="y", color="#E3E8E3")
    a.set_axisbelow(True)
fig.tight_layout()
fig.savefig(OUT / "fig_island.png", dpi=200)
plt.close(fig)
print("wrote fig_island.png", cash, liab)

# --- Figure 3: lenses (Table 1) ---------------------------------------------------------
groups = [("Advanced\neconomies", 2750, 0.055), ("China", 1350, 0.06), ("Developing,\nexcluding China", 2400, 0.105)]
mkt = [B * I - I * crf(rr) for _, I, rr in groups]
six = [B * I - I * crf(0.06) for _, I, rr in groups]
x = np.arange(len(groups))
w = 0.36
fig, ax = plt.subplots(figsize=(10, 4.6))
b1 = ax.bar(x - w / 2 - 0.01, mkt, w, color=BLUE, label="At market cost of capital")
b2 = ax.bar(x + w / 2 + 0.01, six, w, color=GREEN, label="At a 6% social rate")
for bars in (b1, b2):
    for bb in bars:
        ax.text(bb.get_x() + bb.get_width() / 2, bb.get_height() + 3, f"{bb.get_height():.0f}", ha="center", color=INK)
ax.set_xticks(x)
ax.set_xticklabels([g[0] for g in groups])
ax.set_ylabel("Savings less capital charge,\nUS\\$ billion a year")
ax.set_ylim(0, 185)
ax.legend(frameon=False, loc="upper right")
ax.grid(axis="y", color="#E3E8E3")
ax.set_axisbelow(True)
fig.tight_layout()
fig.savefig(OUT / "fig_lenses.png", dpi=200)
plt.close(fig)
print("wrote fig_lenses.png", [round(v) for v in mkt], [round(v) for v in six])
