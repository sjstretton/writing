# Efficiency Frontiers for Public Spending and Extending CBA Across Sectors and the Economy

Scope: (Part 1) technical-efficiency frontiers (DEA/FDH/SFA), allocative "marginal return per dollar across sectors", portfolio and Pareto frontiers, MACCs, and RDM/DMDU. (Part 2) cross-sector BCA (Copenhagen Consensus), sector conversion metrics (health, education, social protection, WASH and resilience), and economy-wide or general-equilibrium CBA. The final section sets out implications for a Python/Excel tool that extends SISEPUEDE/CDPM transformation CBA.

**Method note (read first).** The research used about 50 WebSearch queries. WebFetch could not resolve any host from this sandbox (ideas.repec.org, imf.org, ncbi, worldbank OKR, copenhagenconsensus.com), and direct curl downloads were blocked by the proxy (HTTP 403). The turn's web-search budget then ran out. As a result:
- Each item under "Cited Findings" was confirmed through search-result abstracts or bibliographic records at the linked URL. I did not read the full texts.
- Numbers marked "(secondary)" come from a source that cites the original, not from the original itself.
- Classic citations and items I could not check again in this session are listed under "Gaps", with bibliographic details from prior knowledge marked **UNVERIFIED**.

---

## Q1. Technical-efficiency frontiers of public spending (DEA, FDH, SFA): key applications, and how the scores become model parameters

### Takeaway
Cross-country frontier studies consistently find large technical inefficiency in public spending.
- Public investment: an average gap of about 30% (IMF PIE-X, 2015).
- Health and education: output scores of roughly 0.8–0.9 in developing countries, which leaves 10–20% of attainable output unrealised. Africa usually scores lowest.

The scores enter macro and costing models in three ways:
- an "efficiency parameter" that scales how much spending becomes effective capital or output (as in the IMF DIG/DIGNAR models and Gupta et al.'s efficiency-adjusted public capital);
- a "potential savings" or "potential output gain" figure;
- a convergence assumption: institutional (PIM) reform closes one-half to two-thirds of the gap.

### Cited Findings

**Foundational public-sector applications**
- **Gupta & Verhoeven (2001)**, "The efficiency of government expenditure: experiences from Africa," *Journal of Policy Modeling* 23(4): 433–467, DOI 10.1016/S0161-8938(00)00036-3.
  - Method: FDH on education and health spending in 38 African countries, 1984–95.
  - Findings: African countries were on average less efficient than countries in Asia and the Western Hemisphere. Their efficiency improved over the period. Better outcomes "require more than larger budget allocations."
  - An earlier version is IMF WP/97/153 (with Keiko Honjo).
  - Sources: [IDEAS/RePEc](https://ideas.repec.org/a/eee/jpolmo/v23y2001i4p433-467.html); [IMF WP 97/153](https://www.imf.org/en/Publications/WP/Issues/2016/12/30/The-Efficiency-of-Government-Expenditure-Experiences-From-Africa-2409)
- **Afonso, Schuknecht & Tanzi (2005)**, "Public sector efficiency: An international comparison," *Public Choice* 123(3–4): 321–347. The earlier version is ECB WP 242 (2003).
  - Scope: 23 industrialised countries.
  - Indicators: a composite Public Sector Performance (PSP) indicator plus 7 sub-indicators. Four are "opportunity" indicators (administration, education, health, infrastructure). Three are Musgravian (allocation, distribution, stabilisation).
  - Method: input and output efficiency are measured with a non-parametric (DEA-type) frontier against spending.
  - Findings: "significant differences in public sector performance and efficiency," which implies "a large potential for expenditure savings." Sources: [IDEAS](https://ideas.repec.org/a/kap/pubcho/v123y2005i3p321-347.html); [SSRN 701123](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=701123)
  - Follow-up: ECB WP 581 (2006), "Public sector efficiency: evidence for new EU member states and emerging markets." It finds that expenditure efficiency in the new EU member states is quite diverse, especially compared with top-performing emerging markets in Asia. Source: [ECB WP 581](https://www.ecb.europa.eu/pub/pdf/scpwps/ecbwp581.pdf)
  - Later work by the same authors reports average input-efficiency scores of about 0.6–0.7, i.e. the same outputs could in principle be produced with 30–40% fewer inputs (secondary). Source: [Afonso (ed.) *Handbook on Public Sector Efficiency* (Edward Elgar, 2023), intro chapter](https://ddd.uab.cat/pub/caplli/2023/ea12526bad29/AFONSO_9781839109157_2P.pdf)
- **Herrera & Pang (2005)**, "Efficiency of Public Spending in Developing Countries: An Efficiency Frontier Approach," World Bank Policy Research WP 3645.
  - Method: FDH and DEA frontiers for health and education in 140 countries, using 1996–2002 data. A Banco de la República version gives 1975–2002, so the sources conflict on the start year.
  - Second stage: lower efficiency is associated with higher spending levels, a larger wage-bill share, a higher ratio of public to private financing, HIV/AIDS prevalence, income inequality and aid dependence (aid volatility hampers planning). Urbanisation is the only positively associated variable. The authors stress that "no causality may be inferred."
  - Sources: [World Bank OKR](https://openknowledge.worldbank.org/entities/publication/a61e59ba-30af-5096-b049-b504bf617e34/full); [BanRep version](https://www.banrep.gov.co/sites/default/files/publicaciones/archivos/espe_051-3_0.pdf)
  - Secondary reports put output-efficiency scores at roughly 0.80 for education and 0.90 for health. Source: [ADB Economics WP 435 (secondary)](https://www.adb.org/sites/default/files/publication/161539/ewp-435.pdf)
  - Update: a 2018 World Bank WP (Herrera & Ouedraogo) extends the benchmarking to education, health and infrastructure. A paper titled "Efficiency of public spending in education, health, and infrastructure: an international benchmarking exercise" appears in the *Journal of Applied Economics* (2025). Sources: [Taylor & Francis](https://www.tandfonline.com/doi/full/10.1080/15140326.2025.2480985); [Academia copy](https://www.academia.edu/78993217/Efficiency_of_Public_Spending_in_Education_Health_and_Infrastructure_An_International_Benchmarking_Exercise)
- **Grigoli & Kapsoli (2013/2018)**, "Waste Not, Want Not: The Efficiency of Health Expenditure in Emerging and Developing Economies," IMF WP 13/187. Published in *Review of Development Economics* 22(1): 384–403 (2018).
  - Method: a stochastic frontier model.
  - Findings: African economies have the lowest efficiency. Sources: [IMF WP page](https://www.imf.org/en/publications/wp/issues/2016/12/31/waste-not-want-not-the-efficiency-of-health-expenditure-in-emerging-and-developing-economies-40899); [IMF WP PDF](https://www.imf.org/external/pubs/ft/wp/2013/wp13187.pdf)
  - Secondary citations of this paper report that removing inefficiency could add about 5 years of (healthy) life expectancy in Africa or low-income countries, versus about 1.5 years in advanced economies, and about 3 years in LAC. These figures vary by citing source, so check them against the original. Sources: [PLOS One LAC determinants study](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0216620); [JOGH 2023 Africa meta-analysis](https://jogh.org/2023/jogh-13-04131)
- **Grigoli (2014)**, "A Hybrid Approach to Estimating the Efficiency of Public Spending on Education in Emerging and Developing Economies," IMF WP 14/19. Also published in *Applied Economics and Finance* 2(1): 19–32 (2015).
  - Method: a secondary-education frontier, estimated separately for lower- and higher-income economies.
  - Findings: there are large potential enrolment gains, especially in lower-income economies and Africa.
  - Levers: reduce high pupil–teacher ratios and improve government effectiveness (WGI). Sources: [IMF](https://www.imf.org/en/publications/wp/issues/2016/12/31/a-hybrid-approach-to-estimating-the-efficiency-of-public-spending-on-education-in-emerging-41293); [IMF PDF](https://www.imf.org/external/pubs/ft/wp/2014/wp1419.pdf); [AEF](https://redfame.com/journal/index.php/aef/article/view/609/0)
- **IMF (2022)**, "Patterns and Drivers of Health Spending Efficiency," WP/22/48. Efficiency gains occurred in most countries. Lower inequality, less corruption, and interventions that expand access to basic services are associated with higher efficiency. Source: [IMF WP 22/48](https://www.imf.org/-/media/files/publications/wp/2022/english/wpiea2022048-print-pdf.pdf)

**Public investment efficiency (PIE-X) and its use**
- **IMF (2015)**, *Making Public Investment More Efficient* (Policy Paper, June 2015).
  - PIE-X is a cross-country frontier that compares public capital stock per capita (input) with the coverage and quality of infrastructure (output).
  - Average inefficiency is "around 30 percent."
  - "The most efficient public investors get twice the growth 'bang' for their public investment 'buck'" compared with the least efficient.
  - Strengthening PIM institutions could close up to two-thirds of the efficiency gap.
  - Sources: [IMF Policy Paper](https://www.imf.org/en/Publications/Policy-Papers/Issues/2016/12/31/Making-Public-Investment-More-Efficient-PP4959); [PDF (PIMA site)](https://infrastructuregovern.imf.org/content/dam/PIMA/Forum/IGEUR/Resources/Making%20Public%20Investment%20More%20Efficient%202015.pdf); [IMF Survey 2015](https://www.imf.org/en/News/Articles/2015/09/28/04/53/sonew061815a)
  - Conflicting presentations of the same number: an IMF slide deck says the "average country is 27% below efficiency frontier" ([IMF PIM slides via G24](https://g24.org/wp-content/uploads/2023/10/IMF_Public-Investment-Management.pdf)), and the IMF PFM blog says "around one-third of potential benefits" is lost ([IMF PFM blog 2015](https://blog-pfm.imf.org/pfmblog/2015/11/trapping-the-white-elephants-can-the-latest-public-investment-boom-avoid-the-mistakes-of-the-past.html)).
- **Schwartz, Fouad, Hansen & Verdier (eds.) (2020)**, *Well Spent: How Strong Infrastructure Governance Can End Waste in Public Investment* (IMF). Stronger infrastructure governance could recover more than half of observed efficiency losses. Source: [IMF presentation, MoF Japan seminar 2020](https://www.mof.go.jp/pri/research/seminar/fy2020/tff2020_publication_01.pdf)
- **PIMA coverage.** PIMA covers 15 institutions across three phases (planning, allocation, implementation). It had been applied in 82 countries, including 37 LIDCs, according to a later IMF note. Source: [IMF How-To Note 2025/001](https://www.imf.org/-/media/files/publications/howtonotes/2025/english/htnea2025001.pdf.md)

**How efficiency scores become model parameters**
- **Efficiency-adjusted public capital.** Gupta, Kangur, Papageorgiou & Wane (2014), "Efficiency-Adjusted Public Capital and Growth," *World Development* 57: 164–178 (IMF WP 11/217).
  - Method: public capital stocks for 52 developing countries are adjusted with a Public Investment Management Index (appraisal, selection, implementation, evaluation).
  - Findings: the marginal product of public capital is higher in low-income countries. Investment quality helps explain growth differences, mainly in LICs. Effective public capital may be as little as about half of conventional perpetual-inventory estimates (secondary).
  - Sources: [IMF WP 11/217](https://imf.org/en/Publications/WP/Issues/2016/12/31/Efficiency-Adjusted-Public-Capital-and-Growth-25248); [IMF PFM blog](https://blog-pfm.imf.org/en/pfmblog/2011/11/efficiency-adjusted-public-capital-and-growth); [Central Banking summary](https://www.centralbanking.com/central-banking/research/2110119/public-capital-productivity-imf-paper)
- **DIG/DIGNAR models (IMF).** Gurara, Melina & Zanna (2019), "Some Policy Lessons from Country Applications of the DIG and DIGNAR Models," IMF WP 19/62.
  - Scope: reviews 65+ country applications.
  - Calibration: outcomes depend on the *efficiency of public investment* parameter and on the *rate of return on public capital*, plus the type of financing and revenue-mobilisation capacity.
  - Lessons: raising efficiency or project returns raises growth and lowers debt risk. Gradual scale-ups are preferred because of crowding-out and absorptive-capacity limits. Source: [IMF WP 19/62](https://www.imf.org/en/Publications/WP/Issues/2019/03/18/Some-Policy-Lessons-from-Country-Applications-of-the-DIG-and-DIGNAR-Models-46665)
- **Absorptive capacity as a cost parameter.** An IMF WP using road-project data finds that unit costs rise non-linearly once public investment reaches about 10% of GDP. The threshold is about 7% of GDP in low-efficiency countries. Source: [IMF WP 2020, "On the Capacity to Absorb Public Investment: How Much is Too Much?"](https://www.imf.org/en/Publications/WP/Issues/2020/02/28/On-the-Capacity-to-Absorb-Public-Investment-How-Much-is-Too-Much-49039). The attribution comes from a search summary, so confirm the exact figures in the paper.
- **SDG costing.** Gaspar, Amaglobeli, Garcia-Escribano, Prady & Soto (2019), "Fiscal Policy and Development: Human, Social, and Physical Investment for the SDGs," IMF SDN/19/03.
  - Scope: costs education, health, roads, electricity and water/sanitation for 155 countries (49 LIDCs, 72 EMs, 34 AEs).
  - Findings: additional 2030 spending of about US$0.5 trillion for LIDCs (an average of about 15 percentage points of GDP) and about US$2.1 trillion for EMs.
  - Recommendations: raise tax capacity and improve spending efficiency. Sources: [IMF SDN page](https://imf.org/en/Publications/Staff-Discussion-Notes/Issues/2019/01/18/Fiscal-Policy-and-Development-Human-Social-and-Physical-Investments-for-the-SDGs-46444); [full PDF mirror](https://www.sipotra.it/wp-content/uploads/2019/03/Fiscal-Policy-and-Development-Human-Social-and-Physical-Investment-for-the-SDGs.pdf)

**Inference methods**
- **Simar & Wilson (2007)**, "Estimation and inference in two-stage, semi-parametric models of production processes," *Journal of Econometrics* 136(1): 31–64.
  - Argument: conventional second-stage regressions of DEA scores on environmental variables lack a coherent data-generating process, and they are invalidated by serial correlation among the estimated efficiencies.
  - Remedy: bootstrap algorithms (truncated regression with bias-corrected scores).
  - Implementation: the Stata command `simarwilson` (Badunenko & Tauchmann 2019, *Stata Journal*). Sources: [UCLouvain record](https://research.dial.uclouvain.be/entities/publication/4ac5e6e9-969c-4278-8bb7-1d1aa03acfbe); [FAU record of Stata implementation](https://open.fau.de/items/7c80a826-df3e-4f62-aff2-69b4f7dc476b/full)

### Inferences
- **Scores reported.** Public-spending applications almost always report *output-oriented* scores in human-development sectors ("how much more outcome for the same money") and *input-oriented* scores in budget or "potential savings" framings. Output-oriented, VRS or FDH scores are the natural haircut for a CBA tool, because the tool already fixes the budget and asks what outcome it buys.
- **Typical magnitudes for defaults** (with heavy caveats). Use about 0.7 for public investment (from the roughly 30% PIE-X gap), and roughly 0.8 for education and 0.9 for health output efficiency in developing countries (Herrera & Pang, secondary). Africa and LICs sit lower.
- **Convergence.** Two IMF figures support a scenario in which PIM reform closes 50–67% of the gap over a reform period: "up to two-thirds" (IMF 2015) and ">half" (*Well Spent*). The pace is not documented and is an assumption.
- **Second-stage drivers.** Wage-bill share, inequality, aid volatility, governance or corruption, and urbanisation are the variables the literature repeatedly associates with efficiency. A tool can use them to pick peer-group frontiers or to adjust a default score when no country-specific estimate exists. Simar & Wilson's critique means naïve OLS or Tobit second stages should not be used to project scores.
- **Use in GE models.** The DIG "efficiency parameter" and Gupta et al.'s efficiency-adjusted capital show how macro models take the score: as the share of each spending dollar that becomes productive capital. That is the cleanest link between a DEA score and a macro-fiscal module.

### Gaps
- **Classic methodological citations (not re-verified this session; details are UNVERIFIED and from prior knowledge):**
  - Farrell (1957), "The measurement of productive efficiency," *JRSS Series A* 120(3): 253–290.
  - Charnes, Cooper & Rhodes (1978), "Measuring the efficiency of decision making units," *EJOR* 2(6): 429–444.
  - Banker, Charnes & Cooper (1984), *Management Science* 30(9): 1078–1092 (VRS/BCC).
  - Deprins, Simar & Tulkens (1984), "Measuring labor-efficiency in post offices," in Marchand, Pestieau & Tulkens (eds.), *The Performance of Public Enterprises*, North-Holland, pp. 243–267 (FDH).
  - Simar & Wilson (1998), "Sensitivity analysis of efficiency scores: how to bootstrap in nonparametric frontier models," *Management Science* 44(1): 49–61.
  - Aigner, Lovell & Schmidt (1977), *J. Econometrics* 6(1): 21–37.
  - Meeusen & van den Broeck (1977), *International Economic Review* 18(2): 435–444 (SFA).
- **Afonso et al. headline figures.** I could not confirm the 2005 paper's numbers (e.g., average input efficiency, or "countries could use X% less resources"). The 2010 published version of the EU/emerging-markets paper (believed to be *Applied Economics* 42(17), 2010) is UNVERIFIED.
- **PIE-X detail.** The breakdown by income group (AE, EM, LIDC gaps) and the exact DEA specification (output-oriented, VRS, sample years) could not be extracted.
- **IMF SDG costing.** I did not confirm whether SDN/19/03 adjusts unit costs for efficiency or benchmarks input-to-outcome against high performers. My prior understanding is that it benchmarks inputs (e.g., teachers per pupil, health workers per capita) at the levels of strong performers; this is UNVERIFIED.
- **Grigoli & Kapsoli life-expectancy gains.** The original numbers were not read.

---

## Q2. Allocative efficiency across sectors: estimates of the marginal return to a dollar of public spending by sector

### Takeaway
The best-established body of evidence on "returns per unit of public spending across sectors" is IFPRI's simultaneous-equation work on rural India and China. In India, rural roads and agricultural R&D rank highest per rupee for both productivity and poverty reduction, with education third. Input subsidies (fertiliser, power, irrigation, credit) and irrigation rank low at the margin, even though subsidies mattered early in the Green Revolution. In China, education has the largest poverty impact and agricultural R&D the largest agricultural-growth impact. These are *marginal* returns, estimated over historical periods. They are the conceptual template for an allocative frontier: equalise marginal net benefit per dollar across sectors.

### Cited Findings
- **Fan, Hazell & Thorat (2000)**, "Government Spending, Growth and Poverty in Rural India," *American Journal of Agricultural Economics* 82(4): 1038–1051.
  - Method: a simultaneous-equation model on Indian state-level data for 1970–93.
  - Findings: roads and agricultural research have "much larger poverty impacts per rupee spent than any other government investment" and also generate higher productivity growth. Education has the third-largest marginal impact. Irrigation, soil and water conservation, health, and rural/community development have "only modest" growth and poverty effects per additional rupee.
  - The IFPRI Research Report 110 version carries the full coefficient tables. Sources: [IDEAS](https://ideas.repec.org:443/a/oup/ajagec/v82y2000i4p1038-1051.html); [Wiley](https://onlinelibrary.wiley.com/doi/abs/10.1111/0002-9092.00101); [CGSpace](https://cgspace.cgiar.org/items/468ced3b-24ba-4e11-acfa-e427e26bbc9f); [IFPRI RR 110](https://ideas.repec.org/p/fpr/resrep/110.html)
- **Fan, Gulati & Thorat (2008)**, "Investment, subsidies, and pro-poor growth in rural India," *Agricultural Economics* 39(2): 163–170 (IFPRI DP 716, 2007).
  - Findings: credit, fertiliser and irrigation subsidies were crucial for small-farmer adoption early in the Green Revolution (late 1960s–1970s). Today, agricultural research, education and rural roads are the three most effective spending items for growth and poverty reduction.
  - Recommendation: reallocate away from fertiliser, irrigation, power and credit subsidies toward R&D, rural infrastructure and education. Institutional reform may matter as much as reallocation. Sources: [IDEAS](https://ideas.repec.org/a/bla/agecon/v39y2008i2p163-170.html); [IFPRI DP 716 PDF](https://ageconsearch.umn.edu/record/42397/files/IFPRIDP00716.pdf)
- **Fan, Zhang & Zhang (China).** Their IFPRI work on 1978–97 provincial data finds:
  - education has by far the largest impact on poverty reduction and the second-largest on production growth;
  - agricultural R&D and extension has the largest impact on agricultural growth;
  - rural telecommunications is second for poverty reduction;
  - irrigation and subsidised anti-poverty loans have minimal impact.
  - Publications: *Growth, Inequality, and Poverty in Rural China: The Role of Public Investments* (IFPRI RR 125, 2002), and "Reforms, investment, and poverty in rural China," *Economic Development and Cultural Change* 52(2): 395–421 (2004), DOI 10.1086/380593. Sources: [IFPRI RR 125](https://ideas.repec.org/p/fpr/resrep/125.html); [EPTD DP 66](https://econpapers.repec.org/RePEc:fpr:eptddp:66); [CGSpace EDCC record](https://cgspace.cgiar.org/items/db41a13e-5cb2-4c53-bd63-a7a8dab4924c)
- **Mogues, Yu, Fan & McBride (2012)**, "The Impacts of Public Investment in and for Agriculture: Synthesis of the Existing Evidence," FAO ESA Working Paper No. 12-07 (IFPRI authors). This is a synthesis across developing countries. One example: the IRR of biofortification (golden rice, Philippines) is 66–133%. Sources: [AgEcon Search PDF](https://ageconsearch.umn.edu/record/288994/files/a-ap108e.pdf); [AGRODEP](https://agrodep.org/node/2531)
- **FAO SOFA 2012 chapter (drawing on this synthesis).**
  - Alston et al. (2000) reviewed 292 studies (1953–97) and found an average rate of return to agricultural research of about 60% in developing countries.
  - Evenson (2001) found returns above 20% in four-fifths of applied research programmes and three-quarters of extension programmes. Source: [FAO SOFA 2012 ch.](https://www.fao.org/4/i3028e/i3028e05.pdf)
- **Copenhagen Consensus Halftime (2023).** The agricultural R&D benefit-cost ratio is 33. This is consistent with the high returns to agricultural research found in the IFPRI and FAO literature. Source: [CCC Ag R&D manuscript](https://copenhagenconsensus.com/sites/default/files/2023-03/Ag%20R&D%20Best%20Investment%20Manuscript%20230311.pdf)

### Inferences
- The IFPRI approach estimates ∂(output or poverty)/∂(spending_k) for each spending category k from a structural system. That is exactly the "marginal benefit per dollar" needed to trace an allocative frontier. The coefficients are historical and context-specific (India 1970–93; China 1978–97), so they can be used as priors or sanity checks, not as transferable parameters.
- The consistent ranking across India and China (R&D, roads and education above subsidies and irrigation at the margin) supports a prior for the tool: hold *subsidies* and *transfers to producers* to a higher evidence bar than *public goods* when reallocating.
- The literature notes that early-stage subsidies had high returns which later fell. Marginal returns therefore decline with the level of spending, so the frontier should use declining marginal-benefit curves, not constant BCRs.

### Gaps
- **Exact per-rupee or per-yuan return coefficients.** For example, rupees of agricultural GDP per rupee spent on R&D or roads, or persons lifted from poverty per million rupees. These are in IFPRI RR 110/125 and FGT 2008 but could not be extracted.
- **IFPRI SPEED database** (Statistics on Public Expenditures for Economic Development). Its coverage and current version were not verified. My prior understanding is that it covers about 150 countries from 1980 onward, by COFOG-like function; this is UNVERIFIED.
- **Growth-maximising composition of spending.** The cross-country literature (e.g., Devarajan, Swaroop & Zou 1996, *JME*) was not searched.

---

## Q3. Portfolio and Pareto frontiers, MACCs, and decision-making under deep uncertainty (RDM/DMDU)

### Takeaway
Three frontier concepts apply to public portfolios:
- **Mean-variance frontiers** (Awerbuch & Berger's electricity portfolio theory): minimise expected cost for a given cost risk.
- **Budget-constrained selection frontiers** (BCR ranking or knapsack): maximise net benefit for each budget level.
- **Robustness frontiers** (RDM): find strategies that perform acceptably across thousands of futures. The World Bank's *Lifelines* applied this to resilient infrastructure (BCR > 1 in 96% of scenarios, median $4 per $1). The IDB/RAND Costa Rica decarbonisation study applied it to an economy-wide transformation package ($41 billion net benefit at 5%).

MACCs are a static special case of the efficient frontier. They are criticised for ignoring interactions, co-benefits, uncertainty and timing: with a long-term target and deployment-speed limits, it can be optimal to begin expensive measures early.

### Cited Findings

**Portfolio theory for public energy decisions**
- **Awerbuch & Berger (2003)**, "Applying portfolio theory to EU electricity planning and policy-making," IEA/EET Working Paper EET/2003/03, IEA/OECD, Paris.
  - Approach: mean-variance analysis of generation mixes. The inverse of generating cost (kWh per €) is treated as "return", and the volatility of its cost components, mainly fuel, as "risk". Adding fixed-cost renewables can lower portfolio risk at little or no expected-cost penalty.
  - Antecedents: a 2002 Berger–Awerbuch–Haas report and Berger's TU Wien dissertation on "Portfolio analysis of EU electricity generating mixes."
  - Sources: [Austrian BMVIT report](https://nachhaltigwirtschaften.at/resources/nw_pdf/0302_versorgungssicherheit.pdf); [TU Wien repository](https://repositum.tuwien.at/handle/20.500.12708/186168); [EIB Papers 2007 v12 n2 (discussion)](https://www02.eib.org/attachments/efs/eibpapers/eibpapers_2007_v12_n02_en.pdf); [South African application, JESA](https://journals.assaf.org.za/jesa/article/view/1545)

**RDM / DMDU**
- **Lempert, Popper & Bankes (2003)**, *Shaping the Next One Hundred Years: New Methods for Quantitative, Long-Term Policy Analysis*, RAND MR-1626.
  - Reframes "What will the long-term future bring?" as "How can we choose actions today that will be consistent with our long-term interests?"
  - Robust decision methods "examine a vast range of plausible futures and design near-term, often adaptive, strategies to be robust across them." Source: [RAND MR-1626](https://www.rand.org/pubs/monograph_reports/MR1626.html)
- **Costa Rica decarbonisation.** Groves, Syme, Molina-Perez, et al. (2020), *The Benefits and Costs of Decarbonizing Costa Rica's Economy: Informing the Implementation of Costa Rica's National Decarbonization Plan under Uncertainty* (IDB and RAND, RR-A633-1).
  - Central result: about **$41 billion net benefit, 2020–2050, discounted at 5%** (benefits about $78 billion; costs about $37 billion of investment plus forgone land value).
  - Transport: energy savings, fewer accidents, less congestion and lower air-pollution damage outweigh the higher upfront cost of EVs and zero-emission transit.
  - Land use: higher agricultural productivity and forest ecosystem services.
  - Errors in secondary sources: an IDB blog misstates benefits as "USD 78 million."
  - Venue: **I found no *Nature Sustainability* paper.** The citable source is the IDB/RAND report.
  - Sources: [IDB publication](https://publications.iadb.org/en/benefits-and-costs-decarbonizing-costa-ricas-economy-informing-implementation-costa-ricas-national); [RAND RR-A633-1 PDF](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA600/RRA633-1/RAND_RRA633-1.pdf); [IDB blog "41 billion reasons"](https://www.iadb.org/en/blog/nature-climate-and-disaster-risk/41-billion-reasons-why-costa-ricas-progress-decarbonization-can-inspire-world); [IDB sustainability blog](https://blogs.iadb.org/sostenibilidad/en/?p=19521)
- **Related RDM application** (Dominican Republic decarbonisation; Victor-Gallardo, Quirós-Tortós et al.): scenarios evaluated across 1,000 futures. Source: [Frontiers in Climate 2024, 10.3389/fclim.2024.1380382](https://www.frontiersin.org/journals/climate/articles/10.3389/fclim.2024.1380382/pdf)
- **Lifelines (World Bank, 2019; Hallegatte, Rentschler & Rozenberg).**
  - Results across thousands of scenarios: the net benefit of more resilient infrastructure in LMICs is **$4.2 trillion** over asset lifetimes in the median scenario, i.e. **$4 of benefit per $1 invested**. The BCR is above 1 in 96% of scenarios, above 2 in 77%, and above 4 in half. Climate change roughly doubles the net benefits.
  - Cost: $11–65 billion per year, about 3% of baseline power, transport and WASH investment needs.
  - Sources: [World Bank OKR, Lifelines](https://openknowledge.worldbank.org/handle/10986/31913); [PRWP 8896 (Hallegatte, Rentschler & Rozenberg, background paper)](https://ideas.repec.org/p/wbk/wbrwps/8896.html)

**MACCs and their critique**
- **Kesicki & Ekins (2012)**, "Marginal abatement cost curves: a call for caution," *Climate Policy* 12(2): 219–236, DOI 10.1080/14693062.2011.582347.
  - Critique: MACCs omit ancillary benefits, treat uncertainty in a limited way, ignore intertemporal dynamics, and lack transparency. Expert-based curves also ignore interactions between measures, risk inconsistent baselines and double counting. Forestry abatement is especially hard to represent.
  - Recommendation: use MACCs as one aid among several. Sources: [IDEAS](https://ideas.repec.org/a/taf/tcpoxx/v12y2012i2p219-236.html); [UCL working version](https://www.ucl.ac.uk/bartlett/sustainable/publications/2011/jan/marginal-abatement-cost-curves-call-caution)
- **Vogt-Schilb & Hallegatte (2014)**, "Marginal abatement cost curves and the optimal timing of mitigation measures," *Energy Policy* 66: 645–653.
  - Model: adding a maximum implementation speed to each measure shows that the optimal short-term strategy depends on the long-term target.
  - Implication: meeting a 2020 target might require expensive, high-potential, slow-to-deploy measures that are needed for 2050. Picking only cheap options locks in carbon-intensive capital, and some expensive options should be deployed before the cheap ones are exhausted.
  - Extension: Vogt-Schilb, Meunier & Hallegatte (JEEM 2018) cover timing and sectoral allocation. Sources: [World Bank OKR PDF](https://openknowledge.worldbank.org/server/api/core/bitstreams/64f0e470-8ce9-5ad6-9fcf-94992a1766d5/content); [IDEAS](https://ideas.repec.org/p/hal/journl/hal-00916328.html); [CIRED WP version "When starting with the most expensive option makes sense"](https://cases.som.yale.edu/sites/default/files/SSRN-id1932025.pdf)

### Inferences
- **What a "budget-efficient frontier" is.** For a CBA tool, it is the upper concave envelope of (cumulative cost, cumulative net benefit) for portfolios selected under increasing budgets. A MACC is the same object rotated, with abatement on the x-axis and cost per tCO2 on the y-axis. The Kesicki–Ekins and Vogt-Schilb–Hallegatte critiques mean the tool should:
  - model interactions between measures, or at least flag measures that share the same abatement or outcome pool;
  - include co-benefits, which SISEPUEDE/CDPM already does;
  - add deployment-rate constraints and a long-term target when ranking measures over time.
- **Robustness on top of efficiency.** *Lifelines* and Costa Rica show the practical pattern: compute BCR/NPV over a large ensemble of futures, then report the share of futures with BCR > 1 and percentile BCRs. Costa Rica is the closest published precedent for the SISEPUEDE/CDPM family: an economy-wide transformation package evaluated with BCA under deep uncertainty.
- **When Awerbuch-style mean-variance helps.** It is most useful where cost-risk correlations are measurable (fuel prices). For cross-sector social portfolios, scenario-based downside metrics (e.g., 10th-percentile NPV or regret) are easier to defend than covariance matrices.

### Gaps
- **Not re-verified this session (UNVERIFIED, from prior knowledge):**
  - Hallegatte, Shah, Lempert, Brown & Gill (2012), "Investment Decision Making Under Deep Uncertainty: Application to Climate Change," World Bank PRWP 6193.
  - Hallegatte et al. (2016), *Shock Waves: Managing the Impacts of Climate Change on Poverty* (World Bank).
  - Marchau, Walker, Bloemen & Popper (eds.) (2019), *Decision Making under Deep Uncertainty: From Theory to Practice* (Springer, open access).
  - Groves & Lempert (2007), "A new analytic method for finding policy-relevant scenarios," *Global Environmental Change* 17(1): 73–85.
- **World Bank MACTool** (Marginal Abatement Cost Tool, which reports break-even carbon prices and investment needs). Not verified; there were no search results before the budget ran out.
- **Portfolio-selection references** (knapsack, incremental BCR, portfolio decision analysis, e.g., Salo, Keisler & Morton (eds.) 2011, *Portfolio Decision Analysis*, Springer; Weingartner 1963 on capital rationing). Not verified. The algorithms in the final section are standard OR methods, presented as inference.
- **Costa Rica study details.** The number of futures and the discount-rate sensitivity were not extracted.

---

## Q4. Cross-sector benefit-cost comparisons: Copenhagen Consensus methods and results

### Takeaway
Copenhagen Consensus (CCC) is the main operational precedent for ranking interventions across sectors by BCR with harmonised assumptions. The 2023 "Halftime for the SDGs" project (JBCA special issue, 12 interventions, *Best Things First*) reports BCRs from 18 (nutrition) to about 125 (e-procurement), with a pooled BCR of 52. Recent CCC papers use an **8% base discount rate**, and value mortality with VSL or VSLY scaled to income. Earlier CCC projects asked for 3% and 5%, and earlier country projects valued DALYs as multiples of GDP per capita. Parameters therefore vary across CCC rounds and must be harmonised before results are pooled.

### Cited Findings
- **JBCA Volume 14, Supplement S1 (Spring 2023).** "Halftime for the Sustainable Development Goals 2016–2030," guest-edited by Bjørn Lomborg and funded by the Gates Foundation. The front matter states it "is not the standard Journal of Benefit-Cost Analysis peer review process and should not be quoted as peer-reviewed by JBCA." It covers 12 interventions with BCRs above 15. Sources: [JBCA S1 front matter](https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/26B0DF6FAE8D35ADEEEA341F49B02848/S2194588823000386a.pdf/bca-volume-14-issue-s1-cover-and-front-matter.pdf); [CCC Halftime](https://copenhagenconsensus.com/halftime)
- **Introduction to the issue.** Its title is "Save 4.2 Million Lives and Generate $1.1 Trillion in Economic Benefits for Only $41 Billion." It reports total benefits of $2.1 trillion (including the value of lives saved) and a pooled BCR of 52. Source: [Cambridge PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/26AC5E41A3D76031B85178E84D070CD8/S2194588823000325a.pdf/save_42_million_lives_and_generate_11_trillion_in_economic_benefits_for_only_41_billion_introduction_to_the_special_issue_on_the_most_efficient_policies_for_the_sustainable_development_goals.pdf)
- **Best Things First (Lomborg 2023), the popular book version.** It gives a cost of about $35 billion per year, 4.2 million lives saved per year and $1.1 trillion in additional income for the poor. The cost figure ($35 billion) differs from the JBCA introduction ($41 billion), so it should be checked. Source: [lomborg.com](https://lomborg.com/best-things-first)
- **Individual BCRs confirmed:**
  - TB: 46 (range 28–84 across specifications). Source: [CCC TB](https://copenhagenconsensus.com/publication/halftime-sdgs-tuberculosis)
  - Maternal and newborn health: 87. Source: [CCC manuscript](https://copenhagenconsensus.com/sites/default/files/2023-03/Maternal%20and%20Newborn%20health%20Manuscript%20230211_1.pdf)
  - Chronic disease: 23. Source: [CCC manuscript](https://copenhagenconsensus.com/sites/default/files/2023-04/Chronic%20Dieseases%20Manuscript%20230211_0.pdf)
  - Nutrition: 18. Source: [CCC manuscript](https://copenhagenconsensus.com/sites/default/files/2023-03/Nutrition%20Best%20Investment%20Manuscript%20230211.pdf)
  - Agricultural R&D: 33. Source: [CCC manuscript](https://copenhagenconsensus.com/sites/default/files/2023-03/Ag%20R&D%20Best%20Investment%20Manuscript%20230311.pdf)
  - Malaria: 48 (secondary). Source: [EA Forum summary](https://forum.effectivealtruism.org/posts/WeruztmEM53mLjbkL/copenhagen-consensus-center-s-best-investment-papers-for-the)
  - E-procurement: 125 (secondary; the same EA Forum post gives a range of 18 to 125). Source: [EA Forum summary](https://forum.effectivealtruism.org/posts/WeruztmEM53mLjbkL/copenhagen-consensus-center-s-best-investment-papers-for-the)
  - Other policies in the set: childhood immunisation (about $7.6 billion in investment, BCR not confirmed), education, trade, land tenure, and highly skilled migration. Sources: [CCC research page](https://copenhagenconsensus.com/halftime-sustainable-development-goals-2016-2030/research); [lomborg.com](https://lomborg.com/best-things-first)
- **Discounting and mortality valuation in Halftime papers:**
  - The vaccine (DOVE model) paper uses an 8% base discount rate "following CCC guidance" and anchors VSL at about 160 × GDP per capita. The exact formula was not read. Source: [JBCA vaccine paper PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/27886D1E905A32EF04A4C9CEA559E119/S2194588823000118a.pdf/sustainable-development-goal-halftime-project-benefit-cost-analysis-using-methods-from-the-decade-of-vaccine-economics-model.pdf)
  - The chronic-disease paper also uses 8%. Source: [CCC chronic disease](https://copenhagenconsensus.com/sites/default/files/2023-04/Chronic%20Dieseases%20Manuscript%20230211_0.pdf)
  - The maternal and newborn paper values a DALY with a VSLY of about $2,983 for low- and lower-middle-income countries. Source: [CCC MNH](https://copenhagenconsensus.com/sites/default/files/2023-03/Maternal%20and%20Newborn%20health%20Manuscript%20230211_1.pdf)
  - Commentators note that 8% is about double the roughly 4% common in cost-effectiveness work. Source: [EA Forum](https://forum.effectivealtruism.org/posts/WeruztmEM53mLjbkL/copenhagen-consensus-center-s-best-investment-papers-for-the)
- **Earlier CCC rounds used different parameters:**
  - A review of the post-2015 project says analysts were told to use **3% and 5%** with sensitivity analysis. Source: [Anderljung, "Weighing the World"](https://copenhagenconsensus.com/sites/default/files/documents/weighing_the_world-_cost-benefit_analyses_of_the_sustainable_development_goals_-_markus_anderljung_1.pdf)
  - Haiti Priorise (2017) required DALYs to be valued at three multiples of GDP per capita. Source: [Haiti Priorise cholera paper](https://copenhagenconsensus.com/sites/default/files/documents/haiti_priorise_cholera_-_english.pdf)
  - CCC discounting has long been criticised (2006 commentary). Source: [Emerald, *J. Risk Finance* 2006](https://www.emerald.com/insight/content/doi/10.1108/jrf.2006.29407aaf.002/full/html)

### Inferences
- CCC's core design is the minimal design for a cross-sector tool: a single discount rate, a single VSL/VSLY or DALY value scaled to income, the same benefit-accounting conventions, BCRs reported with sensitivity, and an expert panel ranking. Its main weaknesses for a government tool:
  - no marginal-cost-of-funds adjustment;
  - BCRs are averages for packages at a given scale, not marginal curves;
  - little attention to implementation efficiency or absorptive capacity;
  - the quality of review for the 2023 issue is explicitly not standard JBCA peer review.
- The very high BCRs (18–125) concentrate on mortality-reducing health interventions and governance reforms (e-procurement, land tenure). Climate transformations evaluated in SISEPUEDE/CDPM will usually show BCRs of about 1–5, as in Costa Rica (≈2.1 = 78/37) and *Lifelines* (≈4). They will rank lower unless avoided climate damages and co-benefits are monetised on a comparable basis. In the tool, that comparability is set by the carbon price and the VSL.

### Gaps
- **Country Priorities projects** (Bangladesh Priorities, India Consensus with Andhra Pradesh and Rajasthan Priorities, Ghana Priorities). Their years, top BCRs and harmonised parameters were not verified; only Haiti Priorise was confirmed.
- **Complete Halftime parameter sheet.** The full methodology (discount-rate sensitivity values, the exact VSL formula and elasticity) and the immunisation BCR (believed to be about 101) are not verified.

---

## Q5. Health: DCP3 packages, cost-effectiveness thresholds, and converting DALYs or deaths to money (VSL/VSLY and the BCA Reference Case)

### Takeaway
- **Health is the sector with the most developed "efficient package" tools.** DCP3 costs an Essential UHC package of 218 interventions at about $79 per capita in LICs and $130 per capita in LMICs (about 8% and 4.2% of GNI). A 115-intervention highest-priority subset costs about half as much.
- **Thresholds.** The WHO-CHOICE 1–3× GDP-per-capita cost-per-DALY threshold has been replaced in the literature by supply-side "opportunity cost" thresholds, which are far lower (Ochalek, Claxton et al.).
- **Monetising for cross-sector BCA.** The Robinson–Hammitt reference case transfers VSL from the US using a VSL/income ratio of about 160–170 and an income elasticity of about 1.5, with sensitivity analysis.

### Cited Findings
- **Watkins et al. (2020)**, "Resource requirements for essential universal health coverage: a modelling study based on findings from Disease Control Priorities, 3rd edition," *Lancet Global Health*. Results at 80% coverage, in 2016 US$:
  - **Full EUHC package (218 interventions):** $79 per capita per year in LICs (95% CrI 60–110) and $130 (100–180) in LMICs. That is 8.0% (5.7–11.3) and 4.2% (2.9–5.9) of 2015 GNI.
  - **Highest-priority sub-package (115 interventions):** about half the cost, 3.7% of GNI in LICs and 2.0% in LMICs. The DCP3 site refers to a 108-intervention "HPP", and a commentary refers to 112; the count depends on the version.
  - **Cost structure:** mortality-reducing interventions account for about two-thirds of cost. Sources: [PMC7248571](https://pmc.ncbi.nlm.nih.gov/articles/PMC7248571); [DCP3 PDF](https://www.dcp-3.org/sites/default/files/resources/1-s2.0-S2214109X20301212-main_1.pdf); [DCP3 site](https://www.dcp-3.org/dcp3)
- **Ochalek, Lomas & Claxton (2018)**, "Estimating health opportunity costs in low-income and middle-income countries: a novel approach and evidence from cross-country data," *BMJ Global Health* 3(6): e000964.
  - Method: country-specific cost-per-DALY-averted thresholds based on health opportunity costs, i.e. the mortality and DALY effect of marginal health spending.
  - Coverage: initial estimates for 123 countries (per the CHE briefing).
  - Argument: widely cited thresholds are "not founded on an assessment of the likely health opportunity costs" and their use "is likely to reduce rather than improve health outcomes overall."
  - Caveat: the underlying elasticities (e.g., Nakamura et al. 2016) are unstable. Sources: [PMC6231096](https://pmc.ncbi.nlm.nih.gov/articles/PMC6231096); [CHE RP 122](https://eprints.whiterose.ac.uk/135883/1/CHERP122_cost_DALY_LMIC_threshold.pdf); [CHE policy brief](https://idsihealth.org//wp-content/uploads/2016/12/Cost-per-DALY-thresholds-CHE-PRB-2016.pdf)
- **Woods, Revill, Sculpher & Claxton (2016)**, "Country-Level Cost-Effectiveness Thresholds: Initial Estimates and the Need for Further Research," *Value in Health* 19(8): 929–935. They derive thresholds from the UK NHS estimate using income elasticities of the value of health. Opportunity-cost thresholds fall "far below the range previously posited by the WHO." Source: [White Rose](https://eprints.whiterose.ac.uk/112025)
- **Robinson, Hammitt & O'Keeffe (2019)**, "Valuing Mortality Risk Reductions in Global Benefit-Cost Analysis," *JBCA* 10(S1): 15–50.
  - Evidence base: 26 VSL studies across the 172 countries that were LMICs at some point in the past 20 years; few or no direct estimates for most LMICs.
  - Recommendation: transfer values using a base value and an income elasticity, with standardised sensitivity analysis.
  - Parameters reported in search summaries: base VSL/income ratios of 80–170 (spanning the OECD and World Bank practice). The VSL/income ratio for LMICs should not exceed the US ratio (about 170). Comparisons imply elasticities of 1.2–2.6 (median 1.5).
  - Application: a separate LMIC study applying these options reports a VSL of $76,000 at 100× GNI per capita and $121,000 at 160× GNI per capita.
  - Sources: [PMC7473065](https://pmc.ncbi.nlm.nih.gov/articles/PMC7473065/); [2017 draft PDF](https://content.sph.harvard.edu/wwwhsph/sites/2447/2017/09/Robinson-Hammitt-OKeeffe-VSL-2017-10-27.pdf); [JBCA LMIC estimates article](https://www.cambridge.org/core/journals/journal-of-benefit-cost-analysis/article/estimating-the-values-of-mortality-risk-reductions-in-low-and-middle-incomecountries1/C8755CC23245A642F547F33FDA3E8BAE)
- **Hammitt & Robinson (2011).** US-based studies suggest income elasticities of 0.4–0.6, while LMIC studies often assume 1.0. They argue for higher elasticities when transferring to low-income populations. Source: [ResearchGate](https://www.researchgate.net/publication/227378612_The_Income_Elasticity_of_the_Value_per_Statistical_Life_Transferring_Estimates_between_High_and_Low_Income_Populations). Related: [Viscusi & Masterman, "Income Elasticities and Global Values of a Statistical Life," JBCA](https://www.cambridge.org/core/journals/journal-of-benefit-cost-analysis/article/income-elasticities-and-global-values-of-a-statistical-life/5AE299883F668DCC265C41A377E1E063)
- **Robinson, Hammitt et al. (2019)**, *Reference Case Guidelines for Benefit-Cost Analysis in Global Health and Development* (May 2019, Gates-funded, about 19 authors). They provide default parameter values and build on the March 2019 JBCA special issue (intro: Robinson, Hammitt, Jamison & Walker, JBCA 10: 1–14). Sources: [Guidelines PDF](https://content.sph.harvard.edu/wwwhsph/sites/2447/2019/05/BCA-Guidelines-May-2019.pdf); [Summary PDF](https://www.econ.umd.edu/sites/www.econ.umd.edu/files/pubs/BCA%20Guidelines%20Summary%20May%202019.pdf); [Harvard CHDS repository](https://repository.chds.hsph.harvard.edu/repository/collection/bca-low-and-middle-income-countries/resource/3348)
- **Applied lessons.** A JBCA article examines "Lessons from Applying Value of Statistical Life and Alternate Methods to Benefit–Cost Analysis to Inform Development Spending." Source: [Cambridge](https://www.cambridge.org/core/journals/journal-of-benefit-cost-analysis/article/lessons-from-applying-value-of-statistical-life-and-alternate-methods-to-benefitcost-analysis-to-inform-development-spending/739EE6278D90030793671EC15226E23C)

### Inferences
- **Two conversion routes for health.**
  - *Welfare-economic route* (needed for cross-sector BCA): deaths averted × VSL, or life-years × VSLY, with VSL = VSL_US × (GNIpc_c / GNIpc_US)^1.5 and a sensitivity at elasticity 1.0 and at a ratio of 100–160× GNIpc.
  - *Health-system opportunity-cost route*: DALYs ÷ the supply-side threshold, giving "health-equivalent" net benefit. This is useful inside the health envelope, but not across sectors.
  - For SISEPUEDE/CDPM, the first route should be the default. Air-pollution and accident co-benefits are already mortality-based, so health interventions and climate co-benefits then share one VSL.
- **The DCP3 per-capita costs** give a top-down cost benchmark ($79 per capita in LICs, $130 in LMICs; about half for the priority subset) for a health "transformation" block. Unit costs can be scaled by the health-efficiency score from Q1.

### Gaps
- **Reference Case defaults not confirmed:** the exact numbers (base ratio 160 vs 170, a floor of about 20× income, VSLY derivation, recommended discount rate of 3%). My prior understanding (UNVERIFIED) is: a US VSL/GNIpc ratio of 160, extrapolation at elasticity 1.5 with a lower bound of 20× GNIpc, sensitivity at elasticity 1.0 and at 100× GNIpc, and a 3% real discount rate with sensitivity analysis.
- **Country threshold values** from Woods et al. and Ochalek et al. (e.g., the share of GDP per capita) were not extracted.
- **Other items not verified:** the WHO-CHOICE threshold critique papers (e.g., Marseille et al. 2015 and Bertram et al. 2016 in *Bull. WHO*), the DCP3 main volume (Jamison et al. 2018, vol. 9), and IHME or World Bank VSL guidance (e.g., the World Bank/IHME 2016 *Cost of Air Pollution* VSL transfer).

---

## Q6. Education: Smart Buys, LAYS per $100, and returns to schooling

### Takeaway
Education cost-effectiveness evidence is now harmonised in two ways:
- **Learning-adjusted years of schooling (LAYS) per $100.** The best programmes deliver about 3 LAYS per $100 per child, while many interventions deliver about 0. Angrist et al. 2020 underpins the GEEAP "Smart Buys" tiers, with structured pedagogy, teaching at the right level and parent-directed ECD as "Great Buys".
- **Monetisation.** LAYS can be converted to money with the about 9% private return per year of schooling (Psacharopoulos & Patrinos 2018), which makes cross-sector BCRs possible.

### Cited Findings
- **Angrist, Evans, Filmer, Glennerster, Rogers & Sabarwal (2020)**, "How to Improve Education Outcomes Most Efficiently? A Comparison of 150 Interventions Using the New Learning-Adjusted Years of Schooling Metric," World Bank PRWP 9450 / CGD WP 558.
  - Scope: 150 impact evaluations in 46 countries.
  - Findings: the most cost-effective programmes deliver "the equivalent of three additional years of high-quality schooling for just $100 per child," compared with "zero years for other classes of interventions."
  - Why LAYS: it addresses the problem that standard-deviation gains are relative to local distributions. Sources: [CGD PDF](https://cgdev.org/sites/default/files/how-improve-education-outcomes-most-efficiently-comparison-150-interventions-using-new.pdf); [World Bank OKR](https://openknowledge.worldbank.org/entities/publication/2a873f3a-1bd1-577f-aef0-bc7c386d0fb5); [RePEc CGD WP 558](https://econpapers.repec.org/RePEc:cgd:wpaper:558)
  - Update: a 2023 Blavatnik School WP (BSG-WP-2023-057) finds teaching at the right level and structured pedagogy (lesson plans plus training plus monitoring) among the most consistently cost-effective approaches. Source: [BSG WP 2023-057](https://www.bsg.ox.ac.uk/sites/default/files/2023-12/BSG-WP-2023-057%20How%20to%20Improve%20Education%20Outcomes%20Most%20Efficiently.pdf)
- **GEEAP (2023)**, *Cost-Effective Approaches to Improve Global Learning: What Does Recent Evidence Tell Us Are "Smart Buys"?* This is the third GEEAP report, updating the 2020 edition.
  - Evidence base: more than 13,000 additional studies screened, giving more than 400 high-quality evaluations.
  - Tiers: Great Buys, Good Buys, Promising but Limited Evidence, Effective but Relatively Expensive, and a fifth tier.
  - Great Buys include structured pedagogy, targeting instruction by learning level, and parent-directed early-childhood stimulation. Sources: [World Bank press release, 9 May 2023](https://www.worldbank.org/en/news/press-release/2023/05/09/education-smart-buys-cost-effectively-supporting-teachers-and-parents-can-lead-to-significant-learning-improvements); [World Bank feature, 21 June 2023](https://www.worldbank.org/en/news/feature/2023/06/21/evidence-based-cost-effective-learning-education-improvements); [UKFIET blog](https://www.ukfiet.org/2023/cost-effective-education-interventions-for-learning-impact-what-have-we-found-and-where-are-the-gaps/)
- **Psacharopoulos & Patrinos (2018)**, "Returns to investment in education: a decennial review of the global literature," *Education Economics* 26(5): 445–458 (WB PRWP 8402).
  - Evidence base: 1,120 estimates in 139 countries, 1950–2014.
  - Private return: about **9% per year of schooling**, stable over decades.
  - Social returns: above 10% at secondary and higher levels.
  - Returns are higher for women and in low-income countries. Sources: [IDEAS](https://ideas.repec.org:443/a/taf/edecon/v26y2018i5p445-458.html); [WB PRWP 8402](https://ideas.repec.org/p/wbk/wbrwps/8402.html)
- **Copenhagen Halftime** lists an education intervention among its 12 best investments. The specific BCR was not confirmed in this session. Source: [lomborg.com](https://lomborg.com/best-things-first)

### Inferences
- **A simple "value of a LAYS"** for the tool is PV(lifetime earnings gain) = Σ_t [r_s × w_t × employment_t] / (1+δ)^t, with r_s ≈ 0.09 (private) or above 0.10 (social, secondary). The gain starts at labour-market entry, so heavy discounting (e.g., CCC's 8%) penalises education relative to near-term health benefits. Discount-rate sensitivity is therefore essential.
- **LAYS per $100** can be read directly as a sector-internal cost-effectiveness frontier: sort interventions by LAYS per $, then convert to money for the cross-sector frontier.

### Gaps
- **Not extracted:** the full Great Buys / Good Buys list and the fifth tier's name in GEEAP 2023, and LAYS per $100 for specific interventions.
- **Not verified:** the CCC Halftime education BCR (my prior understanding is that it covers teaching at the right level and structured pedagogy; UNVERIFIED).

---

## Q7. Social protection: MVPF, cash-transfer multipliers, and cash benchmarking

### Takeaway
- **Cross-policy metric.** The MVPF (willingness-to-pay ÷ net fiscal cost; Hendren & Sprung-Keyser 2020) puts every policy on one scale. A non-distortionary cash transfer has MVPF = 1, which is the natural benchmark for "cash benchmarking". Child health and education investments often reach very high or even infinite MVPFs because they pay for themselves.
- **Evidence from LMICs.** GE effects can push the welfare value of cash above 1: the local multiplier in Kenya is 2.5 (Egger et al. 2022), and a Brazil paper shows tax-revenue feedback raising the MVPF of Bolsa Família.
- **Financing side.** The marginal cost of public funds (MCF) in African countries averages about 1.1–1.2 (Auriol & Warlters 2012).

### Cited Findings
- **Hendren & Sprung-Keyser (2020)**, "A Unified Welfare Analysis of Government Policies," *QJE* 135(3): 1209–1318 (NBER WP 26144).
  - Scope: 133 US policy changes covering social insurance, education and job training, taxes and cash transfers, and in-kind transfers.
  - Definition: MVPF = beneficiaries' willingness to pay ÷ net cost to government, including long-run fiscal externalities.
  - Findings: direct investments in low-income children's health and education have historically had the highest MVPFs, often infinite because they are self-financing. Adult-targeted policies are mostly 0.5–2. Sources: [Hendren site](https://hendren.scholars.harvard.edu/publications/unified-welfare-analysis-government-policies); [NBER WP 26144](https://www.nber.org/system/files/working_papers/w26144/revisions/w26144.rev1.pdf); [Stanford summary](https://inequality.stanford.edu/node/10240)
- **Egger, Haushofer, Miguel, Niehaus & Walker (2022)**, "General Equilibrium Effects of Cash Transfers: Experimental Evidence from Kenya," *Econometrica* 90(6): 2603–2643.
  - Design: about USD 1,000 transfers to more than 10,500 poor households in 653 randomised villages, a shock of more than 15% of local GDP.
  - Findings: large spillovers to non-recipients and firms, minimal price inflation, and a **local transfer multiplier of 2.5**.
  - Earlier NBER WP 26600 versions reported 2.6–2.7, so cite the Econometrica figure. Sources: [NBER WP 26600](https://www.nber.org/system/files/working_papers/w26600/w26600.pdf); [Weiss Fund](https://weissfund.uchicago.edu/working-papers/general-equilibrium-effects-of-cash-transfers-experimental-evidence-from-kenya/); [teaching slides](https://emiguel.econ.berkeley.edu/wordpress/wp-content/uploads/2019/11/GE_ECMA_TeachingSlides.pdf)
- **"Cash Transfers and the Local Economy: Evidence from Brazil"** (Econometrica, forthcoming; authors not confirmed in search).
  - Benchmark: the MVPF of a non-distortionary transfer is 1.
  - Findings: local demand effects that raise tax revenue can substantially increase the MVPF. Means-testing can lower it if it discourages formal employment. Source: [Econometric Society PDF](https://www.econometricsociety.org/publications/econometrica/forthcoming-papers/0000/00/00/Cash-Transfers-and-the-Local-Economy-Evidence-from-Brazil/file/19856-4.pdf)
- **Niehaus & Suri (2024), handbook chapter on cash transfers in LMICs.** Covers optimal public-finance issues: incidence within and across households, value under financial frictions, and external effects. Source: [UCSD PDF](https://econweb.ucsd.edu/~pniehaus/papers/handbook_chapter_cash_transfers.pdf)
- **Auriol & Warlters (2012)**, "The marginal cost of public funds and tax reform in Africa," *Journal of Development Economics* 97(1): 58–72 (earlier World Bank PRWP 3679, 2005; IDEI WP 2007).
  - Method: CGE-based MCF estimates for five tax instruments in 38 African countries.
  - Findings: a base-case average MCF of about 1.2, and about 1.1 for each country's lowest-cost instrument (often VAT). The earlier WP gave 1.17. A larger informal sector means higher MCF, and MCF is not strongly related to income. Sources: [UT Capitole PDF](https://publications.ut-capitole.fr/id/eprint/975/1/auriol_975.pdf); [World Bank PRWP 3679](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/358481468003006205)

### Inferences
- **MVPF as a common currency.** It handles the fiscal-externality problem that BCR ignores: induced tax revenue, avoided transfers, and climate-policy revenue recycling. Hendren-style comparison rule: reallocate from policy A to B if MVPF_B > MVPF_A. If the tool sticks with BCR, the equivalent is BCR_adj = PV(benefits) / [MCF × PV(net fiscal cost)].
- **Cash as the benchmark.** An unconditional transfer is valued at about 1 per $ by recipients (before GE effects). Any sector programme with welfare value per fiscal $ below about 1 (or below MCF) is dominated by cash, which is the logic of cash benchmarking. The Kenya multiplier (2.5) is an *output* multiplier, not a welfare MVPF. It should not be dropped into a BCR as a benefit without addressing double counting and displacement.
- **MCF default.** About 1.1–1.2 for Sub-Saharan Africa (Auriol & Warlters), higher where informality is large.

### Gaps
- **Not found:** a multi-country set of MVPFs for LMIC cash transfers, and the Brazil paper's authors (believed to be Gerard, Naritomi & Silva; UNVERIFIED).
- **Cash benchmarking literature** not verified. My prior understanding (UNVERIFIED) is McIntosh & Zeitlin's USAID/GiveDirectly benchmarking studies in Rwanda (e.g., *J. Development Economics* 2022).
- **Not verified:** Dahlby (2008), *The Marginal Cost of Public Funds: Theory and Applications* (MIT Press), and Finkelstein & Hendren (2020, *JEP*) on MVPF. Details UNVERIFIED.
- **No search budget remained** for the Policy Impacts Library or the global MVPF database.

---

## Q8. Infrastructure, water and resilience: BCRs

### Takeaway
Representative headline BCRs:
- resilient infrastructure: median about 4 (*Lifelines*);
- adaptation across five areas: 2–10, with about $7.1 trillion of net benefits from $1.8 trillion (Global Commission on Adaptation 2019);
- universal sanitation: 5.5; drinking water: 2.0; combined 4.3 (Hutton 2013).

These are global averages from model-based exercises and are scenario-dependent. They are useful as priors or bounds, not as country parameters.

### Cited Findings
- **Lifelines (World Bank 2019).** Median net benefit of $4.2 trillion, a BCR of about 4, and BCR > 1 in 96% of scenarios (see Q3 for details). Sources: [OKR](https://openknowledge.worldbank.org/handle/10986/31913); [PRWP 8896](https://ideas.repec.org/p/wbk/wbrwps/8896.html); [summary](https://thewaternetwork.com/article-FfV/lifelines-the-resilient-infrastructure-opportunity-world-bank-report-6SFu5CdSuGmnGpSdKNARew)
- **Global Commission on Adaptation (2019)**, *Adapt Now: A Global Call for Leadership on Climate Resilience*.
  - Headline: investing $1.8 trillion globally in 2020–2030 across five areas could generate $7.1 trillion in net benefits.
  - The five areas: early warning systems, climate-resilient infrastructure, improved dryland agriculture, mangrove protection, and water resource resilience.
  - BCRs range from about 2:1 to 10:1, in some cases higher. Sources: [WRI press release](https://www.wri.org/news/2019/09/release-global-leaders-call-urgent-action-climate-adaptation-commission-finds); [UNEP press release](https://www.unep.org/news-and-stories/press-release/global-leaders-call-urgent-action-climate-adaptation-commission); [WRI blog](https://www.wri.org/blog/2019/09/4-things-know-about-global-adaptation-challenge)
- **Hutton (2013)**, "Global costs and benefits of reaching universal coverage of sanitation and drinking-water supply," *Journal of Water and Health*.
  - Global BCRs: **5.5 for sanitation, 2.0 for water supply, 4.3 combined**. Benefits counted are health gains and access-time savings.
  - Costs: $35 billion per year for sanitation and $17.5 billion per year for water over 2010–2015, concentrated in South Asia, East Asia and SSA. Sources: [SuSanA library](https://susana.org/knowledge-hub/resources?id=3636); [WASHplus blog](https://blogs.washplus.org/drinkingwaterupdates/2013/01/global-costs-and-benefits-of-reaching-universal-coverage-of-sanitation-and-drinking-water-supply/index.html)

### Inferences
- **Benefit streams per sector.** For roads, water and resilience, BCRs depend on a few streams: time savings (value of time), avoided asset losses and service disruptions, health (VSL), and productivity. These overlap with SISEPUEDE transport co-benefits, and the time-value and VSL parameters must be shared to avoid inconsistency.
- **Scenario-share reporting.** *Lifelines'* "share of scenarios with BCR > 1, > 2, > 4" is a compact way to report risk-adjusted BCRs in a cross-sector table.

### Gaps
- **Not verified:** Hutton's journal volume and pages (believed to be *J. Water Health* 11(1): 1–12, 2013; UNVERIFIED); country-level WASH BCRs (e.g., the Hutton & Haller 2004 WHO study); and GCA methodology details (the background paper by Hallegatte et al., discount rate).
- **Roads BCRs** for rural roads in LMICs (beyond IFPRI's per-rupee rankings) were not searched.

---

## Q9. Economy-wide and general-equilibrium CBA, linking sectoral CBA to macro-fiscal models, and government practice (Green Book, Spending Reviews)

### Takeaway
- **When partial equilibrium is enough.** Partial-equilibrium CBA is adequate for small, marginal projects in undistorted markets. It breaks down when:
  - projects are large relative to the economy (e.g., cash transfers above 15% of local GDP);
  - prices adjust;
  - pre-existing distortions (taxes, informality, agglomeration externalities) mean secondary-market effects carry welfare weight.
- **Three bridges exist:**
  - *CGE-consistent welfare measurement*: Farrow & Rose 2018, plus MCF estimated from CGE models.
  - *Specific "wider economic impact" add-ons*: UK DfT TAG A2.x (agglomeration and productivity).
  - *Macro-structural or CGE models fed by sectoral investment and returns*: World Bank CCDRs, where sector models feed MANAGE (CGE) and MFMod; and the IMF DIG/DIGNAR models with explicit efficiency and return parameters.
- **Government cross-department prioritisation.** HM Treasury's Green Book and Spending Reviews, and OECD spending reviews, are the institutional analogues. They were not verified in this session.

### Cited Findings
- **Farrow & Rose (2018)**, "Welfare Analysis: Bridging the Partial and General Equilibrium Divide for Policy Analysis," *JBCA* 9(1): 67–83, DOI 10.1017/bca.2017.29 (open access; JBCA Best Article 2018).
  - Argument: CGE advances have narrowed the theoretical gap between PE and GE welfare measures. They discuss shared foundations, functional specification, common price movements and closure rules.
  - Policy challenge: they question the OMB guidance against counting GE (secondary) effects and suggest relaxing it. Sources: [Cambridge](https://resolve.cambridge.org/core/journals/journal-of-benefit-cost-analysis/article/welfare-analysis-bridging-the-partial-and-general-equilibrium-divide-for-policy-analysis/6ECE243839186E36C848B0E83EAAA8CF); [UMBC WP version](https://economics.umbc.edu/files/2016/10/WP_16_02.pdf)
- **World Bank CCDR macro modelling.**
  - Türkiye CCDR Background Note 6: sector-level models (power, transport, buildings, forest landscapes) feed MANAGE (a single-country, recursive-dynamic CGE with energy and emissions) and MFMod (macro-structural). Together they assess growth, household welfare, employment and mitigation trade-offs of a net-zero pathway. Source: [World Bank OKR (Türkiye CCDR background note)](https://openknowledge.worldbank.org/entities/publication/b24de6a0-d160-4410-958c-311494a1a303)
  - Argentina CCDR Background Note 9: MFMod's macro-structural design (identities plus error-correction behavioural equations) and CPAT for carbon pricing and fuel-subsidy reform (emissions, fiscal, GDP, co-benefits). Climate-aware MFMod versions are a principal CCDR tool. Source: [World Bank documents](https://documents.banquemondiale.org/fr/publication/documents-reports/documentdetail/099250212052236552)
  - MFMod exists as a linked system of 184 country models and has been the Bank's main forecasting and analysis tool since 2015. The MANAGE-WB user guide is PRWP 11258. Sources: [World Bank Macro-Modeling publications](https://www.worldbank.org/en/programs/economicpolicy-macro-modeling/publications); [GTAP resource (MANAGE)](https://gtap.agecon.purdue.edu/resources/res_download.asp?D_ID=12287)
- **IMF DIG/DIGNAR.** These models carry an explicit public-investment efficiency parameter and a return on public capital, and have been applied in 65+ countries (see Q1). Source: [IMF WP 19/62](https://www.imf.org/en/Publications/WP/Issues/2019/03/18/Some-Policy-Lessons-from-Country-Applications-of-the-DIG-and-DIGNAR-Models-46665)
- **MCF from CGE models.** Auriol & Warlters use a CGE model to estimate MCF for 38 African countries (about 1.1–1.2; see Q7), which is the standard way to bring economy-wide tax distortions into project BCRs. Source: [World Bank PRWP 3679](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/358481468003006205)
- **UK DfT Transport Analysis Guidance (TAG).**
  - Unit A2.1 is the overview of wider economic impacts.
  - Unit A2.4, "Appraisal of Productivity Impacts" (May 2025 version), covers transmission mechanisms and displacement, agglomeration, and static and dynamic clustering. It is used with the WITA software.
  - The A2 family was restructured after a 2016 consultation and became definitive in May 2018. Sources: [TAG A2.4 May 2025 PDF](https://assets.publishing.service.gov.uk/media/6899e4c7ad0cbc0e2764320e/tag-unit-a2-4-productivity-impacts-may-25.pdf); [TAG A2.1 overview](https://assets.publishing.service.gov.uk/media/600ea9258fa8f5654ca409df/tag-unit-a2-1-wider-impacts-overview-document.pdf); [gov.uk A2.4 page](https://www.gov.uk/government/publications/webtag-tag-unit-a2-4-productivity-impacts-may-2018); [2016 consultation](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/554783/transport-appraisal-guidance-webtag-consultation-document.pdf)
- **Egger et al. (2022)** is the leading experimental demonstration of GE effects of a large transfer (multiplier 2.5, >15% of local GDP). Source: [NBER WP 26600](https://www.nber.org/system/files/working_papers/w26600/w26600.pdf)

### Inferences
- **A practical "economy-wide CBA" architecture** (as in CCDRs) is two-layered:
  - *Layer 1*: sector or transformation BCA (SISEPUEDE/CDPM, plus new sector modules).
  - *Layer 2*: a macro-fiscal model. It receives the *investment path* (as demand and capital accumulation, scaled by the efficiency parameter), *productivity or return shocks* (from Layer-1 benefits that are market productivity, e.g., time savings, health-driven labour supply, learning-driven human capital), and *fiscal flows* (costs, revenues, MCF).
  - Non-market benefits (VSL-valued mortality, carbon) stay in the welfare ledger and are not fed into GDP. This avoids double counting and matches the CCDR MANAGE/MFMod split.
- **When to use GE corrections.** Use them only when (i) the programme is large relative to GDP or a local economy, (ii) the relevant markets are distorted (taxes, informality, unemployment), or (iii) agglomeration or network effects are plausible (transport). Otherwise use PE CBA with MCF, which is what Farrow & Rose and TAG's approach imply.

### Gaps
- **HM Treasury Green Book and Spending Reviews** (2022 Green Book edition; STPR 3.5% declining after 30 years; the 2025 Spending Review's cross-department prioritisation and "zero-based" review). Not verified; the search budget ran out. Details are UNVERIFIED.
- **OECD spending-review practice** (e.g., the OECD survey on spending reviews and the share of member countries using them). Not verified.
- **World Bank MFMod-CC** documentation and how CCDRs translate sectoral investment needs and returns into growth (e.g., capital-productivity assumptions). Not extracted.
- **Not searched:** Dahlby's general-equilibrium CBA contributions, Nordhaus/IAM integration, ENVISAGE/GTAP appraisal uses, and the "DIG-type social return" calibration values (e.g., default returns on public capital of 10–25% in DIG applications). The latter is UNVERIFIED.
- **US OMB Circular A-94.** Its status (2023 revision and any 2025 reversal) was not verified.

---

## Q10. Implications for a practical tool (Python/Excel, extending SISEPUEDE/CDPM transformation CBA)

### Takeaway
Three components:
1. **Technical-efficiency haircut.** A sector-specific, output-oriented DEA/FDH efficiency score φ (0 < φ ≤ 1) scales outcomes per dollar, or equivalently multiplies unit costs by 1/φ. It should be bootstrapped for uncertainty and allowed to converge toward the frontier only with explicit PIM reform. The defaults the literature supports are about 0.7 for public investment and about 0.8–0.9 for education and health in developing countries.
2. **A common metric.** Use a risk-reported, MCF-adjusted BCR, or an MVPF. Both require only a short list of harmonised conversion factors.
3. **An allocative frontier.** Rank options by incremental BCR (divisible or mutually exclusive options), or solve a 0-1 knapsack (indivisible), across a range of budgets. Overlay robustness across scenario ensembles (RDM-style) to get a Pareto frontier of expected net benefit versus downside risk.

### Cited Findings (anchors for the parameters below)
- Public investment efficiency gap of about 30% on average; PIM reform closes up to two-thirds of it (IMF 2015) or more than half (*Well Spent* 2020). Sources: [IMF 2015](https://www.imf.org/en/Publications/Policy-Papers/Issues/2016/12/31/Making-Public-Investment-More-Efficient-PP4959); [IMF 2020 presentation](https://www.mof.go.jp/pri/research/seminar/fy2020/tff2020_publication_01.pdf)
- Health and education output efficiency of about 0.9 and 0.8 in developing countries (Herrera & Pang 2005, secondary). Source: [ADB EWP 435](https://www.adb.org/sites/default/files/publication/161539/ewp-435.pdf)
- Bootstrap inference for DEA second stages. Source: [Simar & Wilson 2007](https://research.dial.uclouvain.be/entities/publication/4ac5e6e9-969c-4278-8bb7-1d1aa03acfbe)
- Efficiency parameter and return on public capital as core DIG inputs. Source: [IMF WP 19/62](https://www.imf.org/en/Publications/WP/Issues/2019/03/18/Some-Policy-Lessons-from-Country-Applications-of-the-DIG-and-DIGNAR-Models-46665)
- Unit costs rise above about 10% of GDP public investment (about 7% in low-efficiency countries). Source: [IMF WP 2020 absorptive capacity](https://www.imf.org/en/Publications/WP/Issues/2020/02/28/On-the-Capacity-to-Absorb-Public-Investment-How-Much-is-Too-Much-49039)
- MCF of about 1.1–1.2 in Africa. Source: [Auriol & Warlters](https://publications.ut-capitole.fr/id/eprint/975/1/auriol_975.pdf)
- MVPF definition and benchmark (cash = 1). Sources: [Hendren & Sprung-Keyser](https://hendren.scholars.harvard.edu/publications/unified-welfare-analysis-government-policies); [Brazil paper](https://www.econometricsociety.org/publications/econometrica/forthcoming-papers/0000/00/00/Cash-Transfers-and-the-Local-Economy-Evidence-from-Brazil/file/19856-4.pdf)
- VSL transfer: ratio about 160–170 × income, elasticity about 1.5. Source: [Robinson, Hammitt & O'Keeffe 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC7473065/)
- About 9% private return per year of schooling. Source: [Psacharopoulos & Patrinos 2018](https://ideas.repec.org/p/wbk/wbrwps/8402.html)
- LAYS per $100 metric. Source: [Angrist et al. 2020](https://cgdev.org/sites/default/files/how-improve-education-outcomes-most-efficiently-comparison-150-interventions-using-new.pdf)
- Discount rates in practice: CCC Halftime uses 8% ([vaccine paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/27886D1E905A32EF04A4C9CEA559E119/S2194588823000118a.pdf/sustainable-development-goal-halftime-project-benefit-cost-analysis-using-methods-from-the-decade-of-vaccine-economics-model.pdf)), and the Costa Rica decarbonisation BCA uses 5% ([IDB](https://publications.iadb.org/en/benefits-and-costs-decarbonizing-costa-ricas-economy-informing-implementation-costa-ricas-national))
- Scenario-share BCR reporting. Source: [Lifelines PRWP 8896](https://ideas.repec.org/p/wbk/wbrwps/8896.html)
- MACC timing and deployment-rate caveat. Source: [Vogt-Schilb & Hallegatte 2014](https://openknowledge.worldbank.org/server/api/core/bitstreams/64f0e470-8ce9-5ad6-9fcf-94992a1766d5/content)

### Inferences

**(a) Computing and using a DEA/FDH technical-efficiency score as a haircut or parameter**

1. **Choose the unit and the sector.** The unit is a country-year panel per sector. Examples:
   - health: input = public health spending per capita (PPP); outputs = life expectancy or HALE, U5 survival;
   - education: input = spending per pupil; outputs = net enrolment, harmonised test scores or LAYS;
   - infrastructure: input = public capital stock per capita (PIM); output = infrastructure coverage and quality index (the PIE-X style).
   - Add non-discretionary inputs where possible (e.g., adult literacy, GDP per capita) or estimate separate frontiers by income group (Grigoli 2014).
2. **Compute the output-oriented score.**
   - *DEA-VRS*: for country o, solve max η s.t. Σ_j λ_j y_j ≥ η·y_o, Σ_j λ_j x_j ≤ x_o, Σ λ_j = 1, λ ≥ 0. The score is φ_o = 1/η ∈ (0, 1].
   - *FDH*: the same with λ_j ∈ {0, 1}, i.e. only observed peers that dominate o.
   - In Python this is a small LP per country (`scipy.optimize.linprog`) or an existing package. In Excel it is Solver per row, or a precomputed table.
3. **Get uncertainty.** Run a Simar–Wilson smoothed bootstrap (Simar & Wilson 1998, UNVERIFIED citation) for bias-corrected φ̂ and confidence intervals. At minimum, report DEA and FDH side by side (FDH ≥ DEA scores) as a band.
4. **Where no country-specific score exists,** use the defaults (public investment φ ≈ 0.70; health ≈ 0.90; education ≈ 0.80; lower for SSA and LICs) as triangular distributions.
5. **Use the score in the CBA in one of three equivalent ways, and pick only one so it is not counted twice:**
   - **Outcome haircut:** benefits per $ = frontier benefits per $ × φ. Use this when unit costs come from international norms such as DCP3, Smart Buys or engineering costs.
   - **Unit-cost markup:** effective unit cost = norm unit cost / φ. Use this for capital projects, which is equivalent to the DIG "efficiency parameter".
   - **Effective capital:** ΔK_eff = φ × I. Use this when passing investment to the macro-fiscal layer (Gupta et al. 2014; DIG).
6. **Model convergence and absorptive capacity.**
   - Make φ time-varying: φ_t = φ_0 + g·(1 − φ_0)·s_t, where s_t is a PIM-reform scenario switch and g ≤ 0.5–0.67 over the reform horizon. The speed is an assumption.
   - Add a scale penalty: unit cost multiplier rising when total public investment exceeds about 7–10% of GDP.
7. **Do not let φ do double duty.** If unit costs already come from that country's own historical outturns, which embed its inefficiency, set φ = 1 for costs and use it only in an "efficiency-reform" scenario.

**(b) A common cross-sector metric and the minimal conversion factors**

- **Primary metric: MCF-adjusted, risk-reported BCR**
  - BCR*_i = PV_δ(B_i) / [MCF × PV_δ(net fiscal cost_i) + PV_δ(non-fiscal costs_i)], where net fiscal cost = outlays − induced revenues − avoided transfers.
  - Report the mean over the scenario ensemble, P10/P90, and Pr(BCR* > 1). Report NPV alongside it, because BCR ranks only under a binding budget.
- **Alternative metric: MVPF_i = WTP_i / net fiscal cost_i.**
  - Compare against MCF: fund when MVPF > MCF, or rank by MVPF.
  - It is preferable for transfers and human-capital programmes with large fiscal externalities.
  - For non-market benefits it needs the same conversion factors as the BCR.
- **Minimal conversion-factor list** (one harmonised table, country-scaled):
  1. **Discount rate** δ, with sensitivity. Central 5% (as in the Costa Rica decarbonisation BCA), with 3% and 8% (CCC Halftime). Use a declining long-term rate if the government's guidance uses one.
  2. **MCF.** Default 1.2 (SSA average), with a range of 1.1–1.5. Higher with large informality.
  3. **VSL.** VSL_c = VSL_US × (GNIpc_c / GNIpc_US)^ε with ε = 1.5. Sensitivity: ε = 1.0, and a ratio of 100–160× GNIpc. VSLY = VSL / (discounted remaining life expectancy of the affected population), or the CCC-style VSLY per DALY. One VSL is used for health interventions, air-pollution co-benefits, road safety and disaster mortality.
  4. **Value of a LAYS or school year.** PV of a 9% (private) or 10%+ (social) earnings gain per LAYS over the working life, starting at labour-market entry.
  5. **Carbon price.** The government's or World Bank's shadow price of carbon path. A value is needed but none was verified in this session.
  6. **Value of time** (for transport, WASH access, roads). A share of the wage, from national guidance. Not verified.
  7. **Efficiency score φ** by sector (from part a).
  8. **Distributional weights** (optional). Not covered in this session.
  9. **Shadow wage and FX factors** (optional; standard MDB economic-analysis practice). Not covered.
- **Sector benchmarks to sanity-check computed BCRs:**
  - WASH: 2.0 (water), 5.5 (sanitation).
  - Resilient infrastructure: median about 4.
  - Adaptation: 2–10.
  - Copenhagen "best buys": 18–125 (pooled 52, at 8%).
  - Agricultural R&D: BCR 33 (CCC), about 60% average IRR (Alston et al. via FAO).
  - Decarbonisation package (Costa Rica): about 2.1.
  - Health opportunity-cost thresholds (Ochalek/Claxton) serve as a within-health check.

**(c) A simple algorithm for an allocative "efficient frontier" of a spending portfolio under a fiscal constraint**

1. **Inputs.**
   - Options i = 1…N, grouped by mutually exclusive families g. A family is the scale or design variants of one intervention or transformation, e.g., a SISEPUEDE transformation at ambition levels low, mid and high.
   - For each option: fiscal cost path c_it, benefit path b_its across scenarios s = 1…S (an RDM ensemble), sector, and earliest start or maximum deployment rate.
   - Budget path B_t, or a single PV budget B.
2. **Pre-process each family (incremental analysis).**
   - Sort the variants by PV cost.
   - Remove options with lower expected PV benefit than a cheaper option (strict dominance).
   - Compute incremental BCR_k = ΔPV(B) / [MCF × ΔPV(C)] between successive variants.
   - Remove variants that violate convexity (extended dominance: incremental BCR higher than the previous step's). Recompute until the incremental BCRs decline.
   - The result is each family's efficient-expansion path.
3. **Greedy frontier (divisible or near-divisible options; Excel-friendly).**
   - Pool all incremental steps across families.
   - Sort by incremental BCR in descending order, enforcing within-family order.
   - Cumulate cost and benefit.
   - Each cumulative point is on the budget-efficient frontier (an upper concave hull of cumulative NPV against cumulative cost). The incremental BCR at the budget line is the **shadow price of public funds** (the cutoff BCR).
   - Fund all steps with incremental BCR ≥ max(cutoff, MCF).
4. **Exact frontier (indivisible options; Python).** Solve a 0-1 knapsack MILP with PuLP, OR-Tools or `scipy.optimize.milp`:
   - Objective: maximise Σ_i x_i · E_s[NPV_is].
   - Budget: Σ_i x_i · c_it ≤ B_t for all t.
   - Family exclusivity: Σ_{i∈g} x_i ≤ 1 for each family g.
   - Optional constraints: sector floors or caps (mandates, absorptive capacity, e.g., total public investment ≤ 7–10% of GDP); precedence (transformation B requires A); deployment-rate limits (the Vogt-Schilb & Hallegatte critique of static MACCs); an emissions-target constraint (Σ abatement ≥ target), which makes the problem MACC-consistent.
   - Sweep B over a grid to trace the frontier.
5. **Risk layer (Pareto with robustness).**
   - For each budget level, compute for the chosen portfolio: E[NPV], P10 NPV (or CVaR), max regret across scenarios, and Pr(portfolio BCR > 1).
   - Re-solve with the objective E[NPV] − λ·CVaR, or maximise P10 NPV, for λ ∈ [0, λ_max] to get a Pareto set of (expected value, downside) at each budget.
   - Optional: an Awerbuch-style mean–variance portfolio when the cost or benefit covariance across options is estimated from the ensemble. Rows are scenarios, columns are options, and Σ is their covariance.
   - Report the frontier as a chart: x = budget (or downside risk), y = expected NPV, with dots for current allocation and for sector-only optima. The gap between the current allocation and the frontier at the same budget is the **allocative-efficiency gain**. The gap from applying φ is the **technical-efficiency gain**.
6. **Diagnostics to report.**
   - Cutoff BCR compared with MCF: if the cutoff is well above MCF, there is a case for more spending or revenue; if below, the budget is too large for the available options.
   - Share of the budget by sector compared with the status quo.
   - Options that enter the frontier in more than 80% of scenarios (robust "no-regret" set; the *Lifelines*-style statistic).
   - Sensitivity of the frontier to δ (3/5/8%), the VSL elasticity (1.0/1.5), the carbon price, and φ.

### Gaps
- **Not verified in this session:** carbon-price defaults (World Bank shadow carbon price guidance, national SCC), value-of-time defaults, and distributional-weight conventions. Each must be sourced before the conversion table is fixed.
- **Not tested:** the incremental-BCR, extended-dominance and knapsack procedures are standard operations-research and health-economics methods given here as inference, without a verified citation in this session. Candidates to check include Weingartner (1963), Salo, Keisler & Morton (2011), and the UK DfT value-for-money BCR categories (Poor < 1, Low 1–1.5, Medium 1.5–2, High 2–4, Very High > 4; UNVERIFIED). The UK Green Book capital-rationing guidance is also unchecked.
- **Not evaluated:** whether SISEPUEDE/CDPM's existing transformation outputs (costs and benefits by scenario) can be fed directly into step 1. That depends on the repo's data structures, which were not part of this research scope.
