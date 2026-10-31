"""Distributional incidence of the carbon consumption tax by income quintile.

Working paper 1.6 (Carbon Consumption Tax), Section 6 and Appendix C.

Data (Eurostat, downloaded once to ~/.cache/cct_figaro):
  hbs_str_t223    budget shares (per mille) by income quintile and COICOP, 2020 wave
  hbs_exp_t133    mean consumption expenditure by income quintile (PPS per household), 2020
  nama_10_co3_p3  household final consumption by COICOP, 2022, million euro
  env_ac_ainah_r2 household direct GHG emissions for heating and transport, 2022
plus defaults_by_category.csv from calibrate_defaults.py (purchasers'-price
intensities, kg CO2e per euro).

Experiment, at the 2037 parameters (carbon price P = EUR 200/tCO2e):
  1. Carbon component on taxable spending at default intensities, with the
     value component cut to keep the swap revenue-neutral, (a) nationally and
     (b) at one EU-wide rate.
  2. The forward obligation on fuel for homes and vehicles (direct emissions),
     with receipts returned (a) as a further value-component cut or (b) as an
     equal lump sum per household, nationally.
Outputs: distribution_quintiles.csv, distribution_countries.csv.

Simplifications (stated in the paper): budget shares are applied to spending
net of taxes; every member state uses the same EU-wide default intensities;
the burden is the full carbon price on every tonne (one price per tonne),
measured against no carbon price, so ETS costs already in prices are included.
"""
from pathlib import Path

import numpy as np
import pandas as pd

from calibrate_defaults import API, CACHE, EU27, fetch, jsonstat_to_frame

HERE = Path(__file__).resolve().parent
P = 200.0  # EUR per tonne CO2e in 2037

cats = pd.read_csv(HERE / "defaults_by_category.csv").set_index("category")
e = cats["ghg_purchasers"]  # kg CO2e per euro, purchasers' prices excl. taxes
food = (e["Agricultural and fishery products"] * cats.at["Agricultural and fishery products", "hh_spend_beur"]
        + e["Processed food, beverages, tobacco"] * cats.at["Processed food, beverages, tobacco", "hh_spend_beur"]) \
    / (cats.at["Agricultural and fishery products", "hh_spend_beur"]
       + cats.at["Processed food, beverages, tobacco", "hh_spend_beur"])
svc = e["Communication, business and personal services"]


def load(dataset, query, name):
    path = fetch(f"{API}/statistics/1.0/data/{dataset}?lang=EN&{query}", CACHE / name)
    return jsonstat_to_frame(path)


def main():
    shares = load("hbs_str_t223", "time=2020", "hbs_str_t223_2020.json")
    levels = load("hbs_exp_t133", "time=2020&unit=PPS_HH", "hbs_exp_t133_2020.json")
    co3 = load("nama_10_co3_p3", "time=2022&unit=CP_MEUR&coicop=TOTAL&coicop=CP045&coicop=CP072",
               "nama_10_co3_p3_2022.json")
    hh = load("env_ac_ainah_r2", "time=2022&unit=THS_T&airpol=GHG&nace_r2=HH_HEAT&nace_r2=HH_TRA",
              "env_ac_ainah_r2_hh_2022.json")
    co3 = co3.pivot_table(index="geo", columns="coicop", values="value")
    hh = hh.pivot_table(index="geo", columns="nace_r2", values="value")

    # embodied intensities of household energy, EU level (kg CO2e per euro of COICOP spending)
    fp_d35 = e["Electricity, gas, steam"] * cats.at["Electricity, gas, steam", "hh_spend_beur"]
    fp_c19 = cats.at["Refined petroleum products", "ghg_all"] * cats.at["Refined petroleum products", "hh_spend_beur"]
    e_cp045 = fp_d35 / (co3.at["EU27_2020", "CP045"] / 1000)
    e_cp072 = fp_c19 / (co3.at["EU27_2020", "CP072"] / 1000)

    # COICOP (3-digit) -> embodied intensity; None = exempt from VAT
    bridge = {
        "CP011": food, "CP012": e["Processed food, beverages, tobacco"],
        "CP021": e["Processed food, beverages, tobacco"], "CP022": e["Processed food, beverages, tobacco"],
        "CP023": None,
        "CP031": e["Textiles, clothing, footwear"], "CP032": e["Textiles, clothing, footwear"],
        "CP041": None, "CP042": None, "CP043": e["Construction"],
        "CP044": e["Water supply, sewerage, waste"], "CP045": e_cp045,
        "CP051": e["Furniture and other manufactured goods"], "CP052": e["Textiles, clothing, footwear"],
        "CP053": e["Electronics and electrical equipment"], "CP054": e["Minerals, metals, metal products"],
        "CP055": e["Minerals, metals, metal products"], "CP056": e["Chemicals and pharmaceuticals"],
        "CP061": e["Chemicals and pharmaceuticals"], "CP062": None, "CP063": None,
        "CP071": e["Motor vehicles and other transport equipment"], "CP072": e_cp072,
        "CP073": (e["Land and water transport, logistics"] * cats.at["Land and water transport, logistics", "hh_spend_beur"]
                  + e["Air transport"] * cats.at["Air transport", "hh_spend_beur"])
        / (cats.at["Land and water transport, logistics", "hh_spend_beur"] + cats.at["Air transport", "hh_spend_beur"]),
        "CP081": svc, "CP082": e["Electronics and electrical equipment"], "CP083": svc,
        "CP091": e["Electronics and electrical equipment"],
        "CP092": e["Motor vehicles and other transport equipment"],
        "CP093": e["Furniture and other manufactured goods"], "CP094": svc,
        "CP095": e["Wood, paper, printing"],
        "CP096": 0.5 * (e["Air transport"] + e["Accommodation and food services"]),
        "CP101": None, "CP102": None, "CP103": None, "CP104": None, "CP105": None,
        "CP111": e["Accommodation and food services"], "CP112": e["Accommodation and food services"],
        "CP121": 0.5 * (svc + e["Chemicals and pharmaceuticals"]), "CP122": None,
        "CP123": e["Furniture and other manufactured goods"], "CP124": None,
        "CP125": None, "CP126": None, "CP127": svc,
    }

    sh = shares[shares.coicop.isin(bridge) & shares.quant_inc.str.startswith("QU")]
    countries = sorted(set(sh.geo) & set(EU27))
    lev = levels[levels.quant_inc.str.startswith("QU")].pivot_table(index="geo", columns="quant_inc", values="value")
    rows = []
    for c in countries:
        s = sh[sh.geo == c].pivot_table(index="coicop", columns="quant_inc", values="value") / 1000
        if s.shape[0] < 40 or c not in lev.index:
            continue
        s = s.reindex(list(bridge)).fillna(0.0)
        taxable = s.loc[[k for k, v in bridge.items() if v is not None]].sum()
        carbon = sum(s.loc[k] * v for k, v in bridge.items() if v is not None) * P / 1000
        d_heat = hh.at[c, "HH_HEAT"] / co3.at[c, "CP045"]   # kt / MEUR = kg per euro
        d_tra = hh.at[c, "HH_TRA"] / co3.at[c, "CP072"]
        direct = (s.loc["CP045"] * d_heat + s.loc["CP072"] * d_tra) * P / 1000
        x = lev.loc[c]                       # PPS per household, by quintile
        w = x / x.sum()                      # spending weights within the country
        for q in ["QU1", "QU2", "QU3", "QU4", "QU5"]:
            rows.append({"geo": c, "quintile": q, "spend_weight": w[q],
                         "country_spend_meur": co3.at[c, "TOTAL"],
                         "taxable_share": taxable[q], "carbon_share": carbon[q],
                         "direct_share": direct[q]})
    df = pd.DataFrame(rows)

    # (1a) national revenue-neutral cut; (1b) one EU-wide cut
    def wavg(g, col):
        return (g[col] * g["spend_weight"]).sum() / g["spend_weight"].sum()

    nat = df.groupby("geo").apply(lambda g: wavg(g, "carbon_share") / wavg(g, "taxable_share"),
                                  include_groups=False)
    df["cut_national"] = df.geo.map(nat)
    df["w_eu"] = df.spend_weight * df.country_spend_meur
    cut_eu = (df.carbon_share * df.w_eu).sum() / (df.taxable_share * df.w_eu).sum()
    df["swap_national"] = df.carbon_share - df.cut_national * df.taxable_share
    df["swap_eu"] = df.carbon_share - cut_eu * df.taxable_share
    # (2) obligation, recycled nationally through VAT or as an equal lump sum per household
    rec_vat = df.groupby("geo").apply(lambda g: wavg(g, "direct_share") / wavg(g, "taxable_share"),
                                      include_groups=False)
    df["oblig_vat"] = df.direct_share - df.geo.map(rec_vat) * df.taxable_share
    # lump sum: national receipts per household, as a share of each quintile's spending
    lump = df.groupby("geo").apply(lambda g: (g.direct_share * g.spend_weight).sum() / 5,
                                   include_groups=False)
    df["oblig_lump"] = df.direct_share - df.geo.map(lump) / df.spend_weight
    df["full_vat"] = df.swap_national + df.oblig_vat
    df["full_lump"] = df.swap_national + df.oblig_lump
    df.to_csv(HERE / "distribution_by_country_quintile.csv", index=False, float_format="%.5f")

    cols = ["carbon_share", "taxable_share", "direct_share", "swap_national", "swap_eu",
            "oblig_vat", "oblig_lump", "full_vat", "full_lump"]
    quint = df.groupby("quintile").apply(lambda g: pd.Series(
        {k: (g[k] * g.country_spend_meur).sum() / g.country_spend_meur.sum() for k in cols}),
        include_groups=False)
    quint.to_csv(HERE / "distribution_quintiles.csv", float_format="%.5f")
    ctry = df.groupby("geo").apply(lambda g: pd.Series(
        {k: (g[k] * g.spend_weight).sum() / g.spend_weight.sum() for k in cols}
        | {"country_spend_meur": g.country_spend_meur.iloc[0]}), include_groups=False)
    ctry.to_csv(HERE / "distribution_countries.csv", float_format="%.5f")
    pd.set_option("display.width", 200)
    print(f"countries: {len(countries)} with data -> {df.geo.nunique()} used: {sorted(df.geo.unique())}")
    print(f"energy intensities: CP045 embodied {e_cp045:.3f}, CP072 embodied {e_cp072:.3f} kg/EUR")
    print(f"EU-wide revenue-neutral value cut: {cut_eu * 100:.2f} pp of taxable spending")
    print((quint * 100).round(2).to_string())
    print((ctry[cols] * 100).round(2).sort_values("swap_eu").to_string())


if __name__ == "__main__":
    main()
