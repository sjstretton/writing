# Evidence check, 20 November 2026: Egypt (research assistant's report; [S] = search summary only, unconfirmed; everything else read on a page or file opened)

# Egypt fact check — status at 20 Nov 2026

Stopped on the coordinator's instruction; the web-search budget for this turn also ran out, so items 13, 23 and parts of 8, 10, 18 and 25 were not finished. Figures marked **[S]** come from search-result summaries only (page not opened, often HTTP 403) and should be treated as unverified leads. Everything else was read on a page or file I opened. Context that affects most 2026 numbers: IMF documents describe a "war in the Middle East" from March 2026 (oil spike, Israeli pipeline gas suspended in March and restored in April, pound depreciation).

## Source keys (all opened)
- **IMF-7R**: IMF Country Report No. 26/224, Seventh Review under the EFF and Second Review under the RSF, staff report completed 17 July 2026, published August 2026. https://www.imf.org/-/media/files/publications/cr/2026/english/1egyea2026002.pdf
- **IMF-56R**: IMF Country Report No. 26/069, Fifth and Sixth Reviews under the EFF and First Review under the RSF, published 26 March 2026 (includes the World Bank assessment letter). https://www.imf.org/-/media/files/publications/cr/2026/english/1egyea2026001.pdf
- **WEO**: IMF World Economic Outlook database, October 2026 (published 13 Oct 2026), via the IMF SDMX API. Egypt data are fiscal years: "FY(t-1/t) = CY(t)". https://api.imf.org/external/sdmx/2.1/data/WEO/EGY.NGDPD+NGDP_RPCH+LP+GGXWDG_NGDP+PCPIPCH.A?startPeriod=2023&endPeriod=2028
- **Ember**: Ember yearly electricity data, calendar years, downloaded 20 Nov 2026 (country page last updated 22 Apr 2026). https://files.ember-energy.org/public-downloads/generation/outputs/release_generation_yearly_global.csv
- **MoF-Debt**: Egypt Ministry of Finance Debt Management Unit, "Portfolio Risk Management under the current Geopolitical Tensions", April 2026. https://thedocs.worldbank.org/en/doc/79cff17003d1ab45aa70a8613c106464-0350012026/original/Egypt-Debt-Management.pdf
- **Ent-Blackout / Ent-Gas / Ent-Cost**: three EnterpriseAM articles of 30 Sep 2026. https://enterpriseam.com/egypt/2026/09/30/why-a-gas-shortage-becomes-a-blackout-in-your-living-room/ ; https://enterpriseam.com/egypt/2026/09/30/a-giant-gas-discovery-brought-egypt-back-what-brings-it-back-again/ ; https://enterpriseam.com/egypt/2026/09/30/the-real-cost-of-egypts-electricity-is-split-between-your-bill-the-treasury-and-the-countrys-dollar-reserves/
- **Ent-45**: EnterpriseAM, 11 Aug 2026. https://enterpriseam.com/egypt/going-green/egypt-has-raised-its-renewables-target-to-45-by-2028-without-publishing-the-demand-forecast-to-verify-it/
- **Ent-CBE**: EnterpriseAM, 1 Nov 2026. https://enterpriseam.com/egypt/2026/11/01/cbe-hikes-for-the-first-time-since-march-2024-raising-rates-100-bps-and-moving-its-inflation-target-to-4q-2027/

## A. Power system

**1. Generation and mix.**
- Calendar 2025 (Ember): total 241.6 TWh. Confidence high for the dataset.

| Source | TWh | Share |
|---|---|---|
| Gas | 184.4 | 76.3% |
| Other fossil (oil) | 23.9 | 9.9% |
| Hydro | 14.8 | 6.1% |
| Wind | 9.9 | 4.1% |
| Solar | 8.5 | 3.5% |
| Wind + solar | 18.5 | 7.6% |
| All renewables | 33.3 | 13.8% |

- Calendar 2024 (Ember): total 237.6 TWh; gas 77.9%, other fossil 10.1%, wind + solar 5.5%, renewables 12.0%.
- The 2025 gas and oil rows both show exactly −0.38% year on year, which suggests an estimated split.
- Differing sources:
  - Climate Action Tracker (chart dated 17 July 2026) gives gas 80%, oil about 7%, and "Gas-fired generation rose from 167 TWh in 2020 to 196 TWh in 2025". https://climateactiontracker.org/countries/egypt/policies-action/
  - MEES, 27 Feb 2026, citing NREA: "Egypt generated a record 35.19TWh of electricity from renewable power plants in 2025"; hydro 17.3, wind 10.5, solar 7.43 TWh. https://www.mees.com/2026/2/27/power-water/egypt-renewables-surge-to-annual-record/929097e0-13e9-11f1-a124-2f202365ce8a
  - EEHC via Ent-Blackout: gas was 79.1% of power-plant fuel in FY2024/25, down from 83.7% in FY2023/24.

**2. Capacity, peak, surplus.**
- Capacity by source, end-2025 (Ember): total 63.5 GW; gas 53.43, other fossil 0.79, hydro 2.83, wind 3.03, solar 3.27, bioenergy 0.13. High.
- EEHC via Ent-Blackout: 59.7 GW in June 2024; "EEHC recorded 60.8 GW of installed capacity and a 38 GW peak load in FY 2024/25". Medium-high.
- Latest ministry figure: 64.4 GW total, 10.5 GW renewables, 1.1 GW batteries (Ahram, 22 Oct 2026) **[S]**. https://english.ahram.org.eg/News/580650.aspx
- Peak demand: "a record peak load of 40,000 megawatts (MW) on Tuesday, August 11" 2026; previous record 39,800 MW in 2025 (Arab Finance via Zawya). https://www.zawya.com/en/economy/egypts-electricity-grid-hits-record-40000-mw-peak-load-amid-summer-heat-429151 . A 40,200 MW reading the next day is **[S]**.
- Siemens plants: Beni Suef, Burullus and New Capital, commissioned 2017–2018, added 14.4 GW (EIA country brief, 13 Aug 2024). https://www.eia.gov/international/analysis/country/EGY . They supplied about one-third of FY2024/25 electricity (Ent-Blackout).
- Surplus: no official reserve-margin figure found. My arithmetic gives nameplate about 58–60% above peak (63.5–64.4 GW against 40.0–40.2 GW). Ent-Blackout says spare capacity is "thinner than it looks" because output depends on fuel supply.
- Largest renewable addition in one year (Ember): +1.55 GW in 2025 (7.71 to 9.26 GW), the largest in the series. Earlier years: +1.04 (2024), +0.99 (2018), +0.90 (2019). High for the dataset.
- NREA via MEES: renewable capacity up 23% to 9.06 GW by end-2025.
- Planned additions (Ent-45): 11.2 GW by end-2026, 16.8 GW by end-2027, 27.7 GW by end-2028.

**3. Targets.**
- 2030: "increase electricity generation contribution to be 42% of generation mix by 2030" (Second Updated NDC, June 2023). https://unfccc.int/sites/default/files/NDC/2023-06/Egypts%20Updated%20First%20Nationally%20Determined%20Contribution%202030%20%28Second%20Update%29.pdf . High.
- 2026 revision:
  - World Bank letter in IMF-7R: "The target for the renewable energy share to reach 42 percent has been advanced to 2028 instead of 2030."
  - Authorities' memorandum in IMF-7R: "Following the May 2026 update of the renewable energy strategy… By end-2028, renewables are projected to account for about 45 percent of electricity generation capacity."
  - Ent-45: "The government is now targeting 45% of the electricity mix by 2028", but the pathway is expressed in installed capacity and no updated strategy document has been published.
- 2040: Climate Action Tracker reports 58% by 2040 announced in June 2024, then cut to 40% in October 2024, and that ISES 2035 "has not been updated since its adoption in 2016". Medium. A ">60% by 2040" figure (trade.gov, Oilprice) is **[S]**.
- Current share: 13.8% in 2025 (Ember), against 42%.

**4. Demand growth.**
- Ember demand: 216.1 TWh (2022, +3.4%), 221.8 (2023, +2.6%), 236.2 (2024, +6.5%), 240.2 (2025, +1.7%). High.
- Projected: the government anticipated "an 8% increase in electricity demand this summer" 2026 (Zawya, above). EEHC's FY2026/27 planning budget targets 263 TWh of generation (Ent-45).
- EEHC peak forecast of 41,581 MW (+4.5%) or 42,300 MW (+6.3%) is **[S]**.

**5. Losses, grid, interconnector.**
- Losses: "have declined to 17.6%" (electricity minister; Daily News Egypt, 28 Sep 2026). https://www.dailynewsegypt.com/2026/09/28/egypt-cuts-fuel-consumption-costs-by-egp-70bn-as-grid-losses-fall-to-17-6-minister/ . Medium. 19.6% in 2023/24 is **[S]**.
- World Bank letter in IMF-56R: "progress in terms of actual reduction in losses remains limited".
- Grid finance:
  - EIB, 15 June 2026: €600m loan plus up to €90m EU grants, covering 44% of the EETC programme to connect 22 GW of renewables by 2030. Borrower is the government through the central bank. https://www.eib.org/en/press/all/2026-206-egypt-and-eu-join-forces-on-eur690-million-clean-energy-grid-investment
  - EBRD: "Around €350 million has already been structured to reinforce transmission infrastructure" with KfW and AFD. https://www.ebrd.com/home/what-we-do/impact-management/impact-case-studies/accelerating-decarbonisation-in-egypt.html
  - EETC investment budgets of EGP 44.9bn (FY2025/26) and about EGP 37bn (FY2026/27) are **[S]**.
- Egypt–Saudi link: 3 GW, 500 kV HVDC, about 1,400 km, US$1.8bn. On 26 Aug 2026 it was "in the final stages of technical and operational trials". https://enterpriseam.com/egypt/2026/08/26/egypt-saudi-arabia-in-final-stages-of-trials-for-3-gw-electricity-interconnection/ . Still at trial operation on 28 Sep 2026 (Daily News Egypt). Commercial operation by 20 Nov 2026: NOT FOUND.

**6. Tariffs and subsidy.**
- Average tariff and unit cost of supply: NOT FOUND. A figure of about 257 piastres/kWh cost against a 68-piastre lowest tier (Al Manassa) is **[S]**.
- Electricity subsidy:
  - FY2024/25: "increased electricity subsidies to EGP 10 billion (0.1 percent of GDP)" and "kept tariffs below cost-recovery levels" (World Bank letter, IMF-56R).
  - FY2025/26: budgeted EGP 75bn, about 0.4% of GDP (same letter).
  - FY2026/27: budget allocation EGP 104.2bn (Ent-Cost).
  - IMF-7R implied electricity subsidy (energy minus fuel, my subtraction): EGP 10bn FY2024/25, 77bn FY2025/26 estimate, 114bn FY2026/27 projection.
  - Government estimate of the annual gap between generation costs and household tariffs after the August rise: about EGP 100bn (Ent-Cost).
- Tariff rises:
  - August 2024: residential +14–40%, commercial +23.5–46% (Arab Finance via Zawya). https://www.zawya.com/en/economy/north-africa/understanding-egypts-electricity-tariff-increases-mmvvqa6k
  - 2025: none. "the last tariff increase took place in August 2024" (IMF-56R).
  - April 2026 (IMF-7R Text Table 3): households above 1,000 kWh EGP 2.23 to 2.58 (+16%); commercial bands +20% to +91%, e.g. 1–100 kWh 85 to 162 piastres.
  - May 2026: irrigation, water and commercial/service +31.4% (Ent-Cost).
  - August 2026: households +12% on average (Ent-Cost).
- 11 March 2026: financial viability plan for the electricity sector adopted (IMF-7R). High for IMF items.

## B. Gas and fuel

**7. Gas.**
- Production (JODI via Ent-Gas): peak 70.4 bcm in 2021; 42.3 bcm in 2025; first half 2026 19.5 bcm (−7.8% year on year, about 3.8 bcf/d). Medium-high.
- Other estimates: Rystad 43 bcm for 2025 and 49 bcm for 2024 (The National, 18 Dec 2025). https://www.thenationalnews.com/business/energy/2025/12/18/israels-35bn-gas-deal-to-ease-egypts-energy-crunch-and-cut-import-costs . Enerdata 38 bcm **[S]**.
- Consumption: about 7.5 bcf/d against local output of about 3.8 bcf/d (The National).
- Trade (Ent-Gas): imports 8.6 bcm (2023) to 22.2 bcm (2025); exports 12 bcm (2022) to 1.1 bcm (2025); net deficit 21.1 bcm in 2025. First half 2026 imports 13.1 bcm, of which LNG 8.8 and pipeline 4.3.
- Switch to importer: first LNG import "since September 2018" in April 2024, the same month Egypt exported "its last LNG cargoes" (MEES, 10 Jan 2025). https://www.mees.com/2025/1/10/refining-petrochemicals/egypt-lng-imports-hit-7-year-high-278mn-t-for-2024-eyes-tentative-exports-for-2025/afbd2790-cf54-11ef-b27b-ebbe8e49403c
- LNG volumes: 2.78–2.79 mt in 2024; "a record 8.92mn tons of LNG in 2025, 91% of which came from the US" (MEES/Kpler, 2 Jan 2026). https://www.mees.com/2026/1/2/refining-petrochemicals/egypt-lng-imports-record-2025-more-to-come-in-2026/691f0f70-e7dd-11f0-acc6-1d86dba5c11b . Platts 9.01 mt for 2025 and 11.14 mt forecast for 2026 are **[S]**.
- Import bill:
  - First half 2026: "USD 6.04 bn on natural gas imports", up 73% from USD 3.5bn (Capmas via Ent-Cost).
  - Monthly: about USD 560m in February 2026 to USD 1.65bn in March.
  - FY2026/27 budget for gas imports: USD 10.7bn.
  - LNG cargo: about USD 80m after the war against USD 40m before.
  - March–June 2026: "the import bill expanded by approximately US$3.5 billion, with natural gas accounting for roughly half" (IMF-7R).
  - Net oil and gas trade deficit: USD 7.6bn FY2023/24, 13.9bn FY2024/25, 20.1bn estimated FY2025/26 (IMF via Ent-Cost).
  - Calendar-year bills of about $4.9bn (2024, all gas) and about $8.9bn (2025, LNG) are **[S]**.
- Israeli gas: Rystad estimate $7.29/mmBtu, with LNG "double that"; 130 bcm to 2040, up to $35bn (The National). No contract price published. Low-medium.
- Gas price to power plants: $4/mmBtu from December 2024, up from $3, is **[S]**. "natural gas (22-30 percent)" rises in March 2026 (IMF-7R), category unspecified. Current power-plant price: NOT FOUND.
- Share of gas burnt in power: current figure NOT FOUND. Only "By 2014, power generation consumed 57% of domestic gas" (IRENA via Ent-Blackout).

**8. Fuel subsidies and prices.**
- Budget-sector outturns and projections (IMF-7R Tables 3a and 3b). High for EGP and % of GDP; US$ are my conversions at the average rate implied by IMF EGP GDP and WEO US$ GDP, so approximate.

| Fiscal year | Fuel subsidy (EGP bn) | % GDP | About US$ bn | Total energy (EGP bn) | % GDP |
|---|---|---|---|---|---|
| FY2023/24 | 165 | 1.2 | 4.5 | 167 | 1.2 |
| FY2024/25 | 156 | 0.9 | 3.1 | 166 | 0.9 |
| FY2025/26 (estimate) | 93 | 0.4 | 1.9 | 170 | 0.8 |
| FY2026/27 (projection) | 84 | 0.3 | 1.6 | 198 | 0.8 |

- Budget allocations: FY2026/27 total energy subsidy EGP 120bn, down from about 150bn, with fuel about EGP 16–16.5bn, is **[S]** (Ahram, Enterprise, Al Manassa). Note the IMF projects fuel at EGP 84bn for the same year.
- Price rises:
  - 2025: "raised by 2 EGP (an increase of 11-15 percent depending on fuel product) on April 11 and by 2 EGP on October 17" (IMF-56R).
  - 10 March 2026: +EGP 3 per litre, above the 10% cap. 95-octane 21 to 24; 92-octane 19.25 to 22.25; 80-octane 17.75 to 20.75; diesel 17.50 to 20.50; LPG cylinder 225 to 275; CNG 10 to 13 (IMF-7R Text Table 3; Rio Times, 7 Nov 2026). https://www.riotimesonline.com/egypt-petrol-diesel-prices-unchanged-december-2026/
  - 15 October 2026: "The committee fixed diesel and all three petrol grades until the end of December 2026."
  - 2024 rises (March, July, October): not verified on an opened page.
- IMF commitment: "full cost recovery for retail fuel products to be achieved by end-December 2025". Reported as met: "we reached cost recovery… in December 2025" (IMF-7R).
- After the war, the increase in energy subsidies "was contained to EGP 15 billion 0.07 percent of GDP in FY 2025/26". The automatic mechanism (10% quarterly cap) was announced to resume in July 2026.
- Protests and reversals: 1977 bread riots and the 2014 and 2016 reforms NOT FOUND (not verified this session). No 2026 protests surfaced in searches. Amnesty's July 2024 report of more than 100 detained over protest calls is **[S]**.

**9. Fuel oil and load-shedding.**
- "Egypt's power plants consumed 7.49 mn tons of heavy fuel oil in FY 2024/25, up almost 30% y-o-y from 5.74 mn tons"; diesel about 253 kt, +152% (EEHC via Ent-Blackout). Medium-high.
- Ember "other fossil" generation: 8.0 TWh (2022), 16.6 (2023), 24.0 (2024), 23.9 (2025).
- Load-shedding: the government put "a USD 1.18 bn price tag on the gas and mazut imports" in June 2024 (Ent-Blackout). Start in July 2023, two-hour rolling cuts and the halt from 21 July 2024 are **[S]** (Al Arabiya, Ahram).

## C. Renewables and contracts

**10. Benban.**
- Capacity: "a planned total capacity of 1.8 GW" (EBRD, 20 Oct 2017). https://www.ebrd.com/home/news-and-events/news/2017/ebrd-and-partners-support-egypts-largest-solar-portfolio.html . About 1,465 MW operating is **[S]**.
- Cost: "Estimated Cost: USD 2 billion", about 1,800 MW, 25-year PPAs (ECES Policy Paper II, January 2026). https://eces.org.eg/wp-content/uploads/2026/01/A-Series-of-Policy-Papers-on-Renewable-Energy-Policy-Paper-II-A-Surf-Through-Egypts-Renewable-Energy-Projects-1998-2025.pdf . US$4bn: NOT FOUND.
- Financiers: EBRD US$500m framework for 16 projects (750 MW), with GCF, FMO, IsDB and ICD. IFC-led US$653m for 13 plants (752 MW) is **[S]**.
- Feed-in tariff of 8.4 US cents/kWh (round 2, 20–50 MW), paid in pounds with partial dollar indexation, is **[S]**.
- Sovereign guarantee of EETC's obligations: NOT FOUND.

**11. Recent PPAs.** Every project found sells to EETC under a 25-year PPA; most tariffs are undisclosed.

| Project | Size | Tariff | Cost and finance | Currency, guarantee | Source |
|---|---|---|---|---|---|
| Kom Ombo (ACWA) | 200 MW solar | "2.47 Cent USD/kwhr" | US$163m; completed 8 July 2024 | Not stated | https://acwapower.com/en/what-we-do/projects/kom-ombo-pv/ |
| Suez Wind (ACWA) | 1.1 GW | NOT FOUND | US$1.5bn (page also says US$1.1bn); about $704m debt **[S]** | "EETC acts as the sole off-taker" | https://acwapower.com/en/what-we-do/projects/suez-wind-energy-11-gw/ |
| ACWA Red Sea wind | 2 GW | "$2.4 cents per kilowatt-hour" | Not stated | Not stated | Zawya citing Asharq, undated 2026: https://www.zawya.com/en/projects/utilities/egypt-to-buy-electricity-from-red-sea-wind-farm-at-24-cents-kwh-eg8byp2s |
| Scatec Obelisk | 1.1 GW solar + 100 MW/200 MWh | Not disclosed | $590m capex; $479.1m debt from EBRD, AfDB, BII | "25-year, US dollar-denominated PPA"; "The PPA is backed by a sovereign guarantee" | pv magazine, 17 Apr 2026: https://www.pv-magazine.com/2026/04/17/the-financial-strategy-behind-egypts-largest-solar-plus-storage-project/ |
| Red Sea Wind Energy (Engie) | 650 MW | NOT FOUND | JBIC about $240m **[S]** | Finance ministry backs EETC **[S]** | Search summary |
| Scatec Shadwan wind | 900 MW | NOT FOUND | EBRD up to $192m proposed **[S]** | US dollar, sovereign guarantee **[S]** | Search summary |
| AMEA Abydos | 500 MW solar + 300 MWh | NOT FOUND | IFC $72m for the battery **[S]** | Not found | Search summary |
| AMEA Amunet wind | 500 MW | NOT FOUND | USD 700m; operating May 2025 | Not found | ECES paper II |

- One search summary named Egypt Aluminium as Obelisk's offtaker; that appears to be a separate Scatec project.
- Scatec's 5 GW wind deal: status NOT FOUND.
- Storage: first utility-scale battery (300 MWh) commissioned July 2025 (IMF-56R). Agreements "will add 17.4 GW in 2027 and 2028, together with 13.8 GWh of battery storage" (IMF-7R). Other storage deals are **[S]**: AMEA standalone 1,500 MWh (about USD 800m), Scatec 1.95 GW + 3.9 GWh PPA (January 2026), Nefer Menya 1.2 GW + 600 MWh (USD 566m debt, October 2026).
- ECES cites proposed Zafarana hybrid targets of about 2.0 cents (solar) and 2.4 cents (wind).

**12. NWFE energy pillar.**
- Target: "Egypt aims to replace 5 GW of thermal energy with 10 GW of renewable energy" (IMF-56R).
- Progress at March 2026 (EBRD page above): US$5bn of private investment mobilised, "half of its target for the end of 2028"; 5.15 GW mobilised; "more than 10 GW of renewable energy power purchase agreements (PPAs) have been signed", almost 6 GW at financial close; "More than 1 GW of inefficient fossil fuel generation has been permanently closed." Medium-high.
- Donor pledge amount: NOT FOUND (the page implies US$10bn only as a private-investment target).

**13. Capacity factors.** Published figures NOT FOUND. Crude fleet averages from Ember 2025 generation over year-end capacity (my arithmetic): wind about 37%, solar about 30%. Low.

**14. Green hydrogen.** SCZONE "has attracted $64bn in green hydrogen investments through 12 framework agreements" (18 mt a year projected); 30 MoUs signed, 14 active (SCZONE chairman; Daily News Egypt, 23 Dec 2024). https://www.dailynewsegypt.com/?p=825818 . Medium; these are pledges.

## D. Macro and finance

**15. GDP, growth, population (WEO, fiscal years). High.**

| WEO year | Fiscal year | GDP (US$ bn) | Real growth | Population (m) |
|---|---|---|---|---|
| 2024 | FY2023/24 | 383.1 | 2.4% | 106.6 |
| 2025 | FY2024/25 | 364.6 | 4.4% | 107.9 |
| 2026 | FY2025/26 | 442.9 | 5.1% | 110.1 |
| 2027 | FY2026/27 | 486.2 | 4.7% | 112.3 |

- IMF-7R (July 2026) had growth of 4.6% for FY2025/26 and 4.4% for FY2026/27, and EGP GDP of 18,136bn (FY2024/25) and 21,407bn (FY2025/26).
- Table 13 of both IMF reports shows "Nominal GDP 499.8" (US$ bn), which is inconsistent with the rest; ignore it.

**16. Debt, interest, financing needs.**
- General government gross debt, programme definition (IMF-7R): 90.9% of GDP FY2023/24; 86.8% FY2024/25; 85.6% FY2025/26 estimate; 82.8% FY2026/27. WEO: 86.8% (2025), 84.0% (2026).
- IMF debt-sustainability definition: 91.8% FY2024/25, 91.1% FY2025/26.
- Budget-sector debt (MoF-Debt): 85.6% of GDP June 2025, 77.1% December 2025.
- Interest, budget sector (IMF-7R): EGP 1,363bn (9.8% GDP) FY2023/24; 1,919bn (10.6%) FY2024/25; 3,049bn (14.2%) FY2025/26 estimate; 3,056bn (12.0%) FY2026/27. The IMF notes a definitional break from FY2024/25, when accrued interest is included.
- Interest relative to revenue:
  - IMF text: "interest payments absorb about 73 percent of revenues" and "Interest payments absorb roughly 83 percent of tax revenues" (IMF-56R).
  - My ratios from Table 3a: FY2024/25 72.5% of revenue and 87% of tax revenue; FY2025/26 estimate 94.6% and 109%.
- External debt (IMF-7R Table 2a): US$161.2bn end-June 2025 (44.2% of GDP); US$163.0bn estimated end-June 2026 (37.4%). Central bank releases of US$163.9bn and US$164.8bn are **[S]**, with conflicting date labels.
- External budget-sector debt: US$76.4bn at December 2025 (MoF-Debt).
- Gross financing needs (IMF-7R): 35.3% of GDP FY2024/25; "expected to peak at about 42.0 percent of GDP in FY2025/26"; 36.2% FY2026/27. High.

**17. Rates, inflation, exchange rate.**
- Policy rate: on 29 Oct 2026 the central bank raised 100 bp, the first rise since March 2024. Deposit 20.0%, lending 21.0%, main operation 20.5%. This followed 825 bp of cuts in six moves from April 2025, implying a 27.25% deposit rate before. Next meeting 17 Dec 2026 (Ent-CBE). High.
- IMF-7R end-June main-operation rates: 27.75% (2024), 24.5% (2025), 19.5% (2026).
- T-bills: 364-day cleared at 26.08% and 182-day at 25.46% on 29 Oct 2026 (Ent-CBE).
- Inflation: urban headline 13.9% and core 14.1% in September 2026 (Ent-CBE). October urban 12.7% and core 13.1% are **[S]** but consistent across outlets. June 2026 was 14.3% (IMF release of 30 July 2026).
- Exchange rate: central bank selling rate 56.12 per dollar on 29 Oct 2026, a record low (Ent-CBE); midpoint 54.70 on 5 Nov 2026 (Rio Times). About 53.4–53.9 in mid-November and about 47.7 in late February 2026 are **[S]**. The March 2024 float level was not verified.

**18. Ratings and Eurobonds.**
- Ratings, all **[S]** but consistent across outlets: Moody's B3 (raised from Caa1 on 16 Oct 2026, outlook positive); S&P B/B stable (affirmed October 2026); Fitch B stable (October 2026). Medium.
- 10-year Eurobond yield: NOT FOUND.
- Spread: JPMorgan sovereign spread 322 bp in mid-August 2026, lowest since 2014, and 5-year CDS about 269 bp are **[S]** (Enterprise, 20 Aug 2026).
- Recent issues:
  - May 2026: $1bn 8-year social bond at 7.625% (guidance about 8%, orders about $3.9bn) **[S]**.
  - June 2026: Samurai, JPY 80bn (USD 500m), 5-year at 2.87% and 10-year at 3.5% (EnterpriseAM, 1 July 2026; opened; details under item 19).
  - FY2024/25 and after: "Egypt issued US$3 billion in Eurobonds and Sukuks during FY2024/25, and a $1.5 billion in Sukuks in October 2025" (IMF-56R).
  - 3 Nov 2026: $500m tap **[S]**.

**19. Guaranteed and labelled issues.**
- Panda bond, October 2023: RMB 3.5bn; guarantees from AIIB and AfDB "helped attract investors and secured competitive terms" (AIIB, 25 Oct 2023). https://www.aiib.org/en/news-events/news/2023/AIIB-AfDB-Guarantee-Africa-s-First-Sustainable-Panda-Bond.html . Three-year tenor, 3.51% coupon and guarantee caps (AfDB up to US$345m, AIIB up to US$200m) are **[S]**.
- Samurai bonds:
  - March 2022: JPY 60bn, insured by NEXI (AFC page). The 0.85% coupon and SMBC guarantee are **[S]**.
  - November 2023: JPY 75bn, 5-year, 1.5%, SMBC guarantee with full AFC re-guarantee. "The pricing was made possible by the guarantee provided by Sumitomo Mitsui Banking Corporation"; the structure was "significantly lowering the country's all-in cost of the funding". https://www.africafc.org/news-and-insights/news/afc-supports-the-egyptian-government-as-re-guarantor-on-jpy75-billion-samurai-bond-issue
  - June 2026: JPY 80bn, with a USD 620m AfDB partial credit guarantee; rated AA+/AA by JCR. https://enterpriseam.com/egypt/2026/07/01/egypt-raises-usd-500-mn-in-afdb-backed-samurai-bonds/
- Green bond, 29 Sep 2020: $750m, 5-year, 5.25% (guidance 5.75%, upsized from $500m) is **[S]** (Bloomberg, World Bank). No measured greenium found.
- Did guarantees lower the coupon? MoF-Debt says "Guaranteed issuances… allow Egypt to access markets at more favorable pricing and extend average time to maturity". Compare 1.5–3.5% guaranteed yen and yuan coupons with 7.6% unguaranteed dollars; this is not currency-adjusted. Medium.

**20. Swap lines and partners.**
- China: renewed 3 June 2026 and "expanded from the previous 18 billion yuan (2.65 billion U.S. dollars) to 30 billion yuan"; valid three years (Xinhua on gov.cn). https://english.www.gov.cn/news/202606/03/content_WS6a202aa0c6d00ca5f9a0b633.html . High. Original signing in December 2016 is **[S]**.
- UAE: AED 5bn swap signed September 2023 and renewed for five years on 29 Sep 2026 is **[S]** (central bank page returned 403).
- Ras El-Hekma: the US$35bn headline was not verified on an opened page. IMF-7R shows net FDI of US$45.6bn in FY2023/24 and "USD 11 bn of UAE deposits converted in FY23/24".
- India and Saudi local-currency arrangements: NOT FOUND.
- BRICS membership from January 2024 is **[S]**.
- NDB: admitted 29 Dec 2021 (NDB release). https://www.ndb.int/news/ndb-admits-egypt-as-new-member/ . Effective membership date is **[S]** (2023).

**21. IMF programme.**
- Fifth and sixth EFF reviews and first RSF review completed 25–26 Feb 2026: about US$2bn (SDR 1,465.44m) plus US$273m RSF. EFF "extended through December 15, 2026". https://www.imf.org/en/news/articles/2026/02/26/pr-26064-egypt-imf-completes-5th-and-6th-revs-under-ext-arrange-under-eff-and-1st-rev-under-rsa
- Seventh EFF and second RSF reviews completed 30 July 2026: SDR 1.11bn (about US$1.5bn) plus SDR 200m. Total to date SDR 5.4bn (about US$7.3bn). https://www.imf.org/en/news/articles/2026/07/30/pr26271-egypt-imf-completes-the-7th-review-under-eff-and-2nd-review-under-the-rsf . High.
- Final review: mission in Cairo in the week of 29 Oct 2026; Board targeted by mid-December; about US$2.3bn remaining (The National, 29 Oct 2026). https://www.thenationalnews.com/news/us/2026/10/29/imf-sets-december-target-to-clear-egypts-last-programme-review/ . Staff-level agreement as of 20 Nov: NOT FOUND.
- The US$8bn and US$1.3bn programme sizes were not re-verified on an opened page.

**22. World Bank exposure and operations.**
- IBRD loans outstanding to Egypt: US$12.38bn at 31 Oct 2026, with US$2.31bn undisbursed. This is my aggregation of the World Bank "IBRD Statement of Loans" snapshot; Egypt ranks 11th. https://datacatalogapi.worldbank.org/dexapps/fone/api/apiservice?datasetId=DS00047&resourceId=RS00049&type=json . Medium-high.
- Single-borrower limit: "the FY26 SBL is $31.7 billion for highly creditworthy countries below the GDI, and $22.6 billion" above it (IBRD MD&A, 31 Mar 2026). https://thedocs.worldbank.org/en/doc/4f8e88be21bdf2e7dddfae2cd6e3e30b-0040012026/original/IBRD-Financial-Statements-March-2026.pdf . Egypt is at about 39% of the higher limit, so not near it.
- Egypt was not in IBRD's top ten exposures at March 2026 (tenth was Morocco, US$11.9bn).
- IMF Table 13 shows World Bank claims of US$13.0bn at end-June 2025; the difference from the IBRD figure is unreconciled.
- Recent operations:
  - World Bank GROWTH II policy loan, US$1bn, 8 May 2026, including "a US$200 million credit guarantee from the United Kingdom". https://www.worldbank.org/en/news/press-release/2026/05/08/new-us-1-billion-world-bank-group-development-financing-to-support-egypt-s-private-sector-led-job-creation-macroeconomic
  - EIB €600m grid loan (item 5).
  - EBRD, AfDB and BII $479.1m for Obelisk (item 11).
  - EETC being unbundled from EEHC to become an independent system operator (IMF-7R).
  - EBRD €200m to EETC (December 2025) is **[S]**.
- A World Bank private-sector payment guarantee in energy: NOT FOUND.

**23. Cost of capital.**
- Damodaran, 5 Jan 2026: Egypt rated Caa1; default spread 6.37%; country risk premium 9.71%; total equity risk premium 13.94%; CDS spread 3.41%. https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html . High.
- IMF effective interest rate on public debt: 13.5% (FY2024/25), 18.2% (FY2025/26).
- IRENA 2023 Egypt values, IEA Cost of Capital Observatory, Ameli et al., Steffen 2020: NOT FOUND (page 403, search budget exhausted).

**24. State enterprises.**
- EGPC arrears to international oil companies: US$6.2bn in October 2024; about US$2.1bn in December 2025; "By June 2026, EGPC cleared all outstanding arrears". Clearance was funded by guaranteed EGPC borrowing and "budgetary transfers (EGP 167 billion through March 2026) both to EGPC and EEHC" (IMF-7R).
- FY2025/26 budget: "EGP 75 billion directly to EGPC and an additional EGP 75 billion to EEHC to clear its payables to EGPC"; guarantees to EGPC "currently at 18 percent of GDP", to fall 25% in FY2026/27 (IMF-56R). High.
- Finance ministry settled EGP 166bn of unpaid subsidy reimbursements in May 2026 (Ent-Cost).
- Military firms: "military encroachment in various economic activities appears to persist" (IMF-56R). Divestment proceeds to date about US$520m (IMF release, 30 July 2026).
- State Ownership Policy: adopted, per the July 2026 release. A draft second edition for 2026–2030 is **[S]**.
- EEHC total debt and EGAS figures: NOT FOUND.

**25. Pensions and demography.**
- Treasury instalment to NOSI: "EGP 238.55 billion in FY2025/26", then rising 6.4% a year, stepping up to 7% by July 2029; "Law No. 11 of 2026" (Business Today Egypt, 7 June 2026). https://www.businesstodayegypt.com/amp/1/7568/El-Sisi-approves-higher-treasury-payments-to-social-insurance-fund . Medium.
- IMF-7R "Transfer to SIF": EGP 143bn FY2024/25, 151bn FY2025/26, 169bn FY2026/27; different coverage, unreconciled.
- NOSI investment assets of about EGP 732bn, the 50-year settlement and Law 148/2019 details are **[S]**.
- Median age and working-age share: NOT FOUND. Population as in item 15.

**26. CCDR and NDC costing.**
- CCDR (World Bank, 8 Nov 2022). https://documents1.worldbank.org/curated/en/099510011012235419/pdf/P17729200725ff0170ba05031a8d4ac26d7.pdf . High.
  - "The total investment needs between 2022 and 2030, are estimated to be USD$105 billion (at 2022 real prices)". This is the cities scenario only, not economy-wide.
  - Breakdown: urban mobility US$57bn; green housing and efficiency 32.4bn; waste 8.4bn; drainage and nature-based solutions 5.6bn; urban water 1.65bn. Annualised US$11.7bn.
  - Power: "Achieving the NZ100 pathway requires US$96 billion (+85%) of additional investment in electricity generation supply and storage over the 2030-2050 horizon". Current-policy path needs "up to US$113 billion in cumulative investments by 2050" beyond 2030.
  - Net-zero system cost +US$44bn, or US$29bn net of fuel savings.
  - Subsidies: electricity about US$8bn plus diesel about US$4bn, "about 3% of GDP".
- NDC: "estimated at minimum USD 246 billion. The mitigation interventions require USD 196 billion and the adaptation interventions require USD 50 billion", conditional on international finance (NDC PDF above). High.

**27. CBAM.** "Egypt is among the top six countries exporting CBAM-covered goods to the EU, with an estimated 6 percent of its 2022 exports (especially fertilizers, cement, steel, aluminum) falling within CBAM's scope… real income could shrink by ~0.6 percent… up to an 8.3 percent drop in exports of certain carbon-intensive products" (World Bank letter, IMF-56R). High. Fertiliser exports to the EU of $1.6bn (2022) and $993m (2023) are **[S]**.

## Not verified
- 2: an official surplus or reserve-margin figure; the 64.4 GW and 40,200 MW readings (**[S]**).
- 5: whether the Saudi link is in commercial operation; EETC budget figures.
- 6: average tariff and unit cost of supply.
- 7: current gas price to power plants; share of gas used in power; calendar-year LNG bills for 2024 and 2025; contract price of Israeli gas.
- 8: FY2026/27 fuel allocation (**[S]**); 2024 price-rise dates; 1977, 2014 and 2016 history; any 2026 protests.
- 9: load-shedding start and end dates (**[S]**).
- 10: Benban tariff, payment currency, IFC amount, sovereign guarantee, US$4bn cost.
- 11: tariffs for every project except Kom Ombo and ACWA's 2 GW wind; finance ministry guarantee for Red Sea Wind and Shadwan (**[S]**); battery contract prices.
- 12: donor pledge amounts.
- 13: published capacity factors.
- 17: March 2024 float level; October 2026 inflation on an opened page.
- 18: 10-year Eurobond yield; current spread; ratings and the May 2026 bond on an opened page.
- 19: Panda coupon and tenor, 2022 Samurai coupon, green bond terms (**[S]**).
- 20: Ras El-Hekma US$35bn; UAE swap details; India and Saudi arrangements; BRICS and NDB effective dates.
- 21: final-review staff-level agreement; headline programme sizes.
- 22: a World Bank private-sector guarantee; the IMF versus IBRD exposure gap.
- 23: IRENA, IEA and academic cost-of-capital estimates.
- 24: EEHC and EGAS debt.
- 25: NOSI assets; median age and working-age share.
