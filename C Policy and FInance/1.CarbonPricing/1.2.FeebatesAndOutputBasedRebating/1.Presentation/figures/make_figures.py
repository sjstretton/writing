"""Figures for Climate Fiscal Policy Brief No. 1.2 (v1.1).

The brief uses the working paper's calibrated figure, so that one set of numbers runs through both forms and the
deck. This script regenerates the working paper's figures from ../../2.Source/make_wp_figures.py (2024 Ember
generation mixes for India, Indonesia and South Africa; IPCC 2006 emission factors; stylized costs) and copies the
one the brief uses into this folder. Run from any directory:  python3 make_figures.py

The previous stylized figure (fig1-power-tax-vs-feebate.png, brief v1.0) is in ../../8.PreviousVersions.
"""
import shutil
import subprocess
import sys
from pathlib import Path

here = Path(__file__).resolve().parent
src = here.parents[1] / "2.Source"
subprocess.run([sys.executable, "make_wp_figures.py"], cwd=src, check=True, stdout=subprocess.DEVNULL)
for fig in ("fig3_price_effects.png",):
    shutil.copy2(src / "figures" / fig, here / fig)
    print("copied", fig)
