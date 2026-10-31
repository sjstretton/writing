"""Worked examples for paper 5.1, The CPAT Mitigation Module: Methods in Brief (working paper v0.2).

All prices and costs are stylized, labelled as such in the paper. Emission
factors and net calorific values are IPCC (2006) defaults. Elasticities are the
legacy CPAT defaults for low-, lower-middle- and upper-middle-income countries,
which take the same values (cpat_ai/data/Public01/tidy/xai_elasticities.csv,
checked 31 Oct 2026).

Run: python3 worked_examples.py   (prints Tables 1 and 2 of the paper and the checks
quoted in the section on the penalty-based rule)
"""
import math

CARBON_PRICE = 50.0  # USD per tCO2

# ---------------------------------------------------------------- demand ----
# name, pre-policy retail price (USD/GJ), EF (tCO2/GJ), usage elast., efficiency elast.
GJ_PER_L_DIESEL = 43.0e-3 * 0.84    # IPCC NCV 43.0 TJ/Gg x stylized density 0.84 kg/l
GJ_PER_L_GASOLINE = 44.3e-3 * 0.74  # IPCC NCV 44.3 TJ/Gg x stylized density 0.74 kg/l
FUELS = [
    ("Coal, industry", 4.0, 0.0946, -0.3, -0.4),
    ("Natural gas, industry", 8.0, 0.0561, -0.5, -0.5),
    ("Diesel, road transport", 1.00 / GJ_PER_L_DIESEL, 0.0741, -0.3, -0.3),
    ("Gasoline, road transport", 1.10 / GJ_PER_L_GASOLINE, 0.0693, -0.4, -0.4),
]


def demand_response(p0, tax, eu, ef):
    """Fuel use ratio after a permanent price step (CPAT eq. M3.1, no GDP change)."""
    ratio = (p0 + tax) / p0
    total = eu + ef + eu * ef
    return ratio, total, ratio ** total


def demand_table():
    rows = []
    for name, p0, efac, eu, ef in FUELS:
        tax = CARBON_PRICE * efac
        ratio, total, q = demand_response(p0, tax, eu, ef)
        rebound = -(eu * ef) / (eu + ef)  # share of the gross response offset (positive)
        rows.append((name, p0, tax, 100 * (ratio - 1), total, 100 * (q - 1),
                     100 * rebound))
    return rows


# ----------------------------------------------------------- investment ----
TECH = ["Solar", "Wind", "Gas", "Coal", "Oil"]
LCOE0 = [45.0, 55.0, 60.0, 65.0, 120.0]       # USD/MWh, stylized, before carbon
TCO2_PER_MWH = [0.0, 0.0, 0.40, 0.95, 0.70]   # stylized plant intensities


def costs(cp):
    return [c + cp * e for c, e in zip(LCOE0, TCO2_PER_MWH)]


def logit_shares(c, k=2.0):
    """CPAT investment logit: weights exp(-K * C_i / C_min).

    Equivalently, the minimiser of sum(C_i s_i) + tau * sum(s_i ln s_i) on the simplex, with
    tau = C_min / K (an entropy penalty in USD/MWh)."""
    cmin = min(c)
    w = [math.exp(-k * x / cmin) for x in c]
    s = sum(w)
    return [x / s for x in w]


def velocity_shares(c, lam=100.0):
    """Exact minimiser of sum(C_i s_i + lam/2 s_i^2) on the simplex.

    Interior solution s_i = 1/N + (Cbar - C_i)/lam over the active set; drop any
    technology with a negative share and recompute the mean over the rest.
    """
    active = list(range(len(c)))
    while True:
        n = len(active)
        cbar = sum(c[i] for i in active) / n
        s = {i: 1.0 / n + (cbar - c[i]) / lam for i in active}
        neg = [i for i in active if s[i] < 0]
        if not neg:
            return [s.get(i, 0.0) for i in range(len(c))]
        active = [i for i in active if s[i] >= 0]


def acceleration_update(c, s_prev, lam_v=100.0, lam_a=0.0):
    """Combined velocity-acceleration rule (interior, before clipping)."""
    n = len(c)
    cbar = sum(c) / n
    return [(lam_a * sp + lam_v / n) / (lam_v + lam_a) + (cbar - ci) / (lam_v + lam_a)
            for ci, sp in zip(c, s_prev)]


def investment_table(prices=(0.0, 75.0)):
    rows = []
    for cp in prices:
        c = costs(cp)
        lg = logit_shares(c)
        vl = velocity_shares(c)
        rows.append((cp, c, lg, vl))
    return rows


if __name__ == "__main__":
    print("Table: demand response to a USD 50/tCO2 carbon price")
    print("| Fuel | Price before (USD/GJ) | Carbon charge (USD/GJ) | Price change (%) | Total elasticity | Fuel use change (%) | Rebound (% of gross) |")
    for r in demand_table():
        print("| %s | %.1f | %.2f | %.0f | %.2f | %.1f | %.0f |" % r)
    print()
    print("Table: investment shares, logit (K=2) vs velocity penalty (lambda=100)")
    for cp, c, lg, vl in investment_table():
        print("carbon price", cp)
        for t, ci, a, b in zip(TECH, c, lg, vl):
            print("| %s | %.1f | %.1f | %.1f |" % (t, ci, 100 * a, 100 * b))
    # background-paper example (stylized costs 20..100): exact vs proportional
    c = [20, 30, 40, 50, 100]
    print("background example exact:", [round(100 * x, 1) for x in velocity_shares(c)])
    pos = [max(0.0, 1 / 5 + (sum(c) / 5 - x) / 100) for x in c]
    print("background example, proportional rescaling:", [round(100 * x / sum(pos), 1) for x in pos])
    # checks quoted in the text (no carbon price)
    c0 = costs(0.0)
    tau = min(c0) / 2.0
    w = [math.exp(-x / tau) for x in c0]
    print("entropy form, tau = %.1f USD/MWh:" % tau, [round(100 * x / sum(w), 1) for x in w])
    print("irrelevant 6th technology at 300 (velocity):", [round(100 * x, 1) for x in velocity_shares(c0 + [300.0])])
    dup = [c0[0]] + c0
    print("solar listed twice: logit solar total %.1f, velocity solar total %.1f" % (
        100 * sum(logit_shares(dup)[:2]), 100 * sum(velocity_shares(dup)[:2])))
    two = [45.0, 55.0]
    print("solar and wind only: logit solar %.1f, velocity solar %.1f" % (
        100 * logit_shares(two)[0], 100 * velocity_shares(two)[0]))
