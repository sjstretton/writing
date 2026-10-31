# Internal context: how CDPM/CPM (formerly SISEPUEDE) does CBA today, and the CPAT-CPM macro-fiscal bridge

Conventions used in these notes:
- Relative link paths are relative to `/home/user/CPAT-CDPM/`. Absolute paths (`/home/user/CPAT-AI/...`) are in the CPAT repo. Paths are wrapped in `<...>` because they contain spaces.
- **Facts from files** carry a file link. **Facts from public web pages** carry a URL. **Inferences** are only in the "Inferences" subsections.
- Web access was limited. The web-search budget for this session was already used up. `sisepuede.readthedocs.io`, `costs-benefits-ssp.readthedocs.io` and `imf.org` did not resolve from this sandbox. Only GitHub pages could be fetched, so the public-documentation evidence is thinner than planned.
- Helper scripts and text extracts are in `/tmp/claude-0/-home-user/10f05c0e-3ad4-522f-ac5a-3e36970d0c23/scratchpad/` (`txt/`, `cba*.py`, `xl*.py`, `omml.py`, `msg.py`).

**The main correction for the proposal.** The brief assumed that "CPM" or "CPAT-CPM" is a combined IMF-style macro-fiscal tool (GIMF/DIGNAD/DIGNAR). The internal documents do not support this.
- In every internal file, **CPM is the renamed SISEPUEDE**, the physical pathways (quantity) model. The **CPAT-CPM bridge** links CPAT (the World Bank–IMF price and fiscal tool) to that model.
- **GIMF, DIGNAD and DIGNAR appear nowhere** in either repository (details in Q4).
- The macro-fiscal machinery that does exist internally has four parts:
  1. CPAT's GDP effects, driven by MFMod-median fiscal multipliers for each use of revenue.
  2. A planned simple debt-dynamics equation fed by IMF WEO projections.
  3. A Tax and Macro-Fiscal indicator dashboard.
  4. Planned links to MFMod, MANAGE and MINDSET.

---

## Q1. What is CDPM/CPM (is it the renamed SISEPUEDE? who maintains it?), and what are its sectors, transformations/strategies and outputs?

### Takeaway
CPM is SISEPUEDE under a new name. Inside the Bank it is called "CPT/CPM". The one place "CDPM" appears is a single slide that uses it for the same pathways engine. The model is maintained by James Syme and Edmundo Molina-Pérez's team at Tec de Monterrey (Escuela de Gobierno y Transformación Pública). It covers all IPCC sectors in about 15–16 subsectors. It runs named "transformations", which are bundled into "strategies", against a baseline, solves the power sector with NemoMod, and prices the differences with a separate cost–benefit package (`costs_benefits_ssp`).

### Cited Findings
**Identity and naming**
- "CPM (formerly SiSePuede) is a quantity model: it has no prices, but it represents a country's full greenhouse gas inventory, a library of policy transformations such as heat pumps or leak repair, and a cost–benefit module that prices them." — [CPAT_CPM_Methodology_v0925.docx §1.1](<MainProjectFolder/2. Other Documentation/CPAT_CPM_Methodology_v0925.docx>)
- "CPM (formerly SiSePuede; referred to as CPT/CPM within the Bank)". A work programme with David Groves is "consolidating CPAT, CPM (formerly SiSePuede), MANAGE and MINDSET into a single country policy analysis tool, first applied in Libya, Egypt and Morocco". — [FY27 Work Plan (CPM comments version), Section B](<MainProjectFolder/2. Other Documentation/Stephen_FY27_Work_Plan - Coded CPAT - and CPAT-CPM Elements_CPM_comments.docx>); same wording in [Stephen_FY27_Work_Plan_v2.6_15thOct.docx](</home/user/CPAT-AI/Presentations - Overarching/Stephen_FY27_Work_Plan_v2.6_15thOct.docx>)
- "CDPM" appears once, on the slide "Typology of Key Impacts" (a later copy titles it "Economic Impacts"): "Transformations — Subsidies can pay some of the Marginal Costs of private abatement — **In CDPM.**" The expansion of the acronym is not given. — [Slides_Oct-19th-WBside-Pathways_CPAT_proposal.pptx, slide 3](<CPAT Excel - UI and Working Version/Slides_Oct-19th-WBside-Pathways_CPAT_proposal.pptx>); [Pathways_CPAT_proposal.pptx, slide 3](<MainProjectFolder/1. Project Presentations/Pathways_CPAT_proposal.pptx>)
- The partnership's software is the "Pathways Toolkit": "adapting and extending SISEPUEDE, a sector-based low-emissions pathways model, into software called the 'Pathways Toolkit'". It covers carbon markets (Article 6 tool), "Carbon Pricing & Fiscal – CPAT (two-way CPAT-Sisepuede integration)" and "Jobs - MINDSET 1.0 and MANAGE". — [Partnership_Agreement-Tec de Monterrey-Feb2026.docx](<MainProjectFolder/9. CPAT-LTS Project/Core Document and Example Data/More Project Documents/Partnership_Agreement-Tec de Monterrey-Feb2026.docx>)
- One Egypt deck expands the name as "Sectoral Pathways & Uncertainty Exploration for Decarbonization — physical pathways, AFOLU/IPPU/Waste/Energy, DMDU sampling". — [2.Egypt_CPAT_SISEPUEDE_Integration_How.pptx, slide 1](<MainProjectFolder/1. Project Presentations/2.Egypt_CPAT_SISEPUEDE_Integration_How.pptx>)

**Who maintains it**
- The Uganda runs were sent by James Coburn Syme (jsyme@tec.mx) to Stephen Stretton. — [Latest SISEPUEDE Runs.msg](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/Latest SISEPUEDE Runs.msg>)
- Several slides refer to the counterpart lead: "Final coded CPAT to Edmundo"; "The build behind it can use more than one implementation flow. That is Edmundo's call." — [Pathways_CPAT_proposal.pptx, slides 2, 5](<MainProjectFolder/1. Project Presentations/Pathways_CPAT_proposal.pptx>)
- The contract is a US$215,000 partnership with the Escuela de Gobierno y Transformación Pública (Tec de Monterrey). Selected line items:
  - A1.4 "CPAT Integration" $20,000
  - A1.5 "Fiscal Analyses" $20,000
  - A1.6 "Macro and Investment analyses" TBC

  — [Partnership_Agreement-Tec de Monterrey-Feb2026.docx](<MainProjectFolder/9. CPAT-LTS Project/Core Document and Example Data/More Project Documents/Partnership_Agreement-Tec de Monterrey-Feb2026.docx>)
- The public GitHub repository is `jcsyme/sisepuede`, licensed Apache-2.0 / GPL-3.0. — [github.com/jcsyme/sisepuede](https://github.com/jcsyme/sisepuede)
- The cost–benefit package is a separate repository, `milocortes/costs_benefits_ssp` (GPL-3.0), "part of the SISEPUEDE decarbonization toolbox". — [github.com/milocortes/costs_benefits_ssp](https://github.com/milocortes/costs_benefits_ssp)
- An internal review describes SISEPUEDE as "The most complete open model … (RAND and IDB)". It has been applied to 18 LAC countries, plus Mexico, Peru, Oaxaca, Uganda, Morocco and Libya. — [Global_Investment_Needs_SISEPUEDE.docx, Exec. summary](<MethodologyReview/Global_Investment_Needs_SISEPUEDE.docx>)

**Structure and sectors**
- Model structure: "SISEPUEDE represents an economy as a set of sector models … Each is driven by population and GDP. Users define transformations … combined into strategies … calibrated to historical emissions (Climate Watch) … genetic algorithm and particle swarm optimisation … about a thousand futures drawn by Latin Hypercube sampling … Energy production is optimised by NemoMod … The cost-benefit module (costs_benefits_ssp) then converts physical differences between each strategy and the baseline into money." — [Global_Investment_Needs_SISEPUEDE.docx, App. A.1](<MethodologyReview/Global_Investment_Needs_SISEPUEDE.docx>)
- The Uganda output lists 15 emission subsectors as `emission_co2e_subsector_total_{agrc, ccsq, entc, fgtv, frst, inen, ippu, lndu, lsmm, lvst, scoe, soil, trns, trww, waso}`. — [sisepuede_ide_run_2025-10-29T19;49;25.722413.csv](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413/sisepuede_ide_run_2025-10-29T19;49;25.722413.csv>)
- The CBA file additionally uses `pflo` (cross-cutting diets and industrial CCS) and `wali` (liquid waste and sanitation). — [cba_results.csv](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413/cba_results.csv>)
- The bridge deck describes CPM as:
  - "A full inventory — fifteen subsectors"
  - "A transformation library — named policies with a single magnitude each, stackable into strategies"
  - "A power system — least-cost dispatch and capacity expansion"
  - "A cost–benefit module — technical cost, system cost and externalities per lever"
  - "Runs to 2050 — no prices inside it"
  - CPM input files have "2,638 columns of activity, technology and cost"

  — [CPAT_CPM_bridge_map.pptx, slides 3–4](<MainProjectFolder/1. Project Presentations/CPAT_CPM_bridge_map.pptx>)
- Demand is income-driven only: "Prices play no part"; "Demand does not respond to price. Prices enter only the power-supply optimization and the economic module." — [Activity_levels_SISEPUEDE_CPAT_CBAM_FTT (1).docx, App. D/E](<MethodologyReview/Activity_levels_SISEPUEDE_CPAT_CBAM_FTT (1).docx>)
- GDP is exogenous: Uganda "GDP is exogenously specified … (2019 USD PPP)". The bridge measures CPM GDP in PPP dollars, "3.6 times CPAT's market dollars" for Egypt. — [SiSEPUEDE_analysis-Uganda v2025_10_16.docx](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413/SiSEPUEDE_analysis-Uganda v2025_10_16.docx>); [CPAT_CPM_Methodology_v0925.docx §2.2](<MainProjectFolder/2. Other Documentation/CPAT_CPM_Methodology_v0925.docx>)

**Transformations and strategies (from `ATTRIBUTE_STRATEGY.csv`)**
- Strategy IDs and their "singleton" transformations, each coded `TX:<SECTOR>:<ACTION>`:
  - 0 = `BASE`
  - 1000–1019: AFOLU, e.g. `AGRC:DEC_CH4_RICE`, `LNDU:DEC_DEFORESTATION`, `LVST:DEC_ENTERIC_FERMENTATION`; composite `AF:ALL`
  - 2000–2012: circular economy, e.g. `TRWW:INC_CAPTURE_BIOGAS`, `WALI:INC_TREATMENT_URBAN`, `WASO:INC_RECYCLING`; composite `CE:ALL`
  - 3000–3024: energy, e.g. `ENTC:TARGET_RENEWABLE_ELEC` ("95% of electricity is generated by renewables in 2050"), `ENTC:LEAST_COST_SOLUTION`, `FGTV:DEC_LEAKS`, `INEN:SHIFT_FUEL_HEAT`, `SCOE:SHIFT_FUEL_HEAT`, `TRNS:SHIFT_FUEL_LIGHT_DUTY`, `TRNS:SHIFT_MODE_PASSENGER`; composite `EN:ALL`
  - 4000–4006: IPPU, e.g. `IPPU:DEC_CLINKER`, `IPPU:DEC_HFCS`; composite `IP:ALL`
  - 6000–6001: `PFLO:INC_HEALTHIER_DIETS`, `PFLO:INC_IND_CCS`
  - Named strategies: 6002 `PFLO:ALL` ("All Actions"), 6003 `PFLO:NDC`, 6004 `PFLO:NZ` (Net Zero), 6005 `PFLO:BAU`, 6006 `PFLO:ASP`, 6007–6009 NDC 2.0 variants.

  — [ATTRIBUTE_STRATEGY.csv](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413/ATTRIBUTE_STRATEGY.csv>)
- The Egypt Low-Emissions Pathway used "51 transformations" (AFOLU 14, Energy 22, IPPU 7, Circular Economy 11). Emissions: BAU 2050 138.9 MtCO2e; LEP 2050 52.9 (−62%). "What's missing: the Egypt run produces emissions and capital costs but does not price the carbon tax revenue, fossil-subsidy savings, or distributional impact." — [2.Egypt_CPAT_SISEPUEDE_Integration_How.pptx, slide 2](<MainProjectFolder/1. Project Presentations/2.Egypt_CPAT_SISEPUEDE_Integration_How.pptx>)

**Outputs**
- Per James Syme's email:
  - `sisepuede_run_…csv` holds "primary inputs and outputs … including emissions and drivers".
  - `cba_results.csv` holds "cost benefit results for each non-baseline run".
  - Tables are indexed by `time_period` and `primary_id`. "time_period = 0 is 2015 … add 2015 to get the year".
  - `primary_id` 0 = baseline; 70070 = strategy 6004 (net zero / "HBLE (high benefits, low emission)"); 74074 = 6008 (NDC2 from 2020); 75075 = 6009 (NDC2 from 2025).

  — [Latest SISEPUEDE Runs.msg](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/Latest SISEPUEDE Runs.msg>)

### Inferences
- "CDPM" is most likely an informal variant name for the same pathways engine (CPM/SISEPUEDE plus its cost module). The slide context ("Subsidies can pay some of the Marginal Costs of private abatement — In CDPM") refers to CPM's cost module. The repository name `CPAT-CDPM` suggests the same. The expansion (perhaps "Country Development/Decarbonization Pathways Model") is a guess.
- "CPT/CPM" probably stands for "Country Pathways Tool/Model", consistent with "Country Pathways Tool" in the FY27 Objective 2 title. This is also inferred, not stated.

### Gaps
- No document defines "CDPM" or "CPM" as acronyms.
- The public SISEPUEDE documentation could not be fetched (readthedocs did not resolve). Read it directly for the official sector and transformation lists ([sisepuede.readthedocs.io](https://sisepuede.readthedocs.io/en/latest/), linked from `MainProjectFolder/6. SiSePuede Documentation and Repo/*.url`).

---

## Q2. Exactly how does CDPM/SISEPUEDE's CBA work (categories, discounting, base year, carbon, who pays, fiscal flows, capital vs recurrent, financing cost)?

### Takeaway
The cost–benefit module computes, for each item, the difference between a strategy and the baseline, times a unit factor, times an annual-change factor. It returns **undiscounted annual flows** in what appear to be 2019 US dollars (a LAC-average basis). Results come by strategy, sector, item and year. Discounting is applied afterwards: 7% in the LAC study, 5% for Costa Rica. Power capex and opex, however, arrive **pre-discounted** from NemoMod. There is **no public/private (or household/firm/state) split, no fiscal flows (taxes, subsidies, revenues), no separate gross-capex line, no cost of capital or financing cost, and no macro feedback.** Carbon is not valued in the headline (the waste appendix does value it).

### Cited Findings
**Core equation and variants**
- Core equation (A1): `V_{k,t} = (x^S_{k,t} − x^B_{k,t}) · m_k · g_k^{max(0, t−8)}`, where:
  - `x` is the driving physical variable (strategy S vs baseline B);
  - `m_k` is the unit cost factor "in 2019 US dollars";
  - `g_k` is an annual change in the factor;
  - "Period 0 is 2015, so the factor starts changing from 2023".

  — [Global_Investment_Needs_SISEPUEDE.docx, App. A.1 (equations extracted from OMML)](<MethodologyReview/Global_Investment_Needs_SISEPUEDE.docx>)
- The source code confirms it: `difference_value` = strategy − baseline; `value = difference_value * cb_orm.multiplier * cb_orm.annual_change ** time_period_for_multiplier_change`, with the exponent `np.maximum(0, time_period − SSP_GLOBAL_TIME_PERIOD_2023)` ("Assume cost change only begins in 2023"). **The code contains no discount rate or discount factor.** — [cb_calculate.py](https://raw.githubusercontent.com/milocortes/costs_benefits_ssp/main/costs_benefits_ssp/cb_calculate.py)
- Variants:
  - `scale_variable`: no baseline subtraction; the cost is proportional to a level.
  - `fraction_change`: `fraction_change = tx_frac/ba_frac`, `difference_value = effect_value*(1−fraction_change)`.
  - System cost: rows where `cost_type == "system_cost"`.
  - Technical cost: from the `TransformationCost` table for the transformations in the strategy.

  — [cb_calculate.py](https://raw.githubusercontent.com/milocortes/costs_benefits_ssp/main/costs_benefits_ssp/cb_calculate.py); [Global_Investment_Needs_SISEPUEDE.docx, A.1](<MethodologyReview/Global_Investment_Needs_SISEPUEDE.docx>)

**Post-processing**
- `cb_process_interactions`:
  - It "rescales overlapping transformations so that, for example, efficiency savings are not counted twice".
  - In code, each transformation's mean `relative_effect` is normalised so the scalars sum to 1. That scalar multiplies `value`, `difference_value`, `variable_value_baseline` and `variable_value_pathway`.

  — [cb_calculate.py](https://raw.githubusercontent.com/milocortes/costs_benefits_ssp/main/costs_benefits_ssp/cb_calculate.py); [Global_Investment_Needs_SISEPUEDE.docx](<MethodologyReview/Global_Investment_Needs_SISEPUEDE.docx>)
- `cb_shift_costs`:
  - Rows before `SSP_GLOBAL_TIME_PERIOD_TX_START` are copied with `_shifted<year>` appended to `variable`.
  - They are moved forward by `SSP_GLOBAL_TIME_PERIOD_TX_START`, and the originals' `value` is set to 0.
  - The README comment: "SHIFT any stray costs incurred from 2015 to 2025 to 2025 and 2035."

  — [cb_calculate.py](https://raw.githubusercontent.com/milocortes/costs_benefits_ssp/main/costs_benefits_ssp/cb_calculate.py); [costs_benefits_ssp README](https://github.com/milocortes/costs_benefits_ssp)
- Category families:
  - "Technical: costs or benefits that actors in a sector usually experience and that are largely internal to markets".
  - "Non-technical: costs or benefits tied to development goals" (crashes, air pollution, biodiversity, congestion time).

  — [costs_benefits_ssp README](https://github.com/milocortes/costs_benefits_ssp)
- The package writes `cba_resultados.csv`; Uganda's file is `cba_results.csv`. — [costs_benefits_ssp README](https://github.com/milocortes/costs_benefits_ssp)

**Discounting**
- "The module itself never discounts. It returns undiscounted annual flows … The present value is computed afterwards." The present value is `PV = Σ_{t=2025}^{2050} Σ_k V_{k,t}/(1+r)^{t−t0}` (A2), with r = 7% in the LAC study (Kalra et al. 2023), called a "higher bound". Costa Rica (Groves et al. 2020) used 5%. — [Global_Investment_Needs_SISEPUEDE.docx, A.1 and Table A1](<MethodologyReview/Global_Investment_Needs_SISEPUEDE.docx>)
- Power sector inconsistency:
  - NemoMod reports `vdiscountedcapitalinvestment` and `vdiscountedoperatingcost`, stored as `nemomod_entc_discounted_capital_investment_*` and `nemomod_entc_discounted_operating_costs_*`. "The cost-benefit database maps power capex and opex directly onto these discounted series."
  - The documented NemoMod default rate is 5% (`attributes/analytical_parameters.csv`), but the shipped `sisepuede.config` sets `discount_rate: 0.0`.
  - So power capex is either discounted twice or once, depending on the rate; other lines are undiscounted.

  — [Global_Investment_Needs_SISEPUEDE.docx, A.1 "Power-sector capital"](<MethodologyReview/Global_Investment_Needs_SISEPUEDE.docx>)
- The Uganda CBA confirms the mapping: `cb:entc:technical_cost:electricity:capex` ← `nemomod_entc_discounted_capital_investment_pp_wind`; `cb:entc:technical_cost:electricity:opex` ← `nemomod_entc_discounted_operating_costs_pp_wind`. — [cba_results.csv](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413/cba_results.csv>)

**Cost of capital and annualisation**
- "`InterestRateTechnology` and `InterestRateStorage` … are stubbed in SISEPUEDE (their formatters return nothing). Depreciation defaults to the sinking-fund method. So there is no way to give a solar farm in Zambia a higher cost of capital than one in Chile." — [Global_Investment_Needs_SISEPUEDE.docx, A.1](<MethodologyReview/Global_Investment_Needs_SISEPUEDE.docx>)
- Capital is annualised inconsistently:
  - The EV premium (USD 12,000 + 1,000 charging) is divided by 15,000 km/yr over 12 years, giving USD 0.039/vkm. This is straight-line, i.e. a 0% interest rate.
  - Several building and industry factors are "levelised costs as presented" with "no discount rate … documented".
  - N2O abatement costs from EPA are undiscounted.

  — [Global_Investment_Needs_SISEPUEDE.docx, A.1 and Table A1](<MethodologyReview/Global_Investment_Needs_SISEPUEDE.docx>)
- Technical costs "mix capital, operations and avoided costs"; the "investment" line is "closer to a net incremental cost". "Gross capital output: No, technical costs mix capital and operations." — [Global_Investment_Needs_SISEPUEDE.docx, §"Why the investment-needs number differs" and step table](<MethodologyReview/Global_Investment_Needs_SISEPUEDE.docx>)
- "Mode shift (freight and passenger) carries no technical cost, because the infrastructure is 'deeply uncertain, highly localized, and beyond this study's scope'". — [Global_Investment_Needs_SISEPUEDE.docx, A.1](<MethodologyReview/Global_Investment_Needs_SISEPUEDE.docx>)

**Cost and benefit factors (Table A1 / A.6, 2019 USD, LAC average)**
- Technical cost factors:
  - New transmission USD 2.70/MWh (NREL)
  - EV LDV USD 0.039/vkm capital, −0.012/vkm maintenance
  - Electric trucks/buses USD 0.042/vkm + 0.011/kWh
  - Rail electrification USD 0.0013 per tkm or pkm
  - Maritime fuel switch USD 0.0005/tkm
  - Fugitive leaks USD 20/tCO2e; flaring USD 2/tCO2e
  - CCS cement/steel/chemicals USD 40/50/100 per tCO2
  - Reforestation USD 45/ha/yr
- Benefit factors:
  - Diet health USD 1,750 per person shifting
  - Air pollution coal/gas USD 2.77/0.99 per GJ (IMF, Parry et al. 2014)
  - Transport pollution diesel/gasoline USD 0.31/0.039 per litre
  - Crashes and congestion: IMF per-vkm values
- "Currency | 2019 USD, LAC average | costs_benefits_ssp docs".
- "The full set is in the docs/cost_factors folder of the costs_benefits_ssp repository. It has 21 tables."

— [Global_Investment_Needs_SISEPUEDE.docx, Table A1, A.6](<MethodologyReview/Global_Investment_Needs_SISEPUEDE.docx>)

**Carbon valuation**
- "The study excludes the social cost of carbon from the headline benefits … The waste-sector appendix nonetheless values avoided emissions at the social cost of carbon, an inconsistency." — [Global_Investment_Needs_SISEPUEDE.docx, A.2](<MethodologyReview/Global_Investment_Needs_SISEPUEDE.docx>)

**No public/private split, no fiscal flows, no macro feedback**
- From the bridge deck: "The cost module prices the resource cost of a transformation, not who disburses it. A heat pump is bought by a household, an electric railway by the state, a furnace by a firm. Splitting each lever's cost between state, household and firm is what this mapping needs and what neither model holds today." — [CPAT_CPM_bridge_map.pptx, slide 12](<MainProjectFolder/1. Project Presentations/CPAT_CPM_bridge_map.pptx>)
- Gaps listed in the internal review: "It reports no gross capital requirement … Its discount rate is ad hoc … It has no country cost of capital and no financing module (who pays, public or private, domestic or external). It has no macro feedback." On jobs: "Investment does not raise growth, prices do not adjust, and financing does not crowd anything out." — [Global_Investment_Needs_SISEPUEDE.docx, App. B and A.1 "Jobs and the wider economy"](<MethodologyReview/Global_Investment_Needs_SISEPUEDE.docx>)
- The Uganda wide output (4,054 columns) contains no column matching `price`, `revenue`, `tax` or `subsid`. It does contain:
  - `totalvalue_enfu_fuel_consumed_*` (fuel value, 51 "value" columns)
  - `nemomod_*_discounted_capital_investment_*` (48)
  - `nemomod_*_discounted_operating_costs_*`
  - `gdp_mmm_usd`, `gdp_per_capita_usd`

  — [sisepuede_ide_run_2025-10-29T19;49;25.722413.csv](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413/sisepuede_ide_run_2025-10-29T19;49;25.722413.csv>)
- SISEPUEDE has fuel price input fields, but they serve only NemoMod and costing: `cost_enfu_fuel_natural_gas_usd_per_mmbtu`, `cost_enfu_fuel_diesel_usd_per_m3`, `nemomod_entc_capital_cost_pp_solar_mm_usd_per_gw`, `nemomod_entc_fixed_cost_*`. — [2.Egypt_CPAT_SISEPUEDE_Integration_How.pptx](<MainProjectFolder/1. Project Presentations/2.Egypt_CPAT_SISEPUEDE_Integration_How.pptx>)
- Measured: "a carbon price moved CPM's generation mix by 0.000 pp through three independent routes". — [CPAT_CPM_bridge_map.pptx, slide 3](<MainProjectFolder/1. Project Presentations/CPAT_CPM_bridge_map.pptx>)

**Uncertainty and results**
- About 1,000 futures by Latin Hypercube; PRIM scenario discovery. "The discount rate and the cost of capital, though, are not among the uncertain inputs." — [Global_Investment_Needs_SISEPUEDE.docx, A.1](<MethodologyReview/Global_Investment_Needs_SISEPUEDE.docx>)
- LAC study headline (PV 2025–2050, 2019 USD, 7%):
  - Technical costs USD 1.3 trillion (≈2% of GDP a year)
  - Fuel savings 0.9 trillion
  - Avoided air pollution 0.5 trillion
  - Health/safety/productivity 1.0 trillion
  - Total net benefit 2.7 trillion
  - "Net benefit, financial flows only" 0.7 trillion

  — [Global_Investment_Needs_SISEPUEDE.docx, Table A2](<MethodologyReview/Global_Investment_Needs_SISEPUEDE.docx>)

**Recommendations already drafted internally (A.4/A.5)**
- Dual discount rate: social rate 6% plus country/technology WACC.
- Fix NemoMod double discounting.
- Implement `InterestRateTechnology`.
- Use capital recovery factors (CRFs) instead of straight-line charges.
- Report gross capex separately.
- Add mode-shift infrastructure.
- Localise unit costs.
- "Add a financing layer: split investment into public and private, domestic and external, and link it to a debt module (… MFMod)".
- Separate carbon line.
- Put the discount rate into the futures.

— [Global_Investment_Needs_SISEPUEDE.docx, A.4–A.5](<MethodologyReview/Global_Investment_Needs_SISEPUEDE.docx>)

### Inferences
- Because the module never discounts and has no financing or ownership dimension, every flow in the CBA is an **economic resource-cost (or benefit) flow attributed to the economy as a whole**. A fiscal or allocative-efficiency layer therefore has to supply, outside the module:
  - a payer split
  - a capex/opex split
  - a financing/discounting convention
  - the conversion from resource cost to budget outlay (taxes, subsidies, transfers)
- The `entc` capex rows are already discounted at NemoMod's internal rate, which is unknown for Uganda. Any new layer should read NemoMod's undiscounted capacity additions × capital cost, or re-derive capex, rather than discount `cb:entc:technical_cost:electricity:capex` again.

### Gaps
- The NemoMod discount rate used in the Uganda run (0% vs 5%) is not recorded in the files.
- The `SSP_GLOBAL_COLNAMES_OF_RESULTS` definition (`cb_config`) and the 21 cost-factor tables were not retrieved.
- Whether the unit-factor base year is still 2019 USD for Uganda and MENA, rather than LAC-specific, is not stated in the Uganda files.

---

## Q3. What does a real CBA output look like (Uganda run, 2025-10-29): columns, categories, units, years and magnitudes?

### Takeaway
`cba_results.csv` is a long table of **annual, undiscounted** values:
- 37,540 rows.
- 3 strategies × 1 future × 1 region, years 2019–2070.
- 1,065 distinct items named `cb:<sector>:<category>:<subcategory>:<detail>`.

Sign convention: **negative = cost, positive = benefit**. Technical costs are about US$197–259 bn undiscounted over 2025–2050 (about 1–4% of PPP GDP a year). Non-technical co-benefits are larger. Health, sanitation and water-pollution benefits from wastewater and sanitation transformations dominate.

### Cited Findings
**File structure**
- Columns: `strategy_code, future_id, region, time_period, difference_variable, variable_value_baseline, variable_value_pathway, difference_value, variable, value`.
- Strategies: `PFLO:NZ`, `PFLO:NDC_2_2020_TUNED`, `PFLO:NDC_2_2025_TUNED`; `future_id` 0; region `uganda`.
- `time_period` runs 4–55, i.e. 2019–2070. — [cba_results.csv](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413/cba_results.csv>) (analysed with pandas, script `cba*.py`); year mapping from [Latest SISEPUEDE Runs.msg](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/Latest SISEPUEDE Runs.msg>)
- 18 category slugs (third field of `variable`), with the number of distinct items in each:

  | Category | Items |
  |---|---|
  | `technical_cost` | 455 |
  | `air_pollution` | 91 |
  | `crop_value` | 91 |
  | `system_cost` | 70 |
  | `technical_savings` | 70 |
  | `lvst_value` | 63 |
  | `sector_specific` | 35 |
  | `congestion` | 28 |
  | `fuel_cost` | 28 |
  | `road_safety` | 28 |
  | `water_pollution` | 28 |
  | `consumer_savings` | 21 |
  | `ecosystem_services` | 14 |
  | `human_health` | 14 |
  | `ippu_value` | 14 |
  | `env_pollution` | 7 |
  | `land_pollution` | 7 |
  | `indoor_air_pollution` | 1 |

  — [cba_results.csv](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413/cba_results.csv>)
- Example item names:
  - `cb:entc:technical_cost:electricity:{capex,opex,transmission}`
  - `cb:trns:technical_cost:electrification:{LDV,hdv_charger,hdv_vehicles,rail}`
  - `cb:trns:system_cost:passenger_transport:road_light`
  - `cb:scoe:technical_cost:efficiency:{appliance,building_shell}`
  - `cb:inen:sector_specific:fuel_cost:X` (difference variable `totalvalue_enfu_fuel_consumed_inen_fuel_oil`)
  - `cb:wali:human_health:safe_sanitation:X`
  - `cb:trww:water_pollution:wastewater_treatment:P`
  - `cb:lndu:ecosystem_services:forests:primary`
  - `cb:trns:{air_pollution,congestion,road_safety}:X:<fuel>`
  - `cb:scoe:indoor_air_pollution`

  The `difference_variable` holds the physical driver, e.g. `vehicle_distance_traveled_trns_road_light_electricity`, `area_lndu_forests_primary`, `pop_safelymanaged_urban`, `qty_waso_open_dump_yard_tonne`, `energy_consumption_scoe_total`. — [cba_results.csv](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413/cba_results.csv>)

**Sign convention and data quirks**
- Example: `cb:entc:technical_cost:electricity:capex` sums to −57.8 bn (a cost), while `cb:trww:water_pollution:*` is positive (a benefit). — [cba_results.csv](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413/cba_results.csv>)
- The sign convention is **opposite** in the MAC file, where "technical_cost_* … + = net cost to implement; − = net saving". — [tornado_vs_whirlpool.pptx, slide 2](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/tornado_vs_whirlpool.pptx>)
- Rows for periods 14–19 (2029–2034) roughly double because of 3,900 `*_shifted2019…_shifted2024` rows (≈US$10.5 bn in total). These are the `cb_shift_costs` re-timing of pre-2025 costs, not duplicates: no duplicate keys were found. — [cba_results.csv](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413/cba_results.csv>)

**Magnitudes** (my calculations from `value`; US$ bn; presumably 2019 USD; undiscounted unless stated)

| Category | NZ | NDC2-2020 | NDC2-2025 |
|---|---|---|---|
| technical_cost 2025–2050 | −258.8 | −196.8 | −159.3 |
| technical_savings 2025–2050 | 43.4 | 3.3 | 2.6 |
| system_cost 2025–2050 | 51.3 | 1.9 | 1.2 |
| fuel_cost 2025–2050 | 24.5 | 8.6 | 6.7 |
| human_health 2025–2050 | 177.5 | 103.2 | 78.9 |
| consumer_savings 2025–2050 | 176.0 | 47.8 | 36.7 |
| indoor_air_pollution 2025–2050 | 18.8 | 136.0 | 57.6 |
| water_pollution 2025–2050 | 35.1 | 61.1 | 48.8 |
| crop_value 2025–2050 | 65.9 | 61.2 | 45.5 |
| air_pollution 2025–2050 | 9.1 | 8.5 | 6.6 |
| **Net, 2025–2050** | **406.9** | **326.4** | **195.1** |
| Net PV at 6% (base 2025) | 161.4 | 184.6 | 89.8 |
| of which technical_cost PV at 6% | −96.2 | −81.3 | −59.5 |
| Net PV at 7% | 140.8 | 170.6 | 80.2 |
| Net, 2019–2070 | 1,568.4 | 859.2 | 714.5 |

— computed from [cba_results.csv](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413/cba_results.csv>)

- Annual technical cost as % of baseline `gdp_mmm_usd` (PPP):
  - 2030: NZ −1.41%, NDC2-2020 −2.89%, NDC2-2025 −0.89%
  - 2040: NZ −2.57%
  - 2050: NZ −3.77%

  Uganda baseline `gdp_mmm_usd` is 128.4 in 2025 and 679.2 in 2050. — computed from [cba_results.csv](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413/cba_results.csv>) and [sisepuede_ide_run…csv](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413/sisepuede_ide_run_2025-10-29T19;49;25.722413.csv>)
- Largest NZ technical-cost items (2019–2050, undiscounted, US$ bn):
  - `trww:…tertiary_anaerobic` −52.8
  - `scoe:efficiency:appliance` −36.9
  - `lvst:ent_ferm_mgmt` −30.1
  - `agrc:producer_food_waste` −27.8
  - `trww:waste_to_energy` −18.4
  - `wali:sanitation:safeman_rural` −17.8
  - `entc:electricity:capex` −13.9
  - `wali:sanitation:safeman_urban` −13.2
  - `waso:waste_to_energy:landfill` −12.9

  — computed from [cba_results.csv](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413/cba_results.csv>)
- The Uganda memo lists the CBA categories as:
  - "Capital costs: Investments required to achieve the outcomes of the transformations"
  - avoided air pollution
  - avoided environmental pollution
  - ecosystem services
  - industrial output
  - agricultural output
  - avoided water pollution
  - consumer savings

  The reference case runs 2019–2070. GDP is in 2019 USD PPP, with growth falling linearly to 2% by 2050. — [SiSEPUEDE_analysis-Uganda v2025_10_16.docx](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413/SiSEPUEDE_analysis-Uganda v2025_10_16.docx>)

**Uganda baseline context relevant to fiscal work**
- Oil: "total extraction of crude oil peaks at an estimated 226 kbd", with 1.56 bn barrels by 2100, plus a 60 kbd refinery from 2026.
- Gas: natural gas exports of 189.95 PJ/yr.
- Vision 2040 quoted: "Increased oil and gas revenue from UGX 62.98Bn to UGX 265Bn".

  — [SiSEPUEDE_analysis-Uganda v2025_10_16.docx](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413/SiSEPUEDE_analysis-Uganda v2025_10_16.docx>)

**MAC file**
- The MAC file compares "Tornado (measure run alone)" with "Whirlpool (leave-one-out from the full package)" for 66 measures (72 rows): "MAC = Net incremental cost (USD) ÷ Emissions avoided (tCO₂e)". — [tornado_vs_whirlpool.pptx](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/tornado_vs_whirlpool.pptx>); [tornado_vs_whirlpool (1).csv](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/tornado_vs_whirlpool (1).csv>)

### Inferences
- The benefit mix is heavily non-cash and non-fiscal: health, sanitation, water pollution, food waste, indoor air. In a fiscal-allocative layer these should be kept separate from the cash flows that could be captured as revenue or savings (fuel cost, system cost, technical savings).
- The `sector_specific:fuel_cost` lines (e.g. `inen` +279.5 bn over 2019–2070 across strategies) and `fuel_cost` lines are the natural hooks for **import-bill and fiscal-subsidy effects**. They are valued at SISEPUEDE fuel costs, not CPAT retail or tax-inclusive prices.
- The PVs above use a 2025 base and my own rates. They are illustrative; they are not SISEPUEDE outputs.

### Gaps
- The `indoor_air_pollution` rows have NaN baseline/pathway values (computed by a separate rule), and how they are computed is not documented here.
- Currency year and real/nominal status are not stated in the Uganda files (2019 USD is inferred from the module documentation).
- Whether `shifted` rows double count air pollution is unresolved.

---

## Q4. What is the "combined GIMF/DIGNAD/DIGNAR (CPM / CPAT-CPM)" macro-fiscal tool, how does investment or spending enter it, and how do CDPM/CPAT outputs feed it (the "bridge")?

### Takeaway
No GIMF, DIGNAD or DIGNAR tool exists in either repository. "CPAT-CPM" is the **CPAT ↔ SISEPUEDE bridge** (Egypt proof of concept, methodology v0925). Investment enters it in two ways:
- **As CPAT's macro side:** carbon-tax revenue is split across 5 uses. Each use has an MFMod-median fiscal multiplier with lags 0–19, which raises GDP. There is no public capital stock, efficiency parameter or return on capital.
- **As CPM's physical side:** the "public investment" share of revenue buys SISEPUEDE transformations through `u_j = min(B_j/c_j, u_j,max)`, using the cost module's cumulative technical cost per dose.

The other internal macro-fiscal elements are:
- a planned **debt-dynamics equation** using IMF WEO projections, with a disaster-cost term
- a **Tax and Macro-Fiscal Dashboard** with fiscal-space, delivery, cost-of-capital and financing-risk blocks
- planned links to **MFMod, MANAGE and MINDSET**

### Cited Findings
**No IMF DSGE models in the repositories**
- A grep for `GIMF|DIGNAD|DIGNAR` across all of `/home/user` (text files, all extracted .docx/.pptx text, and both .msg bodies) returned **no matches**. "CDPM" appears only on the slide cited in Q1. The CPAT-AI repo mentions SISEPUEDE only once, in `CAVEATS.md` (a superseded Sisepuede guide). — searches over [/home/user/CPAT-AI](</home/user/CPAT-AI>) and `/home/user/CPAT-CDPM`

**The bridge: purpose and principle**
- "CPAT is a price model … CPM … is a quantity model … Neither model on its own can say what a carbon tax does once its revenue is spent on physical measures, or what tax would pay for a set of measures that reaches an emissions target."
- Principle: "prices, elasticities and money cross between the models; tonnes of emissions never do."

  — [CPAT_CPM_Methodology_v0925.docx §1](<MainProjectFolder/2. Other Documentation/CPAT_CPM_Methodology_v0925.docx>)
- Versions: CPAT Excel 1.0pre_453; CPM configured for Egypt, run to 2041. — [CPAT_CPM_Methodology_v0925.docx §2.1](<MainProjectFolder/2. Other Documentation/CPAT_CPM_Methodology_v0925.docx>)

**Track 1 (tax → emissions)**
- The user sets a tax path and "the share of its revenue that goes to each of CPAT's five uses: labour tax cuts, corporate tax cuts, public investment, current spending and transfers".
- Price channel, with `k(f,s)` the fractional retail-price rise per US$ of tax and elasticities read from CPAT's table:
  - `R(f,s,t) = [1 + k(f,s)·tax(t)]^ε(f,s)` (1)
  - `ε = εU + εF·(1+εU)` (2)
- Power: `m_policy(t) = m_baseline(t)·S_gas,policy(t)/S_gas,baseline(t)` (3).
- Revenue as income: `GDP_CPM,policy(t) = GDP_CPM,baseline(t)·[1 + Σ_d g_d(t)]` (4).
- Revenue as measures: `u_j = min(B_j/c_j, u_j,max)` (5), where `c_j` is the "Cost of transformation j per unit of intensity, 2022-2041, US$ bn per dose".

  — [CPAT_CPM_Methodology_v0925.docx §3](<MainProjectFolder/2. Other Documentation/CPAT_CPM_Methodology_v0925.docx>)
- Egypt illustration:
  - Tax: US$0 in 2025 rising to US$50 in 2050; split 30% labour tax cuts / 50% public investment / 20% transfers.
  - Revenue raised: US$146.9 bn over 2022–2041.
  - The tax alone cuts 2041 emissions from 810 to 717 MtCO2e.
  - "US$ 72.6 bn of the US$ 73.5 bn for public investment" is spent on transformations; the cumulative reduction reaches 19.5%.

  — [CPAT_CPM_Methodology_v0925.docx §3.7](<MainProjectFolder/2. Other Documentation/CPAT_CPM_Methodology_v0925.docx>)

**Which use of revenue buys what**
- "Public investment pays for those that leave an asset behind; current spending for programmes that leave none; transfers and labour tax cuts for those a household would pay for; and corporate tax cuts for those a firm would pay for." — [CPAT_CPM_Methodology_v0925.docx §4.1](<MainProjectFolder/2. Other Documentation/CPAT_CPM_Methodology_v0925.docx>)
- Coverage (measured / costed but effect not measured / not costed):
  - Public investment 12 (8 offered) / 10 / 12
  - Current spending 0 / 14 / 0
  - Transfers 5 / 1 / 0
  - Labour tax cuts 5 / 1 / 0
  - Corporate tax cuts 5 / 21 / 0

  — [CPAT_CPM_Methodology_v0925.docx §4.2](<MainProjectFolder/2. Other Documentation/CPAT_CPM_Methodology_v0925.docx>)
- Measures offered (US$/tCO2e; capacity to absorb, US$ bn; cumulative 2022–2041, measured one at a time):

  | Measure | US$/tCO2e | Absorbs up to (US$ bn) |
  |---|---|---|
  | HFCs | 8 | 1.7 |
  | Landfill gas | 8 | 0.2 |
  | Oil and gas leaks | 14 | 0.7 |
  | Heat pumps | 24 | 8.9 |
  | Building envelope | 30 | 11.5 |
  | Industrial process heat | 60 | 14.2 |
  | Appliances and lighting | 89 | 36.2 |
  | EVs | 413 | 76.5 |

  Not offered: the renewable target, industrial and vehicle efficiency, and clinker substitution ("whose cost is negative"). — [CPAT_CPM_Methodology_v0925.docx §4.3](<MainProjectFolder/2. Other Documentation/CPAT_CPM_Methodology_v0925.docx>)
- The per-destination mapping to the cost module's "three layers per lever: the technical cost …, the system cost it changes (a saving), and the externalities it avoids":
  - Public investment → "Technical cost of levers that leave an asset behind" (renewable target, building shell, passenger mode shift, urban wastewater)
  - Current spending → programme levers (diets, food waste, agricultural productivity, reforestation)
  - Transfers → "household share of technical cost"
  - Labour tax cuts → household rows plus "the system-cost layer"
  - Corporate tax cuts → "the firm share"

  — [CPAT_CPM_bridge_map.pptx, slide 12](<MainProjectFolder/1. Project Presentations/CPAT_CPM_bridge_map.pptx>)

**Track 2 (target → tax)**
- Revenue required: `R* = C / s_pi` (6), where `C` is "the technical cost of the measures from CPM's cost–benefit module, cumulative 2022-2041, US$ bn".
- Revenue surface: `R(L,s) = R_pi(L)·[1 + Σ_d s_d·β_d(L)]` (7), "built from 35 CPAT runs: 7 tax levels × 5 uses". Worst error is 0.09%. "The surface is linear in the shares because the GDP effect of each use in CPAT is a multiplier on the money it receives."
- Egypt result: measures cost US$17.2 bn, so the tax must raise US$34.4 bn. CPAT confirms "US$ 6.4 per tonne in 2040", raising US$34.6 bn. CPAT also reports:
  - GDP +0.10% in 2041
  - poorest decile +0.43% of consumption, richest −0.10%
  - "fuel fiscal balance US$ 4.3 bn better"
  - "welfare benefit of US$ 5.0 bn in 2040"
  - 5,301 deaths averted by 2040

  — [CPAT_CPM_Methodology_v0925.docx §5](<MainProjectFolder/2. Other Documentation/CPAT_CPM_Methodology_v0925.docx>); [CPAT_CPM_tool_walkthrough.pptx](<MainProjectFolder/1. Project Presentations/CPAT_CPM_tool_walkthrough.pptx>)
- Reporting rule: "CPM's cost–benefit module gives the technical cost of each transformation and what it saves the energy system in fuel and in generating capacity. CPAT gives GDP, the fiscal balance, welfare, health … their figures are shown side by side and never added." — [CPAT_CPM_Methodology_v0925.docx §6](<MainProjectFolder/2. Other Documentation/CPAT_CPM_Methodology_v0925.docx>)
- Caveats stated by the team:
  - "Track 2 is open-loop."
  - "One use of the revenue is connected. Only public investment buys measures."
  - "Transformations are measured one at a time … CPM's cost–benefit module splits their shared cost with weights that do not match what the runs show. Heat pumps combined with building insulation are the case to avoid."
  - "CPAT Excel is the reference. The coded version … reproduced about half of Excel's policy response for Egypt."

  — [CPAT_CPM_Methodology_v0925.docx §7](<MainProjectFolder/2. Other Documentation/CPAT_CPM_Methodology_v0925.docx>)
- An unresolved choice: "the pathway in step 2 is not unique … the track needs a rule for choosing between them — least tax, least net cost, most GDP, most welfare. That is a policy choice". — [CPAT_CPM_bridge_map.pptx, slide 14](<MainProjectFolder/1. Project Presentations/CPAT_CPM_bridge_map.pptx>)

**CPAT variables the bridge reads (Annex A)**
- `mit.gdp.pre.lvl.1`, `mit.gdp.pst.lvl.2`
- `mit.gdp.<pit|inv|cur|tra>.pct.2` ("GDP effect of each use of the revenue")
- `mit.rev.new.usd.<1|2>` (revenue). It appears twice with different unit labels, "US$ bn of 2026, and real 2021 US$", which is unresolved.
- `mit.nim.pow.<tech>.t.<1|2>` (new power capacity investment, MW)
- `mit.sp.pow.<nga|coa>.a.1`
- `distn.<tef|pit|pui|cts|tgt>.tot.dec.ove`
- `air.*`, `mit.wel.*`
- Dashboard inputs P7–P11: revenue shares.

The coded CPAT does not yet produce the revenue and GDP-feedback outputs. — [CPAT_CPM_Methodology_v0925.docx, Annex](<MainProjectFolder/2. Other Documentation/CPAT_CPM_Methodology_v0925.docx>)

**How spending enters CPAT's GDP**
- "Fiscal multipliers by group, instrument and lag 0-19 (sheet Multipliers, from the legacy sheet: MFMod medians)". The uses map to labour tax (`pit`), corporate tax (`cit`), public investment (`capt`), current spending (`gnfs`) and transfers (`trns`). "The revenue itself counts as an energy-tax increase (instrument `exc`, share -1)."
- Egypt defaults: labour 30, corporate 0, public investment 50, current 0, transfers 20.

  — [GDP_Method_v6_1.md](</home/user/CPAT-AI/cpat_excel/working_version/GDP_Method_v6_1.md>)
- The equations:
  - E91 `fs(t) = (Rnew(t) − Rnew^(1)(t))/Y0(t)` (fiscal space)
  - E92 `imp(t) = fs(t) − fs(t−1)`
  - E93 `eff_i(t) = sh_i/100·Σ_{k=0..19} imp(t−k)·m_i(k)`
  - E94 `ε_GDP(t) = Σ_i eff_i(t)`
  - E95 `lvl(t) = 1 + ε_GDP(t−1)`; `g(t) = (1+g0(t))·lvl(t)/lvl(t−1) − 1`

  — [Equations_v6_1.md](</home/user/CPAT-AI/cpat_excel/working_version/Equations_v6_1.md>)
- Egypt result: fiscal space 0.74–0.75% of GDP (2027–2030); GDP effect +0.39% by 2040. — [GDP_Method_v6_1.md](</home/user/CPAT-AI/cpat_excel/working_version/GDP_Method_v6_1.md>)
- The bridge assumption list: "C5 The multiplier is a flat scalar per destination. And the four published GDP effects are additive slices of the net". — [CPAT_CPM_bridge_map.pptx, slide 16](<MainProjectFolder/1. Project Presentations/CPAT_CPM_bridge_map.pptx>)

**Debt dynamics, fiscal space and the IMF-projection layer (planned)**
- "2. Debt Equation … a basic form of FSA/DSA … uses 10 years of projections of the main macro-fiscal quantities, coming from the IMF … Does not replace MFMod, FSA and DSA analysis."
- Core equation, as rendered on the slide: `d_{t+1} = d_t·(1+i_t)/(1+g_t+π_t) − pb_t + sfa_t + DC_t`, where `DC_t` = "disaster costs (contingent liabilities)".

  — [Overview-CPAT-Sisepuede-LTS.pptx, slide 18](<MainProjectFolder/8. Archive/Overview-CPAT-Sisepuede-LTS.pptx>); [CPAT-LTS-CSFGrant.pptx](<MainProjectFolder/9. CPAT-LTS Project/CPAT-LTS-CSFGrant.pptx>)
- "For the fiscal component (balancing spending and borrowing), we would use existing IMF projections, perturbed by policy scenarios." — [1. Overview-Flows+Objectives+Timeline.docx](<MainProjectFolder/1. Overview-Flows+Objectives+Timeline.docx>)
- "Fiscal Space modelling … Input the IMF's fiscal space modelling … We process this in R"; and "adding basic DSA-style debt dynamics". — [CPAT-LTS-Update.docx](<MainProjectFolder/9. CPAT-LTS Project/CPAT-LTS-Update.docx>)

**Macro links via World Bank models (not IMF DSGEs)**
- "In the Uganda CCDR, there has been integration between the SiSePuede model and MFmod, the World Bank's main macroeconomic model (also elsewhere MANAGE) focusing on public investment." — [Master Doc-Fiscal-LTS-Program.docx](<MainProjectFolder/8. Archive/Master Doc-Fiscal-LTS-Program.docx>)
- Partnership Task 1 culminates in "the use of the integrated system to support macro-fiscal assessments by linking long-term development and decarbonization pathways to fiscal and macroeconomic inputs". — [Partnership_Agreement-Tec de Monterrey-Feb2026.docx](<MainProjectFolder/9. CPAT-LTS Project/Core Document and Example Data/More Project Documents/Partnership_Agreement-Tec de Monterrey-Feb2026.docx>)

**Public Investment Model Emulator ("pseudo-model")**
- To be built "within SiSePuede to translate public investment into emissions reduction, initially in Egypt". It models "Optimized allocation of public investment across sectors" and "Emissions outcomes associated with specific investment allocations".
- Outputs: "Investment needs; Emissions trajectories …; Public/private shares; Policy-relevant reporting indicators".
- It feeds "Fiscal space analysis; Debt and financing projections". "The model emulator supports Excel CPAT only."

  — [Combined Document CPAT-LTS-Sisepuede.docx, A3.2/B3](<MainProjectFolder/Combined Document CPAT-LTS-Sisepuede.docx>)

**Tax and Macro-Fiscal Dashboard (separate deliverable)**
- "53 indicators, 217 countries … Nine blocks: four judge (fiscal space, delivery, cost of capital, financing risk); five give context and detail … scored 1–10 … from 16 public datasets (IMF, World Bank, PEFA, Ember, IRENA)". It was handed to Dirk (23 Oct 2026). — [AIClimate-FiscalTools_v2.5.pptx, slides 19–20](</home/user/CPAT-AI/Presentations - Overarching/AIClimate-FiscalTools_v2.5.pptx>); [Stephen_FY27_Work_Plan_v2.6_15thOct.docx](</home/user/CPAT-AI/Presentations - Overarching/Stephen_FY27_Work_Plan_v2.6_15thOct.docx>)

**New CPAT UI mock-up**
- The workbook has a results sheet "💰 Macro & Fiscal", next to "🌍 Energy & Emissions", "⚖️ Equity & Distribution" and "🌬️ Co-benefits". — [NewMockupUI-CPAT 1.1 visioning 12.xlsb (sheet names only)](<CPAT Excel - UI and Working Version/NewMockupUI-CPAT 1.1 visioning 12.xlsb>)
- The CPAT 1.0pre_459 workbook has sheets `Multipliers`, `CoC`, `SCC`, `WEO`, `GDPRatios`. — [CPAT 1.0pre_459_EGYMARMEX.xlsb (sheet names)](<CPAT Excel - UI and Working Version/CPAT 1.0pre_459_EGYMARMEX.xlsb>)

### Inferences
- If the proposal wants a DIGNAD/DIGNAR-style layer (public capital stock, investment efficiency, absorptive capacity, return on public capital, user fees, fiscal reaction function), that is **new relative to everything internal**. Today the only mechanism linking public spending to growth is CPAT's reduced-form multiplier on `capt`. It has no efficiency or stock dynamics. The only debt object is the planned `d_{t+1}` equation.
- The natural slot for a DIGNAD-style element is between three points:
  - (i) the revenue/budget amount `B_j` (bridge eq. 5);
  - (ii) CPAT's `capt` multiplier (E93);
  - (iii) the debt equation, which already has a disaster-cost term `DC_t` that matches DIGNAD's disaster/adaptation-capital logic.

### Gaps
- No internal document states that the team uses GIMF, DIGNAD or DIGNAR, or plans to. If the user's premise comes from elsewhere (emails or meetings not in these folders), that source was not available.
- Public descriptions of DIGNAD and DIGNAR could not be verified here (`imf.org` unreachable; search budget exhausted). This is left to the external-literature researcher.

---

## Q5. What do the FY27 work plan, its comments and related plans say about upgrades, priorities, timelines, CBA, fiscal space, public spending efficiency, BOOST, PERs, and other sectors?

### Takeaway
FY27 has two parts:
- **Objective 1:** a coded CPAT engine.
- **Objective 2:** CPAT–CPM integration and Pathways Tool. It brings in the "CPAT-LTS investment approach" in versions: **V1** process emissions for CBAM sectors plus green public investment from CCDR data (prototyped); **V2** debt projections (to be agreed); **V3** efficiency of public investment and energy fiscal costs and risks for finance ministries (to be agreed).

Earlier planning documents call for a finance-ministry "mini-CBA" focused on fiscal indicators: energy security and import dependence, fiscal costs and contingent liabilities. They name PIMA, CBA, BOOST and PFRs as anchors.

### Cited Findings
**Objective 2 scope and versions**
- "The CPAT-LTS investment approach enters the tool in versions: V1 process emissions for CBAM sectors (with Karly, in progress) and green public investment from CCDR data (prototyped); V2 debt projections (to be agreed); V3 efficiency of public investment and energy fiscal costs and risks for finance ministries (to be agreed)." — [FY27 Work Plan (CPM comments), Section B Implementation](<MainProjectFolder/2. Other Documentation/Stephen_FY27_Work_Plan - Coded CPAT - and CPAT-CPM Elements_CPM_comments.docx>); same in [v2.6 15 Oct](</home/user/CPAT-AI/Presentations - Overarching/Stephen_FY27_Work_Plan_v2.6_15thOct.docx>)
- Product list:
  - "Revenue and fiscal: CPAT's revenue calculations, with IMF fiscal projections perturbed by policy scenarios"
  - "Public investment: marginal abatement cost information and SiSePuede's optimized public investment linked back to CPAT-Excel"
  - "Possible Benefits … a fiscal and investment view that finance ministries can use"

  — [FY27 Work Plan (CPM comments)](<MainProjectFolder/2. Other Documentation/Stephen_FY27_Work_Plan - Coded CPAT - and CPAT-CPM Elements_CPM_comments.docx>)

**Timeline (v2.6 and the CPM-comments version)**
- CPM team supervision on prices and policies: 28 Sep–11 Dec 2026.
- "Investment approach, policy interface and air pollution translation; Morocco application": 4–29 Jan 2027. Version v2.6 says pathways tool complete by 15 Jan 2027 (milestone 2c_m1).
- Common Python platform (CPAT, MFMod-Python, FTT): Feb 2027.
- Contract ends 20 March 2027.

— [FY27 Work Plan (CPM comments)](<MainProjectFolder/2. Other Documentation/Stephen_FY27_Work_Plan - Coded CPAT - and CPAT-CPM Elements_CPM_comments.docx>); [v2.6](</home/user/CPAT-AI/Presentations - Overarching/Stephen_FY27_Work_Plan_v2.6_15thOct.docx>)

**CPM team comments ("Alexa")**
- "Today the bridge carries CPAT's demand equation into CPM in closed form, anchored on CPAT Excel outputs; coded CPAT does not run inside CPM."
- Status for Egypt: "policies: carbon pricing done, public investment one of five revenue routes implemented … revenue and fiscal partial; co-benefits and air pollution not started … public investment linked back to CPAT-Excel not built."
- Moving to coded CPAT "needs revenue and GDP-feedback outputs that coded CPAT does not yet produce. Tight for 11 December."

— [FY27 Work Plan (CPM comments), comments](<MainProjectFolder/2. Other Documentation/Stephen_FY27_Work_Plan - Coded CPAT - and CPAT-CPM Elements_CPM_comments.docx>)

**Pathways Tool scoping meeting (13 Oct 2026; Stretton, Groves, Sampson)**
- The user flow ends in an "Optimization layer ★ Better tax level, investments, allocation".
- Outputs: emissions, revenue, investment needs, price responses, GDP, household, distributional, carbon market and CBAM impacts.
- Typology: "Up front Public Investment can pay technical capital cost — Not in. Assumed to be 'like 2' – no distinction between up front and incremental costs"; "Carbon Tax does some of the work on transformation — Not in explicitly."
- Open issue: "Investment costs vs. subsidies — Needs a clearer method. Separate running subsidies from upfront public investment, show how a carbon tax reduces each, and report dollars as well as marginal costs." Also "Does a carbon tax shift investment needs? How does the cost module reflect a tax?"

— [Slides_Oct-19th-WBside-Pathways_CPAT_proposal.pptx, slides 2–7](<CPAT Excel - UI and Working Version/Slides_Oct-19th-WBside-Pathways_CPAT_proposal.pptx>)

**Fiscal-LTS framework and the mini-CBA**
- Finance-ministry objectives table:
  - Objective "Efficiency of Strategic Objectives"; Method "Efficient Prices; Efficient Public Investment"; Instrument "Short term and long-term prices; PIMA, CBA"; Analytical Tool "SiSePuede CBA, CPAT Efficient prices".
  - Objective "Growth"; Instrument "Public Investment, Certainty Policies (PPAs, CFDs)"; Tool "Macro integration in pathways tool".
  - Objective "Debt Interest"; Method "Cheaper borrowing through Fiscal probity, MDB lending, guarantees"; Tool "None".

  — [CPAT-LTS-Update.docx, Appendix: Fiscal-LTS Framework](<MainProjectFolder/9. CPAT-LTS Project/CPAT-LTS-Update.docx>); also in [Combined Document CPAT-LTS-Sisepuede.docx](<MainProjectFolder/Combined Document CPAT-LTS-Sisepuede.docx>)
- "While CCDRs and LTSs focus on emissions pathways … PFRs focus on debt, deficits, fiscal risks, energy prices, and public investment efficiency."
- "Finance-ministry output metrics (mini-CBA)": "Energy security (import dependence, price exposure); Energy transition risks and costs; Fiscal costs, revenues, and contingent liabilities; Designed to support policy trade-offs rather than full welfare optimization."
- "PFRs … lack a dedicated chapter on expenditure policy."

  — [Master Doc-Fiscal-LTS-Program.docx](<MainProjectFolder/8. Archive/Master Doc-Fiscal-LTS-Program.docx>)
- "Develop CPAT towards a simple CBA focused on indicators with fiscal implications (see example tool from NZ). For example fiscal risks from energy, opportunities and opportunity costs from enhanced ff exports/reduced ff imports." Slide "4. Mini CBA": "Systemic CBA (hard) … Phase I: Fiscal related indicators … See CBAX (New Zealand Tool) … See Green Book (UK)". — [Overview-CPAT-Sisepuede-LTS.pptx, slides 16, 27](<MainProjectFolder/8. Archive/Overview-CPAT-Sisepuede-LTS.pptx>)
- "1. Investment Needs … Incorporate the CCDR investment need data into CPAT … Also add basic data on BOOST investment at present." — [Overview-CPAT-Sisepuede-LTS.pptx, slide 17](<MainProjectFolder/8. Archive/Overview-CPAT-Sisepuede-LTS.pptx>)
- Fiscal-LTS components: "A public-investment model that translates public investment into emissions reductions"; "A private-investment policy model (… power sector)"; "A debt-equation approach that integrates IMF revenue forecasts"; "information on total mitigation investment needs (from CCDR) and current investment/maintenance expenditure". — [Master Doc-Fiscal-LTS-Program.docx](<MainProjectFolder/8. Archive/Master Doc-Fiscal-LTS-Program.docx>)
- Sector focus: "We propose to focus only on the energy (grid, storage) and road transport sectors … We'd use the CCDR approach to including what is needed to make that investment resilient." CPAT has "revenue and (generic) public expenditure, without that expenditure being linked up to specific mitigation or adaptation needs". — [CPAT-LTS-Update.docx](<MainProjectFolder/9. CPAT-LTS Project/CPAT-LTS-Update.docx>)
- Later work: "Probably a good idea in FY27 Stephen to work with macro team to do basic investment analysis in MFMod". Future Work Program D includes "integration of MFMod and SISEPUEDE for better macro-fiscal projections". — [Master Doc-Fiscal-LTS-Program.docx](<MainProjectFolder/8. Archive/Master Doc-Fiscal-LTS-Program.docx>)

**Governance flag**
- Dirk Heine comment on the partnership text: "I don't think this section is compatible with our agreements with the IMF on CPAT, and with the data providers behind CPAT." — [Partnership_Agreement-Tec de Monterrey-Feb2026.docx, comments](<MainProjectFolder/9. CPAT-LTS Project/Core Document and Example Data/More Project Documents/Partnership_Agreement-Tec de Monterrey-Feb2026.docx>)
- Licensing: "CPAT (WB proprietary), SiSePuede (open source), integrated package WB proprietary." — [Master Doc-Fiscal-LTS-Program.docx](<MainProjectFolder/8. Archive/Master Doc-Fiscal-LTS-Program.docx>)

### Inferences
- A proposal on public spending efficiency and CBA fits squarely into the not-yet-agreed **V3**: "efficiency of public investment and energy fiscal costs and risks for finance ministries". It also answers the 13 Oct open issue (upfront public capex vs running subsidies; dollars as well as MACs). It is consistent with the "mini-CBA" wording (fiscal indicators first, NZ CBAx / UK Green Book as models).
- Timing: the January 2027 integration window (4–29 Jan) and the 20 March 2027 contract end constrain the scope to a prototype.

### Gaps
- There is no detailed specification of V2 or V3, and none of the "Leonardo" TOR mentioned on the debt-equation slide.
- BOOST is mentioned only as "add basic data on BOOST investment at present". No BOOST data file is in the repository.
- PIMA appears only as an instrument label. No PIMA scores or efficiency parameters are present.

---

## Q6. Any mention of small island states, renewable energy, PPAs/PPPs, oil import bills or fiscal space?

### Takeaway
Small island states appear only as data rows in the CCDR investment compilation: Cabo Verde, Mauritius, Dominica, Grenada, St Vincent, St Lucia. They are never analysed. PPAs, CfDs and PPPs appear as power-sector "certainty policies" and as an Egypt policy upgrade. Oil imports appear only as a mini-CBA indicator idea. Fiscal space is operationalised in CPAT as new revenue as a share of GDP, and in the dashboard as a scored block.

### Cited Findings
**Small island states**
- Cabo Verde CCDR tab, "Constant 2023 US$ million, discounted (6%)". CAPEX for now–2030 / 2031–40 / 2041–50, with notes on the private-finance share:
  - Power 136/150/13 (private share 0.55)
  - Transport 106/123/15 ("25% for the EV part, 0% on roads")
  - Urban 16/20/13 ("20% on waste")
  - Water 14/31/25 ("50% on desal")
  - Agriculture 101/102/38 (0.4)
  - "Industry (blue economy)" 47/52/25 ("50% on tourism, 30% on fishery")
  - OPEX is listed separately.

  — [Investments master fileV7-shared_w_SStretton.xlsx, sheet "Cabo Verde"](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/Investments master fileV7-shared_w_SStretton.xlsx>)
- Mauritius tab ("Constant 2020 US$ billion, discounted (6%)", while the column is headed "2026 - 2050 (US$ million)"):
  - Power 1,103 (CAPEX 928)
  - Transport 664
  - Water 451
  - Agriculture 478
  - Infrastructure 941
  - Blue economy 680
  - Human capital 461
  - Disaster risk reduction 451
  - Waste 173
  - Tourism 67

  — [Investments master fileV7-shared_w_SStretton.xlsx, sheet "Mauritius"](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/Investments master fileV7-shared_w_SStretton.xlsx>)
- Public/private shares are recorded for 16 of 47 economies, including SIDS: Dominica public 0.71; Grenada 0.33; St Vincent 0.33; St Lucia 0.26. "Coverage is dominated by adaptation-heavy small economies (Western Balkans, OECS, Tanzania, CAR)." — [CCDR_mitigation_consistent_table.xlsx, "Public vs Private (partial)"](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/CCDR_mitigation_consistent_table.xlsx>)

**PPAs, CfDs and PPPs**
- "Power sector already has private investment and related policies (includes public investment and PPPs and PPAs/CFDs) … We've upgraded our WACC model to better account for cost of capital -> Next step derisking policies." — [Overview-CPAT-Sisepuede-LTS.pptx, slide 19](<MainProjectFolder/8. Archive/Overview-CPAT-Sisepuede-LTS.pptx>)
- "Upgrade of policy to cover: Carbon tax, Renewable PPA contracts, and public investment (initially for Egypt)". — [Master Doc-Fiscal-LTS-Program.docx](<MainProjectFolder/8. Archive/Master Doc-Fiscal-LTS-Program.docx>)
- CPAT power model details:
  - WACC options (Country, Tech, income group) and "Discounted lifetime = (1 − (1 + WACC)^−N)/(1 − (1 + WACC)^−1)".
  - PPAs: "a share p of coal and gas generation … runs at its capacity factor … whatever its cost", phased out over `YearsToPhaseOutPPAs`.
  - Renewable subsidies enter the levelised fixed cost.

  — [PowerModel_Method_v6_1.md](</home/user/CPAT-AI/cpat_excel/working_version/PowerModel_Method_v6_1.md>)
- "Financing modalities: Public …; Public-private (revenue guarantee) = privately financed but de-risked by public revenue certainty (PPAs, contracts-for-difference, feed-in tariffs, viability-gap funding, guarantees, blended / first-loss); Private". Marked "Illustrative, order-of-magnitude estimates — NOT sourced country-by-country". — [net_zero_by_country.xlsx, Notes](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/net_zero_by_country.xlsx>)

**Oil imports and energy security**
- "opportunities and opportunity costs from enhanced ff exports/reduced ff imports" — [Overview-CPAT-Sisepuede-LTS.pptx, slide 16](<MainProjectFolder/8. Archive/Overview-CPAT-Sisepuede-LTS.pptx>)
- "Energy security (import dependence, price exposure)" — [Master Doc-Fiscal-LTS-Program.docx](<MainProjectFolder/8. Archive/Master Doc-Fiscal-LTS-Program.docx>)
- CPAT outputs include "trade balance". — [CPAT-Concise Training.pptx](<MainProjectFolder/5. CPAT Equations List, Docs and Excel Version/CPAT-Concise Training.pptx>)

**Fiscal space**
- CPAT definition: `FISCALSPACE = (revenue − revenue_ref)/(gdp_bn·MperBn)`, code `fis.sp`. — [Formulas_v6_1.md](</home/user/CPAT-AI/cpat_excel/working_version/Formulas_v6_1.md>)
- "Incorporate fiscal space diagnostics from the World Bank's macro-fiscal data to examine how much financing could realistically be mobilized domestically." — [Master Doc-Fiscal-LTS-Program.docx, Soft Integration TOR](<MainProjectFolder/8. Archive/Master Doc-Fiscal-LTS-Program.docx>)
- "Debt dynamics (is there fiscal space)" — [1.Egypt_CPAT_SISEPUEDE_Integration_WhyAndWhat.pptx](<MainProjectFolder/1. Project Presentations/1.Egypt_CPAT_SISEPUEDE_Integration_WhyAndWhat.pptx>)

**Renewables**
- The SISEPUEDE transformation `ENTC:TARGET_RENEWABLE_ELEC` uses `magnitude`, `dict_entc_renewable_target_msp = {pp_wind: 0.147, pp_solar: 0.103}` and `scale_non_renewables_to_match_surplus_msp = True`.
- "the transformer's 'renewable' category list also counts nuclear and gas-CCS". "an infeasible floor makes NemoMod return an all-zero grid with no error raised."

  — [CPAT_CPM_updates_0731.pptx, slides 3, 6](<MainProjectFolder/2. Other Documentation/CPAT_CPM_updates_0731.pptx>)

### Inferences
- A small-island-state application would rely on CCDR tab data (sector CAPEX/OPEX, private share, resilience flags) rather than an existing SISEPUEDE run. No SIDS SISEPUEDE run is present.
- The "50% on desal", "blue economy" and "tourism" lines suggest the extension's sector list should go beyond SISEPUEDE's IPCC sectors for island states.

### Gaps
- No internal document analyses SIDS, oil-import bills or PPA fiscal liabilities quantitatively.
- The CCDR data are flagged: "As these data have not been formally released, please do not share without letting me know" (David Groves, 19 Dec 2025). — [Investment Needs and Emissions data from CCDRs.msg](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/Investment Needs and Emissions data from CCDRs.msg>)

---

## Q7. What data fields are available that a new module could use (investment needs by sector, public/private share, capacity, macro-fiscal projections)?

### Takeaway
The building blocks exist but are uneven in coverage, units and provenance:
- CCDR investment compilations (47 economies; sector CAPEX/OPEX by decade; a private share for only 16 of them)
- an IRENA-style table of public renewable investment and capacity (203 countries, 2015–2021/22)
- an illustrative net-zero investment split table
- SISEPUEDE Morocco investment needs by sector
- an IMF macro-fiscal projection file for Morocco (growth, inflation, primary balance, interest, exchange rate, debt to 2035)

### Cited Findings
**IMF macro-fiscal projections (Morocco)**
- Sheets `R_hist` (1980–2024) and `R_project` (2025–2035), with columns `code, year, gdp_growth, inflation, primary_balance, interest_rate, exchange_rate, debt`.
- 2025 values: growth 3.905, inflation 2.30, primary balance −1.297, interest 3.706, exchange rate 9.90, debt 68.938. Debt in 2030: 65.104.
- 2031–2035 are flat: flows equal the 2025–2030 average (e.g. growth 3.663, primary balance −0.967) and debt is held at 65.104.

— [IMF-Macro-Fiscal-Projections-MAR.xlsx](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/IMF-Macro-Fiscal-Projections-MAR.xlsx>)

**CCDR investment master file (V7)**
- Sheets include `Summary`, `Global investment needs calc`, `IMF Debt to GDP ratio`, `Income group`, `Sectors`, and one tab per country (≈60 tabs, e.g. Uganda, Egypt, Morocco, Cabo Verde, Mauritius).
- `Summary` columns: `Code, Country, Debt to GDP, GDP per capita, Investments US$b, Investments (% of GDP), Investments Adaptation US$b, Investments Mitigation US$b, Investments Multiple Objective…, GDP (US$billion…), …(% of GDP)…, Investment type for graphing`.
- `Sectors` columns: `Code, Country, Sector, Included_Total, Included_Adaptation, Inlcuded_Mitigation, Included_Multiple_Objectives`.
- Country tab template: rows "CCDR scenario: total gross investments" by Power/Transport/Urban/Water/Agriculture/Forestry/Industry × CAPEX/OPEX; columns `Current, now-2030, 2031-2040, 2041-2050, 2051-2060, Share of investments covered by private sources of finance (with the right enabling environment)?, Scope of investments (e.g., power CAPEX: generation, distribution; power OPEX: fuel costs, co-benefits), Resilience objectives`; plus "CCDR baseline" and "Historic (share of GDP)" blocks.

— [Investments master fileV7-shared_w_SStretton.xlsx](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/Investments master fileV7-shared_w_SStretton.xlsx>) (the `CCDR_…` copy has the same structure plus a China tab)

**CCDR consistent mitigation table**
- "Constant 2020 US$ billion — cumulative, discounted at 6% over each country's CCDR modeling horizon (~2020–2050/60)".
- Examples: Egypt mitigation 29.7 + multiple-objective 119.5; Morocco 8.3; Pakistan 167.7 + 111.2.
- "A public/private split is recorded … for only 16 of 47 economies. These 16 account for ~0.8% of total mitigation investment. China alone is ~74% of mitigation and carries no split."

— [CCDR_mitigation_consistent_table.xlsx](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/CCDR_mitigation_consistent_table.xlsx>)

**Public renewable investment and capacity**
- Sheets:
  - "PubInvestments": "Public Investments (2020 million USD) by Country/area, Technology and Year", 2015–2021, 203 countries, 21 technologies from on-grid solar PV to nuclear, including fossil.
  - "Capacity": installed MW by technology, grid connection and year, 2015–2022.
  - "REShare": renewable share of capacity and generation.

— [PublicInvestmentsCapacityAndRenewableGenPC.xlsx](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/PublicInvestmentsCapacityAndRenewableGenPC.xlsx>)

**Illustrative net-zero investment table**
- Annual average % of GDP 2025–2060, split into Public / Public-private (revenue guarantee) / Private, and by sector (power generation, networks, transport, buildings, industry, AFOLU) and period.
- Countries: WLD, USA, EUU, CHN, BRA, ZAF, IND, IDN, EGY, NGA, SLE. Egypt: total 2.33% of GDP; public 0.45%, public-private 0.79%, private 1.10%.
- Labelled illustrative, not decision-grade.

— [net_zero_by_country.xlsx](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/net_zero_by_country.xlsx>)

**SISEPUEDE Morocco investment needs**
- "Low Emission Pathway" by sector, 2024–2050, units not labelled. 2050 examples: CCS 5.38, Transportation 2.12, Building 1.91, Solid waste 1.54, Industrial combustion 1.01.
- The companion "% of GDP" file carries the footnote "* Not sure if gross or net".

— [morocco_example_investment_needs_nominal.xlsx](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/Sisepuede Example Data/morocco_example_investment_needs_nominal.xlsx>); [morocco_example_investment_needs_gdp_intensity.xlsx](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/Sisepuede Example Data/morocco_example_investment_needs_gdp_intensity.xlsx>)

**Uganda SISEPUEDE wide output**
- `nemomod_entc_discounted_capital_investment_*` by plant, `nemomod_enst_*` storage, `totalvalue_enfu_fuel_consumed_*` by subsector and fuel, `gdp_mmm_usd`, `emission_co2e_subsector_total_*`.
- Sum of NemoMod discounted capital investment across plants and periods (raw units): baseline 31,848; NZ 66,872; NDC2-2020 43,888; NDC2-2025 42,798.

— [sisepuede_ide_run…csv](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413/sisepuede_ide_run_2025-10-29T19;49;25.722413.csv>)

**CPAT data shipped for the integration**
- `cpat_sisepuede` data files: `prices_dom.csv`, `prices_int.csv`, `elasticities.csv`, `weo.csv`, `wdi.csv`, `co_benefits_ffs.csv`, `air_data.csv`, `lcoe_tmp.csv`, `ic.csv`, `existing_ct.csv`, `existing_ets_*.csv` (EGY, MEA and global). — [README.txt](<MainProjectFolder/4. CPAT Repo/data files for cpat_sisepuede/README.txt>) and folder `MainProjectFolder/4. CPAT Repo/data files for cpat_sisepuede/new_data/`

### Inferences
- Units and discounting are inconsistent across sources:
  - CCDR tabs: discounted at 6%, mixed base years (2020/2023/2024/2015).
  - SISEPUEDE CBA: undiscounted, 2019 USD.
  - NemoMod capex: pre-discounted.
  - Morocco needs: unlabelled.
  - IMF projections: % and rates.

  Harmonising currency year, discounting and gross-vs-net should be an explicit first step of any new module.
- The public/private split is the weakest field: 16 of 47 CCDR economies, sector-level, and "with the right enabling environment". Any payer split in the extension will need assumptions or new data, e.g. by transformation type, as the bridge's destination mapping already does qualitatively.

### Gaps
- No BOOST, PEFA, PIMA or PIM-efficiency dataset is in the repository. The dashboard draws on PEFA but lives outside it.
- IMF projections are present only for Morocco. There is no Egypt, Uganda or SIDS file.
- The provenance of `PublicInvestmentsCapacityAndRenewableGenPC.xlsx` is not stated (its structure resembles IRENA/OECD public-finance data).

---

## Implications for designing an extension (concrete hooks and constraints)

### Takeaway
A fiscal and allocative-efficiency layer can attach at well-defined points:
- the CBA long table (`cba_results.csv`: `strategy_code × time_period × variable × value`)
- the bridge's money→dose conversion (`u_j = min(B_j/c_j, u_j,max)`) and its revenue-destination mapping
- CPAT's revenue-use shares and multipliers (`sh_i`, `m_i(k)`, `capt`)
- the planned debt equation (`d_{t+1}`, with `DC_t`)

It must respect SISEPUEDE's conventions:
- undiscounted strategy-minus-baseline flows
- costs negative
- 2019 USD
- PPP GDP
- one-at-a-time transformation costing
- NemoMod pre-discounted power capex
- no payer, financing or fiscal dimension

### Cited Findings (hooks)
**Hooks in the CBA output**
- **Unit of analysis:** rows keyed by `strategy_code`, `future_id`, `region`, `time_period` (+2015 = year), `variable` (`cb:<sector>:<category>:<sub>:<detail>`), `difference_variable` (physical driver), `difference_value`, `value` (US$; −cost / +benefit). — [cba_results.csv](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413/cba_results.csv>); [Latest SISEPUEDE Runs.msg](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/Latest SISEPUEDE Runs.msg>)
- **Category families available to map to payers and fiscal lines:** technical cost, technical savings, system cost, fuel cost, sector-specific fuel cost, and non-technical externalities (air pollution, health, congestion, road safety, ecosystem services, water, land and environmental pollution, crop/livestock/IPPU output value, consumer savings). — [cba_results.csv](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413/cba_results.csv>); [costs_benefits_ssp README](https://github.com/milocortes/costs_benefits_ssp)
- **Strategy and transformation codes** (`TX:<SECTOR>:<ACTION>`, strategy IDs 1000–6009) are the unit to which a public/private/household/firm cost share, an asset/non-asset flag, an asset life and a capex share would be attached. — [ATTRIBUTE_STRATEGY.csv](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413/ATTRIBUTE_STRATEGY.csv>)

**Hooks in the bridge**
- **Money→physical hook:** `u_j = min(B_j/c_j, u_j,max)` with `c_j` in "US$ bn per dose, 2022-2041". Each "destination may only pay for the cost–benefit rows that belong to it". The mapping is public investment → asset-leaving technical cost; current spending → programme cost; transfers and labour tax cuts → household share; corporate tax cuts → firm share. — [CPAT_CPM_Methodology_v0925.docx §3.5, §4](<MainProjectFolder/2. Other Documentation/CPAT_CPM_Methodology_v0925.docx>); [CPAT_CPM_bridge_map.pptx, slides 7, 11–12](<MainProjectFolder/1. Project Presentations/CPAT_CPM_bridge_map.pptx>)
- **Finance-a-target hook:** `R* = C/s_pi` and the revenue surface `R(L,s) = R_pi(L)·[1 + Σ_d s_d·β_d(L)]`. The non-unique pathway choice needs a rule ("least tax, least net cost, most GDP, most welfare"). — [CPAT_CPM_Methodology_v0925.docx §5](<MainProjectFolder/2. Other Documentation/CPAT_CPM_Methodology_v0925.docx>); [CPAT_CPM_bridge_map.pptx, slide 14](<MainProjectFolder/1. Project Presentations/CPAT_CPM_bridge_map.pptx>)

**Hooks in CPAT's macro side**
- Revenue shares on Dashboard P7–P11.
- Multipliers by instrument (`pit`, `cit`, `capt`, `gnfs`, `trns`, `exc`) and lag 0–19 (sheet `Multipliers`, MFMod medians; Base/Low/High).
- `fis.sp` (fiscal space), `fis.imp`, `fis.eff`, `gdp.eff`.
- Exported codes `mit.gdp.<pit|inv|cur|tra>.pct.2`, `mit.rev.new.usd.<1|2>`, `mit.nim.pow.<tech>.t.<1|2>`.

— [GDP_Method_v6_1.md](</home/user/CPAT-AI/cpat_excel/working_version/GDP_Method_v6_1.md>); [Equations_v6_1.md](</home/user/CPAT-AI/cpat_excel/working_version/Equations_v6_1.md>); [CPAT_CPM_Methodology_v0925.docx Annex](<MainProjectFolder/2. Other Documentation/CPAT_CPM_Methodology_v0925.docx>)

**Debt and fiscal-space hooks**
- `d_{t+1} = d_t(1+i_t)/(1+g_t+π_t) − pb_t + sfa_t + DC_t`, fed by `IMF-Macro-Fiscal-Projections-*.xlsx` (`gdp_growth, inflation, primary_balance, interest_rate, exchange_rate, debt`). — [Overview-CPAT-Sisepuede-LTS.pptx, slide 18](<MainProjectFolder/8. Archive/Overview-CPAT-Sisepuede-LTS.pptx>); [IMF-Macro-Fiscal-Projections-MAR.xlsx](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/IMF-Macro-Fiscal-Projections-MAR.xlsx>)
- Dashboard blocks for scoring fiscal space, delivery, cost of capital and financing risk. — [AIClimate-FiscalTools_v2.5.pptx](</home/user/CPAT-AI/Presentations - Overarching/AIClimate-FiscalTools_v2.5.pptx>)

**Discounting and financing hooks**
- The internal review already specifies:
  - CRF `A = I·r/(1−(1+r)^−n)` (eq. 4)
  - `WACC = D/V(r_f+π_c+π_j)(1−τ) + E/V·k^E` (eq. 5)
  - financial net `N^F = Σ(ΔF − ΔOM − A(WACC))` (eq. 6)
  - economic net `N^E = Σ(ΔF − ΔOM − A(r_s)) + CB + P^C·ΔE` (eq. 7), with r_s ≈ 6% and the World Bank shadow carbon price
  - "dual discount rate … gross capital output … financing layer: split investment into public and private, domestic and external … link it to a debt module".

  — [Global_Investment_Needs_SISEPUEDE.docx, method and A.4](<MethodologyReview/Global_Investment_Needs_SISEPUEDE.docx>)
- The CPAT power model already has WACC/CRF machinery (`CoC` sheet), PPA must-run shares and renewable subsidies, i.e. existing hooks for PPA/PPP fiscal liabilities in power. — [PowerModel_Method_v6_1.md](</home/user/CPAT-AI/cpat_excel/working_version/PowerModel_Method_v6_1.md>); [CPAT 1.0pre_459 sheet list](<CPAT Excel - UI and Working Version/CPAT 1.0pre_459_EGYMARMEX.xlsb>)

**Stated open design questions the extension can answer**
- "Separate running subsidies from upfront public investment, show how a carbon tax reduces each, and report dollars as well as marginal costs".
- "Up front Public Investment can pay technical capital cost — Not in".
- An "Optimization layer … Better tax level, investments, allocation".
- V3 "efficiency of public investment and energy fiscal costs and risks for finance ministries".

— [Slides_Oct-19th-WBside-Pathways_CPAT_proposal.pptx](<CPAT Excel - UI and Working Version/Slides_Oct-19th-WBside-Pathways_CPAT_proposal.pptx>); [FY27 Work Plan (CPM comments)](<MainProjectFolder/2. Other Documentation/Stephen_FY27_Work_Plan - Coded CPAT - and CPAT-CPM Elements_CPM_comments.docx>)

### Cited Findings (constraints the SISEPUEDE and bridge methodology imposes)
- **Undiscounted, strategy-minus-baseline flows;** the module "never discounts". Power capex and opex come pre-discounted from NemoMod (config `discount_rate: 0.0` vs documented 5%). Any layer must discount once, consistently. — [Global_Investment_Needs_SISEPUEDE.docx](<MethodologyReview/Global_Investment_Needs_SISEPUEDE.docx>); [cb_calculate.py](https://raw.githubusercontent.com/milocortes/costs_benefits_ssp/main/costs_benefits_ssp/cb_calculate.py)
- **Technical cost is not gross capex.** It "mix[es] capital, operations and avoided costs". Straight-line (0% interest) annualisation is embedded in some unit factors (EVs, trucks). Mode-shift infrastructure is uncosted. — [Global_Investment_Needs_SISEPUEDE.docx](<MethodologyReview/Global_Investment_Needs_SISEPUEDE.docx>)
- **No price response or macro feedback inside CPM.** Taxes enter only as written demand ratios; GDP is exogenous (PPP; 3.6× CPAT market dollars for Egypt). Investment does not raise growth unless an external model (CPAT multipliers, MFMod) does it. — [CPAT_CPM_bridge_map.pptx](<MainProjectFolder/1. Project Presentations/CPAT_CPM_bridge_map.pptx>); [CPAT_CPM_Methodology_v0925.docx §2.2](<MainProjectFolder/2. Other Documentation/CPAT_CPM_Methodology_v0925.docx>)
- **Transformations are costed one at a time** and assumed linear in dose. Interactions are handled by `cb_process_interactions` weights, which "do not match what the runs show" (heat pumps + insulation). Doses are capped at the largest measured, "never extrapolated". — [CPAT_CPM_Methodology_v0925.docx §3.5, §7.1](<MainProjectFolder/2. Other Documentation/CPAT_CPM_Methodology_v0925.docx>)
- **Never add CPAT and CPM benefits:** "both can value the same avoided fuel and pollution". — [CPAT_CPM_tool_walkthrough.pptx, slide 11](<MainProjectFolder/1. Project Presentations/CPAT_CPM_tool_walkthrough.pptx>)
- **Solver and data-integrity traps:**
  - "CPM's electricity model can fail without raising an error and return zeros"
  - infeasible renewable floors return an all-zero grid
  - "a family that stops summing to its original total makes CPM return fewer columns without raising an error"

  — [CPAT_CPM_Methodology_v0925.docx §3.6](<MainProjectFolder/2. Other Documentation/CPAT_CPM_Methodology_v0925.docx>); [CPAT_CPM_updates_0731.pptx](<MainProjectFolder/2. Other Documentation/CPAT_CPM_updates_0731.pptx>); [CPAT_CPM_bridge_map.pptx, slide 10](<MainProjectFolder/1. Project Presentations/CPAT_CPM_bridge_map.pptx>)
- **Horizons differ:** CPAT runs to 2041; CPM runs 2015–2050 (Uganda to 2070). "the response is held flat beyond 2041". — [CPAT_CPM_bridge_map.pptx, slide 5](<MainProjectFolder/1. Project Presentations/CPAT_CPM_bridge_map.pptx>)
- **Governance:** CPAT is WB proprietary and IMF-linked, and the Dirk Heine comment questions compatibility with IMF and data-provider agreements. The CCDR data are not formally released. — [Partnership_Agreement-Tec de Monterrey-Feb2026.docx](<MainProjectFolder/9. CPAT-LTS Project/Core Document and Example Data/More Project Documents/Partnership_Agreement-Tec de Monterrey-Feb2026.docx>); [Investment Needs and Emissions data from CCDRs.msg](<MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/Investment Needs and Emissions data from CCDRs.msg>)

### Inferences (design suggestions consistent with both models)
1. **Add a per-transformation "fiscal attribute table"** keyed on `TX:<SECTOR>:<ACTION>`, sitting outside SISEPUEDE. Fields:
   - capex share of technical cost
   - asset life
   - payer shares (state / SOE / household / firm), defaulting to the bridge's destination mapping
   - revenue-capture potential (user fees, tariffs)
   - fiscal line (capital spending / current spending / subsidy / tax expenditure / guarantee)

   Apply it to `cba_results.csv` rows to produce a "budget view" alongside the existing "economic view". This fills the gap the bridge deck names ("Splitting each lever's cost between state, household and firm … neither model holds today").
2. **Discount once, in the new layer**, with two rates: a social rate (≈6%) for the economic NPV and a WACC or sovereign cost of funds for the fiscal and financial view. Re-derive `entc` capex from undiscounted capacity × capital cost, rather than re-discounting `nemomod_entc_discounted_*`.
3. **Allocative-efficiency ranking:** use the existing one-at-a-time measurement, but with net benefit per public dollar, not technical cost per tonne:
   - (economic NPV incl. co-benefits) / (PV of net budget cost) per transformation
   - possibly with a marginal-cost-of-public-funds weight on the budget cost

   Feed the ranking into the bridge's `B_j` allocation and the planned optimisation layer. The Tornado/Whirlpool MAC files already provide standalone vs leave-one-out costs for interaction checks.
4. **Public spending efficiency (V3):** a PIMA/efficiency factor could scale the dose bought per dollar (e.g. `u_j = min(e·B_j/c_j, u_j,max)`) and/or CPAT's `capt` multiplier. Both slots exist; neither currently has an efficiency parameter.
5. **Debt and fiscal space (V2):** route the net budget flows (capex + opex − captured revenues − subsidy savings from CPAT `fis.sp`) into the `d_{t+1}` equation driven by `IMF-Macro-Fiscal-Projections-<ISO>.xlsx`. Use `DC_t` for disaster or adaptation costs, which suits SIDS.
6. **For SIDS,** start from CCDR tabs (sector CAPEX/OPEX, private share, desalination, blue economy, DRR) rather than SISEPUEDE runs. Add an import-bill line from `fuel_cost` / `sector_specific:fuel_cost` deltas valued at import parity, and PPA/CfD contingent liabilities using CPAT power-model PPA settings.

### Gaps
- There is no internal specification of how the bridge's US$/tCO2e and `c_j` costs were time-aggregated (undiscounted cumulative 2022–2041 is implied, not stated).
- There are no internal estimates of investment efficiency, user-fee recovery or MCPF, and no BOOST or PEFA extracts.
- No DIGNAD/DIGNAR/GIMF parameterisation exists anywhere internal. If the proposal relies on those models, their parameters must come from the external literature (covered by the other researcher).
