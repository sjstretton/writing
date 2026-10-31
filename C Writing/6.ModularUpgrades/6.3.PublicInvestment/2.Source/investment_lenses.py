#!/usr/bin/env python3
"""Cost-of-capital lenses for climate investment needs (stylized).

Reproduces Table 2 of PublicInvestment.qmd: the annual capital charge on one
year's investment, set against fuel and operating savings, at different rates.

Inputs (all stated in the paper):
  - Investment needs, 2030, USD billion (IHLEG third report, Bhattacharya et al. 2024):
    advanced economies 2,750; China 1,350; EMDEs other than China 2,400
    (midpoints of the published ranges).
  - Financial savings per dollar of capital, b = 0.133 a year: chosen so that the
    benefit-cost ratio at 6% and a 25-year life is 1.70, the order of magnitude of
    the SISEPUEDE results for Latin America and the Caribbean (Kalra et al. 2023).
    Stylized; a country run replaces it.
  - Asset life n = 25 years; end-of-year capital recovery factor.
Run: python3 investment_lenses.py
"""

def crf(r, n=25):
    return r / (1 - (1 + r) ** -n)

B = 0.133      # savings per dollar of capital a year (stylized)
N = 25

def breakeven_rate(b=B, n=N):
    lo, hi = 0.0001, 0.5
    for _ in range(100):
        mid = (lo + hi) / 2
        if crf(mid, n) < b:
            lo = mid
        else:
            hi = mid
    return mid

groups = {
    "Advanced economies": (2750, 0.055, 0.07),
    "China": (1350, 0.06, 0.08),
    "EMDEs other than China": (2400, 0.105, 0.15),
}

print("CRF(6%,25) =", round(crf(0.06), 4), " benefit-cost ratio at 6% =", round(B / crf(0.06), 2))
print("Break-even cost of capital r* (CRF(r*,25) = b):", round(100 * breakeven_rate(), 1), "%")
print()
print("| Group | Investment | Charge at market rate | Net (market) | Net (high) | Charge at 6% | Net (6%) |")
print("|---|---:|---:|---:|---:|---:|---:|")
tot = [0] * 6
for g, (I, r, rh) in groups.items():
    sav = B * I
    row = [I, I * crf(r), sav - I * crf(r), sav - I * crf(rh), I * crf(0.06), sav - I * crf(0.06)]
    tot = [a + b for a, b in zip(tot, row)]
    print(f"| {g} ({100*r:.1f}%/{100*rh:.0f}%) | " + " | ".join(f"{x:,.0f}" for x in row) + " |")
print("| World | " + " | ".join(f"{x:,.0f}" for x in tot) + " |")
print()
print("CPAT default WACC by income group, per USD 1,000 of capital (savings 133 a year):")
for g, r in [("HIC", 0.075), ("UMIC", 0.10), ("LMIC", 0.125), ("LIC", 0.15)]:
    c = 1000 * crf(r)
    print(f"  {g}: {100*r:.1f}%  charge {c:.0f}  net {1000*B - c:+.0f}")
print()
pen = 2400 * (crf(0.105) - crf(0.06))
print(f"EMDE cost-of-capital penalty at 10.5% vs 6%: USD {pen:.0f} bn a year per year's investment")
print(f"Per point of WACC on USD 4,800 bn of clean energy near 6%: USD {4800*(crf(0.07)-crf(0.06)):.0f} bn")
