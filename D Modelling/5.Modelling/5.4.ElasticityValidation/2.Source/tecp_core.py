"""Copied unchanged (below this note) from paper 6.1 (v0.3),
D Modelling/6.ModularUpgrades/6.1.PolicyEquivalentCarbonPriceAndCES/2.Source/tecp_model.py,
so that paper 5.4 runs on its own. Paper 5.4 uses it to show how the elasticity
calibration moves emission cuts and the Total Effective Carbon Price.
"""
"""Core model for working paper 6.1 (v0.3), "Measure Carbon Pricing by the
Emissions It Cuts: The Total Effective Carbon Price".

Nested CES energy demand in each sector; the first-order, second-order and
exact (iterative) Total Effective Carbon Price (TECP); instruments as price
changes; non-price instruments; partial adjustment.

The stylized three-sector economy and the three instruments are identical to
those of Climate Fiscal Policy Brief No. 6.1 (1.Presentation/figures/
make_figures.py), so the paper and the brief report the same numbers.
`check_against_brief()` asserts this.

Notation (per sector s): q_f quantity, p_f delivered price, e_f emission factor,
X = sum p q (energy spending), s_f = p_f q_f / X (cost share),
x_f = e_f / p_f (emissions per dollar of fuel f), kappa = sum s_f x_f = E/X,
V = sum s_f (x_f - kappa)^2. sigma: substitution elasticity; eta: |demand
elasticity| (positive number).
"""

from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent

# --------------------------------------------------------------------------
# Stylized economy (identical to the brief). Power: TWh, $/MWh, tCO2/MWh;
# transport and industry: PJ, $/GJ, tCO2/GJ. Quantity x emission factor = MtCO2.
# --------------------------------------------------------------------------
ECON = {
    "Power": {
        "sigma": 2.0, "eta": 0.2,
        "fuels": {"Coal": (100.0, 70.0, 0.95),
                  "Gas": (60.0, 80.0, 0.40),
                  "Renewables": (40.0, 70.0, 0.0)},
    },
    "Road transport": {
        "sigma": 1.5, "eta": 0.4,
        "fuels": {"Gasoline": (600.0, 30.0, 0.069),
                  "Diesel": (500.0, 28.0, 0.074),
                  "Biofuel": (80.0, 34.0, 0.025)},
    },
    "Industry": {
        "sigma": 0.8, "eta": 0.3,
        "fuels": {"Coal": (300.0, 4.0, 0.095),
                  "Oil": (150.0, 18.0, 0.074),
                  "Gas": (400.0, 10.0, 0.056)},
    },
}
SECTORS = list(ECON)
TAX = 30.0
TAX_SECTORS = ("Power", "Industry")
SUBSIDY = 10.0
LCFS_CUT = 0.02


def arrays(sector, econ=ECON):
    d = econ[sector]["fuels"]
    names = list(d)
    q, p, e = (np.array([d[n][i] for n in names]) for i in range(3))
    return names, q, p, e


def params(sector, econ=ECON):
    return econ[sector]["sigma"], econ[sector]["eta"]


def stats(sector, econ=ECON):
    """Cost shares, carbon per dollar, kappa, V, spending X, emissions E."""
    _, q, p, e = arrays(sector, econ)
    X = np.sum(p * q)
    s = p * q / X
    x = e / p
    kappa = np.sum(s * x)
    V = np.sum(s * (x - kappa) ** 2)
    return dict(s=s, x=x, kappa=kappa, V=V, X=X, E=np.sum(q * e), Ef=q * e)


# ---------------- semi-elasticities (Proposition 1) ----------------------
def semi_elasticities(sector, econ=ECON):
    sig, eta = params(sector, econ)
    st = stats(sector, econ)
    return sig * (st["x"] - st["kappa"]), eta * st["kappa"], st["kappa"]


def semi_elasticities_old(sector, econ=ECON):
    """v0.2 and earlier: sigma (1 - w)(e - ebar)/p and |eta| ebar / C,
    with energy shares w, energy-weighted ebar and C the energy-weighted
    average price (so that ebar / C = kappa)."""
    sig, eta = params(sector, econ)
    _, q, p, e = arrays(sector, econ)
    w = q / q.sum()
    ebar = np.sum(w * e)
    C = np.sum(w * p)
    return sig * (1 - w) * (e - ebar) / p, eta * ebar / C, w, ebar, C


# ---------------- first- and second-order cuts ---------------------------
def linear_cut(sector, dp, econ=ECON, sig=None, eta=None):
    """First-order emission reduction (Mt), split (switching, demand)."""
    s0, e0 = params(sector, econ)
    sig = s0 if sig is None else sig
    eta = e0 if eta is None else eta
    _, q, p, e = arrays(sector, econ)
    st = stats(sector, econ)
    pi = dp / p
    pibar = np.sum(st["s"] * pi)
    return np.sum(st["Ef"] * sig * (pi - pibar)), st["E"] * eta * pibar


def second_order_term(sector, dp, econ=ECON):
    """Second-order part of the emission reduction (Mt):
    -sum E_f { 1/2 [sigma pi_f^2 - (sigma - eta)(pibar^2 + sigma V_pi)] + 1/2 L_f^2 },
    L_f = -sigma pi_f + (sigma - eta) pibar. Verified in verify_derivations.py."""
    sig, eta = params(sector, econ)
    _, q, p, e = arrays(sector, econ)
    st = stats(sector, econ)
    pi = dp / p
    pibar = np.sum(st["s"] * pi)
    Vpi = np.sum(st["s"] * (pi - pibar) ** 2)
    L = -sig * pi + (sig - eta) * pibar
    second = 0.5 * (sig * pi ** 2 - (sig - eta) * (pibar ** 2 + sig * Vpi)) + 0.5 * L ** 2
    return -np.sum(st["Ef"] * second)


# ---------------- exact nonlinear CES ------------------------------------
def exact_quantities(sector, dp, econ=ECON, sig=None, eta=None, a_int=1.0, a_ext=1.0):
    """Exact CES quantities after price change dp. With a_int, a_ext < 1, the
    log of the unit-input requirement (switching) and the log of the service
    aggregate (demand) have moved only those fractions of the way to their
    new equilibrium (geometric partial adjustment, Appendix C)."""
    s0, e0 = params(sector, econ)
    sig = s0 if sig is None else sig
    eta = e0 if eta is None else eta
    _, q, p, e = arrays(sector, econ)
    s = stats(sector, econ)["s"]
    P = (p + dp) / p
    if abs(sig - 1.0) < 1e-9:
        lnC = np.sum(s * np.log(P))
    else:
        lnC = np.log(np.sum(s * P ** (1 - sig))) / (1 - sig)
    ln_h = -sig * np.log(P) + sig * lnC      # unit-input requirement (switching)
    ln_Q = -eta * lnC                         # service aggregate (demand)
    return q * np.exp(a_int * ln_h + a_ext * ln_Q)


def exact_emissions(sector, dp, econ=ECON, **kw):
    _, q, p, e = arrays(sector, econ)
    return np.sum(exact_quantities(sector, dp, econ, **kw) * e)


def base_emissions(sector, econ=ECON):
    _, q, _, e = arrays(sector, econ)
    return np.sum(q * e)


def bisect(f, lo, hi, n=80):
    flo = f(lo)
    for _ in range(n):
        mid = 0.5 * (lo + hi)
        fm = f(mid)
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ---------------- instruments as price changes ---------------------------
def dp_uniform(sector, rate, econ=ECON):
    _, _, _, e = arrays(sector, econ)
    return rate * e


def lcfs_target(econ=ECON):
    _, q, _, e = arrays("Road transport", econ)
    return (1 - LCFS_CUT) * np.sum(q * e) / np.sum(q)


def solve_lcfs_lambda(econ=ECON, **kw):
    """Credit price at which the standard just binds in the exact CES model."""
    _, q, _, e = arrays("Road transport", econ)
    target = lcfs_target(econ)

    def gap(lam):
        qn = exact_quantities("Road transport", lam * (e - target), econ, **kw)
        return np.sum(qn * e) / np.sum(qn) - target

    return bisect(gap, 0.0, 600.0)


def dp_instrument(name, sector, lam=None, econ=ECON):
    names, q, p, e = arrays(sector, econ)
    dp = np.zeros_like(p)
    if name == "tax" and sector in TAX_SECTORS:
        dp = TAX * e
    elif name == "subsidy" and sector == "Power":
        dp = np.array([-SUBSIDY if n == "Renewables" else 0.0 for n in names])
    elif name == "standard" and sector == "Road transport":
        dp = lam * (e - lcfs_target(econ))
    return dp


INSTRUMENTS = ("tax", "subsidy", "standard")
LABELS = {"tax": "Carbon tax, $30/t (power, industry)",
          "subsidy": "Renewable subsidy, $10/MWh (power)",
          "standard": "Low-carbon fuel standard, -2% (road)"}


def package_dp(lam, keys=INSTRUMENTS, scale=1.0, econ=ECON):
    return {s: scale * sum(dp_instrument(k, s, lam, econ) for k in keys) for s in SECTORS}


# ---------------- TECP: first order, second order, exact ------------------
def Lambda(econ=ECON, parts=False):
    out = {}
    for s in SECTORS:
        out[s] = linear_cut(s, dp_uniform(s, 1.0, econ), econ)
    tot = sum(a + b for a, b in out.values())
    return (tot, out) if parts else tot


def Lambda_closed_form(econ=ECON):
    """Lambda = sum_s X_s (sigma_s V_s + eta_s kappa_s^2)  (Proposition 1)."""
    tot = 0.0
    for s in SECTORS:
        sig, eta = params(s, econ)
        st = stats(s, econ)
        tot += st["X"] * (sig * st["V"] + eta * st["kappa"] ** 2)
    return tot


def Gamma(econ=ECON):
    """Second derivative of the uniform-tax cut at zero: R_U(t) ~ Lambda t + Gamma t^2 / 2."""
    return 2.0 * sum(second_order_term(s, dp_uniform(s, 1.0, econ), econ) for s in SECTORS)


def tecp_linear(dps, econ=ECON):
    cut = sum(sum(linear_cut(s, dps[s], econ)) for s in SECTORS)
    return cut / Lambda(econ)


def tecp_second_order(dps, econ=ECON):
    L = Lambda(econ)
    R1 = sum(sum(linear_cut(s, dps[s], econ)) for s in SECTORS)
    R2 = sum(second_order_term(s, dps[s], econ) for s in SECTORS)
    t1 = R1 / L
    return t1 + (R2 - 0.5 * Gamma(econ) * t1 ** 2) / L


def exact_cut(dps, econ=ECON, **kw):
    return sum(base_emissions(s, econ) - exact_emissions(s, dps[s], econ, **kw) for s in SECTORS)


def tecp_exact_from_cut(cut, econ=ECON, **kw):
    def gap(t):
        return sum(base_emissions(s, econ) - exact_emissions(s, dp_uniform(s, t, econ), econ, **kw)
                   for s in SECTORS) - cut
    lo = -0.99 * min(np.min(arrays(s, econ)[2][arrays(s, econ)[3] > 0] / arrays(s, econ)[3][arrays(s, econ)[3] > 0])
                     for s in SECTORS)
    return bisect(gap, lo, 2000.0)


def tecp_exact(dps, econ=ECON, **kw):
    return tecp_exact_from_cut(exact_cut(dps, econ, **kw), econ, **kw)


def tecp_horizon_linear(dps, a_int, a_ext, econ=ECON):
    """First-order TECP at a horizon where the switching and demand margins have
    completed fractions a_int, a_ext of their adjustment (Corollary 1)."""
    num = den = 0.0
    for s in SECTORS:
        i, x = linear_cut(s, dps[s], econ)
        iu, xu = linear_cut(s, dp_uniform(s, 1.0, econ), econ)
        num += a_int * i + a_ext * x
        den += a_int * iu + a_ext * xu
    return num / den


def explicit_price_metric(econ=ECON):
    E = sum(base_emissions(s, econ) for s in SECTORS)
    return TAX * sum(base_emissions(s, econ) for s in TAX_SECTORS) / E


def check_against_brief():
    lam = solve_lcfs_lambda()
    dps = package_dp(lam)
    t_lin, t_ex = tecp_linear(dps), tecp_exact(dps)
    assert abs(lam - 166.0) < 0.5, lam
    assert abs(t_lin - 33.21) < 0.01, t_lin
    assert abs(t_ex - 36.86) < 0.01, t_ex
    assert abs(Lambda() - 1.5947) < 1e-4
    assert abs(Lambda() - Lambda_closed_form()) < 1e-10
    return lam, t_lin, t_ex


if __name__ == "__main__":
    print(check_against_brief())
