"""Model and calibration for 'The Climate Investment Trust: Hold Capital, Lend Its Strength'.

Three pieces, matching the three propositions of the working paper:
  1. Buffer sizing: capital needed so that second-loss guarantee losses exhaust
     the buffer with probability no more than alpha in a year (one-factor model),
     and the lifetime incentive per donor dollar of a buffer fund vs a payout fund.
  2. Growth dynamics: trust capital with safe yield, guarantee fees, expected
     losses, running costs and a fee share of private co-investment returns.
  3. Allocation rule: base allocation plus an international feebate between
     beneficiary accounts; participation and feasibility checks.

All parameters are stylized unless a source is named in the working paper.
Run:  python3 model.py   (prints every number used in the working paper and the brief)
v0.3 (31 Oct 2026): carry, horizon and liquidity added to Proposition 1; growth reported with the
stress-case buffer held (peer review M1-M3). The v0.2 script is in ../8.PreviousVersions/model-v0.2.py.
"""
import numpy as np
from scipy.stats import norm

# ---------------------------------------------------------------- parameters
BASE = dict(
    n=20,          # number of equal-sized guaranteed sovereign programs (stylized)
    p=0.0077,      # annual prob. of a call: MDB sovereign default rate 1984-2024 (GEMs 2025)
    rho=0.20,      # asset correlation in the one-factor model (stylized)
    L=0.049,       # loss given call: 1 - 95.1% MDB sovereign recovery (GEMs 2025)
    alpha=0.01,    # target annual probability that the buffer is exhausted
    s=0.03,        # spread saved by the borrower on guaranteed debt (stylized)
    f=0.0,         # guarantee fee charged on exposure, per year
    r_s=0.04,      # yield on the buffer's safe assets (stylized)
    c=0.005,       # running costs, share of capital per year (stylized)
    K0=5.0,        # trust capital at launch, $bn: $1bn donor grants + $4bn country stakes
    E_p=95.0,      # private equity co-invested through the investment function, $bn
    r_e=0.10,      # gross return on construction-stage equity (one assumption, see paper)
    phi=0.25,      # fee: share of private investment returns paid to the trust
    i_L=0.05,      # rate on the policy loans that finance country stakes (stylized)
)


# Loss cases (settled 29 Oct 2026). BASE uses the MDB record, which reflects
# preferred-creditor status a new facility might not inherit; hence the cases
# below. Same n, rho and alpha in every case.
CASES = {
    "base (MDB record)": (0.0077, 0.049),
    "middle (3% x 10%)": (0.03, 0.10),
    "stress (3% x 37%)": (0.03, 0.37),   # Cruces and Trebesch (2013) haircut
}


# ---------------------------------------------------------- 1. buffer sizing
def vasicek_quantile(p, rho, alpha):
    """Large-portfolio default rate exceeded with probability alpha."""
    return norm.cdf((norm.ppf(p) + np.sqrt(rho) * norm.ppf(1 - alpha)) / np.sqrt(1 - rho))


def buffer_ratio_mc(n, p, rho, L, alpha, sims=400_000, seed=1):
    """Buffer as a share of exposure (b = B/G) so that P(loss > B) <= alpha,
    for n equal exposures, by Monte Carlo of the one-factor model."""
    rng = np.random.default_rng(seed)
    z = rng.standard_normal(sims)
    cond_p = norm.cdf((norm.ppf(p) - np.sqrt(rho) * z) / np.sqrt(1 - rho))
    defaults = rng.binomial(n, cond_p)
    loss_share = L * defaults / n
    return float(np.quantile(loss_share, 1 - alpha))


def buffer_ratio_large(p, rho, L, alpha):
    return L * vasicek_quantile(p, rho, alpha)


def incentive_per_donor_dollar(s, lam, f=0.0, carry=0.0, b=0.0):
    """Present value of spread savings delivered per dollar of donor capital held
    as a buffer (Proposition 1b). carry = donors' discount rate minus the buffer's
    net yield; with carry = 0 the result is (s - f)/(lam - f) and does not depend on b.
    A payout fund delivers exactly 1. Infinite if fees cover expected loss at zero carry."""
    denom = lam - f + carry * b
    if denom <= 0:
        return np.inf
    return (s - f) / denom


def horizon_value(s, lam, b, T, f=0.0, net_yield=0.035, disc=0.035):
    """Spread savings to year T per dollar held, and the discounted capital left at T
    (exposure kept at K/b; capital earns net_yield; flows discounted at disc)."""
    r = (lam - f) / b - net_yield + disc
    inc = ((s - f) / b) * (1 - np.exp(-r * T)) / r
    return inc, np.exp(-r * T)


def debt_service_share(rate=0.05, years=10):
    """One year's payment on an amortizing loan, as a share of principal."""
    return rate / (1 - (1 + rate) ** -years)


def liquidity_buffer(n, p, rho, L, alpha, m, **kw):
    """Buffer when each call costs m of the program in cash before recovery and L in the end:
    the quantile number of calls k times max(L, m)/n (Proposition 1d)."""
    b = buffer_ratio_mc(n, p, rho, L, alpha, **kw)
    k = round(b * n / L)
    return max(b, k * m / n)


# ------------------------------------------------------ 2. growth dynamics
def capital_path(T=30, K0=5.0, E_p=95.0, r_e=0.10, phi=0.25, r_s=0.04, c=0.005,
                 lam=0.0111, f=0.0, b=0.08, contributions=0.0):
    """Trust capital each year. Exposure is kept at G = K/b."""
    K = [K0]
    for _ in range(T):
        k = K[-1]
        G = k / b
        dk = r_s * k - c * k + (f - lam) * G + phi * r_e * E_p + contributions
        K.append(max(k + dk, 0.0))
    return np.array(K)


def steady_state_capital(E_p, r_e, phi, r_s, c, lam, f, b, g=0.0):
    """K* where growth equals g (Proposition 2), if the net burn rate is positive."""
    burn = g + c + (lam - f) / b - r_s
    return np.inf if burn <= 0 else phi * r_e * E_p / burn


# ------------------------------------------------------ 3. allocation rule
def allocations(e, Y, tau, base_total, leave_one_out=False):
    """Allocation to each beneficiary account: equal base share plus an
    international feebate tau*(ebar - e_i)*Y_i (tonnes = intensity x output)."""
    e, Y = np.asarray(e, float), np.asarray(Y, float)
    N = len(e)
    if leave_one_out:
        ebar = np.array([(np.dot(e, Y) - e[i] * Y[i]) / (Y.sum() - Y[i]) for i in range(N)])
    else:
        ebar = np.dot(e, Y) / Y.sum()
    feebate = tau * (ebar - e) * Y
    return base_total / N + feebate, feebate


def max_feasible_tau(e, Y, balances):
    """Highest feebate rate at which no deduction exceeds an account balance."""
    e, Y, balances = map(lambda x: np.asarray(x, float), (e, Y, balances))
    ebar = np.dot(e, Y) / Y.sum()
    owed = (e - ebar) * Y           # tonnes above benchmark (positive = pays)
    mask = owed > 0
    return float(np.min(balances[mask] / owed[mask]))


# ------------------------------------------------------------------ tables
def main():
    P = BASE
    lam = P["p"] * P["L"]
    b_mc = buffer_ratio_mc(P["n"], P["p"], P["rho"], P["L"], P["alpha"])
    b_inf = buffer_ratio_large(P["p"], P["rho"], P["L"], P["alpha"])
    B = {name: buffer_ratio_mc(20, p, 0.2, L, 0.01) for name, (p, L) in CASES.items()}
    LAM = {name: p * L for name, (p, L) in CASES.items()}
    b_st = B["stress (3% x 37%)"]
    print("== Proposition 1: buffer sizing (base case) ==")
    print(f"expected loss rate lambda = p*L = {lam:.5f}")
    print(f"buffer ratio b, n={P['n']}: {b_mc:.4f}  (leverage {1/b_mc:.1f}x)")
    print(f"buffer ratio b, large n: {b_inf:.4f}  (leverage {1/b_inf:.1f}x)")
    print(f"exposure supported by $5bn: {P['K0']/b_mc:.0f} $bn")
    print("\nBuffer ratio table by case (n=20, alpha=1%), % of exposure:")
    print("case                 rho=0.1  rho=0.2  rho=0.3  rho=0.4  | large n rho=0.2")
    for name, (p, L) in CASES.items():
        row = [buffer_ratio_mc(20, p, r, L, 0.01) for r in (0.1, 0.2, 0.3, 0.4)]
        print(f"{name:20s} " + "   ".join(f"{100*x:.2f}" for x in row)
              + f"  | {100*buffer_ratio_large(p, 0.2, L, 0.01):.2f}")
    print("\nalpha=0.5%, by case:", [round(buffer_ratio_mc(20, p, 0.2, L, 0.005), 4) for p, L in CASES.values()])

    print("\nIncentive per donor dollar (payout fund = 1), exposure and savings per $5bn:")
    for name in CASES:
        l, b = LAM[name], B[name]
        print(f"  {name}: EL={l*100:.4f}%  no fee {incentive_per_donor_dollar(P['s'], l):.1f}; "
              f"fee=EL/2 {incentive_per_donor_dollar(P['s'], l, l/2):.1f}; "
              f"carry 0.5% {incentive_per_donor_dollar(P['s'], l, carry=0.005, b=b):.1f}; "
              f"carry 2% {incentive_per_donor_dollar(P['s'], l, carry=0.02, b=b):.1f}; "
              f"b={b*100:.2f}% -> $5bn supports ${5/b:,.0f}bn, saving ${P['s']*5/b:.1f}bn/yr; "
              f"expected loss ${l*5/b:.2f}bn/yr")
    print("  record losses, stress buffer held: carry 0 "
          f"{incentive_per_donor_dollar(P['s'], lam):.1f}; carry 0.5% "
          f"{incentive_per_donor_dollar(P['s'], lam, carry=0.005, b=b_st):.1f}; carry 2% "
          f"{incentive_per_donor_dollar(P['s'], lam, carry=0.02, b=b_st):.1f}")
    print("\nSavings to 2050 (25 years) per dollar held, and capital left (PV), zero carry:")
    for name in CASES:
        inc, left = horizon_value(P["s"], LAM[name], B[name], 25)
        print(f"  {name}: {inc:.1f}; capital left {left:.2f}")
    inc, left = horizon_value(P["s"], lam, b_st, 25)
    print(f"  record losses, stress buffer held: {inc:.1f}; capital left {left:.2f}")

    m = debt_service_share()
    print(f"\nProposition 1(d), liquidity: a call costs one year's debt service, m = {m:.4f} of the program")
    for name, (p, L) in CASES.items():
        bc = liquidity_buffer(20, p, 0.2, L, 0.01, m)
        print(f"  {name}: buffer {B[name]*100:.2f}% -> with cash calls {bc*100:.2f}%; $5bn supports ${5/bc:,.0f}bn")

    print("\n== Proposition 2: growth ==")
    fee_income = P["phi"] * P["r_e"] * P["E_p"]
    print(f"fee income on private equity: {fee_income:.3f} $bn/yr")
    for name in ("base (MDB record)", "stress (3% x 37%)"):
        l, b = LAM[name], B[name]
        print(f"  {name}, own buffer: f_min = {l - b*(P['r_s']-P['c']):.5f} ({(l - b*(P['r_s']-P['c']))/l:.0%} of EL); "
              f"no-fee burn {l/b - (P['r_s']-P['c']):.3f}")
    print(f"  record losses, stress buffer: net growth with no fee {(P['r_s']-P['c']) - lam/b_st:.4f}; "
          f"f_min {lam - b_st*(P['r_s']-P['c']):.4f}")
    print("Capital paths, stress-case buffer held (exposure = K/0.0925), no guarantee fee:")
    for lab, l in (("record losses", lam), ("stress losses", LAM["stress (3% x 37%)"])):
        for E_p in (95, 10, 0):
            path = capital_path(T=25, K0=P["K0"], E_p=E_p, lam=l, f=0.0, b=b_st)
            ks = steady_state_capital(E_p, P["r_e"], P["phi"], P["r_s"], P["c"], l, 0.0, b_st)
            print(f"  {lab:14s} private ${E_p:>3}bn: K1={path[1]:.2f} K10={path[10]:.1f} K25={path[25]:.1f} "
                  f"K*={ks:.1f}; exposure at 25y ${path[25]/b_st:,.0f}bn")
    print("For comparison (v0.2), full leverage on the record, $95bn private, no fee:")
    path = capital_path(T=25, K0=P["K0"], E_p=95, lam=lam, f=0.0, b=b_mc)
    ks = steady_state_capital(95, P["r_e"], P["phi"], P["r_s"], P["c"], lam, 0.0, b_mc)
    print(f"  K10={path[10]:.1f} K*={ks:.1f}; exposure at K* ${ks/b_mc:,.0f}bn")
    g0 = (P["r_s"] - P["c"] - lam / b_st) + fee_income / P["K0"]
    print(f"initial growth (stress buffer, record losses, $95bn): {g0:.3f}")
    carry = (P["i_L"] - P["r_s"]) * 4.0
    print(f"carrying cost of $4bn borrowed country stakes: {carry*1000:.0f} $m/yr in total, "
          f"{carry*100:.0f} $m per country of ten")

    print("\n== Proposition 3: allocation (stylized 10-country power sector) ==")
    e = np.linspace(0.3, 0.9, 10)      # tCO2/MWh
    Y = np.full(10, 200e6)             # MWh a year (200 TWh each)
    base_total = 1.0e9                 # base allocation $1bn a year, $0.1bn per country
    for tau in (10, 25):
        A, fb = allocations(e, Y, tau, base_total=base_total)
        print(f"  tau=${tau}/t: feebate sum={fb.sum():.0f}; max deduction ${-fb.min()/1e9:.2f}bn")
    owed_max = (e.max() - np.dot(e, Y) / Y.sum()) * Y[0]
    carry_i = (P["i_L"] - P["r_s"]) * 0.4e9
    print(f"  most intensive country {owed_max/1e6:.0f} Mt above benchmark; carry per country ${carry_i/1e6:.0f}m")
    for name in CASES:
        Vc = P["s"] * (P["K0"] / B[name]) / 10
        print(f"    {name} buffer: V_i ${Vc*1000:.0f}m/yr; participation tau max "
              f"${(base_total/10 + Vc*1e9 - carry_i)/owed_max:.1f}/t")
    for K in (5, 18.5, 28, 34):
        bal = np.full(10, K * 1e9 / 10)
        print(f"  trust ${K}bn split equally: max feasible tau = ${max_feasible_tau(e, Y, bal):.0f}/t")


if __name__ == "__main__":
    main()
