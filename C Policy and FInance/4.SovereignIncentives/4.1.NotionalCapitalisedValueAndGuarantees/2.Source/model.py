"""Model and calibration for working paper 4.1 (Reward the Stock as Well as the Flow:
notional capitalized value and guarantee-based climate incentives).

Run:  python3 model.py        (prints every number used in the paper and brief)

Notation (as in the paper)
  B_t     notional capitalized value (balance), $
  S_0     carbon stock at entry, tCO2
  p_s     stock price: $ of opening balance per tCO2 of stock
  p_e     debit price: $ debited per tCO2 emitted (credited per tCO2 below the allowance)
  A_t     allowance (benchmark path), tCO2/yr
  E_t     emissions, tCO2/yr (fossil plus land use)
  lam_t   capacity ratio: guarantee capacity per $ of balance
  G_t     guarantee capacity = lam_t * B_t, capped by eligible green borrowing D
  ds      spread saved per $ of guaranteed exposure per year
  EL      guarantor's expected loss per $ of exposure per year = PD * LGD
  k       buffer held per $ of exposure;  phi = net annual carry cost of the buffer
  r       discount rate;  theta = decay rate of the capacity ratio

Sources for the anchored numbers are given beside each one. Everything marked
STYLIZED is an assumption chosen for illustration.
"""
from __future__ import annotations

import math

import numpy as np

# ----------------------------------------------------------------------------
# Anchored parameters
# ----------------------------------------------------------------------------
# GEMs consortium (EIB press release, 7 Oct 2025): sovereign and sovereign-
# guaranteed lending by MDBs, 1984-2024: average annual default rate 0.77%,
# average recovery 95.1%.
PD_GEMS = 0.0077
LGD_GEMS = 1 - 0.951
EL_GEMS = PD_GEMS * LGD_GEMS            # 0.038% a year

# IBRD policy minimum equity-to-loans ratio: 18%, lowered from 19% (World Bank press
# release, 15 Oct 2024). Used only for the capital-charge sensitivity.
K_IBRD = 0.18

# Series cases shared with working papers 4.2 (Climate Investment Trust) and
# 4.3 (sustainability-linked lending). Settled 29 Oct 2026: the MDB record is the
# base case; the Cruces-Trebesch case is the stress test.
#   BASE (MDB record): annual call probability 0.77% and loss per call 4.9%
#     (GEMs 1984-2024 default and recovery rates on MDB sovereign and
#     sovereign-guaranteed lending; they reflect preferred-creditor status).
#   MIDDLE: 3% annual calls, 10% loss per call.
#   STRESS: 3% annual calls, 37% loss per call (average sovereign haircut,
#     Cruces and Trebesch 2013).
# In every case: 20 guaranteed programs, asset correlation 0.2, buffer sized so
# the annual probability of exhaustion is 1%. Buffer ratios come from the Monte
# Carlo in 4.2.ClimateInvestmentTrust/2.Source/model.py: 0.49% (two calls of
# 4.9% across 20 programs), 2.5% and 9.25% (rounded to 9.3% in the text).
EL_SERIES = 0.03 * 0.37               # stress case, 1.11% a year
K_SERIES = 0.093
EL_MID, K_MID = 0.03 * 0.10, 0.025
K_GEMS = 0.0049
CASES = {"MDB record (base)": (EL_GEMS, K_GEMS),
         "10% loss per call (middle)": (EL_MID, K_MID),
         "3% calls x 37% loss (stress)": (EL_SERIES, K_SERIES)}

# Gabon blue bond, Aug 2023: 6.097% coupon (AfSDJN 2023), 200 bp over US Treasuries,
# rated Aa2 with DFC political risk insurance against the sovereign's Caa1/B; Gabon's
# 2031 eurobonds yielding about 10% (Smith 2023, M&G Bond Vigilantes).
GABON_GUARANTEED = 6.097
GABON_MARKET = (10.0,)

# Share of sovereign credit spreads that is a risk premium rather than expected
# default loss: about a third (Longstaff, Pan, Pedersen and Singleton 2011).
RP_SHARE = 1 / 3

# Guyana LCDS 2030: forests store 19.5 GtCO2e on about 18 million hectares.
GUY_STOCK = 19.5e9
GUY_AREA = 18e6

# Guyana-Hess: at least $750m for 37.5 million ART-TREES credits (2016-2030).
HESS_USD, HESS_T = 750e6, 37.5e6

# TFFF: about $4 per hectare a year; deduction of 100x ($400) per hectare
# deforested at low deforestation rates and 200x ($800) at higher rates.
TFFF_PER_HA = 4.0
TFFF_PENALTY = (400.0, 800.0)

# Indonesia proved coal reserves, end-2020 (bp Statistical Review 2021), Mt:
# anthracite and bituminous 23,141; sub-bituminous and lignite 11,728.
IDN_BIT, IDN_SUB = 23_141e6, 11_728e6
# IPCC (2006) Vol. 2 ch. 1 defaults: other bituminous 25.8 GJ/t x 94.6 kgCO2/GJ;
# sub-bituminous 18.9 GJ/t x 96.1 kgCO2/GJ (applied to lignite too: an overstatement).
EF_BIT = 25.8 * 94.6 / 1000
EF_SUB = 18.9 * 96.1 / 1000

# ----------------------------------------------------------------------------
# STYLIZED baseline
# ----------------------------------------------------------------------------
DS = 0.03        # spread saved, close to Gabon and to Time and Chance ch. 21
R = 0.05         # discount rate
PHI = 0.0        # net carry cost of buffer: zero when the buffer earns the rate used to discount (as in 3.2)
K = K_GEMS       # buffer per $ of exposure (base case: MDB record)
EL = EL_GEMS     # guarantor's expected loss per $ of exposure a year (base case: MDB record)
D_FOREST = 5e9   # eligible green borrowing of the forest country (outstanding)
P_E = 50.0       # debit price, $/tCO2


def annuity(T: float, r: float = R) -> float:
    """Present value of $1 a year for T years."""
    return (1 - (1 + r) ** -T) / r


def cost_rate(el: float = EL, k: float = K, phi: float = PHI) -> float:
    """Annual economic cost to the guarantor per $ of exposure."""
    return el + k * phi


def ratio(ds: float = DS, el: float = EL, k: float = K, phi: float = PHI,
          fee: float = 0.0) -> float:
    """Proposition 1: incentive value / guarantor cost."""
    return (ds - fee) / (el + k * phi - fee)


def econ_ratio(ds: float = DS, el: float = EL, rp_share: float = RP_SHARE) -> float:
    """Proposition 1(b): economic value / guarantor cost when the country gives up its
    default option: value = risk premium + guarantor's expected loss."""
    return (rp_share * ds + el) / el


def dp_factor(sigma: float, r: float = R) -> float:
    """Dixit-Pindyck trigger multiplier beta/(beta-1) for a cost following a driftless
    random walk with a deterministic benefit (payout rate delta = r)."""
    a = 0.5 * sigma ** 2
    beta = (a + math.sqrt(a * a + 4 * a * r)) / (2 * a)
    return beta / (beta - 1)


def cpe(p_e: float, ds: float = DS, r: float = R, theta: float = 0.0, lam: float = 1.0) -> float:
    """Proposition 2: carbon-price equivalent of the debit, $/tCO2 at entry."""
    return lam * p_e * ds / (r + theta)


def p_e_needed(m0: float, ds: float = DS, r: float = R, theta: float = 0.0, lam: float = 1.0) -> float:
    return m0 * (r + theta) / (lam * ds)


# ----------------------------------------------------------------------------
# Balance dynamics
# ----------------------------------------------------------------------------
def balance_path(B0, p_e, A, E):
    """B_{t+1} = max(B_t + p_e (A_t - E_t), 0)."""
    B = [B0]
    for a, e in zip(A, E):
        B.append(max(B[-1] + p_e * (a - e), 0.0))
    return np.array(B)


YEARS = np.arange(2027, 2051)
N = len(YEARS)
# STYLIZED forest-country emissions (fossil plus land use), MtCO2/yr
A_PATH = np.linspace(12e6, 0.0, N)          # allowance falls to zero in 2050
E_BAU = np.full(N, 15e6)                     # business as usual
E_ACT = np.maximum(15e6 - 1.2e6 * np.arange(N), 3e6)  # acts now: 15 -> 3 Mt by 2037


def early_action(K0, dE, g, m0, m_inf=0.0, b=0.0, omega=0.0, theta=None, r=R, horizon=200):
    """Net value W(tau) of adopting at tau, Proposition 3. Returns (taus, W)."""
    if theta is None:
        theta = g
    taus = np.linspace(0, 30, 301)
    s = np.linspace(0, horizon, 20001)
    ds_ = s[1] - s[0]
    m = m_inf + (m0 - m_inf) * np.exp(-theta * s)
    flow = dE * (m + b - omega) * np.exp(-r * s)
    tail = np.cumsum(flow[::-1])[::-1] * ds_          # integral from s to horizon
    W = np.interp(taus, s, tail) - K0 * np.exp(-(r + g) * taus)
    return taus, W


def main():
    print("=== Proposition 1: incentive-to-cost ratio ===")
    for name, (el, k) in CASES.items():
        print(f"{name}: EL = {el*100:.4f}%, buffer {k*100:.2f}% -> R = {ratio(el=el, k=k):.1f}; "
              f"R with 2% carry = {ratio(el=el, k=k, phi=0.02):.1f}; $5bn supports ${5/k:,.0f}bn")
    print(f"MDB record with IBRD-style 18% capital at 2% carry: R = {ratio(el=EL_GEMS, k=K_IBRD, phi=0.02):.1f}")
    print(f"priced on the record, stress-case buffer held at 2% carry: R = {ratio(el=EL_GEMS, k=K_SERIES, phi=0.02):.1f}; "
          f"extra carry on $3.1bn stress buffer: ${3.1e9*0.02/1e6:.0f}m a year")
    for name, (el, k) in CASES.items():
        print(f"  economic value (risk premium {RP_SHARE*DS*100:.1f} pp + EL) / cost, {name}: {econ_ratio(el=el):.1f}")
    for ds in (0.015, 0.03, 0.045):
        print(f"  ds={ds*100:.1f}%: R base={ratio(ds=ds):.0f}, stress={ratio(ds=ds, el=EL_SERIES, k=K_SERIES):.1f}")
    print(f"donor cost per $ of carbon-price equivalent: base {cost_rate()/DS*100:.2f} cents; stress {EL_SERIES/DS*100:.0f} cents")
    print(f"break-even EL (R=1): {(DS - K*PHI)*100:.1f}%")
    print(f"leverage of buffer: {1/K:.1f}x; $5bn supports ${5/K:.0f}bn")
    print(f"Gabon saving against its 2031 bonds: about {GABON_MARKET[0]-GABON_GUARANTEED:.1f} pp (gross of the insurance premium)")
    fee = cost_rate()
    print(f"cost-covering fee {fee*100:.2f}%: country keeps {(DS-fee)*100:.2f}% a year")

    print("\n=== Time and Chance ch. 21: three readings ===")
    nccv, rel, s = 10e9, 1e9, 0.03
    # A: $1bn cap on outstanding exposure for 10 years
    print(f"A cap $1bn, 10y: {rel*s/1e6:.0f}m/yr, {rel*s*10/1e6:.0f}m total; PV {rel*s*annuity(10)/1e6:.0f}m")
    # B: $1bn of new 10-year bullet guarantees a year for 10 years
    out = np.array([min(t + 1, 10) for t in range(10)]) * rel  # outstanding in years 1..10
    tot_B = 10 * rel * s * 10
    pv_B = sum(rel * s * annuity(10) / (1 + R) ** t for t in range(10))
    print(f"B flow $1bn/yr new 10y loans: year-10 saving {out[-1]*s/1e6:.0f}m/yr; lifetime {tot_B/1e9:.1f}bn; PV {pv_B/1e9:.2f}bn")
    # C: full $10bn as cap
    print(f"C cap $10bn: {nccv*s/1e6:.0f}m/yr; {nccv*s*10/1e9:.1f}bn over 10y; PV {nccv*s*annuity(10)/1e9:.2f}bn")
    # Marginal effect of 1 Mt at $100/t under C: lose $100m capacity for remaining 9 years
    print(f"C: CPE of the debit with 9 years left: ${100*s*annuity(9):.0f}/t; under A: $0/t (cap slack)")

    print("\n=== Forest country, Guyana-scale stock ===")
    dens = GUY_STOCK / GUY_AREA
    p_s = D_FOREST / GUY_STOCK
    print(f"density {dens:.0f} tCO2e/ha; p_s to size balance at ${D_FOREST/1e9:.0f}bn: ${p_s:.3f}/t")
    print(f"balance at $100/t on whole stock: ${GUY_STOCK*100/1e12:.2f}tn")
    tau = cpe(P_E)
    print(f"CPE at p_e=${P_E:.0f}: ${tau:.0f}/t; per ha deforested ${tau*dens:,.0f}")
    print(f"CPE if the scheme ends in 2050, tonne emitted in 2027 (23 years of lost capacity): ${P_E*DS*annuity(23):.0f}/t; "
          f"in 2040: ${P_E*DS*annuity(10):.0f}/t")
    print(f"single-price NCV (p_e=p_s) CPE: ${cpe(p_s):.2f}/t")
    print(f"annual incentive at full capacity ${D_FOREST*DS/1e6:.0f}m; PV 20y ${D_FOREST*DS*annuity(20)/1e9:.2f}bn")
    print(f"buffer held ${K*D_FOREST/1e9:.2f}bn; annual donor cost ${cost_rate()*D_FOREST/1e6:.1f}m")
    print(f"donor cost per tonne of CPE: ${tau*cost_rate()/DS:.2f}/t")
    for name, (el, k) in CASES.items():
        print(f"  {name}: buffer ${k*D_FOREST/1e9:.3f}bn; annual cost ${el*D_FOREST/1e6:.1f}m; cost per tonne ${tau*el/DS:.2f}")
    print(f"Hess average price ${HESS_USD/HESS_T:.0f}/t; ~${HESS_USD/15/1e6:.0f}m a year over 15 years")
    print(f"TFFF: ${TFFF_PER_HA/dens*1000:.1f} per kt per year -> capitalized at 5%: ${TFFF_PER_HA/dens/R:.3f}/t")
    print(f"TFFF penalty per tonne: ${TFFF_PENALTY[0]/dens:.2f}-{TFFF_PENALTY[1]/dens:.2f}/t")

    Bb = balance_path(D_FOREST, P_E, A_PATH, E_BAU)
    Ba = balance_path(D_FOREST, P_E, A_PATH, E_ACT)
    zero = YEARS[np.argmax(Bb[1:] <= 0)] if (Bb[1:] <= 0).any() else None
    print(f"BAU balance exhausted in {zero}; action balance 2035 ${Ba[9]/1e9:.2f}bn, 2050 ${Ba[-1]/1e9:.2f}bn")
    print(f"cumulative incentive value 2027-50 (undiscounted): BAU ${DS*np.minimum(Bb[:-1],D_FOREST).sum()/1e9:.2f}bn; act ${DS*np.minimum(Ba[:-1],D_FOREST).sum()/1e9:.2f}bn")
    pvb = sum(DS * min(b, D_FOREST) / (1 + R) ** t for t, b in enumerate(Bb[:-1]))
    pva = sum(DS * min(b, D_FOREST) / (1 + R) ** t for t, b in enumerate(Ba[:-1]))
    print(f"PV incentive 2027-50: BAU ${pvb/1e9:.2f}bn; act ${pva/1e9:.2f}bn; gain from acting ${(pva-pvb)/1e9:.2f}bn")

    print("\n=== Scale: what a big incentive needs (ds=3%) ===")
    for target in (0.1e9, 0.5e9, 1e9, 5e9):
        G = target / DS
        print(f"incentive ${target/1e9:.1f}bn/yr: capacity ${G/1e9:.0f}bn; PV20 value ${target*annuity(20)/1e9:.1f}bn")
        for name, (el, k) in CASES.items():
            print(f"    {name}: buffer ${k*G/1e9:.2f}bn; donor cost ${el*G/1e6:.1f}m/yr")
    print("\n=== Coal variant, Indonesia-scale reserves ===")
    co2 = IDN_BIT * EF_BIT + IDN_SUB * EF_SUB
    print(f"factors {EF_BIT:.2f}, {EF_SUB:.2f} tCO2/t; reserves ~{co2/1e9:.0f} GtCO2")
    print(f"whole stock at $1/t: ${co2/1e9:.0f}bn")
    retire = 2e9 * EF_BIT
    for ds in (0.01, 0.03):
        G = retire * 1.0
        print(f"retire 2 Gt coal ({retire/1e9:.1f} GtCO2) at p_r=$1/t -> capacity ${G/1e9:.1f}bn; ds={ds*100:.0f}% -> ${G*ds/1e6:.0f}m/yr; CPE factor {ds/R:.1f}")

    print("\n=== Proposition 3: early action (energy reform) ===")
    K0, dE, g = 1e9, 5e6, 0.05
    m0 = (R + g) * K0 / dE
    f15, f20 = dp_factor(0.15), dp_factor(0.20)
    print(f"minimum m0 = (r+g)K0/dE = ${m0:.0f}/t; option-value multiplier {f15:.2f}-{f20:.2f} (volatility 15-20%): "
          f"${f15*m0:.0f}-{f20*m0:.0f}/t")
    for th in (0.0, g):
        print(f"theta={th:.2f}: p_e needed ${p_e_needed(m0, theta=th):.0f}/t; donor PV cost base ${dE*m0/(R+th)*cost_rate()/DS/1e6:.1f}m, "
              f"stress ${dE*m0/(R+th)*EL_SERIES/DS/1e6:.0f}m; same incentive as cash ${dE*m0/(R+th)/1e6:.0f}m")
    taus, W = early_action(K0, dE, g, m0 * 1.0)
    print(f"W(0)={W[0]/1e6:.0f}m, argmax tau={taus[np.argmax(W)]:.1f}")
    taus, W = early_action(K0, dE, g, m0 * 0.6)
    print(f"with 60% of m0: argmax tau={taus[np.argmax(W)]:.1f}")
    print(f"no incentive, b=0: hurdle met? {0 >= m0}")
    b = 5.0   # illustrative co-benefit, $/t, to show adoption is delayed rather than never
    print(f"no incentive, co-benefit $5/t: adopts at T* = ln((r+g)K0/(dE b))/g = {math.log((R+g)*K0/(dE*b))/g:.0f} years")


if __name__ == "__main__":
    main()
