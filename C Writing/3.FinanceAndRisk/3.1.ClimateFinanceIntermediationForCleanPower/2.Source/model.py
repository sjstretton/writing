"""Model and calibration for Stretton, "Guarantee the Contract, Not the Debt:
A Payment Intermediary for Clean Power" (working paper v0.2, October 2026).

Run:  python3 model.py        (prints every number quoted in the paper and
                                writes calibration_tables.csv)

All parameters marked STYLIZED are illustrative, not estimates.
"""
from math import exp, sqrt
import csv
from pathlib import Path

from statistics import NormalDist

N = NormalDist()
HERE = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# 1. Plant and LCOE as a function of WACC
# ---------------------------------------------------------------------------
# Representative utility-scale solar plant (STYLIZED; same as Time and Chance ch. 14)
CAPEX_PER_KW = 800.0      # $/kW
CAP_FACTOR = 0.20         # 20 percent -> 1,752 kWh per kW per year
OM_PER_KW_YR = 12.0       # $/kW-year
LIFE = 25                 # years
MW = 100                  # plant size for the worked example

KWH_PER_KW = 8760 * CAP_FACTOR


def crf(r, T=LIFE):
    """Capital recovery factor (annuity factor) at real rate r over T years."""
    if r == 0:
        return 1.0 / T
    return r / (1 - (1 + r) ** (-T))


def lcoe(r):
    """Levelized cost in US cents per kWh at real WACC r."""
    return 100 * (CAPEX_PER_KW * crf(r) + OM_PER_KW_YR) / KWH_PER_KW


def finance_share(r):
    """Share of LCOE that is the return on capital (above straight-line depreciation)."""
    total = CAPEX_PER_KW * crf(r) + OM_PER_KW_YR
    return (CAPEX_PER_KW * crf(r) - CAPEX_PER_KW / LIFE) / total


def dlcoe_dr(r, h=1e-5):
    return (lcoe(r + h) - lcoe(r - h)) / (2 * h)


# ---------------------------------------------------------------------------
# 2. Offtaker default hazard with delayed partial recovery (Proposition 1)
# ---------------------------------------------------------------------------
# Default episodes arrive at intensity lam per year (physical). In an episode the
# offtaker withholds all payments for D years; at the end it pays a fraction R of
# the arrears. Investors price episodes at the risk-neutral intensity m*lam.
# Long-run share of time in arrears: phi = lam D / (1 + lam D) (alternating renewal).
# A payment withheld at a uniform point of the episode and paid at its end is
# worth R (1 - exp(-r D)) / (r D) of its face value: the recovery value Rtilde.
# Each contracted dollar is worth 1 - phi (1 - Rtilde) in expectation, so the
# break-even tariff is LCOE(r0) / (1 - h), with haircut h = phi^Q (1 - Rtilde).

def phi(lam, D):
    return lam * D / (1 + lam * D)


def rtilde(R, D, r, extra_delay=0.0):
    base = (1 - exp(-r * D)) / (r * D) if D > 0 else 1.0
    return R * base * exp(-r * extra_delay)


def haircut(lam, R, D, r0, m):
    return phi(m * lam, D) * (1 - rtilde(R, D, r0))


def tariff_with_risk(lam, R, D, r0, m):
    return lcoe(r0) / (1 - haircut(lam, R, D, r0, m))


def wacc_equivalent(tariff_c, lo=0.0001, hi=0.5):
    """WACC at which LCOE equals a given tariff (bisection)."""
    for _ in range(80):
        mid = (lo + hi) / 2
        if lcoe(mid) < tariff_c:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


# Central case (STYLIZED)
R0 = 0.08          # WACC without offtaker risk (country, construction, equity)
LAM = 0.15         # a payment-default episode every 6-7 years on average
REC = 0.60         # 60 percent of withheld payments eventually paid
DELAY = 1.0        # episodes last a year
MPR = 2.0          # risk-neutral / physical intensity ratio (market price of risk)

# ---------------------------------------------------------------------------
# 3. Contract guarantee vs debt guarantee (Proposition 2)
# ---------------------------------------------------------------------------
GEARING = 0.75       # debt share of capex (STYLIZED)
THETA = 0.30         # share of the offtaker haircut that falls on debt holders (STYLIZED)
REC_G = 0.95         # facility recovers 95% using intercept and waterfall (STYLIZED)
DELAY_G = 1.0        # ...one year after the episode ends (STYLIZED)
REC_D = 0.50         # debt guarantor's recovery by subrogation against the SPV (STYLIZED)
DELAY_D = 3.0        # (STYLIZED)
P_OTHER = 0.01       # annual intensity of non-offtaker events a debt guarantee also covers
L_OTHER = 0.30       # loss on debt from those events, share of debt (STYLIZED)
DEBT_TENOR = 18


def tariff_no_guarantee():
    return tariff_with_risk(LAM, REC, DELAY, R0, MPR)


def tariff_contract_guarantee():
    return lcoe(R0)


def tariff_debt_guarantee():
    h = haircut(LAM, REC, DELAY, R0, MPR) * (1 - THETA)
    return lcoe(R0) / (1 - h)


def annual_revenue_musd(tariff_c, mw=MW):
    return mw * 1000 * KWH_PER_KW * tariff_c / 100 / 1e6


def guarantor_cost_contract(mw=MW):
    """Expected annual cost to the facility ($m): phi (physical) x (1 - Rtilde_G) x payments."""
    A = annual_revenue_musd(tariff_contract_guarantee(), mw)
    return phi(LAM, DELAY) * (1 - rtilde(REC_G, DELAY, R0, DELAY_G)) * A


def guarantor_cost_debt():
    """Expected annual cost to a debt guarantor ($m): offtaker-driven + other risks."""
    A = annual_revenue_musd(tariff_debt_guarantee())
    debt = GEARING * CAPEX_PER_KW * MW * 1000 / 1e6
    ds = debt * crf(R0, DEBT_TENOR)
    # share THETA of the project's offtaker losses reaches debt; guarantor recovers
    # REC_D of what it pays, DELAY_D years later, from the SPV.
    offtaker = THETA * phi(LAM, DELAY) * A * (1 - REC_D * exp(-R0 * DELAY_D))
    other = P_OTHER * L_OTHER * debt
    return offtaker, other, debt, ds


# ---------------------------------------------------------------------------
# 4. Waterfall expected loss and liquidity buffer (Proposition 3)
# ---------------------------------------------------------------------------
# Layers after the offtaker: subnational owner, national government (intercept),
# multilateral agency, donor contingency account. q_k = probability that layer k
# pays in full when called (STYLIZED).
LAYERS = [("Offtaker cures (recovery)", None),
          ("Subnational owner", 0.50),
          ("National government", 0.80),
          ("Multilateral agency", 0.90),
          ("Donor contingency account", 1.00)]


def waterfall_expected_costs(lam, A, R1, D1, r, qs):
    """Expected annual cost to each layer behind the facility ($m/yr).

    A: annual contract payments. The facility pays generators throughout each
    episode (expected arrears phi*A a year), recovers Rtilde from the offtaker,
    and passes the unrecovered remainder down the layers, each paying with
    probability q_k. Returns ([cost by layer], facility residual)."""
    residual = phi(lam, D1) * A * (1 - rtilde(R1, D1, r))
    out = []
    reach = 1.0
    for q in qs:
        out.append(residual * reach * q)
        reach *= (1 - q)
    return out, residual * reach


def vasicek_quantile(p, rho, conf):
    """Large-portfolio fraction of offtakers in default at confidence conf."""
    return N.cdf((N.inv_cdf(p) + sqrt(rho) * N.inv_cdf(conf)) / sqrt(1 - rho))


# Regional facility (STYLIZED): 2 GW of solar contracts with 10 offtakers
REG_MW = 2000
REG_RHO = 0.30
REG_CONF = 0.995
BRIDGE = 0.5      # years the facility funds arrears before the sovereign layer pays (STYLIZED)

# ---------------------------------------------------------------------------
# 5. Declining tariff with the same present value as a flat tariff
# ---------------------------------------------------------------------------
FLAT = 5.0           # US c/kWh, flat real, 20 years (Time and Chance ch. 8 example)
TERM = 20
FALL_YEARS = 7       # tariff falls linearly to half its starting value by year 7
NEWBUILD_START, NEWBUILD_END = 5.0, 2.5  # cost of new solar falls 5.0 -> 2.5 by year 7


def declining_path(p0, term=TERM, fall=FALL_YEARS):
    path = []
    for t in range(1, term + 1):
        if t <= fall:
            path.append(p0 * (1 - 0.5 * (t - 1) / (fall - 1)))
        else:
            path.append(p0 * 0.5)
    return path


def pv(path, r):
    return sum(x / (1 + r) ** t for t, x in enumerate(path, start=1))


def solve_p0(r):
    target = pv([FLAT] * TERM, r)
    unit = pv(declining_path(1.0), r)
    return target / unit


def newbuild_path(term=TERM, fall=FALL_YEARS):
    out = []
    for t in range(1, term + 1):
        if t <= fall:
            out.append(NEWBUILD_START - (NEWBUILD_START - NEWBUILD_END) * (t - 1) / (fall - 1))
        else:
            out.append(NEWBUILD_END)
    return out


# ---------------------------------------------------------------------------
# Main: print every number the paper quotes
# ---------------------------------------------------------------------------
def main():
    rows = []
    print("1. LCOE vs WACC: $800/kW, CF 20%, O&M $12/kW-yr, 25 years")
    for r in [0.04, 0.05, 0.06, 0.08, 0.10, 0.12, 0.15]:
        print(f"  WACC {r:5.0%}: LCOE {lcoe(r):4.2f} c/kWh; x{lcoe(r)/lcoe(0.04):.2f} of 4%; "
              f"finance share {finance_share(r):.0%}")
        rows.append(["lcoe", r, round(lcoe(r), 3), round(finance_share(r), 3)])
    print(f"  dLCOE/dr at 8%: {dlcoe_dr(0.08)/100:.3f} c/kWh per percentage point")
    print(f"  Plant output: {MW} MW x {KWH_PER_KW:.0f} kWh/kW = {MW*KWH_PER_KW/1e3:.0f} MWh/yr; capex ${CAPEX_PER_KW*MW/1e3:.0f}m")
    for r in [0.05, 0.08, 0.12]:
        print(f"  100 MW at {r:.0%}: annual revenue requirement ${annual_revenue_musd(lcoe(r)):.2f}m")

    print("\n2. Offtaker premium (Proposition 1)")
    h = haircut(LAM, REC, DELAY, R0, MPR)
    t = tariff_with_risk(LAM, REC, DELAY, R0, MPR)
    print(f"  central: lam={LAM}, R={REC}, D={DELAY}, m={MPR}, r0={R0}: phi_Q={phi(MPR*LAM, DELAY):.3f}, "
          f"Rtilde={rtilde(REC, DELAY, R0):.3f}, haircut={h:.3f}")
    print(f"  tariff without offtaker risk {lcoe(R0):.2f} c/kWh; with {t:.2f}; premium {t-lcoe(R0):.2f} c/kWh "
          f"({t/lcoe(R0)-1:.1%}); WACC-equivalent {wacc_equivalent(t)*100:.1f}% (+{(wacc_equivalent(t)-R0)*100:.1f} pp)")
    print("  grid (D=1, m=2): tariff premium % / WACC-equivalent pp")
    for lam in [0.05, 0.10, 0.15, 0.25]:
        cells = []
        for R in [0.3, 0.6, 0.9]:
            tt = tariff_with_risk(lam, R, DELAY, R0, MPR)
            cells.append(f"R={R}: {tt/lcoe(R0)-1:5.1%} / +{(wacc_equivalent(tt)-R0)*100:3.1f}pp")
            rows.append(["premium", lam, R, round(tt / lcoe(R0) - 1, 4), round((wacc_equivalent(tt) - R0) * 100, 2)])
        print(f"   lam={lam:4.2f}: " + "; ".join(cells))
    for D in [0.5, 2.0]:
        tt = tariff_with_risk(LAM, REC, D, R0, MPR)
        print(f"   D={D}: premium {tt/lcoe(R0)-1:.1%}, +{(wacc_equivalent(tt)-R0)*100:.1f}pp")
    tt = tariff_with_risk(LAM, REC, DELAY, R0, 1.0)
    print(f"   m=1 (expected loss only): premium {tt/lcoe(R0)-1:.1%}, +{(wacc_equivalent(tt)-R0)*100:.1f}pp")

    print("\n3. Contract vs debt guarantee (Proposition 2), 100 MW plant")
    t0, tc, td = tariff_no_guarantee(), tariff_contract_guarantee(), tariff_debt_guarantee()
    print(f"  tariff: none {t0:.2f}; contract guarantee {tc:.2f}; debt guarantee {td:.2f} c/kWh")
    sc = annual_revenue_musd(t0) - annual_revenue_musd(tc)
    sd = annual_revenue_musd(t0) - annual_revenue_musd(td)
    gc = guarantor_cost_contract()
    go, gx, debt0, ds = guarantor_cost_debt()
    print(f"  annual saving to offtaker: contract ${sc:.3f}m; debt ${sd:.3f}m")
    print(f"  guarantor expected annual cost: contract ${gc:.3f}m; debt ${go+gx:.3f}m "
          f"(offtaker-driven ${go:.3f}m, other risks ${gx:.3f}m)")
    print(f"  saving per $ of expected guarantor cost: contract {sc/gc:.1f}; debt {sd/(go+gx):.1f}")
    A = annual_revenue_musd(tc)
    print(f"  maximum exposure: debt guarantee ${debt0:.0f}m face at close (debt service ${ds:.2f}m/yr); "
          f"contract guarantee arrears per one-year episode ${A*DELAY:.2f}m")
    print(f"  ratio phi_Q(1-Rt)/[phi(1-Rt_G)] = "
          f"{haircut(LAM, REC, DELAY, R0, MPR)/(phi(LAM, DELAY)*(1-rtilde(REC_G, DELAY, R0, DELAY_G))):.1f}")
    rows += [["guarantee", "none", round(t0, 3)], ["guarantee", "contract", round(tc, 3), round(sc, 3), round(gc, 4)],
             ["guarantee", "debt", round(td, 3), round(sd, 3), round(go + gx, 4)]]

    print("\n4. Waterfall and liquidity (Proposition 3): regional facility, 2 GW")
    tariff = lcoe(R0)
    annual = REG_MW * 1000 * KWH_PER_KW * tariff / 100 / 1e6
    X = annual * DELAY  # arrears accumulated over an episode, if all offtakers default
    qs = [q for _, q in LAYERS[1:]]
    costs, fac = waterfall_expected_costs(LAM, annual, REC, DELAY, R0, qs)
    print(f"  annual contract payments ${annual:.0f}m; arrears if every offtaker is in a one-year episode ${X:.0f}m")
    print(f"  expected arrears funded per year ${phi(LAM, DELAY)*annual:.1f}m; unrecovered after offtaker "
          f"{1-rtilde(REC, DELAY, R0):.1%}")
    for (name, q), c in zip(LAYERS[1:], costs):
        print(f"   {name:28s} q={q:.2f}: expected ${c:.2f}m/yr ({c/annual:.2%} of payments)")
        rows.append(["waterfall", name, q, round(c, 3), round(c / annual, 5)])
    for no_donor in [False, True]:
        qs2 = qs[:-1] if no_donor else qs
        costs2, fac2 = waterfall_expected_costs(LAM, annual, REC, DELAY, R0, qs2)
        tag = "without donor account" if no_donor else "with donor account"
        print(f"   facility expected loss {tag}: ${fac2:.3f}m/yr ({fac2/annual:.3%} of payments)")
    print(f"   total expected cost to all layers: ${sum(costs):.2f}m/yr ({sum(costs)/annual:.2%} of payments)")
    print(f"   SECI-style margin of 2.4% of payments would be ${0.024*annual:.1f}m/yr")
    for p in [round(1 - exp(-LAM), 3), 0.05]:
        f = vasicek_quantile(p, REG_RHO, REG_CONF)
        B = f * annual * BRIDGE
        print(f"  Vasicek: p={p}, rho={REG_RHO}, {REG_CONF:.1%}: fraction in arrears {f:.0%}; "
              f"buffer to bridge {BRIDGE} yr ${B:.0f}m = {B/annual:.0%} of annual payments "
              f"(${B/REG_MW*1000:.0f}k per MW)")
        rows.append(["buffer", p, REG_RHO, round(f, 3), round(B, 1)])
    for rho in [0.1, 0.3, 0.5]:
        f = vasicek_quantile(round(1 - exp(-LAM), 3), rho, REG_CONF)
        print(f"   sensitivity rho={rho}: fraction {f:.0%}")

    print("\n5. Declining tariff with equal present value (r=8%)")
    p0 = solve_p0(0.08)
    path = declining_path(p0)
    nb = newbuild_path()
    print(f"  flat {FLAT} c/kWh for {TERM} yrs = declining from {p0:.2f} to {p0/2:.2f} by year {FALL_YEARS}")
    print(f"  year-10 tariff: flat {FLAT:.2f}, declining {path[9]:.2f}, new-build {nb[9]:.2f}")
    rem_flat = pv([FLAT] * (TERM - FALL_YEARS), 0.08)
    rem_dec = pv(path[FALL_YEARS:], 0.08)
    print(f"  value of remaining payments after year {FALL_YEARS} (c/kWh-yrs, PV at year 7): flat {rem_flat:.1f}; declining {rem_dec:.1f}")
    exc_flat = pv([FLAT - n for n in nb[FALL_YEARS:]], 0.08)
    exc_dec = pv([p - n for p, n in zip(path[FALL_YEARS:], nb[FALL_YEARS:])], 0.08)
    print(f"  of which above new-build cost: flat {exc_flat:.1f}; declining {exc_dec:.1f}")
    alt = declining_path(6.0)
    print(f"  check of older draft: 6c falling to 3c has PV {pv(alt,0.08):.1f} vs flat 5c {pv([FLAT]*TERM,0.08):.1f}")
    rows.append(["declining", round(p0, 3), round(p0 / 2, 3), round(rem_flat, 2), round(rem_dec, 2)])

    print("\n6. India: SECI trading margin vs the offtaker premium")
    # Rs 0.07/kWh trading margin and Rs 2.93/kWh weighted average PSA tariff (ICRA 2025)
    print(f"  SECI margin Rs 0.07 on Rs 2.93 = {0.07/2.93:.1%} of tariff")
    print(f"  WACC cut that pays for it: {0.07/2.93/ (dlcoe_dr(0.10)/lcoe(0.10)) * 100:.2f} pp "
          f"(elasticity at 10% WACC: {dlcoe_dr(0.10)/lcoe(0.10)/100:.3f} per pp)")

    kwh = 60e6 * KWH_PER_KW  # ~60 GW under SECI sale agreements, solar capacity factor (STYLIZED)
    h = haircut(LAM, REC, DELAY, R0, MPR)
    print(f"  stylized: 60 GW x {KWH_PER_KW:.0f} kWh/kW = {kwh/1e9:.0f} TWh/yr; central-case premium {h/(1-h):.1%} of Rs 2.93 "
          f"= Rs {2.93*h/(1-h):.2f}/kWh = Rs {kwh*2.93*h/(1-h)/1e7:,.0f} crore a year; SECI margin Rs {kwh*0.07/1e7:,.0f} crore")

    with open(HERE / "calibration_tables.csv", "w", newline="") as fh:
        csv.writer(fh).writerows(rows)


if __name__ == "__main__":
    main()
