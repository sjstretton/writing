"""Spot-check of Table 2 (paper 7.2) against the publishers' own public releases, 31 Oct 2026.

Reads, without any login or personal data:
  - IMF DataMapper API (World Economic Outlook and Fiscal Monitor, October 2026 vintage): gross debt, GDP in US dollars,
    revenue, overall balance and primary balance, general government;
  - IMF SDMX API, dataflow IMF.FAD/WORLD (WoRLD, release of 18 Feb 2026): taxes, excises and total revenue;
  - Ember yearly electricity data (long format CSV): share of renewables in generation.
and recomputes the dashboard's derived indicators and its 1-10 scores with the percentile bounds printed by
illustrative_comparison.py (the panel itself sits in the private tools repository).

    python3 check_public_sources.py            # prints the comparison; output kept in check_public_sources_output.txt
"""
import io
import json
import urllib.request

import pandas as pd

ISO = ["COL", "IDN", "MAR", "ZAF"]
UA = {"User-Agent": "curl/8.5.0"}


def get(url, accept=None):
    h = dict(UA)
    if accept:
        h["Accept"] = accept
    with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=180) as r:
        return r.read()


def datamapper(ind, year="2024"):
    v = json.loads(get(f"https://www.imf.org/external/datamapper/api/v1/{ind}"))["values"][ind]
    return {iso: v.get(iso, {}).get(year) for iso in ISO}


# Panel values (Table 2 of working paper v0.1) and the panel's 5th/95th percentiles (illustrative_comparison_output.txt)
PANEL = {"tax": [23.0, 10.1, 20.8, 25.2], "debt": [61.0, 40.2, 67.7, 76.0], "itr": [13.5, 15.1, 7.9, 18.9],
         "excise_share": [3.0, 8.6, 6.9, 7.8], "ffs_exp": [0.4, 3.0, 1.9, 0.0], "ffs_imp": [5.4, 9.2, 5.0, 12.9],
         "renew": [79.9, 28.0, 29.5, 7.0]}
BOUNDS = {"tax": (4.64, 29.96, 1), "debt": (14.29, 132.86, -1), "itr": (0.25, 25.75, -1)}


def score(x, lo, hi, d):
    x = min(max(x, lo), hi)
    return 1 + 9 * ((x - lo) if d > 0 else (hi - x)) / (hi - lo)


out = []
# 1. WEO / Fiscal Monitor, October 2026
debt = datamapper("GGXWDG_NGDP")
gdp = datamapper("NGDPD")
pb, rev, nb = datamapper("GGXONLB_G01_GDP_PT"), datamapper("GGR_G01_GDP_PT"), datamapper("GGXCNL_G01_GDP_PT")
itr = {i: 100 * (pb[i] - nb[i]) / rev[i] for i in ISO}

# 2. WoRLD (IMF.FAD, SDMX): taxes (G11), excises (G1142), revenue (G1), % of GDP
key = "+".join(ISO) + ".G11_POGDP_PT_R+G1142_POGDP_PT_R+G1_POGDP_PT_R.*.A"
w = pd.read_csv(io.BytesIO(get(f"https://api.imf.org/external/sdmx/2.1/data/IMF.FAD,WORLD/{key}?startPeriod=2022",
                               "application/vnd.sdmx.data+csv;version=1.0.0")))
w = w[["COUNTRY", "INDICATOR", "TIME_PERIOD", "OBS_VALUE", "SECTOR"]]


def world(iso, ind):
    s = w[(w.COUNTRY == iso) & (w.INDICATOR == ind)].dropna(subset=["OBS_VALUE"]).sort_values("TIME_PERIOD")
    return s.iloc[-1] if len(s) else None


# 3. Ember, renewables share of generation, 2024
e = pd.read_csv(io.BytesIO(get("https://storage.googleapis.com/emb-prod-bkt-publicdata/public-downloads/"
                               "yearly_full_release_long_format.csv")), low_memory=False)
e = e[(e["ISO 3 code"].isin(ISO)) & (e.Year == 2024) & (e.Category == "Electricity generation") & (e.Unit == "%")
      & (e.Variable == "Renewables")].set_index("ISO 3 code")["Value"]

# IMF fossil fuel subsidies, 2025 update (WP/25/270), Annex III, 2024: US$ billion and the IMF's own % of GDP
IMF_FFS = {"IDN": (42, 2.7, 128, 8.5), "MAR": (3, 1.8, 8, 4.8), "ZAF": (0, 0.0, 52, 11.9)}

rows = []
for k, iso in enumerate(ISO):
    tx, ex, rv = world(iso, "G11_POGDP_PT_R"), world(iso, "G1142_POGDP_PT_R"), world(iso, "G1_POGDP_PT_R")
    ex_rev = w[(w.COUNTRY == iso) & (w.INDICATOR == "G1_POGDP_PT_R") & (w.TIME_PERIOD == ex.TIME_PERIOD)].OBS_VALUE
    r = {"iso": iso,
         "tax WoRLD (panel)": f"{tx.OBS_VALUE:.1f} {int(tx.TIME_PERIOD)} {tx.SECTOR} ({PANEL['tax'][k]})",
         "tax score": round(score(tx.OBS_VALUE, *BOUNDS['tax']), 1),
         "debt WEO Oct26 (panel)": f"{debt[iso]:.1f} ({PANEL['debt'][k]})",
         "debt score": round(score(debt[iso], *BOUNDS['debt']), 1),
         "net int/rev (panel)": f"{itr[iso]:.1f} ({PANEL['itr'][k]})",
         "itr score": round(score(itr[iso], *BOUNDS['itr']), 1),
         "gross int/rev*": None,
         "excise %GDP": f"{ex.OBS_VALUE:.2f} {int(ex.TIME_PERIOD)}",
         "excise/revenue (panel)": f"{100 * ex.OBS_VALUE / ex_rev.iloc[0]:.1f} ({PANEL['excise_share'][k]})",
         "renewables Ember 2024 (panel)": f"{e.get(iso, float('nan')):.1f} ({PANEL['renew'][k]})"}
    if iso in IMF_FFS:
        a, ap, b, bp = IMF_FFS[iso]
        r["FFS exp/imp: US$bn/WEO GDP; IMF %; (panel)"] = (f"{100 * a / gdp[iso]:.1f}/{100 * b / gdp[iso]:.1f}; "
                                                         f"{ap}/{bp}; ({PANEL['ffs_exp'][k]}/{PANEL['ffs_imp'][k]})")
    rows.append(r)
pd.set_option("display.width", 250)
df = pd.DataFrame(rows).drop(columns=["gross int/rev*"]).set_index("iso").T
print("Spot-check of Table 2 against public releases (values recomputed; panel values in brackets)")
print(df.to_string())
print("\nWEO GDP 2024, US$ billion:", {i: round(gdp[i], 1) for i in ISO})
print("Fiscal Monitor 2024, % of GDP: primary balance", {i: round(pb[i], 2) for i in ISO},
      "overall balance", {i: round(nb[i], 2) for i in ISO}, "revenue", {i: round(rev[i], 2) for i in ISO})
