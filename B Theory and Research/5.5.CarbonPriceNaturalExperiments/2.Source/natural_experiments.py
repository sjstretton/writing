"""Paper 5.5: "Carbon Prices Cut Emissions: Evidence from Ten Natural Experiments".

Run from this folder:  python3 natural_experiments.py

1. Holds, in one place, the carbon price (or carbon-price equivalent) and the ex post
   emission or fuel-use effect for each case, as reported in the paper. Every number
   comes from the research notes in ../5.Notes/research/ (sources named there and in
   CarbonPriceNaturalExperiments.bib); US$ conversions use annual-average exchange rates
   (FRED H.10 series AEXSDUS, AEXUSEU, AEXCAUS, AEXUSUK) unless the note says otherwise.
2. Computes a common yardstick: the effect per US$10 per tonne of CO2, a rough
   semi-elasticity, with the horizon stated. Writes table_per10.csv.
3. Draws Figure 1 (effect against price, log price axis): figures/fig1_effect_vs_price.png, and copies it
   to ../1.Presentation/figures/ for the policy brief.

The yardstick is the author's arithmetic, not a published estimate: percent effect
divided by the price in US$/t, times 10. It ignores differences in horizon, coverage,
baseline and design, which the paper discusses.
"""
import csv
import shutil
from pathlib import Path

HERE = Path(__file__).parent
FIG = HERE / "figures"
FIG.mkdir(exist_ok=True)

# Sector groups (three categorical slots of the reference palette, validated all-pairs;
# marker shape is the secondary encoding).
GROUPS = {
    "Road transport": {"color": "#2a78d6", "marker": "o"},
    "Buildings": {"color": "#eb6834", "marker": "s"},
    "Power and industry": {"color": "#1baf7a", "marker": "^"},
}

# label, group, price (US$/t, central), price range, effect % (central), effect range,
# horizon, what the effect measures, source key
CASES = [
    ("US state gasoline taxes", "Road transport", 11.25, None, 1.43, (1.15, 1.43),
     "1 year", "gasoline use", "DavisKilian2011; Coglianese2017"),
    ("BC gasoline (households)", "Road transport", 22.0, None, 8.0, (5.0, 8.0),
     "2-4 years", "household gasoline use", "LawleyThivierge2018"),
    ("BC transport CO2", "Road transport", 30.0, None, 5.0, (5.0, 19.0),
     "short run (to long run)", "transport CO2", "Pretis2022"),
    ("Germany eco-tax", "Road transport", 81.0, None, 13.75, (11.5, 16.0),
     "6 years (2005)", "transport CO2", "RunstHohle2022"),
    ("Sweden carbon tax", "Road transport", 122.0, None, 9.4, (6.3, 9.4),
     "14 years (2005)", "transport CO2, tax alone", "Andersson2019"),
    ("Indonesia fuel reform", "Road transport", 143.0, (64.0, 143.0), 10.0, None,
     "2 years", "toll-road traffic", "Burke2017"),
    ("BC natural gas (homes)", "Buildings", 30.0, None, 7.0, None,
     "6 years", "residential gas use", "XiangLawley2019"),
    ("Switzerland 2015", "Buildings", 62.0, None, 6.95, (4.3, 9.6),
     "8 years", "heating-fuel CO2", "FOEN 2018 (Ecoplan)"),
    ("Swiss house owners", "Buildings", 85.0, None, 14.0, (12.0, 14.0),
     "9 years", "heating-fuel use", "Francescutto and Mathys 2022"),
    ("Sweden heating", "Buildings", 124.0, None, 11.0, (11.0, 46.0),
     "1-6 years after 2004", "residential CO2 (derived share)", "RunstThonipara2020"),
    ("Germany 2022 gas, homes", "Buildings", 430.0, (160.0, 475.0), 21.0, (21.0, 28.0),
     "months", "small-consumer gas use", "Ruhnau2023"),
    ("EU ETS phase II", "Power and industry", 19.0, None, 15.0, (8.1, 16.3),
     "1-5 years", "installation CO2", "Dechezleprêtre et al. 2023; Colmer et al. 2025; Bayer and Aklin 2020"),
    ("UK carbon price floor", "Power and industry", 26.0, None, 23.0, (6.2, 26.0),
     "1-5 years", "power-sector CO2", "Leroutier2022; Abrell2022; Gugler2023"),
    ("Germany 2022 gas, industry", "Power and industry", 790.0, (155.0, 970.0), 27.0, (23.0, 27.0),
     "months", "industrial gas use", "Ruhnau2023"),
]


def per10(effect, price):
    return 10.0 * effect / price


def write_table():
    rows = []
    for (label, group, price, prange, eff, erange, horizon, measure, src) in CASES:
        lo, hi = (erange if erange else (eff, eff))
        plo, phi = (prange if prange else (price, price))
        rows.append({
            "case": label, "group": group,
            "price_usd_t": price, "price_range": f"{plo:g}-{phi:g}",
            "effect_pct": eff, "effect_range": f"{lo:g}-{hi:g}",
            "per_usd10_central": round(per10(eff, price), 2),
            "per_usd10_range": f"{per10(lo, phi):.1f}-{per10(hi, plo):.1f}",
            "horizon": horizon, "measure": measure, "source": src,
        })
    with open(HERE / "table_per10.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    for r in rows:
        print(f"{r['case']:28s} {r['price_usd_t']:7.1f} US$/t  {r['effect_pct']:5.1f}%  "
              f"per US$10: {r['per_usd10_central']:5.2f} (range {r['per_usd10_range']})  [{r['horizon']}]")


# Label positions in data coordinates (x, y, alignment), set by eye to avoid collisions.
LABELS = {
    "US state gasoline taxes": (12.6, 1.5, "left"),
    "BC gasoline (households)": (20.5, 4.2, "right"),
    "BC transport CO2": (31.5, 3.0, "left"),
    "Germany eco-tax": (76, 13.8, "right"),
    "Sweden carbon tax": (130, 7.4, "left"),
    "Indonesia fuel reform": (158, 10.0, "left"),
    "BC natural gas (homes)": (32.5, 7.7, "left"),
    "Switzerland 2015": (66, 4.4, "left"),
    "Swiss house owners": (86, 17.4, "center"),
    "Sweden heating": (131, 12.6, "left"),
    "Germany 2022 gas, homes": (290, 19.5, "center"),
    "EU ETS phase II": (17.6, 15.0, "right"),
    "UK carbon price floor": (27.8, 23.6, "left"),
    "Germany 2022 gas, industry": (560, 29.4, "center"),
}
SHORT = {"BC natural gas (homes)": "BC gas (homes)"}
YMAX = 36


def draw_figure():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    ink, muted, grid, surface = "#0b0b0b", "#52514e", "#e4e3df", "#ffffff"
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9})
    fig, ax = plt.subplots(figsize=(7.2, 4.8), dpi=200)
    fig.patch.set_facecolor(surface)
    ax.set_facecolor(surface)

    # Reference curves: constant effect per US$10/t (1 and 10 percent).
    xs = np.logspace(np.log10(5), np.log10(1000), 200)
    for k, txt in ((1.0, "1% per US\\$10/t"), (10.0, "10% per US\\$10/t")):
        ys = k * xs / 10.0
        m = ys <= YMAX
        ax.plot(xs[m], ys[m], color="#b9b8b2", lw=1.0, zorder=1)
        lx, ly = (370, 33.2) if k == 1.0 else (37, 33.2)
        ax.text(lx, ly, txt, color=muted, fontsize=7.5, ha="left", va="center")

    for (label, group, price, prange, eff, erange, horizon, measure, src) in CASES:
        g = GROUPS[group]
        if erange:
            lo, hi = erange
            if hi > YMAX:  # clip and mark the top of a range that runs off the chart
                ax.plot([price, price], [lo, YMAX - 0.8], color=g["color"], lw=2.0, solid_capstyle="round", zorder=2)
                ax.scatter([price], [YMAX - 0.8], marker="^", s=30, color=g["color"], zorder=3)
                ax.annotate(f"to {hi:g}", (price, YMAX - 0.8), xytext=(5, -2), textcoords="offset points",
                            fontsize=7, color=muted, va="center")
            else:
                ax.plot([price, price], erange, color=g["color"], lw=2.0, solid_capstyle="round", zorder=2)
        if prange:
            ax.plot(prange, [eff, eff], color=g["color"], lw=2.0, solid_capstyle="round", zorder=2)
        ax.scatter([price], [eff], s=46, marker=g["marker"], color=g["color"],
                   edgecolors=surface, linewidths=1.6, zorder=3)
        lx, ly, ha = LABELS[label]
        ax.text(lx, ly, SHORT.get(label, label), ha=ha, va="center", fontsize=7.5, color=ink, zorder=4)

    ax.set_xscale("log")
    ax.set_xlim(5, 1200)
    ax.set_ylim(0, YMAX)
    ax.set_xticks([5, 10, 20, 50, 100, 200, 500, 1000])
    ax.set_xticklabels(["5", "10", "20", "50", "100", "200", "500", "1,000"])
    ax.set_xlabel("Carbon price or carbon-price equivalent (US\\$ per tonne of CO$_2$, log scale)", color=muted)
    ax.set_ylabel("Ex post cut in emissions or fuel use (%)", color=muted)
    ax.grid(True, which="major", axis="both", color=grid, lw=0.8)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color("#b9b8b2")
    ax.tick_params(colors=muted, length=0)

    handles = [plt.Line2D([], [], marker=v["marker"], color=v["color"], lw=0, markersize=7, label=k)
               for k, v in GROUPS.items()]
    ax.legend(handles=handles, loc="upper left", frameon=False, fontsize=8, labelcolor=ink)
    fig.tight_layout()
    out = FIG / "fig1_effect_vs_price.png"
    fig.savefig(out, facecolor=surface)
    print("wrote", out)
    brief_fig = HERE.parent / "1.Presentation" / "figures"   # the policy brief uses the same figure
    brief_fig.mkdir(parents=True, exist_ok=True)
    shutil.copy2(out, brief_fig / out.name)
    print("copied to", brief_fig / out.name)


if __name__ == "__main__":
    write_table()
    draw_figure()
