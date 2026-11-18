"""Worked examples for paper 6.8 (Investment needs, abatement costs and public money in CPAT).

All inputs are stylized and labelled. Unit cost factors are from the public SISEPUEDE
costs-and-benefits documentation (2019 USD, LAC average); other inputs are assumptions
stated next to them. Run: python3 worked_examples.py
"""


def crf(r, n):
    """Capital recovery factor, end-of-year convention."""
    if r == 0:
        return 1.0 / n
    return r / (1.0 - (1.0 + r) ** (-n))


def annuity_pv(r, n):
    """Present value of 1 a year for n years, end of year."""
    return 1.0 / crf(r, n)


def ev_example():
    # SISEPUEDE docs (transport page): USD 12,000 premium + USD 1,000 charger, 15,000 km/yr,
    # 12-year life, maintenance saving USD 0.012/vkm, capital factor declines by 0.9 a year from 2023.
    premium_2023 = 12_000 + 1_000
    premium = premium_2023 * 0.9 ** 7          # 2030 purchase
    km, life = 15_000, 12
    maint_saving = 0.012 * km                  # USD/yr
    # Assumptions (stylized): gasoline car 7.5 l/100 km; EV 0.18 kWh/km (as in the investment-needs tool)
    litres = 7.5 / 100 * km
    kwh = 0.18 * km
    gas_supply, gas_retail = 0.60, 1.10        # USD/l (assumption; retail as in paper 5.1's example)
    el_supply, el_retail = 0.10, 0.15          # USD/kWh (assumption)
    ef_gas = 69.3 * 44.3 * 0.74 / 1e6          # tCO2/l: IPCC 2006 default EF x NCV x density 0.74 kg/l
    ef_grid = 0.5 / 1000                       # tCO2/kWh (assumption)
    e = litres * ef_gas - kwh * ef_grid        # tCO2/yr avoided per EV

    def net_annual(r, fuel_p, el_p):
        return premium * crf(r, life) - maint_saving - (litres * fuel_p - kwh * el_p)

    out = {}
    out["premium_2030"] = premium
    out["tco2_per_year"] = e
    out["resource_MAC_6pct"] = net_annual(0.06, gas_supply, el_supply) / e
    out["private_MAC_12pct"] = net_annual(0.12, gas_retail, el_retail) / e
    # Subsidy: 30% of the premium, additionality 0.5, lambda 1.2.
    sigma, a, lam = 0.30, 0.5, 1.2
    pv_e = e * annuity_pv(0.06, life)                       # discounted tonnes per EV
    subsidy = sigma * premium
    lost_excise_pv = litres * (gas_retail - gas_supply) * annuity_pv(0.06, life)  # per additional EV (upper bound: all of retail-supply margin is tax)
    resource_cost_pv = net_annual(0.06, gas_supply, el_supply) * annuity_pv(0.06, life)
    out["subsidy_per_ev"] = subsidy
    out["fiscal_cost_per_t"] = subsidy / (a * pv_e) + lost_excise_pv / pv_e
    out["public_MAC_lambda"] = resource_cost_pv / pv_e + (lam - 1) * out["fiscal_cost_per_t"]
    # Shadow-price equivalent of the subsidy on CPAT's efficiency margin: sh = p*sigma/(1-sigma)
    out["sh_equiv_per_litre"] = gas_retail * sigma / (1 - sigma)
    return out


def enteric_example():
    # SISEPUEDE docs (agriculture page): USD 40 per head; transformation cuts enteric CH4 by 25% per head (cattle).
    # IPCC 2006 Tier 1 enteric factor, Latin America "other cattle": 56 kg CH4/head/yr; GWP100 28 (AR5).
    cost_head = 40.0
    t_head = 0.25 * 56 * 28 / 1000
    c = cost_head / t_head
    kappa = 50.0  # USD/tCO2e: width of the uptake ramp (soft-constraint parameter, assumption)

    def uptake(price):
        return min(1.0, max(0.0, (price - c) / kappa))

    return {
        "tco2e_per_head": t_head,
        "cost_per_t": c,
        "uptake_fee_75": uptake(75),
        "uptake_fee_120": uptake(120),
        "uptake_sub_120": uptake(120),
        "uptake_fee_75_plus_sub_60": uptake(75 + 60),
    }


def ppp_example():
    # Stylized public asset: capex 100, life 25, public O&M 2% of capex a year.
    K, n, om = 100.0, 25, 2.0
    i_g = 0.06       # government borrowing rate (assumption)
    rho = 0.03       # PPP risk premium over i_g (assumption)
    w = i_g + rho
    n_c = 20         # contract length
    e = 0.0          # construction-cost efficiency of the PPP (assumption: none)
    ap = (1 - e) * K * crf(w, n_c) + om
    pv_ap = ap * annuity_pv(i_g, n_c)
    pv_public = K + om * annuity_pv(i_g, n_c)
    # Break-even efficiency gain that makes the PPP cost no more than public delivery
    e_star = 1 - (K * crf(i_g, n_c)) / (K * crf(w, n_c))
    return {
        "availability_payment": ap,
        "pv_ap_at_ig": pv_ap,
        "pv_public_route": pv_public,
        "financing_premium": pv_ap - pv_public,
        "breakeven_efficiency": e_star,
        "crf_public_25y": crf(i_g, n),
    }


if __name__ == "__main__":
    for name, fn in [("EV purchase subsidy", ev_example), ("Enteric fermentation", enteric_example), ("PPP conversion", ppp_example)]:
        print(f"== {name}")
        for k, v in fn().items():
            print(f"  {k:28s} {v:12.3f}")
