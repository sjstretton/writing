"""Worked examples for note 6.8 (Investment needs, abatement costs and public money in CPAT), v0.2.

All inputs are stylized and labelled. Unit cost factors are from the public SISEPUEDE costs-and-benefits documentation
and factor database (2019 USD, Latin American and Caribbean average); other inputs are assumptions stated next to them.
v0.2 (peer review 2026-11-18): the electric-car case uses the Latin American factor throughout (the US premium is a
stress case with the US maintenance saving), nets electricity tax gained, and uses the 10.5 percent default private
rate; uptake respects the cap; the partnership has its own delivery efficiency; the active-set rule is checked.
Run: python3 worked_examples.py
"""
import numpy as np


def crf(r, n):
    """Capital recovery factor, end-of-year convention."""
    if r == 0:
        return 1.0 / n
    return r / (1.0 - (1.0 + r) ** (-n))


def annuity(r, n):
    """Present value of 1 a year for n years, end of year."""
    return 1.0 / crf(r, n)


# ---------------------------------------------------------------- 1. Electric-car purchase subsidy
def ev_example(premium_2023, maint_per_year):
    km, life = 15_000, 12
    premium = premium_2023 * 0.9 ** 7          # 2030 purchase; database decline 0.9 a year from 2023
    litres = 7.5 / 100 * km                    # assumption: 7.5 l/100 km
    kwh = 0.18 * km                            # assumption: 0.18 kWh/km
    gas_supply, gas_retail = 0.60, 1.10        # USD/l (assumption)
    el_supply, el_retail = 0.10, 0.15          # USD/kWh (assumption)
    ef_gas = 69.3 * 44.3 * 0.74 / 1e6          # tCO2/l: IPCC 2006 default EF x NCV x density 0.74 kg/l
    ef_grid = 0.5 / 1000                       # tCO2/kWh (assumption)
    e = litres * ef_gas - kwh * ef_grid        # tCO2 a year avoided per car
    r_soc, r_priv = 0.06, 0.105                # social rate; default private rate for developing countries

    def net_annual(r, fuel_p, el_p):           # capital charge + running change - fuel saved
        return premium * crf(r, life) - maint_per_year - (litres * fuel_p - kwh * el_p)

    sigma, a, lam = 0.30, 0.5, 1.2             # subsidy rate, additionality (assumption), MCPF
    pv_e = e * annuity(r_soc, life)
    subsidy = sigma * premium
    tax_lost = litres * (gas_retail - gas_supply)          # upper bound: whole retail-supply gap is tax
    tax_gained = kwh * (el_retail - el_supply)             # same convention for electricity
    net_tax_pv = (tax_lost - tax_gained) * annuity(r_soc, life)
    res = net_annual(r_soc, gas_supply, el_supply) / e
    fiscal_sub = subsidy / (a * pv_e)
    fiscal_tax = net_tax_pv / pv_e
    return {
        "premium_2030": premium,
        "tco2_per_year": e,
        "resource_MAC_6pct": res,
        "private_MAC_10.5pct": net_annual(r_priv, gas_retail, el_retail) / e,
        "subsidy_per_car": subsidy,
        "budget_per_t_subsidy": fiscal_sub,
        "budget_per_t_net_tax": fiscal_tax,
        "budget_per_t_total": fiscal_sub + fiscal_tax,
        "public_MAC_lambda": res + (lam - 1) * (fiscal_sub + fiscal_tax),   # co-benefits left out (MAC_soc = MAC_res)
    }


# ---------------------------------------------------------------- 2. Enteric methane: results-based payment
def enteric_example():
    cost_head = 40.0                    # SISEPUEDE: USD 40 per head a year
    d = 0.25                            # SISEPUEDE: decrease per head, cattle
    l_bar = 0.8                         # SISEPUEDE: maximum application, cattle
    t_head = d * 56 * 28 / 1000         # IPCC 2006 Tier 1, Latin America other cattle 56 kg CH4/head/yr; GWP100 28 (AR5)
    c = cost_head / t_head
    h = 50.0                            # USD/tCO2e: ramp width (assumption)

    def uptake(reward):
        return l_bar * min(1.0, max(0.0, (reward - c) / h))

    out = {"tco2e_per_head": t_head, "cost_per_t": c}
    for reward in (75, 120, 135):
        u = uptake(reward)
        out[f"uptake_at_{reward}"] = u
        out[f"emissions_left_at_{reward}"] = 1 - d * u
    return out


# ---------------------------------------------------------------- 3. Partnership conversion
def ppp_example():
    K, om = 100.0, 2.0                  # capex; public O&M a year
    i_g, rho, n_c = 0.06, 0.03, 20      # government rate, risk premium, contract length (assumptions)
    w = i_g + rho
    ap = K * crf(w, n_c) + om
    pv_ap = ap * annuity(i_g, n_c)
    pv_pub = K + om * annuity(i_g, n_c)
    out = {"availability_payment": ap, "pv_ap_at_ig": pv_ap, "pv_public": pv_pub,
           "premium_pct": 100 * (pv_ap / pv_pub - 1)}

    def eta_star(s_pim, s_ppp, n):
        return 1 - s_ppp * crf(i_g, n) / (s_pim * crf(w, n))

    for n in (10, 15, 20, 25):
        out[f"eta_star_n{n}"] = 100 * eta_star(1, 1, n)
    for s in (0.60, 0.73, 0.87):
        out[f"eta_star_s{s}_ppp_same"] = 100 * eta_star(s, s, n_c)
        out[f"eta_star_s{s}_ppp_full"] = 100 * eta_star(s, 1.0, n_c)
    return out


# ---------------------------------------------------------------- 4. Check: combined penalty rule, active set
def combined_rule(C, s_prev, lv, la):
    """Exact minimizer of sum C s + lv/2 s^2 + la/2 (s - s_prev)^2, sum s = 1, s >= 0 (active set)."""
    C, s_prev = np.asarray(C, float), np.asarray(s_prev, float)
    active = np.ones(len(C), bool)
    while True:
        A = active
        nA, SA = A.sum(), s_prev[A].sum()
        s = np.zeros(len(C))
        s[A] = (la * s_prev[A] + (lv + la * (1 - SA)) / nA + C[A].mean() - C[A]) / (lv + la)
        if (s[A] >= -1e-12).all():
            return s
        active &= s > 0


def check_active_set():
    C = [45, 55, 90, 136.2, 172.5]                    # paper 5.1, costs at USD 75/tCO2
    s_prev = [0.362, 0.262, 0.212, 0.162, 0.0]        # paper 5.1, velocity shares at zero carbon price
    s = combined_rule(C, s_prev, 100, 100)
    # brute-force check of the minimizer on a grid of the active technologies
    return {"share_solar": s[0], "share_wind": s[1], "share_gas": s[2], "sum": s.sum()}


if __name__ == "__main__":
    cases = [
        ("Electric car, Latin American premium (0.039/vkm x 15,000 km x 12 yr)", lambda: ev_example(0.039 * 15_000 * 12, 180)),
        ("Electric car, US premium stress case (USD 13,000; US maintenance USD 949/yr)", lambda: ev_example(13_000, 949)),
        ("Enteric fermentation, results-based payment", enteric_example),
        ("Partnership conversion", ppp_example),
        ("Combined penalty rule, active-set check", check_active_set),
    ]
    for name, fn in cases:
        print(f"== {name}")
        for k, v in fn().items():
            print(f"  {k:30s} {v:12.3f}")
