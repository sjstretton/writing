"""Figures for Climate Fiscal Policy Brief No. 1.1 (v1.1).

The brief uses the working paper's calibrated figures, so that one set of numbers runs through both forms.
This script regenerates them from the working paper's scripts in ../../2.Source and copies the ones the brief
uses into this folder. Run from this folder.
"""
import shutil
import subprocess
import sys
from pathlib import Path

src = Path(__file__).resolve().parents[2] / "2.Source"
for script in ("make_fig1_incidence.py", "simulate_steel.py", "make_fig3_crediting.py"):
    subprocess.run([sys.executable, script], cwd=src, check=True)
for fig in ("fig1_incidence_by_regime.png",):
    shutil.copy2(src / "figures" / fig, Path(__file__).parent / fig)
    print("copied", fig)
