"""Figures for Climate Fiscal Policy Brief No. 1.3 (v1.1).

The brief uses the working paper's figures, so that one set of numbers runs through both forms.
This script regenerates them from the working paper's script in ../../2.Source (which also prints
every fiscal number the brief and the deck use) and copies the ones the brief and deck use into
this folder. Run from any directory:  python3 make_figures.py
"""
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
src = HERE.parents[1] / "2.Source"
subprocess.run([sys.executable, "make_wp_figures.py"], cwd=src, check=True)
for fig in ("fig2-neutrality-rule.png", "fig4-vat-chain.png"):
    shutil.copy2(src / "figures" / fig, HERE / fig)
    print("copied", fig)
