"""Paper 6.5, section "A country run: Kenya" (Table 5): the tool's Kenya run (illustrative results from the tool, not official estimates).

Reads, without modifying, two output files of the Climate Fiscal AI Tools repository:
  * MacFiscEnergyScenarioProto/MacroFiscalModels/results/integrated_results.csv (row KEN):
    budget need, pricing screen, macro model, debt paths, cross-check, debt risk rating;
  * MacFiscEnergyScenarioProto/InvestmentNeeds/national_model/results/nmim_summary_v0_2.csv
    (row KEN): 2030 investment on the net zero and current-trends paths, payer split, emissions.
The tool's Kenya briefing (briefings/Kenya_briefing.md, 20 Oct 2026) reports the same numbers.

    python3 kenya_run.py [--tools /home/user/climate-fiscal-ai-tools]
"""
import argparse
import csv
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--tools", default="/home/user/climate-fiscal-ai-tools")
root = Path(ap.parse_args().tools) / "MacFiscEnergyScenarioProto"


def row(path, key, iso="KEN"):
    with open(path) as f:
        for r in csv.DictReader(f):
            if r[key] == iso:
                return r


ir = row(root / "MacroFiscalModels/results/integrated_results.csv", "iso3")
nm = row(root / "InvestmentNeeds/national_model/results/nmim_summary_v0_2.csv", "iso")
gdp = float(nm["gdp_2030"])
pct = lambda k: 100 * float(nm[k]) / gdp
print(f"2030 GDP USD {gdp:.1f} bn; WACC {100 * float(nm['wacc']):.2f}%")
print(f"investment net zero {pct('inv2_2030'):.2f}% GDP (USD {float(nm['inv2_2030']):.2f} bn); "
      f"current trends {pct('inv1_2030'):.2f}%; incremental {pct('dinv_2030'):.2f}%")
print(f"emissions 2030: baseline {float(nm['ghg1_2030']):.1f}, net zero {float(nm['ghg2_2030']):.1f} MtCO2e "
      f"({100 * (1 - float(nm['ghg2_2030']) / float(nm['ghg1_2030'])):.0f}% lower)")
for i, lab in enumerate(["P1 pure public", "P2 utility", "P3 contracted", "P4 viability gap", "P5 private"], 1):
    print(f"  {lab}: {pct(f'typ{i}_2030'):.2f}% GDP")
print(f"direct budget need 2030 {pct('bud_2030'):.2f}% GDP (USD {float(nm['bud_2030']):.2f} bn)")
keys = ["model", "model_reason", "budget_need_2030_pct_gdp", "budget_capital_2030_pct_gdp",
        "budget_spending_2030_pct_gdp", "pricing_tau_t", "pricing_binding", "pricing_abatement_pct",
        "pricing_revenue_2030_pct_gdp", "pricing_share_of_need_pct", "financing_gap_2030_pct_gdp",
        "debt_2024_pct_gdp", "gdp_dev_2030_pct", "gdp_dev_2050_pct", "debt_2030_pct_gdp",
        "debt_2050_pct_gdp", "debt_change_2050_pp", "alt_model", "alt_gdp_dev_2050_pct",
        "alt_debt_2050_pct_gdp", "energy_saving_2050_pct_gdp", "dsf_rating_base",
        "dsf_rating_programme", "dsf_capacity", "dsf_ci", "dsf_assumptions"]
for k in keys:
    print(f"{k}: {ir[k]}")
