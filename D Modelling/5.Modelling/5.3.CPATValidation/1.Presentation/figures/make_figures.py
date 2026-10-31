"""Figures for Climate Fiscal Policy Brief No. 5.3 (v1.0).

The brief uses the working paper's figures, so that one set of numbers runs through both forms. This script
regenerates them from the working paper's script in ../../2.Source and copies the ones the brief and the deck use
into this folder. Run from this folder.
"""
import shutil
import subprocess
import sys
from pathlib import Path

src = Path(__file__).resolve().parents[2] / "2.Source"
subprocess.run([sys.executable, "make_figures.py"], cwd=src, check=True)
for fig in ("fig1_backcast.png", "fig2_sensitivity.png"):
    shutil.copy2(src / "figures" / fig, Path(__file__).parent / fig)
    print("copied", fig)
