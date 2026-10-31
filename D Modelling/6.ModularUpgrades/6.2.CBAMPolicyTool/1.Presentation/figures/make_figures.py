"""Figures for Climate Fiscal Policy Brief No. 6.2 (v1.0) and its deck.

One set of numbers runs through the working paper, the brief and the deck. This script reruns the working
paper's scripts in ../../2.Source (cbam_example.py, egypt_example.py), copies the charge-path figure, and draws
the Egypt chart from table_egypt.csv. Run from any folder:  python3 make_figures.py
"""
import csv
import shutil
import subprocess
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
SRC = HERE.parents[1] / "2.Source"
for script in ("cbam_example.py", "egypt_example.py"):
    subprocess.run([sys.executable, script], cwd=SRC, check=True, stdout=subprocess.DEVNULL)
shutil.copy2(SRC / "figures" / "fig1_charge_path.png", HERE / "fig1_charge_path.png")
print("copied fig1_charge_path.png")

rows = list(csv.DictReader(open(SRC / "table_egypt.csv")))
rows.sort(key=lambda r: float(r["charge_default_eur_m"]))
names = [r["product"] for r in rows]
dflt = [float(r["charge_default_eur_m"]) for r in rows]
best = [float(r["charge_best_eur_m"]) for r in rows]
fig, ax = plt.subplots(figsize=(7.0, 3.6), dpi=200)
y = range(len(rows))
ax.barh([i + 0.2 for i in y], dflt, height=0.38, color="#2a78d6", label="Declared at the EU default value")
ax.barh([i - 0.2 for i in y], best, height=0.38, color="#1baf7a", label="With verified data where it pays (tool estimate)")
for i, (d, b) in enumerate(zip(dflt, best)):
    ax.text(d + 4, i + 0.2, f"{d:.0f}", va="center", fontsize=7.5, color="#0b0b0b")
    ax.text(b + 4, i - 0.2, f"{b:.0f}", va="center", fontsize=7.5, color="#0b0b0b")
ax.set_yticks(list(y))
ax.set_yticklabels(names, fontsize=8)
ax.set_xlabel("EUR million a year, full phase-in, EUR 80/tCO2, 2025 volumes", fontsize=8)
ax.set_xlim(0, 420)
ax.grid(axis="x", color="#e4e3df", lw=0.8)
ax.set_axisbelow(True)
for sp in ("top", "right"):
    ax.spines[sp].set_visible(False)
ax.tick_params(colors="#52514e", labelsize=8)
ax.legend(fontsize=7.5, frameon=False, loc="lower right")
fig.tight_layout()
fig.savefig(HERE / "fig2_egypt_charges.png")
print("drew fig2_egypt_charges.png")
