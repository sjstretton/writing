"""Figures for Climate Fiscal Policy Brief No. 1.4 (v1.1).

The brief uses the working paper's calibrated figure, so that one set of numbers runs through both forms.
This script regenerates the working paper's figures and tables from ../../2.Source/make_wp_figures.py and
copies the one the brief uses into this folder. Run from any folder:  python3 make_figures.py
"""
import shutil
import subprocess
import sys
from pathlib import Path

src = Path(__file__).resolve().parents[2] / "2.Source"
subprocess.run([sys.executable, "make_wp_figures.py"], cwd=src, check=True, stdout=subprocess.DEVNULL)
for fig in ("fig1_shuffling_model.png",):
    shutil.copy2(src / "figures" / fig, Path(__file__).parent / fig)
    print("copied", fig)
