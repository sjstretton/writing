"""Paper 6.2, "The CBAM Policy Tool": Egypt application (illustrative tool results).

Run from this folder:  python3 egypt_example.py   (add --refetch to re-query Eurostat)

v0.2 (31 Oct 2026), after the peer review (../5.Notes/PeerReview-2026-10-31.md):
  * EU import volumes are now Eurostat's public record (EU imports from Egypt,
    2024 and 2025, data/eurostat_eu_imports_from_eg.csv), not the tool's own
    volume estimates, which differed widely (urea 1,600 kt in the tool against
    2,557 kt recorded for 2024; hot-rolled flat steel 364 against 696 kt).
  * Two corrections bring the tool's fertilizer factors into line with the
    CBAM rules (Implementing Regulation (EU) 2025/2547):
      - urea: the CO2 bound in urea (44/60 = 0.733 t/t) is counted as emitted.
        Annex II point B.8.2 lets CO2 used in a product count as not emitted
        only if it is "permanently chemically bound"; urea releases it when
        applied to soil (IPCC 2006, Vol. 4, ch. 11.4). The tool deducted it.
      - ammonium nitrate: both nitrogen atoms come from ammonia (one through
        nitric acid, a CBAM precursor), so a tonne of AN embeds 34/80 = 0.425 t
        of ammonia, not the 17/80 = 0.2125 t the tool counted.
  * Steel sensitivity: the tool's gas-based DRI-EAF factor (0.73 tCO2/t in
    workbook v1.2) against its v1.1 value (1.63) and against Iran's EU default
    for CN 7208 (1.94), the closest gas-DRI producer with a country default.
  * "Best declaration": each product declared at the lower of the default and
    the estimate (a producer above the default keeps the default).

Inputs:
  * Egypt_CBAM_EF_v1.2.xlsx, sheet EF, Section C (CN lines): the tool's
    bottom-up CBAM-relevant intensity ("CBAM-equiv", tCO2e/t) and its line
    volumes, used only to weight lines within a product (route mix).
    Illustrative results from the CBAM Policy Tool's Egypt application (2026),
    not official estimates.
  * 'DVs as adopted_v20260204_.xlsx' (Commission workbook for Implementing
    Regulation (EU) 2025/2621): Egypt sheet; where Egypt has no value (all
    carbon steel), the "Other Countries and Territories" sheet, which applies.
    Direct emissions for steel and aluminium; total for cement and fertilisers.
Full phase-in (2034): no free-allocation adjustment. Mark-up 30 percent (steel,
cement, aluminium), 1 percent (fertilisers). Stylized certificate price
EUR 80/tCO2. Volumes held at the year shown.

Outputs: table_egypt.csv, table_egypt_sensitivity.csv (and printed totals).
"""

from pathlib import Path
import csv
import json
import sys
import urllib.request

import openpyxl

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA = HERE / "data"
P_EU = 80.0
YEAR = "2025"
UREA_BOUND_CO2 = 44.0 / 60.0          # t CO2 per t urea, stoichiometric
NH3_IN_AN_MISSING = 17.0 / 80.0       # t NH3 per t AN via nitric acid, omitted by the tool
NH3_LINE = "Anhydrous ammonia"        # tool line whose factor is ammonia's full EF
DRI_LINES = {"Flat-rolled HRC, hot-rolled, not clad (DRI-route share)", "Bars and rods, rebar (DRI-route long)"}
STEEL_CASES = [("Tool v1.2 (0.73)", None), ("Tool v1.1 (1.63)", 1.627), ("Iran's EU default (1.94)", 1.94)]

# name, tool lines (route mix), Eurostat CN codes, default sheet, default CN, mark-up, correction
PRODUCTS = [
    ("Hot-rolled flat steel", ["Flat-rolled HRC, hot-rolled, not clad (DRI-route share)", "Flat HRC, scrap-EAF route share"],
     ["7208"], "Other", "7208", 0.30, None),
    ("Long steel", ["Bars and rods, rebar (DRI-route long)", "Bars and rods, rebar (scrap-route)",
                    "Wire rod in coils (scrap-route)", "Angles, shapes and sections (scrap-route)"],
     ["7213", "7214", "7216"], "Other", "7214 20 00", 0.30, None),
    ("Cement clinker", ["Cement clinker"], ["252310"], "Egypt", "2523 10 00", 0.30, None),
    ("Anhydrous ammonia", ["Anhydrous ammonia"], ["281410"], "Egypt", "28141000", 0.01, None),
    ("Urea", ["Urea (≥45% N)"], ["310210"], "Egypt", "3102 10 19", 0.01, "urea"),
    ("Ammonium nitrate", ["Ammonium nitrate"], ["310230"], "Egypt", "3102 30 90", 0.01, "an"),
    ("Unwrought aluminum", ["Unwrought aluminium, not alloyed", "Unwrought aluminium alloys"],
     ["7601"], "Egypt", "7601", 0.30, None),
]


def refetch():
    """Re-query Eurostat Comext (EU imports from Egypt) and rewrite the data CSV."""
    base = ("https://ec.europa.eu/eurostat/api/comext/dissemination/statistics/1.0/data/DS-045409"
            "?format=JSON&freq=A&reporter=EU&partner=EG&flow=1&indicators=QUANTITY_IN_100KG"
            "&indicators=VALUE_IN_EUROS&time=2024&time=2025&lang=en&product=")
    rows = []
    for cn in sorted({c for p in PRODUCTS for c in p[2]}):
        d = json.load(urllib.request.urlopen(base + cn, timeout=60))
        ind = d["dimension"]["indicators"]["category"]["index"]
        tim = d["dimension"]["time"]["category"]["index"]
        nt = len(tim)
        for y, j in tim.items():
            q = d["value"].get(str(ind["QUANTITY_IN_100KG"] * nt + j))
            v = d["value"].get(str(ind["VALUE_IN_EUROS"] * nt + j))
            rows.append(dict(cn=cn, year=y, quantity_t=round(q / 10, 3) if q else 0, value_eur=v or 0,
                             source="Eurostat Comext DS-045409, reporter EU, partner EG, flow import"))
    with open(DATA / "eurostat_eu_imports_from_eg.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def volumes():
    out = {}
    for r in csv.DictReader(open(DATA / "eurostat_eu_imports_from_eg.csv")):
        out[(r["cn"], r["year"])] = float(r["quantity_t"]) / 1000.0     # kt
    return out


def tool_lines():
    wb = openpyxl.load_workbook(ROOT / "Egypt_CBAM_EF_v1.2.xlsx", data_only=True)
    rows = list(wb["EF"].iter_rows(values_only=True))
    hdr = [str(h).replace("\n", " ") if h else "" for h in rows[4]]
    i_prod, i_eq, i_eu = hdr.index("Product"), hdr.index("CBAM- equiv"), hdr.index("EU exp kt")
    out = {}
    for r in rows[39:]:          # Section C
        if r[i_prod] and isinstance(r[i_eq], (int, float)):
            out[r[i_prod]] = (float(r[i_eq]), float(r[i_eu] or 0))
    return out


def defaults():
    wb = openpyxl.load_workbook(ROOT / "DVs as adopted_v20260204_.xlsx", read_only=True, data_only=True)
    res = {}
    for sheet, key in (("Egypt", "Egypt"), ("_Other Countries and Territorie", "Other")):
        for r in wb[sheet].iter_rows(values_only=True):
            if r[0] is None:
                continue
            cn = str(r[0]).strip()
            if cn == "2523 10 00" and "Grey" not in str(r[1] or ""):
                continue
            total = r[4] if isinstance(r[4], (int, float)) else None
            direct = r[2] if isinstance(r[2], (int, float)) else None
            res[(key, cn)] = (direct, total)
    return res


def intensity(lines, members, corr, dri=None):
    """Tool intensity for a product: line factors weighted by the tool's route mix, with rule corrections."""
    w = sum(lines[m][1] for m in members)
    e = sum((dri if (dri is not None and m in DRI_LINES) else lines[m][0]) * lines[m][1] for m in members) / w
    if corr == "urea":
        e += UREA_BOUND_CO2
    elif corr == "an":
        e += NH3_IN_AN_MISSING * lines[NH3_LINE][0]
    return e


def table(lines, dv, vol, year, dri=None):
    rows = []
    for name, members, cns, sheet, dcn, mk, corr in PRODUCTS:
        q = sum(vol[(c, year)] for c in cns)
        e_raw = intensity(lines, members, None, dri)
        e = intensity(lines, members, corr, dri)
        direct, total = dv[(sheet, dcn)]
        base = direct if dcn.startswith(("72", "76")) else total
        d_mk = base * (1 + mk)
        c_def, c_est = P_EU * d_mk, P_EU * e
        rows.append(dict(product=name, eurostat_cn="+".join(cns), default_cn=dcn, default_sheet=sheet,
                         eu_imports_kt=round(q), tool_estimate_as_published=round(e_raw, 2),
                         estimate_cbam_rules=round(e, 2), default_before_markup=round(base, 2),
                         default_with_markup=round(d_mk, 2), charge_default_eur_t=round(c_def),
                         charge_estimate_eur_t=round(c_est), charge_default_eur_m=round(c_def * q / 1000, 1),
                         charge_estimate_eur_m=round(c_est * q / 1000, 1),
                         charge_best_eur_m=round(min(c_def, c_est) * q / 1000, 1)))
    return rows


def totals(rows):
    return {k: round(sum(r[k] for r in rows), 1) for k in
            ("eu_imports_kt", "charge_default_eur_m", "charge_estimate_eur_m", "charge_best_eur_m")}


def main():
    lines, dv, vol = tool_lines(), defaults(), volumes()
    rows = table(lines, dv, vol, YEAR)
    with open(HERE / "table_egypt.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    for r in rows:
        print(r)
    for y in ("2024", "2025"):
        t = totals(table(lines, dv, vol, y))
        steel = [r for r in table(lines, dv, vol, y) if "steel" in r["product"]]
        print(y, t, "steel default/estimate EUR m:",
              round(sum(r["charge_default_eur_m"] for r in steel), 1),
              round(sum(r["charge_estimate_eur_m"] for r in steel), 1))
    sens = []
    for label, dri in STEEL_CASES:
        for y in ("2024", "2025"):
            st = [r for r in table(lines, dv, vol, y, dri) if "steel" in r["product"]]
            sens.append(dict(case=label, year=y,
                             hot_rolled_estimate=st[0]["estimate_cbam_rules"], long_estimate=st[1]["estimate_cbam_rules"],
                             steel_charge_default_eur_m=round(sum(r["charge_default_eur_m"] for r in st), 1),
                             steel_charge_estimate_eur_m=round(sum(r["charge_estimate_eur_m"] for r in st), 1)))
    with open(HERE / "table_egypt_sensitivity.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(sens[0]))
        w.writeheader()
        w.writerows(sens)
    for s in sens:
        print(s)


if __name__ == "__main__":
    if "--refetch" in sys.argv:
        refetch()
    main()
