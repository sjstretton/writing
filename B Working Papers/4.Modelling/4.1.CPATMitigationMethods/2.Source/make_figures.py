"""Figures for paper 4.1. Run: python3 make_figures.py (writes figures/*.png)."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from worked_examples import TECH, costs, logit_shares, velocity_shares

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figures")
os.makedirs(OUT, exist_ok=True)
INK, MUTED, GRID = "#1f1f1e", "#6b6a63", "#d9d8d2"
SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"]  # fixed order
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "text.color": INK,
                     "axes.edgecolor": MUTED, "axes.labelcolor": INK,
                     "xtick.color": MUTED, "ytick.color": MUTED})


def flow_figure():
    fig, ax = plt.subplots(figsize=(7.2, 3.9))
    ax.set_xlim(0, 101); ax.set_ylim(4, 60); ax.axis("off")
    W, H = 18, 17
    X = [1, 28, 55, 82]
    TOP, BOT = 40, 9

    def box(x, y, title, body, fill="#eef4fc"):
        ax.add_patch(FancyBboxPatch((x, y), W, H, boxstyle="round,pad=0.3,rounding_size=1.0",
                                    fc=fill, ec=MUTED, lw=0.8))
        ax.text(x + W / 2, y + H - 1.8, title, ha="center", va="top", weight="bold", fontsize=8.3)
        ax.text(x + W / 2, y + H - 5.6, body, ha="center", va="top", fontsize=6.4, color=MUTED,
                linespacing=1.3)

    def arrow(x0, y0, x1, y1, dashed=False):
        ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                    arrowprops=dict(arrowstyle="-|>", color=INK if not dashed else MUTED, lw=0.9,
                                    linestyle="--" if dashed else "-", shrinkA=0, shrinkB=0))

    def label(x, y, s, ha="left"):
        ax.text(x, y, s, fontsize=6.7, color=MUTED, ha=ha, va="center")

    grey = "#f3f2ee"
    box(X[0], TOP, "Inputs", "energy balances\nIMF price data\nGDP, population\nworld fuel prices\npolicy settings", grey)
    box(X[1], TOP, "1. Prices", "supply cost\n+ existing taxes\n- subsidies\n+ carbon charge\n(+ VAT)")
    box(X[2], TOP, "2. Fuel demand", "income, usage and\nefficiency elasticities;\nefficiency trend;\nleakage to biomass")
    box(X[3], TOP, "4. Emissions", "fuel use x emission\nfactor, calibrated\nto inventory;\nother gases by driver")
    box(X[0], BOT, "6. GDP", "change in revenue\nx fiscal multipliers\nby lag", grey)
    box(X[1], BOT, "5. Revenues", "fuel use x tax rates;\nVAT; subsidies;\nauctioned ETS share")
    box(X[2], BOT, "3. Power", "electricity demand;\ndispatch; retirement;\ninvestment; storage;\ntariffs")
    box(X[3], BOT, "Outputs", "fuel use, prices,\nCO2 and GHGs,\nrevenue, generation,\nwelfare, GDP", grey)
    ym = TOP + H / 2
    arrow(X[0] + W + 0.5, ym, X[1] - 0.5, ym)
    arrow(X[1] + W + 0.5, ym, X[2] - 0.5, ym)
    arrow(X[2] + W + 0.5, ym, X[3] - 0.5, ym)
    yb = BOT + H / 2
    arrow(X[2] - 0.5, yb, X[1] + W + 0.5, yb)          # power -> revenues
    arrow(X[1] - 0.5, yb, X[0] + W + 0.5, yb)          # revenues -> GDP
    arrow(X[2] + W + 0.5, yb, X[3] - 0.5, yb)          # power -> outputs
    arrow(X[1] + W / 2, TOP - 0.5, X[1] + W / 2, BOT + H + 0.5)   # prices -> revenues
    label(X[1] + W / 2 + 1, 30.5, "tax rates")
    arrow(X[2] + W / 2, TOP - 0.5, X[2] + W / 2, BOT + H + 0.5)   # demand -> power
    label(X[2] + W / 2 + 1, 30.5, "electricity\ndemand")
    arrow(X[3] + W / 2, TOP - 0.5, X[3] + W / 2, BOT + H + 0.5)   # emissions -> outputs
    arrow(X[2] + W + 0.5, BOT + H - 1, X[3] - 0.5, TOP + 1)       # power fuel -> emissions
    label(X[2] + W + 1.5, 23.5 + 9, "power\nfuel use")
    arrow(X[0] + W / 2, BOT + H + 0.5, X[0] + W / 2, TOP - 0.5, dashed=True)  # GDP -> next year
    label(X[0] + W / 2 + 1, 30.5, "GDP,\nnext year")
    fig.savefig(os.path.join(OUT, "fig1_flow.png"), dpi=220, bbox_inches="tight")
    plt.close(fig)


def allocation_figure():
    cps = [x * 2.5 for x in range(0, 61)]
    lg = [logit_shares(costs(cp)) for cp in cps]
    vl = [velocity_shares(costs(cp)) for cp in cps]
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.0), sharey=True)
    for ax, data, title in [(axes[0], lg, "CPAT logit rule (K = 2)"),
                            (axes[1], vl, "Velocity penalty (λ = 100 USD/MWh)")]:
        for j, t in enumerate(TECH):
            ys = [100 * d[j] for d in data]
            ax.plot(cps, ys, color=SERIES[j], lw=2, label=t)
            if ys[-1] > 3:
                ax.text(cps[-1] + 2, ys[-1], t, color=INK, fontsize=7, va="center")
        ax.set_title(title, fontsize=8.5, loc="left")
        ax.set_xlabel("Carbon price (USD/tCO2)")
        ax.grid(axis="y", color=GRID, lw=0.6)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_xlim(0, 175)
    axes[0].set_ylabel("Share of new investment (%)")
    axes[0].legend(frameon=False, fontsize=7, loc="upper left", ncol=1)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig2_allocation.png"), dpi=220, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    flow_figure()
    allocation_figure()
    print("figures written to", OUT)
