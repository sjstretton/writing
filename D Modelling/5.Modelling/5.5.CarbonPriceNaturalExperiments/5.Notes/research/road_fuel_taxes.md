# Road-fuel tax increases as natural experiments (US states, Germany, UK, Ireland): ex post evidence

Scope: ex post evidence on road-fuel tax rises in high-income countries other than Sweden and British Columbia. Researched 1 November 2026. Numbers are quoted from full texts I downloaded and read unless marked "abstract only" or "snippet only". Working-paper (WP) versions were read where the journal version is paywalled. Treat page and table numbers as WP numbers unless stated. Anything not checked is marked [VERIFY: reason].

## Which candidates have the strongest ex post evidence, and which should the paper document fully?

### Takeaway
Document fully: (1) **US state gasoline taxes**, the strongest case: peer-reviewed, hundreds of tax changes, several methods, standard errors. (2) **Germany's Ökosteuer, 1999–2003**: one peer-reviewed synthetic-control study plus a working-paper programme using SCM, generalised SCM and synthetic difference-in-differences, all pointing to transport CO2 about 10–16% below the counterfactual. (3) The **UK fuel duty escalator** is a weaker third: one peer-reviewed SCM study, with a questionable donor pool. For **BEHG (2021)** and **Ireland (2010)** I found no credible causal ex post estimate of the effect on fuel use or emissions. The official BEHG evaluation says outright that such an estimate cannot be done seriously.

### Cited Findings
- US: Davis and Kilian's preferred estimate uses 210 state-month nominal tax increases, January 1989 to March 2008 (Table 4, col. 4, p. 29): elasticity −0.46 (SE 0.23) — [Davis & Kilian NBER WP 14685](https://www.nber.org/system/files/working_papers/w14685/w14685.pdf). Li, Linn and Muehlegger use 2,064 state-years, 1966–2008. Over that period state taxes "rose in 488 state-years and fell in 44" — [Li, Linn & Muehlegger NBER WP 17891, p. 9](https://nber.org/system/files/working_papers/w17891/w17891.pdf).
- Germany Ökosteuer: peer-reviewed SCM finding "the carbon price increase by about 66 €/t CO2 led to a considerable decline of transport emissions by 0.2–0.35 t per person and year" — [Runst & Höhle 2022, Energy Policy (abstract)](https://ideas.repec.org/a/eee/enepol/v160y2022ics0301421521005206.html). WP evidence: "emission gaps in the transport sector of around 10% for CO2" over 1999–2009 — [Basaglia, Behr & Drupp 2023, DIW DP 2041, p. 2](https://www.diw.de/documents/publikationen/73/diw_01.c.875084.de/dp2041.pdf).
- UK escalator: SCM "average treatment effect in the treated time frame is 0.352 metric tons of CO2 per capita" — [Bretschger & Grieg 2020 WP, §3.4.1](https://www.ethz.ch/content/dam/ethz/special-interest/mtec/cer-eth/cer-eth-dam/documents/working-papers/WP-20-332.pdf). Published as Energy Policy 195 (2024) 114359; abstract only seen — [IDEAS](https://ideas.repec.org/a/eee/enepol/v195y2024ics0301421524003793.html).
- BEHG: the UBA report behind the government's second statutory evaluation (§23 BEHG) says that, "Aufgrund der Vielzahl bestehender Klimaschutzinstrumente und dem vergleichsweisen kurzen bisherigen Bestehen des nEHS ist die empirische ex-post Abschätzung der hier betrachteten Minderungswirkungen nicht seriös leistbar, weswegen hier ex-ante modelliert wird." In English: because of the many other climate instruments and the short life of the national ETS so far, an empirical ex post estimate of these reductions cannot seriously be done, so they are modelled ex ante — [UBA Climate Change 59/2024, p. 40](https://foes.de/publikationen/2024/2024-12_FOES_BEHG.pdf).
- Meta-evidence for context: 80 causal ex post evaluations across 21 carbon pricing schemes show statistically significant reductions of "–5% to –21% across the schemes (–4% to –15% after correcting for publication bias)" — [Döbbeling-Hildebrandt et al. 2024, Nat. Commun. 15:4147 (abstract)](https://doi.org/10.1038/s41467-024-48512-w). Green (2021) finds 37 ex post studies, with reductions "generally between 0% and 2% per year" — [Green 2021, ERL 16:043004 (abstract)](https://doi.org/10.1088/1748-9326/abdae9).

### Inferences
- The US case gives the cleanest **elasticity** evidence but not a single "episode". Its outputs answer "what does a 10 c/gal (~US$11/t) tax rise do within a year?" The German case gives an **episode-level** counterfactual: a ramp to about €65/t (petrol) and €57/t (diesel) over five years, with CO2 gaps measured to 2005–2009.
- The UK and German SCM estimates (0.35 t and 0.2–0.42 t per capita per year) are close to Andersson's Sweden estimate of 0.29 t, as Bretschger and Grieg themselves note. Treat this agreement cautiously: all three rely on country-level transport CO2 built from fuel sales (see the caveats section).

### Gaps
- I found no synthetic-control or DiD study that isolates a single US state tax episode as a case study. The US evidence is all pooled panels or IV.

## Conversion conventions: which emission factors and arithmetic are used?

### Takeaway
Petrol/gasoline: **8.887 kg CO2 per US gallon = 2.348 kg/l** (EPA). Diesel: **2.676 kg/l** (UBA's German factor). Sensitivity: UBA's German petrol factor is 2.401 kg/l. Carbon-price equivalent = tax per litre (or gallon) ÷ kg CO2 per litre (or gallon). German VAT on fuel was 16% in 1999–2003 [VERIFY: 16% standard rate from 1 April 1998 to end-2006, not re-checked this session] and 19% in 2021.

### Cited Findings
- "Every gallon of gasoline burned creates about 8,887 grams of CO2" — [US EPA](https://www.epa.gov/greenvehicles/greenhouse-gas-emissions-typical-passenger-vehicle). Dividing by 3.785 l per US gallon gives 2.348 kg/l (my arithmetic).
- UBA petrol: "73,1 kg CO2 / GJ … Heizwert 43,5 GJ/t … Dichte 0,755 kg/l", so €25/t = 6.00 ct/l (this implies 2.401 kg/l). UBA diesel: "74 kg CO2/GJ … 42,8 GJ/t … 0,845 kg/l", so €25/t = 6.69 ct/l (this implies 2.676 kg/l) — [UBA Climate Change 45/2022, fn. 9–10, pp. 28–31](https://www.umweltbundesamt.de/system/files/medien/1410/publikationen/2022-12-02_climate-change_45-2022_wirkung-nat-brennstoffemissionshandel.pdf).
- Basaglia et al. use 2.235 kg/l (gasoline) and 2.66 kg/l (diesel) in their emission simulations — [DIW DP 2041, fn. 29](https://www.diw.de/documents/publikationen/73/diw_01.c.875084.de/dp2041.pdf). Their stated eco-tax carbon costs, €66/t gasoline and €58/t diesel, imply about 2.33 and 2.65 kg/l (my back-calculation).

### Inferences
- Worked conversions (my arithmetic):
  - 1 US c/gal = US$1.125/tCO2.
  - 5 c/gal = US$5.63/t.
  - 10 c/gal = US$11.25/t. Davis and Kilian (p. 1) say "$10.00 per ton of carbon dioxide … would increase gasoline taxes by approximately 9 cents", which is consistent.
  - 3.07 €ct/l petrol = €13.1/t (2.348) or €12.8/t (2.401).
  - 3.07 €ct/l diesel = €11.5/t (2.676).
- Choosing among the emission factors shifts the German petrol carbon price by about ±€1–2/t. That is immaterial for the argument.

### Gaps
- I did not confirm EPA's diesel factor (10,180 g/gal) in this session, so diesel uses UBA's factor.

## US state gasoline taxes: tax changes, retail prices, carbon-price equivalent, and ex post effects on fuel use and CO2

### Takeaway
State tax changes are small: most are under 10 c/gal, about 3–6% of the pump price and about US$1–11/tCO2. Instrumenting with them, Davis and Kilian (2011) estimate that a **10 c/gal (≈US$11/t) tax rise cuts gasoline use by 1.43% (SE 0.72) within about a year**. That is "about 1.5%" of vehicle CO2 and 0.48% of total US CO2. Li, Linn and Muehlegger (2014) find a **5 c/gal tax rise cuts consumption by 0.86% (SE 0.25)**, about three times the effect of an equal market price rise. Coglianese et al. (2017) show that anticipatory buying around tax dates inflates tax-IV estimates; correcting for it gives an elasticity of **−0.37 (SE 0.24, not significant)**.

### Cited Findings
**Tax changes and price context**
- Average nominal prices and taxes by period, US cents per gallon (cpg) (Li et al. Table 1, p. 58):

  | Period | Tax-inclusive retail price | State tax | Federal tax | Tax share of retail price |
  |---|---|---|---|---|
  | 1986–90 | 98.0 | 15.1 | 10.1 | 25.7% |
  | 1991–95 | 113.9 | 19.1 | 16.7 | 31.4% |
  | 1996–2000 | 125.0 | 20.3 | 18.4 | 30.9% |
  | 2001–05 | 163.3 | 20.8 | 18.4 | 24.0% |
  | 2006–08 | 278.0 | 21.8 | 18.4 | 14.5% |

  Source: [Li, Linn & Muehlegger WP 17891](https://nber.org/system/files/working_papers/w17891/w17891.pdf).
- "Most tax changes are fairly small, typically less than 10 cents per gallon" (p. 3). In 2008 Georgia's excise tax was 7.5 cpg and Washington's 37.5 cpg. "At the median, taxes make up approximately 26 percent of the after-tax price" (p. 9) — [Li et al. WP](https://nber.org/system/files/working_papers/w17891/w17891.pdf).
- Davis and Kilian: of 11,730 state-month observations in January 1989 to March 2008, "only 268 were strict changes", of which 210 were nominal increases (pp. 9–10; Table 4). Sample means were an after-tax price of $1.81/gal and a tax of $0.45/gal. Estimated pass-through was "113% of the tax … shifted to prices with a standard error of 7%" (fn. 12) — [Davis & Kilian WP](https://www.nber.org/system/files/working_papers/w14685/w14685.pdf).

**Davis and Kilian (2011)**
- Method: monthly state panel, Jan 1989 to Mar 2008, with gasoline price instrumented by state gasoline taxes. Ad valorem taxes are excluded from the instrument. They also report OLS and structural VARs — [Davis & Kilian WP](https://www.nber.org/system/files/working_papers/w14685/w14685.pdf).
- OLS price elasticity: −0.10 (national) and −0.19 (state panel) (Table 1). State-panel IV on all months: −1.14, with a Moreira 95% CI of [−1.45, −0.86] (p. 9).
- Restricting the IV to months with nominal tax changes (Table 4, p. 29):
  - all changes: −0.74 (0.38), n=268;
  - **nominal increases only: −0.46 (0.23)**, first-stage F 30.6, n=210;
  - increases of at least 1 cent: −0.42 (0.23);
  - increases of at least 2 cents: −0.28 (0.38).
- Their view of the preferred estimate: "We view this estimate as the most credible estimate of the likely effect of proposed gasoline tax increases" (p. 10). Elsewhere: it "provides a plausible upper bound on the likely effects … within a year" (p. 19). Robustness (Table 5): −0.47 (median IV), −0.49, −0.43, −0.45 with controls.
- Effect of a 10 c/gal tax, evaluated at the March 2008 volume-weighted after-tax price of $3.21 (Table 6, p. 31):
  - OLS national: −0.31% (0.11);
  - OLS panel: −0.59% (0.12);
  - **IV panel: −1.43% (0.72)**.
  - "If instead the effects are evaluated at this lower base level [$1.75, Dec 2008], the effect … is approximately twice as large" (p. 13).
- SVAR 12-month elasticities (Table 7): price elasticity −0.12; tax elasticity −0.13 (12 lags) and −0.15 (AIC lags).
- CO2: "(−1.43%)0.338 = −0.48%" of total US CO2, where 0.338 is transport's share of US CO2. "one can rule out carbon emission decreases in excess of 1.0% with 95% confidence" (pp. 19–20). In the intro: "decrease U.S. carbon emissions from the transportation sector by about 1.5% and decrease total U.S. carbon emissions by about 0.5%" (p. 1) — [Davis & Kilian WP](https://www.nber.org/system/files/working_papers/w14685/w14685.pdf).
- The published abstract confirms: "a 10‐cent per gallon increase in the gasoline tax would reduce carbon emissions from vehicles in the United States by about 1.5%" — [Davis & Kilian 2011, JAE 26(7):1187–1214, via Crossref](https://doi.org/10.1002/jae.1156).

**Li, Linn and Muehlegger (2014)**
- Method: annual state panel, 1966–2008, 2,064 obs. Dependent variable is log gasoline per adult. Log price is split into log(tax-exclusive price) and log(1 + tax/tax-exclusive price). Controls: state and year fixed effects, covariates, state quadratic trends. Data from FHWA Highway Statistics — [Li et al. WP](https://nber.org/system/files/working_papers/w17891/w17891.pdf).
- Benchmark (Table 2, cols. 7–8; standard errors clustered by state):
  - tax-inclusive price elasticity: **−0.097 (0.037)**;
  - coefficient on log(tax-exclusive price): **−0.113 (0.038)**;
  - coefficient on log(1+tax ratio), the tax elasticity: **−0.292 (0.084)**;
  - test of equality: p = 0.009.
- Effect of $0.05/gal, evaluated at 1988 means (tax 24.1 cpg, tax-exclusive price 69.2 cpg, "inflated to 2008 dollars"):
  - price rise: **−0.286% (0.109)**;
  - tax rise: **−0.864% (0.248)**;
  - test of equal effects: p = 0.033.
  - The text says the tax effect is "three times as large" (p. 4) — [Li et al. WP, Table 2, pp. 59–60](https://nber.org/system/files/working_papers/w17891/w17891.pdf).
- IV version (Table 4, col. 6), instrumenting with 1966 tax-exclusive price × crude price and (1 + tax/crude price): tax-exclusive −0.0697 (0.0240) and tax −0.323 (0.0828). A 5c tax rise gives −0.955% (0.245); a 5c price rise gives −0.148% (0.076).
- Other margins: tax rises are associated with larger MPG gains in newer vehicles (p = 0.03 in the newer-vehicle sample). There are "no statistically significant differential effects on VMT"; the VMT price elasticity is −0.39 in the preferred specification (pp. 35–37). The published abstract says "consumers respond more strongly to gasoline tax changes under a variety of model specifications" and gives no numbers — [AEJ: Policy 6(4):302–42](https://www.aeaweb.org/articles?id=10.1257/pol.6.4.302).

**Coglianese, Davis, Kilian and Stock (2017)**
- Buyers "increase gasoline purchases before tax increases and delay gasoline purchases before tax decreases", which makes the tax instrument endogenous — [Coglianese et al. NBER WP 20980, abstract](https://www.nber.org/system/files/working_papers/w20980/w20980.pdf).
- Same 11,730 state-months. Adding one lead and one lag gives a cumulative elasticity of **−0.368 (0.239)**, against **−1.135 (0.250)** with no leads or lags (Table 2). Alternative estimates: −0.29 to −0.41; GMM −0.31 to −0.36 — [WP 20980](https://www.nber.org/system/files/working_papers/w20980/w20980.pdf).
- Published in J. Applied Econometrics 32(1):1–15 (2017), according to the bibliography of [DIW DP 2041](https://www.diw.de/documents/publikationen/73/diw_01.c.875084.de/dp2041.pdf) [VERIFY: DOI 10.1002/jae.2500 not checked].

### Inferences
- Percentage price rises (my arithmetic):
  - 10 c/gal = 3.1% of $3.21 (March 2008) or 5.7% of $1.75 (December 2008).
  - 5 c/gal = 5.4% of the nominal 1988 mean tax-inclusive price (93.3 cpg). At 2008 dollars it would be roughly 3% [VERIFY: Li et al. say the 1988 means were inflated to 2008 dollars; my CPI factor of about 1.8 is not sourced].
- Reported as "tax elasticity of fuel use", the US range is about **−0.3 to −0.46**: Li et al. −0.29; Coglianese et al. −0.37 (n.s.); Davis–Kilian −0.46 (upper bound). The tax-exclusive or market-price elasticity is about −0.1 to −0.2.
- For a 10 c/gal (US$11/t) tax rise at $3.21/gal (my arithmetic):
  - Coglianese's −0.37 implies about −1.15% gasoline use;
  - Davis–Kilian's −0.46 implies −1.43%;
  - Li et al.'s 5c result, scaled linearly, implies about −1.7%.
  - All are short-run (about one year) effects.
- Possible overstatement in Davis–Kilian's total-CO2 figure: they multiply the gasoline change by transport's whole share of US CO2 (0.338). Diesel and jet fuel are part of that share, so the −0.48% total-US figure may overstate the effect of a gasoline-only tax [VERIFY: gasoline's share of US transport CO2 was not retrieved].

### Gaps
- I did not check the published JAE (2011) and AEJ (2014) tables against the WP numbers. The JAE abstract matches the WP headline (1.5%). Table numbering and values in the journal versions are [VERIFY].
- Kilian and Zhou (2023, FRB Dallas WP), "Heterogeneity in the pass-through from oil to gasoline prices…", reportedly finds that Li et al.'s tax elasticity "is not significantly different from tax-exclusive price elasticity in the US after accounting for anticipation effects". This is secondhand, from [DIW DP 2041, fn. 5](https://www.diw.de/documents/publikationen/73/diw_01.c.875084.de/dp2041.pdf). I did not see the paper.
- I found no US study that reports confidence intervals for CO2 directly, other than Davis–Kilian's statement ruling out reductions above 1.0% of total US CO2.

## Germany's Ökosteuer (1999–2003): tax path, retail prices, carbon-price equivalent, and ex post effects on fuel use and CO2

### Takeaway
Five steps of 6 Pf (3.07 ct) per litre on petrol and diesel added **15.34 ct/l net (about 17.8 ct/l with 16% VAT)**. That was about **22% of the 1998 petrol pump price and 30% of the diesel price**, or **€65/t (petrol) and €57/t (diesel)**. Two independent SCM studies estimate German transport CO2 at about **11–16% (2005)** and **8–13% on average over 1999–2009** below synthetic counterfactuals, or **0.2–0.42 t per capita**. The fuel-use effect appears with a lag of three to four years (−9.6% to −14.7% fuel per capita by 2005). Elasticity estimates suggest the tax had much larger effects than equal market price changes. Model-based government-commissioned studies (DIW/GWS) are not ex post evidence.

### Cited Findings
**Tax path and prices**
- "In each year between 1999 and 2003, the fuel tax on gasoline and diesel was increased by 3.07 cents (6 Pfennig) per liter. This led to a total tax increase of 15.35 cents per liter." The reform "came into effect in April 1999" — [Basaglia, Behr & Drupp 2023, DIW DP 2041, appendix p. 21](https://www.diw.de/documents/publikationen/73/diw_01.c.875084.de/dp2041.pdf). Runst and Höhle: "five annual tax increases by about 3 Euro Cents per liter … The cumulative taxation level of 15 cents/liter amounts to a quasi-carbon tax of about 66 Euro per ton of CO2" — [Runst & Höhle ifh WP 29/2021, §1](https://ifh.wiwi.uni-goettingen.de/site/assets/files/2239/ifh_wp-29_2021.pdf).
- "In 2003, implicit carbon costs due to the eco-tax amounted to €58 ($65) per tCO2 for diesel and €66 ($74) for gasoline" — [DIW DP 2041, p. 1](https://www.diw.de/documents/publikationen/73/diw_01.c.875084.de/dp2041.pdf).
- Post-2003 energy tax: "liegen die Sätze seit 2003 konstant bei 65,45 ct/l für Benzin, 47,04 ct/l für Diesel" ("rates have been constant since 2003 at 65.45 ct/l for petrol and 47.04 ct/l for diesel") — [UBA CC 45/2022, p. ~27](https://www.umweltbundesamt.de/system/files/medien/1410/publikationen/2022-12-02_climate-change_45-2022_wirkung-nat-brennstoffemissionshandel.pdf). This implies pre-reform rates of 50.11 ct/l (= 98 Pf) and 31.70 ct/l (= 62 Pf) (my arithmetic) [VERIFY: pre-1999 Mineralölsteuer rates not directly sourced].
- ADAC annual average pump prices ("bis 2001: Pfennig je Liter"; converted at 1.95583 DM/€ by me) — [ADAC table via Autoflotte](https://www.autoflotte.de/downloadfile/733714/SpritpreisEntwicklung.pdf):

  | Year | Super, Pf (ct) | Diesel, Pf (ct) |
  |---|---|---|
  | 1998 | 158.8 (81.2) | 114.4 (58.5) |
  | 1999 | 168.8 (86.3) | 124.4 (63.6) |
  | 2000 | 198.8 (101.6) | 156.9 (80.2) |
  | 2001 | 200.0 (102.3) | 160.3 (82.0) |
  | 2002 | 104.6 ct | 83.6 ct |
  | 2003 | 109.2 ct | 88.4 ct |

**Runst and Höhle (2022), peer-reviewed SCM**
- Published as Energy Policy 160:112655, DOI 10.1016/j.enpol.2021.112655. I saw the abstract of the published version and the full text of the WP.
- Abstract: "the carbon price increase by about 66 €/t CO2 led to a considerable decline of transport emissions by 0.2–0.35 t per person and year … the sales share of diesel cars quickly increases after the reform, whereas the fuel efficiency of non-diesel cars increases with a three-year time lag" — [IDEAS abstract](https://ideas.repec.org/a/eee/enepol/v160y2022ics0301421521005206.html).
- WP details:
  - Data set one: 23 European countries, 1993–2005.
  - Data set two: 25 countries worldwide, longer pre-period.
  - "The emissions reduction in Germany in 2005 amounts to 250 kg, or about 11.5% of transport emissions in 1999". Alternative specifications: "about 350 kg in 2005, i.e. a 16% decrease".
  - Donors are mainly France, the Netherlands and Switzerland.
  - Motor fuel per capita: "a lag of three to four years … In 2005, we observe a decline by 38 to 58 TOEs … a relative decline of 9.6% to 14.7%".
  - Diesel car share: "risen by 2% compared with the synthetic control group".
  - Placebo: only Poland shows a decline, and it is temporary (2001–03).
  - Passenger-km show no reduction.
  - The global placebo shows declines in Japan, France, Italy and the UK, which the authors attribute to later, separate causes.
  - Source: [Runst & Höhle WP, §3](https://ifh.wiwi.uni-goettingen.de/site/assets/files/2239/ifh_wp-29_2021.pdf).

**Basaglia, Behr and Drupp (2023), DIW DP 2041, working paper (not peer-reviewed)**
- SCM with 7 specifications. Main donor pool: 20 countries, 1971–2009. Austria and Luxembourg are excluded "due to non-negligible fuel tourism" (p. 12).
- "In 2007, this distance was on average -0.42 metric tons of CO2 per capita, equivalent to a 19 percent reduction. Between 1999 and 2009, annual emission reduction amounted to 0.23 metric tons of CO2 per capita on average, which cumulatively sums up to 208,216,572 tons of CO2" (p. 16).
- Range across specifications: "CO2 per capita emissions of the transportation sector decrease, on average, from 8.1% to 13.4% between 1999 and 2009" (p. 17).
- Inference: "mean joint two-sided p-values are below 5% for CO2" (p. 17).
- Generalised SCM, mean CO2 effect in t/cap (Table 2, p. 20):
  - **−0.43 [95% CI −0.53; −0.34]**;
  - −0.39 [−0.50; −0.25] (economic activity controls);
  - −0.44 [−0.57; −0.29] (EU-only donors).
- Co-benefits: PM2.5 −27% and NOx −13%; about €80 bn in avoided damages (p. 2).
- Annual German time series of fuel demand, 1971/72–2009 (38–39 obs):
  - real price elasticity: gasoline −0.54 (OLS) and −0.50 (IV); diesel −0.34 and −0.28 (p. 22);
  - "tax-exclusive price elasticity of demand for gasoline (diesel) of -0.32 (-0.26) and an eco-tax elasticity of demand of -2.7 (-1.1)" (p. 3);
  - the eco-tax semi-elasticity per cent/l is −0.0306 (SE 0.0070) for gasoline and −0.014 (SE 0.00359) for diesel (Table 4, col. 3, p. 24);
  - salience accounts for "around 70% (55%) of the observed contraction in gasoline (diesel) consumption" (p. 5);
  - adding a lead shows no anticipation effect (fn. 28).
  - Source: [DIW DP 2041](https://www.diw.de/documents/publikationen/73/diw_01.c.875084.de/dp2041.pdf).
- Later version: Basaglia, Behr and Drupp (2025), "Fuel Taxation and Environmental Externalities: Evidence from the World's Largest Environmental Tax Reform", CESifo WP 11949 / CEPR DP 20453. It uses synthetic DiD on "more than 1,000 European regions" and finds "sizable aggregate reductions for all emissions, exceeding 10 percent on average per year relative to synthetic baselines". Avoided external costs are "more than €100 billion, two-thirds of which stem from health benefits" — [IDEAS abstract only](https://ideas.repec.org/p/ces/ceswps/_11949.html).

**Model-based (not ex post)**
- The DIW's 2001 "Modellgestützte Analyse der ökologischen Steuerreform mit LEAN, PANTA RHEI und dem Potsdamer Mikrosimulationsmodell" (DP 248, Kohlhaas et al.) is a model-based analysis — [DIW DP 248 page (snippet only)](https://www.diw.de/de/diw_01.c.444280.de/publikationen/diskussionspapiere/2001_0248/modellgestuetzte_analyse_der_oekologischen_steuerreform_mit_lean__panta_rhei__und_dem_potsdamer_mikrosimulationsmodell.html). A DIW Economic Bulletin figure shows CO2 deviations of up to about −3% against a reference scenario, according to a search snippet — [DIW EB 2001](https://www.diw.de/documents/publikationen/73/diw_eb_2001-05-5.pdf) [VERIFY: figure not read].
- Knigge and Görlach (2005, Ecologic for UBA) and Kohlhaas (2005, DIW) draw on such model results [VERIFY: not opened; classed as model-based on that basis].

### Inferences
- Path by step (my arithmetic). Each step is 3.07 ct net, or 3.56 ct with 16% VAT. The step as a share of the previous year's average price:

  | Step | Super | Diesel | Cumulative carbon price, petrol (÷2.348) | Cumulative carbon price, diesel (÷2.676) |
  |---|---|---|---|---|
  | 1999 | +4.4% | +6.1% | €13 | €11 |
  | 2000 | +4.1% | +5.6% | €26 | €23 |
  | 2001 | +3.5% | +4.4% | €39 | €34 |
  | 2002 | +3.5% | +4.3% | €52 | €46 |
  | 2003 | +3.4% | +4.3% | €65 | €57 |

- Cumulative rise including VAT: 17.8 ct = 21.9% of the 1998 Super price and 30.4% of the 1998 diesel price. It was 16.3% and 20.1% of the 2003 prices.
- Most of the 1998–2003 rise in pump prices (Super +28 ct) came from crude oil, especially in 2000. The tax accounts for about 18 ct of it. So consumers saw large non-tax price movements at the same time.
- Read literally, the time-series eco-tax semi-elasticity (−3.06% per cent/l for gasoline) implies very large cumulative cuts in gasoline use. It is identified from one national annual series in which the tax ramp coincides with the switch from gasoline to diesel. Treat it as indicative of salience, not as a policy multiplier.
- Comparing the three SCM-type estimates: Runst–Höhle find −11.5% to −16% by 2005. Basaglia et al. find −8.1% to −13.4% on average over 1999–2009, and −19% in 2007. The regional SDID finds more than 10% per year. They are consistent in direction and broadly in size.

### Gaps
- Tax dates beyond "April 1999" and "each year 1999–2003" are [VERIFY: whether steps 2–5 took effect on 1 January].
- I did not retrieve Frondel and Vance (2014), "More pain at the diesel pump? An econometric comparison of diesel and petrol price elasticities", J. Transport Econ. & Policy 48(3):449–463. The reference comes from the DIW DP 2041 bibliography. It estimates general price elasticities from household data, not effects specific to the tax [VERIFY: abstract not seen].
- I did not find a quantification of German fuel tourism ("Tanktourismus") after 1999. Basaglia et al. cite Dings (2004): Luxembourg's fuel sales per capita are 5–8 times its neighbours'.

## UK fuel duty escalator (1993–1999): what ex post evidence exists?

### Takeaway
The only causal ex post estimate I found is the SCM study by Bretschger and Grieg (2024; WP 2020). It reports transport CO2 0.35 t per capita lower per year than a synthetic UK, about 0.5 t by the end, with p ≈ 0.07. The synthetic UK is built from Ireland, Japan, New Zealand and Greece, which is an odd donor pool. Government figures from the period (2–5 MtC saved in 2010) are model-based projections.

### Cited Findings
- Design, per DETR memo: the escalator was introduced in 1993 at 3% real a year, raised to 5% in November 1993, and in July 1997 the Budget committed to 6% real increases. Projected savings were "2–5 MtC in 2010" from a 6% escalator over 1996–2002. These come from the NRTF/VMM model and the DTI EP65 model, which uses a long-run fuel demand elasticity of −0.41. Road transport emitted about 32 MtC in 1997 — [DETR submission reproduced by Japan MoE G8 best-practice page](https://www.env.go.jp/earth/g8_2000/forum/g8bp/detail/uk/uk07.html). The same page's overview dates the 5% rate to 1995, which conflicts.
- Bretschger and Grieg:
  - Donor pool: OECD countries, excluding Norway, Sweden, Finland and the Netherlands.
  - Weights: New Zealand .375, Greece .253, Japan .176, with Ireland making up the remainder.
  - "When the policy ends, the UK has emissions that are more than .500 metric ton lower than synthetic UK per capita. The average treatment effect in the treated time frame is 0.352 metric tons of CO2 per capita."
  - Placebo rank: "top 7.1% of the sample … comparable to a p-value of 0.071".
  - Leave-one-out mean: 0.325 t.
  - No discernible GDP effect.
  - Gasoline-consumption SCM fits poorly ("less robust").
  - Rail travel rose 30%, but that is "only … 200 passenger km per capita" against about 12,000 by road.
  - Source: [Bretschger & Grieg WP 20/332, §3.4, §6.2](https://www.ethz.ch/content/dam/ethz/special-interest/mtec/cer-eth/cer-eth-dam/documents/working-papers/WP-20-332.pdf).
- Published abstract: "the tax has a large and significant impact on CO2 emissions from traffic, while there is no discernible impact on GDP or growth. We do not find large changes in driving behaviours" — [Energy Policy 195:114359 (2024), IDEAS](https://ideas.repec.org/a/eee/enepol/v195y2024ics0301421524003793.html).
- The WP's own description of the policy is loose: "the tax on fuel was increased by 10% in 1993 … 3% more than inflation per year". It says the escalator was frozen in 2001 after the 2000 protests. This omits the 5% and 6% rates — [WP §3.1](https://www.ethz.ch/content/dam/ethz/special-interest/mtec/cer-eth/cer-eth-dam/documents/working-papers/WP-20-332.pdf).

### Inferences
- Ireland is a donor, and Irish fuel sales may have been inflated by fuel bought there by Northern Ireland drivers as UK duty rose. If so, the synthetic UK's emissions would be biased upward and the UK effect overstated. This is my inference and is not tested in the paper.
- Compared with the US and German cases, the UK evidence is thinner: one study, a small donor pool, and annual World Bank data.

### Gaps
- I did not retrieve duty rates in pence per litre by year, pump prices, or the escalator's end date. The Commons Library briefing SN03015 and the parliamentary EAC report returned HTTP 403. So I cannot compute a carbon-price equivalent or the % retail price rise here [VERIFY: needs the Commons Library SN03015 or IFS fuel duty history].
- I did not see the full text of the published 2024 version, so the numbers above are from the 2020 WP.
- I did not find peer-reviewed DfT or HM Treasury ex post evaluations. Dargay and Glaister and Graham are general elasticity studies and reviews; I did not retrieve them.

## Germany's national emissions trading on heating and transport fuels (BEHG, €25/t from 2021): what ex post evidence exists?

### Takeaway
€25/t added **6.0 ct/l to petrol and 6.7 ct/l to diesel net of VAT, or about 7.1 and 8.0 ct/l with 19% VAT**. That was roughly 5.5% (petrol) and 7% (diesel) of 2020 average pump prices. The 2021 price rise was dominated by crude prices: the CO2 component explained about 21% (petrol) and 24% (diesel) of the 2020–21 increase. I found **no ex post causal estimate** of BEHG's effect on fuel use or CO2. The official evaluation reports use ex ante modelling and say ex post estimation is not feasible.

### Cited Findings
- Price path: €25/t (2021), €30 (2022), €30 (2023), €45 (2024), €55 (2025) — [Clean Energy Wire factsheet (search snippet)](https://www.cleanenergywire.org/factsheets/germanys-planned-carbon-pricing-system-transport-and-buildings). A figure of "around 7 cents per litre of petrol, 8 cents per litre of diesel" is widely cited — [Clean Energy Wire news (snippet only)](https://www.cleanenergywire.org/news/germany-enters-2021-price-transport-and-heating-emissions).
- UBA petrol 2021: "Der CO2-Preis beträgt im Jahr 2021 bei Benzin 6 Cent je Liter und hatte damit einen Anteil von 3,8% am Endverbraucherpreis" (in 2021 the CO2 price on petrol was 6 cents per litre, 3.8% of the retail price). The 2021 average petrol price was 157.9 ct/l. "Zwischen 2020 und 2021 stieg der Benzinpreis im Jahresmittel um 28,6 ct/l (+22 %). Die Einführung der CO2-Komponente … hatte einen Anteil von knapp 21 % an dieser Preissteigerung" (between 2020 and 2021 the annual average petrol price rose by 28.6 ct/l, +22%; the CO2 component accounted for just under 21% of that rise). In 2022 it rose "von 6,0 auf 7,2 ct/l" (from 6.0 to 7.2 ct/l) — [UBA CC 45/2022, pp. 28–30](https://www.umweltbundesamt.de/system/files/medien/1410/publikationen/2022-12-02_climate-change_45-2022_wirkung-nat-brennstoffemissionshandel.pdf).
- UBA diesel 2021: "Preissteigerung von 6,7 ct/l … Anteil von 4,8 % am durchschnittlichen Endverbraucherpreis … Rund 24 % des Preisanstiegs zwischen 2020 und 2021 … Insgesamt stieg der Dieselpreis im Jahresmittel um 27,5 ct/l (+24 %)" (a price rise of 6.7 ct/l, 4.8% of the average retail price; about 24% of the 2020–21 rise; overall the annual average diesel price rose by 27.5 ct/l, +24%). It rose "von 6,7 auf 8 ct/l" in 2022 — [UBA CC 45/2022, pp. 30–31](https://www.umweltbundesamt.de/system/files/medien/1410/publikationen/2022-12-02_climate-change_45-2022_wirkung-nat-brennstoffemissionshandel.pdf).
- The UBA summary gives different shares, gross including VAT: 2021 average shares of "5 % für Benzin, 6 % für Diesel und 11 % für Heizöl". In March 2022 petrol peaked at 215.5 ct/l and diesel at 218.4 ct/l — [UBA CC 45/2022, Kurzbeschreibung and pp. 29–31](https://www.umweltbundesamt.de/system/files/medien/1410/publikationen/2022-12-02_climate-change_45-2022_wirkung-nat-brennstoffemissionshandel.pdf).
- Ex ante modelled effects: 11.65 Mt CO2 reduction in 2030 across sectors, of which 7.75 Mt is in transport (PB21 projection) — [UBA CC 59/2024 summary](https://foes.de/publikationen/2024/2024-12_FOES_BEHG.pdf). Ex post estimation "nicht seriös leistbar" (cannot seriously be done) (p. 40, quoted above).
- Related ex post work on the 2022 fuel tax cut (Tankrabatt), not on BEHG: Dovern et al. (2023), "Estimating pass-through rates for the 2022 tax reduction on fuel prices in Germany", Energy Economics 126 — [IDEAS (title only seen)](https://ideas.repec.org/a/eee/eneeco/v126y2023ics0140988323004462.html).

### Inferences
- % increase (my arithmetic):
  - Petrol: 2020 average = 157.9 − 28.6 = 129.3 ct/l, so 7.14 ct with VAT = **5.5%**.
  - Diesel: 2020 average ≈ 27.5/0.24 = 114.6 ct/l, so 7.96 ct with VAT = **6.9%**.
  - Carbon price is €25/t by construction.
- Confounds that make a clean BEHG design hard:
  - the COVID-19 demand collapse in 2020 and recovery in 2021;
  - the crude price recovery (+22–24% pump prices in 2021);
  - the 2022 energy price shock;
  - the June–August 2022 fuel tax cut and 9-euro public transport ticket, and the 2023 Deutschlandticket [VERIFY: dates and amounts not checked this session];
  - VAT returning from 16% to 19% on 1 January 2021, the same day BEHG started [VERIFY: temporary 2020 VAT cut not checked this session].

### Gaps
- No peer-reviewed or credible working-paper ex post estimate of BEHG's effect on fuel demand or CO2 was found, despite several English and German searches. No station-level pass-through study of the January 2021 step was found either. One may exist in the 2025–26 literature; I could not find it.

## Ireland's carbon tax (2010): what ex post evidence exists?

### Takeaway
€15/t applied to petrol and auto-diesel from 9–10 December 2009 and to other fuels from 1 May 2010. That is about **4.2 c/l on petrol and 4.9 c/l on diesel including VAT**, a few percent of pump prices. It rose to €20/t in December 2011. **I found no causal ex post evaluation of its effect on transport fuel or heating emissions.** ESRI work is ex ante or model-based. The 2008–2012 Irish recession is a severe confound.

### Cited Findings
- "The increases, including VAT, amounted to 4.2 cent per litre of petrol and 4.9 cent per litre of diesel". Effective for petrol and auto-diesel at midnight on 9 December 2009; other fuels from 1 May 2010 — [Oireachtas PQ answers, search snippets](https://www.oireachtas.ie/en/debates/question/2010-02-02/149/); [IEA policy database](https://origin.iea.org/policies/1721-ireland-carbon-tax) [VERIFY: figures from search summaries; the PQ pages did not render when fetched].
- €20/t on petrol from 7 December 2011 — [Irish Statute Book, Finance Act 2012 s.68](https://www.irishstatutebook.ie/eli/2012/act/9/section/68/enacted/en/html) (search snippet).
- ESRI RS79, "The Economic and Environmental Impacts of Increasing the Irish Carbon Tax", is model-based — [ESRI RS79](https://www.esri.ie/system/files/publications/RS79_0.pdf) (snippet only).
- In the ESRI study of the 2008 car tax reform, the fuel-tax effect is "about 0.1 million tonnes of carbon dioxide, compared to some 6.0 mln tCO2 for total private transport emissions". This is simulation, not ex post — [ESRI WP 349 / Energy Policy (search snippet)](https://www.esri.ie/system/files/media/file-uploads/2015-07/WP349.pdf).

### Inferences
- €15/t × 2.35 kg/l = 3.5 c/l net, or 4.3 c with 21% VAT, for petrol. €15/t × 2.68 = 4.0 c, or 4.9 c with VAT, for diesel. This is consistent with the official 4.2 and 4.9 c (my arithmetic).

### Gaps
- No ESRI or peer-reviewed ex post (DiD, SCM, ITS) estimate of the Irish carbon tax's effect on transport or heating fuel use was found. Not suitable as a fully documented case.

## Caveats and critiques that apply across these cases

### Takeaway
There are five main threats. Fuel-sales-based emissions data count fuel tourism as abatement. Tax increases cluster with other policies and with oil price swings. Consumers buy ahead of tax dates. Synthetic controls rest on few pre-period years and small donor pools. And the larger "tax vs price" (salience) effect is disputed.

### Cited Findings
- **Anticipation:** gasoline buyers "increase gasoline purchases before tax increases and delay gasoline purchases before tax decreases". This invalidates naive tax-IV, and correcting for it lowers the elasticity from −1.14 to −0.37 — [Coglianese et al. WP 20980](https://www.nber.org/system/files/working_papers/w20980/w20980.pdf). Basaglia et al. find no anticipation in annual German data (fn. 28) — [DIW DP 2041](https://www.diw.de/documents/publikationen/73/diw_01.c.875084.de/dp2041.pdf).
- **Salience dispute:** Li et al. find tax effects about three times price effects. Kilian and Zhou (2023) reportedly find no significant difference once anticipation is modelled (secondhand, from [DIW DP 2041 fn. 5](https://www.diw.de/documents/publikationen/73/diw_01.c.875084.de/dp2041.pdf)). Rivers and Schaufele (2015, JEEM 74:23–36) find a salience effect for BC (reference only).
- **Fuel tourism:** Basaglia et al. exclude Austria and Luxembourg from donors because "more fuel tourism has likely taken place and emission data is not reliable" (fn. 14) — [DIW DP 2041](https://www.diw.de/documents/publikationen/73/diw_01.c.875084.de/dp2041.pdf). Runst and Höhle do not discuss it — [ifh WP 29/2021](https://ifh.wiwi.uni-goettingen.de/site/assets/files/2239/ifh_wp-29_2021.pdf).
- **Confounds in Germany:** the shift to diesel (diesel share up 2 points by 2005), voluntary agreements on carbon from EU car makers, VW's FSI/TDI engine technology, reunification (data-set fit poorer in 1990–92), and the 2008 crisis (gaps converge after 2007) — [Runst & Höhle WP §3–4](https://ifh.wiwi.uni-goettingen.de/site/assets/files/2239/ifh_wp-29_2021.pdf); [DIW DP 2041 fn. 21](https://www.diw.de/documents/publikationen/73/diw_01.c.875084.de/dp2041.pdf).
- **SCM inference:** the UK p-value of 0.071 is the minimum attainable with the donor pool. For GDP the authors note "the amount of placebo tests we are able to run will not be sufficient for a p-value below the normal cutoff" — [Bretschger & Grieg WP](https://www.ethz.ch/content/dam/ethz/special-interest/mtec/cer-eth/cer-eth-dam/documents/working-papers/WP-20-332.pdf).
- **Model-based vs ex post (BEHG):** official evaluations model the effects ex ante — [UBA CC 59/2024, p. 40](https://foes.de/publikationen/2024/2024-12_FOES_BEHG.pdf).

### Inferences
- For the paper's "what carbon prices did" framing, the US elasticities translate cleanly into "% fuel use per US$/t". The tax elasticity of about −0.3 to −0.46 at about 3% price change gives about −0.1% to −0.15% fuel use per US$1/t in the first year. The German SCM gaps are cumulative five-to-ten-year effects of a €57–65/t ramp. Do not compare the two directly without saying the horizons differ.
- The German and UK SCM effect sizes (≥10% of transport CO2) are large relative to the price changes (+22% to +30% from the tax). They imply long-run tax elasticities around −0.4 to −0.7, which is at the high end of conventional long-run price elasticities (my arithmetic, rough). This supports either a salience or persistence story, or some bias from fuel tourism and confounds.

### Gaps
- I did not retrieve Dahl (2012) or Havranek, Irsova and Janda (2012), the gasoline elasticity meta-analyses, so no benchmark numbers from them are given here.

## Full references: which sources were seen, and in what form?

### Takeaway
Every number above comes from the sources below. "Full text" means I read the PDF in this session.

### Cited Findings
- Davis, L. W., and Kilian, L. (2011). "Estimating the effect of a gasoline tax on carbon emissions." *Journal of Applied Econometrics* 26(7): 1187–1214. DOI [10.1002/jae.1156](https://doi.org/10.1002/jae.1156). I saw the published abstract via Crossref and the full text of [NBER WP 14685](https://www.nber.org/system/files/working_papers/w14685/w14685.pdf) (Jan. 2009, rev. Apr. 2009).
- Li, S., Linn, J., and Muehlegger, E. (2014). "Gasoline taxes and consumer behavior." *American Economic Journal: Economic Policy* 6(4): 302–342. DOI [10.1257/pol.6.4.302](https://www.aeaweb.org/articles?id=10.1257/pol.6.4.302). I saw the abstract (paraphrased) and the full text of [NBER WP 17891](https://nber.org/system/files/working_papers/w17891/w17891.pdf) (rev. Feb. 2014).
- Coglianese, J., Davis, L. W., Kilian, L., and Stock, J. H. (2017). "Anticipation, tax avoidance, and the price elasticity of gasoline demand." *Journal of Applied Econometrics* 32(1): 1–15 [VERIFY: DOI]. I saw the full text of [NBER WP 20980](https://www.nber.org/system/files/working_papers/w20980/w20980.pdf) (Feb. 2015).
- Runst, P., and Höhle, D. (2022). "The German eco tax and its impact on CO2 emissions." *Energy Policy* 160: 112655. DOI 10.1016/j.enpol.2021.112655. I saw the published abstract ([IDEAS](https://ideas.repec.org/a/eee/enepol/v160y2022ics0301421521005206.html)) and the full text of [ifh WP 29/2021](https://ifh.wiwi.uni-goettingen.de/site/assets/files/2239/ifh_wp-29_2021.pdf).
- Basaglia, P., Behr, S. M., and Drupp, M. A. (2023). "De-Fueling Externalities: How Tax Salience and Fuel Substitution Mediate Climate and Health Benefits." DIW Discussion Paper 2041. Full text: [DIW DP 2041](https://www.diw.de/documents/publikationen/73/diw_01.c.875084.de/dp2041.pdf). Working paper, not peer-reviewed.
- Basaglia, P., Behr, S. M., and Drupp, M. A. (2025). "Fuel Taxation and Environmental Externalities: Evidence from the World's Largest Environmental Tax Reform." CESifo WP 11949; CEPR DP 20453. Abstract only: [IDEAS](https://ideas.repec.org/p/ces/ceswps/_11949.html). Working paper.
- Bretschger, L., and Grieg, E. (2024). "Carbon taxes, CO2 emissions, and the economy: The effects of fuel taxation in the UK." *Energy Policy* 195: 114359. DOI 10.1016/j.enpol.2024.114359. Abstract only ([IDEAS](https://ideas.repec.org/a/eee/enepol/v195y2024ics0301421524003793.html)); I read the full text of the WP version "Exiting the fossil world" ([CER-ETH WP 20/332](https://www.ethz.ch/content/dam/ethz/special-interest/mtec/cer-eth/cer-eth-dam/documents/working-papers/WP-20-332.pdf), Apr. 2020).
- Schrems, I., Auf der Maur, A., Kemmler, A., Trachsel, T., Saad, N., Bach, S., and Knautz, J. (2022). *Wirkung des nationalen Brennstoffemissionshandels – Auswertungen und Analysen* (Teilbericht). UBA Climate Change 45/2022. Full text: [UBA](https://www.umweltbundesamt.de/system/files/medien/1410/publikationen/2022-12-02_climate-change_45-2022_wirkung-nat-brennstoffemissionshandel.pdf).
- Zerzawy, F., Runkel, M., van Loock, H., Auf der Maur, A., Kemmler, A., Kulkarni, P., and Zwicker, M.-L. (2024). *Wirkung des nationalen Brennstoffemissionshandels – 2. Teilbericht*. UBA Climate Change 59/2024. Full text (searched): [FÖS](https://foes.de/publikationen/2024/2024-12_FOES_BEHG.pdf).
- Döbbeling-Hildebrandt, N., Miersch, K., Khanna, T. M., Bachelet, M., Bruns, S. B., Callaghan, M., et al. (2024). "Systematic review and meta-analysis of ex-post evaluations on the effectiveness of carbon pricing." *Nature Communications* 15: 4147. DOI [10.1038/s41467-024-48512-w](https://doi.org/10.1038/s41467-024-48512-w). Abstract only.
- Green, J. F. (2021). "Does carbon pricing reduce emissions? A review of ex-post analyses." *Environmental Research Letters* 16(4): 043004. DOI [10.1088/1748-9326/abdae9](https://doi.org/10.1088/1748-9326/abdae9). Abstract only.
- Data sources:
  - ADAC annual fuel prices, 1950–2004 — [Autoflotte PDF](https://www.autoflotte.de/downloadfile/733714/SpritpreisEntwicklung.pdf).
  - US EPA emission factor — [EPA](https://www.epa.gov/greenvehicles/greenhouse-gas-emissions-typical-passenger-vehicle).
  - DETR memo on the escalator — [env.go.jp](https://www.env.go.jp/earth/g8_2000/forum/g8bp/detail/uk/uk07.html).

### Inferences
- The peer-reviewed core for the paper is: Davis and Kilian (2011), Li et al. (2014) and Coglianese et al. (2017) for the US; Runst and Höhle (2022) for Germany; Bretschger and Grieg (2024) for the UK. Basaglia et al. (2023, 2025) are credible working papers and should be flagged as such.

### Gaps
- Not obtained:
  - Knigge and Görlach (2005);
  - Kohlhaas (2005);
  - Frondel and Vance (2014) full text;
  - Dargay;
  - Glaister and Graham (2002);
  - Köppl and Schratzenstaller (2023);
  - Dahl (2012);
  - Havranek et al. (2012);
  - UK duty rates by year;
  - FHWA/EIA series directly.
