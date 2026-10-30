"""Figure for Climate Fiscal Policy Brief No. 2.1. Run: python3 make_figures.py
Uses the model in ../../2.Source/model.py."""
import sys
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "2.Source"))
import model as M  # noqa: E402

BLUE, ORANGE, INK, INK2 = "#2a78d6", "#eb6834", "#0b0b0b", "#52514e"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.grid": True, "grid.color": "#e6e5e0", "grid.linewidth": 0.6,
                     "xtick.color": INK2, "ytick.color": INK2, "figure.dpi": 150,
                     "savefig.bbox": "tight"})

rs = [0.04, 0.05, 0.06, 0.08, 0.10, 0.12, 0.15]
fig, ax = plt.subplots(figsize=(6.4, 3.4))
cap = [M.lcoe(r) * (M.CAPEX_PER_KW / M.LIFE) / (M.CAPEX_PER_KW * M.crf(r) + M.OM_PER_KW_YR) for r in rs]
om = [M.lcoe(r) * M.OM_PER_KW_YR / (M.CAPEX_PER_KW * M.crf(r) + M.OM_PER_KW_YR) for r in rs]
fin = [M.lcoe(r) - c - o for r, c, o in zip(rs, cap, om)]
x = range(len(rs))
ax.bar(x, [c + o for c, o in zip(cap, om)], color="#9ec5f4", width=0.6, label="Hardware and operation")
ax.bar(x, fin, bottom=[c + o for c, o in zip(cap, om)], color=BLUE, width=0.6, label="Return on capital")
for i, r in enumerate(rs):
    ax.text(i, M.lcoe(r) + 0.1, f"{M.lcoe(r):.1f}¢", ha="center", fontsize=9, color=INK)
ax.set_xticks(list(x), [f"{r:.0%}" for r in rs])
ax.set_xlabel("Cost of capital (WACC, real)")
ax.set_ylabel("US cents per kWh")
ax.legend(frameon=False, fontsize=8.5, loc="upper left")
ax.grid(axis="x", visible=False)
fig.savefig(HERE / "fig1-lcoe-by-wacc.png")
print("written fig1-lcoe-by-wacc.png")
