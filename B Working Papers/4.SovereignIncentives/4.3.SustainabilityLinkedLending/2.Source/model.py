"""Calibration for 'Codify Sustainability-Linked Sovereign Lending, Then Give It Scale'.

Climate Fiscal Policy Brief No. 4.3 and working paper StrettonWP43.
Run: python3 model.py   (prints every number used in the brief and working paper)

Public inputs (sources in the paper's .bib):
  Uruguay 2023 IBRD loan (MEF briefing note, Dec 2023): USD 350m, 15.5-year maturity,
  4-year grace, semi-annual principal USD 15.2m from April 2028 to April 2039,
  step-down 50 bp a year in performance years 2028-32 (max USD 6.7m) and 100 bp a year
  in 2033-37 (max USD 5.8m); total cap USD 12.5m.
Everything else is STYLIZED and labelled as such.
"""
import numpy as np

R = 0.05  # discount rate for present values (stylized)

# Guarantee loss parameters shared with 3.1 and 3.2 (StrettonWP31, StrettonWP32),
# settled 29 Oct 2026. BASE: the MDB sovereign loss record (GEMs 2025: default rate
# 0.77% a year, recovery 95.1%, 1984-2024), buffer 0.49% of exposure. The record
# reflects preferred-creditor status a new facility might not inherit, so two less
# favorable cases are reported: MIDDLE 3% calls x 10% loss (buffer 2.5%) and STRESS
# 3% calls x 37% loss (average sovereign haircut 1970-2010, Cruces and Trebesch
# 2013; buffer 9.3%). All buffers: 1% annual chance of exhaustion, 20 programs,
# correlation 0.2. Buffers are held in safe assets earning the discount rate, so net
# carry is zero; a 2% carry is a sensitivity.
PD, LGD, BUFFER = 0.0077, 0.049, 0.0049             # base: MDB record
PD_MID, LGD_MID, BUFFER_MID = 0.03, 0.10, 0.025     # middle
PD_STRESS, LGD_STRESS, BUFFER_STRESS = 0.03, 0.37, 0.093  # stress
CASES = {"base (MDB record)": (PD, LGD, BUFFER),
         "middle (3% x 10%)": (PD_MID, LGD_MID, BUFFER_MID),
         "stress (3% x 37%)": (PD_STRESS, LGD_STRESS, BUFFER_STRESS)}
R_BUFFER = 0.0
R_BUFFER_SENS = 0.02


def annuity(r, n):
    return (1 - (1 + r) ** -n) / r


# ---------------------------------------------------------------- Uruguay loan
def uruguay_schedule():
    """Reproduce the published maximum buy-down from the amortization schedule.

    Principal: USD 350m; 23 semi-annual repayments of USD 15.2m, April 2028-April 2039.
    Interest for calendar year y is charged on the average balance outstanding in y.
    Returns dict year -> (avg balance, step-down bp, reward USD m).
    """
    pay_dates = [2028 + 0.25 + 0.5 * k for k in range(23)]  # Apr and Oct
    principal = 350.0
    rows = {}
    for y in range(2028, 2039):
        # balance at quarterly points within the year
        pts = [y + q / 4 for q in range(4)]
        bal = [max(principal - 15.2 * sum(d <= p for d in pay_dates), 0) for p in pts]
        avg = float(np.mean(bal))
        bp = 50 if y <= 2032 else (100 if y <= 2037 else 0)
        rows[y] = (avg, bp, avg * bp / 1e4)
    return rows


def uruguay_summary(r=R, base_year=2023):
    rows = uruguay_schedule()
    first = sum(v[2] for y, v in rows.items() if 2028 <= y <= 2032)
    second = sum(v[2] for y, v in rows.items() if 2033 <= y <= 2037)
    pv = sum(v[2] / (1 + r) ** (y - base_year) for y, v in rows.items())
    return dict(first=first, second=second, total=first + second, pv=pv,
                share_of_principal=(first + second) / 350.0)


# ------------------------------------------------- Proposition 1: minimum reward
def min_reward(net_cost, q1, q0):
    """Minimum present value V* of the reward that makes the policy worth adopting.

    net_cost: PV of the policy's net domestic cost C - B (USD m)
    q1, q0: probability the KPI target is met with and without the policy.
    """
    return net_cost / (q1 - q0)


# ---------------------------------------- Proposition 3: bound and leverage
def rebate_value(D, step_bp, years, r=R):
    """PV of a step-down of step_bp on a bullet loan D (USD m) for `years`."""
    return D * step_bp / 1e4 * annuity(r, years)


def loan_needed(C, i, years, r=R):
    """Smallest loan whose ENTIRE interest bill, if waived, has PV >= C."""
    return C / (i * annuity(r, years))


def guarantee(G, s_bp, pd, lgd, buffer, r_buffer, years, r=R):
    """Incentive value to the government and cost to the guarantor of capacity G.

    s_bp: spread saved on guaranteed borrowing; pd: annual default probability;
    lgd: loss given default; buffer: capital held per unit exposure;
    r_buffer: annual opportunity cost of that capital.
    """
    a = annuity(r, years)
    iv = G * s_bp / 1e4 * a
    el = G * pd * lgd * a
    carry = G * buffer * r_buffer * a
    return dict(incentive=iv, expected_loss=el, carry=carry, cost=el + carry,
                ratio=iv / (el + carry))


# ----------------------------------------------- stylized coal reform
COAL = dict(gw=2.0, hours=6000, intensity=0.95)   # stylized: 2 GW retired early
POLICY_COST_PER_YEAR = 100.0                     # USD m a year, stylized
POLICY_YEARS = 10


def coal_reform(r=R):
    t_per_year = COAL['gw'] * 1e3 * COAL['hours'] * COAL['intensity'] / 1e6  # MtCO2
    pv_cost = POLICY_COST_PER_YEAR * annuity(r, POLICY_YEARS)
    return dict(mt=t_per_year, pv_cost=pv_cost,
                cost_per_t=POLICY_COST_PER_YEAR / t_per_year)


def main():
    u = uruguay_summary()
    print("URUGUAY 2023 LOAN (public terms; reward reproduced from the schedule)")
    for y, (b, bp, rw) in uruguay_schedule().items():
        print(f"  {y}: avg balance {b:6.1f}  step-down {bp:3d} bp  reward {rw:4.2f}")
    print(f"  years 1-5 max {u['first']:.1f} (published 6.7); years 6-10 max {u['second']:.1f} (published 5.8)")
    print(f"  total {u['total']:.1f} (cap 12.5) = {100*u['share_of_principal']:.1f}% of principal")
    print(f"  PV at {R:.0%} to 2023: {u['pv']:.1f}")

    c = coal_reform()
    print("\nSTYLIZED COAL REFORM")
    print(f"  emissions avoided {c['mt']:.1f} MtCO2/yr; policy cost PV {c['pv_cost']:.0f}; "
          f"cost per tonne {c['cost_per_t']:.1f} USD/t")

    print("\nPROPOSITION 1: minimum reward")
    for q0 in (0.0, 0.3, 0.6):
        print(f"  q1=0.9 q0={q0}: V* = {min_reward(c['pv_cost'], 0.9, q0):.0f}")

    print("\nSIZE COMPARISON (PV, USD m, 10 years, r=5%)")
    sll = rebate_value(1000, 100, 10)
    waiver = rebate_value(1000, 600, 10)
    print(f"  100 bp on USD 1bn: {sll:.0f}  -> implied USD/t on coal reform {sll/annuity(R,10)/c['mt']:.2f}")
    print(f"  full interest waiver (6%) on USD 1bn: {waiver:.0f}")
    print(f"  loan needed for 100 bp to match policy cost: {c['pv_cost']/(0.01*annuity(R,10)):.0f}")
    print(f"  loan needed if ALL interest (6%) waived: {loan_needed(c['pv_cost'], 0.06, 10):.0f}")
    gstar = c['pv_cost'] / (0.03 * annuity(R, 10))
    print(f"  guarantee capacity that matches the policy cost: {gstar:.0f}")
    for name, (pd_, lgd_, buf_) in CASES.items():
        g = guarantee(G=gstar, s_bp=300, pd=pd_, lgd=lgd_, buffer=buf_, r_buffer=R_BUFFER, years=10)
        gc = guarantee(G=gstar, s_bp=300, pd=pd_, lgd=lgd_, buffer=buf_, r_buffer=R_BUFFER_SENS, years=10)
        print(f"   {name}: incentive {g['incentive']:.0f}; donor cost {g['cost']:.1f}; ratio {g['ratio']:.1f}; "
              f"buffer held {buf_*gstar:.1f}; with 2% carry cost {gc['cost']:.1f} ratio {gc['ratio']:.1f}; "
              f"breakeven carry b*r_b < {(0.03 - pd_*lgd_)*1e4:.0f} bp")
    pc = 10 * c['mt'] * annuity(R, 10)
    print(f"  policy crediting at USD 10/t on the coal reform: {pc:.0f}")
    print("\nLEVERAGE SENSITIVITY (ratio incentive/donor cost; zero carry)")
    for lgd_ in (LGD, LGD_STRESS):
        for s in (150, 300, 450):
            for pd in (0.0077, 0.01, 0.03, 0.05):
                print(f"  L={lgd_:.3f} s={s}bp pd={pd:.4f}: {guarantee(1, s, pd, lgd_, 0, R_BUFFER, 10)['ratio']:.1f}")


if __name__ == "__main__":
    main()
