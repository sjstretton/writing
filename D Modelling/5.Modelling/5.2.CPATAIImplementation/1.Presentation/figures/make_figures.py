"""Figures for Climate Fiscal Policy Brief No. 5.2 and its deck (v1.0, 31 Oct 2026). Run from any folder.

fig_register.png  entries in the CPAT-AI register at release 1.0.2, legacy bugs split by priority
                  (working paper Table 1; tracker Tracking_Legacy_Bugs_v1.0.2.xlsx, counts recomputed 31 Oct 2026)
fig_growth.png    legacy bugs registered over October 2026 (task log excel_ai/core/CAVEATS.md; register 1.0.2, 1.1.0)
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE, GREEN, LEAF, GREY, INK = "#1F4E79", "#2E7D32", "#97BC62", "#9AA59C", "#1B1B1B"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.edgecolor": "#6B7B6E", "axes.labelcolor": INK,
                     "xtick.color": INK, "ytick.color": INK})
HERE = os.path.dirname(os.path.abspath(__file__))

# --- Register at release 1.0.2 (29 Oct 2026)
labels = ["Legacy bugs", "Issues", "Departures", "Prototype bugs", "Documentation bugs", "Upgrades"]
vals = [228, 135, 35, 22, 20, 14]
high, med, low = 24, 62, 142          # legacy bugs by priority
assert high + med + low == vals[0]
fig, ax = plt.subplots(figsize=(10, 4.6))
y = list(range(len(labels)))[::-1]
ax.barh(y[1:], vals[1:], color=BLUE, height=0.6)
ax.barh(y[0], high, color=GREEN, height=0.6, label="High priority")
ax.barh(y[0], med, left=high, color=LEAF, height=0.6, label="Medium")
ax.barh(y[0], low, left=high + med, color=GREY, height=0.6, label="Low (latent or reporting)")
for yi, v in zip(y, vals):
    ax.text(v + 3, yi, str(v), va="center", color=INK)
ax.text(high / 2, y[0], "24", va="center", ha="center", color="white", fontsize=11, fontweight="bold")
ax.text(high + med / 2, y[0], "62", va="center", ha="center", color=INK, fontsize=11)
ax.text(high + med + low / 2, y[0], "142", va="center", ha="center", color=INK, fontsize=11)
ax.set_yticks(y)
ax.set_yticklabels(labels)
ax.set_xlabel("Entries in the CPAT-AI register, release 1.0.2 (29 October 2026)")
ax.set_xlim(0, 255)
ax.grid(axis="x", color="#E3E8E3")
ax.set_axisbelow(True)
ax.legend(loc="lower right", frameon=False, fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig_register.png"), dpi=200)
plt.close(fig)

# --- Legacy bugs registered over time (October 2026)
dates = ["18 Oct\n(v0.4.12)", "20 Oct\n(v0.6.3)", "29 Oct\n(release 1.0.2)", "30 Oct\n(release 1.1.0)"]
count = [64, 159, 228, 231]
fig, ax = plt.subplots(figsize=(10, 4.6))
x = range(len(dates))
ax.bar(list(x), count, color=[BLUE, BLUE, GREEN, BLUE], width=0.55)
for xi, c in zip(x, count):
    ax.text(xi, c + 4, str(c), ha="center", color=INK, fontsize=13)
ax.set_xticks(list(x))
ax.set_xticklabels(dates)
ax.set_ylabel("Legacy bugs in the register")
ax.set_ylim(0, 260)
ax.grid(axis="y", color="#E3E8E3")
ax.set_axisbelow(True)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig_growth.png"), dpi=200)
plt.close(fig)
print("wrote fig_register.png, fig_growth.png")
