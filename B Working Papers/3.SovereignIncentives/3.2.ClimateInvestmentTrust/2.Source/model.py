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
Run:  python3 model.py   (prints the tables used in the paper)
"""
import numpy as np
from scipy.stats import norm

# ---------------------------------------------------------------- parameters
BASE = dict(
    n=20,          # number of equal-sized guaranteed sovereign programs (stylized)
    p=0.03,        # annual prob. a government fails to honour its first-loss indemnity (stylized)
    rho=0.20,      # asset correlation in the one-factor model (stylized)
    L=0.37,        # loss given call; average sovereign haircut, Cruces and Trebesch (2013)
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


def incentive_per_donor_dollar(s, lam, f=0.0):
    """Present value of spread savings delivered per dollar of donor capital held
    as a buffer, discounting at the buffer's own safe yield (Proposition 1b).
    A payout fund delivers exactly 1. Infinite if fees cover expected loss."""
    if lam - f <= 0:
        return np.inf
    return (s - f) / (lam - f)


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
    print("== Proposition 1: buffer sizing (base case) ==")
    print(f"expected loss rate lambda = p*L = {lam:.4f}")
    print(f"buffer ratio b, n={P['n']}: {b_mc:.4f}  (leverage {1/b_mc:.1f}x)")
    print(f"buffer ratio b, large n: {b_inf:.4f}  (leverage {1/b_inf:.1f}x)")
    print(f"exposure supported by $5bn: {P['K0']/b_mc:.0f} $bn")
    print("\nBuffer ratio table (n=20, L=0.37, alpha=1%):")
    print("p      rho=0.1  rho=0.2  rho=0.3")
    for p in (0.01, 0.03, 0.05):
        row = [buffer_ratio_mc(20, p, r, 0.37, 0.01) for r in (0.1, 0.2, 0.3)]
        print(f"{p:.2f}   " + "   ".join(f"{x:.3f}" for x in row))
    print("\nalpha=0.5%, base:", round(buffer_ratio_mc(20, 0.03, 0.2, 0.37, 0.005), 4))
    print("L=0.10, base:", round(buffer_ratio_mc(20, 0.03, 0.2, 0.10, 0.01), 4))
    print("\nIncentive per donor dollar (payout fund = 1):")
    for L in (0.37, 0.10):
        for f_share in (0.0, 0.5):
            lamL = P["p"] * L
            print(f"  L={L:.2f} fee={f_share:.0%} of EL: "
                  f"{incentive_per_donor_dollar(P['s'], lamL, f_share*lamL):.1f}")

    print("\n== Proposition 2: growth ==")
    fee_income = P["phi"] * P["r_e"] * P["E_p"]
    print(f"fee income on private equity: {fee_income:.2f} $bn/yr")
    for label, E_p, f in (("book scale, no fee", 95, 0.0), ("book scale, fee=EL/2", 95, lam / 2),
                          ("modest private, no fee", 10, 0.0), ("no private, fee=EL/2", 0, lam / 2)):
        path = capital_path(T=25, K0=P["K0"], E_p=E_p, lam=lam, f=f, b=b_mc)
        kstar = steady_state_capital(E_p, P["r_e"], P["phi"], P["r_s"], P["c"], lam, f, b_mc)
        print(f"  {label:24s} K1={path[1]:.2f} K10={path[10]:.1f} K25={path[25]:.1f} K*={kstar:.1f}")
    g0 = (P["r_s"] - P["c"] - lam / b_mc) + fee_income / P["K0"]
    print(f"initial growth rate (book scale, no fee): {g0:.3f}; doubling {np.log(2)/np.log(1+g0):.1f} yrs")
    f_min = lam - b_mc * (P["r_s"] - P["c"])
    print(f"insurance-only phase: fee needed for zero growth f_min = {f_min:.4f} "
          f"({f_min/lam:.0%} of EL); incentive left s - f_min = {P['s']-f_min:.4f}")
    print(f"spread savings delivered by $5bn buffer: {P['s']*P['K0']/b_mc:.2f} $bn/yr")
    carry = (P["i_L"] - P["r_s"]) * 4.0
    print(f"carrying cost of $4bn borrowed country stakes: {carry*1000:.0f} $m/yr")

    print("\n== Proposition 3: allocation (stylized 10-country power sector) ==")
    e = np.linspace(0.3, 0.9, 10)      # tCO2/MWh
    Y = np.full(10, 200e6)             # MWh a year (200 TWh each)
    for tau in (10, 25):
        A, fb = allocations(e, Y, tau, base_total=1.0e9)
        print(f"  tau=${tau}/t: feebate sum={fb.sum():.0f}; min alloc ${A.min()/1e9:.2f}bn; max ${A.max()/1e9:.2f}bn")
    A, fb = allocations(e, Y, 10, base_total=1.0e9, leave_one_out=True)
    print(f"  leave-one-out benchmark, tau=$10/t: feebate sum=${fb.sum()/1e9:.3f}bn (not exactly zero)")
    owed_max = (e.max() - np.dot(e, Y) / Y.sum()) * Y[0]
    V_i = P["s"] * (P["K0"] / b_mc) / 10
    print(f"  dirtiest country owes {owed_max/1e6:.0f} Mt above benchmark; "
          f"guarantee incentive per country ${V_i*1000:.0f}m/yr; "
          f"participation tau max with base $0.1bn: ${(0.1e9 + V_i*1e9 - 4e7)/owed_max:.1f}/t")
    for K in (5, 28):
        bal = np.full(10, K * 1e9 / 10)
        print(f"  trust ${K}bn split equally: max feasible tau = ${max_feasible_tau(e, Y, bal):.0f}/t")


if __name__ == "__main__":
    main()
