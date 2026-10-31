"""Figure for Brief 4.3. Reuses the working paper's model. Run: python3 make_figures.py"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "2.Source"))
import make_wp_figures as w  # noqa: E402

if __name__ == "__main__":
    w.fig_size(os.path.join(HERE, "fig1-size-problem.png"))
    print("written fig1-size-problem.png")
