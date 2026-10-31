"""Paper 4.5, "The CBAM Policy Tool": worked example with public data only.

Run from this folder:  python3 cbam_example.py   (add --refetch to re-query Eurostat)

Exporter: Türkiye. Goods: hot-rolled flat steel (CN 7208), rebar (CN 7214 20 00),
unwrought aluminium (CN 7601). Inputs:
  * default values (direct emissions, before mark-up): Commission workbook
    'DVs as adopted' (4 Feb 2026) for Implementing Regulation (EU) 2025/2621;
  * EU imports from Türkiye, tonnes and euro: Eurostat Comext DS-045409;
  * mark-ups 10/20/30 percent in 2026/2027/2028+ (Regulation 2025/2621);
  * phase-in: share of embedded emissions not covered by the free-allocation
    adjustment, 1 - CBAM factor, from Directive 2003/87/EC Art. 10a(1a);
  * default CBAM benchmarks (Column B) from Implementing Regulation (EU)
    2025/2620, Annex point 5.3 (read 30 Oct 2026): CN 7208 route (C) 1.370,
    CN 7214 20 00 route (C) 1.364, CN 7601 route (K) 1.423 tCO2/t. They affect
    2026-2033 only, not the full phase-in results.
Stylized: certificate price EUR 80/tCO2 (as in paper 1.4); domestic carbon
price EUR 20/tCO2 effectively paid on all embedded emissions (actual-values
route only, Article 9).

Outputs: table_example.csv, table_aggregate.csv, figures/fig1_charge_path.png
"""

from pathlib import Path
import csv
import json
import sys
import urllib.request

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
FIG = HERE / "figures"
FIG.mkdir(exist_ok=True)

P_EU = 80.0          # EUR per tCO2, stylized certificate price
P_DOM = 20.0         # EUR per tCO2, stylized domestic carbon price
YEAR_TRADE = 2025
PHASE_IN = {2026: 0.025, 2027: 0.05, 2028: 0.10, 2029: 0.225, 2030: 0.485,
            2031: 0.61, 2032: 0.735, 2033: 0.86, 2034: 1.0}
MARKUP = {2026: 0.10, 2027: 0.20}           # 0.30 from 2028
BENCHMARK = {"7208": 1.370, "72142000": 1.364, "7601": 1.423}  # IR 2025/2620, Annex 5.3, Column B
SHORT = {"7208": "Hot-rolled flat steel", "72142000": "Rebar", "7601": "Unwrought aluminum"}


def markup(year):
    return MARKUP.get(year, 0.30)


def load():
    dv = {r["cn"]: r for r in csv.DictReader(open(DATA / "default_values_turkiye.csv"))}
    tr = {(r["cn"], int(r["year"])): r for r in csv.DictReader(open(DATA / "eurostat_eu_imports_from_tr.csv"))}
    return dv, tr


def refetch():
    """Re-query Eurostat Comext and print the numbers for comparison with the CSV."""
    base = ("https://ec.europa.eu/eurostat/api/comext/dissemination/statistics/1.0/data/DS-045409"
            "?format=JSON&freq=A&reporter=EU&partner=TR&flow=1&indicators=QUANTITY_IN_100KG"
            "&indicators=VALUE_IN_EUROS&time=2024&time=2025&lang=en&product=")
    for cn in SHORT:
        d = json.load(urllib.request.urlopen(base + cn, timeout=60))
        ind = d["dimension"]["indicators"]["category"]["index"]
        tim = d["dimension"]["time"]["category"]["index"]
        nt = len(tim)
        for y, j in tim.items():
            q = d["value"].get(str(ind["QUANTITY_IN_100KG"] * nt + j))
            v = d["value"].get(str(ind["VALUE_IN_EUROS"] * nt + j))
            print(cn, y, "tonnes", q / 10 if q else None, "EUR", v)


def charge_per_tonne(see, cn, year, credit_price=0.0):
    """EUR per tonne: certificate price x certificates net of the free-allocation
    adjustment, less a carbon price effectively paid at origin (per tonne)."""
    covered = max(0.0, see - (1 - PHASE_IN[year]) * BENCHMARK[cn])
    gross = P_EU * covered
    return max(0.0, gross - credit_price * see), gross


def example():
    dv, tr = load()
    rows, agg = [], []
    for cn in SHORT:
        see0 = float(dv[cn]["see_direct_tco2_per_t"])
        route = dv[cn]["route"]
        q = float(tr[(cn, YEAR_TRADE)]["quantity_t"])
        v = float(tr[(cn, YEAR_TRADE)]["value_eur"])
        unit = v / q
        for year in (2026, 2030, 2034):
            see_def = see0 * (1 + markup(year))
            c_def, _ = charge_per_tonne(see_def, cn, year)
            c_avg, _ = charge_per_tonne(see0, cn, year)
            c_avg_cr, _ = charge_per_tonne(see0, cn, year, P_DOM)
            rows.append(dict(cn=cn, product=SHORT[cn], year=year, unit_value_eur_t=round(unit),
                             see_default_marked_up=round(see_def, 3), see_country_average=round(see0, 3),
                             charge_default=round(c_def, 1), charge_actual_at_average=round(c_avg, 1),
                             charge_actual_with_domestic_20=round(c_avg_cr, 1),
                             charge_default_pct_value=round(100 * c_def / unit, 1)))
            agg.append(dict(cn=cn, year=year, tonnes=round(q), value_eur_m=round(v / 1e6, 1),
                            charge_default_eur_m=round(c_def * q / 1e6, 1),
                            charge_average_eur_m=round(c_avg * q / 1e6, 1),
                            charge_with_credit_eur_m=round(c_avg_cr * q / 1e6, 1),
                            domestic_revenue_eur_m=round(P_DOM * see0 * q / 1e6, 1)))
    for name, data in (("table_example.csv", rows), ("table_aggregate.csv", agg)):
        with open(HERE / name, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(data[0]))
            w.writeheader()
            w.writerows(data)
    return rows, agg


def figure():
    dv, _ = load()
    see0 = float(dv["7208"]["see_direct_tco2_per_t"])
    years = sorted(PHASE_IN)
    series = [
        ("Default value with mark-up", [charge_per_tonne(see0 * (1 + markup(y)), "7208", y)[0] for y in years], "#2a78d6", "-"),
        ("Actual data at the country average", [charge_per_tonne(see0, "7208", y)[0] for y in years], "#eb6834", "-"),
        ("Actual data, with a EUR 20 domestic carbon price credited",
         [charge_per_tonne(see0, "7208", y, P_DOM)[0] for y in years], "#1baf7a", "--"),
    ]
    fig, ax = plt.subplots(figsize=(7.0, 3.8), dpi=200)
    for lab, ys, col, ls in series:
        ax.plot(years, ys, color=col, lw=2, ls=ls, marker="o", ms=4, label=lab)
        ax.annotate(f"{ys[-1]:.0f}", (years[-1], ys[-1]), xytext=(6, 0), textcoords="offset points",
                    va="center", fontsize=8, color="#0b0b0b")
    ax.set_ylabel("EUR per tonne of steel", fontsize=9)
    ax.set_xlim(2025.6, 2034.8)
    ax.set_ylim(0, 280)
    ax.grid(color="#e4e3df", lw=0.8)
    ax.set_axisbelow(True)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    ax.tick_params(colors="#52514e", labelsize=8)
    ax.legend(fontsize=7.5, frameon=False, loc="upper left")
    fig.tight_layout()
    fig.savefig(FIG / "fig1_charge_path.png")
    plt.close(fig)


if __name__ == "__main__":
    if "--refetch" in sys.argv:
        refetch()
    rows, agg = example()
    for r in rows:
        print(r)
    for a in agg:
        print(a)
    figure()
