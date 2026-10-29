"""Slide figure for the paper deck: fig_corrective.png (numbers as in the paper)."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
BLUE, GREEN, GREY, INK = "#1F4E79", "#2E7D32", "#9AA59C", "#1B1B1B"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "axes.spines.top": False,
    "axes.spines.right": False, "axes.edgecolor": "#6B7B6E", "axes.labelcolor": INK,
    "xtick.color": INK, "ytick.color": INK})
HERE = os.path.dirname(os.path.abspath(__file__))

# Country A (stylized): current excise against corrective rate, US$ per liter (paper Table 4)
import numpy as np
fuels = ["Petrol", "Diesel"]
cur = [0.30, 0.18]; cor = [0.31, 0.43]; lo = [0.13, 0.20]; hi = [0.68, 0.91]
x = np.arange(2); w = 0.36
fig, ax = plt.subplots(figsize=(10, 4.6))
b1 = ax.bar(x - w/2 - 0.01, cur, w, color=BLUE, label="Current excise")
b2 = ax.bar(x + w/2 + 0.01, cor, w, color=GREEN, label="Corrective rate (range: low to high case)")
ax.errorbar(x + w/2 + 0.01, cor, yerr=[np.array(cor)-lo, np.array(hi)-cor], fmt="none", ecolor=INK, capsize=6, lw=1.5)
for b in list(b1) + list(b2):
    ax.text(b.get_x() + 0.03, b.get_height() + 0.015, f"{b.get_height():.2f}", ha="left", color=INK)
ax.set_xticks(x); ax.set_xticklabels(fuels)
ax.set_ylabel("US$ per liter"); ax.set_ylim(0, 1.0)
ax.legend(frameon=False, loc="upper left")
ax.grid(axis="y", color="#E3E8E3"); ax.set_axisbelow(True)
fig.tight_layout(); fig.savefig(os.path.join(HERE, "fig_corrective.png"), dpi=200)
