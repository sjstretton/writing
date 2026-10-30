"""Slide figure fig_countries.png: Sierra Leone and Liberia, two Level 1 measures from the
Excise-Fiscal Diagnostic (paper 5.1, Table 5). Illustrative results from the diagnostic, not
official estimates. Carbon component = 2.31 kg CO2 per liter of petrol x USD 50/t (paper Table 4)."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
BLUE, GREEN, GREY, INK = "#1F4E79", "#2E7D32", "#9AA59C", "#1B1B1B"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.spines.top": False,
    "axes.spines.right": False, "axes.edgecolor": "#6B7B6E", "axes.labelcolor": INK,
    "xtick.color": INK, "ytick.color": INK})
HERE = os.path.dirname(os.path.abspath(__file__))

panels = [
    ("Excise collected, % of GDP", ["Sierra Leone\n2024–25", "Liberia\nFY2024", "Africa\naverage"],
     [1.265, 0.37, 2.4], [BLUE, BLUE, GREY], ["1.25–1.28", "0.37", "2.4"]),
    ("Petrol, US$ per liter", ["Sierra Leone", "Liberia\n(levies)", "Carbon alone\nat $50/t", "OECD\naverage"],
     [0.23, 0.095, 0.116, 0.55], [BLUE, BLUE, GREEN, GREY], ["0.23", "0.095", "0.12", "0.55"]),
]
fig, axes = plt.subplots(1, 2, figsize=(10, 4.6))
for ax, (title, labels, vals, cols, txt) in zip(axes, panels):
    bars = ax.bar(range(len(vals)), vals, color=cols, width=0.62)
    for b, v, t in zip(bars, vals, txt):
        ax.text(b.get_x() + b.get_width() / 2, v + max(vals) * 0.02, t, ha="center", color=INK)
    ax.set_xticks(range(len(vals))); ax.set_xticklabels(labels, fontsize=10.5)
    ax.set_title(title, loc="left", fontsize=13, color=INK)
    ax.set_ylim(0, max(vals) * 1.18)
    ax.grid(axis="y", color="#E3E8E3"); ax.set_axisbelow(True)
fig.tight_layout(); fig.savefig(os.path.join(HERE, "fig_countries.png"), dpi=200)
