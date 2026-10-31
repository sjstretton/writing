"""Figures for Climate Fiscal Policy Brief No. 5.4 (v1.0).

The brief uses the working paper's figures, so that one set of numbers runs through both forms.
This script regenerates them from the working paper's script in ../../2.Source and copies the one the
brief uses into this folder. Run from this folder:  python3 make_figures.py
"""
import shutil
import subprocess
import sys
from pathlib import Path

src = Path(__file__).resolve().parents[2] / "2.Source"
subprocess.run([sys.executable, "elasticity_check.py"], cwd=src, check=True, stdout=subprocess.DEVNULL)
for fig in ("fig2_timing.png", "fig1_cpat_vs_literature.png"):
    shutil.copy2(src / "figures" / fig, Path(__file__).parent / fig)
    print("copied", fig)
