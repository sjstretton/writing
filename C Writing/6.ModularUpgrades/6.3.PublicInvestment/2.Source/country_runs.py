"""Paper 4.6, section 6: country runs (illustrative results from the tools, not official estimates).

Run:  python3 country_runs.py  [--tools PATH_TO_climate-fiscal-ai-tools] [--cdpm PATH_TO_CPAT-CDPM]

1. Investment-needs model v1.1 (Climate Fiscal AI Tools,
   MacFiscEnergyScenarioProto/InvestmentNeeds/Mitigation_Investment_Needs_v1.1.xlsx,
   sheet Results_Country): 2030 investment, incremental investment and its
   incremental cost under the three lenses for Kenya, Uganda and St. Lucia.
2. SISEPUEDE run for Uganda, October 2025 (CPAT-CDPM, MainProjectFolder/9. CPAT-LTS
   Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413/cba_results.csv
   and the run's input-output file for GDP): cost-benefit lines summed over
   2025-2050, net present values at 6, 7 and 8.5 percent (base 2025), technical
   cost by sector, and the share of benefits a budget or utility could see as cash.
   SISEPUEDE time_period 0 = 2015.

Outputs: country_runs_lenses.csv, country_runs_uganda.csv (and printed checks).
"""

from pathlib import Path
import argparse
import csv

import openpyxl
import pandas as pd

HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
ap.add_argument("--tools", default="/home/user/climate-fiscal-ai-tools")
ap.add_argument("--cdpm", default="/home/user/cpmodelai/CPAT-CDPM")
args = ap.parse_args()

# ---- 1. Investment-needs lenses -------------------------------------------------
wb = openpyxl.load_workbook(Path(args.tools) / "MacFiscEnergyScenarioProto/InvestmentNeeds/"
                            "Mitigation_Investment_Needs_v1.1.xlsx", read_only=True, data_only=True)
rows = list(wb["Results_Country"].iter_rows(values_only=True))
hdr = list(rows[3])
out = []
for r in rows[4:]:
    if r[0] in ("KEN", "UGA", "LCA"):
        d = dict(zip(hdr, r))
        out.append(dict(country=d["Country"], income=d["WB income"],
                        gdp_2030_bn=round(d["GDP 2030 (USD bn)"], 1),
                        invest_bn=round(d["Total investment I"], 3), invest_pct_gdp=round(100 * d["I, % GDP"], 1),
                        incr_invest_bn=round(d["Incremental investment dI"], 3),
                        incr_pct_gdp=round(100 * d["dI, % GDP"], 2),
                        wacc_pct=round(100 * d["Market WACC (a)"], 1), wacc_source=d["WACC source"],
                        cost_a_m=round(1000 * d["Incr. cost (a) market"], 1),
                        cost_b_m=round(1000 * d["Incr. cost (b) WB rate"], 1),
                        cost_c_m=round(1000 * d["Incr. cost (c) WB + local co-ben."], 1),
                        pima_invest_bn=round(d["PIMA-adjusted I"], 3), pim_gap=d["PIM efficiency gap"]))
with open(HERE / "country_runs_lenses.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0]))
    w.writeheader()
    w.writerows(out)
for o in out:
    print(o)

# ---- 2. SISEPUEDE Uganda run -----------------------------------------------------
run = Path(args.cdpm) / "MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413"
d = pd.read_csv(run / "cba_results.csv")
d["year"] = d.time_period + 2015
d["cat"] = d.variable.str.split(":").str[2]
d["sec"] = d.variable.str.split(":").str[1]
x = d[(d.year >= 2025) & (d.year <= 2050)]
names = {"PFLO:NZ": "Net zero", "PFLO:NDC_2_2020_TUNED": "NDC 2.0 from 2020", "PFLO:NDC_2_2025_TUNED": "NDC 2.0 from 2025"}
cash = ["fuel_cost", "system_cost", "technical_savings"]
res = []
for code, name in names.items():
    s = x[x.strategy_code == code]
    bycat = s.groupby("cat").value.sum() / 1e9
    benefits = bycat[bycat > 0].sum()
    row = dict(strategy=name, technical_cost_bn=round(bycat["technical_cost"], 1),
               benefits_bn=round(benefits, 1), cash_benefits_bn=round(bycat[cash].sum(), 1),
               cash_share_pct=round(100 * bycat[cash].sum() / benefits, 1),
               net_undiscounted_bn=round(s.value.sum() / 1e9, 1))
    for r in (0.06, 0.07, 0.085):
        row[f"npv_{int(r * 1000)}_bn"] = round((s.value / (1 + r) ** (s.year - 2025)).sum() / 1e9, 1)
    tc = s[s.cat == "technical_cost"].groupby("sec").value.sum()
    row["power_share_of_tech_cost_pct"] = round(100 * tc.get("entc", 0) / tc.sum(), 1)
    res.append(row)
with open(HERE / "country_runs_uganda.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(res[0]))
    w.writeheader()
    w.writerows(res)
for r in res:
    print(r)

nz = x[(x.strategy_code == "PFLO:NZ") & (x.cat == "technical_cost")]
print("NZ technical cost by sector (USD bn):", (nz.groupby("sec").value.sum() / 1e9).round(1).sort_values().to_dict())
g = pd.read_csv(run / "sisepuede_ide_run_2025-10-29T19;49;25.722413.csv", usecols=["primary_id", "time_period", "gdp_mmm_usd"])
g = g[g.primary_id == 0].set_index("time_period").gdp_mmm_usd
tcy = nz.groupby("time_period").value.sum() / 1e9
for y in (2030, 2050):
    print(f"NZ technical cost {y}: {-tcy[y - 2015]:.1f} bn = {-100 * tcy[y - 2015] / g[y - 2015]:.1f}% of the run's GDP")
