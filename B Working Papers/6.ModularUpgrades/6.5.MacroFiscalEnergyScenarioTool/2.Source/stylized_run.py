"""Stylized run for the Macro-Fiscal-Energy Scenario Tool paper (5.2).

Runs the tool's GIMF-lite and DIGNAD-lite at their DEFAULT, ILLUSTRATIVE calibrations (no country
data) on a stylized programme: extra public green investment of 1% of GDP a year for ten years.
Also evaluates the PriceFeasibility formulas for a stylized power sector.

The models live in the private Climate Fiscal AI Tools repository; point MFM_PATH at its
MacFiscEnergyScenarioProto/MacroFiscalModels folder. Nothing in that repository is modified.

    MFM_PATH=/home/user/climate-fiscal-ai-tools/MacFiscEnergyScenarioProto/MacroFiscalModels \
        python3 stylized_run.py
"""
import os
import sys
from dataclasses import replace
import numpy as np

sys.path.insert(0, os.environ.get(
    "MFM_PATH", "/home/user/climate-fiscal-ai-tools/MacFiscEnergyScenarioProto/MacroFiscalModels"))
import gimf_lite as gm      # noqa: E402
import dignad_lite as dg    # noqa: E402

PROG = [0.01] * 10          # 1% of GDP a year, years 1-10, then zero
YEARS = [1, 5, 10, 20, 40]


def gimf(label, p, **kw):
    out, ss0, ssT, cal = gm.solve(p, **kw)
    g = [100 * (out["y"][t - 1] - 1) for t in YEARS]
    d = [100 * out["debt_gdp"][t - 1] for t in YEARS]
    print(f"{label:46s} GDP%: " + " ".join(f"{x:6.2f}" for x in g)
          + " | debt%GDP: " + " ".join(f"{x:5.1f}" for x in d))


def dignad(label, p):
    o, ss, *_ = dg.solve(p)
    g = [100 * (o["y"][t - 1] / ss["y"] - 1) for t in YEARS]
    d = [100 * o["debt_gdp"][t - 1] for t in YEARS]
    print(f"{label:46s} GDP%: " + " ".join(f"{x:6.2f}" for x in g)
          + " | debt%GDP: " + " ".join(f"{x:5.1f}" for x in d))


print("Years:", YEARS)
print("GIMF-lite, default illustrative calibration (debt target 50% of GDP)")
p = gm.Params()
gimf("Debt financed (rule closes with transfers)", p, ig_extra=PROG + [0.0])
gimf("Tax financed (labour tax, no new debt)", replace(p, dfs=0.0, instrument="tau_l"), ig_extra=PROG + [0.0])
gimf("Debt financed, 0.5% of GDP carbon revenue", p, ig_extra=PROG + [0.0], rev_extra=[0.005] * 10 + [0.0])
gimf("Debt financed, efficiency s = 0.5 not 0.7", replace(p, s=0.5), ig_extra=PROG + [0.0])

print("DIGNAD-lite, default illustrative calibration, no disaster")
q = dg.Params(eps_k=0.0, eps_g=0.0, eps_a=0.0, rec=0.0, prog=tuple(PROG))
dignad("30% grants, 30% concessional, 40% commercial", q)
dignad("No grants or concessional loans", replace(q, sh_grant=0.0, sh_conc=0.0))

# PriceFeasibility formulas (README), stylized power sector
print("\nPriceFeasibility, stylized power sector")
s_max, tau_switch = 0.40, 40.0      # max substitution share; switching price, USD/t
e_avg, e_hi = 0.60, 0.95            # tCO2/MWh: average grid, coal-and-oil generators
phi, p_res, p_whole = 0.6, 150.0, 90.0   # pass-through; residential tariff, wholesale price USD/MWh
elast, b40, q40, res_share = 0.3, 0.03, 0.2, 0.35
phase = 3


def metrics(tt, tf, rebate=0.0):
    tm = tt + tf
    a_sub = s_max * (1 - np.exp(-tm / tau_switch))
    dp = phi * e_avg * tt / p_res
    a_dem = elast * dp
    E = 1 - (1 - a_sub) * (1 - a_dem)
    F1 = 100 * dp / phase
    F2 = 100 * b40 * dp * (1 - min(rebate / (phi * res_share * q40), 1))
    F3 = 100 * (tt * e_hi * (1 - phi) + tf * (e_hi - e_avg)) / p_whole
    return 100 * E, F1, F2, F3


for name, tt, tf in [("Tax 50", 50, 0), ("Feebate 50", 0, 50), ("Tax 25 + feebate 25", 25, 25)]:
    E, F1, F2, F3 = metrics(tt, tf)
    print(f"{name:22s} abatement {E:5.1f}%  F1 {F1:4.1f}%  F2 {F2:4.2f}%  F3 {F3:4.1f}%")

# best feasible mixes under two sets of limits (no rebate). Placeholder limits, as in the tool.
for lim in [(10, 0.5, 15), (2, 0.5, 15)]:
    best = {}
    for tt in range(0, 201):
        for tf in range(0, 201):
            E, F1, F2, F3 = metrics(tt, tf)
            if F1 <= lim[0] and F2 <= lim[1] and F3 <= lim[2]:
                for k, ok in (("tax", tf == 0), ("feebate", tt == 0), ("hybrid", True)):
                    if ok and E > best.get(k, (-1,))[0]:
                        best[k] = (E, tt, tf, F1, F2, F3)
    print(f"Limits F1 <= {lim[0]}%, F2 <= {lim[1]}%, F3 <= {lim[2]}%")
    for k, v in best.items():
        print(f"  best {k:8s} abatement {v[0]:5.1f}%  tax {v[1]:3d}  feebate {v[2]:3d}"
              f"  F1 {v[3]:4.1f}  F2 {v[4]:4.2f}  F3 {v[5]:4.1f}")
