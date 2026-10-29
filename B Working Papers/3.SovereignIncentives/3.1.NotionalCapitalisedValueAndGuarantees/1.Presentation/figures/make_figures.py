"""Figure for Climate Fiscal Policy Brief No. 3.1. Run: python3 make_figures.py
Reuses the stylized model in ../../2.Source/model.py and writes the PNG beside this script.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "2.Source"))

import make_wp_figures as F  # noqa: E402

if __name__ == "__main__":
    F.fig_balance(HERE / "fig1-balance-paths.png")
    F.fig_ratio(HERE / "fig2-incentive-cost-ratio.png")
    print("written to", HERE)
