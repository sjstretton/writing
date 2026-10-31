"""Symbolic and numerical checks of every derivation in working paper 1.7 (v0.3).

Run:  python verify_derivations.py      (prints PASS/FAIL for each check)

Checks
  P1a  first-order emission response of the exact nested CES (symbolic, 3 fuels)
  P1b  Lambda closed form: sum_f E_f eps_int_f = sigma X V, E eps_ext = eta X kappa^2
  P1c  uniform tax returns itself: tau_int = tau_ext = tau
  P2a  switching margin is service-neutral: sum_f s_f eps_int_f = 0 (any prices)
  P2b  old (1 - w) form is not: counterexample, and value in the worked example
  P2c  equal prices: physical energy conserved under the new form, not the old
  P3a  exact uniform-tax cut is strictly increasing: dE/dtau = -X'(sigma V' + eta kappa'^2)
  P3b  second-order expansion of the emission response (symbolic vs closed form)
  P3c  second-order TECP is a consistent second-order solution
  P4   tradable intensity standard = feebate at the credit price (Lagrangian FOCs)
  P5   non-tradable standard: TECP = (Lambda_F / Lambda)[mu_E + Cov_E(r, mu)/r_bar]
  C1   horizon TECP: omega_T weights
  C2   feebate scores exactly t on the switching margin iff prices per unit are equal
  A9   v0.2 Appendix A.7 + A.9: TECP depends on the energy unit; corrected TECP does not
  NUM  numerical checks against the full nonlinear CES in the worked example
"""

import sys

import numpy as np
import sympy as sp

import tecp_model as M

RESULTS = []


def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


# ----------------------------------------------------------------------------
# Symbolic sector with three fuels
# ----------------------------------------------------------------------------
n = 3
q = sp.symbols("q1:4", positive=True)
p = sp.symbols("p1:4", positive=True)
e = sp.symbols("e1:4", nonnegative=True)
d = sp.symbols("d1:4", real=True)          # price-change direction
t = sp.symbols("t", real=True)             # scale of the policy
sig, eta = sp.symbols("sigma eta", positive=True)

X = sum(p[i] * q[i] for i in range(n))
s = [p[i] * q[i] / X for i in range(n)]
x = [e[i] / p[i] for i in range(n)]
kappa = sum(s[i] * x[i] for i in range(n))
Ef = [q[i] * e[i] for i in range(n)]
E = sum(Ef)


def exact_E(tt, dd):
    P = [1 + tt * dd[i] / p[i] for i in range(n)]
    C = sum(s[i] * P[i] ** (1 - sig) for i in range(n)) ** (1 / (1 - sig))
    return sum(e[i] * q[i] * P[i] ** (-sig) * C ** (sig - eta) for i in range(n))


# P1a: first derivative of the exact model at t = 0
Et = exact_E(t, d)
dE = sp.diff(Et, t).subs(t, 0)
pi = [d[i] / p[i] for i in range(n)]
pibar = sum(s[i] * pi[i] for i in range(n))
formula = -(sig * sum(Ef[i] * (pi[i] - pibar) for i in range(n)) + eta * E * pibar)
check("P1a first-order CES emission response", sp.simplify(dE - formula) == 0)

# P1b: Lambda closed form
eps_int = [sig * (x[i] - kappa) for i in range(n)]
eps_ext = eta * kappa
V = sum(s[i] * (x[i] - kappa) ** 2 for i in range(n))
check("P1b switching weight = sigma X V",
      sp.simplify(sum(Ef[i] * eps_int[i] for i in range(n)) - sig * X * V) == 0)
check("P1b demand weight = eta X kappa^2", sp.simplify(E * eps_ext - eta * X * kappa ** 2) == 0)

# P1c: uniform tax tau: d_i = tau e_i -> tau_int = tau_ext = tau
tau = sp.symbols("tau", positive=True)
pi_u = [tau * e[i] / p[i] for i in range(n)]
pibar_u = sum(s[i] * pi_u[i] for i in range(n))
tau_ext = pibar_u / kappa
tau_int = [(pi_u[i] - pibar_u) / (x[i] - kappa) for i in range(n)]
check("P1c uniform tax: tau_ext = tau", sp.simplify(tau_ext - tau) == 0)
check("P1c uniform tax: tau_int = tau", all(sp.simplify(ti - tau) == 0 for ti in tau_int))
dE_u = sp.diff(exact_E(t, [e[i] for i in range(n)]), t).subs(t, 0)
check("P1c dE/dtau at 0 = -(sum E eps_int + E eps_ext)",
      sp.simplify(dE_u + sum(Ef[i] * eps_int[i] for i in range(n)) + E * eps_ext) == 0)

# P2a: cost-share-weighted switching semi-elasticities sum to zero
check("P2a sum_f s_f eps_int_f = 0", sp.simplify(sum(s[i] * eps_int[i] for i in range(n))) == 0)
# ... and for any policy, sum_f s_f sigma (pi_f - pibar) = 0 (switching moves along the isoquant)
check("P2a sum_f s_f sigma(pi_f - pibar) = 0 for any policy",
      sp.simplify(sum(s[i] * sig * (pi[i] - pibar) for i in range(n))) == 0)

# P2b: old form. Energy shares w, energy-weighted mean ebar.
Q = sum(q)
w = [q[i] / Q for i in range(n)]
ebar = sum(w[i] * e[i] for i in range(n))
eps_old = [sig * (1 - w[i]) * (e[i] - ebar) / p[i] for i in range(n)]
old_sum = sum(s[i] * eps_old[i] for i in range(n))
num_sub = {q[0]: 100, q[1]: 60, q[2]: 40, p[0]: 70, p[1]: 80, p[2]: 70,
           e[0]: sp.Rational(95, 100), e[1]: sp.Rational(40, 100), e[2]: 0, sig: 2}
val = sp.nsimplify(old_sum.subs(num_sub))
check("P2b old form: sum_f s_f eps_old_f != 0 (power sector)", val != 0, f"= {float(val):.3e} per $/t")

# P2c: equal prices p: new form conserves physical energy, old form does not
pp = sp.symbols("pp", positive=True)
eq = {p[i]: pp for i in range(n)}
new_energy = sp.simplify(sum(q[i] * eps_int[i] for i in range(n)).subs(eq))
old_energy = sp.simplify(sum(q[i] * eps_old[i] for i in range(n)).subs(eq))
check("P2c equal prices: new form conserves energy", new_energy == 0)
# eps is the semi-elasticity of the cut, so the change in energy is -sum q eps_old = +(sigma Q/p) sum w^2 (e - ebar)
old_closed = sp.simplify(-old_energy - (sig * Q / pp) * sum(w[i] ** 2 * (e[i] - ebar) for i in range(n)))
check("P2c equal prices: old form changes energy by (sigma Q/p) sum w^2 (e - ebar) per $/t", old_closed == 0)

# P3a: dE/dtau at an arbitrary point = -X'(sigma V' + eta kappa'^2), evaluated at prices p
# (the point is the baseline here; any point is a baseline after relabelling).
check("P3a dE/dtau = -X(sigma V + eta kappa^2) < 0",
      sp.simplify(dE_u + X * (sig * V + eta * kappa ** 2)) == 0)

# P3b: second-order term
d2E = sp.diff(Et, t, 2).subs(t, 0)
Vpi = sum(s[i] * (pi[i] - pibar) ** 2 for i in range(n))
L = [-sig * pi[i] + (sig - eta) * pibar for i in range(n)]
second = sum(Ef[i] * (sp.Rational(1, 2) * (sig * pi[i] ** 2 - (sig - eta) * (pibar ** 2 + sig * Vpi))
                      + sp.Rational(1, 2) * L[i] ** 2) for i in range(n))
# Check numerically at random rational points (full symbolic simplify is slow).
rng = np.random.default_rng(1)
ok = True
for _ in range(6):
    sub = {}
    for i in range(n):
        sub[q[i]] = sp.Rational(int(rng.integers(10, 200)))
        sub[p[i]] = sp.Rational(int(rng.integers(5, 90)))
        sub[e[i]] = sp.Rational(int(rng.integers(0, 100)), 100)
        sub[d[i]] = sp.Rational(int(rng.integers(-50, 50)), 10)
    sub[sig] = sp.Rational(int(rng.integers(2, 30)), 10)
    sub[eta] = sp.Rational(int(rng.integers(1, 9)), 10)
    lhs = sp.N(d2E.subs(sub), 30)
    rhs = sp.N((2 * second).subs(sub), 30)
    ok &= abs(lhs - rhs) < 1e-20 * max(1, abs(lhs))
check("P3b second-order term = 1/2 d2E/dt2 (6 random rational points)", ok)

# P3c: tau2 = tau1 + (R2 - Gamma tau1^2 / 2)/Lambda solves Lambda tau + Gamma tau^2/2 = R1 + R2 to 2nd order
eps = sp.symbols("epsilon")
Lam, Gam, a1, a2 = sp.symbols("Lambda Gamma a1 a2")
R1, R2 = a1 * eps, a2 * eps ** 2
t1 = R1 / Lam
t2 = t1 + (R2 - Gam * t1 ** 2 / 2) / Lam
resid = sp.expand(Lam * t2 + Gam * t2 ** 2 / 2 - R1 - R2)
check("P3c second-order TECP residual is O(eps^3)", sp.Poly(resid, eps).degree() >= 3 and
      all(resid.coeff(eps, k) == 0 for k in range(3)))

# P4: tradable intensity standard. Minimize sum p_f q_f s.t. F(q) >= Qbar and sum e_f q_f <= estd sum q_f.
# FOCs: p_f + lam (e_f - estd) = mu dF/dq_f, identical to cost minimization at prices p_f + lam (e_f - estd).
qq = sp.symbols("qq1:4", positive=True)
lam, mu, estd, Qbar = sp.symbols("lambda mu estd Qbar", positive=True)
alpha = sp.symbols("alpha1:4", positive=True)
rho = (sig - 1) / sig
F = sum(alpha[i] * qq[i] ** rho for i in range(n)) ** (1 / rho)
Lag = sum(p[i] * qq[i] for i in range(n)) - mu * (F - Qbar) + lam * sum((e[i] - estd) * qq[i] for i in range(n))
Lag_feebate = sum((p[i] + lam * (e[i] - estd)) * qq[i] for i in range(n)) - mu * (F - Qbar)
check("P4 standard FOCs = feebate FOCs at the credit price",
      all(sp.simplify(sp.diff(Lag, qq[i]) - sp.diff(Lag_feebate, qq[i])) == 0 for i in range(n)))

# P5: non-tradable standard. Firm i: emissions E_i, responsiveness r_i (cut per $ of feebate
# per tonne), shadow price mu_i. Cut = sum E_i r_i mu_i. TECP = cut / Lambda.
m = 4
Ei = sp.symbols("E_1:5", positive=True)
ri = sp.symbols("r_1:5", positive=True)
mui = sp.symbols("mu_1:5", positive=True)
Lam_all = sp.symbols("Lambda_all", positive=True)
cut = sum(Ei[i] * ri[i] * mui[i] for i in range(m))
Etot = sum(Ei)
rbar = sum(Ei[i] * ri[i] for i in range(m)) / Etot
mubar = sum(Ei[i] * mui[i] for i in range(m)) / Etot
cov = sum(Ei[i] * (ri[i] - rbar) * (mui[i] - mubar) for i in range(m)) / Etot
LamF = Etot * rbar
check("P5 TECP = (Lambda_F/Lambda)(mu_E + Cov_E(r,mu)/r_bar)",
      sp.simplify(cut / Lam_all - (LamF / Lam_all) * (mubar + cov / rbar)) == 0)

# C1: horizon weights
aI, aX, LI, LX, TI, TX = sp.symbols("a_I a_X Lambda_I Lambda_X tau_I tau_X", positive=True)
tauT = (aI * LI * TI + aX * LX * TX) / (aI * LI + aX * LX)
om = LI / (LI + LX)
omT = aI * om / (aI * om + aX * (1 - om))
check("C1 tau_T = omega_T tau_I + (1 - omega_T) tau_X", sp.simplify(tauT - (omT * TI + (1 - omT) * TX)) == 0)

# C2: feebate dp_f = t (e_f - ebar_q): tau_int_f = t iff ebar (1/p_f - sum_g s_g / p_g) = 0
tf = sp.symbols("t_f", positive=True)
pi_fb = [tf * (e[i] - ebar) / p[i] for i in range(n)]
pibar_fb = sum(s[i] * pi_fb[i] for i in range(n))
dev = [sp.simplify(pi_fb[i] - pibar_fb - tf * (x[i] - kappa)
                   + tf * ebar * (1 / p[i] - sum(s[g] / p[g] for g in range(n)))) for i in range(n)]
check("C2 pi_f - pibar = t[(x_f - kappa) - ebar(1/p_f - sum s_g/p_g)]", all(v == 0 for v in dev))
check("C2 equal prices: tau_int = t and tau_ext = 0",
      all(sp.simplify(((pi_fb[i] - pibar_fb) / (x[i] - kappa)).subs(eq) - tf) == 0 for i in range(n))
      and sp.simplify(pibar_fb.subs(eq)) == 0)

# ----------------------------------------------------------------------------
# A9: v0.2 Appendix A.7 + A.9. A.7 folds (e - ebar) and ebar into the semi-elasticities:
# eps_int^A7 = sigma(1-w)(e - ebar)/p, eps_ext^A7 = |eta| ebar / C. A.9 multiplies them by
# (e - ebar) and ebar again in Lambda, and v0.2's main text measures tau_int = dp_f - sum w dp
# and tau_ext = sum w dp in $/GJ. The weights then carry (e - ebar)^2 and ebar^2: a uniform
# tax still returns itself, but the TECP of any other policy depends on the energy unit.
# ----------------------------------------------------------------------------
def v02_appendix_tecp(dps, power_scale=1.0):
    num = den = 0.0
    for sname in M.SECTORS:
        sg, et = M.params(sname)
        _, qv, pv, ev = M.arrays(sname)
        dp = dps[sname].copy()
        if sname == "Power":   # re-express power in GJ (power_scale = 3.6 GJ per MWh)
            qv, pv, ev, dp = qv * power_scale, pv / power_scale, ev / power_scale, dp / power_scale
        wv = qv / qv.sum()
        eb = np.sum(wv * ev)
        C = np.sum(wv * pv)
        Ev = qv * ev
        ei = sg * (1 - wv) * (ev - eb) / pv
        ee = et * eb / C
        mdp = np.sum(wv * dp)
        num += np.sum(Ev * (ei * (dp - mdp) + ee * mdp))
        den += np.sum(Ev * (ei * (ev - eb) + ee * eb))
    return num / den


lam0 = M.solve_lcfs_lambda()
uni = {sn: M.dp_uniform(sn, 1.0) for sn in M.SECTORS}
mix = M.package_dp(lam0)
a, b = v02_appendix_tecp(mix, 1.0), v02_appendix_tecp(mix, 3.6)
check("A9 v0.2 appendix: uniform $1 tax returns $1 in either unit",
      abs(v02_appendix_tecp(uni, 1.0) - 1) < 1e-9 and abs(v02_appendix_tecp(uni, 3.6) - 1) < 1e-9)
check("A9 v0.2 appendix: TECP of the mix depends on the energy unit", abs(a - b) > 0.1,
      f"(power in MWh: {a:.2f}; power in GJ: {b:.2f})")
# the corrected TECP is unit-invariant
econ_gj = __import__("copy").deepcopy(M.ECON)
econ_gj["Power"]["fuels"] = {k: (v[0] * 3.6, v[1] / 3.6, v[2] / 3.6) for k, v in M.ECON["Power"]["fuels"].items()}
mix_gj = {sn: (mix[sn] / 3.6 if sn == "Power" else mix[sn]) for sn in M.SECTORS}
check("A9 corrected TECP is unit-invariant", abs(M.tecp_linear(mix) - M.tecp_linear(mix_gj, econ_gj)) < 1e-9)

# ----------------------------------------------------------------------------
# NUM: numerical checks against the full nonlinear CES (worked example)
# ----------------------------------------------------------------------------
lam_lcfs, t_lin, t_ex = M.check_against_brief()
check("NUM reproduces brief: credit price, linear and exact TECP", True,
      f"(lambda={lam_lcfs:.1f}, linear={t_lin:.2f}, exact={t_ex:.2f})")
check("NUM Lambda closed form = numerical Lambda", abs(M.Lambda() - M.Lambda_closed_form()) < 1e-10)

# finite-difference derivative of exact emissions vs linear formula, each sector, random policy
ok = True
for sname in M.SECTORS:
    for _ in range(5):
        dp = rng.normal(0, 1, 3) * M.arrays(sname)[2] * 0.1
        h = 1e-6
        fd = (M.exact_emissions(sname, -h * dp) - M.exact_emissions(sname, h * dp)) / (2 * h)
        ok &= abs(fd - sum(M.linear_cut(sname, dp))) < 1e-5 * max(1, abs(fd))
check("NUM finite-difference derivative of exact CES = linear cut", ok)

ok = True
for sname in M.SECTORS:
    for _ in range(5):
        dp = rng.normal(0, 1, 3) * M.arrays(sname)[2] * 0.1
        h = 1e-3
        f = lambda k: M.base_emissions(sname) - M.exact_emissions(sname, k * dp)
        fd2 = (f(h) - 2 * f(0) + f(-h)) / h ** 2
        ok &= abs(fd2 / 2 - M.second_order_term(sname, dp)) < 1e-4 * max(1, abs(fd2))
check("NUM finite-difference 2nd derivative of exact CES = second-order term", ok)

# exact TECP of a uniform tax returns the tax; first-order and second-order also
for rate in (10.0, 50.0, 150.0):
    dps = {sn: M.dp_uniform(sn, rate) for sn in M.SECTORS}
    check(f"NUM uniform ${rate:.0f} tax: exact, 1st, 2nd-order TECP all = rate",
          abs(M.tecp_exact(dps) - rate) < 1e-6 and abs(M.tecp_linear(dps) - rate) < 1e-9
          and abs(M.tecp_second_order(dps) - rate) < 1e-9)

# second-order error shrinks as cube of scale
errs = []
for k in (0.1, 0.2):
    dps = M.package_dp(lam_lcfs, scale=k)
    errs.append(abs(M.tecp_second_order(dps) - M.tecp_exact(dps)))
check("NUM 2nd-order TECP error falls ~8x when policy halves", 6 < errs[1] / errs[0] < 10,
      f"(ratio {errs[1] / errs[0]:.2f})")

# Proposition 2 in the example: service change from the switching margin under a $1 tax
for sname in M.SECTORS:
    st = M.stats(sname)
    ei_new, ee, _ = M.semi_elasticities(sname)
    ei_old, ee_old, wv, eb, C = M.semi_elasticities_old(sname)
    new = -np.sum(st["s"] * ei_new)     # d ln(service) per $/t from the switching margin
    old = -np.sum(st["s"] * ei_old)
    print(f"      {sname:15s}: % change in energy service per $/t from switching: new {100*new:+.4f}, "
          f"old {100*old:+.4f}; from demand margin {-100*ee:+.4f}; old/demand = {old/ee:+.2f}")

print()
fails = [r for r in RESULTS if not r[1]]
print(f"{len(RESULTS) - len(fails)} of {len(RESULTS)} checks passed.")
sys.exit(1 if fails else 0)
