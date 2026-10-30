"""Figure for the brief; reuses the working-paper model in ../../2.Source."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "2.Source"))
import make_wp_figures as F

if __name__ == "__main__":
    F.fig_subordination(os.path.join(HERE, "fig1-first-loss-vs-correlation.png"))
    F.fig_lcoe(os.path.join(HERE, "fig2-lcoe-two-stage.png"))
    print("written to", HERE)
