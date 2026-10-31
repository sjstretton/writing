# Internal tools, part 2: the combined GIMF / DIGNAD / DIGNAR tool and the investment-needs models

Source: the public repo `cpmodel/new-ai-tools` (shallow clone at commit b77f69a, 20 Oct 2026), read directly by the coordinator. These are the user's own tools. The internal note `internal_cdpm_and_macro_tool.md` did not find them because they are not in CPAT-AI or CPAT-CDPM. Paths below are relative to the repo root.

## 1. What the "combined GIMF DIGNAD DIGNAR tool" is

`MacroFiscalModels/` holds simplified Python re-implementations of IMF and World Bank tools. Method note: `MacroFiscalModels/MacroFiscalModels_Method_v0_1.md`.

| File | Content |
|---|---|
| `gimf_lite.py` | One-country GIMF: Blanchard-Yaari OLG (non-Ricardian) plus liquidity-constrained households, sticky prices and wages, Taylor rule, UIP, public capital, deficit fiscal rule. Climate add-on: `ig_extra` (public investment), `IX` (private investment), `sav` (net energy saving, % GDP, entered as a value-added gain), `dfs` (debt-financed share), `g_extra` (spending that builds no capital), `rev_extra` (earmarked revenue). |
| `dignad_lite.py` | DIGNAD: savers and hand-to-mouth households; standard (`ig1`) and adaptation (`ig2`, cost premium `mu_a`) public capital; PIMA efficiency `s`; disasters; grant / concessional / commercial financing. With `rents0 > 0` it becomes DIGNAR-lite (resource rents, `gov_take`, `rents_path`). |
| `lic_dsf.py` | LIC-DSF-lite (2018 framework): Composite Indicator, thresholds, loan-cohort PV, five indicators, standard plus disaster stress tests, mechanical rating. Coefficients are from memory and still need checking. |
| `nmim_bridge.py` | NMIM to the models: `pub` (direct budget need = P1 + public gap of P4), split into `pub_cap` and `pub_spend`; `prv` (private investment); `sav` (fuel savings less extra O&M); `power_co2`; `wacc`. |
| `calibration.py` | Shared calibration from the Tax and Macro-Fiscal Dashboard panel, plus a model-choice rule and a cross-check. |
| `integrated.py` | Chain: dashboard → NMIM → PriceFeasibility (feasible carbon-pricing revenue, power only) → GIMF-, DIGNAD- or DIGNAR-lite → LIC-DSF-lite → `results/integrated_results.csv` (186 countries). |

### Shared calibration (`calibration.py`, method §4a)

- Efficiency: `s` = 1 − efficiency gap. The gap comes from PEFA PI-11 (score 1 → 40%, score 4 → 13%, linear), otherwise IMF (2015) by income group.
- Return on public capital `Rg`: 20 / 17 / 15 / 10% from LIC to HIC (income-group assumption).
- Tax split: 40% consumption, 45% labour, 15% capital.
- Debt: concessional share = IDS multilateral share of PPG external debt.
- Borrowing cost: IDS private creditor rate less 3 points, kept between 3% and 8%.
- Depreciation: δ = 7%, δ_G = 4%.
- Model choice: DIGNAD-lite for LICs, disaster-prone countries, and LMICs with a multilateral share of at least 50%. DIGNAR-lite where fossil rents are at least 10% of GDP and the country is not high income. GIMF-lite otherwise.

### DIGNAD-lite parameters (dataclass `Params`)

| Group | Parameters (default) |
|---|---|
| Public capital | `s` 0.6, `Rg` 0.20, `ig1` 0.06, `ig2` 0.01, `mu_a` 0.25 |
| Fiscal and debt | `tau_y`, `tau_c`, `gc`, `grants` 0.02, `dk` 0.30 at `rk` 1%, `dc` 0.20, `eta_g` 0.05, `lam_tau` and `lam_tr` 0.05 (fiscal rule) |
| Disaster | `eps_k`, `eps_g`, `rho_res` 0.8, `eps_a`, `rho_a`, `theta_a` |
| Reconstruction and financing | `rec`, `rho_rec`, `bbb`, `sh_grant` 0.3, `sh_conc` 0.3, `amort_k` |
| Programme | `prog` (public investment path, % GDP), `prog_bbb` (adaptation share), `prog_taper`, `prog_spend` (spending that builds no capital), `rev` (earmarked revenue, % GDP) |
| Resource block | `rents0`, `gov_take`, `rents_path` |

GIMF-lite `Params` adds `psi` 0.25, `Rg` 0.15, `s` 0.7, `g`, `ig`, `tau_l`, `tau_c`, `tau_k`, `b` 0.5, `nfd`, `lam_b`, instrument `tr` / `tau_l`, `zeta`, `dfs`.

### Open items already on the tool's own TODO list (`MacroFiscalModels/TODO.md`; this proposal should deliver them)

1. **Energy-savings channel in DIGNAD-lite** (GIMF-lite already has it), so mitigation investment earns its real return, the fuel and O&M savings. Marked "most important of the four".
2. **Sector-weighted return on public capital** `Rg`:
   - high for grids, transmission, public transport and access;
   - low for replacement generation;
   - near zero domestically for land use and non-CO2.
3. **Absorptive-capacity costs:** unit costs rise with the speed of the scale-up.
4. **Efficiency-return switch:** hold the output elasticity fixed rather than `Rg`, following Berg et al. 2019.
5. **One model with switches:** GIMF-lite as the core, with DIGNAD blocks added as switches.
6. **DIGNAR resource block** using the dashboard's rent indicators.
7. *Done:* spending versus capital split in the bridge.
8. **Fuller treatment of investment efficiency:**
   - PIMA scores;
   - absorptive capacity;
   - a reform scenario closing up to two-thirds of the gap (IMF 2015);
   - **execution rates (BOOST) as a separate leak**.
9. **Tariff revenue versus public return:** model the utility explicitly. That means:
   - tariff revenue and cost recovery;
   - utility debt as a contingent liability in the DSF (PEFA PI-10.3);
   - keeping financial return (tariffs, a transfer from users) apart from economic return (fuel savings, reliability, access).

Further TODO items relevant here:
- Item 10: energy savings must reach DIGNAD/DIGNAR countries too, for consistency.
- Item 16: the tariff rise has an economic cost the macro models do not see.
- Item 17: data issues. The Solomon Islands budget need is 91% of GDP in 2030. In Jamaica, power-only pricing revenue is 5.5 times the budget need, which shows how large the oil bill of an oil-fired island is.

### Known limitations (method §6; integrated-run caveats)

- Energy savings enter as a value-added gain, though for imported fuel they are really a terms-of-trade gain. In the Kenya example they drive about two-thirds (later 84%) of the long-run GDP gain.
- GIMF-lite countries show a median +7.7% GDP gain by 2050, against +0.7% for DIGNAD-lite countries. The gap comes from the savings channel, not from the economics.
- Utility (P2) investment enters as private investment. State-owned utility debt and tariff shortfalls are not counted in public debt.
- Splitting spending from capital lowers the GDP effect a lot. About 80% of Kenya's 2030 budget need, and 97% of Liberia's, is land-use and non-CO2 spending.
- LIC-DSF-lite: 5 of 66 LIC/LMIC ratings worsen with the programme (Cameroon, DR Congo, Liberia, Madagascar, Chad).

## 2. The CDPM-based investment-needs method and NMIM

**`InvestmentNeeds/README.md`.** It states: "CDPM was formerly called SiSePuede." The method note is *Global Investment Needs for Climate Action: A Method Based on CDPM (formerly SiSePuede)* (October 2026), equations 1-7. It is implemented in `Mitigation_Investment_Needs_v1.1.xlsx` (2030 snapshot, 195 economies).

**Three cost-of-capital lenses:**
- (a) market country WACC, with fuel and operating savings;
- (b) World Bank 6% (Fay et al. 2016; IBRD about 5.2% by switch), with savings;
- (c) as (b), plus local air-pollution co-benefits, with carbon at the WB shadow price as a memo item.

**Core equations:**
- Capital charge: `A = dI × CRF(r,n)`, `CRF = r/(1−(1+r)^−n)`.
- Incremental cost:
  - `IC(a) = dI[CRF(r_mkt,n) − b]`
  - `IC(b) = dI[CRF(6%,n) − b]`
  - `IC(c) = IC(b) − c·dI`

  Here b is savings and c is co-benefits per dollar of capital per year. Cost per tonne = IC / (a·dI).

**PIMA adjustment (public share only):**
- `I_PIMA = I[(1−π) + π/(1−gap)]`
- Gap: AE 13%, EM 27%, LIC 40% (IMF 2015), or from PEFA PI-11.
- Public share π: AE 30%, China 50%, EMDC 40%.
- Reform scenario closes two-thirds of the gap.
- BOOST capital budget execution (104 economies), PEFA PI-12.2 and climate-PFM diagnostics are reported but do not enter the formula.

**NMIM v0.2 (`InvestmentNeeds/national_model/NMIM_Method_v0_2.md`):** 186 countries, 2024-2050, CPAT norms. Incremental cost:

`IC(a)_t = Σ_s K_s,t × CRF(WACC_c, life_s) + spending_t + dO&M_t − fuel savings_t`

Asset lives: generation 25, grids 40, vehicles 12, buildings 25, industry 25 years.

**"Who pays" typology (v0.2 §4):**

| Type | Financed by |
|---|---|
| P1 Pure public | Taxes |
| P2 Regulated utility | Tariffs |
| P3 Contracted revenue | IPP PPAs, CfDs, concessions |
| P4 Viability gap | Market revenue plus a public top-up |
| P5 Pure private | Investors and households |

How the shares are set:
- They depend on cost recovery u = min(1, max(0, (1 − retail/supply cost)/0.5)) and cost of capital h = min(1, max(0, (WACC−6%)/8%)).
- They also depend on power market structure (PSRT, PPI) and fossil subsidies.
- **Direct budget need = P1 + 30% of P4.**

The method's "Financing implications" table maps each type to:
- its public role;
- its fiscal cost (P2 and P3 are *contingent*: guarantees, arrears, FX risk);
- the lens that matters.

Results: in other EMDCs, P1 + P4 are about half of net zero investment; in LICs, about two-thirds falls on the budget.

**Weak points stated by the method:**
- Type shares are judgements.
- Cost recovery ignores collection losses.
- PSRT ends in 2013.

## 3. Tax and Macro-Fiscal Dashboard (`TaxMacroFiscalDashboard/`)

Indicator config `build/config/indicators.csv` includes:

| Block | Indicators |
|---|---|
| "Can they build it?" (PIMA) | `capex_execution_rate_pct` (World Bank BOOST); `pefa_pi11_pim_score`; `pefa_pi122_asset_monitoring`; `climate_pfm_diagnostic_on_record` |
| Finance | `pefa_pi103_contingent_liabilities` |
| Fossil and climate fiscal context | energy taxes levied, fossil subsidies paid, environment-protection spending share |

The panel has 53-64 indicators for 217 countries; Appendix C has WEO ratios. **BOOST therefore already enters the tool chain, as a capital execution rate**, but it is not used in any formula yet.

## 4. Implications for the proposal (coordinator's inferences)

- The natural home for the proposed layer is between NMIM / CDPM and `MacroFiscalModels` (a new module, plus a small bridge change). Writing it in CPAT house style (method note, version notes, CAVEATS) matches how both repos work.
- NMIM's P1-P5 typology already defines which share of each line falls on the budget. The proposal should reuse it as the "payer tag", not invent a new one. P3 is exactly the PPA route; P4 is the viability gap (the Pigouvian top-up); P2 is the utility channel with contingent liabilities.
- The InvestmentNeeds lens (b)/(c) is the World Bank economic-analysis view (λ = 1). The new layer adds the fiscal ledger and the cost of public funds (λ). With λ = 1, the economic results should reproduce lens (b)/(c), which is a natural regression check.
- Efficiency has two existing, slightly different uses. InvestmentNeeds applies a cost uplift (`π/(1−gap)`); the macro models apply `s` to capital accumulation. The proposal must say which one applies where, to avoid double counting.
- TODO items 1, 2, 3, 4, 8 and 9 in `MacroFiscalModels/TODO.md` match the proposal's macro-bridge outputs one for one: energy savings, sector `Rg_j`, absorptive capacity, the efficiency/return switch, BOOST execution leak, and the utility / tariff / contingent-liability treatment.
