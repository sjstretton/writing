"""Symbolic and numerical checks of Propositions 1-3 (working paper 1.6, Section 3).

Chain of n stages. Stage k buys stage k-1's output, adds value w_k and emits a_k
tonnes ("carbon added"); p_k is its sales value net of tax; v the value rate; P
the carbon price; C_k the carbon base on its sales invoice (tonnes); q_k an
explicit carbon price it pays on its own emissions (ETS, energy obligation,
recognized foreign price); Q_k = sum_{j<=k} q_j a_j the price already paid,
carried on the invoice.  Run: python3 check_propositions.py
"""
import sympy as sp

n = 4
P, v = sp.symbols("P v", positive=True)
w = sp.symbols(f"w1:{n + 1}", positive=True)
a = sp.symbols(f"a1:{n + 1}", positive=True)
q = sp.symbols(f"q1:{n + 1}", nonnegative=True)
C = sp.symbols(f"C1:{n + 1}", positive=True)          # arbitrary invoice bases

p = [sum(w[: k + 1]) for k in range(n)]               # taxable chain: p_k = p_{k-1} + w_k
E = [sum(a[: k + 1]) for k in range(n)]               # embodied carbon


def remit(k, base):
    prev_p = p[k - 1] if k else 0
    prev_b = base[k - 1] if k else 0
    return v * (p[k] - prev_p) + P * (base[k] - prev_b)


# Proposition 1(i): total remitted depends only on the final-stage base.
total = sum(remit(k, C) for k in range(n))
assert sp.simplify(total - (v * p[-1] + P * C[-1])) == 0
# Proposition 1(ii): with correct bases each firm pays P times its carbon added.
for k in range(n):
    assert sp.simplify(remit(k, E) - (v * w[k] + P * a[k])) == 0

# Proposition 3: invoices carry Q_k; carbon component on sale is P*E_k - Q_k.
Q = [sum(q[j] * a[j] for j in range(k + 1)) for k in range(n)]
net = [P * E[k] - Q[k] for k in range(n)]
for k in range(n):
    prev = net[k - 1] if k else 0
    assert sp.simplify((net[k] - prev) - (P - q[k]) * a[k]) == 0
# every tonne bears q_k + (P - q_k) = P in total
assert sp.simplify(sum((net[k] - (net[k - 1] if k else 0)) + q[k] * a[k] for k in range(n))
                   - P * E[-1]) == 0

# Proposition 2: stage j exempt (no output tax, no input credit); its
# irrecoverable input taxes enter its price.  Downstream bases correct (C=E).
for j in range(n):
    pj = [None] * n
    for k in range(n):
        if k == 0:
            pj[k] = w[0]
        elif k == j:
            pj[k] = pj[k - 1] + w[k] + v * pj[k - 1] + P * E[k - 1]
        else:
            pj[k] = pj[k - 1] + w[k]
    if j == 0:
        pj[0] = w[0]
    # consumer outlay
    if j == n - 1:
        outlay = pj[-1]
    else:
        outlay = (1 + v) * pj[-1] + P * E[-1]
    baseline = (1 + v) * p[-1] + P * E[-1]
    excess = sp.expand(outlay - baseline)
    if 0 < j < n - 1:   # intermediate exemption: upstream carbon charged twice, plus value tax on it
        expected = (1 + v) * (v * p[j - 1] + P * E[j - 1])
        assert sp.simplify(excess - sp.expand(expected)) == 0
    if j == n - 1:      # final-stage exemption: upstream charged once, own carbon a_n uncharged
        expected = -v * w[n - 1] - P * a[n - 1]
        assert sp.simplify(excess - sp.expand(expected)) == 0

# Worked example in the text (2032: P = 100, v = 0.125; ETS price 80 at stage 1).
num = {P: 100, v: sp.Rational(1, 8)}
ex_p = [200, 500, 800]
ex_a = [sp.Rational(4, 10), sp.Rational(1, 10), sp.Rational(2, 100)]
ex_q = [80, 0, 0]
E3 = [sum(ex_a[: k + 1]) for k in range(3)]
Q3 = [sum(ex_q[j] * ex_a[j] for j in range(k + 1)) for k in range(3)]
rows = []
for k in range(3):
    vat = num[v] * (ex_p[k] - (ex_p[k - 1] if k else 0))
    cc = (num[P] * E3[k] - Q3[k]) - ((num[P] * E3[k - 1] - Q3[k - 1]) if k else 0)
    rows.append((k + 1, float(vat), float(cc), float(ex_q[k] * ex_a[k]),
                 float(E3[k] * 1000 / ex_p[k])))
print("stage, value VAT, carbon component, ETS paid, embodied kg/EUR")
for r in rows:
    print(r)
print("totals:", sum(r[1] for r in rows), sum(r[2] for r in rows), sum(r[3] for r in rows))
assert sum(r[2] for r in rows) + sum(r[3] for r in rows) == float(num[P] * E3[-1])
print("All propositions checked symbolically for n =", n)
