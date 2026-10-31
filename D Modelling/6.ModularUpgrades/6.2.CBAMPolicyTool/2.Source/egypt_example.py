"""Paper 4.5, "The CBAM Policy Tool": Egypt application (illustrative tool results).

Run from this folder:  python3 egypt_example.py

Inputs, read directly from the workbooks in the paper folder:
  * Egypt_CBAM_EF_v1.2.xlsx, sheet EF, Section C (CN lines): the tool's
    bottom-up CBAM-relevant intensity ("CBAM-equiv", tCO2e/t) and 2024 EU
    export volumes (kt) by CN line. These are illustrative results from the
    CBAM Policy Tool's Egypt application (2026), not official estimates.
  * 'DVs as adopted_v20260204_.xlsx' (Commission workbook for Implementing
    Regulation (EU) 2025/2621): Egypt sheet; where Egypt has no value for a
    CN code (all carbon-steel products), the "Other Countries and
    Territories" sheet, which then applies. Defaults are direct emissions for
    steel and aluminium and total (direct + indirect) for cement and
    fertilisers, matching CBAM scope.
Full phase-in (2034): no free-allocation adjustment, so benchmarks do not
matter. Mark-up 30 percent (steel, cement, aluminium) and 1 percent
(fertilisers). Stylized certificate price EUR 80/tCO2, as in the Türkiye
example. Volumes held at 2024.

Output: table_egypt.csv (and printed totals).
"""

from pathlib import Path
import csv

import openpyxl

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
P_EU = 80.0

# Tool CN lines (Section C row labels in the EF sheet) grouped into the
# products shown in the paper, with the Commission CN code whose default applies.
GROUPS = [
    ("Hot-rolled flat steel", "7208", "Other", "4.0487",
     ["Flat-rolled HRC, hot-rolled, not clad (DRI-route share)", "Flat HRC, scrap-EAF route share"], 0.30),
    ("Long steel (rebar, wire rod, sections)", "7214 20 00", "Other", None,
     ["Bars and rods, rebar (DRI-route long)", "Bars and rods, rebar (scrap-route)",
      "Wire rod in coils (scrap-route)", "Angles, shapes and sections (scrap-route)"], 0.30),
    ("Grey clinker", "2523 10 00", "Egypt", None, ["Cement clinker"], 0.30),
    ("Anhydrous ammonia", "28141000", "Egypt", None, ["Anhydrous ammonia"], 0.01),
    ("Urea", "3102 10 19", "Egypt", None, ["Urea (≥45% N)"], 0.01),
    ("Ammonium nitrate", "3102 30 90", "Egypt", None, ["Ammonium nitrate"], 0.01),
    ("Unwrought aluminum", "7601", "Egypt", None,
     ["Unwrought aluminium, not alloyed", "Unwrought aluminium alloys"], 0.30),
]


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
            desc = str(r[1] or "")
            if cn == "2523 10 00" and "Grey" not in desc:
                continue
            # columns: CN, description, direct, indirect, total, ...
            total = r[4] if isinstance(r[4], (int, float)) else None
            direct = r[2] if isinstance(r[2], (int, float)) else None
            res[(key, cn)] = (direct, total)
    return res


def main():
    lines, dv = tool_lines(), defaults()
    table, tot = [], dict(kt=0, dflt=0, act=0)
    for name, cn, sheet, _, members, mk in GROUPS:
        q = sum(lines[m][1] for m in members)
        e_tool = sum(lines[m][0] * lines[m][1] for m in members) / q
        direct, total = dv[(sheet, cn)]
        base = direct if cn.startswith(("72", "76")) else total
        d_mk = base * (1 + mk)
        c_def, c_act = P_EU * d_mk, P_EU * e_tool
        save = c_def - c_act
        table.append(dict(product=name, cn=cn, default_sheet=sheet, eu_exports_kt_2024=round(q),
                          tool_cbam_eq=round(e_tool, 2), default_before_markup=round(base, 2),
                          default_with_markup=round(d_mk, 2), charge_default_eur_t=round(c_def),
                          charge_tool_eur_t=round(c_act), saving_eur_t=round(save),
                          charge_default_eur_m=round(c_def * q / 1000, 1),
                          charge_tool_eur_m=round(c_act * q / 1000, 1)))
        tot["kt"] += q
        tot["dflt"] += c_def * q / 1000
        tot["act"] += c_act * q / 1000
    with open(HERE / "table_egypt.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(table[0]))
        w.writeheader()
        w.writerows(table)
    for r in table:
        print(r)
    all_eu = sum(v[1] for v in lines.values())
    print(f"covered EU exports {tot['kt']:.0f} kt of {all_eu:.0f} kt in the tool's CN lines")
    print(f"total charge at default EUR {tot['dflt']:.0f} m; at tool estimate EUR {tot['act']:.0f} m; "
          f"saving EUR {tot['dflt'] - tot['act']:.0f} m")
    steel = [r for r in table if "steel" in r["product"]]
    print("steel: default EUR m", sum(r["charge_default_eur_m"] for r in steel),
          "tool EUR m", sum(r["charge_tool_eur_m"] for r in steel))


if __name__ == "__main__":
    main()
