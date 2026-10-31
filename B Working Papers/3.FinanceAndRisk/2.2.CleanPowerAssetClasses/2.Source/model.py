"""Model and calibration for 'From Projects to Asset Classes' (paper 2.2).

Run:  python3 model.py          (prints every table used in the paper and brief)

Three pieces:
  1. LCOE of a stylized solar plant as a function of the cost of capital,
     with single-stage and two-stage (construction, then refinancing) finance.
  2. One-factor (Vasicek) large-pool loss model: the subordination (first loss
     plus mezzanine) needed for the senior tranche to reach a target default
     probability, as a function of default correlation and recovery.
  3. Two-factor (global plus host-country) extension by Monte Carlo: how pooling
     operating assets across N host countries lowers the first loss needed.
  4. A tiered bond guarantee: probability that each tier is called, Gaussian copula.

All parameters are stylized unless a source is given in the paper.
"""
import numpy as np
from scipy.stats import norm, multivariate_normal

# ---------------------------------------------------------------- 1. LCOE
CAPEX = 800.0      # $/kW, stylized (as in the series' LCOE table)
CF = 0.20          # capacity factor
OM = 12.0          # $/kW/yr
LIFE = 25          # years of operation
BUILD = 2          # years of construction
KWH = CF * 8760    # kWh per kW per year = 1,752


def crf(r, n=LIFE):
    """Capital recovery factor."""
    return r / (1 - (1 + r) ** -n) if r > 0 else 1.0 / n


def lcoe(r, capex=CAPEX):
    """LCOE in US cents/kWh, capital spent at commissioning, single rate r."""
    return 100 * (capex * crf(r) + OM) / KWH


def financing_share(r):
    return 1 - lcoe(0.0) / lcoe(r)


def lcoe_staged(r_con, r_op, capex=CAPEX, build=BUILD):
    """LCOE when capital is drawn evenly over `build` years at rate r_con and the
    plant's capitalized cost at commissioning is then recovered at r_op."""
    # even drawdown: average capital outstanding for build/2 years
    capitalized = capex * (1 + r_con) ** (build / 2)
    return 100 * (capitalized * crf(r_op) + OM) / KWH


# ---------------------------------------------------------- 2. Vasicek pool
def vasicek_quantile(p, rho, q):
    """q-quantile of the default fraction in a large homogeneous pool."""
    return norm.cdf((norm.ppf(p) + np.sqrt(rho) * norm.ppf(q)) / np.sqrt(1 - rho))


def subordination(p, rho, lgd, target_pd):
    """Attachment point K such that P(pool loss > K) = target_pd."""
    return lgd * vasicek_quantile(p, rho, 1 - target_pd)


def tranche_default_prob(p, rho, lgd, attach):
    """P(pool loss > attach) in the large-pool limit."""
    x = attach / lgd
    if x >= 1:
        return 0.0
    return 1 - norm.cdf((np.sqrt(1 - rho) * norm.ppf(x) - norm.ppf(p)) / np.sqrt(rho))


def expected_tranche_loss(p, rho, lgd, a, d, n=20001):
    """Expected loss of tranche [a, d] as a share of the pool, large-pool limit."""
    z = np.linspace(-8, 8, n)
    w = norm.pdf(z) * (z[1] - z[0])
    L = lgd * norm.cdf((norm.ppf(p) - np.sqrt(rho) * z) / np.sqrt(1 - rho))
    return float(np.sum(w * np.clip(L - a, 0, d - a)))


def structure_wacc(e, m, r_e, r_m, r_s, cost=0.003):
    """Blended cost of a tranched pool: first loss e, mezzanine m, senior rest,
    plus an all-in running cost of structuring, servicing and guarantee fees."""
    s = 1 - e - m
    return e * r_e + m * r_m + s * r_s + cost


# --------------------------------------------- 3. Two-factor, N host countries
def mc_subordination(p, rho_g, rho_c, lgd, target_pd, n_countries, sims=400_000, seed=1):
    """Monte Carlo attachment point for a pool spread equally over n_countries,
    each a large sub-pool. Asset value: sqrt(rho_g) Z + sqrt(rho_c) Y_c + noise."""
    rng = np.random.default_rng(seed)
    Z = rng.standard_normal(sims)
    Y = rng.standard_normal((sims, n_countries))
    s = np.sqrt(1 - rho_g - rho_c)
    frac = norm.cdf((norm.ppf(p) - np.sqrt(rho_g) * Z[:, None] - np.sqrt(rho_c) * Y) / s)
    L = lgd * frac.mean(axis=1)
    return float(np.quantile(L, 1 - target_pd))


# ------------------------------------------------- 4. Tiered bond guarantee
def tier_call_probs(pds, rho):
    """out[k-1] = probability that tiers 1..k all fail (Gaussian copula, equal pairwise
    correlation rho). So out[0] = tier 2 is called, out[1] = tier 3 is called,
    out[2] = bondholders lose."""
    out = []
    for k in range(1, len(pds) + 1):
        thr = norm.ppf(pds[:k])
        if k == 1:
            out.append(pds[0])
            continue
        cov = np.full((k, k), rho)
        np.fill_diagonal(cov, 1.0)
        out.append(float(multivariate_normal(mean=np.zeros(k), cov=cov).cdf(thr)))
    return out


# ---------------------------------------------------------------- tables
BASE = dict(p=0.05, lgd=0.20)          # 10-year cumulative PD and LGD, operating plants
TARGETS = [("near-AAA", 0.001), ("strong investment grade", 0.005), ("investment grade", 0.01)]
RHOS = [0.05, 0.10, 0.20, 0.30]
R_E, R_M, R_S = 0.12, 0.08, 0.05        # stylized required returns, $ terms
MEZZ_PD = 0.05                          # mezzanine attaches where P(loss > a) = 5%


def table_lcoe():
    rows = []
    for r in [0.04, 0.06, 0.08, 0.10, 0.12, 0.15]:
        rows.append((r, lcoe(r), lcoe(r) / lcoe(0.04), financing_share(r)))
    return rows


def table_first_loss(p=BASE["p"], lgd=BASE["lgd"]):
    rows = []
    for rho in RHOS:
        rows.append((rho, [subordination(p, rho, lgd, t) for _, t in TARGETS]))
    return rows


def capital_structure(p=BASE["p"], lgd=BASE["lgd"], rho=0.20, target=0.001):
    k_senior = subordination(p, rho, lgd, target)
    k_mezz = subordination(p, rho, lgd, MEZZ_PD)
    e = k_mezz              # first loss: absorbs up to the mezzanine attachment
    m = k_senior - k_mezz   # mezzanine
    return e, m, 1 - e - m


def main():
    print("Table A. LCOE of stylized solar ($800/kW, CF 20%, O&M $12/kW/yr, 25 yrs)")
    for r, c, rel, sh in table_lcoe():
        print(f"  r={r:5.0%}  LCOE={c:4.2f} c/kWh  rel={rel:4.2f}  financing share={sh:4.0%}")

    print("\nTable B. Subordination (% of pool) for senior target 10-yr PD; p=5%, LGD=20%")
    for rho, ks in table_first_loss():
        print(f"  rho={rho:4.2f}  " + "  ".join(f"{n}({t:.1%}): {k:5.1%}" for (n, t), k in zip(TARGETS, ks)))
    print("  LGD = 40% (stress recovery 60%):")
    for rho, ks in table_first_loss(lgd=0.40):
        print(f"  rho={rho:4.2f}  " + "  ".join(f"{k:5.1%}" for k in ks))
    print("  p = 10% (lower-middle-income project finance average, Moody's 2017), LGD 28%:")
    for rho, ks in table_first_loss(p=0.10, lgd=0.28):
        print(f"  rho={rho:4.2f}  " + "  ".join(f"{k:5.1%}" for k in ks))
    print("  expected pool loss p*LGD =", BASE["p"] * BASE["lgd"])

    print("\nTable C. Capital structure and blended cost, rho=0.20, senior target 0.1%")
    e, m, s = capital_structure()
    w = structure_wacc(e, m, R_E, R_M, R_S)
    print(f"  first loss {e:5.1%}  mezzanine {m:5.1%}  senior {s:5.1%}  blended cost {w:5.2%}")
    el_e = expected_tranche_loss(BASE['p'], 0.20, BASE['lgd'], 0, e)
    el_m = expected_tranche_loss(BASE['p'], 0.20, BASE['lgd'], e, e + m)
    el_s = expected_tranche_loss(BASE['p'], 0.20, BASE['lgd'], e + m, 1)
    print(f"  expected loss as % of tranche over 10 yrs: equity {el_e/e:5.1%}  mezz {el_m/m:5.2%}  senior {el_s/s:6.3%}")
    print(f"  check senior PD: {tranche_default_prob(BASE['p'], 0.20, BASE['lgd'], e + m):.4f}")

    print("\nTable D. LCOE: single-stage vs two-stage (construction 2 yrs at 12%)")
    cases = [("single-stage 10%", lcoe_staged(0.10, 0.10)),
             ("single-stage 12%", lcoe_staged(0.12, 0.12)),
             ("two-stage, refinance at 8% (project bond)", lcoe_staged(0.12, 0.08)),
             (f"two-stage, refinance at pooled {w:.1%}", lcoe_staged(0.12, w)),
             ("two-stage, refinance at 6%", lcoe_staged(0.12, 0.06))]
    base = cases[0][1]
    for n, c in cases:
        print(f"  {n:45s} {c:4.2f} c/kWh  ({c/base-1:+5.0%} vs single-stage 10%)")

    print("\nTable E. Diversification across host countries (rho_g=0.10, rho_c=0.15, target 0.1%)")
    for n in [1, 3, 5, 10, 20]:
        k = mc_subordination(BASE['p'], 0.10, 0.15, BASE['lgd'], 0.001, n)
        print(f"  N={n:3d}  subordination {k:5.1%}")
    print(f"  limit (single-factor, rho=0.10): {subordination(BASE['p'], 0.10, BASE['lgd'], 0.001):5.1%}")
    print(f"  N=1 analytic (rho=0.25):          {subordination(BASE['p'], 0.25, BASE['lgd'], 0.001):5.1%}")

    print("\nTable F. Tiered bond guarantee: probability each tier is called (10-yr)")
    pds = [0.15, 0.08, 0.002]   # state utility regulator, national govt, donor-backed SPV
    for rho in [0.0, 0.5, 0.8]:
        probs = tier_call_probs(pds, rho)
        print(f"  rho={rho:3.1f}  tier2 called {probs[0]:6.2%}  tier3 called {probs[1]:6.2%}  bondholders lose {probs[2]:7.4%}")


if __name__ == "__main__":
    main()
