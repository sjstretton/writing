"""Calibrate default embodied-carbon intensities by product category for the EU.

Working paper 1.6 (Carbon Consumption Tax), Appendix C.

Method: environmentally extended multi-regional input-output (MRIO) model built
from two Eurostat datasets for reference year 2022:

  * naio_10_fcp_ip4  FIGARO inter-country input-output table, product by product,
                     basic prices, million euro (46 economies x 64 products).
  * env_ac_ghgfp     Greenhouse gas emission footprints (FIGARO application),
                     thousand tonnes CO2-equivalent; with c_dest=WORLD and
                     na_item=TOTAL it gives total emissions by emitting country
                     and NACE A*64 industry.  env_ac_co2fp gives CO2 only.

Industry emissions are assigned to the matching CPA product (one-to-one A*64
mapping).  Multipliers m = f_hat (I - A)^-1 give kg CO2e embodied per euro of
final demand for each origin-product.  EU-27 household final consumption
(P3_S14) weights them into intensities by product category, by origin group.
Units: thousand tonnes / million euro = kg per euro.

Outputs (beside this script):
  defaults_by_category.csv   Table 1 of the paper
  defaults_by_product.csv    the 64-product detail
  basket_summary.csv         basket intensities, VAT base, validation check

Run:  python3 calibrate_defaults.py   (downloads ~75 MB once to ~/.cache/cct_figaro)
"""
from pathlib import Path
import gzip
import json
import os
import urllib.request

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
CACHE = Path(os.environ.get("CCT_CACHE", Path.home() / ".cache" / "cct_figaro"))
YEAR = "2022"
API = "https://ec.europa.eu/eurostat/api/dissemination"
EU27 = ["AT", "BE", "BG", "CY", "CZ", "DE", "DK", "EE", "EL", "ES", "FI", "FR",
        "HR", "HU", "IE", "IT", "LT", "LU", "LV", "MT", "NL", "PL", "PT", "RO",
        "SE", "SI", "SK"]
FD = ["P3_S13", "P3_S14", "P3_S15", "P51G", "P5M"]

# Product categories for Table 1.  vat: "taxable", or "exempt" for products
# mainly exempt or outside the scope of VAT (Directive 2006/112/EC, Arts 13,
# 132 and 135: public bodies, health, education, social care, financial
# services, insurance, letting of immovable property).
CATEGORIES = [
    ("Agricultural and fishery products", ["A01", "A02", "A03"], "taxable"),
    ("Processed food, beverages, tobacco", ["C10-12"], "taxable"),
    ("Textiles, clothing, footwear", ["C13-15"], "taxable"),
    ("Wood, paper, printing", ["C16", "C17", "C18"], "taxable"),
    ("Refined petroleum products", ["C19"], "taxable"),
    ("Chemicals and pharmaceuticals", ["C20", "C21"], "taxable"),
    ("Rubber and plastic products", ["C22"], "taxable"),
    ("Minerals, metals, metal products", ["B", "C23", "C24", "C25"], "taxable"),
    ("Electronics and electrical equipment", ["C26", "C27"], "taxable"),
    ("Machinery and equipment", ["C28", "C33"], "taxable"),
    ("Motor vehicles and other transport equipment", ["C29", "C30"], "taxable"),
    ("Furniture and other manufactured goods", ["C31_32"], "taxable"),
    ("Electricity, gas, steam", ["D35"], "taxable"),
    ("Water supply, sewerage, waste", ["E36", "E37-39"], "taxable"),
    ("Construction", ["F"], "taxable"),
    ("Wholesale and retail trade services", ["G45", "G46", "G47"], "taxable"),
    ("Land and water transport, logistics", ["H49", "H50", "H52", "H53"], "taxable"),
    ("Air transport", ["H51"], "taxable"),
    ("Accommodation and food services", ["I"], "taxable"),
    ("Communication, business and personal services",
     ["J58", "J59_60", "J61", "J62_63", "M69_70", "M71", "M72", "M73", "M74_75",
      "N77", "N78", "N79", "N80-82", "R90-92", "R93", "S94", "S95", "S96", "T", "U"],
     "taxable"),
    ("Financial services and insurance", ["K64", "K65", "K66"], "exempt"),
    ("Real estate services (incl. imputed rent)", ["L"], "exempt"),
    ("Public administration, education, health, social care",
     ["O84", "P85", "Q86", "Q87_88"], "exempt"),
]


def fetch(url, dest):
    dest = Path(dest)
    if not dest.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        print("downloading", url)
        with urllib.request.urlopen(url, timeout=900) as r, open(dest, "wb") as f:
            f.write(r.read())
    return dest


def cpa_to_nace(code):
    """CPA_C10-12 -> C10-C12; CPA_C31_32 -> C31_C32; CPA_L -> L."""
    c = code.replace("CPA_", "")
    letter = c[0]
    for sep in ("-", "_"):
        if sep in c:
            a, b = c.split(sep)
            return f"{a}{sep}{letter}{b}"
    return c


def jsonstat_to_frame(path):
    d = json.load(open(path))
    ids, sizes = d["id"], d["size"]
    labels = [list(d["dimension"][k]["category"]["index"].keys()) for k in ids]
    # order keys by their index position
    for i, k in enumerate(ids):
        idx = d["dimension"][k]["category"]["index"]
        labels[i] = sorted(idx, key=idx.get)
    rows = []
    for flat, v in d["value"].items():
        flat = int(flat)
        coord = []
        for s in reversed(sizes):
            coord.append(flat % s)
            flat //= s
        coord = list(reversed(coord))
        rows.append([labels[j][coord[j]] for j in range(len(ids))] + [v])
    return pd.DataFrame(rows, columns=ids + ["value"])


def load_io():
    path = fetch(f"{API}/sdmx/2.1/data/naio_10_fcp_ip4/?format=TSV&compressed=true",
                 CACHE / "naio_10_fcp_ip4.tsv.gz")
    with gzip.open(path, "rt") as f:
        header = f.readline().rstrip("\n").split("\t")
        col = [h.strip() for h in header].index(YEAR)
        recs = []
        for line in f:
            parts = line.rstrip("\n").split("\t")
            key = parts[0].split(",")
            raw = parts[col].strip().split(" ")[0]
            if raw in ("", ":"):
                continue
            recs.append((key[1], key[2], key[3], key[5], float(raw)))
    return pd.DataFrame(recs, columns=["use", "ava", "dest", "orig", "v"])


def load_emissions(dataset):
    path = fetch(f"{API}/statistics/1.0/data/{dataset}?lang=EN&c_dest=WORLD&na_item=TOTAL"
                 f"&time={YEAR}", CACHE / f"{dataset}_world_{YEAR}.json")
    df = jsonstat_to_frame(path)
    return df.set_index(["c_orig", "nace_r2"])["value"]


def load_eu_footprint(dataset):
    path = fetch(f"{API}/statistics/1.0/data/{dataset}?lang=EN&c_dest=EU27_2020&c_orig=WORLD"
                 f"&time={YEAR}", CACHE / f"{dataset}_eu27_{YEAR}.json")
    df = jsonstat_to_frame(path)
    return df.set_index(["na_item", "nace_r2"])["value"]


def main():
    io = load_io()
    countries = sorted(set(io.loc[io.orig != "DOM", "orig"]))
    products = sorted(p for p in set(io.ava) if p.startswith("CPA_"))
    n_c, n_p = len(countries), len(products)
    idx = {(c, p): i * n_p + j for i, c in enumerate(countries) for j, p in enumerate(products)}
    N = n_c * n_p
    print(f"{n_c} economies x {n_p} products = {N}")

    inter = io[io.ava.str.startswith("CPA_") & io.use.str.startswith("CPA_")]
    Z = np.zeros((N, N))
    r = [idx[(o, a)] for o, a in zip(inter.orig, inter.ava)]
    c = [idx[(d, u)] for d, u in zip(inter.dest, inter.use)]
    np.add.at(Z, (r, c), inter.v.values)

    fd = io[io.ava.str.startswith("CPA_") & io.use.isin(FD)]
    fd = fd.assign(row=[idx[(o, a)] for o, a in zip(fd.orig, fd.ava)])
    Ytot = np.zeros(N)
    np.add.at(Ytot, fd.row.values, fd.v.values)
    x = Z.sum(axis=1) + Ytot
    xs = np.where(x > 1e-6, x, 1.0)
    A = Z / xs[None, :]

    results = {}
    for gas, ds in (("ghg", "env_ac_ghgfp"), ("co2", "env_ac_co2fp")):
        em = load_emissions(ds)
        f = np.zeros(N)
        for (cc, p), i in idx.items():
            f[i] = em.get((cc, cpa_to_nace(p)), 0.0)
        s = np.where(x > 1e-6, f / xs, 0.0)
        # multipliers: m = s (I - A)^-1  <=>  (I - A)^T m^T = s^T
        m = np.linalg.solve((np.eye(N) - A).T, s)
        results[gas] = (m, f.sum())

    # EU-27 final demand by origin-product
    eu = fd[fd.dest.isin(EU27)]
    eu_hh = eu[eu.use == "P3_S14"]
    eu_all = eu
    g = {}
    for name, sub in (("hh", eu_hh), ("all", eu_all)):
        vec = np.zeros(N)
        np.add.at(vec, sub.row.values, sub.v.values)
        g[name] = vec

    origin_group = np.array(["EU" if cc in EU27 else ("CN" if cc == "CN" else "XEU")
                             for cc in countries for _ in products])
    prod_of = np.array([p for _ in countries for p in products])

    def intensity(weights, m, mask):
        w = weights * mask
        return (m * w).sum() / w.sum() if w.sum() > 0 else np.nan, w.sum()

    rows = []
    for p in products:
        pm = prod_of == p
        row = {"product": p}
        for gas in ("ghg", "co2"):
            m = results[gas][0]
            row[f"{gas}_all_origins"], row["hh_spend_meur"] = intensity(g["hh"], m, pm)
            row[f"{gas}_eu_origin"], _ = intensity(g["hh"], m, pm & (origin_group == "EU"))
            row[f"{gas}_extra_eu"], row["hh_spend_extra_eu_meur"] = intensity(
                g["hh"], m, pm & (origin_group != "EU"))
            row[f"{gas}_china"], _ = intensity(g["hh"], m, pm & (origin_group == "CN"))
        rows.append(row)
    byprod = pd.DataFrame(rows)
    byprod.to_csv(HERE / "defaults_by_product.csv", index=False, float_format="%.4f")

    cat_rows = []
    total_hh = g["hh"].sum()
    for name, codes, vat in CATEGORIES:
        mask = np.isin(prod_of, ["CPA_" + c for c in codes])
        row = {"category": name, "cpa": " ".join(codes), "vat": vat}
        for gas in ("ghg", "co2"):
            m = results[gas][0]
            row[f"{gas}_all"], spend = intensity(g["hh"], m, mask)
            row[f"{gas}_eu"], _ = intensity(g["hh"], m, mask & (origin_group == "EU"))
            row[f"{gas}_extra_eu"], spend_x = intensity(g["hh"], m, mask & (origin_group != "EU"))
            row[f"{gas}_china"], _ = intensity(g["hh"], m, mask & (origin_group == "CN"))
        row["hh_spend_beur"] = spend / 1000
        row["share_of_hh_spend"] = spend / total_hh
        row["import_share"] = spend_x / spend
        cat_rows.append(row)
    cats = pd.DataFrame(cat_rows)
    used = set(sum((c for _, c, _ in CATEGORIES), []))
    missing = [p for p in products if p.replace("CPA_", "") not in used]
    assert not missing, missing
    cats.to_csv(HERE / "defaults_by_category.csv", index=False, float_format="%.4f")

    # basket summaries
    taxable = np.isin(prod_of, ["CPA_" + c for n, cs, v in CATEGORIES if v == "taxable" for c in cs])
    summ = []
    for gas in ("ghg", "co2"):
        m = results[gas][0]
        for label, mask in (("household basket, all products", np.ones(N, bool)),
                            ("household basket, VAT-taxable products", taxable),
                            ("household basket, taxable goods only (A-C, D-E)",
                             taxable & np.array([p[4] in "ABCDE" for p in prod_of])),
                            ("household basket, taxable, EU origin", taxable & (origin_group == "EU")),
                            ("household basket, taxable, extra-EU origin", taxable & (origin_group != "EU"))):
            val, spend = intensity(g["hh"], m, mask)
            summ.append({"gas": gas, "basket": label, "kg_per_eur": val, "spend_beur": spend / 1000})
        # validation: model EU-27 footprint (all final demand, excl. household direct)
        model_fp = (m * g["all"]).sum()
        summ.append({"gas": gas, "basket": "model EU27 footprint, all final demand (Mt)",
                     "kg_per_eur": np.nan, "spend_beur": model_fp / 1000})
        hh_fp = (m * g["hh"]).sum()
        summ.append({"gas": gas, "basket": "model EU27 household footprint excl. direct (Mt)",
                     "kg_per_eur": np.nan, "spend_beur": hh_fp / 1000})
        try:
            ds = "env_ac_ghgfp" if gas == "ghg" else "env_ac_co2fp"
            ef = load_eu_footprint(ds)
            summ.append({"gas": gas, "basket": "Eurostat EU27 footprint, all final demand excl. HH (Mt)",
                         "kg_per_eur": np.nan, "spend_beur": ef[("TOTAL", "TOTAL")] / 1000})
            summ.append({"gas": gas, "basket": "Eurostat EU27 household direct emissions (Mt)",
                         "kg_per_eur": np.nan, "spend_beur": ef[("P3_S14", "HH")] / 1000})
            summ.append({"gas": gas, "basket": "Eurostat EU27 household footprint excl. direct (Mt)",
                         "kg_per_eur": np.nan, "spend_beur": ef[("P3_S14", "TOTAL")] / 1000})
        except Exception as exc:  # validation is optional
            print("validation download failed:", exc)
    summ = pd.DataFrame(summ)
    summ.to_csv(HERE / "basket_summary.csv", index=False, float_format="%.4f")
    pd.set_option("display.width", 200)
    print(cats[["category", "vat", "ghg_all", "co2_all", "ghg_eu", "ghg_extra_eu", "ghg_china",
                "hh_spend_beur", "share_of_hh_spend", "import_share"]].round(3).to_string())
    print(summ.round(3).to_string())


if __name__ == "__main__":
    main()
