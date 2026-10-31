#!/usr/bin/env python3
"""Common activity layer: every number in the worked example of ActivityModelling.qmd (v0.2).

Activity rule (the layer's equation in the paper):
    A_t = A_0 (P_t/P_0)^beta (y_t/y_0)^eps (c_t/c_base)^eta
Stylized drivers: population +1% a year, income per person +2% a year, ten years, elasticities held fixed.
Parameter values and their sources are in the paper's parameter table. Prints:
  1. Table 3 (change over ten years, the beta = 1 variant, the price term for a 20% rise in the service cost);
  2. CPAT's income-level factor and the electricity income elasticity at USD 3,000 and above USD 22,000;
  3. the car-share crossing times of Proposition 3 (constant elasticities) and the share path with the
     Gompertz elasticity of CPAT's fleet model (saturation 800 per 1,000);
  4. the Gompertz elasticity against the straight-line approximation;
  5. the stylized steel and clinker example.
Run: python3 activity_layer.py
"""
import math

POP_G, INC_G, YEARS = 0.01, 0.02, 10

# CPAT income-level factor (CPAT-AI model documentation, 03_Energy_demand, constants IncfA..IncfNorm)
A4, A3, A2, A1, A0, NORM, XCAP = 0.012019, -0.365464, 4.011846, -18.722243, 31.75949, 0.74, 10.0


def inc_factor(gdp_pc):
    x = min(XCAP, math.log(gdp_pc))
    return max(0.0, A4 * x**4 + A3 * x**3 + A2 * x**2 + A1 * x + A0) / NORM


ELEC_BASE = 0.8  # legacy CPAT income elasticity, electricity, residential and industry (all income groups)
eps_elec = round(ELEC_BASE * inc_factor(3000), 2)

# activity, beta (models' choice), eps, eta
ROWS = [
    ("Electricity, homes, at USD 3,000 per person", eps_elec, eps_elec, -0.44),
    ("Passenger travel (passenger-km)", 1.0, 1.0, 0.0),
    ("Road freight (tonne-km)", 1.0, 1.0, -0.1),
    ("Home heat, hot water and cooking (useful heat)", 1.0, 0.4, -0.2),
    ("Steel and aluminum", 1.2, 1.2, -0.4),
    ("Cement and clinker", 0.6, 0.6, -0.1),
    ("Fertilizers", 0.9, 0.9, -0.4),
    ("Cars in use, below 300 per 1,000 people", 1.0, 2.0, -0.25),
    ("Vans and trucks", 1.0, 1.0, -0.2),
    ("Km per car", 0.0, 0.1, -0.05),
]


def growth(beta, eps, years=YEARS):
    return (1 + POP_G) ** (beta * years) * (1 + INC_G) ** (eps * years)


def main():
    print("1. Table 3")
    print("| Activity | beta | eps | Change over 10 years | With beta = 1 | 20% rise in service cost |")
    for name, b, e, eta in ROWS:
        g = growth(b, e) - 1
        g1 = growth(1.0 if b == e else b, e) - 1
        print(f"| {name} | {b:.2f} | {e:.2f} | {100*g:+.0f}% | {100*g1:+.0f}% | {100*(1.2**eta - 1):+.1f}% |")
    print(f"Total GDP over ten years: {100*(growth(1, 1) - 1):+.1f}%")
    cars, km, pkm = growth(1, 2.0), growth(0, 0.1), growth(1, 1.0)
    print(f"Car passenger-km relative to total passenger-km after ten years: x{cars*km/pkm:.3f}")
    print(f"Car use (cars x km per car) after a 20% rise in the cost of driving: {100*(1.2**-0.30 - 1):+.1f}%")
    print("Population-exponent gap, percentage points a year at 1% population growth:")
    for name, b, e, _ in ROWS:
        if b == e and b != 1.0:
            print(f"   {name}: {100*(1-e)*math.log(1.01):+.2f}")

    print("\n2. CPAT income-level factor")
    for y in (1000, 2250, 3000, 6000, 10000, 22026):
        print(f"   GDP per person {y}: factor {inc_factor(y):.3f}, electricity elasticity {ELEC_BASE*inc_factor(y):.2f}")

    print("\n3. Proposition 3: years until car passenger-km would exceed total passenger-km")
    expo = 2.0 + 0.1 - 1.0
    for s in (0.3, 0.5):
        t = -math.log(s) / (expo * math.log(1 + INC_G))
        print(f"   starting share {s:.0%}: {t:.1f} years (crosses in year {math.ceil(t)}), constant elasticities")
    # With CPAT's Gompertz curve (a=-5.897, b=-0.23 per 1,000 USD), saturation 800, starting at USD 3,000.
    a, b, sat, y0 = -5.897, -0.23, 800.0, 3000.0
    own = lambda y: sat * math.exp(a * math.exp(b * y / 1000))
    for s in (0.3, 0.5):
        peak, path = 0, []
        for t in range(0, 201):
            y = y0 * (1 + INC_G) ** t
            share = s * (own(y) / own(y0)) * ((1 + INC_G) ** (0.1 * t)) / ((1 + INC_G) ** (1.0 * t))
            peak = max(peak, share)
            path.append(share)
        cross = next((t for t, v in enumerate(path) if v > 1), None)
        print(f"   Gompertz, start {s:.0%} at USD 3,000 ({own(y0):.0f} per 1,000): peak share {peak:.2f}, "
              f"crosses 1 in year {cross}, ownership then {own(y0*(1+INC_G)**cross):.0f} per 1,000")

    print("\n4. Gompertz income elasticity (saturation 800) against the straight line 2.0 to 300, 0 at 800")
    for o in (30, 90, 150, 300, 450, 600, 750):
        lf = math.log(o / sat)
        el = lf * math.log(lf / a)
        line = 2.0 if o <= 300 else 2.0 * (800 - o) / 500
        print(f"   {o} per 1,000: Gompertz {el:.2f}, line {line:.2f}, gap {line-el:+.2f}")
    ypk = -1000 / b
    print(f"   peak elasticity {a*b*(ypk/1000)*math.exp(b*ypk/1000):.2f} at USD {ypk:,.0f}, "
          f"ownership {own(ypk):.0f} per 1,000")

    print("\n5. Stylized steel and clinker example (USD 50 per tCO2, no rebate)")
    for name, ef, price, eta in (("Steel, blast furnace", 2.0, 600.0, -0.4), ("Clinker", 0.8, 60.0, -0.1)):
        share = 50 * ef / price
        print(f"   {name}: cost +{100*share:.0f}%, output {100*((1+share)**eta - 1):+.1f}%")


if __name__ == "__main__":
    main()
