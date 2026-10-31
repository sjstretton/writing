#!/usr/bin/env python3
"""Common activity layer: worked example for ActivityModelling.qmd (Table 3).

Activity rule (equation 1 of the paper):
    A_t = A_0 (P_t/P_0)^beta (y_t/y_0)^eps (c_t/c_base)^eta
Stylized drivers: population +1% a year, income per person +2% a year, ten years,
2025 elasticities held fixed. Parameter values are those set out in Table 2 of the
paper (sources there). Run: python3 activity_layer.py
"""
POP_G, INC_G, YEARS = 0.01, 0.02, 10

rows = [  # activity, beta, eps, eta
    ("Electricity, homes, at USD 3,000 per person", 0.83, 0.83, -0.44),
    ("Passenger travel, combined", 1.0, 1.24, 0.0),
    ("Road freight (tonne-km)", 1.0, 1.0, -0.1),
    ("Home heating, hot water and cooking (useful heat)", 1.0, 0.39, -0.2),
    ("Steel and aluminum", 1.17, 1.17, -0.4),
    ("Cement and clinker", 0.60, 0.60, -0.1),
    ("Fertilizers", 0.92, 0.92, -0.4),
    ("Cars in use, below 300 per 1,000 people", 1.0, 2.0, -0.25),
    ("Vans and trucks", 1.0, 1.0, -0.2),
    ("Km per car", 0.0, 0.05, -0.05),
]

def growth(beta, eps, years=YEARS):
    return (1 + POP_G) ** (beta * years) * (1 + INC_G) ** (eps * years)

print("| Activity | beta | eps | Change over 10 years | Change with beta = 1 |")
print("|---|---:|---:|---:|---:|")
for name, b, e, _ in rows:
    g = growth(b, e) - 1
    g1 = growth(1.0 if b == e else b, e) - 1
    print(f"| {name} | {b:.2f} | {e:.2f} | {100*g:+.0f}% | {100*g1:+.0f}% |")

print("\nPrice term: energy cost of the service up 20 percent")
for name, b, e, eta in rows:
    print(f"  {name}: {100*(1.2**eta - 1):+.1f}%")
car = 1.2 ** -0.25 * 1.2 ** -0.05 - 1
print(f"Car use (cars x km per car): {100*car:+.1f}%")

# Consistency check: car-km must fit inside passenger-km.
occ = 1.7
print("\nYears until car passenger-km would grow to equal total travel, if cars start at a share s of pkm:")
for s in (0.3, 0.5):
    t, share = 0, s
    while share < 1 and t < 200:
        t += 1
        share = s * growth(1, 2.0, t) * growth(0, 0.05, t) / growth(1, 1.24, t)
    print(f"  starting share {s:.0%}: {t} years (elasticity 2.0 held fixed)")
