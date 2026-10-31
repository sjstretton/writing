"""Figures and fiscal tables for working paper 1.3 (Converting a VAT into a Destination Carbon Tax).

Reads the CSV outputs of calibrate_defaults.py and distribution.py (run those
first), prints every number used in the paper's fiscal tables, and writes:

  figures/fig1-default-intensities.png   default intensities by product category
  figures/fig2-neutrality-rule.png       value component and total rates under the neutrality rule
  figures/fig3-distribution.png          incidence by income quintile and by member state
  figures/fig4-vat-chain.png             the three-stage worked example

Run from any directory:  python3 make_wp_figures.py
Units: intensity e in kg CO2e per euro; price P in EUR/tCO2e; P*e/10 = percentage points.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
FIG = HERE / "figures"
FIG.mkdir(exist_ok=True)
YEARS = np.arange(2027, 2038)

# reference palette (light): categorical slots 1-3, ink, muted, grid
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, MUTED, GRID = "#0b0b0b", "#52514e", "#e4e3df"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9,
                     "axes.edgecolor": MUTED, "axes.labelcolor": INK,
                     "xtick.color": MUTED, "ytick.color": MUTED})

cats = pd.read_csv(HERE / "defaults_by_category.csv")
# Like-for-like import comparison: EU-made intensity at the mix of products imported from outside the EU.
_t = cats[cats.vat == "taxable"]
_w = _t.hh_spend_beur * _t.import_share
print(f"Extra-EU imports {(_w * _t.ghg_extra_eu).sum() / _w.sum():.3f} kg/EUR; EU-made at the same mix "
      f"{(_w * _t.ghg_eu).sum() / _w.sum():.3f} kg/EUR; ratio "
      f"{(_w * _t.ghg_extra_eu).sum() / (_w * _t.ghg_eu).sum():.2f}")
# What a default schedule at the EU-made average would charge on the whole taxable basket, against its embodied carbon.
print(f"Taxable basket at EU-made defaults {(_t.hh_spend_beur * _t.ghg_eu).sum() / _t.hh_spend_beur.sum():.3f} kg/EUR; "
      f"embodied (all origins) {(_t.hh_spend_beur * _t.ghg_all).sum() / _t.hh_spend_beur.sum():.3f} kg/EUR")
basket = pd.read_csv(HERE / "basket_summary.csv")
sources = pd.read_csv(HERE / "footprint_sources.csv")

E2022 = float(basket.query("gas == 'ghg' and basket == 'household basket, VAT-taxable products'").kg_per_eur.iloc[0])
BASE = float(basket.query("gas == 'ghg' and basket == 'household basket, VAT-taxable products'").spend_beur.iloc[0])
S_ETS = float(sources.query("gas == 'ghg'").iloc[0].share)
Q_ETS = 80.0      # stylized ETS price, EUR/t, held constant
V0 = 15.0


def price(year):
    return 20.0 * (year - 2027)


def receipts_pp(P, e, s=S_ETS, q=Q_ETS):
    """Net carbon-component receipts, pp of the taxable base, after deducting ETS prices."""
    return (P * e * (1 - s) + max(P - q, 0.0) * e * s) / 10.0


def path(g):
    """Intensity falling g a year from 2022; value component cut by last year's receipts."""
    e = {y: E2022 * (1 - g) ** (y - 2022) for y in range(2026, 2038)}
    R = {y: receipts_pp(price(y), e[y]) for y in range(2026, 2038)}
    v = {y: V0 - R[y - 1] if y > 2027 else V0 for y in YEARS}
    return e, R, v


def fiscal_tables():
    print(f"Taxable household base 2022: EUR {BASE:,.0f} bn; intensity {E2022:.3f} kg CO2e/EUR;"
          f" ETS-type share of its footprint {S_ETS:.3f}")
    print(f"1 pp of value component = EUR {BASE / 100:,.1f} bn; brief's 0.5 pp = EUR {BASE / 200:,.1f} bn")
    print(f"EUR 20/t at {E2022:.3f} kg/EUR on the base = EUR {20 * E2022 / 1000 * BASE:,.1f} bn (gross)")
    print("Table 2: 2037, P = 200")
    for e in (0.15, 0.20, 0.25, 0.30, E2022):
        gross = 200 * e / 10
        net = receipts_pp(200, e)
        print(f"  e={e:.3f}: gross {gross:5.2f} pp; net of ETS deduction {net:5.2f} pp; "
              f"neutral value component {V0 - net:5.2f}%; brief path (value 10%) revenue change "
              f"{net - 5:+5.2f} pp = EUR {(net - 5) * BASE / 100:+6.0f} bn")
    print("Neutrality rule, value component by year:")
    for g in (0.03, 0.05, 0.07):
        e, R, v = path(g)
        brk = (V0 - v[2037]) * 10 / 200
        print(f"  g={g:.0%}: e2037={e[2037]:.3f}; v2032={v[2032]:.2f}; v2037={v[2037]:.2f}; "
              f"receipts 2037 {R[2037]:.2f} pp; break-even intensity 2037 {brk:.3f}")


def fig1():
    d = cats[cats.vat == "taxable"].sort_values("ghg_all")
    y = np.arange(len(d))
    fig, ax = plt.subplots(figsize=(7.0, 6.2), dpi=200)
    h = 0.38
    ax.barh(y + h / 2, d.ghg_eu, height=h - 0.04, color=BLUE, label="Made in the EU")
    ax.barh(y - h / 2, d.ghg_extra_eu, height=h - 0.04, color=ORANGE, label="Imported from outside the EU")
    ax.scatter(d.ghg_purchasers, y, marker="|", s=120, color=INK, zorder=4,
               label="All origins, per euro of retail price")
    ax.set_yticks(y)
    ax.set_yticklabels(d.category, fontsize=8, color=INK)
    ax.set_xlabel("kg CO₂e per euro of household spending (2022)")
    ax.grid(axis="x", color=GRID, lw=0.8)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.set_xlim(0, 3.1)
    ax.legend(loc="lower right", frameon=False, fontsize=8)
    fig.suptitle("Imports from outside the EU embody 1.3 to 3 times the carbon per euro\nof the same manufactures made in the EU",
                 x=0.01, ha="left", fontsize=10.5, color=INK)
    fig.text(0.01, 0.005, "Bars at basic prices; tick marks spread trade margins over goods (purchasers' prices,"
             " excluding taxes).\nSource: author's MRIO calculation from Eurostat FIGARO tables "
             "(naio_10_fcp_ip4) and GHG footprints\n(env_ac_ghgfp), 2022; 2.Source/calibrate_defaults.py.",
             fontsize=7, color=MUTED)
    fig.tight_layout(rect=(0, 0.06, 1, 0.95))
    fig.savefig(FIG / "fig1-default-intensities.png")
    plt.close(fig)


def fig2():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 3.6), dpi=200, sharey=False)
    for g, col in ((0.03, ORANGE), (0.05, BLUE), (0.07, AQUA)):
        _, _, v = path(g)
        ys = [v[y] for y in YEARS]
        a1.plot(YEARS, ys, color=col, lw=2)
        a1.text(2037.2, ys[-1], f"{g:.0%} a year", va="center", fontsize=7.5, color=INK)
    a1.plot(YEARS, V0 - 0.5 * (YEARS - 2027), color=MUTED, lw=1.2, ls="--")
    a1.text(2037.2, 10.0, "Fixed path", va="center", fontsize=7.5, color=MUTED)
    a1.set_ylim(9, 15.5)
    a1.set_xlim(2027, 2040.3)
    a1.set_title("A. Value component under the rule,\nby annual fall in basket intensity", loc="left",
                 fontsize=9, color=INK)
    a1.set_ylabel("Percent of price")
    _, _, v = path(0.05)
    for x, col in ((0.10, "#86b6ef"), (0.25, "#2a78d6"), (0.40, "#1c5cab"), (0.80, "#0d366b")):
        ys = [v[y] + price(y) * x / 10 for y in YEARS]
        a2.plot(YEARS, ys, color=col, lw=2)
        a2.text(2037.2, ys[-1], f"{x:.2f} kg/€", va="center", fontsize=7.5, color=INK)
    a2.set_xlim(2027, 2040.0)
    a2.set_title("B. Total rate on goods of given intensity\n(central case, 5% a year)", loc="left",
                 fontsize=9, color=INK)
    for ax in (a1, a2):
        ax.grid(axis="y", color=GRID, lw=0.8)
        ax.set_xticks(range(2027, 2038, 5))
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
    fig.text(0.01, 0.01, "Carbon price rises €20/tCO₂e a year from 2027; value component each year falls by the "
             "previous\nyear's net carbon receipts. Basket: taxable household spending, 0.41 kg CO₂e/€ in 2022; "
             f"{S_ETS:.0%} of its footprint\ndeducted at a stylized ETS price of €{Q_ETS:.0f}/t. "
             "Source: 2.Source/make_wp_figures.py.", fontsize=7, color=MUTED)
    fig.tight_layout(rect=(0, 0.12, 1, 1))
    fig.savefig(FIG / "fig2-neutrality-rule.png")
    plt.close(fig)


def fig3():
    q = pd.read_csv(HERE / "distribution_quintiles.csv", index_col=0) * 100
    c = pd.read_csv(HERE / "distribution_countries.csv", index_col=0)
    c = (c.drop(columns="country_spend_meur") * 100).sort_values("swap_eu")
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 4.8), dpi=200, gridspec_kw={"width_ratios": [1, 1.25]})
    x = np.arange(5)
    w = 0.26
    for i, (col, lab, colr) in enumerate((("swap_national", "VAT swap only", BLUE),
                                          ("full_vat", "+ obligation, returned as VAT cut", ORANGE),
                                          ("full_lump", "+ obligation, returned per household", AQUA))):
        a1.bar(x + (i - 1) * w, q[col], width=w - 0.03, color=colr, label=lab)
    a1.axhline(0, color=MUTED, lw=0.8)
    a1.set_xticks(x)
    a1.set_xticklabels(["Poorest\nfifth", "2", "3", "4", "Richest\nfifth"], fontsize=8)
    a1.set_ylabel("Net change in tax, % of spending")
    a1.legend(frameon=False, fontsize=7, loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=1)
    a1.set_title("A. By income quintile (national neutrality)", loc="left", fontsize=9, color=INK)
    y = np.arange(len(c))
    a2.barh(y, c.swap_eu, color=[ORANGE if v > 0 else BLUE for v in c.swap_eu], height=0.75)
    a2.axvline(0, color=MUTED, lw=0.8)
    a2.set_yticks(y)
    a2.set_yticklabels(c.index, fontsize=7)
    a2.set_xlabel("Net change in tax, % of spending")
    a2.set_title("B. By member state, one EU-wide value cut", loc="left", fontsize=9, color=INK)
    for ax in (a1, a2):
        ax.grid(axis="y" if ax is a1 else "x", color=GRID, lw=0.8)
        ax.set_axisbelow(True)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
    fig.text(0.01, 0.01, "€200/tCO₂e on 2022 intensities; 22 member states with 2020 household budget survey"
             " detail.\nSource: author's calculation from Eurostat hbs_str_t223, hbs_exp_t133, nama_10_co3_p3,"
             " env_ac_ainah_r2\nand the default intensities; 2.Source/distribution.py.", fontsize=7, color=MUTED)
    fig.tight_layout(rect=(0, 0.09, 1, 1))
    fig.savefig(FIG / "fig3-distribution.png")
    plt.close(fig)


def fig4():
    stages = ["Steel mill", "Appliance maker", "Retailer"]
    vat = [25.0, 37.5, 37.5]
    cc = [8.0, 10.0, 2.0]
    ets = [32.0, 0.0, 0.0]
    fig, ax = plt.subplots(figsize=(6.4, 3.0), dpi=200)
    x = np.arange(3)
    ax.bar(x - 0.2, vat, width=0.36, color=BLUE, label="Value component remitted")
    ax.bar(x + 0.2, ets, width=0.36, color=MUTED, label="ETS price paid")
    ax.bar(x + 0.2, cc, width=0.36, bottom=ets, color=ORANGE, label="Carbon component remitted")
    for i in range(3):
        ax.text(x[i] + 0.2, ets[i] + cc[i] + 1, f"€{ets[i] + cc[i]:.0f}", ha="center", fontsize=7.5, color=INK)
        ax.text(x[i] - 0.2, vat[i] + 1, f"€{vat[i]:.1f}", ha="center", fontsize=7.5, color=INK)
    ax.set_xticks(x)
    ax.set_xticklabels([f"{s}\n{t}" for s, t in zip(stages, ("adds 400 kg", "adds 100 kg", "adds 20 kg"))],
                       fontsize=8)
    ax.set_ylabel("Euros per finished appliance")
    ax.grid(axis="y", color=GRID, lw=0.8)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.set_ylim(0, 58)
    ax.legend(frameon=False, fontsize=7.5, loc="upper center", ncol=3)
    ax.set_title("Each firm pays €100/t on the carbon it adds, net of carbon prices already paid",
                 loc="left", fontsize=9.5, color=INK)
    fig.text(0.01, 0.01, "Stylized, 2032: value component 12.5%, carbon price €100/t, ETS price €80/t at the"
             " mill.\nSales values €200, €500, €800. Source: 2.Source/check_propositions.py.",
             fontsize=7, color=MUTED)
    fig.tight_layout(rect=(0, 0.08, 1, 1))
    fig.savefig(FIG / "fig4-vat-chain.png")
    plt.close(fig)


if __name__ == "__main__":
    fiscal_tables()
    fig1()
    fig2()
    fig3()
    fig4()
    print("wrote figures to", FIG)
