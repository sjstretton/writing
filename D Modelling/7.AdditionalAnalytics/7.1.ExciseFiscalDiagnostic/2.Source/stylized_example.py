"""Stylized worked example for paper 7.1, The Excise-Fiscal Diagnostic (working paper v0.4).

Country A is fictitious. Every number below is a labelled stylized input, chosen to be of a
realistic order of magnitude for a lower-middle-income country; none is an estimate for any real
country. Physical constants are from public sources cited in the paper:
  CO2 per liter = IPCC (2006) default CO2 emission factor x default net calorific value x an assumed
  density (the author's assumption: petrol 0.745 kg/l, diesel 0.84 kg/l, typical market fuels).
Run:  python3 stylized_example.py  (writes stylized_example_output.txt beside this file)

v0.4 (31 Oct 2026): CO2 factors computed from IPCC defaults (petrol 2.29 kg/l, not 2.31); the
static gain reported exactly; component shares, a social-cost carbon case (USD 185/t), a
low-elasticity revenue case and the VSL transfer comparison added (peer review 31 Oct 2026).
"""
from pathlib import Path

OUT = []


def p(s=""):
    OUT.append(s)
    print(s)


FX = 100.0          # local currency units (LCU) per USD
GDP = 40e9          # USD, 2025
CPI_2020, CPI_2025 = 100.0, 140.0

# code, line, rate, rate basis, retail price (LCU per unit), volume (units/yr), unit, ABV
LINES = [
    ("E1", "Petrol", 30.0, "specific, per liter", 110.0, 1.0e9, "liter", None),
    ("E2", "Diesel, road", 18.0, "specific, per liter", 105.0, 2.0e9, "liter", None),
    ("T1", "Cigarettes", 1500.0, "specific, per 1,000 sticks", 150.0, 150e6, "pack of 20", None),
    ("A1", "Beer (5% ABV)", 40.0, "specific, per liter", 200.0, 300e6, "LPA", 0.05),
    ("A5", "Spirits (40% ABV)", 0.30, "30% of ex-factory value (600 LCU/l)", 1200.0, 15e6, "LPA", 0.40),
]


def per_unit_lcu(code, rate):
    if code == "T1":
        return rate * 0.02           # per 1,000 sticks -> per pack of 20
    if code == "A5":
        return rate * 600.0          # ad valorem on ex-factory price, per liter
    return rate


p("Table 3: three comparable measures, Country A (stylized)")
p(f"{'code':4} {'line':18} {'USD/std unit':>13} {'unit':>11} {'% of price':>10} {'% of GDP':>9}")
usd_lpa = {}
for code, name, rate, basis, price, vol, unit, abv in LINES:
    lcu = per_unit_lcu(code, rate)                       # LCU per liter or per pack
    usd = lcu / FX
    usd_std = usd / abv if abv else usd                  # per LPA for alcohol
    usd_lpa[code] = usd_std
    share = 100 * lcu / price
    rev = usd * vol
    p(f"{code:4} {name:18} {usd_std:13.2f} {unit:>11} {share:10.0f} {100 * rev / GDP:9.2f}")
p(f"Spirits pay {100 * (1 - usd_lpa['A5'] / usd_lpa['A1']):.0f}% less per liter of pure alcohol than beer")

p(f"\nErosion: specific rates unchanged since 2020 keep {100 * CPI_2020 / CPI_2025:.0f}% of their real value "
  f"(a {100 * (1 - CPI_2020 / CPI_2025):.0f}% real cut); petrol's 2020 rate is worth LCU {30 * CPI_2025 / CPI_2020:.0f} "
  f"(USD {30 * CPI_2025 / CPI_2020 / FX:.2f}) in 2025 prices")
p(f"Five years at 7% inflation: a specific rate keeps {100 / 1.07 ** 5:.0f}% of its real value")

# CO2 per liter from IPCC 2006 defaults (Vol. 2, ch. 1, Tables 1.2 and 1.4)
EF = {"Petrol": 69_300, "Diesel": 74_100}          # kg CO2 per TJ
NCV = {"Petrol": 44.3, "Diesel": 43.0}             # TJ per Gg (= MJ per kg)
DENSITY = {"Petrol": 0.745, "Diesel": 0.84}         # kg per liter (author's assumption)
CO2 = {f: EF[f] * NCV[f] / 1e6 * DENSITY[f] for f in EF}   # kg CO2 per liter
p("\nCO2 per liter (IPCC 2006 defaults, assumed density): "
  + ", ".join(f"{f} {CO2[f]:.2f} kg" for f in CO2))

# Corrective benchmark: t* = e_C + e_P + beta * (e_cong + e_acc + e_road), USD/liter
SCC = {"low": 25.0, "central": 50.0, "high": 100.0}
BETA = {"low": 0.35, "central": 0.5, "high": 0.65}
EXT = {   # stylized external costs, USD per liter (low, central, high)
    "Petrol": {"air": (0.02, 0.04, 0.08), "cong": (0.04, 0.10, 0.20), "acc": (0.10, 0.20, 0.35), "road": (0.0, 0.0, 0.01)},
    "Diesel": {"air": (0.08, 0.15, 0.30), "cong": (0.02, 0.05, 0.10), "acc": (0.10, 0.20, 0.35), "road": (0.02, 0.05, 0.08)},
}
CURRENT = {"Petrol": 0.30, "Diesel": 0.18}
VOL = {"Petrol": 1.0e9, "Diesel": 2.0e9}
PUMP = {"Petrol": 1.10, "Diesel": 1.05}
idx = {"low": 0, "central": 1, "high": 2}


def benchmark(f, case, scc=None, beta=None):
    i = idx[case]
    e = EXT[f]
    carbon = CO2[f] / 1000 * (scc if scc is not None else SCC[case])
    b = beta if beta is not None else BETA[case]
    km = e["cong"][i] + e["acc"][i] + e["road"][i]
    return dict(carbon=carbon, air=e["air"][i], cong=e["cong"][i], acc=e["acc"][i], road=e["road"][i],
                naive=carbon + e["air"][i] + km, t=carbon + e["air"][i] + b * km, beta=b)


p("\nTable 4: corrective benchmark for road fuels, USD per liter (stylized)")
for f in ("Petrol", "Diesel"):
    c, lo, hi = benchmark(f, "central"), benchmark(f, "low"), benchmark(f, "high")
    p(f"{f}: carbon {c['carbon']:.3f}  air {c['air']:.2f}  congestion {c['cong']:.2f}  accidents {c['acc']:.2f}"
      f"  road {c['road']:.2f}  naive sum {c['naive']:.3f}  corrective t* {c['t']:.3f}"
      f"  (range {lo['t']:.3f}-{hi['t']:.3f})  current {CURRENT[f]:.2f}  gap {c['t'] - CURRENT[f]:+.3f}"
      f"  (low {lo['t'] - CURRENT[f]:+.3f}, high {hi['t'] - CURRENT[f]:+.3f})")
    km_part = c["beta"] * (c["cong"] + c["acc"] + c["road"])
    p(f"   shares of t*: carbon {100 * c['carbon'] / c['t']:.0f}%, air {100 * c['air'] / c['t']:.0f}%, "
      f"distance-related (beta-weighted) {100 * km_part / c['t']:.0f}% "
      f"(of which accidents {100 * c['beta'] * c['acc'] / c['t']:.0f}%)")
    for b in (0.35, 0.65):
        p(f"   beta {b}: t* {benchmark(f, 'central', beta=b)['t']:.3f}")
    sc = benchmark(f, "central", scc=185.0)
    p(f"   social-cost case (USD 185/t): carbon {sc['carbon']:.3f}, t* {sc['t']:.3f}")
    gap = c["t"] - CURRENT[f]
    if gap > 0:
        static = gap * VOL[f]
        p(f"   closing the gap: static USD {static / 1e6:.0f} million, +{100 * static / GDP:.2f}% of GDP")
        for el in (-0.1, -0.3):
            dq = el * gap / PUMP[f]                     # short-run elasticity, full pass-through
            dyn = (CURRENT[f] + gap) * VOL[f] * (1 + dq) - CURRENT[f] * VOL[f]
            p(f"   with elasticity {el}: volume {100 * dq:.1f}%, revenue +{100 * dyn / GDP:.2f}% of GDP")

# Carbon component at USD 50/t, for the country comparison in Section 7
p("\nCarbon component at USD 50/t: " + ", ".join(f"{f} {CO2[f] / 1000 * 50:.3f}" for f in CO2)
  + "; at USD 185/t: " + ", ".join(f"{f} {CO2[f] / 1000 * 185:.3f}" for f in CO2))
p(f"Sierra Leone petrol 0.23 / carbon component = {0.23 / (CO2['Petrol'] / 1000 * 50):.1f}x")

# VSL transfer: OECD-based option (100 x income, elasticity 1.0) against Robinson et al. (2019)
# preferred option (US VSL 9.4 million, 160 x US GNI per head, elasticity 1.5, floor 20 x income)
y = 800.0                                   # stylized income per head, USD
US_VSL, US_RATIO = 9.4e6, 160.0
y_us = US_VSL / US_RATIO
v_oecd = 100 * y
v_us15 = max(US_VSL * (y / y_us) ** 1.5, 20 * y)
p(f"\nVSL at income USD {y:.0f}: OECD-based option USD {v_oecd:,.0f} ({v_oecd / y:.0f}x income); "
  f"US-based, elasticity 1.5 USD {v_us15:,.0f} ({v_us15 / y:.0f}x income); ratio {v_oecd / v_us15:.1f}")

Path(__file__).with_name("stylized_example_output.txt").write_text("\n".join(OUT) + "\n", encoding="utf-8")
