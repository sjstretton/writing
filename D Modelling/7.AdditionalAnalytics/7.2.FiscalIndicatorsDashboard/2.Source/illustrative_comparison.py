"""Illustrative comparison for the Fiscal Indicators Dashboard paper (7.2; the v0.1 docstring said 5.3).

Reads the dashboard's built panel (global_data_wide.csv, compiled from public datasets: IMF WEO,
IMF WoRLD 2026, IMF fossil fuel subsidy data for 2024 from the 2025 update, Ember) and reproduces the dashboard's scoring:
a direction-aware 5th-95th percentile rescale to 1-10 across all economies in the panel.

    PANEL=/home/user/climate-fiscal-ai-tools/TaxMacroFiscalDashboard/build/output/global_data_wide.csv \
        python3 illustrative_comparison.py
"""
import os
import pandas as pd

PANEL = os.environ.get(
    "PANEL", "/home/user/climate-fiscal-ai-tools/TaxMacroFiscalDashboard/build/output/global_data_wide.csv")
w = pd.read_csv(PANEL)
ISO = ["COL", "IDN", "MAR", "ZAF"]
# indicator, direction (+1 high = better, -1 high = worse, 0 magnitude read as high = more)
IND = [("tax_revenue_pct_gdp", 1), ("gross_debt_pct_gdp", -1), ("interest_to_revenue_pct", -1),
       ("excise_revenue_pct_of_revenue", 0), ("ff_subsidy_explicit_pct_gdp", 0),
       ("ff_subsidy_implicit_pct_gdp", 0), ("price_gasoline_usd_litre", 0),
       ("renewable_share_electricity_pct", 1)]


def score(v, lo, hi, d):
    x = min(max(v, lo), hi)
    s = 1 + 9 * (x - lo) / (hi - lo)
    return s if d >= 0 else 1 + 9 * (hi - x) / (hi - lo)


rows = []
for code, d in IND:
    col = w[code].dropna()
    lo, hi = col.quantile(0.05), col.quantile(0.95)
    r = {"indicator": code, "n": len(col), "p5": round(lo, 2), "p95": round(hi, 2)}
    for iso in ISO:
        rec = w.loc[w.iso3 == iso].iloc[0]
        v, y = rec[code], rec.get(code + "__year")
        r[iso] = f"{v:.2f} ({score(v, lo, hi, d):.1f}) [{int(y) if pd.notna(y) else ''}]"  # 2 decimals: gasoline prices
    rows.append(r)
pd.set_option("display.width", 250)
print("value (score 1-10) [year]; magnitudes scored high = more")
print(pd.DataFrame(rows).to_string(index=False))
