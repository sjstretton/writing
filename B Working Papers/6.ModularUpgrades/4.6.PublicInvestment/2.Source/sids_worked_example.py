#!/usr/bin/env python3
"""
SIDS worked example: a small island state escaping the "oil trap".

A diesel-dependent island replaces part of its diesel generation with 60 MW of
solar PV plus a 120 MWh battery. The same plant is financed four ways (R1a/R1b
commercial loan, R2 concessional loan, R3/R4 IPP with a PPA) and each route is
scored with the Public Spending Value (PSV) metrics of design_brief.md section 2
(Steps 5-9): fiscal ledger, W, F, MVPF, NB_lambda, FNPV, debt and PPA liability.
The worked-example specification is design_brief.md section 3.

Units: USD million ("$m") for money, GWh for energy, $/kWh for unit costs
(1 $/kWh x 1 GWh = $1 m). Constant prices. Year 0 = construction (capex paid,
loan disbursed); years 1..25 = operation. End-of-year cash flows.

Run:    python3 -I sids_worked_example.py
Writes: sids_worked_example_results.csv      (one row per financing route)
        sids_worked_example_sensitivity.csv  (one row per sensitivity case and route)
        Both go to the folder that holds this script. Markdown tables go to stdout.

Source tags used in the comments:
  [brief]       design_brief.md section 3 (worked-example specification)
  [notes s.N]   capex_opex_ppp_ppa_sids.md section N (full citations are there)
  [theory QN]   theory_rules_mcpf_mvpf.md question N
  illustrative  an assumption with no source
  NOT verified  background knowledge that the research notes do not contain

Accounting conventions (the PSV identity)
-----------------------------------------
Agents: (i) the public sector = budget plus the state utility whose losses the
budget covers ("budget/utility"); (ii) domestic non-budget agents = electricity
consumers, plus any resident financiers; (iii) non-residents = foreign lenders
and IPP owners; (iv) the world (carbon, memo item).

  S_t  = avoided diesel cost (fuel + variable O&M) at resource prices
  X_t  = fuel excise lost on the displaced diesel (a domestic transfer)
  theta = share of the avoided fuel bill (incl. excise) kept by the public sector;
          (1 - theta) passes to consumers through fuel pass-through in tariffs.
          The public sector pays the full plant cost (debt service or PPA).

  F_t  = net fiscal cost = debt service + public O&M + public replacement
         + PPA payments + capex not loan-financed - loan disbursed
         + X_t - theta*(S_t + X_t)
  W_t  = (1 - theta)*(S_t + X_t) + resident financiers' net receipts
         (+ carbon value if the carbon switch is on)
  W, F = present values at the social discount rate (6%)
  ENPV = W - F  (asserted in code against an independent calculation)

ENPV here is the *island* (national) ENPV: resource flows plus the net
payments to non-resident financiers. The World Bank financing-neutral ENPV
("ENPV_wb", resource flows only) is identical for every route; the two differ
by the financing premium = PV at 6% of (payments to financiers - money they put
in). With all financiers resident, ENPV = ENPV_wb for every route (asserted).
"""

from pathlib import Path

import numpy as np
import pandas as pd

OUT_DIR = Path(__file__).resolve().parent
L_PER_BBL = 158.987  # litres per barrel (unit conversion)

# =============================================================================
# 1. PARAMETERS (every value carries its source or "illustrative")
# =============================================================================
BASE = {
    # ---- Island -------------------------------------------------------------
    "demand_gwh": 300.0,           # [brief; notes s.4, s.8] St Lucia 399 GWh, SVG 136 GWh (NREL Energy Snapshots 2020)
    "diesel_share": 1.00,          # [brief "almost all diesel"; notes s.4] St Lucia ~99% diesel (NREL 2020)
    "gdp_musd": 2000.0,            # illustrative [brief; notes s.8 "assumption (not verified)"]
    "debt_pct_gdp": 85.0,          # illustrative [brief]: high risk of debt distress
    "year0": 2027,                 # illustrative: construction year (t = 0); operation 2028-2052
    # ---- Project ------------------------------------------------------------
    "pv_mw": 60.0,                 # [brief]
    "pv_cf": 0.18,                 # illustrative [notes s.8 "assumption"; ASPIRE-implied ~16.5%]
    "delivered_share": 0.95,       # illustrative [notes s.6]: share of PV output that displaces diesel (storage, curtailment losses)
    "bess_mwh": 120.0,             # [brief] (30 MW / 4 h in notes s.6)
    "pv_capex_per_kw": 1200.0,     # [notes s.4, s.8 inference] IRENA RPGC 2024 global $691/kW x 1.5-1.7 island premium implied by Maldives ASPIRE tariffs
    "bess_capex_per_kwh": 350.0,   # illustrative [notes s.8]: IRENA RPGC 2025 ~$140/kWh (4-h, global) x island premium (assumption)
    "integration_share": 0.05,     # illustrative [notes s.8]: integration and soft costs, share of total capex
    "capex_mult": 1.0,             # sensitivity multiplier on all capex (0.7 / 1.3)
    "om_share": 0.015,             # [brief "O&M about 1.5% of capex"; notes s.8 r_PV 1-2%/yr, assumption]
    "life": 25,                    # [brief; notes s.8 PV life 25 y, assumption]
    "bess_repl": True,             # switch: battery replaced once within the 25-year life
    "bess_repl_year": 15,          # illustrative [notes s.6, s.8]: BESS life 15 y
    "bess_repl_share": 0.60,       # illustrative [notes s.6, s.8]: replacement at 60% of original BESS capex
    # ---- Diesel counterfactual ---------------------------------------------
    "brent": 80.0,                 # [brief] central; EIA STEO Oct 2026 as reported: 2026 avg $96, 2027 $84 [notes s.4]
    "crack_usd_bbl": 25.0,         # illustrative [notes s.8]: gasoil crack spread over Brent
    "island_premium_usd_l": 0.15,  # illustrative [notes s.8]: freight, storage and margin to the island power station
    "sfc_kwh_per_l": 3.9,          # [notes s.4] modern gensets 200-215 g/kWh ~ 3.8-4.2 kWh/L (vendor guide, [weak])
    "diesel_vom_usd_kwh": 0.02,    # illustrative [notes s.8]: non-fuel variable O&M of diesel gensets
    "excise_usd_l": 0.0,           # [brief] default 0: power-sector diesel often exempt (illustrative)
    "theta": 0.5,                  # [brief] base 0.5; 1 if the budget covers utility losses (policy parameter, notes s.8)
    # ---- Emissions and carbon (memo item) ----------------------------------
    "ef_kgco2_per_gj": 74.1,       # IPCC 2006 Guidelines default, gas/diesel oil: background knowledge, NOT verified in the notes
    "ncv_gj_per_t": 43.0,          # IPCC 2006 Guidelines default NCV, gas/diesel oil: background knowledge, NOT verified
    "diesel_density_kg_l": 0.84,   # illustrative
    "spc_2020": {"low": 40.0, "high": 80.0},  # [theory Q7] WB 2024 SPC guidance note, US$/tCO2e in 2020 (2017 US$)
    "spc_growth": 0.0225,          # [theory Q7] growth rate used in the WB 2024 note (40 -> 50 in 2030 -> 78 in 2050)
    "spc_case": "low",             # path used for the "incl. carbon" columns; the high path is a memo column
    "carbon_in_w": False,          # switch: if True, carbon counts in W (and so in ENPV, MVPF, NB). Default: memo only
    # ---- Discounting and the cost of public funds --------------------------
    "sdr": 0.06,                   # [theory Q6] WB 2016 discounting note: 1-2x per-capita growth, typically 6%
    "gov_rate": 0.08,              # illustrative [brief; notes s.8 "assumption (not verified)"]: marginal borrowing rate
    "lambdas": (1.2, 2.0),         # [theory Q1] 1.2: Auriol & Warlters (2012) Africa average, Norway convention; 2.0: stress value [design_brief Step 6]
    "lambda_liq": 2.0,             # illustrative: lambda in the liquidity-constrained years (time-varying lambda variant)
    "liq_years": 7,                # illustrative: liquidity-constrained window = years 1-7 (the short tenor)
    # ---- Financing routes ---------------------------------------------------
    "comm_rate": 0.08,             # [brief] R1 commercial loan rate (= gov_rate)
    "comm_tenor_short": 7,         # [brief] R1a: the only tenor the market offers
    "comm_tenor_long": 25,         # [brief] R1b: comparison (not available to the island in the base case)
    "conc_rate": 0.015,            # [brief; notes s.8] IDA/RST-type terms (IDA terms not verified; RST: 20 y, 10.5 y grace)
    "conc_tenor": 30,              # [brief; notes s.8]
    "conc_grace": 5,               # [brief: 5-10 y; notes s.8 default 5 y] choice: 5 years, interest-only
    "wacc_ipp": 0.11,              # [brief; notes s.4, s.8] IEA CoC Observatory: SE Asia solar 8-9.4%, AE 5-6.5%; SIDS higher (assumption)
    "wacc_ipp_guaranteed": 0.085,  # [brief]; notes s.8 assume a 2 pp guarantee effect (assumption); brief uses 2.5 pp
    "ppa_term": 25,                # [notes s.3] Zambia Scaling Solar: tariff fixed for 25 y (ASPIRE: 20 y). Asset reverts to utility after term
    "financier_resident_share": 0.0,  # illustrative: lenders and IPP owners are non-residents
    # ---- Debt sustainability ------------------------------------------------
    "dsf_ppp_shock_share": 0.35,   # [notes s.3] LIC-DSF Guidance Note (2017): stress adds 35% of the PPP capital stock to PPG debt...
    "dsf_ppp_trigger": 0.03,       # [notes s.3] ...when the PPP capital stock exceeds 3% of GDP
    "dsf_pv_rate": 0.05,           # candidate, NOT verified [notes s.8 gaps]: discount rate for the PV of new debt (DSF-style)
}


def route_book(p):
    """The four financing routes of the brief (R1 split into two tenors)."""
    return {
        "R1a": {"label": "Budget, commercial 8%, 7-yr", "kind": "loan",
                "rate": p["comm_rate"], "tenor": p["comm_tenor_short"], "grace": 0},
        "R1b": {"label": "Budget, commercial 8%, 25-yr (comparison)", "kind": "loan",
                "rate": p["comm_rate"], "tenor": p["comm_tenor_long"], "grace": 0},
        "R2": {"label": "Budget, concessional 1.5%, 30-yr, 5-yr grace", "kind": "loan",
               "rate": p["conc_rate"], "tenor": p["conc_tenor"], "grace": p["conc_grace"]},
        "R3": {"label": "IPP + PPA, WACC 11%, no guarantee", "kind": "ppa",
               "wacc": p["wacc_ipp"]},
        "R4": {"label": "IPP + PPA, WACC 8.5%, WB/MIGA guarantee", "kind": "ppa",
               "wacc": p["wacc_ipp_guaranteed"]},
    }


# =============================================================================
# 2. BUILDING BLOCKS
# =============================================================================
def crf(r, n):
    """Capital recovery factor, end-of-year payments: r / (1 - (1+r)^-n)."""
    return r / (1.0 - (1.0 + r) ** -n) if r != 0 else 1.0 / n


def pv(flows, r):
    """Present value at t = 0 of a flow vector indexed t = 0, 1, 2, ..."""
    t = np.arange(len(flows))
    return float(np.sum(np.asarray(flows, dtype=float) / (1.0 + r) ** t))


def fuel_cost_usd_kwh(p, brent=None):
    """Diesel fuel cost per kWh [notes s.4 inference]:
    [(Brent + crack)/159 L per bbl + island premium per L] / SFC (kWh per L)."""
    b = p["brent"] if brent is None else brent
    return ((b + p["crack_usd_bbl"]) / L_PER_BBL + p["island_premium_usd_l"]) / p["sfc_kwh_per_l"]


def brent_for_avoided_cost(p, usd_kwh):
    """Inverse of the avoided-cost formula: the Brent price at which the avoided
    diesel cost (fuel + variable O&M) equals usd_kwh."""
    fuel = usd_kwh - p["diesel_vom_usd_kwh"]
    return (fuel * p["sfc_kwh_per_l"] - p["island_premium_usd_l"]) * L_PER_BBL - p["crack_usd_bbl"]


def derive(p):
    """Physical and cost quantities that do not depend on the financing route."""
    d = {}
    # Energy displaced: MW x 8760 h x CF x delivered share -> MWh; /1000 -> GWh
    d["e_gwh"] = p["pv_mw"] * 8760 * p["pv_cf"] * p["delivered_share"] / 1000.0
    d["diesel_gwh"] = p["demand_gwh"] * p["diesel_share"]
    d["share_displaced"] = d["e_gwh"] / d["diesel_gwh"]
    # Capex ($m). Integration is a share of the total: K = (K_pv + K_bess) / (1 - s)
    k_pv = p["pv_mw"] * 1000 * p["pv_capex_per_kw"] / 1e6
    k_bess = p["bess_mwh"] * 1000 * p["bess_capex_per_kwh"] / 1e6
    k_tot = (k_pv + k_bess) / (1.0 - p["integration_share"])
    m = p["capex_mult"]
    d["capex_pv"], d["capex_bess"] = m * k_pv, m * k_bess
    d["capex"] = m * k_tot
    d["capex_int"] = d["capex"] - d["capex_pv"] - d["capex_bess"]
    d["om"] = p["om_share"] * d["capex"]                                  # $m/yr
    d["repl"] = p["bess_repl_share"] * d["capex_bess"] if p["bess_repl"] else 0.0
    # Avoided diesel cost ($/kWh and $m/yr)
    d["fuel_usd_kwh"] = fuel_cost_usd_kwh(p)
    d["avoided_usd_kwh"] = d["fuel_usd_kwh"] + p["diesel_vom_usd_kwh"]
    d["S"] = d["e_gwh"] * d["avoided_usd_kwh"]                            # $m/yr avoided
    d["diesel_fuel_bill"] = d["diesel_gwh"] * d["fuel_usd_kwh"]           # whole system, fuel only
    d["litres_m"] = d["e_gwh"] / p["sfc_kwh_per_l"]                       # million litres/yr avoided
    d["X"] = d["litres_m"] * p["excise_usd_l"]                            # $m/yr excise lost
    # Heat rate and emissions (kg CO2 per litre = kg/GJ x GJ/t x kg/L / 1000)
    d["heat_rate_mj_kwh"] = p["ncv_gj_per_t"] * p["diesel_density_kg_l"] / p["sfc_kwh_per_l"]
    d["efficiency"] = 3.6 / d["heat_rate_mj_kwh"]
    d["kgco2_per_l"] = p["ef_kgco2_per_gj"] * p["ncv_gj_per_t"] * p["diesel_density_kg_l"] / 1000.0
    d["tco2_per_mwh"] = d["kgco2_per_l"] / p["sfc_kwh_per_l"]
    d["ktco2"] = d["e_gwh"] * d["tco2_per_mwh"]                           # GWh x t/MWh = kt
    return d


def spc_path(p, years, case):
    """WB 2024 shadow price of carbon path, US$/tCO2e (2017 US$) [theory Q7]."""
    return p["spc_2020"][case] * (1.0 + p["spc_growth"]) ** (np.asarray(years) - 2020)


def loan_schedule(principal, rate, tenor, grace, horizon):
    """Interest-only during grace, then a level (CRF) annuity to maturity."""
    interest = np.zeros(horizon + 1)
    principal_paid = np.zeros(horizon + 1)
    balance = principal
    annuity = principal * crf(rate, tenor - grace)
    for t in range(1, tenor + 1):
        interest[t] = balance * rate
        payment = interest[t] if t <= grace else annuity
        principal_paid[t] = payment - interest[t]
        balance -= principal_paid[t]
    assert abs(balance) < 1e-6, "loan not fully repaid"
    return interest, principal_paid


def ppa_tariff(p, d, wacc):
    """Levelised PPA tariff, $/kWh [design_brief Step 8; notes s.8 formula 3]:
    T = [(capex + PV_wacc(battery replacement within the term)) x CRF(wacc, term) + O&M] / E."""
    term = p["ppa_term"]
    k_eff = d["capex"]
    if d["repl"] > 0 and p["bess_repl_year"] <= term:
        k_eff += d["repl"] / (1.0 + wacc) ** p["bess_repl_year"]
    return (k_eff * crf(wacc, term) + d["om"]) / d["e_gwh"]


# =============================================================================
# 3. ONE ROUTE: ledger and PSV metrics
# =============================================================================
def evaluate(p, route):
    d = derive(p)
    life = p["life"]
    assert p["ppa_term"] <= life, "PPA term longer than asset life"
    horizon = max(life, route.get("tenor", 0), p["ppa_term"] if route["kind"] == "ppa" else 0)
    t = np.arange(horizon + 1)
    op = (t >= 1) & (t <= life)                       # operating years

    # ---- Resource flows (route-independent) --------------------------------
    S = np.where(op, d["S"], 0.0)                     # avoided diesel cost
    X = np.where(op, d["X"], 0.0)                     # excise lost (transfer)
    capex = np.where(t == 0, d["capex"], 0.0)
    om = np.where(op, d["om"], 0.0)
    repl = np.where(t == p["bess_repl_year"], d["repl"], 0.0) if d["repl"] > 0 else np.zeros_like(S)
    years = p["year0"] + t
    carbon = {c: np.where(op, d["ktco2"] * spc_path(p, years, c) / 1000.0, 0.0)  # kt x $/t / 1000 = $m
              for c in ("low", "high")}

    # ---- Financing: who pays what ------------------------------------------
    zeros = np.zeros_like(S)
    loan_in, debt_service, ppa = zeros.copy(), zeros.copy(), zeros.copy()
    tariff = np.nan
    if route["kind"] == "loan":                       # public build, loan-financed
        interest, principal = loan_schedule(d["capex"], route["rate"], route["tenor"], route["grace"], horizon)
        debt_service = interest + principal
        loan_in = capex.copy()
        capex_pub, om_pub, repl_pub = capex, om, repl
        fin_receipts, fin_outlays = debt_service, loan_in
    elif route["kind"] == "ppa":                      # IPP builds, owns and operates; utility buys energy
        tariff = ppa_tariff(p, d, route["wacc"])
        in_term = (t >= 1) & (t <= p["ppa_term"])
        ppa = np.where(in_term, tariff * d["e_gwh"], 0.0)
        capex_pub = zeros                             # IPP pays capex
        om_pub = np.where(in_term, 0.0, om)           # utility pays O&M only after the asset reverts
        repl_pub = np.where(t > p["ppa_term"], repl, 0.0)
        fin_receipts = ppa
        fin_outlays = capex + (om - om_pub) + (repl - repl_pub)
    else:
        raise ValueError(route["kind"])

    # ---- Fiscal ledger (budget/utility perspective), Step 5 ----------------
    theta = p["theta"]
    captured = theta * (S + X)                        # avoided fuel bill kept by the public sector
    net_fiscal = loan_in - capex_pub - debt_service - om_pub - repl_pub - ppa + captured - X
    F_t = -net_fiscal                                 # net fiscal cost

    # ---- Non-budget agents --------------------------------------------------
    consumers = (1.0 - theta) * (S + X)
    resident_fin = p["financier_resident_share"] * (fin_receipts - fin_outlays)
    W_t = consumers + resident_fin
    if p["carbon_in_w"]:
        W_t = W_t + carbon[p["spc_case"]]

    # ---- Present values at the SDR and the PSV identity, Step 6 ------------
    r = p["sdr"]
    W, F = pv(W_t, r), pv(F_t, r)
    enpv = W - F
    carbon_pv = {c: pv(carbon[c], r) for c in carbon}
    carbon_extra = 0.0 if p["carbon_in_w"] else carbon_pv[p["spc_case"]]
    resource = S - capex - om - repl + (carbon[p["spc_case"]] if p["carbon_in_w"] else 0.0)
    enpv_wb = pv(resource, r)                          # financing-neutral (World Bank) ENPV
    fin_premium = pv(fin_receipts - fin_outlays, r)    # paid to financiers above the 6% opportunity cost
    enpv_check = enpv_wb - (1.0 - p["financier_resident_share"]) * fin_premium
    assert abs(enpv - enpv_check) < 1e-6, f"PSV identity ENPV = W - F fails: {enpv} vs {enpv_check}"

    lam_base, lam_stress = p["lambdas"]
    lam_t = np.where((t >= 1) & (t <= p["liq_years"]), p["lambda_liq"], lam_base)

    def mvpf(w, f):
        if f <= 0:
            return np.nan, "pays for itself" if w >= 0 else "F<=0 but W<0"
        return w / f, ""

    mv, mv_note = mvpf(W, F)
    mv_c, _ = mvpf(W + carbon_extra, F)

    # ---- Debt and liabilities, Step 8 ---------------------------------------
    gdp = p["gdp_musd"]
    plant_payments = debt_service + om_pub + repl_pub + ppa       # what the public sector pays for the plant (t >= 1)
    is_ppp = route["kind"] == "ppa"
    ppp_stock_share = d["capex"] / gdp if is_ppp else 0.0
    dsf_stress = p["dsf_ppp_shock_share"] * ppp_stock_share * 100 if ppp_stock_share > p["dsf_ppp_trigger"] else 0.0

    # Payback: first year from which cumulative net fiscal cash stays >= 0 to the horizon
    cum = np.cumsum(net_fiscal)
    neg = np.where(cum < -1e-9)[0]
    payback = 0 if len(neg) == 0 else (int(neg[-1]) + 1 if neg[-1] < horizon else np.nan)
    payback_note = ("cumulative never negative" if payback == 0 else
                    "never recovers within horizon" if pd.isna(payback) else f"year {payback}")

    yr1_payment = debt_service[1] + om_pub[1] + ppa[1]
    out = {
        "route": None, "label": route.get("label", ""),
        "energy_gwh": d["e_gwh"], "capex_musd": d["capex"],
        "avoided_cost_usd_kwh": d["avoided_usd_kwh"],
        "fuel_bill_avoided_musd_yr": d["S"],
        "ppa_tariff_usd_kwh": tariff,
        "yr1_plant_payment_musd": yr1_payment,
        "yr1_plant_payment_usd_kwh": yr1_payment / d["e_gwh"],
        "breakeven_brent_yr1": brent_for_avoided_cost(p, yr1_payment / d["e_gwh"]),
        "ENPV_wb_6_musd": enpv_wb,
        "ENPV_wb_6_carbon_musd": enpv_wb + carbon_extra,
        "financing_premium_pv6_musd": fin_premium,
        "ENPV_6_musd": enpv,
        "ENPV_6_carbon_musd": enpv + carbon_extra,
        "carbon_pv6_low_musd": carbon_pv["low"],
        "carbon_pv6_high_musd": carbon_pv["high"],
        "W_6_musd": W,
        "F_6_musd": F,
        "MVPF": mv,
        "MVPF_note": mv_note,
        "MVPF_carbon": mv_c,
        f"NB_{lam_base}_musd": W - lam_base * F,
        f"NB_{lam_stress}_musd": W - lam_stress * F,
        "NB_liq_musd": W - pv(lam_t * F_t, r),
        "FNPV_gov8_musd": pv(net_fiscal, p["gov_rate"]),
        "FNPV_conc_musd": pv(net_fiscal, p["conc_rate"]),
        "EAFC_musd_yr": F * crf(r, life),
        "self_financing": bool(F <= 0),
        # F is linear in theta (dF/dtheta = -PV(S+X)): the capture share at which F = 0
        "theta_star_self_financing": (F + theta * pv(S + X, r)) / pv(S + X, r),
        "payback_year": payback,
        "payback_note": payback_note,
    }
    for y in range(1, 8):
        out[f"net_cash_y{y}_musd"] = net_fiscal[y]
    out.update({
        "min_net_cash_musd": float(net_fiscal[1:].min()),
        "headline_debt_added_pct_gdp": loan_in[0] / gdp * 100,
        "debt_after_pct_gdp": p["debt_pct_gdp"] + loan_in[0] / gdp * 100,
        "new_debt_pv5_pct_gdp": pv(debt_service, p["dsf_pv_rate"]) / gdp * 100,
        "grant_element_6": 1 - pv(debt_service, r) / d["capex"] if route["kind"] == "loan" else np.nan,
        "ppa_pv8_musd": pv(ppa, p["gov_rate"]),
        "ppa_pv8_pct_gdp": pv(ppa, p["gov_rate"]) / gdp * 100,
        "ppa_pv8_to_capex": pv(ppa, p["gov_rate"]) / d["capex"] if is_ppp else np.nan,
        "dsf_ppp_stress_pct_gdp": dsf_stress,
        "net_fiscal_liability_pv8_musd": pv(plant_payments, p["gov_rate"]) - pv(captured - X, p["gov_rate"]),
        "net_external_liability_pv8_musd": pv(plant_payments, p["gov_rate"]) - pv(S, p["gov_rate"]),
    })
    ledger = pd.DataFrame({
        "year": t, "calendar_year": years, "fuel_saved_S": S, "captured_theta_S": captured,
        "excise_lost": X, "debt_service": debt_service, "ppa_payment": ppa, "om_public": om_pub,
        "repl_public": repl_pub, "loan_in": loan_in, "capex_public": capex_pub,
        "net_fiscal": net_fiscal, "F_t": F_t, "W_t": W_t, "carbon_low": carbon["low"],
    })
    return out, ledger


def run_routes(p, routes=None):
    rows, ledgers = [], {}
    for key, rt in (routes or route_book(p)).items():
        res, led = evaluate(p, rt)
        res["route"] = key
        rows.append(res)
        ledgers[key] = led
    return pd.DataFrame(rows), ledgers


# =============================================================================
# 4. SELF-CHECKS
# =============================================================================
def self_checks(p):
    # (a) CRF reference values quoted in notes s.8
    for (r, n), ref in {(0.08, 25): 0.094, (0.08, 20): 0.102, (0.11, 20): 0.126, (0.08, 15): 0.117}.items():
        assert abs(crf(r, n) - ref) < 0.0006, (r, n, crf(r, n))
    # (b) a loan's debt service discounted at its own rate equals the principal
    for rate, tenor, grace in [(0.08, 7, 0), (0.08, 25, 0), (0.015, 30, 5)]:
        i, a = loan_schedule(100.0, rate, tenor, grace, tenor)
        assert abs(pv(i + a, rate) - 100.0) < 1e-6
    # (c) financing neutrality: with resident financiers, ENPV equals the WB ENPV on every route
    q = dict(p, financier_resident_share=1.0)
    df, _ = run_routes(q)
    assert np.allclose(df["ENPV_6_musd"], df["ENPV_wb_6_musd"]), "financing neutrality fails"
    # (d) theta moves value between W and F one-for-one: ENPV unchanged
    e = [run_routes(dict(p, theta=th))[0]["ENPV_6_musd"].values for th in (0.0, 0.5, 1.0)]
    assert np.allclose(e[0], e[1]) and np.allclose(e[1], e[2]), "ENPV depends on theta"
    # (e) carbon switch: carbon in W reproduces the memo "incl. carbon" ENPV
    a, _ = run_routes(p)
    b, _ = run_routes(dict(p, carbon_in_w=True))
    assert np.allclose(a["ENPV_6_carbon_musd"], b["ENPV_6_musd"])
    # (f) NB at lambda = 1 equals ENPV
    assert np.allclose(a["W_6_musd"] - 1.0 * a["F_6_musd"], a["ENPV_6_musd"])


# =============================================================================
# 5. SENSITIVITY
# =============================================================================
SENS_COLS = ["avoided_cost_usd_kwh", "ppa_tariff_usd_kwh", "yr1_plant_payment_usd_kwh",
             "ENPV_wb_6_musd", "ENPV_6_musd", "FNPV_gov8_musd", "W_6_musd", "F_6_musd",
             "MVPF", "MVPF_note", "NB_1.2_musd", "NB_2.0_musd", "NB_liq_musd", "net_cash_y1_musd",
             "headline_debt_added_pct_gdp", "ppa_pv8_pct_gdp"]


def sensitivity(p):
    out = []

    def add(name, value, df):
        df = df.copy()
        df.insert(0, "value", value)
        df.insert(0, "sensitivity", name)
        out.append(df[["sensitivity", "value", "route"] + SENS_COLS])

    for b in (60.0, 80.0, 110.0):
        add("Brent $/bbl", b, run_routes(dict(p, brent=b))[0])
    for m in (0.7, 1.0, 1.3):
        add("capex multiplier", m, run_routes(dict(p, capex_mult=m))[0])
    for w in (0.07, 0.085, 0.11, 0.13):
        rt = {"IPP": {"label": f"IPP + PPA, WACC {w:.1%}", "kind": "ppa", "wacc": w}}
        add("IPP WACC", w, run_routes(p, rt)[0])
    for n in (7, 15, 25):
        rt = {"R1 (8%)": {"label": f"Budget, commercial 8%, {n}-yr", "kind": "loan",
                          "rate": p["comm_rate"], "tenor": n, "grace": 0}}
        add("commercial tenor (yrs)", n, run_routes(p, rt)[0])
    for th in (0.0, 0.5, 1.0):
        add("theta (fiscal capture)", th, run_routes(dict(p, theta=th))[0])
    return pd.concat(out, ignore_index=True)


# =============================================================================
# 6. MARKDOWN PRINTING HELPERS
# =============================================================================
def md_table(df, fmt=None, default="{:,.1f}"):
    fmt = fmt or {}
    cols = list(df.columns)
    lines = ["| " + " | ".join(str(c) for c in cols) + " |",
             "|" + "|".join("---" if i == 0 else "---:" for i in range(len(cols))) + "|"]
    for _, row in df.iterrows():
        cells = []
        for c in cols:
            v = row[c]
            if isinstance(v, (bool, np.bool_)):
                cells.append("yes" if v else "no")
            elif isinstance(v, (int, float, np.integer, np.floating)):
                cells.append("n/a" if pd.isna(v) else fmt.get(c, default).format(v))
            else:
                cells.append(str(v))
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def mvpf_text(row, col="MVPF"):
    return row["MVPF_note"] if row["MVPF_note"] else f"{row[col]:.2f}"


# =============================================================================
# 7. MAIN
# =============================================================================
def main():
    p = BASE
    self_checks(p)
    d = derive(p)
    res, ledgers = run_routes(p)

    # ---- Write CSVs ----------------------------------------------------------
    first = ["route", "label"]
    res = res[first + [c for c in res.columns if c not in first]]
    res.round(4).to_csv(OUT_DIR / "sids_worked_example_results.csv", index=False)
    sens = sensitivity(p)
    sens.round(4).to_csv(OUT_DIR / "sids_worked_example_sensitivity.csv", index=False)

    # ---- Derived inputs -----------------------------------------------------
    print("## Derived inputs (Brent $%.0f)\n" % p["brent"])
    rows = [
        ("Energy displaced (GWh/yr)", f"{d['e_gwh']:.1f} ({d['share_displaced']:.0%} of diesel generation)"),
        ("Capex PV / BESS / integration / total ($m)",
         f"{d['capex_pv']:.1f} / {d['capex_bess']:.1f} / {d['capex_int']:.1f} / {d['capex']:.1f} "
         f"({d['capex'] / p['gdp_musd']:.1%} of GDP)"),
        ("O&M ($m/yr); BESS replacement yr %d ($m)" % p["bess_repl_year"], f"{d['om']:.2f}; {d['repl']:.1f}"),
        ("Diesel fuel cost / avoided cost ($/kWh)", f"{d['fuel_usd_kwh']:.3f} / {d['avoided_usd_kwh']:.3f}"),
        ("Avoided diesel cost S ($m/yr)", f"{d['S']:.2f} ({d['S'] / p['gdp_musd']:.2%} of GDP)"),
        ("Whole-system diesel fuel bill ($m/yr)", f"{d['diesel_fuel_bill']:.1f} ({d['diesel_fuel_bill'] / p['gdp_musd']:.1%} of GDP)"),
        ("Implied heat rate (MJ/kWh) / efficiency", f"{d['heat_rate_mj_kwh']:.2f} / {d['efficiency']:.0%}"),
        ("CO2 factor (kg/L; t/MWh); avoided (kt/yr)",
         f"{d['kgco2_per_l']:.2f}; {d['tco2_per_mwh']:.3f}; {d['ktco2']:.1f}"),
        ("Diesel litres avoided (m L/yr)", f"{d['litres_m']:.1f}"),
        ("Economic LCOE at 6% / 8% ($/kWh)",
         " / ".join(f"{((d['capex'] + d['repl'] / (1 + r) ** p['bess_repl_year']) * crf(r, p['life']) + d['om']) / d['e_gwh']:.3f}"
                    for r in (0.06, 0.08))),
        ("SPC low path 2028 / 2052 ($/t, 2017 US$)",
         " / ".join(f"{v:.0f}" for v in spc_path(p, [2028, 2052], "low"))),
    ]
    print(md_table(pd.DataFrame(rows, columns=["Item", "Value"])))
    sens_brent_dS = d["e_gwh"] / p["sfc_kwh_per_l"] / L_PER_BBL * 10  # $m per $10/bbl on displaced energy
    print(f"\nFuel-bill sensitivity: ${sens_brent_dS:.2f} m/yr per $10/bbl on the displaced 90 GWh; "
          f"${d['diesel_gwh'] / p['sfc_kwh_per_l'] / L_PER_BBL * 10:.2f} m/yr on the whole 300 GWh.")
    # Break-even Brent for the financing-neutral ENPV
    af = (1 - (1 + p["sdr"]) ** -p["life"]) / p["sdr"]
    cost_pv = d["capex"] + d["om"] * af + d["repl"] / (1 + p["sdr"]) ** p["bess_repl_year"]
    print(f"Break-even Brent for ENPV_wb = 0 at 6%: ${brent_for_avoided_cost(p, cost_pv / (d['e_gwh'] * af)):.0f}/bbl")

    # ---- Main route table ---------------------------------------------------
    print("\n## Main results by route (Brent $80, theta = 0.5, $m unless stated)\n")
    t1 = res[["route", "ENPV_wb_6_musd", "financing_premium_pv6_musd", "ENPV_6_musd", "ENPV_6_carbon_musd",
              "W_6_musd", "F_6_musd"]].copy()
    t1["MVPF"] = res.apply(mvpf_text, axis=1)
    t1["NB(1.2)"] = res["NB_1.2_musd"]
    t1["NB(2.0)"] = res["NB_2.0_musd"]
    t1["NB(liq)"] = res["NB_liq_musd"]
    t1["FNPV@8%"] = res["FNPV_gov8_musd"]
    t1.columns = ["Route", "ENPV_wb", "Fin. premium", "ENPV", "ENPV+CO2", "W", "F", "MVPF",
                  "NB(1.2)", "NB(2.0)", "NB(liq)", "FNPV@8%"]
    print(md_table(t1, default="{:,.0f}"))

    print("\n## Debt and liability view (% of GDP unless stated)\n")
    t2 = res[["route", "headline_debt_added_pct_gdp", "debt_after_pct_gdp", "new_debt_pv5_pct_gdp",
              "ppa_pv8_pct_gdp", "ppa_pv8_to_capex", "dsf_ppp_stress_pct_gdp",
              "net_fiscal_liability_pv8_musd", "net_external_liability_pv8_musd", "grant_element_6"]].copy()
    t2.columns = ["Route", "Headline debt added", "Debt after", "PV new debt @5%", "PPA PV@8%",
                  "PPA PV / capex", "LIC-DSF PPP stress", "Net fiscal liab. PV@8% ($m)",
                  "Net external liab. PV@8% ($m)", "Grant element @6%"]
    print(md_table(t2, fmt={"PPA PV / capex": "{:.2f}", "Grant element @6%": "{:.0%}",
                            "Net fiscal liab. PV@8% ($m)": "{:,.0f}", "Net external liab. PV@8% ($m)": "{:,.0f}"}))

    print("\n## Switching values\n")
    sv = pd.DataFrame({
        "Route": res["route"],
        "lambda* (NB = 0) = MVPF": res.apply(mvpf_text, axis=1),
        "theta* (F = 0)": res["theta_star_self_financing"],
        "Brent* (yr-1 payment = avoided cost)": [f"${b:.0f}" if b > 0 else "any price"
                                                 for b in res["breakeven_brent_yr1"]],
    })
    print(md_table(sv, fmt={"theta* (F = 0)": "{:.2f}"}))

    # ---- The trap: payments vs the fuel bill they replace -------------------
    print("\n## Annual plant payment vs the fuel bill it replaces (year 1)\n")
    rows = []
    for _, r_ in res.iterrows():
        be = r_["breakeven_brent_yr1"]
        row = {"Route": r_["route"], "Payment $m": r_["yr1_plant_payment_musd"],
               "Payment $/kWh": r_["yr1_plant_payment_usd_kwh"],
               "Break-even Brent": f"${be:.0f}" if be > 0 else "any price"}
        for b in (60, 80, 110):
            avoided = d["e_gwh"] * (fuel_cost_usd_kwh(p, b) + p["diesel_vom_usd_kwh"])
            row[f"Fuel bill avoided @${b} ($m)"] = avoided
            row[f"Payment < bill @${b}?"] = "yes" if r_["yr1_plant_payment_musd"] < avoided else "NO"
        rows.append(row)
    print(md_table(pd.DataFrame(rows), fmt={"Payment $/kWh": "{:.3f}"}))

    print("\n## Net cash flow to budget/utility, years 1-7 ($m; theta = 0.5)\n")
    cash_cols = ["route"] + [f"net_cash_y{y}_musd" for y in range(1, 8)] + ["min_net_cash_musd", "payback_note"]
    t3 = res[cash_cols].copy()
    t3.columns = ["Route"] + [f"Y{y}" for y in range(1, 8)] + ["Worst year (1-30)", "Cumulative payback"]
    print(md_table(t3))

    print("\n## Same, system view (theta = 1: public sector keeps the whole fuel saving)\n")
    r1, _ = run_routes(dict(p, theta=1.0))
    t4 = r1[cash_cols].copy()
    t4.columns = t3.columns
    print(md_table(t4))

    print("\n## R1a ledger, selected years ($m; theta = 0.5)\n")
    led = ledgers["R1a"]
    led = led[led["year"].isin([0, 1, 2, 7, 8, 15, 25])][
        ["year", "fuel_saved_S", "captured_theta_S", "debt_service", "om_public", "repl_public",
         "loan_in", "capex_public", "net_fiscal"]]
    print(md_table(led, fmt={"year": "{:.0f}"}))

    # ---- Sensitivity pivots -------------------------------------------------
    print("\n## Sensitivity (full table in sids_worked_example_sensitivity.csv)\n")
    for name in ("Brent $/bbl", "capex multiplier", "theta (fiscal capture)"):
        s = sens[sens["sensitivity"] == name]
        for metric in ("ENPV_6_musd", "NB_1.2_musd", "FNPV_gov8_musd", "net_cash_y1_musd"):
            pt = s.pivot(index="route", columns="value", values=metric).reset_index()
            pt.columns = ["Route"] + [f"{name} = {v:g}" for v in pt.columns[1:]]
            print(f"\n{metric} by {name}\n")
            print(md_table(pt, default="{:,.0f}"))
        if name == "theta (fiscal capture)":
            s2 = s.copy()
            s2["MVPF_txt"] = s2.apply(mvpf_text, axis=1)
            pt = s2.pivot(index="route", columns="value", values="MVPF_txt").reset_index()
            pt.columns = ["Route"] + [f"theta = {v:g}" for v in pt.columns[1:]]
            print("\nMVPF by theta\n")
            print(md_table(pt))
    for name in ("IPP WACC", "commercial tenor (yrs)"):
        s = sens[sens["sensitivity"] == name].copy()
        s["MVPF_txt"] = s.apply(mvpf_text, axis=1)
        cols = ["value", "ppa_tariff_usd_kwh", "yr1_plant_payment_usd_kwh", "avoided_cost_usd_kwh", "ENPV_6_musd",
                "FNPV_gov8_musd", "MVPF_txt", "NB_1.2_musd", "NB_2.0_musd", "NB_liq_musd", "net_cash_y1_musd",
                "ppa_pv8_pct_gdp"]
        print(f"\n{name}\n")
        print(md_table(s[cols], fmt={"value": "{:g}", "ppa_tariff_usd_kwh": "{:.3f}",
                                     "yr1_plant_payment_usd_kwh": "{:.3f}", "avoided_cost_usd_kwh": "{:.3f}"}))

    print(f"\nWrote {OUT_DIR / 'sids_worked_example_results.csv'}")
    print(f"Wrote {OUT_DIR / 'sids_worked_example_sensitivity.csv'}")
    print("Self-checks passed: CRF references, loan PV at own rate, PSV identity ENPV = W - F, "
          "financing neutrality with resident financiers, theta invariance of ENPV, carbon switch, NB(1) = ENPV.")


if __name__ == "__main__":
    main()
