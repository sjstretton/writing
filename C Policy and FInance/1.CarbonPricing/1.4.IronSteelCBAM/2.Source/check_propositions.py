"""Symbolic and numeric checks of Propositions 1-6 in IronSteelCBAM.qmd (v0.3).

Run from this folder:  python check_propositions.py
Prints "ok" after each check; raises AssertionError on failure.
"""
import sympy as sp

tau, eB, eS, Q, QEU, s, c, t, k, e0, rho, mu, theta, lam, eR, pi = sp.symbols(
    "tau e_B e_S Q Q_EU s c t k e_0 rho mu theta lambda e_R pi", positive=True)

# ---------- Proposition 1: plant-level measurement ----------
x = sp.symbols("x", nonnegative=True)           # scrap-route output sent to the EU
bill_P = tau * (eS * x + eB * (QEU - x))
assert sp.simplify(sp.diff(bill_P, x) + tau * (eB - eS)) == 0   # bill falls in x
qS = s * Q
x0 = s * QEU                                     # proportional allocation
gain_cap = sp.simplify(bill_P.subs(x, x0) - bill_P.subs(x, QEU))   # case qS >= QEU
assert sp.simplify(gain_cap - tau * (eB - eS) * (1 - s) * QEU) == 0
gain_lim = sp.simplify(bill_P.subs(x, x0) - bill_P.subs(x, qS))    # case qS < QEU
assert sp.simplify(gain_lim - tau * (eB - eS) * s * (Q - QEU)) == 0
# in terms of the average intensity ebar, with eB = (ebar - s eS)/(1-s)
ebar = sp.symbols("ebar", positive=True)
eB_of = (ebar - s * eS) / (1 - s)
assert sp.simplify(gain_cap.subs(eB, eB_of) - tau * (ebar - eS) * QEU) == 0
mu_ = QEU / Q
assert sp.simplify(gain_lim.subs(eB, eB_of) - tau * (ebar - eS) * s * (1 - mu_) * Q / (1 - s)) == 0
# brief example: 10 Mt, 2 Mt scrap, 1 Mt to EU, 2.0 / 0.4, EUR 80
num = gain_cap.subs({tau: 80, eB: 2.0, eS: 0.4, s: 0.2, QEU: 1})
assert abs(float(num) - 102.4) < 1e-9
print("Proposition 1 ok")

# ---------- Proposition 2: fixed scrap ----------
D, Sbar, Delta = sp.symbols("D Sbar Delta", positive=True)
W = eS * Sbar + eB * (D - Sbar)                 # world emissions, scrap fully used
# exporter adds Delta of scrap-EAF output; scrap supply rises by theta*Delta;
# displaced users replace (1-theta)*Delta with output at intensity e_R
dW = -(eB - eS) * Delta + (1 - theta) * (eR - eS) * Delta
assert sp.simplify(dW.subs(eR, eB) + theta * (eB - eS) * Delta) == 0
assert sp.simplify(dW.subs({eR: eB, theta: 0})) == 0
print("Proposition 2 ok")

# ---------- Proposition 3: country-sector measurement ----------
bill_C = tau * (s * eS + (1 - s) * eB) * QEU
assert sp.diff(bill_C, x) == 0
print("Proposition 3 ok")

# ---------- Proposition 4: feebate under price-paid recognition ----------
qi = sp.symbols("q1:4", positive=True)
ei = sp.symbols("e1:4", positive=True)
eb = sum(q * e for q, e in zip(qi, ei)) / sum(qi)
net = sum(q * t * (e - eb) for q, e in zip(qi, ei))
assert sp.simplify(net) == 0
print("Proposition 4 ok")

# ---------- Proposition 5: signal recognition ----------
eoft = e0 - t / k
# (ii) delivered cost of an EU-bound tonne, feebate at t, recognition weight rho
Dcost = t**2 / (2 * k) + (tau - rho * t) * eoft        # valid for rho*t <= tau
dD = sp.diff(Dcost, t)
t_int = sp.solve(sp.Eq(dD, 0), t)[0]
assert sp.simplify(t_int - (tau + rho * k * e0) / (1 + 2 * rho)) == 0
assert sp.simplify(t_int.subs(rho, 0) - tau) == 0
# rho = 1: interior >= tau iff k e0 >= 2 tau, so the corner t = tau binds
assert sp.simplify((t_int.subs(rho, 1) - tau) - (k * e0 - 2 * tau) / 3) == 0
assert sp.simplify(sp.diff(Dcost, t, 2) - (1 + 2 * rho) / k) == 0
# saving at t = tau relative to rho = 0 (1.1, Prop. 7)
assert sp.simplify(Dcost.subs({rho: 0, t: tau}) - Dcost.subs({rho: 1, t: tau}) - tau * (e0 - tau / k)) == 0
# (iii) country best response: resource cost on all output, CBAM on share mu
N = t**2 / (2 * k) + mu * (tau - rho * t) * eoft
t_c = sp.solve(sp.Eq(sp.diff(N, t), 0), t)[0]
assert sp.simplify(t_c - mu * (tau + rho * k * e0) / (1 + 2 * rho * mu)) == 0
assert sp.simplify(t_c.subs(rho, 0) - mu * tau) == 0
dtc = sp.simplify(sp.diff(t_c, rho))
assert sp.simplify(dtc - mu * (k * e0 - 2 * mu * tau) / (1 + 2 * rho * mu)**2) == 0
# (iv) adoption thresholds: net gain of a feebate at t = tau
gain0 = mu * tau * e0 - (tau**2 / (2 * k) + mu * tau * eoft.subs(t, tau))   # rho = 0
assert sp.simplify(gain0 - tau**2 / k * (mu - sp.Rational(1, 2))) == 0
gain1 = mu * tau * e0 - tau**2 / (2 * k)                                     # rho = 1
mu_star = sp.solve(sp.Eq(gain1, 0), mu)[0]
assert sp.simplify(mu_star - tau / (2 * k * e0)) == 0
# implied price per tonne abated of the relief: mu*rho*t*ebar / (t/k)
implied = sp.simplify(mu * rho * t * eoft / (t / k))
assert sp.simplify(implied - mu * rho * k * eoft) == 0
# numbers used in the text (k e0 = 166.67, tau = 80, mu = 0.1)
ke0 = sp.Rational(500, 3)
vals = {tau: 80, mu: sp.Rational(1, 10)}
tc1 = (mu * (tau + ke0) / (1 + 2 * mu)).subs(vals)
print("  t* rho=0:", float((mu * tau).subs(vals)), " rho=1:", round(float(tc1), 1),
      " mu threshold rho=1:", round(float((tau / (2 * ke0)).subs(vals)), 3))
print("Proposition 5 ok")

# ---------- Proposition 6: blended measurement ----------
ebar_cs = sp.symbols("ebar_cs", positive=True)
ehat_B = lam * eB + (1 - lam) * ebar_cs
ehat_S = lam * eS + (1 - lam) * ebar_cs
shuffle_gain = tau * (ehat_B - ehat_S)
assert sp.simplify(shuffle_gain - lam * tau * (eB - eS)) == 0
assert sp.simplify(sp.diff(tau * ehat_S, eS) - lam * tau) == 0
print("Proposition 6 ok")
