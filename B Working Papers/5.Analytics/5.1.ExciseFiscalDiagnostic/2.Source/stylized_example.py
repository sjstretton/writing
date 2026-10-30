"""Stylized worked example for the Excise-Fiscal Diagnostic paper (5.1, v0.2).

Country A is fictitious. Every number below is a labelled stylized input, chosen to be of a
realistic order of magnitude for a lower-middle-income country; none is an estimate for any real
country. Physical constants (CO2 per liter) and the WHO tobacco benchmark are from public sources
cited in the paper. Run:  python3 stylized_example.py
"""
FX = 100.0          # local currency units (LCU) per USD
GDP = 40e9          # USD, 2025
CPI_2020, CPI_2025 = 100.0, 140.0

# code, line, rate, rate basis, retail price (LCU per unit), volume (units/yr), unit, LPA divisor
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


print("Table: three comparable measures, Country A (stylized)")
print(f"{'code':4} {'line':18} {'USD/std unit':>13} {'unit':>11} {'% of price':>10} {'% of GDP':>9}")
for code, name, rate, basis, price, vol, unit, abv in LINES:
    lcu = per_unit_lcu(code, rate)                       # LCU per liter or per pack
    usd = lcu / FX
    usd_std = usd / abv if abv else usd                  # per LPA for alcohol
    share = 100 * lcu / price
    rev = usd * vol
    print(f"{code:4} {name:18} {usd_std:13.2f} {unit:>11} {share:10.0f} {100 * rev / GDP:9.2f}")

print(f"\nErosion: specific rates unchanged since 2020 keep {100 * CPI_2020 / CPI_2025:.0f}% of their real value "
      f"(a {100 * (1 - CPI_2020 / CPI_2025):.0f}% real cut)")

# Corrective benchmark for road fuels: t* = e_C + e_P + beta * (e_cong + e_acc + e_road), USD/liter
CO2 = {"Petrol": 2.31, "Diesel": 2.68}          # kg CO2 per liter (IPCC 2006 defaults, rounded)
SCC = {"low": 25.0, "central": 50.0, "high": 100.0}
BETA = {"low": 0.35, "central": 0.5, "high": 0.65}
# stylized external costs, USD per liter of fuel (low, central, high)
EXT = {
    "Petrol": {"air": (0.02, 0.04, 0.08), "cong": (0.04, 0.10, 0.20), "acc": (0.10, 0.20, 0.35), "road": (0.0, 0.0, 0.01)},
    "Diesel": {"air": (0.08, 0.15, 0.30), "cong": (0.02, 0.05, 0.10), "acc": (0.10, 0.20, 0.35), "road": (0.02, 0.05, 0.08)},
}
CURRENT = {"Petrol": 0.30, "Diesel": 0.18}
VOL = {"Petrol": 1.0e9, "Diesel": 2.0e9}
PUMP = {"Petrol": 1.10, "Diesel": 1.05}
idx = {"low": 0, "central": 1, "high": 2}

print("\nTable: corrective benchmark for road fuels, USD per liter (stylized)")
for f in ("Petrol", "Diesel"):
    out = {}
    for case in ("low", "central", "high"):
        i = idx[case]
        e = EXT[f]
        carbon = CO2[f] / 1000 * SCC[case]
        km = e["cong"][i] + e["acc"][i] + e["road"][i]
        out[case] = dict(carbon=carbon, air=e["air"][i], cong=e["cong"][i], acc=e["acc"][i], road=e["road"][i],
                         naive=carbon + e["air"][i] + km, t=carbon + e["air"][i] + BETA[case] * km)
    c = out["central"]
    print(f"{f}: carbon {c['carbon']:.2f}  air {c['air']:.2f}  congestion {c['cong']:.2f}  accidents {c['acc']:.2f}"
          f"  road {c['road']:.2f}  naive sum {c['naive']:.2f}  corrective t* {c['t']:.2f}"
          f"  (range {out['low']['t']:.2f}-{out['high']['t']:.2f})  current {CURRENT[f]:.2f}"
          f"  gap {c['t'] - CURRENT[f]:+.2f}")
    gap = c["t"] - CURRENT[f]
    if gap > 0:
        static = gap * VOL[f]
        dq = -0.3 * gap / PUMP[f]                     # short-run elasticity -0.3, full pass-through
        dyn = (CURRENT[f] + gap) * VOL[f] * (1 + dq) - CURRENT[f] * VOL[f]
        print(f"   closing the gap: static +{100 * static / GDP:.2f}% of GDP; with elasticity -0.3, "
              f"volume {100 * dq:.1f}%, revenue +{100 * dyn / GDP:.2f}% of GDP")
