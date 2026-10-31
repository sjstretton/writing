# Worked example: a small island state escaping the oil trap

A diesel-dependent island replaces 30% of its diesel generation with 60 MW of solar PV and a 120 MWh battery. The same plant is financed in four ways, and each route is scored with the Public Spending Value (PSV) metrics (design brief, section 2, Steps 5-9; specification in section 3).

Files in this folder:
- `sids_worked_example.py`: the model (pure Python with numpy and pandas; run with `python3 -I sids_worked_example.py`).
- `sids_worked_example_results.csv`: one row per route, all metrics.
- `sids_worked_example_sensitivity.csv`: one row per sensitivity case and route.

All money is in US$ million ($m), in constant prices. Year 0 is construction; years 1-25 are operation. Cash flows fall at the end of each year. Numbers below are rounded from the script output.

## 1. Method in brief

**Routes.**

| Route | Financing | Terms |
|---|---|---|
| R1a | Budget, commercial loan | 8%, 7-year level annuity. This is the only market tenor the island can get. |
| R1b | Budget, commercial loan | 8%, 25-year level annuity. Shown for comparison only; not available in the base case. |
| R2 | Budget, concessional loan (IDA- or RST-type) | 1.5%, 30 years. Interest only in years 1-5, then a level annuity over years 6-30. |
| R3 | IPP with a 25-year PPA, no guarantee | WACC 11%. |
| R4 | IPP with a 25-year PPA, WB or MIGA guarantee | WACC 8.5%. |

In R1 and R2 the public utility owns the plant and pays O&M and the year-15 battery replacement. In R3 and R4 the IPP pays capex, O&M and the replacement, and recovers them through the PPA tariff.

**PPA tariff:** `T = [(capex + PV_WACC(battery replacement)) x CRF(WACC, 25) + O&M] / E`, with the end-of-year `CRF = r / (1 - (1+r)^-n)`. This is the brief's formula, with the replacement added as in the notes (`capex_opex_ppp_ppa_sids.md` s.8). The PPA is treated as take-or-pay on expected output, so every payment counts as committed.

**Agents and the fiscal capture share θ.** The public sector is the budget plus the state utility whose losses the budget covers. The avoided diesel cost is S (fuel plus variable O&M, at resource prices).
- The public sector keeps a share θ of S, plus any fuel excise X. The rest, (1 − θ), passes to electricity consumers through fuel pass-through in tariffs.
- The public sector pays the whole plant cost (debt service or PPA payments). Base tariffs are not raised.
- Lenders and IPP owners are non-residents. This is a parameter (`financier_resident_share`).

**Fiscal ledger (Step 5), per year:**

```
net fiscal flow_t = loan disbursed - public capex - debt service - public O&M - public replacement
                    - PPA payments + θ(S_t + X_t) - X_t
F_t = -(net fiscal flow_t)
```

**Decision metric (Step 6), all at the 6% social discount rate:**

```
W    = PV[(1 - θ)(S + X)] + PV[resident financiers' net receipts]   (+ carbon if switched on)
F    = PV[F_t]
ENPV = W - F                               (asserted in code against an independent calculation)
MVPF = W / F; "pays for itself" when F <= 0
NB_λ = W - λF                              at λ = 1.2 and λ = 2.0
NB(liq) = W - Σ λ_t F_t / 1.06^t           with λ_t = 2.0 in years 1-7 and 1.2 after (illustrative)
```

**Two economic NPVs.**
- `ENPV_wb` is the World Bank-style, financing-neutral ENPV: resource flows only. It is the same for every route.
- `ENPV` (= W − F) is the island's ENPV. It equals `ENPV_wb` minus the **financing premium**: the PV at 6% of what the island pays non-resident financiers, less the money they put in. A concessional loan has a negative premium (its grant element). An 8% loan or an 11%-WACC PPA has a positive one.
- With resident financiers, `ENPV = ENPV_wb` on every route. The script asserts this.

**FNPV** discounts the net fiscal flow at the government's marginal borrowing rate (8%). It is reported separately; W, F and MVPF stay on the 6% basis.

**Liabilities (Step 8).**
- Headline debt added at year 0.
- PV of PPA payments at 8%.
- LIC-DSF PPP stress: 35% of the PPP capital stock when the stock exceeds 3% of GDP (LIC-DSF Guidance Note 2017, via the notes s.3).
- Net fiscal liability: PV at 8% of the public sector's payments for the plant, minus PV at 8% of the fuel savings it captures. By construction this equals −FNPV.
- Net external liability: the same payments minus the PV of avoided fuel imports.

**Self-checks in the script:**
- CRF values match the notes' references.
- A loan's debt service, discounted at the loan rate, equals the principal.
- ENPV = W − F holds on every route.
- Financing neutrality holds when financiers are resident.
- ENPV does not change with θ.
- The carbon switch is consistent with the memo column.
- NB at λ = 1 equals ENPV.

## 2. Assumptions

Source tags:
- "notes s.N" = `capex_opex_ppp_ppa_sids.md`, section N, where the full citations are.
- "theory QN" = `theory_rules_mcpf_mvpf.md`, question N.
- "brief" = `design_brief.md`, section 3.

| Parameter | Value | Source or status |
|---|---|---|
| Electricity demand | 300 GWh/yr | brief; notes s.4/s.8: St Lucia 399 GWh, St Vincent and the Grenadines (SVG) 136 GWh (NREL Energy Snapshots 2020) |
| Diesel share of generation | 100% | brief ("almost all diesel"); notes s.4: St Lucia about 99% |
| GDP | $2.0 bn | illustrative (brief; notes s.8 "assumption, not verified") |
| Public debt | 85% of GDP, high risk of distress | illustrative (brief) |
| Construction year (t = 0) | 2027 | illustrative |
| PV size; battery size | 60 MW; 120 MWh | brief |
| PV capacity factor; share delivered | 18%; 95% | illustrative (notes s.6/s.8 assumptions; ASPIRE tariffs imply about 16.5%) |
| PV capex | $1,200/kW | notes s.4/s.8 inference: IRENA RPGC 2024 global $691/kW × 1.5-1.7 island premium implied by Maldives ASPIRE tariffs |
| Battery capex | $350/kWh | illustrative (notes s.8: IRENA RPGC 2025 global ~$140/kWh × island premium, assumption) |
| Integration and soft costs | 5% of total capex | illustrative (notes s.8) |
| O&M | 1.5% of capex a year ($1.8 m) | brief; notes s.8 give r_PV 1-2% (assumption). The notes' component split (PV 1.5%, battery 2.5%) would give $2.1 m |
| Asset life | 25 years | brief; notes s.8 (assumption) |
| Battery replacement | year 15, at 60% of the original battery cost ($25.2 m) | illustrative (notes s.6/s.8) |
| Brent | $80 central; $60 and $110 in the sensitivity | brief; notes s.4: EIA STEO Oct 2026 as reported, 2026 average $96, 2027 $84 |
| Gasoil crack; island delivery premium | $25/bbl; $0.15/L | illustrative (notes s.8) |
| Diesel specific fuel consumption | 3.9 kWh/L (heat rate 9.3 MJ/kWh, 39% efficiency) | notes s.4: 200-215 g/kWh ≈ 3.8-4.2 kWh/L (vendor guide, tagged [weak]) |
| Diesel non-fuel variable O&M | $0.02/kWh | illustrative (notes s.8) |
| Fuel excise on power diesel | $0/L | brief default (often exempt); illustrative |
| Fiscal capture share θ | 0.5 base; 0 and 1 in the sensitivity | brief; a policy parameter (notes s.8) |
| Diesel CO2 factor | 74.1 kg/GJ, NCV 43.0 GJ/t, density 0.84 kg/L → 2.68 kg/L, 0.686 t/MWh | IPCC 2006 default values from background knowledge, **not verified** in these notes; the density is illustrative |
| Shadow price of carbon | WB low path: $40/t in 2020, growing 2.25% a year (≈$48 in 2028, $82 in 2052); high path is twice that | theory Q7: WB 2024 SPC guidance note (2017 US$; not converted to the model's price base) |
| Social discount rate | 6% | theory Q6: WB 2016 discounting note |
| Government marginal borrowing rate | 8% | illustrative (brief; notes s.8 "assumption, not verified") |
| λ (MCPF) | 1.2 base; 2.0 stress | theory Q1: Auriol and Warlters (2012) Africa average ≈ 1.2; Norway convention 1.2. The stress value follows design brief Step 6 |
| Liquidity λ_t | 2.0 in years 1-7, then 1.2 | illustrative |
| Concessional terms | 1.5%, 30 years, 5 years' grace | brief; notes s.8 (IDA- or RST-type terms; IDA terms not verified; RST is 20 years with 10.5 years' grace) |
| IPP WACC | 11% without guarantee; 8.5% with | brief; notes s.4/s.8: IEA cost-of-capital data, SE Asia solar 8-9.4% vs 5-6.5% in advanced economies; SIDS higher (assumption). The notes assume a 2 pp guarantee effect; the brief uses 2.5 pp |
| PPA term | 25 years | notes s.3: Zambia Scaling Solar tariff fixed for 25 years (ASPIRE: 20 years) |
| Financiers' residence | all non-resident | illustrative |
| LIC-DSF PPP stress | 35% of the PPP capital stock if the stock is above 3% of GDP | notes s.3: LIC-DSF Guidance Note (2017) |
| Discount rate for the PV of new debt | 5% | candidate value, **not verified** (notes s.8 gaps) |

**Derived inputs (Brent $80).**

| Item | Value |
|---|---|
| Energy displaced | 89.9 GWh/yr (30% of diesel generation) |
| Capex: PV / battery / integration / total | $72.0 m / $42.0 m / $6.0 m / **$120.0 m (6.0% of GDP)** |
| Diesel fuel cost / avoided cost (fuel + variable O&M) | $0.208/kWh / **$0.228/kWh** |
| Avoided diesel cost S | **$20.5 m/yr (1.0% of GDP)** |
| Whole-system diesel fuel bill | $62.3 m/yr (3.1% of GDP) |
| Emissions avoided | 61.7 kt CO2/yr (23.0 m litres of diesel) |
| Economic LCOE of the plant, at 6% / 8% | $0.134/kWh / $0.153/kWh |
| Brent at which the financing-neutral ENPV is zero | about $22/bbl |
| Fuel-bill sensitivity | $1.45 m/yr per $10/bbl on the 90 GWh displaced; $4.8 m/yr on the whole 300 GWh |

## 3. Results

### 3.1 Main PSV table (Brent $80, θ = 0.5, $m)

| Route | ENPV_wb | Fin. premium | ENPV | ENPV + CO2 | W | F | MVPF | NB(1.2) | NB(2.0) | NB(liq) | FNPV@8% |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R1a commercial 8%, 7 years | 108 | 9 | 100 | 146 | 131 | 31 | 4.18 | 93 | 68 | 28 | −38 |
| R1b commercial 8%, 25 years | 108 | 24 | 85 | 131 | 131 | 46 | 2.82 | 75 | 38 | 63 | −38 |
| R2 concessional 1.5%, 30 years | 108 | −57 | 165 | 212 | 131 | −34 | pays for itself | 172 | 200 | 197 | +33 |
| R3 PPA, WACC 11% | 108 | 60 | 49 | 95 | 131 | 82 | 1.59 | 32 | −34 | 3 | −69 |
| R4 PPA, WACC 8.5%, guaranteed | 108 | 29 | 80 | 126 | 131 | 51 | 2.55 | 69 | 28 | 51 | −43 |

Notes on the columns:
- The carbon value (PV at 6%) is $47 m on the low SPC path and $93 m on the high path.
- W is the same for every route. At θ = 0.5 it is half the PV of the avoided fuel bill.
- The equivalent annual fiscal cost, F × CRF(6%, 25), is in the CSV: R1a $2.5 m/yr, R1b $3.6 m, R2 −$2.7 m, R3 $6.4 m, R4 $4.0 m.

### 3.2 Debt and liability view

| Route | Headline debt added (% GDP) | Debt after (% GDP) | PV of new debt at 5% (% GDP) | PPA PV at 8% (% GDP) | PPA PV / capex | LIC-DSF PPP stress (% GDP) | Net fiscal liability, PV at 8% ($m) | Net external liability, PV at 8% ($m) | Grant element at 6% |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R1a | 6.0 | 91.0 | 6.7 | 0 | n/a | 0 | 38 | −71 | −7% |
| R1b | 6.0 | 91.0 | 7.9 | 0 | n/a | 0 | 38 | −71 | −20% |
| R2 | 6.0 | 91.0 | 3.6 | 0 | n/a | 0 | −33 | −142 | 48% |
| R3 | 0 | 85.0 | 0 | 8.9 | 1.48 | 2.1 | 69 | −41 | n/a |
| R4 | 0 | 85.0 | 0 | 7.6 | 1.27 | 2.1 | 43 | −66 | n/a |

How to read the two liability columns:
- A negative net external liability means the payments for the plant are smaller, in PV, than the fuel imports it avoids.
- The net fiscal liability equals −FNPV at 8%.

### 3.3 The trap: the annual payment against the fuel bill it replaces (year 1)

| Route | Payment for the plant ($m/yr) | $/kWh | Brent at which the payment equals the avoided cost | Smaller than the fuel bill at $60 / $80 / $110? |
|---|---:|---:|---:|---|
| R1a (debt service $23.0 m + O&M $1.8 m) | 24.8 | 0.276 | $110 | no / no / no (equal at $110) |
| R1b | 13.0 | 0.145 | $29 | yes / yes / yes |
| R2 (interest only in years 1-5; $7.6 m a year from year 6) | 3.6 | 0.040 | any price | yes / yes / yes |
| R3 (PPA tariff) | 16.7 | 0.186 | $54 | yes (barely) / yes / yes |
| R4 (PPA tariff) | 14.2 | 0.159 | $37 | yes / yes / yes |

The fuel bill avoided is $17.6 m, $20.5 m and $24.8 m a year at Brent $60, $80 and $110.

**Net cash flow to the budget or utility, years 1-7 ($m).** Values are the same in each of years 1-7 except R2, whose interest-only period ends after year 5.

| Route | θ = 0.5: years 1-7 | θ = 0.5: worst year (1-30) | θ = 0.5: cumulative payback | θ = 1: years 1-7 | θ = 1: cumulative payback |
|---|---:|---:|---|---:|---|
| R1a | −14.6 a year (−102 over 7 years, 5.1% of GDP) | −16.8 (year 15) | year 23 | −4.4 a year | year 9 |
| R1b | −2.8 a year | −28.0 (year 15) | never | +7.4 | never negative |
| R2 | +6.6 (years 1-5), +2.6 (years 6-7) | −22.6 (year 15) | never negative | +16.9 / +12.9 | never negative |
| R3 | −6.4 a year | −6.4 | never | +3.8 | never negative |
| R4 | −4.0 a year | −4.0 | never | +6.2 | never negative |

Year 15 carries the $25.2 m battery replacement on the public routes. In R2, debt service of $5.8 m a year continues in years 26-30, after the asset is retired.

### 3.4 Switching values

| Route | λ* at which NB = 0 (= MVPF) | θ* at which F = 0 (pays for itself) | Brent* at which the year-1 payment = avoided cost |
|---|---:|---:|---:|
| R1a | 4.18 | 0.62 | $110 |
| R1b | 2.82 | 0.68 | $29 |
| R2 | pays for itself | 0.37 | any price |
| R3 | 1.59 | 0.81 | $54 |
| R4 | 2.55 | 0.70 | $37 |

## 4. Sensitivity (full table in `sids_worked_example_sensitivity.csv`)

**Brent $60 / $80 / $110** (avoided cost $0.196 / $0.228 / $0.276 per kWh; θ = 0.5; $m)

| Route | ENPV | FNPV at 8% | MVPF | NB(1.2) | Year-1 net cash |
|---|---:|---:|---:|---:|---:|
| R1a | 62 / 100 / 155 | −53 / −38 / −15 | 2.25 / 4.18 / 44.9 | 53 / 93 / 154 | −16.1 / −14.6 / −12.4 |
| R1b | 47 / 85 / 140 | −53 / −38 / −15 | 1.73 / 2.82 / 8.54 | 34 / 75 / 136 | −4.3 / −2.8 / −0.6 |
| R2 | 128 / 165 / 221 | 17 / 33 / 56 | pays for itself (all three) | 131 / 172 / 233 | 5.2 / 6.6 / 8.8 |
| R3 | 12 / 49 / 104 | −84 / −69 / −46 | 1.11 / 1.59 / 2.91 | **−9** / 32 / 93 | −7.9 / −6.4 / −4.3 |
| R4 | 43 / 80 / 135 | −58 / −43 / −20 | 1.61 / 2.55 / 6.75 | 29 / 69 / 130 | −5.5 / −4.0 / −1.8 |

**Capex −30% / base / +30%** (O&M and the battery replacement scale with capex)

| Route | ENPV | FNPV at 8% | MVPF | NB(1.2) | Year-1 net cash |
|---|---:|---:|---:|---:|---:|
| R1a | 148 / 100 / 51 | 6 / −38 / −82 | pays for itself / 4.18 / 1.64 | 152 / 93 / 35 | −7.2 / −14.6 / −22.1 |
| R1b | 138 / 85 / 31 | 6 / −38 / −82 | pays for itself / 2.82 / 1.31 | 139 / 75 / 11 | 1.1 / −2.8 / −6.7 |
| R2 | 194 / 165 / 136 | 56 / 33 / 10 | pays for itself (all three) | 207 / 172 / 137 | 7.7 / 6.6 / 5.6 |
| R3 | 113 / 49 / **−15** | −15 / −69 / −122 | 7.14 / 1.59 / **0.89** | 109 / 32 / **−45** | −1.4 / −6.4 / −11.4 |
| R4 | 134 / 80 / 25 | 3 / −43 / −88 | pays for itself / 2.55 / 1.24 | 135 / 69 / 4 | 0.3 / −4.0 / −8.3 |

**IPP WACC** (one PPA route; Brent $80; θ = 0.5)

| WACC | PPA tariff ($/kWh) | Avoided cost ($/kWh) | ENPV | FNPV at 8% | MVPF | NB(1.2) | NB(2.0) | NB(liq) | Year-1 net cash | PPA PV at 8% (% GDP) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 7.0% | 0.143 | 0.228 | 97 | −28 | 3.87 | 90 | 63 | 79 | −2.6 | 6.9 |
| 8.5% | 0.159 | 0.228 | 80 | −43 | 2.55 | 69 | 28 | 51 | −4.0 | 7.6 |
| 11.0% | 0.186 | 0.228 | 49 | −69 | 1.59 | 32 | −34 | 3 | −6.4 | 8.9 |
| 13.0% | 0.208 | 0.228 | 22 | −91 | 1.21 | 1 | −86 | −37 | −8.5 | 10.0 |

At 13% the tariff is above the avoided cost at Brent $60 ($0.196/kWh).

**Commercial loan tenor at 8%**

| Tenor | Year-1 payment ($/kWh) | ENPV | FNPV at 8% | MVPF | NB(1.2) | NB(2.0) | NB(liq) | Year-1 net cash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 7 years | 0.276 | 100 | −38 | 4.18 | 93 | 68 | 28 | −14.6 |
| 15 years | 0.176 | 92 | −38 | 3.37 | 84 | 53 | 59 | −5.6 |
| 25 years | 0.145 | 85 | −38 | 2.82 | 75 | 38 | 63 | −2.8 |

**Fiscal capture θ = 0 / 0.5 / 1** (ENPV is unchanged: R1a 100, R1b 85, R2 165, R3 49, R4 80)

| Route | F | MVPF | NB(1.2) | FNPV at 8% | Year-1 net cash |
|---|---:|---:|---:|---:|---:|
| R1a | 162 / 31 / −100 | 1.61 / 4.18 / pays for itself | 67 / 93 / 119 | −147 / −38 / 71 | −24.8 / −14.6 / −4.4 |
| R1b | 177 / 46 / −85 | 1.48 / 2.82 / pays for itself | 49 / 75 / 101 | −147 / −38 / 71 | −13.0 / −2.8 / 7.4 |
| R2 | 96 / −34 / −165 | 2.71 / pays for itself / pays for itself | 146 / 172 / 198 | −76 / 33 / 142 | −3.6 / 6.6 / 16.9 |
| R3 | 213 / 82 / −49 | 1.23 / 1.59 / pays for itself | 6 / 32 / 58 | −178 / −69 / 41 | −16.7 / −6.4 / 3.8 |
| R4 | 182 / 51 / −80 | 1.44 / 2.55 / pays for itself | 43 / 69 / 95 | −152 / −43 / 66 | −14.2 / −4.0 / 6.2 |

F at θ = 0 and θ = 1 follows from F(θ) = F(0.5) − (θ − 0.5) × PV(S), with PV(S) = $262 m at 6%.

## 5. Interpretation

- **The trap is a liquidity and debt-statistics problem, not a solvency problem.**
  - The asset is very good economically. Its financing-neutral ENPV is +$108 m at 6%. Its LCOE of $0.134/kWh is far below the $0.228/kWh diesel cost it avoids, and the ENPV stays positive down to Brent of about $22/bbl.
  - With the only loan on offer (8%, 7 years), debt service plus O&M is $24.8 m a year, against a $20.5 m fuel saving. Even if the public sector kept every dollar saved (θ = 1), it would run a deficit of $4.4 m a year for seven years. Break-even needs Brent at $110.
  - Headline debt jumps by 6% of GDP on day one (85% → 91%), whatever the tenor. Debt statistics score the gross liability, not the self-financing asset behind it.
  - These are three different constraints: liquidity (tenor), solvency (FNPV) and the DSA (stock). They need different fixes.
- **Tenor is not price.**
  - At the government's own 8% rate, the 7-year and 25-year loans have the same FNPV (−$38 m): stretching the tenor does not change solvency.
  - At the 6% social rate, the longer loan costs more, because the island pays the 2-point spread for longer (financing premium $24 m against $9 m). So with a constant λ, R1a beats R1b: NB(1.2) is 93 against 75.
  - Only when λ is higher in the cash-constrained years does the ranking flip: NB(liq) is 28 for R1a and 63 for R1b.
  - Lesson for the tool: one constant λ cannot see the trap. It needs a time-varying λ, or an explicit liquidity constraint, next to NB_λ.
- **Concessional finance wins on every metric, where it is available.** R2 has:
  - a grant element of 48% at 6%;
  - a financing premium of −$57 m, which lifts the island ENPV to $165 m;
  - a positive net cash flow from year 1;
  - an FNPV of +$33 m at 8%.

  It pays for itself even at θ = 0.5; the threshold is θ* = 0.37. It still adds 6% of GDP to headline debt, though only 3.6% in PV terms at a 5% rate (a candidate value). IDA, RST and swap volumes are small relative to need (notes s.4).
- **A PPA does turn capex into an annual payment smaller than the fuel bill, at moderate WACC.**
  - The tariff is $0.186/kWh at 11% and $0.159/kWh at 8.5% with a guarantee, against an avoided cost of $0.228. That is $16.7 m and $14.2 m a year against $20.5 m.
  - The payment stays below the fuel bill down to Brent of $54 and $37.
  - At 13% WACC the tariff is $0.208: still below the avoided cost at $80, but above it at $60.
- **When the PPA is a good deal, and when it is hidden debt.**
  - The guaranteed PPA (R4) costs only about $5 m more in PV than sovereign borrowing at 8% (FNPV −$43 m against −$38 m). It adds no headline debt, ring-fences O&M, and has positive net cash from year 1 when θ = 1. That is a good deal.
  - The unguaranteed PPA (R3) costs about $31 m more. It halves the island ENPV (49 against 100), and its MVPF is only 1.59. It fails at λ = 2.0 (NB −34), at Brent $60 (NB(1.2) −9) and at capex +30% (ENPV −15, MVPF 0.89).
  - In both cases the PV of the take-or-pay stream at 8% (8.9% and 7.6% of GDP, or 1.48 and 1.27 times capex) is larger than the 6%-of-GDP debt it keeps off the headline. The LIC-DSF stress adds 2.1% of GDP to PPG debt anyway.
  - The PPA moves the liability off the headline measure; it does not remove it.
- **Net of savings, every route reduces the island's external liabilities.** Payments are below the PV of the fuel imports avoided (net external liability −$41 m for R3 to −$142 m for R2). The fiscal picture depends on who keeps the savings: the net fiscal liability is $69 m for R3 and $43 m for R4 at θ = 0.5. This is the case for DSA credit "net of savings" (brief s.5, radical upgrades), but only where θ is contractually or institutionally secured.
- **Fiscal capture (the revenue return) drives MVPF but not ENPV.**
  - θ moves value one-for-one between consumers (W) and the budget (F), so ENPV does not change.
  - NB_λ rises by (λ − 1) × PV of the extra savings captured: about $26 m for every route when θ moves from 0 to 0.5 at λ = 1.2.
  - For R1a, MVPF goes from 1.61 at θ = 0, to 4.18 at θ = 0.5, to "pays for itself" at θ = 1.
  - At θ = 0 the plant is in effect a budget-financed consumer subsidy. Above θ* it is a self-financing asset: 0.37 for R2, and 0.62-0.81 for the other routes.
  - Tariff design is therefore a fiscal lever worth λ − 1 per dollar: keep part of the fuel saving in the utility rather than passing it all through at once.
- **λ changes the go/no-go decision more than the ranking.**
  - The switching λ* equals the MVPF: 1.59 (R3), 2.55 (R4), 2.82 (R1b), 4.18 (R1a).
  - At λ = 2.0, a country that cannot raise more debt, only the unguaranteed PPA fails.
  - The ranking at constant λ is R2 > R1a > R1b > R4 > R3. Among the routes actually available (R1a, R3, R4, plus R2 if granted), adding the liquidity premium (NB(liq)) moves the guaranteed PPA ahead of the short-tenor loan.
- **Carbon and oil price.**
  - Carbon at the WB shadow price adds $47 m (low path) to $93 m (high path) of PV to every route. It does not reorder the routes, because they all displace the same diesel. It does rescue the marginal cases.
  - Each $10/bbl moves the avoided fuel bill by $1.45 m a year, about $18.5 m in PV. The plant swaps about 30% of the island's oil-price exposure for a fixed payment: a hedge the metrics above do not value.

## 6. Caveats

- **Constant prices, nominal rates.** The 8%, 1.5% and 11% rates come from nominal sources but are applied to constant-price flows. This overstates financing costs, most for the long-tenor and PPA routes. A full model should use nominal flows with a US$ deflator. The SPC is in 2017 US$ and is not inflated to the model's price base, so the carbon value is understated.
- **Who pays the plant cost.** θ applies only to the fuel savings; the plant cost falls wholly on the public sector, because base tariffs are not raised. With full cost-reflective pass-through the budget would see neither the cost nor the saving.
- **PPA liability is an upper bound.** The PPA is treated as take-or-pay on expected output. Many solar PPAs are "take-and-pay" with deemed energy (notes s.3).
- **Guarantee not priced.** There is no guarantee fee and no expected call. A WB or IDA guarantee is backed by a sovereign indemnity, so the exposure is shared and priced, not removed (notes s.3).
- **Benefits left out:**
  - FX shadow price;
  - hedge value;
  - local air pollution;
  - avoided diesel capacity (the gensets stay as back-up);
  - PV degradation;
  - demand growth;
  - curtailment risk;
  - grid-integration costs beyond the 5% integration line.
- **No delivery haircuts (Step 3).** No PIMA or PEFA efficiency haircut, execution delay or optimism bias is applied. In a low-capacity setting a cost uplift on the public routes (and not on a competitively auctioned IPP) would narrow R1 and R2's lead.
- **Unverified inputs.**
  - Island-specific PV and battery capex: the $1,200/kW is inferred from ASPIRE tariffs, and $350/kWh is an assumption.
  - GDP, debt, the 8% sovereign rate and the IDA terms.
  - The 5% PV-of-debt rate.
  - The IPCC emission factor (background knowledge, not in the notes).
- **DSA rules.** The 35% PPP stress applies under the 2018 LIC-DSF. A SIDS assessed under the MAC-DSF faces different rules, and the 2026 LIC-DSF review (roll-out 2027) may change the treatment.
- **Timing simplifications.** Capex and loan disbursement both fall in year 0, with no construction lag or interest during construction. Concessional debt service continues in years 26-30, after the asset is retired. Growth-induced tax revenue is left to the macro model (design brief, Step 5).
