"""Paper 5.1, Section 7: Sierra Leone and Liberia applications of the diagnostic.

Reads the diagnostic's cross-country workbook (Climate Fiscal AI Tools, private
repository) and writes the Level 1 metrics and standard-schedule lines used in
Table 5 to country_metrics_SLE_LBR.csv, plus the carbon component of the
externality spine for comparison.

Run from this folder:
    python3 country_metrics.py [path/to/Excise_Diagnostic_CrossCountry.xlsx]

Only the diagnostic's own measures and results are used (sheets Country_Metrics,
Std_Schedule, Parameters). Uganda is not used: its run was not peer reviewed.
Illustrative results from the diagnostic, not official estimates.
"""

import csv
import sys
from pathlib import Path

import openpyxl

HERE = Path(__file__).resolve().parent
DEFAULT = Path("/home/user/climate-fiscal-ai-tools/ExciseDiagnostic/Excise_Diagnostic_CrossCountry.xlsx")
METRICS = ["X1", "X2", "X6", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9",
           "I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9", "B2", "B3", "B4", "B5",
           "Q1", "Q4", "Q5", "Q6"]
LINES = ["E1", "E2", "E3", "T1", "A1", "A4", "A5", "S1"]

# Carbon component of the spine (equation 4, Table 1): kg CO2 per liter x USD 50/t
CO2_KG_PER_L = {"petrol": 2.31, "diesel": 2.68}
CARBON_PRICE = 50.0


def main(path):
    wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
    out = []
    rows = list(wb["Country_Metrics"].iter_rows(values_only=True))
    for r in rows[4:]:
        if r[1] in METRICS:
            out.append(dict(kind="metric", id=r[1], item=r[2], unit=r[3],
                            SLE=r[4], SLE_dq=r[6], LBR=r[12], LBR_dq=r[14], reference=r[16]))
    rows = list(wb["Std_Schedule"].iter_rows(values_only=True))
    for r in rows[5:]:
        if r[2] in LINES:
            out.append(dict(kind="line", id=r[2], item=r[3], unit=r[4],
                            SLE=f"{r[6]} | USD {r[7]} | {r[8]}", SLE_dq=r[9],
                            LBR=f"{r[18]} | USD {r[19]} | {r[20]}", LBR_dq=r[21], reference=""))
    for fuel, kg in CO2_KG_PER_L.items():
        out.append(dict(kind="spine", id=f"eC_{fuel}", item=f"Carbon component, {fuel}",
                        unit="USD per liter", SLE=round(kg / 1000 * CARBON_PRICE, 3), SLE_dq="",
                        LBR=round(kg / 1000 * CARBON_PRICE, 3), LBR_dq="", reference="USD 50/tCO2"))
    with open(HERE / "country_metrics_SLE_LBR.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)
    for o in out:
        print(o["id"], "|", o["item"], "| SLE:", o["SLE"], "| LBR:", o["LBR"])


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT)
