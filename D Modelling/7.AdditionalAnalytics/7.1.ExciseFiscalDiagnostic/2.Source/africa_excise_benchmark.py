"""Paper 7.1 (working paper v0.4): the African excise benchmark used in Sections 1, 7 and 8.

Replaces the unsourced "African average 2.4 percent of GDP (2021)" of v0.3 with a figure computed
from public data: OECD/AUC/ATAF, Revenue Statistics in Africa 2025 (DOI 10.1787/8d3bf3af-en),
OECD Data Explorer dataflows
  OECD.CTP.TPS,DSD_REV_AFRICA@DF_REV_ALL,2.0          (tax revenue by OECD category, national currency)
  OECD.CTP.TPS,DSD_REF_AFRICA@DF_REFSERIES_AFRICA,2.0  (GDP at current prices, national currency)
Excises are OECD category 5121; 5120 (taxes on specific goods and services) also includes customs
duties (5123). Means and medians are unweighted across the countries with both series.

Run:  python3 africa_excise_benchmark.py [download_dir]
Downloads the two CSV files (no credentials, no personal data) unless they are already in
download_dir, and writes africa_excise_benchmark.csv beside this script.
"""
import csv
import statistics
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = "https://sdmx.oecd.org/public/rest/data/"
FILES = {
    "all.csv": BASE + "OECD.CTP.TPS,DSD_REV_AFRICA@DF_REV_ALL,2.0/all?startPeriod=2021&endPeriod=2023&format=csvfilewithlabels",
    "ref.csv": BASE + "OECD.CTP.TPS,DSD_REF_AFRICA@DF_REFSERIES_AFRICA,2.0/all?startPeriod=2021&endPeriod=2023&format=csvfilewithlabels",
}


def main(d):
    d.mkdir(parents=True, exist_ok=True)
    for name, url in FILES.items():
        if not (d / name).exists():
            urllib.request.urlretrieve(url, d / name)
    gdp = {(x["REF_AREA"], x["TIME_PERIOD"]): float(x["OBS_VALUE"]) * 10 ** int(x["UNIT_MULT"])
           for x in csv.DictReader(open(d / "ref.csv", encoding="utf-8"))
           if x["MEASURE"] == "B1GQ_V" and x["UNIT_MEASURE"] == "XDC" and x["OBS_VALUE"]}
    out = []
    rows = [x for x in csv.DictReader(open(d / "all.csv", encoding="utf-8"))
            if x["CTRY_SPECIFIC_REVENUE"] == "_T" and x["SECTOR"] == "S13" and x["OBS_VALUE"]
            and x["STANDARD_REVENUE"] in ("T_5121", "T_5120")]
    for code in ("T_5121", "T_5120"):
        for year in ("2021", "2022", "2023"):
            v = {x["REF_AREA"]: 100 * float(x["OBS_VALUE"]) * 10 ** int(x["UNIT_MULT"]) / gdp[(x["REF_AREA"], year)]
                 for x in rows if x["STANDARD_REVENUE"] == code and x["TIME_PERIOD"] == year
                 and (x["REF_AREA"], year) in gdp}
            if not v:
                continue
            out.append(dict(category=code, year=year, countries=len(v), mean=round(statistics.mean(v.values()), 2),
                            median=round(statistics.median(v.values()), 2),
                            SLE=round(v.get("SLE", float("nan")), 2), LBR=round(v.get("LBR", float("nan")), 2)))
    with open(HERE / "africa_excise_benchmark.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)
    for o in out:
        print(o)


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "_oecd_download")
