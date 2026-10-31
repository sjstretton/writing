"""Figures for Climate Fiscal Policy Brief No. 6.3 (v1.0) and its deck.

The brief and the deck use the working paper's figures, so that one set of numbers runs through all three.
This script reruns the working paper's scripts in ../../2.Source and copies the figures used here into this
folder. Run from this folder: python3 make_figures.py
"""
import shutil
import subprocess
import sys
from pathlib import Path

src = Path(__file__).resolve().parents[2] / "2.Source"
for script in ("investment_lenses.py", "sids_worked_example.py", "make_figures.py"):
    subprocess.run([sys.executable, script], cwd=src, check=True, stdout=subprocess.DEVNULL)
for fig in ("fig_breakeven.png", "fig_island.png", "fig_lenses.png"):
    shutil.copy2(src / "figures" / fig, Path(__file__).parent / fig)
    print("copied", fig)
