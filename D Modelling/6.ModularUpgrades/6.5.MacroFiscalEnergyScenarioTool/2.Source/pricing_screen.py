"""Paper 6.5, Table 4: the PriceFeasibility screen on a stylized power sector, with no dependence on the private
tools repository (the formulas are equations (2) and (3) of the working paper; the parameters are those of
stylized_run.py). Also reports the sensitivity in the peer review (M7): if high-emitting generators recover only the
grid-average pass-through (phi * e_avg * tau per MWh) instead of the share phi of their own carbon cost, their net
loss is tau * (e_hi - phi * e_avg) and the concentrated-loser limit F3 binds at a lower tax.

    python3 pricing_screen.py
"""
import math

S_MAX, TAU_SWITCH = 0.40, 40.0            # largest displaceable share of fossil output; switching price, USD/t
E_AVG, E_HI = 0.60, 0.95                  # tCO2/MWh: grid average; coal and oil generators
PHI, P_RES, P_WHOLE = 0.6, 150.0, 90.0    # pass-through; residential tariff and wholesale price, USD/MWh
ELAST, B40, Q40, RES_SHARE = 0.3, 0.03, 0.2, 0.35
PHASE = 3                                 # years of phase-in


def metrics(tt, tf, rebate=0.0, own_cost_recovery=True):
    a_sub = S_MAX * (1 - math.exp(-(tt + tf) / TAU_SWITCH))
    dp = PHI * E_AVG * tt / P_RES
    a_dem = ELAST * dp
    e = 1 - (1 - a_sub) * (1 - a_dem)
    f1 = 100 * dp / PHASE
    f2 = 100 * B40 * dp * (1 - min(rebate / (PHI * RES_SHARE * Q40), 1))
    unrecovered = tt * E_HI * (1 - PHI) if own_cost_recovery else tt * (E_HI - PHI * E_AVG)
    f3 = 100 * (unrecovered + tf * (E_HI - E_AVG)) / P_WHOLE
    return 100 * e, f1, f2, f3


def best(limits, **kw):
    out = {}
    for tt in range(201):
        for tf in range(201):
            e, f1, f2, f3 = metrics(tt, tf, **kw)
            if f1 <= limits[0] and f2 <= limits[1] and f3 <= limits[2]:
                for k, ok in (("tax", tf == 0), ("feebate", tt == 0), ("mix", True)):
                    if ok and e > out.get(k, (-1,))[0]:
                        out[k] = (e, tt, tf, f1, f2, f3)
    return out


def report(title, limits, **kw):
    print(f"{title}: limits F1 <= {limits[0]}%, F2 <= {limits[1]}%, F3 <= {limits[2]}%")
    for k, v in best(limits, **kw).items():
        print(f"  best {k:8s} abatement {v[0]:5.1f}%  tax {v[1]:3d}  feebate {v[2]:3d}"
              f"  F1 {v[3]:4.1f}  F2 {v[4]:4.2f}  F3 {v[5]:4.1f}")


report("Table 4, default limits", (10, 0.5, 15))
report("Table 4, tight visible price", (2, 0.5, 15))
report("Sensitivity (M7): generators recover only the grid-average pass-through", (10, 0.5, 15),
       own_cost_recovery=False)
