"""Symbolic and numerical checks of Propositions 1-6 in working paper 1.2 (v0.3).

Run:  python3 check_propositions.py   (needs sympy and numpy)
Every check prints OK or raises AssertionError.
"""
import numpy as np
import sympy as sp

rng = np.random.default_rng(12)


def dispatch(cost, cap, D):
    """Least-cost merit order: fill plants in order of cost up to demand D."""
    order = np.argsort(cost, kind="stable")
    q = np.zeros_like(cap)
    left = D
    for j in order:
        q[j] = min(cap[j], left)
        left -= q[j]
    m = order[np.flatnonzero(q[order] > 0)[-1]]  # marginal plant
    return q, m


# ---- Propositions 1-3 on random systems ------------------------------------
for trial in range(2000):
    J = rng.integers(3, 9)
    c = rng.uniform(0, 100, J)
    e = rng.uniform(0, 1.2, J)
    cap = rng.uniform(1, 10, J)
    D = rng.uniform(0.2, 0.95) * cap.sum()
    t = rng.uniform(1, 150)
    q0, m0 = dispatch(c, cap, D)
    qT, mT = dispatch(c + t * e, cap, D)
    ebar = (qT * e).sum() / D           # realized average benchmark
    qF, mF = dispatch(c + t * (e - ebar), cap, D)
    # Prop 1: identical dispatch and marginal plant
    assert np.allclose(qT, qF) and mT == mF
    # Prop 2: single buyer, pool netted: tariff change = R, with 0 <= R <= t(e0 - et)
    R = ((qF - q0) * c).sum() / D
    e0 = (q0 * e).sum() / D
    assert (qF * (e - ebar)).sum() < 1e-9 * D + 1e-9
    assert R >= -1e-9 and R <= t * (e0 - ebar) + 1e-9
    # tax tariff change = R + t*ebar
    tariff_T = ((qT * (c + t * e)).sum() - (q0 * c).sum()) / D
    assert np.isclose(tariff_T, R + t * ebar)
    # Prop 3: uniform price; p_F = p_T - t*ebar; margins identical for every plant
    pT = c[mT] + t * e[mT]
    pF = c[mF] + t * (e[mF] - ebar)
    assert np.isclose(pF, pT - t * ebar)
    assert np.allclose(pT - c - t * e, pF - c - t * (e - ebar))
    # consumers' extra spending = producers' extra surplus + extra resource cost
    p0 = c[m0]
    ps0 = (q0 * (p0 - c)).sum()
    psF = (qF * (pF - c - t * (e - ebar))).sum()
    assert np.isclose((pF - p0) * D, (psF - ps0) + ((qF - q0) * c).sum())
print("Propositions 1-3: OK on 2000 random merit-order systems")

# ---- Proposition 4: the benchmark cancels from the investment comparison ---
LC, LD, t, eC, eD, eb, beta = sp.symbols("L_C L_D t e_C e_D ebar beta", real=True)
gap_tax = (LC + t * eC) - (LD + t * eD)
gap_fee = (LC + t * (eC - eb)) - (LD + t * (eD - eb))
assert sp.simplify(gap_tax - gap_fee) == 0
print("Proposition 4: OK (clean-dirty cost gap identical under tax and feebate)")

# ---- Proposition 5: dominant firm ------------------------------------------
n = 4
q = sp.symbols(f"q1:{n+1}", positive=True)
e = sp.symbols(f"e1:{n+1}", positive=True)
Q = sum(q)
ebar_s = sum(qi * ei for qi, ei in zip(q, e)) / Q
F1 = t * (e[0] - ebar_s) * q[0]
E1 = e[0] * q[0]
# marginal payment per tonne of own emissions, output held fixed
dF_dE = sp.diff(F1, e[0]) / sp.diff(E1, e[0])
s1 = q[0] / Q
assert sp.simplify(dF_dE - t * (1 - s1)) == 0
# leave-one-out benchmark: e_i - ebar_{-i} = (e_i - ebar)/(1 - s_i)
ebar_m1 = sum(qi * ei for qi, ei in zip(q[1:], e[1:])) / (Q - q[0])
assert sp.simplify((e[0] - ebar_m1) - (e[0] - ebar_s) / (1 - s1)) == 0
# lagged benchmark, permanent cut Delta from period 0, discount factor delta:
Delta, delta, qq, s = sp.symbols("Delta delta q s", positive=True)
pv_gain = t * Delta * qq / (1 - delta) - delta * t * s * Delta * qq / (1 - delta)
assert sp.simplify(pv_gain - t * Delta * qq * (1 - delta * s) / (1 - delta)) == 0
print("Proposition 5: OK (t(1-s); leave-one-out scaling 1/(1-s); lagged t(1-delta s))")

# ---- Proposition 6: gaming the lagged benchmark ----------------------------
# raise intensity by Delta in period tau (benchmark predetermined): cost t*Delta*q;
# next period's benchmark rises by s*Delta: gain delta*t*s*Delta*q.
net = -t * Delta * qq + delta * t * s * Delta * qq
assert sp.simplify(net + t * Delta * qq * (1 - delta * s)) == 0
print("Proposition 6: OK (net gain from inflating intensity = -t*Delta*q*(1-delta*s) < 0)")

# ---- Fuel-specific benchmarks remove the switching incentive ---------------
cc, cg, ec, eg = sp.symbols("c_c c_g e_c e_g", real=True)
single = (cc + t * (ec - eb)) - (cg + t * (eg - eb))
fuel_specific = (cc + t * (ec - ec)) - (cg + t * (eg - eg))  # homogeneous classes
assert sp.simplify(single - (cc - cg + t * (ec - eg))) == 0
assert sp.simplify(fuel_specific - (cc - cg)) == 0
print("Corollary (fuel-specific benchmarks): OK")
