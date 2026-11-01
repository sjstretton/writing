# Carbon prices in industry and buildings as natural experiments: EU ETS (2005–), Swiss CO2 levy on heating fuels (2008–), French Contribution Climat-Énergie (2014–2018)

Research notes for the working paper "What carbon prices did: ten natural experiments". Compiled 1 November 2026. Every number below has a source link. "Derived" means I calculated it from the sourced inputs named next to it. **[VERIFY: …]** marks anything I could not confirm against a primary source. For each study, the references subsection says whether I read the **full text** or only the **abstract or metadata**.

**Emission factors and conventions used throughout**
- Heating oil (extra-light) and gas oil: **2.65 kg CO2/litre**. This is the factor in the Swiss customs levy table ([BAZG Anhang 2, valid from 1.1.2022](https://www.bazg.admin.ch/dam/en/sd-web/2A87XsPiKVSn/Anhang%202%20Berechnung%20der%20g%C3%BCltigen%20Abgabens%C3%A4tze%20auf%20Brennstoffen.pdf)) and matches the brief's 2.65.
- Heavy fuel oil: **3.17 t CO2/t** (same BAZG table, "Heizöl schwer").
- Natural gas: **0.202 t CO2/MWh on a net-calorific (NCV) basis**, as in the brief. Eurostat and French gas prices are quoted per MWh on a gross-calorific (GCV/PCS) basis, so I converted the factor to **0.182 t CO2/MWh GCV** (0.202 × 0.9017, assuming GCV/NCV ≈ 1.109 for natural gas). **[VERIFY: GCV/NCV ratio is a standard assumption, not taken from a source in this session.]** BAZG's own gas factor is 2.68 kg CO2 per kg of gas ([BAZG Anhang 2](https://www.bazg.admin.ch/dam/en/sd-web/2A87XsPiKVSn/Anhang%202%20Berechnung%20der%20g%C3%BCltigen%20Abgabens%C3%A4tze%20auf%20Brennstoffen.pdf)).
- Steam coal: 94.6 kg CO2/GJ × 25.12 GJ/t (6,000 kcal/kg net as received) = **2.376 t CO2 per tonne of coal**, about 0.34 t CO2/MWh. **[VERIFY: the 6,000 kcal/kg spec of the World Bank Richards Bay coal series is from my memory of the Pink Sheet definitions; the sheet itself was not printed in this session.]**
- French road fuels: **gazole 2.651 kg CO2/l and SP95-E5 2.287 kg CO2/l**, the factors the French carbon component is built on ([Fipeco, Ecalle, 30.09.2021, footnote 2](https://www.fipeco.fr/pdf/Carburants2021.pdf)). French domestic heating oil (fioul domestique) is assumed to use the gazole factor. That assumption matches the 2017 per-unit table, where fioul and gazole both carry 8.07 c€/l ([fr.wikipedia, CCE](https://fr.wikipedia.org/wiki/Contribution_climat-%C3%A9nergie)).
- Exchange rates: ECB annual averages ([ECB CHF/EUR](https://data-api.ecb.europa.eu/service/data/EXR/A.CHF.EUR.SP00.A?format=csvdata&startPeriod=2005); [ECB USD/EUR](https://data-api.ecb.europa.eu/service/data/EXR/A.USD.EUR.SP00.A?format=csvdata&startPeriod=2005)). EUA prices in US$ come from ICAP's own daily dollar conversion.

## 1. EU ETS: allowance price path and the implied % increase in industrial fuel costs

### Takeaway
The brief's price path is right in outline, with one correction. ICAP daily secondary-market data give annual means of about €21 (2005) and €17 (2006), a Phase I spot collapse to €0.66 (2007), €22 (2008, Phase II), **€13–14 (2009–2011)**, €7 (2012), €4.5–7.7 (2013–2017), €16–25 (2018–2020) and €53–86 (2021–2025). So the Phase II price sat mostly at €13–14 rather than €15–25 after 2008.

At these prices the full marginal carbon cost was:
- **Natural gas**: about 9–13% of the large-industry price in 2008–2010, 3–5% in 2012–2017, 20–23% in 2019–2020 and 20–33% in 2021–2025.
- **Heavy fuel oil**: similar shares to gas.
- **Coal**: a much larger share of the free-on-board coal price, from 18% to over 100% depending on the year.

Most industrial installations received free allowances, so these shares describe the marginal (opportunity) cost, not the average cash cost.

### Cited Findings
- **Price data source.** ICAP Allowance Price Explorer, EU ETS secondary-market daily series, 2005-03-09 to 2026-09-30 ([ICAP Allowance Price Explorer](https://allowancepriceexplorer.icapcarbonaction.com); [ICAP ETS prices page](https://icapcarbonaction.com/en/ets-prices)).
  - Each daily point carries US$, € and local-currency values. I pulled the data from the explorer's public `/api/systems` endpoint and computed annual means myself.
  - The series is Phase I spot until March 2008. Phase II values start on **2008-03-25**, so my 2008 mean uses only 25 March to December.
- **Cross-checks against other sources.**
  - My 2018 mean of €15.82 equals the "ICAP average 2018 price 15.82 euro" quoted in a search snippet (energynomics.ro, via search; not opened).
  - My 2019 mean of €24.88 is close to Agora Energiewende's €24.84 average 2019 EEX secondary-market price ([Agora chart Abb-27](https://www.agora-energiewende.org/fileadmin/Abbildungen/1810/Abb-27.pdf), via search snippet).
- **Peaks and troughs (ICAP daily, derived).**
  - Phase I high: **€29.78 on 18 April 2006** (€29.03 on 7 July 2005).
  - Phase I spot fell to **€0.01 by December 2007**.
  - Phase II high: **€28.75 on 1 July 2008**.
  - Phase III low: **€2.68 on 17 April 2013**.
  - Phase IV high: **€100.34 on 21 February 2023**.
- **Colmer et al. on Phase I and II prices.** "During Trading Phase I (from 2005 until 2007), permit prices first climbed to $37 before collapsing to less than $1 in early 2007. However, permit prices rebounded to around $21.35 ($2017) during Trading Phase II (between 2008 and 2012)" ([Colmer et al., CEP DP1728 rev. 2023, p. 1](https://cep.lse.ac.uk/pubs/download/dp1728.pdf)).
- **Dechezleprêtre et al. on Phase II prices.** They describe Phase II as a period in which "allowance prices fluctuated between €15 and €30" ([Dechezleprêtre, Nachtigall & Venmans 2023, JEEM, p. 5](https://researchonline.lse.ac.uk/id/eprint/117357)).
- **Penalties and Phase I cap.**
  - The excess-emissions penalty was **€40/t (2005–2007) and €100/t (from 2008)**.
  - Phase I issued about **2.2 billion tons** of permits a year across the then 25 member states, covering almost 50% of EU CO2 emissions.
  - Source: [Bayer & Aklin 2020, PNAS, p. 2](https://strathprints.strath.ac.uk/72023/1/Bayer_Aklin_PNAS_2020_The_European_Union_emissions_trading_system_reduced_CO2.pdf).
- **Reference fuel prices used for the % calculations.**
  - Gas: Eurostat `nrg_pc_203`, EU27_2020, band I4 (100,000–999,999 GJ/yr, i.e. large industrial users), excluding all taxes and levies, semi-annual, € per kWh ([Eurostat nrg_pc_203 API query](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nrg_pc_203?geo=EU27_2020&nrg_cons=GJ100000-999999&unit=KWH&tax=X_TAX&currency=EUR&lang=en)). Annual means in €/MWh: 2007 25.8; 2008 31.6; 2009 27.7; 2010 26.4; 2011 28.7; 2012 31.5; 2013 32.2; 2014 29.6; 2015 27.2; 2016 22.2; 2017 21.8; 2018 23.5; 2019 23.0; 2020 19.1; 2021 29.4; 2022 72.3; 2023 62.1; 2024 45.2; 2025 44.8. The series starts in 2007.
  - Coal: World Bank Pink Sheet "Coal, South African" (FOB Richards Bay), US$/t, annual: 2005 46.20; 2008 120.60; 2012 92.92; 2016 63.95; 2019 71.94; 2020 65.66; 2021 119.84; 2022 240.56; 2023 119.11; 2024 105.77 ([World Bank CMO historical annual data, updated 3 January 2025](https://thedocs.worldbank.org/en/doc/5d903e848db1d1b83e0ec8f744e55570-0350012021/related/CMO-Historical-Data-Annual.xlsx)).
  - Heavy fuel oil: EU Weekly Oil Bulletin, EU-weighted "Fuel oil – heavy, sulphur ≤1%", € per tonne, without taxes, annual mean of weekly data: 2005 267; 2008 413; 2012 606; 2016 288; 2019 445; 2022 697; 2024 615; 2025 587 ([DG ENER Weekly Oil Bulletin price history](https://energy.ec.europa.eu/document/download/906e60ca-8b6a-44e7-8589-652854d2fd3f_en?filename=Weekly_Oil_Bulletin_Prices_History_maticni_4web.xlsx)).
- **Opportunity cost of free allocation.** At €20/tCO2 with full pass-through of free-allowance opportunity costs, carbon costs as a share of gross value added would be: lime 57%, cement 40%, fertilisers and nitrogen compounds 63%, aluminium 10%, basic iron and steel 8%, paper and board 7%. These figures come from Directive 2009/29/EC, as cited by [Dechezleprêtre et al. 2023, p. 17](https://researchonline.lse.ac.uk/id/eprint/117357).

### Inferences
**Table 1.1 (derived): EUA price and the full marginal carbon cost as % of the pre-carbon fuel price to large industrial users.**

Method: carbon cost = EUA price × emission factor (see conventions at the top), divided by the reference fuel price above. Prices are nominal. "% increase" = carbon cost ÷ fuel price excluding carbon cost.

| Year | EUA €/t (ICAP annual mean) | EUA US$/t | Gas: carbon €/MWh GCV → % of I4 price ex-tax | Coal: carbon US$/t coal → % of SA FOB price | Heavy fuel oil: carbon €/t → % of EU HFO price ex-tax |
|---|---|---|---|---|---|
| 2005 | 20.71 | 25.29 | n/a (no Eurostat data) | 60.1 → 130% | 65.6 → 25% |
| 2006 | 17.33 | 21.53 | n/a | 51.2 → 101% | 54.9 → 18% |
| 2007 | 0.66 (Phase I spot) | 0.86 | 0.12 → 0% | 2.1 → 3% | 2.1 → 1% |
| 2008 | 22.45 (Phase II only) | 33.25 | 4.09 → 13% | 79.0 → 66% | 71.2 → 17% |
| 2009 | 13.15 | 18.41 | 2.40 → 9% | 43.7 → 68% | 41.7 → 13% |
| 2010 | 14.34 | 18.98 | 2.61 → 10% | 45.1 → 49% | 45.4 → 11% |
| 2011 | 12.94 | 18.08 | 2.36 → 8% | 43.0 → 37% | 41.0 → 8% |
| 2012 | 7.38 | 9.49 | 1.34 → 4% | 22.5 → 24% | 23.4 → 4% |
| 2013 | 4.47 | 5.94 | 0.81 → 3% | 14.1 → 18% | 14.2 → 3% |
| 2014 | 5.95 | 7.89 | 1.08 → 4% | 18.7 → 26% | 18.9 → 4% |
| 2015 | 7.68 | 8.52 | 1.40 → 5% | 20.2 → 36% | 24.4 → 7% |
| 2016 | 5.35 | 5.92 | 0.97 → 4% | 14.1 → 22% | 17.0 → 6% |
| 2017 | 5.83 | 6.63 | 1.06 → 5% | 15.7 → 18% | 18.5 → 5% |
| 2018 | 15.82 | 18.55 | 2.88 → 12% | 44.1 → 45% | 50.2 → 12% |
| 2019 | 24.88 | 27.84 | 4.53 → 20% | 66.2 → 92% | 78.9 → 18% |
| 2020 | 24.46 | 27.94 | 4.46 → 23% | 66.4 → 101% | 77.5 → 22% |
| 2021 | 52.76 | 62.25 | 9.61 → 33% | 147.9 → 123% | 167.2 → 35% |
| 2022 | 81.04 | 85.51 | 14.76 → 20% | 203.2 → 84% | 256.9 → 37% |
| 2023 | 85.51 | 92.45 | 15.58 → 25% | 219.7 → 184% | 271.1 → 44% |
| 2024 | 66.43 | 73.01 | 12.10 → 27% | 173.5 → 164% | 210.6 → 34% |
| 2025 | 74.35 | 83.89 | 13.54 → 30% | n/a (Pink Sheet file ends 2024) | 235.7 → 40% |

- **Phase means (ICAP daily, derived):**
  - Phase I spot 2005–2007: €12.29 (US$15.17).
  - Phase II, 25 March 2008 to 2012: €13.66 (US$19.00).
  - Phase III 2013–2017: €5.86. Phase III 2018–2020: €21.68. Phase III as a whole: €11.73.
  - Phase IV, 2021 to September 2026: €72.97 (US$81.09).
- **The 2007 figure is a special case.** The 2007 spot price measures expiring Phase I permits only. Firms planning for 2008 faced Phase II futures, which Colmer et al. put at "around $21.35 ($2017)" for Phase II as a whole ([CEP DP1728, p. 1](https://cep.lse.ac.uk/pubs/download/dp1728.pdf)). **[VERIFY: annual mean of Dec-2008 futures during 2007 not retrieved.]**
- **The coal shares are upper bounds.** They are measured against FOB export prices. Delivered prices in Europe (CIF ARA) include freight, so the true shares are lower. Coal shares exceed 100% in 2005–06, 2020–21 and 2023–24, which means the carbon cost exceeded the FOB price of the coal itself.
- **Free allocation separates marginal from average cost.** Through Phases I–II and much of Phase III, most manufacturing installations received free allowances. The table therefore gives the *marginal* (opportunity-cost) increase that should drive abatement, not the cash increase in average energy bills.

### Gaps
- No single official table of annual EUA averages since 2005 was found. Table 1.1 relies on my own averaging of ICAP daily data; ICAP's documentation of the exact contract used (spot or front-December futures) was not read. **[VERIFY: ICAP documentation notes.]**
- Eurostat industrial gas prices before 2007 (`nrg_pc_203_h`) were not available through the API, so 2005–2006 gas shares are missing.
- A European delivered coal price (API2 CIF ARA) and an industrial heavy-fuel-oil price including freight were not retrieved.

### References (full, with access status)
- International Carbon Action Partnership (ICAP). Allowance Price Explorer, EU ETS secondary-market series (system IDs 33 and 34), accessed 1 November 2026. https://allowancepriceexplorer.icapcarbonaction.com. **Data downloaded.**
- Eurostat. Gas prices for non-household consumers, bi-annual data (`nrg_pc_203`), updated 19 October 2026. **Data downloaded.**
- World Bank. Commodity Price Data (The Pink Sheet), annual nominal, updated 3 January 2025. **Data downloaded.**
- European Commission DG ENER. Weekly Oil Bulletin, price history 2005–2026. **Data downloaded.**

## 2. EU ETS: ex post evidence on emissions of regulated manufacturing and power installations

### Takeaway
Rigorous micro and sector studies converge on **roughly 10% (range 8–16%) lower emissions at regulated installations, concentrated in Phase II (2008–2012)**. Phase I effects are small or insignificant. None of the studies finds a measurable loss of output, employment or competitiveness.

Each study named in the brief was checked:
- **Dechezleprêtre, Nachtigall & Venmans (2023, JEEM 118): confirmed.** About −10% over 2005–2012 (−6% Phase I, not significant; −15% Phase II).
- **Colmer, Martin, Muûls & Wagner: confirmed, with corrections.** Published in **Review of Economic Studies, 2025, vol. 92(3)** (not 2024), with the published title using "System". Finding: −14% Phase I and −16.3% Phase II in French manufacturing.
- **Bayer & Aklin (2020, PNAS 117(16)): confirmed.** −8.1% (2005 start) to −11.5% (2008 start) in ETS sectors; 1.2 billion tonnes over 2008–2016 = 3.8% of total EU emissions.
- **Petrick & Wagner (2014, Kiel WP 1912): confirmed.** −0.25 to −0.28 log points in 2008–2010 in Germany; the abstract says "one-fifth". It is a working paper, not peer-reviewed.
- **Klemetsen, Rosendahl & Jakobsen (2020, Climate Change Economics 11(1)): confirmed.** Only a weak Phase II reduction, which Dechezleprêtre et al. report as about −30%.

### Cited Findings
**Dechezleprêtre, Nachtigall & Venmans (2023), JEEM 118, 102758**
- Headline: installation-level data "from national Polluting Emissions Registries in France, Netherlands, Norway and the United Kingdom point to a reduction in carbon emissions in the order of −10% between 2005 and 2012" ([DNV 2023, abstract, p. 1](https://researchonline.lse.ac.uk/id/eprint/117357)).
- Sensitivity range: "sensitivity tests pointing to effects between −7% and −16%". Most of the effect is in Phase II: "the impact is −6% for the first phase and −15% in the second phase" ([DNV 2023, p. 2](https://researchonline.lse.ac.uk/id/eprint/117357)).
- Method:
  - Matching on installation-level inclusion thresholds plus difference-in-differences.
  - Emissions results rest on **240 matched pairs** of ETS and non-ETS installations.
  - Poisson regressions give a treatment effect of −0.10 to −0.11, "roughly 10%… roughly 5 kt for the average installation" (Table 5).
  - By phase: 6% reduction in Phase I, not significant; 15% in Phase II, significant.
  - Source: [DNV 2023, pp. 2, 11](https://researchonline.lse.ac.uk/id/eprint/117357).
- Heterogeneity: the effect is strongest for large installations and in chemicals. "Under-allocated installations seem to have reduced emissions to a larger extent" ([DNV 2023, p. 2](https://researchonline.lse.ac.uk/id/eprint/117357)).
- Economic outcomes:
  - Based on 1,787 matched ETS firms across 31 countries.
  - The ETS "had no significant impact on profits and employment, and led to an increase in regulated firms' revenues and fixed assets".
  - Revenues were 15% higher (13–19% across specifications); fixed assets +8% (3–10%).
  - Source: [DNV 2023, abstract and pp. 17–18](https://researchonline.lse.ac.uk/id/eprint/117357).
- Context: "Between 2005 and 2012, verified emissions by regulated installations were reduced by 17% at constant scope" ([DNV 2023, p. 1](https://researchonline.lse.ac.uk/id/eprint/117357)).

**Colmer, Martin, Muûls & Wagner (2025), Review of Economic Studies 92(3): 1625–1660**
- Headline: the ETS "induced regulated manufacturing firms to reduce carbon dioxide emissions by 14-16% with no detectable contractions in economic activity. We find no evidence of outsourcing to unregulated firms or markets" ([CEP DP1728 rev. March 2023, abstract](https://cep.lse.ac.uk/pubs/download/dp1728.pdf)). The published abstract carries the same 14–16% figure ([RePEc record of RES 92(3):1625–1660](https://ideas.repec.org/a/oup/restud/v92y2025i3p1625-1660..html)).
- By phase: "regulated firms reduced emissions by 14% (p < 0.05) during Trading Phase I and by 16.3% (p < 0.05) during Trading Phase II" (Table 2) ([CEP DP1728, p. 18](https://cep.lse.ac.uk/pubs/download/dp1728.pdf)).
- Investment and intensity results ([CEP DP1728, p. 18](https://cep.lse.ac.uk/pubs/download/dp1728.pdf)):
  - Capital investment rose by 8.3% in Phase I and 10.5% in Phase II (both p < 0.1).
  - CO2 intensity of value added fell by 17.4% in Phase II (p < 0.01).
- Aggregate effect: "aggregate emissions would on average have been 5.4 million tonnes higher each year if there was no EU ETS" over 2005–2012. That is 28% of the aggregate reduction against 2004 emissions, or 47% against the pre-2005 trend ([CEP DP1728, p. 36](https://cep.lse.ac.uk/pubs/download/dp1728.pdf)).
- Data:
  - Matched difference-in-differences on French administrative data (EACEI energy survey, FICUS/FARE accounts, customs data).
  - The linked sample covers **4,201 firms emitting 61.4 Mt CO2 in 2000, 79.3%** of French industrial combustion emissions.
  - Source: [CEP DP1728, p. 17](https://cep.lse.ac.uk/pubs/download/dp1728.pdf).
- Leakage via imports: increased imports "could account for at most a 1.8% reduction in emissions intensity, accounting for at most 10% of the estimate in Trading Phase II" ([CEP DP1728, p. 22](https://cep.lse.ac.uk/pubs/download/dp1728.pdf)).
- Cost bound: marginal abatement costs "could not have exceeded $53 per tonne of CO2 ($2017)" ([CEP DP1728, p. 2](https://cep.lse.ac.uk/pubs/download/dp1728.pdf)).
- **Version difference.** DNV (2023) cite the 2022 working-paper version of Colmer et al. as finding 8–12%, "all of the impact" in Phase II ([DNV 2023, p. 5](https://researchonline.lse.ac.uk/id/eprint/117357)). The 2023 revision and the published RES article report 14–16% with effects in both phases. The paper should cite the published numbers.

**Bayer & Aklin (2020), PNAS 117(16): 8804–8812**
- Headline: "the EU ETS saved about 1.2 billion tons of CO2 between 2008 and 2016 (3.8%) relative to a world without carbon markets" ([Bayer & Aklin 2020, abstract](https://strathprints.strath.ac.uk/72023/1/Bayer_Aklin_PNAS_2020_The_European_Union_emissions_trading_system_reduced_CO2.pdf)).
- Table 1 average treatment effect on the treated, ETS sectors ([Bayer & Aklin 2020, p. 4](https://strathprints.strath.ac.uk/72023/1/Bayer_Aklin_PNAS_2020_The_European_Union_emissions_trading_system_reduced_CO2.pdf)):
  - Treatment starting 2005: **−8.1%** (95% CI −13.2% to −1.7%).
  - Treatment starting 2008: **−11.5%** (95% CI −16.9% to −5.4%).
- The 1.2 Gt is "a reduction of about 7.5% [relative to covered emissions] or roughly 3.8% compared to the EU's total emissions". By sector, "emissions decreased between 20 and 25% against the counterfactual in all sectors" (energy, metals, minerals, chemicals; Fig. 3) ([Bayer & Aklin 2020, p. 6](https://strathprints.strath.ac.uk/72023/1/Bayer_Aklin_PNAS_2020_The_European_Union_emissions_trading_system_reduced_CO2.pdf)).
- Method:
  - Generalised synthetic control with interactive fixed effects.
  - Data: the EU Sectoral Emissions Data (EUSED), which combines EUTL and UNFCCC inventory data.
  - The counterfactual is built from non-ETS sectors that were themselves partly regulated under the Effort Sharing Decision, so the estimates are "conservative".
  - The estimate is "an upper bound for the global effect" because of possible leakage.
  - Source: [Bayer & Aklin 2020, pp. 4, 6](https://strathprints.strath.ac.uk/72023/1/Bayer_Aklin_PNAS_2020_The_European_Union_emissions_trading_system_reduced_CO2.pdf).

**Petrick & Wagner (2014), Kiel Working Paper 1912 (working paper, not peer-reviewed)**
- Abstract: "the policy caused treated firms to abate one-fifth of their CO2 emissions between 2007 and 2010 relative to non-treated firms… predominantly by improving energy efficiency and by curbing the consumption of natural gas and petroleum products, but not electricity use. We find no evidence that emissions trading lowered employment, turnover or exports" ([Petrick & Wagner 2014, abstract](https://www.econstor.eu/bitstream/10419/94357/1/781557828.pdf)).
- Table 3, change in log CO2 ([Petrick & Wagner 2014, pp. 16–17](https://www.econstor.eu/bitstream/10419/94357/1/781557828.pdf)):
  - **Phase I (2005–2007): 0.00 / 0.02 / 0.03**, not significant.
  - **Phase II (2008–2010): −0.28 / −0.25 / −0.26** (all p < 0.05), estimated by nearest-neighbour 1:1, nearest-neighbour 1:20 and reweighted OLS.
  - Sample: 408 treated firms and 23,908 controls.
  - Carbon intensity of gross output fell by 0.18–0.30 log points in Phase II.
- Fuel use in Phase II: non-electricity fuels fell by 0.81–0.87 log points; natural gas by −0.21 to −0.33; oil by −0.45 to −0.56. Gross output rose 4–7% ([Petrick & Wagner 2014, pp. 19, 28](https://www.econstor.eu/bitstream/10419/94357/1/781557828.pdf)).
- Data: German production census (AFiD-Panel Industriebetriebe 1998–2010), plants with ≥20 employees.

**Klemetsen, Rosendahl & Jakobsen (2020), Climate Change Economics 11(1), 2050006**
- Abstract (2016 SSB Discussion Paper 833 version): the authors find a weak tendency of emissions reductions among Norwegian plants in the second phase, but not in other phases. They find no significant effect on emissions intensity in any phase, and positive effects on value added and productivity in Phase II, possibly due to free allowances and pass-through ([SSB DP 833 page](https://www.ssb.no/en/forskning/discussion-papers/the-impacts-of-the-eu-ets-on-norwegian-plants-environmental-and-economic-performance)).
- Magnitude: DNV (2023) summarise it as "weak evidence that regulated plants may have reduced emissions by a large amount (−30%) in the EU ETS′ second phase" using plant data for 2001–2013 ([DNV 2023, p. 5](https://researchonline.lse.ac.uk/id/eprint/117357)).

**Other single-country and early studies (as summarised by DNV 2023, p. 5)**
- Phase I aggregate studies: EU-wide reductions of 2.5–5% (Ellerman & Buchner 2008; Anderson & Di Maria 2011; Ellerman et al. 2010); Germany 5% (Ellerman & Feilhauer 2008); UK electricity 17% (McGuinness & Ellerman 2008) ([DNV 2023, p. 5](https://researchonline.lse.ac.uk/id/eprint/117357)).
- Lithuania (Jaraite & Di Maria 2016): "no reductions in emissions". UK (Calel 2020): no improvement in firms' carbon intensity over 2005–2012 ([DNV 2023, p. 5](https://researchonline.lse.ac.uk/id/eprint/117357)).

**Reviews and meta-analyses (EU ETS-specific numbers)**
- Döbbeling-Hildebrandt et al. (2024), Nature Communications 15, 4147:
  - EU ETS average treatment effect **−7.3%** (95% CI −10.5% to −4.0%), against an all-scheme average of −10.4% (95% CI −11.9% to −8.9%).
  - 13 of the 80 included studies are on the EU ETS.
  - Significant reductions across schemes range from "–5% to –21%… (–4% to –15% after correcting for publication bias)".
  - Source: [Döbbeling-Hildebrandt et al. 2024](https://www.nature.com/articles/s41467-024-48512-w).
- Green (2021), Environmental Research Letters 16(4), 043004: for the EU ETS, "annual emissions reductions (i.e. across all sectors) range between 0% and 1.5% per year". Across schemes, 0–2% per year ([Green 2021](https://iopscience.iop.org/article/10.1088/1748-9326/abdae9)).
- Martin, Muûls & Wagner (2016), REEP 10(1): 129–148: reviews ex post evidence on regulated industrial and power firms under three headings (emissions, economic performance and competitiveness, innovation) ([Mannheim repository record](https://madoc.bib.uni-mannheim.de/40175/)).

### Inferences
- **For the paper's table.** A defensible headline is "EU ETS, manufacturing and power, 2005–2012: about −10% (range −8% to −16%) at regulated installations relative to matched unregulated ones; nearly all in Phase II at €13–22/t." The key estimates are:
  - Bayer & Aklin: −11.5% for 2008–2016 in ETS sectors.
  - DNV: −15% in Phase II.
  - Colmer et al.: −16% in Phase II.
  - Petrick & Wagner: about −22% to −24% (exp(−0.25) − 1 to exp(−0.28) − 1, derived) in 2008–2010.
- **Combining effects with price changes.** Effects of 10–16% coincided with marginal fuel-cost increases of about 8–13% for gas, 8–17% for heavy fuel oil and 37–68% for coal (Table 1.1, 2008–2011). The implied response per % price increase is high relative to standard energy-price elasticities. That is consistent with Bayer & Aklin's argument that anticipated stringency (expected future scarcity), not the spot price, drove abatement. This is an interpretation, not a measured elasticity.
- **Leakage.** The micro studies find no output or employment losses, Colmer et al. bound import-based leakage at ≤10% of the Phase II effect, and Bayer & Aklin find reductions in immobile sectors such as power. Together these suggest the local reductions were mostly real reductions rather than relocation.

### Gaps
- No ex post micro study with installation-level controls for **Phase III (2013–2020) or Phase IV (2021–)** was found in this search. The micro evidence stops in 2012–2013 for DNV, Colmer et al. and Klemetsen et al. Bayer & Aklin's sector panel runs to 2016.
- **Power-sector-specific** quasi-experimental estimates for the EU ETS (as distinct from UK Carbon Price Support studies) were not searched separately. Gugler, Haxhimusa & Liebensteiner (2021, JEEM 106, 102405) appears in the Döbbeling-Hildebrandt reference list ([Nature Communications 2024](https://www.nature.com/articles/s41467-024-48512-w)) but was not read.
- The exact per-tonne price elasticity of emissions cannot be backed out of these studies. Döbbeling-Hildebrandt et al. flag the price elasticity of emissions reductions as an evidence gap ([Nature Communications 2024, abstract](https://www.nature.com/articles/s41467-024-48512-w)).

### References (full, with access status)
- Dechezleprêtre, A., Nachtigall, D. & Venmans, F. (2023). The joint impact of the European Union emissions trading system on carbon emissions and economic performance. *Journal of Environmental Economics and Management*, 118, 102758. https://doi.org/10.1016/j.jeem.2022.102758. **Full text read** (published version, CC BY, LSE Research Online). Page numbers are the article's own (PDF page minus 1). Earlier version: OECD Economics Department WP 1515, ECO/WKP(2018)63.
- Colmer, J., Martin, R., Muûls, M. & Wagner, U. J. (2025). Does pricing carbon mitigate climate change? Firm-level evidence from the European Union Emissions Trading System. *Review of Economic Studies*, 92(3), 1625–1660. https://doi.org/10.1093/restud/rdae055. **Read the full text of CEP Discussion Paper 1728 (revised March 2023, titled "…Emissions Trading Scheme"); the published RES version was seen as abstract and metadata only.** Page numbers above are the DP's printed pages. **[VERIFY: table and page numbers in the published RES version.]**
- Bayer, P. & Aklin, M. (2020). The European Union Emissions Trading System reduced CO2 emissions despite low prices. *PNAS*, 117(16), 8804–8812. https://doi.org/10.1073/pnas.1918128117. **Full text read** (Strathprints copy of the "PNAS Latest Articles" version, pp. 1–9; journal page = 8803 + page, so Table 1 is on journal p. 8807 **[VERIFY]**).
- Petrick, S. & Wagner, U. J. (2014). The impact of carbon trading on industry: Evidence from German manufacturing firms. Kiel Working Paper No. 1912, Kiel Institute for the World Economy, March 2014. https://hdl.handle.net/10419/94357. **Full text read.** No journal version found **[VERIFY]**.
- Klemetsen, M. E., Rosendahl, K. E. & Jakobsen, A. L. (2020). The impacts of the EU ETS on Norwegian plants' environmental and economic performance. *Climate Change Economics*, 11(1), 2050006. https://doi.org/10.1142/S2010007820500062. **Abstract only** (the 2016 SSB DP 833 page); the −30% magnitude is taken from DNV (2023).
- Martin, R., Muûls, M. & Wagner, U. J. (2016). The impact of the European Union Emissions Trading Scheme on regulated firms: What is the evidence after ten years? *Review of Environmental Economics and Policy*, 10(1), 129–148. https://doi.org/10.1093/reep/rev016. **Abstract and metadata only.**
- Döbbeling-Hildebrandt, N., Miersch, K., Khanna, T. M., Bachelet, M., Bruns, S. B., Callaghan, M., Edenhofer, O., Flachsland, C., Forster, P. M., Kalkuhl, M., Koch, N., Lamb, W. F., Ohlendorf, N., Steckel, J. C. & Minx, J. C. (2024). Systematic review and meta-analysis of ex-post evaluations on the effectiveness of carbon pricing. *Nature Communications*, 15, 4147. https://doi.org/10.1038/s41467-024-48512-w. **Full text read** (HTML).
- Green, J. F. (2021). Does carbon pricing reduce emissions? A review of ex-post analyses. *Environmental Research Letters*, 16(4), 043004. https://doi.org/10.1088/1748-9326/abdae9. **Read the abstract and most of the body** (about 100,000 of 114,000 characters).

## 3. Switzerland's CO2 levy on heating fuels: rate path, levy per litre and per MWh, and share of the retail price

### Takeaway
The brief's rate path is confirmed by the customs authority's own chronology:
- CHF 12/t (2008–09), 36 (2010–13), 60 (2014–15), 84 (2016–17), 96 (2018–21) and 120 (from 2022).
- On heating oil that is **3.18, 9.55, 15.90, 22.26, 25.44 and 31.80 Rp per litre** (excluding VAT).

Against annual heating-oil retail prices (3,001–6,000 litre purchases), the levy including VAT made up:
- about **3–5% of the retail price in 2008–09**, about **10–12% in 2010–13**, **17–23% in 2014–15**, **29–40% in 2016–21** and **25–36% in 2022–25**;
- equivalently, about +3% to +65% over the levy-free price, depending on the year.

Levies on gas are smaller per unit of energy: about CHF 2.4/MWh at CHF 12 up to CHF 24/MWh at CHF 120.

### Cited Findings
- **Levy per 1,000 litres of extra-light heating oil (CHF)**, from the BAZG chronology ([BAZG T 4.9](https://www.bazg.admin.ch/dam/de/sd-web/9yMvuZ964tce/T%204.9%20Chronologie%20der%20Z%C3%B6lle%2C%20Min%C3%B6St%20und%20CO2-Abgabe%20%20auf%20Brennstoffen.pdf)):
  - 31.80 (1.1.2008–31.12.2009)
  - 95.50 (2010–2013)
  - 159.00 (2014–2015)
  - 222.60 (2016–2017)
  - 254.40 (2018–2021)
  - 318.00 (from 1.1.2022)
- **Levy per 1,000 kg of natural gas (CHF)**, same table: 30.70; 92.10; 153.60; 216.70; 255.40; 321.60 ([BAZG T 4.9](https://www.bazg.admin.ch/dam/de/sd-web/9yMvuZ964tce/T%204.9%20Chronologie%20der%20Z%C3%B6lle%2C%20Min%C3%B6St%20und%20CO2-Abgabe%20%20auf%20Brennstoffen.pdf)).
- **Calculation basis.** "Bei der Verbrennung von 1 Liter Heizöl extraleicht entstehen 2.65 kg CO2; bei einem Ansatz von Fr. 120.- je Tonne CO2 beträgt die Abgabe je Liter 31.80 Rp." Natural gas: 2.68 kg CO2 per kg, giving 32.16 Rp/kg at CHF 120 ([BAZG Anhang 2, 05.01.2022](https://www.bazg.admin.ch/dam/en/sd-web/2A87XsPiKVSn/Anhang%202%20Berechnung%20der%20g%C3%BCltigen%20Abgabens%C3%A4tze%20auf%20Brennstoffen.pdf)).
- **Rate path in CHF/t.** The levy was CHF 12/tCO2eq in 2008, then "CHF 36 in 2010, CHF 60 in 2014, CHF 84 in 2016 and CHF 96 in 2018, with a legal potential maximum of CHF 120" ([Ott & Weber, IRENE WP 18-09, p. 2](https://www5.unine.ch/RePEc/ftp/irn/pdfs/WP18-09.pdf)). The rate rose because interim targets were missed ([FOEN fact sheet 2018, p. 1](https://www.bafu.admin.ch/dam/en/sd-web/OhnKjWv6AJ-t/Faktenblatt%20Evaluation%20CO2-Abgabe%20(Update%202018)_EN.pdf)). The CHF 120 rate applies from 1 January 2022 ([BAZG Anhang 2](https://www.bazg.admin.ch/dam/en/sd-web/2A87XsPiKVSn/Anhang%202%20Berechnung%20der%20g%C3%BCltigen%20Abgabens%C3%A4tze%20auf%20Brennstoffen.pdf)).
- **Per-volume table in Francescutto & Mathys (2022).** Light oil (CHF/100 L): 3 / 10 / 15.8 / 22.2 / 25.4. Natural gas (CHF/100 m3): 2.5 / 7.4 / 12.4 / 17.4 / 19.8, for 2008–09 / 2010–13 / 2014–15 / 2016–17 / 2018–20 (Table 1) ([Francescutto & Mathys 2022, Energies, p. 3](https://www.mdpi.com/1996-1073/15/9/3019)).
- **Levy share of the price, 2015.** "In 2015, with a tax rate of CHF 60/tCO2, this led to a price increase of CHF 16 for 100 liters of light oil. A hypothetical household buying 3000 L of light oil would therefore have paid CHF 480 in CO2 levy, which corresponded to 21% of the total price of CHF 2200 for this amount of light oil" ([Francescutto & Mathys 2022, pp. 11–12](https://www.mdpi.com/1996-1073/15/9/3019)).
- **Retail price and taxes, January 2022.** Average extra-light heating-oil price (FSO consumer price index, 3,001–6,000 litre purchases) was **CHF 0.959/l**. Total taxes and levies were **CHF 0.312/l, i.e. 32.6% of the sales price** ([BAZG T 4.3, Stand Januar 2022](https://www.bazg.admin.ch/dam/de/sd-web/jcAi9J63UHHV/T%204.3%20Fiskalbelastungs-%20und%20Preisvergleich%20mit%20den%20L%C3%A4ndern%20der%20EU.pdf)). The levy rose to 31.80 Rp/l only on 1 January 2022, so the January index still partly reflects the 25.44 Rp rate.
- **Annual heating-oil prices.** Liechtenstein Office of Statistics, table 552.101, annual average heating-oil price, 3,001–6,000 litres, CHF per 100 l ([LLV eTab 552.101](https://etab.llv.li/PXWEb/pxweb/en/eTab/etab__Raum,%20Umwelt%20und%20Energie__Energiepreise/552.101.px)):
  - 2007 80.64; 2008 109.59; 2009 68.90; 2010 85.41; 2011 98.03; 2012 103.90; 2013 100.46; 2014 99.00; 2015 74.22; 2016 69.97; 2017 78.92;
  - 2018 95.52; 2019 90.53; 2020 69.42; 2021 85.42; 2022 138.82; 2023 115.03; 2024 104.58; 2025 95.94.
  - The 2015 value (74.22) matches the Swiss household example in Francescutto & Mathys (CHF 2,200 ÷ 3,000 l = 73.3).
- **Who pays.** Large greenhouse-gas-intensive companies in the ETS, and companies with reduction commitments, are exempt ([FOEN fact sheet 2018, p. 1](https://www.bafu.admin.ch/dam/en/sd-web/OhnKjWv6AJ-t/Faktenblatt%20Evaluation%20CO2-Abgabe%20(Update%202018)_EN.pdf)). Households cannot avoid it on fossil heating fuels ([Ott & Weber WP 18-09, p. 2](https://www5.unine.ch/RePEc/ftp/irn/pdfs/WP18-09.pdf)).
- **Revenue use.** "About two-thirds are redistributed to households and firms, while the remaining third is used to finance a building renovation programme and a technology fund" ([Ott & Weber WP 18-09, p. 2](https://www5.unine.ch/RePEc/ftp/irn/pdfs/WP18-09.pdf)).

### Inferences
**Table 3.1 (derived): Swiss CO2 levy on heating oil.**
- Columns:
  - Levy including VAT = BAZG levy × (1 + VAT). Swiss VAT was 7.6% (2008–10), 8.0% (2011–17), 7.7% (2018–23) and 8.1% (2024–25). **[VERIFY: that VAT is charged on the CO2 levy. Standard Swiss practice, not confirmed in a source this session.]**
  - Share = levy incl. VAT ÷ retail price.
  - % increase = levy incl. VAT ÷ (retail price − levy incl. VAT).
  - Gas column = rate × 0.202 t/MWh (NCV).
  - EUR and US$ conversions use ECB annual rates.
- **Caveat on prices.** Retail prices are Liechtenstein's annual series, used because the Swiss FSO annual series was not retrievable. Liechtenstein's prices should track Swiss ones under the customs union. **[VERIFY: that Liechtenstein applies the identical CO2 levy; plausible under the customs treaty but not confirmed.]**

| Year | Levy CHF/t | ≈€/t | ≈US$/t | Heating oil levy Rp/l (BAZG) | incl. VAT Rp/l | Retail CHF/100 l | Levy share of retail price | % increase vs levy-free price | Gas levy CHF/MWh (derived) |
|---|---|---|---|---|---|---|---|---|---|
| 2008 | 12 | 7.6 | 11.1 | 3.18 | 3.42 | 109.59 | 3.1% | 3.2% | 2.42 |
| 2009 | 12 | 7.9 | 11.1 | 3.18 | 3.42 | 68.90 | 5.0% | 5.2% | 2.42 |
| 2010 | 36 | 26.1 | 34.6 | 9.55 | 10.28 | 85.41 | 12.0% | 13.7% | 7.27 |
| 2011 | 36 | 29.2 | 40.7 | 9.55 | 10.31 | 98.03 | 10.5% | 11.8% | 7.27 |
| 2012 | 36 | 29.9 | 38.4 | 9.55 | 10.31 | 103.90 | 9.9% | 11.0% | 7.27 |
| 2013 | 36 | 29.2 | 38.8 | 9.55 | 10.31 | 100.46 | 10.3% | 11.4% | 7.27 |
| 2014 | 60 | 49.4 | 65.6 | 15.90 | 17.17 | 99.00 | 17.3% | 21.0% | 12.12 |
| 2015 | 60 | 56.2 | 62.3 | 15.90 | 17.17 | 74.22 | 23.1% | 30.1% | 12.12 |
| 2016 | 84 | 77.1 | 85.3 | 22.26 | 24.04 | 69.97 | 34.4% | 52.3% | 16.97 |
| 2017 | 84 | 75.6 | 85.4 | 22.26 | 24.04 | 78.92 | 30.5% | 43.8% | 16.97 |
| 2018 | 96 | 83.1 | 98.2 | 25.44 | 27.40 | 95.52 | 28.7% | 40.2% | 19.39 |
| 2019 | 96 | 86.3 | 96.6 | 25.44 | 27.40 | 90.53 | 30.3% | 43.4% | 19.39 |
| 2020 | 96 | 89.7 | 102.4 | 25.44 | 27.40 | 69.42 | 39.5% | 65.2% | 19.39 |
| 2021 | 96 | 88.8 | 105.0 | 25.44 | 27.40 | 85.42 | 32.1% | 47.2% | 19.39 |
| 2022 | 120 | 119.4 | 125.8 | 31.80 | 34.25 | 138.82 | 24.7% | 32.8% | 24.24 |
| 2023 | 120 | 123.5 | 133.5 | 31.80 | 34.25 | 115.03 | 29.8% | 42.4% | 24.24 |
| 2024 | 120 | 126.0 | 136.4 | 31.80 | 34.38 | 104.58 | 32.9% | 49.0% | 24.24 |
| 2025 | 120 | 128.1 | 144.7 | 31.80 | 34.38 | 95.94 | 35.8% | 55.8% | 24.24 |

- **Check against Francescutto & Mathys.** My 2015 share (23.1% including VAT) is consistent with their 21% (levy excluding VAT ÷ total price).
- **Size relative to other cases.** Since 2016 the Swiss levy is among the largest carbon-price-driven increases in a household fuel price in any of the paper's cases: roughly +40–65% on heating oil.

### Gaps
- **Swiss natural-gas retail prices** (FSO or SFOE annual, Rp/kWh) were not retrieved, so the gas levy's share of the retail price is not computed. At CHF 120 the gas levy is about 2.4 Rp/kWh (derived).
- The **official Swiss FSO annual heating-oil price series** was not reached; it appears only behind Statista's paywall. The Liechtenstein series is a proxy.

### References (full, with access status)
- Federal Office for Customs and Border Security (BAZG). T 4.9 *Chronologie der Zölle, Mineralölsteuer und CO2-Abgabe auf Brennstoffen*; *Anhang 2: CO2-Abgabe auf Brennstoffen – Berechnung der Abgabesätze, gültig ab 01.01.2022* (05.01.2022); T 4.3 *Fiskalbelastungs- und Preisvergleich mit den Ländern der EU* (Stand Januar 2022). **All three read in full.**
- Amt für Statistik Liechtenstein. Table 552.101 *Heating oil prices (annual average) by quantity purchased*, accessed 1 November 2026. **Data downloaded.**

## 4. Switzerland's CO2 levy: ex post evidence on heating-fuel emissions

### Takeaway
The official FOEN evaluation, carried out by Ecoplan and combining an econometric time-series model with a general-equilibrium model, attributes:
- **0.8–1.8 Mt CO2 in 2015**, which is **4.3–9.6% of about 17 Mt** of levy-relevant fuel emissions;
- **4.1–8.6 Mt cumulatively over 2005–2015**;
- a "net" effect, after removing the building programme and target agreements, of **about 1.3 Mt in 2015 and 6.9 Mt cumulatively**;
- about three-quarters of the effect to households (buildings).

Independent micro studies are mixed:
- **Francescutto & Mathys (2022, Energies)** find **no effect at CHF 12–36** and **−12% to −14% heating-fuel demand for house owners at CHF 60–84** (2014–2017 vs 2006–2007).
- **Fauceglia et al. (2020 WP)** find firm CO2 down **3% (2010–12) and up to 8% (2013–15)**.
- **Ott & Weber (2022, Energy Policy)** find **no short-run household response** to the 2016 increase.
- A 2025 synthetic-control working paper (Schäfer) finds **−6.5% per year** in residential emissions over 2008–2021.

### Cited Findings
**FOEN / Ecoplan evaluation (official, model-based counterfactual on observed data)**
- Methods: three studies.
  - Ecoplan, EPFL & FHNW (2015) and Ecoplan (2017) estimate "the overall effect of the levy from a top-down perspective" with "an econometric model (time-series approach) and a general-equilibrium model". The equilibrium model captures "immediate, short-term effects"; the time-series model "also includes medium to longer-term effects".
  - TEP Energy & Rütter Soceco (2016) surveyed about 4,000 companies.
  - Source: [FOEN fact sheet, 19 Feb 2018, p. 2](https://www.bafu.admin.ch/dam/en/sd-web/OhnKjWv6AJ-t/Faktenblatt%20Evaluation%20CO2-Abgabe%20(Update%202018)_EN.pdf).
- Headline: "the cumulative total impact for the period 2005-2015 is 4.1 to 8.6 million tonnes CO2… In 2015, the impact was 0.8 to 1.8 million tonnes CO2. Measured by the levy-relevant CO2 emissions from fossil thermal fuels, which amounted to around 17 million tonnes in 2015, this corresponds to a reduction of 4.3 to 9.6 percent. Around three quarters of the impacts are produced by households (buildings), and around one quarter by the economy" ([FOEN fact sheet 2018, p. 2](https://www.bafu.admin.ch/dam/en/sd-web/OhnKjWv6AJ-t/Faktenblatt%20Evaluation%20CO2-Abgabe%20(Update%202018)_EN.pdf)).
- Mechanism: "The primary driver of emission reductions is the substitution of heating oil with less CO2-intensive energy sources (natural gas and renewables)" ([FOEN fact sheet 2018, p. 3](https://www.bafu.admin.ch/dam/en/sd-web/OhnKjWv6AJ-t/Faktenblatt%20Evaluation%20CO2-Abgabe%20(Update%202018)_EN.pdf)).
- Net of other instruments: the econometric figures "include the effects of other measures… [and] therefore overestimate the impact". After deducting the building programme and target agreements, "the 'net effect' of the CO2 levy in 2015 is still around 1.3 million tonnes CO2. The cumulative 'net effect' over the entire period 2005-2015 is 6.9 million tonnes CO2" ([FOEN fact sheet 2018, p. 4](https://www.bafu.admin.ch/dam/en/sd-web/OhnKjWv6AJ-t/Faktenblatt%20Evaluation%20CO2-Abgabe%20(Update%202018)_EN.pdf)).
- Household-only figure for 2015: Francescutto & Mathys summarise Ecoplan (2017) as a reduction for households "of between 0.6 (3.2%, short-term effect) and 1.4 (7.2%, long-term effect) million tonnes" ([Francescutto & Mathys 2022, p. 5](https://www.mdpi.com/1996-1073/15/9/3019)).
- Earlier 2015 study (data to 2013): cumulative 2.5–5.4 Mt CO2 to 2013, and 0.5–1.2 Mt in 2013. This comes from a search-engine summary of [Ecoplan/EPFL/FHNW 2015](https://www.Bafu.admin.ch/dam/bafu/de/dokumente/klima/externe-studien-berichte/wirkungsabschaetzungco2-abgabemodellrechnungen.pdf.download.pdf/wirkungsabschaetzungco2-abgabemodellrechnungen.pdf). **[VERIFY: the PDF returned 404; numbers not confirmed in the document.]**

**Francescutto & Mathys (2022), Energies 15(9), 3019 (peer-reviewed, open access)**
- Data and method: Swiss Household Budget Survey 2006–2017, owners only (house owners n = 4,254; flat owners n = 4,387). Before–after regressions with cantonal, month and socio-demographic controls and heating degree days, plus pseudo-panel regressions ([Francescutto & Mathys 2022, abstract and Table 2](https://www.mdpi.com/1996-1073/15/9/3019)).
- Abstract: "No significant effects in the first two policy periods of 2008–2013 were found. Over the period of 2014–2017, a significant reduction in house owners' heating fuel demand of up to 14% with respect to 2006–2007 was detected… A significant CO2 levy semielasticity of heating fuel demand of −1.3% for house owners was further estimated" ([Francescutto & Mathys 2022, abstract](https://www.mdpi.com/1996-1073/15/9/3019)).
- Table 2, preferred column (3), house owners, log heating-fuel demand ([Francescutto & Mathys 2022, p. 11](https://www.mdpi.com/1996-1073/15/9/3019)):
  - CHF 12 (2008–09): −0.01 (s.e. 0.05)
  - CHF 36 (2010–13): −0.05 (0.05)
  - CHF 60 (2014–15): **−0.12\*\*** (0.05)
  - CHF 84 (2016–17): **−0.14\*\*\*** (0.05)
- Flat owners, column (6): −0.04 at CHF 60 (2014–15) and **−0.11\*\*\*** at CHF 84 (2016–17) ([Francescutto & Mathys 2022, p. 11](https://www.mdpi.com/1996-1073/15/9/3019)).
- Pseudo-panel estimates for house owners at CHF 84: −0.15\* to −0.22\*\* (Table 3) ([Francescutto & Mathys 2022, p. 12](https://www.mdpi.com/1996-1073/15/9/3019)).
- Semi-elasticities (Table 4): the CO2-levy coefficient is −0.012\*\*\* to −0.013\*\*\*, against −0.007\*\*\* on the net heating-oil price, for house owners. Households react more to the levy than to market price changes ([Francescutto & Mathys 2022, Table 4, p. 13](https://www.mdpi.com/1996-1073/15/9/3019)).

**Fauceglia, Müller, Leu & Betz (2020), SCCER CREST WP3-2020/02 (working paper, not peer-reviewed)**
- Abstract: the Swiss "carbon tax that increased by 400 percent between 2008 and 2015" led to "small but statistically significant reductions in energy consumption. The effect on CO2 emissions was greater, with up to eight percent… We estimated a tax elasticity of −0.17 for the consumption of light oil and −0.10 for natural gas" ([Fauceglia et al. 2020, abstract](https://www.zhaw.ch/storage/sml/institute-zentren/cee/WP3_02_2020_How_Do_Firms_Respond_to_a_Rising_Carbon_Tax.pdf)).
- Detail ([Fauceglia et al. 2020, p. 3](https://www.zhaw.ch/storage/sml/institute-zentren/cee/WP3_02_2020_How_Do_Firms_Respond_to_a_Rising_Carbon_Tax.pdf)):
  - Energy consumption fell by "about 4% for a typical firm".
  - Emissions fell by "three percent in the second post-policy period (2010-2012) and up to eight percent in the third post-policy period (2013-2015)".
  - Average pre-policy emissions were about 325 tCO2, so the cuts were about 25 tCO2 per firm.
  - Industry substituted natural gas for light oil; services cut both fuels.
- Earlier plant-level version: Fauceglia, Leu & Müller (2019) report CO2 −12% to −15% and energy −4% to −6% on 44,909 firms (2001–2015), with elasticities of −0.1 to −0.23 ([Francescutto & Mathys 2022, p. 5, citing ref. 38](https://www.mdpi.com/1996-1073/15/9/3019); [ZHAW record](https://digitalcollection.zhaw.ch/handle/11475/18378)). The 2020 firm-level version supersedes it with smaller numbers.

**Ott & Weber (2022), Energy Policy 160, 112698 (peer-reviewed)**
- Working-paper version (IRENE WP 18-09, December 2018): difference-in-differences with inverse probability of treatment weighting on the 2016 increase (CHF 60 → 84). Data: SHEDS 2016 and 2017 waves. "No statistically significant effect can be detected across a variety of specifications" ([Ott & Weber WP 18-09, abstract](https://www5.unine.ch/RePEc/ftp/irn/pdfs/WP18-09.pdf)).
- Salience: "the CO2 levy was mentioned only 3.85% of the time as a reason for renovations" ([Ott & Weber WP 18-09, p. 19](https://www5.unine.ch/RePEc/ftp/irn/pdfs/WP18-09.pdf)).
- Published version: titled "How effective is carbon taxation on residential heating demand? A household-level analysis" ([Ott PhD thesis, Neuchâtel 2022, citation of the chapter](https://libra.unine.ch/server/api/core/bitstreams/88207ead-ec88-415b-a604-7056cb9c7cba/content)). It uses five SHEDS waves (2016–2020) and "does not detect any clear short-run impact of the CO2 levy on fossil fuel users in comparison to non-fossil fuel users" (search summary of [libra.unine.ch record](https://libra.unine.ch/handle/20.500.14713/29807)). **[VERIFY: published abstract wording.]**

**Schäfer (2025), working-paper abstract (Chemnitz University of Technology, 21 November 2025; not peer-reviewed)**
- Headline: synthetic control method; "the levy led to an average annual reduction in CO2 emissions of 6.5% during the post-treatment period (2008−2021), corresponding to a decrease of 0.1 metric tons of CO2 per capita per year" ([Schäfer 2025 abstract](https://keynes-gesellschaft.de/wp-content/uploads/2026/03/Abstract-Schaefer-Teresa.pdf)).
- Elasticities ([Schäfer 2025 abstract](https://keynes-gesellschaft.de/wp-content/uploads/2026/03/Abstract-Schaefer-Teresa.pdf)):
  - Heating oil, short run: −0.055 (retail price) vs −1.264 (levy).
  - Natural gas, short run: −0.261 (retail) vs −0.623 (levy).
  - Long run: −0.087 vs −2.007 (oil) and −0.520 vs −1.24 (gas).

**Meta-analysis coverage**
- Döbbeling-Hildebrandt et al. (2024) cover the Swiss **ETS**, not the levy. It is one of three schemes with reduction effects smaller than −5%, all of them from studies "with severe problems in study design" ([Nature Communications 2024](https://www.nature.com/articles/s41467-024-48512-w)).

### Inferences
- **For the paper's table.** A defensible line is "Swiss CO2 levy on heating fuels (buildings and non-ETS firms), 2008–2015: levy CHF 12 → 60/t (heating-oil price +3% → +30%); ex post model-based estimate −4% to −10% of levy-relevant emissions in 2015 (0.8–1.8 Mt), net of co-policies about −1.3 Mt (about −7.6% of ~17 Mt, derived)". Micro evidence corroborates it once the rate reached CHF 60–84: −12% to −14% for house owners, and up to −8% for firms. That micro evidence is a mix of peer-reviewed and working-paper studies, and its weakest member is null (Ott & Weber).
- **Threshold pattern.** No measurable response at CHF 12–36, a clear response at CHF 60–84. This fits with the levy's share of the heating-oil price rising from about 3–12% (2008–13) to 17–34% (2014–17) in Table 3.1. It suggests responses are non-linear in price or need time for heating-system replacement.
- **Strength of identification.** The Ecoplan numbers are "ex post" only in the sense of using observed data with a modelled counterfactual. The general-equilibrium half is closer to a simulation. Francescutto & Mathys (before–after on survey data) and Schäfer (synthetic control) are the cleanest ex post designs. Neither has a contemporaneous untreated Swiss control group for households.

### Gaps
- **No newer official evaluation (data after 2015) was found.** It is not clear whether FOEN has published an update to 2020 or beyond. **[VERIFY on bafu.admin.ch, "CO2-Abgabe Wirkung".]**
- The Ecoplan 2017 report itself was not retrievable (404), so I could not confirm the split between the econometric and general-equilibrium figures by year, or the household and industry breakdown beyond "three quarters / one quarter".
- I did not specifically search University of Basel work (e.g. Hintermann), so no claim is made about it.
- The Schäfer paper is abstract only; its method details, donor pool and peer-review status are unknown.

### References (full, with access status)
- FOEN (Federal Office for the Environment) (2018). *Fact Sheet on the Impact Assessment and Evaluation of the CO2 Levy on Thermal Fuels*, 19 February 2018. **Full text read.**
- Ecoplan (2017). *Wirkungsabschätzung CO2-Abgabe – Aktualisierung bis 2015*. Bern, June 2017. **Not accessed** (link 404); numbers taken from the FOEN fact sheet.
- Ecoplan, EPFL & FHNW (2015). *Wirkungsabschätzung CO2-Abgabe – Modellrechnungen*. December 2015. **Not accessed** (404).
- TEP Energy & Rütter Soceco (2016). *Wirkungsabschätzung CO2-Abgabe – Direktbefragungen*. April 2016. **Not accessed.**
- Francescutto, N. & Mathys, N. A. (2022). The effect of the Swiss CO2 levy on heating fuel demand of private real estate owners. *Energies*, 15(9), 3019. https://doi.org/10.3390/en15093019. **Full text read** (the LAPSE repository copy of the MDPI article).
- Ott, L. & Weber, S. (2022). How effective is carbon taxation on residential heating demand? A household-level analysis. *Energy Policy*, 160, 112698. **Read the full text of the 2018 working paper (IRENE WP 18-09, "The impact of CO2 taxation on Swiss households' heating demand"); published version seen only as citation and search summary.** **[VERIFY: DOI, likely 10.1016/j.enpol.2021.112698.]**
- Fauceglia, D., Müller, T., Leu, T. & Betz, R. (2020). How do firms respond to a rising carbon tax? SCCER CREST Working Paper WP3-2020/02, 30 September 2020. **Read the abstract and introduction.**
- Schäfer, T. (2025). From taxes to transition: The impact of the Swiss CO2 levy on residential heating energy demand. Working paper abstract, Chemnitz University of Technology, 21 November 2025. **Abstract only.**

## 5. France's Contribution Climat-Énergie: rate path, per-unit amounts, and % effect on fuel prices

### Takeaway
The brief's rate path is confirmed: €7 (2014), 14.5 (2015), 22 (2016), 30.5 (2017) and 44.6/t (2018), then frozen after the Gilets Jaunes protests. The planned path of 55 / 65.4 / 75.8 / 86.2 for 2019–2022 was cancelled.

At €44.6 the carbon component is about **11.8 c€/l on diesel and 10.2 c€/l on petrol** (excluding VAT). Adding 20% VAT and comparing with Oil Bulletin pump prices gives:
- **2018 diesel**: about 10% of the pump price (+11% over the no-tax price);
- **petrol**: about 8% (+9%);
- **domestic heating oil**: about 16% (+18%);
- **household gas**: about 14% (+16%);
- **non-ETS industrial gas** (pre-tax): about +27%.

In 2014 the €7 component applied **only to natural gas, heavy fuel oil and coal**; road fuels were not affected.

### Cited Findings
- **Rate path.** 7 €/t (2014), 14.5 (2015), 22 (2016), 30.5 (2017), 44.6 (2018). "Le montant de la « taxe carbone » est depuis gelé à 44,6 €/t CO2." The 2018 Finance Bill had planned 55 (2019), 65.4 (2020), 75.8 (2021) and 86.2 (2022). The 2015 energy-transition law target was 56 €/t in 2020 and 100 €/t in 2030 ([Connaissance des Énergies, updated 6 Sept 2024](https://www.connaissancedesenergies.org/questions-et-reponses-energies/quel-est-le-montant-de-la-taxe-carbone-en-france)).
- **Planned 2018–2022 increases.** The Senate report on the 2018 Finance Bill confirms the rise "de 30,5 à 44,6 euros par tonne de CO2" in 2018. Further rises of €10.40 per year were planned to reach €86.20 in 2022, plus a diesel convergence of +2.6 c€/l per year 2018–2021 ([Sénat, rapport général PLF 2018](https://www.senat.fr/rap/l17-108-311-1/l17-108-311-13.html)).
- **Per-litre amounts at €44.6.** "Elle a atteint 44,6 € par tonne de CO² en 2018 (soit environ 12 centimes par litre de gazole et 10 centimes par litre d'essence sans plomb)". Footnote: "Le gazole contient 0,002651 tonne de CO² par litre, soit une composante carbone de 11,8 c€/l ; le SP95-E5 contient 0,002287 tonne de CO² par litre, soit une composante carbone de 10,2 c€/l" ([Fipeco, Ecalle, 30.09.2021, p. 3](https://www.fipeco.fr/pdf/Carburants2021.pdf)).
- **Tax growth 2013–2018.** "L'augmentation de cette composante explique la hausse du taux de la TICPE sur le SP95-E5 de 2013 à 2018 (+ 13 %). La hausse du taux de la TICPE sur le gazole (+ 39 %) tient à la montée en charge de la composante carbone mais aussi à son alignement progressif sur le taux d'imposition de l'essence" ([Fipeco 2021, p. 3](https://www.fipeco.fr/pdf/Carburants2021.pdf)).
- **2014 scope.** "Fixée à 7 euros la tonne de CO2 en 2014, elle ne s'applique cette année qu'au gaz naturel, au fioul lourd et au charbon" (article 32 of the 2014 Finance Law) ([Localtis / Banque des Territoires, 20 Jan 2014](https://www.banquedesterritoires.fr/lois-de-finances-les-principales-dispositions-pour-lenvironnement-et-lenergie)).
- **2017 per-unit table (secondary source)**, excluding VAT, with total excise and the carbon share ([fr.wikipedia "Contribution climat-énergie", citing DGEC 2016 p. 170 and Code des douanes art. 265](https://fr.wikipedia.org/wiki/Contribution_climat-%C3%A9nergie)):

  | Fuel | Carbon component | Total excise | Carbon share of excise |
  |---|---|---|---|
  | Gazole | 8.07 c€/l | 53.07 | 15% |
  | Essence E10 | 6.97 c€/l | 63.07 | 11% |
  | Fioul domestique | 8.07 c€/l | 11.89 | 68% |
  | Gaz naturel | 5.88 €/MWh PCS | 5.88 | 100% |
  | Charbon | 9.99 €/MWh | 9.99 | 100% |

  Total excise in 2018: gazole 59.40 c€/l; fioul domestique 15.62 c€/l; gaz naturel 8.45 €/MWh PCS; charbon 14.62 €/MWh. **[VERIFY against Code des douanes art. 265 / 266 quinquies; Wikipedia is secondary.]**
- **Revenue by year (secondary source).** €0.3bn (2014), 2.3bn (2015), 3.8bn (2016), 6.4bn (2017), 9.1bn (2018), citing I4CE Point Climat no. 56 and DGEC ([fr.wikipedia](https://fr.wikipedia.org/wiki/Contribution_climat-%C3%A9nergie)). **[VERIFY.]**
- **Prices still below earlier peaks.** I4CE notes that household energy prices including the carbon component "restent inférieurs ou équivalents à leur niveau le plus élevé, c'est‑à‑dire de 2012 pour les produits pétroliers et de 2014 pour le gaz naturel". It also notes that the component was frozen at 44.6 €/tCO2 at the end of 2018 ([I4CE, Panorama des financements climat 2020, Annexe 1, March 2021](https://www.i4ce.org/wp-content/uploads/Annexe-1-Les-prix-des-energies-et-du-carbone.pdf)).
- **French retail oil-product prices with all taxes** (EU Weekly Oil Bulletin, annual mean of weekly data, € per 1,000 l) ([DG ENER Oil Bulletin history](https://energy.ec.europa.eu/document/download/906e60ca-8b6a-44e7-8589-652854d2fd3f_en?filename=Weekly_Oil_Bulletin_Prices_History_maticni_4web.xlsx)):

  | Year | Euro-super 95 | Diesel | Heating oil |
  |---|---|---|---|
  | 2013 | 1,538 | 1,351 | 928 |
  | 2014 | 1,492 | 1,293 | 866 |
  | 2015 | 1,356 | 1,155 | 711 |
  | 2016 | 1,301 | 1,102 | 633 |
  | 2017 | 1,375 | 1,230 | 739 |
  | 2018 | 1,507 | 1,437 | 912 |
  | 2019 | 1,505 | 1,439 | 929 |
  | 2020 | 1,357 | 1,260 | 764 |

- **French gas prices** (Eurostat, annual mean of semesters, €/MWh GCV):

  | Year | Households, band D2, all taxes ([nrg_pc_202](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nrg_pc_202?geo=FR&nrg_cons=GJ20-199&unit=KWH&tax=I_TAX&currency=EUR&lang=en)) | Non-households, band I3, excluding taxes ([nrg_pc_203](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nrg_pc_203?geo=FR&nrg_cons=GJ10000-99999&unit=KWH&tax=X_TAX&currency=EUR&lang=en)) |
  |---|---|---|
  | 2014 | 73.1 | 36.6 |
  | 2015 | 71.7 | 34.0 |
  | 2016 | 66.3 | 30.9 |
  | 2017 | 66.7 | 28.2 |
  | 2018 | 71.4 | 29.8 |
  | 2019 | 78.9 | 30.2 |
  | 2020 | 73.6 | 27.4 |

### Inferences
**Table 5.1 (derived): French carbon component and its weight in fuel prices.**
- Method:
  - Carbon component = rate × factor: diesel 2.651 kg/l, SP95 2.287 kg/l, heating oil 2.651 kg/l, gas 0.182 t/MWh GCV.
  - Household amounts include 20% VAT; industrial gas excludes VAT, which firms recover.
  - Share = component incl. VAT ÷ retail price (Oil Bulletin or Eurostat).
  - % increase = component ÷ (price − component).
  - In 2014 the component did not apply to road fuels or heating oil, so those cells are 0.
- Each cell reads: carbon component c€/l (incl. VAT) → % increase.

| Year | €/t | ≈US$/t | Diesel | Petrol SP95 | Heating oil | Household gas, €/MWh GCV incl. VAT | Non-ETS industrial gas, € ex-VAT → % of pre-tax I3 price |
|---|---|---|---|---|---|---|---|
| 2014 | 7.0 | 9.3 | 0 (not applied) | 0 (not applied) | 0 (not applied) | 1.53 → +2.1% | 1.27 → +3.5% |
| 2015 | 14.5 | 16.1 | 3.84 (4.61) → +4.2% | 3.32 (3.98) → +3.0% | 3.84 (4.61) → +6.9% | 3.17 → +4.6% | 2.64 → +7.8% |
| 2016 | 22.0 | 24.4 | 5.83 (7.00) → +6.8% | 5.03 (6.04) → +4.9% | 5.83 (7.00) → +12.4% | 4.81 → +7.8% | 4.01 → +13.0% |
| 2017 | 30.5 | 34.5 | 8.09 (9.70) → +8.6% | 6.98 (8.37) → +6.5% | 8.09 (9.70) → +15.1% | 6.67 → +11.1% | 5.56 → +19.7% |
| 2018 | 44.6 | 52.7 | 11.82 (14.19) → +11.0% | 10.20 (12.24) → +8.8% | 11.82 (14.19) → +18.4% | 9.75 → +15.8% | 8.12 → +27.3% |
| 2019 | 44.6 | 49.9 | same → +10.9% | same → +8.9% | same → +18.0% | 9.75 → +14.1% | 8.12 → +26.9% |
| 2020 | 44.6 | 50.9 | same → +12.7% | same → +9.9% | same → +22.8% | 9.75 → +15.3% | 8.12 → +29.6% |

- **Check against the official amounts.** My 2017 figures (8.09 / 6.98 / 8.09 c€/l) match the official 8.07 / 6.97 / 8.07. For gas, the official TICGN (5.88 in 2017, 8.45 in 2018 €/MWh PCS) implies a factor of about 0.19 t/MWh PCS rather than my 0.182. Using official TICGN would raise the gas shares by about 4–6%.
- **Industrial gas cell is an upper bound.** The CCE applied to non-ETS industrial users; ETS installations were largely outside it **[VERIFY: exact exemption rules for ETS installations under TICGN/TICPE]**. Reduced rates for energy-intensive users are not modelled here.
- **Price signal masked by falling oil prices.** Retail prices *fell* in 2015–2016 despite the rising component (Oil Bulletin: diesel 1.293 → 1.102 €/l), because oil prices collapsed. That is consistent with I4CE's point that prices stayed at or below the 2012/2014 peaks. The signal was masked, which matters for interpreting any null household response.

### Gaps
- Official year-by-year per-unit tables (DGEC / Code des douanes) were not read directly. Per-unit values for 2014–2016 and 2018 are computed from rates and factors.
- No official source was found for the date in 2014 from which the gas component applied (possibly 1 April 2014 for households). **[VERIFY.]**

### References (full, with access status)
- Ecalle, F. (2021). *La taxation des carburants*. Fipeco, 30 September 2021. **Full text read.**
- Localtis / Banque des Territoires (2014). *Lois de finances: les principales dispositions pour l'environnement et l'énergie*, 20 January 2014. **Relevant passage read.**
- Connaissance des Énergies (2024). *Quel est le montant de la taxe carbone en France ?*, updated 6 September 2024. **Read.**
- Sénat (2017). Rapport général sur le projet de loi de finances pour 2018, tome II, art. 9. **Read** (the tables on that page are images).
- I4CE (2021). *Panorama des financements climat, édition 2020, Annexe 1: Les prix des énergies et du carbone*. **Read.**

## 6. France's carbon tax: ex post evidence on manufacturing firms and households

### Takeaway
The main ex post estimate is **Dussaux (2020, OECD Environment WP 154)**. Using about 8,000 manufacturing firms (2001–2016), it finds:
- a 10% rise in energy costs cuts firm energy use by 6% and CO2 by 9% within a year;
- the carbon tax **cut manufacturing CO2 by about 5% over 2014–2018** relative to no tax, with a small positive net employment effect (+0.8%).

This is a credible but non-peer-reviewed OECD working paper. I could read only its abstract and the OECD blog summary, not the full text.

A second plant-level working paper (Marten 2022) finds that exposure to the tax shifted plants from fossil fuels towards electricity. **I found no ex post (quasi-experimental) evaluation of the CCE's effect on household transport or heating emissions.** The household evidence located is ex ante microsimulation or general elasticity work.

### Cited Findings
**Dussaux (2020), OECD Environment Working Papers No. 154**
- Scope: "The analysis uses data on 8 000 firms that are representative of the French manufacturing sector and observed during 2001-2016. This paper also measures the causal impact of the carbon tax over the period 2014-2018 and simulates the effect of further increasing the carbon tax rate from €45 to €86 per tonne of CO2" ([RePEc abstract](https://ideas.repec.org/p/oec/envaaa/154-en.html)).
- Firm-level elasticities: "a 10% increase in energy costs results in a 6% decline in energy use, a 9% decrease in carbon emissions" and "a 2% decrease in the number of full-time employees within one year". Jobs are reallocated to other firms rather than lost ([OECD Ecoscope blog, 4 Feb 2020](https://oecdecoscope.blog/2020/02/04/carbon-tax-emissions-reduction-and-employment-some-evidence-from-france/)).
- Aggregate: "In five years, the carbon tax decreased carbon emissions by 5%"; the net employment effect is "slightly positive at +0.8%" ([OECD Ecoscope blog](https://oecdecoscope.blog/2020/02/04/carbon-tax-emissions-reduction-and-employment-some-evidence-from-france/)).
- Context in the blog: "EU-ETS covers 75% of French industrial emissions" ([OECD Ecoscope blog](https://oecdecoscope.blog/2020/02/04/carbon-tax-emissions-reduction-and-employment-some-evidence-from-france/)). The carbon tax therefore bites mainly on the remaining non-ETS manufacturing emissions.
- Simulation of doubling the rate (€45 → €86): −8.7% emissions, according to press coverage (Bloomberg, via search summary). Ex ante and secondary. **[VERIFY in full text.]**
- Mt equivalent: about 3.6 Mt avoided (0.5% of France's 2019 carbon footprint), attributed to the Haut Conseil pour le climat (Sept 2021) via [fr.wikipedia](https://fr.wikipedia.org/wiki/Contribution_climat-%C3%A9nergie). **[VERIFY: not confirmed in the HCC report or Dussaux.]**

**Marten (2022), THEMA Working Paper 2022-19 (not peer-reviewed)**
- "Carbon tax reform and French industry response: Insights from panel data, 2005–2019". A linear panel event study of plants' exposure to carbon pricing, including expected future exposure.
- Findings: higher exposure shifts the energy mix toward electricity (a 10 percentage-point increase in exposure → +2.03 pp electricity share), mainly through lower fossil-fuel use and substitution toward gas within fossils; no average job losses ([RePEc abstract](https://ideas.repec.org/p/ema/worpap/2022-19.html)).
- No CO2 magnitude is given in the abstract.

**Household transport and heating**
- I found no quasi-experimental ex post study of the CCE on household fuel or heating demand.
- What exists instead:
  - Ex ante microsimulations, e.g. Douenne's IPP work simulating the 2015–2016 rate rises on 2014 data ([IPP report](https://www.ipp.eu/wp-content/uploads/2016/07/ipp-t-douenne-APE2016-rapport-m2.pdf)).
  - Pre-policy elasticity studies (INSEE, 2006 data: micro price elasticity of fuel demand 0.7–1.0 in absolute value) ([INSEE](https://insee.fr/en/statistiques/1380838)).
- These are not ex post evaluations of the tax and should be excluded under the brief's rules.
- I4CE's observation that household energy prices including the carbon component stayed at or below their 2012/2014 peaks ([I4CE 2021](https://www.i4ce.org/wp-content/uploads/Annexe-1-Les-prix-des-energies-et-du-carbone.pdf)) helps explain why a clean household natural experiment is hard to identify.

### Inferences
- **For the paper's table.** "France CCE, manufacturing (non-ETS energy use), 2014–2018: rate €7 → €44.6/t (non-ETS industrial gas price +3.5% → +27% pre-tax, derived); ex post estimate about −5% CO2 in manufacturing by 2018 (Dussaux 2020, OECD WP)". The household side should be reported as "no ex post estimate available". That is itself a finding: the political reversal in 2018–2019 cut short the experiment before evaluators could isolate it from oil-price swings.
- **How "ex post" Dussaux is.** It appears to estimate firm-level energy-price elasticities ex post and then apply them to the tax-induced price change. That makes it less design-based than a difference-in-differences on the tax itself. **[VERIFY: method description in full text, which I could not access (OECD returned 403).]**

### Gaps
- **Dussaux (2020) full text was not accessible**, so I have no tables, pages, confidence intervals or the exact identification strategy. The 5%, 6%, 9%, −2% and +0.8% figures come from the OECD blog. The 8.7% simulation figure is from press coverage.
- No peer-reviewed version of Dussaux (2020) was found. **[VERIFY: whether it was later published.]**
- No ex post household transport or heating study of the CCE was found. Possible leads I did not check: CGDD/SDES *Théma* notes, Conseil des prélèvements obligatoires (2019), DG Trésor analyses.

### References (full, with access status)
- Dussaux, D. (2020). The joint effects of energy prices and carbon taxes on environmental and economic performance: Evidence from the French manufacturing sector. OECD Environment Working Papers No. 154, OECD Publishing, Paris. https://doi.org/10.1787/b84b1b7d-en. **Abstract (RePEc) and OECD blog only; full text not accessed.**
- Marten, M. (2022). Carbon tax reform and French industry response: Insights from panel data, 2005–2019. THEMA Working Paper 2022-19, CY Cergy Paris Université. **Abstract only.**

## 7. Caveats: free allocation, the 2008–09 recession, carbon leakage, concurrent policies, and what reviews conclude

### Takeaway
The main threats to reading these cases as clean natural experiments are well documented, and the best studies address them directly:
- **Recession**: Bayer & Aklin's effects come on top of the 2008–09 output fall; matched micro designs difference it out.
- **Free allocation**: in the EU ETS it lowered cash costs but not marginal incentives. Under-allocated installations cut more.
- **Leakage**: no evidence of leakage in the EU ETS (Naegele & Zaklan 2019; Dechezleprêtre et al. 2022; Colmer et al. 2025).
- **Concurrent policies**: the Swiss building programme and target agreements inflate the gross levy estimate (FOEN nets them out). French oil-price swings mask the CCE.

Reviews range from "limited" effects (Green 2021: 0–2% per year) to "substantial" ones (Döbbeling-Hildebrandt et al. 2024: −5% to −21% per scheme).

### Cited Findings
- **Recession.** Bayer & Aklin's estimated reductions "of between 8.1 and 11.5% are on top of any emission reductions from reduced economic output during the 2007/2008 financial crisis". Placebo start dates in a ±5-year window around 2008 do not reproduce the effect ([Bayer & Aklin 2020, p. 4](https://strathprints.strath.ac.uk/72023/1/Bayer_Aklin_PNAS_2020_The_European_Union_emissions_trading_system_reduced_CO2.pdf)).
- **Recession in DNV.** Year fixed effects absorb "common shocks to all installations (such as the economic crisis in 2008/2009)" ([DNV 2023, p. 11](https://researchonline.lse.ac.uk/id/eprint/117357)).
- **Other drivers.** Colmer et al. find that 53–72% of the aggregate fall in French industrial emissions in 2005–2012 was driven by factors other than the ETS, e.g. "structural economic change, energy efficiency improvements, and the Great Recession" ([CEP DP1728, p. 36](https://cep.lse.ac.uk/pubs/download/dp1728.pdf)).
- **Free allocation.** "A less generous allocation of free allowances creates a stronger incentive to reduce emissions, as under-allocated installations seem to have reduced emissions to a larger extent" ([DNV 2023, p. 2](https://researchonline.lse.ac.uk/id/eprint/117357)). Positive revenue effects may reflect pass-through of free-allowance opportunity costs ([DNV 2023, p. 17](https://researchonline.lse.ac.uk/id/eprint/117357)). Klemetsen et al. attribute positive value-added effects to free allowances and pass-through ([SSB DP 833](https://www.ssb.no/en/forskning/discussion-papers/the-impacts-of-the-eu-ets-on-norwegian-plants-environmental-and-economic-performance)).
- **Leakage studies.**
  - Naegele & Zaklan (2019, JEEM 93: 125–147) find no evidence that the EU ETS caused carbon leakage in European manufacturing, using GTAP embodied-carbon trade flows ([EconPapers record](https://econpapers.repec.org/RePEc:eee:jeeman:v:93:y:2019:i:c:p:125-147)).
  - Dechezleprêtre, Gennaioli, Martin, Muûls & Stoerk (2022, JEEM 112, 102601) use CDP data for 2007–2014 on 1,122 multinationals (261 under the EU ETS) and find no evidence of emissions moving out of Europe ([LSE Research Online](https://researchonline.lse.ac.uk/id/eprint/116399)).
  - Both are from search summaries; abstracts not opened in full. **[VERIFY wording.]**
- **Concurrent Swiss policies.** The econometric levy estimates "include the effects of other measures… therefore overestimate the impact". The building programme (financed from levy revenue) and target agreements are deducted to obtain the net effect ([FOEN fact sheet 2018, p. 4](https://www.bafu.admin.ch/dam/en/sd-web/OhnKjWv6AJ-t/Faktenblatt%20Evaluation%20CO2-Abgabe%20(Update%202018)_EN.pdf)).
- **Anticipation (Switzerland).** "The CO2 levy (and particularly its announcement) has triggered diverse reactions", and the time-series model includes anticipation of future levy increases ([FOEN fact sheet 2018, pp. 2–3](https://www.bafu.admin.ch/dam/en/sd-web/OhnKjWv6AJ-t/Faktenblatt%20Evaluation%20CO2-Abgabe%20(Update%202018)_EN.pdf)). This is why the cumulative window starts in 2005, before the 2008 introduction.
- **Döbbeling-Hildebrandt et al. (2024).** "Based on 483 effect sizes extracted from 80 causal ex-post evaluations across 21 carbon pricing schemes… Statistically significant emissions reductions range between –5% to –21% across the schemes (–4% to –15% after correcting for publication bias)" ([Nature Communications 2024, abstract](https://www.nature.com/articles/s41467-024-48512-w)).
- **Green (2021).** "Overall, the evidence indicates that carbon pricing has a limited impact on emissions." Only 37 studies assess actual emissions effects; aggregate reductions are about 0–2% per year ([Green 2021, ERL](https://iopscience.iop.org/article/10.1088/1748-9326/abdae9)).
- **Köppl & Schratzenstaller (2023), Journal of Economic Surveys 37(4): 1353–1388.** "An increasing body of empirical studies shows that carbon taxes can effectively reduce carbon emissions or at least dampen their growth while not negatively affecting economic growth, employment, and competitiveness" (abstract, via search summary of the [RePEc record](https://ideas.repec.org/a/bla/jecsur/v37y2023i4p1353-1388.html)).

### Inferences
- **Green vs Döbbeling-Hildebrandt is mostly a units difference.** Green reports *annual* rates (0–1.5% per year for the EU ETS), whereas Döbbeling-Hildebrandt and the micro studies report *cumulative level* effects (−7% to −16%). Over 5–8 years, 1–2% per year compounds to a level effect of roughly −5% to −15%. The paper should state which metric it uses.
- **Ranking the three cases by evidence quality:**
  1. EU ETS: several peer-reviewed micro studies plus a sector-level synthetic control, all agreeing.
  2. Switzerland: an official model-based evaluation and one peer-reviewed micro study agree on direction; one peer-reviewed micro study is null.
  3. France: one OECD working paper on manufacturing, nothing ex post on households.

### Gaps
- Phase III/IV EU ETS leakage studies after 2014, and any evaluation of the 2018 MSR-driven price jump as a natural experiment, were not searched.
- The French CCE's interaction with the EU ETS (which installations were exempt, double-coverage rules) was not documented from a primary source.

### References (full, with access status)
- Naegele, H. & Zaklan, A. (2019). Does the EU ETS cause carbon leakage in European manufacturing? *Journal of Environmental Economics and Management*, 93, 125–147. https://doi.org/10.1016/j.jeem.2018.11.004. **Metadata and abstract summary only.**
- Dechezleprêtre, A., Gennaioli, C., Martin, R., Muûls, M. & Stoerk, T. (2022). Searching for carbon leaks in multinational companies. *Journal of Environmental Economics and Management*, 112, 102601. **Metadata and abstract summary only.** **[VERIFY: DOI.]**
- Köppl, A. & Schratzenstaller, M. (2023). Carbon taxation: A review of the empirical literature. *Journal of Economic Surveys*, 37(4), 1353–1388. https://doi.org/10.1111/joes.12531. **Abstract only, via search summary.**
