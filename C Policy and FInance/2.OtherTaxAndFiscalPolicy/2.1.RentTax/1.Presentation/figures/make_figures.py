"""Figures for Climate Fiscal Policy Brief No. 2.1 (v1.0).

The brief uses the working paper's figure, so that one set of numbers runs through both forms.
This script regenerates it from the working paper's script in ../../2.Source and copies it here.
Run from any folder: python3 make_figures.py
"""
import shutil
import subprocess
import sys
from pathlib import Path

src = Path(__file__).resolve().parents[2] / "2.Source"
subprocess.run([sys.executable, "rent_tax_calcs.py"], cwd=src, check=True)
for fig in ("fig1_effective_rates.png",):
    shutil.copy2(src / "figures" / fig, Path(__file__).parent / fig)
    print("copied", fig)
