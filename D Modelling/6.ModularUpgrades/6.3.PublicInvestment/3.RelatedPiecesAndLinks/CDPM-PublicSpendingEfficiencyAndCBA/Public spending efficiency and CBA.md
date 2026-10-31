---
title: "Cost-Benefit Analysis of Public Spending in SISEPUEDE: The Method and Its Upgrades"
subtitle: "How SISEPUEDE (now CDPM) values climate transformations today, and a Public Spending Value layer that adds the budget, delivery efficiency, financing and other sectors, and links the results to the GIMF, DIGNAD and DIGNAR tool"
date: "October 20, 2026"
---

# Executive summary

Governments have more calls on their money than money. They must decide
what to pay for, and how to get more from each dollar. The first is
*allocative* efficiency: doing the right things. The second is
*technical* efficiency: doing things well. Most spending reviews
measure the second. The larger gains usually come from the first.

SISEPUEDE, the sector pathways model now called CDPM, already has a
cost-benefit module. For every climate transformation it compares a
strategy with a baseline and prices the difference: the technical cost
of the measure, the fuel and system costs it saves, and the health,
pollution, congestion and ecosystem benefits it brings. That is a strong
base. It covers every IPCC sector, values benefits that most models
ignore, and runs about a thousand futures.

But it answers a narrower question than a finance ministry asks. It
says whether a transformation is worth more to the economy than it
costs. It does not say who pays, what it does to the budget, how much
of the money becomes working assets, how it is financed, or whether a
dollar spent on it beats a dollar spent on a clinic or a road. This note
describes SISEPUEDE's method, rates it against international practice,
and sets out the upgrades that close those gaps.

**What SISEPUEDE does.** For each cost or benefit item and year, the
module multiplies the change in a physical quantity (vehicle-km,
hectares, tonnes, petajoules) by a unit cost factor in 2019 US dollars,
with an optional trend in the factor. It returns undiscounted annual
flows by sector, item and year. Present values are computed afterwards.
Power-sector capital comes instead from NemoMod, an embedded least-cost
model.

**Where it falls short.** Six gaps matter most for public spending
(Table 3 rates each):

1. **Discounting is ad hoc and inconsistent.** The module never
   discounts; studies have applied 7% or 5% afterwards; and power
   capital arrives already discounted by NemoMod, at a rate the files do
   not record.
2. **Capital is not shown, and is annualised at a zero interest rate.**
   "Technical cost" mixes capital, operating and avoided costs, and some
   unit factors spread capital in straight lines.
3. **No payer and no budget.** The module prices the resource cost of a
   measure, not who pays it, so it has no taxes, subsidies, fees or
   fiscal flows.
4. **No financing.** There is no cost of capital, no loan terms and no
   contract liabilities.
5. **No delivery.** It assumes every dollar becomes a working asset on
   time, which is far from true in low-capacity countries.
6. **Climate only.** Its measures are climate transformations, so it
   cannot rank them against health, education or road maintenance.

**The rule behind the upgrades.** For each possible use of public
money, ask what people get for each dollar the budget really pays.
"Really pays" means after three corrections: leave out what firms and
households would have done anyway; allow for money that never becomes a
working asset; and subtract the money the measure brings back to the
budget. Fund the measure if people get more than about USD 1.20 for each
such dollar. The extra 20 cents is the hidden cost to the economy of
raising a dollar of tax (λ, the *marginal cost of public funds*). When
money is short, fund the best value per dollar first. In the literature
the ratio is the *marginal value of public funds* (MVPF). With λ = 1 and
no budget limit, the rule reduces to the World Bank's usual net present
value test, so it extends Bank practice rather than replacing it.

**The upgrades.** A small *Public Spending Value* (PSV) layer sits
between SISEPUEDE, the team's investment-needs model (NMIM) and its
macro-fiscal models (GIMF-, DIGNAD- and DIGNAR-lite and LIC-DSF-lite).
It reads SISEPUEDE's output as it is and adds what is missing, in eleven
steps (Table 1).

**Table 1. The upgrades and the gaps they close**

| Upgrade (step) | What it adds | Gap closed |
|-----------------------|------------------------------|------------------------------|
| 1. Tag every flow | Payer, economic nature, NMIM financing type and budget function for each SISEPUEDE line | No payer and no budget |
| 2. Discount once | One social rate (6%), carbon as a switch, power capital re-derived undiscounted | Ad hoc discounting |
| 3. Delivery haircuts | Investment efficiency from PIMA or PEFA, execution delay from BOOST, cost overruns | No delivery |
| 4. Additionality | Public money pays only the viability gap; price instruments tested first | Whole cost charged to the state |
| 5. Fiscal ledger | Net budget flows by year, fiscal NPV, cash profile | No budget |
| 6. Decision metric | Value per net public dollar (MVPF) against λ | No public-funds test |
| 7. Capital and current | Capital recovery factors and recurrent costs; maintenance first | Capital hidden; zero-interest annualisation |
| 8. Financing routes | Loans, concessional finance, utilities, PPAs, guarantees, and their liabilities | No financing |
| 9. Revenue returns | Fees and savings counted in the budget, worth λ per dollar | No revenue treatment |
| 10. Allocative frontier | Ranking across sectors within the fiscal envelope; "sector cards" for health, education, roads, water, resilience and farming | Climate only |
| 11. Macro bridge | The chosen programme passed to the macro and debt models, which return the affordable envelope | No macro feedback |

**Extra care in low-capacity countries.** The rule is the same; the
numbers change. In low-income countries about 40% of the potential value
of public investment is lost (IMF 2015). The layer therefore haircuts
public capital for efficiency, treats slow execution as delay, funds
maintenance before new building, prefers simple auctioned contracts,
caps the speed of scale-up and makes complex programmes beat a simple
cash transfer.

**The upgrades at work: a small island.** Picture an island that makes
almost all its power from imported diesel, at about 23 cents a
kilowatt-hour. A USD 120 million solar-and-battery plant would cut its
fuel bill by about USD 20 million a year. Before financing it is worth
about USD 108 million more than it costs; SISEPUEDE's method would stop
there and call it excellent. The upgrades show why it may still not be
built. The only loan on offer runs for seven years. Repayments and
upkeep of about USD 25 million a year exceed the savings, and public
debt jumps by 6% of GDP overnight. The island is short of cash in the
early years and of room under its debt limits, not of a good project.
Table 10 shows the routes out: a long concessional loan is best on every
count; a competitively tendered power purchase agreement with a World
Bank or MIGA guarantee is a fair second, though its payments are a debt
in disguise worth 1.3 times the plant.

**The plan in four steps.**

1. Two to three weeks to write the specification, fix how existing
   SISEPUEDE results are discounted, and check the data for St Lucia,
   Uganda and Kenya.
2. Four to six weeks to build and test the core calculator (steps 1–7
   and 9).
3. Four to six weeks to add financing routes, contract liabilities and
   the link to the macro and debt models, with the island pilot.
4. Six to eight weeks to add other sectors, the frontier and BOOST
   comparisons.

Bolder options, including a version built into the macro model itself
(Option B), come later.

**A caution.** The external sources were checked against abstracts,
catalogue records and summaries, not full texts. Items marked † must be
checked against the primary text before outside use (Appendix J).

The next section sets out SISEPUEDE's method, the section after rates it,
and the following sections describe the upgrades, the island example
and the plan. The appendices hold the supporting material:

- Appendix A answers the nine questions that prompted this note;
- Appendix B reviews the literature;
- Appendix C describes World Bank and IMF practice;
- Appendix D describes the team's macro-fiscal tool and investment-needs
  model;
- Appendix E gives the worked example in full;
- Appendix F sets out Option B and wider upgrades to World Bank
  practice;
- Appendix G lists risks and open questions;
- Appendices H to K give the formulas, parameters, verification notes
  and a glossary.


# SISEPUEDE's cost-benefit method

## The model in brief

SISEPUEDE (*Sectoral Pathways and Uncertainty Exploration for
Decarbonization*), now renamed CDPM and called CPM or "CPT/CPM" inside
the Bank, is a quantity model. It represents a country's full greenhouse
gas inventory in about 15–16 IPCC subsectors: agriculture, forestry and
land use; livestock; waste and wastewater; industrial processes;
buildings; transport; fugitive emissions; and energy production. Each
sector is driven by population and GDP; demand does not respond to
price. GDP is exogenous and measured in 2019 PPP dollars, 3.6 times
CPAT's market dollars for Egypt.

Users define *transformations*, each coded `TX:<SECTOR>:<ACTION>` (for
example `ENTC:TARGET_RENEWABLE_ELEC`, "95% of electricity is generated
by renewables in 2050", or `WALI:INC_TREATMENT_URBAN`). Transformations
are bundled into *strategies* (identifiers 1000–6009, such as net zero or
an NDC) and run against a baseline. The model is calibrated to
historical emissions, solves the power sector with NemoMod (an
open-source least-cost model) and runs each strategy across about a
thousand futures drawn by Latin Hypercube sampling, with scenario
discovery to find the conditions under which a strategy fails (Kalra et
al. 2023; Groves et al. 2020).

The cost-benefit module is a separate package, `costs_benefits_ssp`. It
converts the physical differences between each strategy and the
baseline into money. The model is maintained by James Syme and Edmundo
Molina-Pérez's team at Tec de Monterrey, under a USD 215,000 partnership
with the Bank that runs to 20 March 2027. Its code is public
(`jcsyme/sisepuede`; `milocortes/costs_benefits_ssp`).

## The core equation

For each cost or benefit item $k$ in year $t$, the module compares the
strategy run $S$ with the baseline run $B$:

$$V_{k,t} = \left( x_{k,t}^{S} - x_{k,t}^{B} \right)\, m_{k}\, g_{k}^{\max(0,\, t - 8)}\quad\quad(1)$$

where:

- $x_{k,t}$ is the physical driver, such as vehicle-km by electric cars,
  hectares of primary forest, people with safely managed sanitation, or
  petajoules of fuel consumed;
- $m_{k}$ is the unit factor in 2019 US dollars, a Latin American
  average;
- $g_{k}$ is an annual change in the factor, such as a falling
  electric-vehicle premium;
- $t$ is the model period, with period 0 in 2015, so factors start to
  change in 2023.

The code confirms this form: the value is the strategy-minus-baseline
difference times the multiplier times the annual change raised to the
periods since 2023. Two variants are used for some items. A
*scale variable* makes the cost proportional to a level rather than a
difference. A *fraction change* makes it proportional to the change in a
share, such as the fraction of waste recycled. Technical costs of
transformations come from a separate table of costs per transformation.

Two post-processing steps follow:

- **Interactions.** `cb_process_interactions` rescales overlapping
  transformations so that, for example, efficiency savings are not
  counted twice when vehicles are also electrified. Each
  transformation's mean relative effect is normalised so the weights
  sum to one.
- **Cost shifting.** `cb_shift_costs` moves costs that fall before the
  start of transformations (2015–2024) forward, to 2025–2034, and sets
  the originals to zero.

## What is counted

The module sorts items into two families. *Technical* items are costs or
benefits that actors in a sector normally experience and that are
largely internal to markets. *Non-technical* items are tied to
development goals: crashes, air pollution, biodiversity, congestion
time. Each output line is named `cb:<sector>:<category>:<sub>:<detail>`,
and the third field gives one of 18 categories (Table 5 gives the
mapping proposed for the upgrade).

**Costs.** Technical cost is the main cost line: 455 of the 1,065 items
in the Uganda run. It is the cost of carrying out a transformation, but
it mixes capital, operating and avoided costs, so it is closer to a net
incremental cost than to gross investment. Some unit factors annualise
capital in a straight line: the electric car premium (USD 12,000 plus
USD 1,000 for charging) is spread over 15,000 km a year for 12 years,
giving USD 0.039 per vehicle-km, which is equivalent to a 0% interest
rate. Several building and industry factors are levelised costs with no
documented rate. Mode-shift infrastructure is not costed, because it is
"deeply uncertain, highly localized" (Kalra et al. 2023).

**Savings.** System cost, technical savings and fuel cost measure the
resources a transformation saves: fuel, generating capacity and
operating costs, valued at SISEPUEDE's fuel costs rather than at retail
or tax-inclusive prices.

**Wider benefits.** Air pollution (IMF values from Parry et al. 2014,
for example USD 2.77 per GJ for coal), indoor air pollution, human
health (diet-related health at USD 1,750 per person shifting),
congestion and road safety (IMF per-km values), water, land and
environmental pollution, and forest ecosystem services. Agricultural,
livestock and industrial output values and consumer savings are also
counted.

**Carbon** is not valued in the headline results, although the LAC
study's waste appendix values it at the social cost of carbon, an
inconsistency (Kalra et al. 2023).

Appendix A of the companion note on global investment needs lists the
unit factors and rates each against international evidence. The full
set is in 21 tables in the package's `docs/cost_factors` folder.

## Discounting

The module never discounts. It returns undiscounted annual flows, and
the present value is computed afterwards:

$$PV = \sum_{t = 2025}^{2050}{\sum_{k}^{}\frac{V_{k,t}}{(1 + r)^{\, t - t_{0}}}}\quad\quad(2)$$

The LAC study used $r = 7\%$, which it calls a "higher bound"; the Costa
Rica study used 5%. Neither is the World Bank's rule, which sets the
social rate between one and two times expected growth per person, 6% at
3% growth (World Bank 2016).

Power is treated differently. NemoMod chooses the least-cost capacity
mix and reports *discounted* capital and operating costs, and the
cost-benefit database maps power capex and opex directly onto those
series (`nemomod_entc_discounted_capital_investment_*` becomes
`cb:entc:technical_cost:electricity:capex`). NemoMod's documented default
rate is 5%, but the shipped configuration sets it to 0%. So, depending
on the run, power capital is discounted twice or once at a different
rate from every other line, and the rate also changes the capacity mix
NemoMod chooses. The rate used in the Uganda run is not recorded.
NemoMod's inputs for a technology-specific cost of capital
(`InterestRateTechnology`, `InterestRateStorage`) are stubbed, so a solar
farm in Zambia cannot be given a higher cost of capital than one in
Chile.

## What a run looks like

The October 2025 Uganda run is typical. Its `cba_results.csv` file has
37,540 rows: three strategies (net zero and two NDC variants), years
2019–2070, and 1,065 items. Costs are negative and benefits positive,
the opposite of the convention in the team's marginal-abatement-cost
file. About 3,900 rows are pre-2025 costs moved forward by cost
shifting. Table 2 summarises the main lines.

**Table 2. Uganda: main cost-benefit lines, 2025–2050 (USD billion,
2019 dollars presumed)**

| Line | Net zero | NDC 2.0 from 2020 | NDC 2.0 from 2025 |
|------------------------------|----------------:|----------------:|----------------:|
| Technical cost (undiscounted) | −258.8 | −196.8 | −159.3 |
| Human health | 177.5 | 103.2 | 78.9 |
| Consumer savings | 176.0 | 47.8 | 36.7 |
| Indoor air pollution | 18.8 | 136.0 | 57.6 |
| Crop value | 65.9 | 61.2 | 45.5 |
| Water pollution | 35.1 | 61.1 | 48.8 |
| System cost and technical savings | 94.7 | 5.2 | 3.8 |
| Fuel cost | 24.5 | 8.6 | 6.7 |
| Air pollution | 9.1 | 8.5 | 6.6 |
| **Net (undiscounted)** | **406.9** | **326.4** | **195.1** |
| Net present value at 6% (base 2025) | 161.4 | 184.6 | 89.8 |
| Net present value at 7% | 140.8 | 170.6 | 80.2 |

Lines do not add to the net, which includes smaller categories. The
present values are calculations for this note, not SISEPUEDE outputs.

Three features stand out. Technical cost runs at 1–4% of GDP a year
(net zero: 1.4% in 2030, 3.8% in 2050), which is large for any budget.
The benefits are mostly non-cash: health, sanitation, water pollution
and indoor air. Only the fuel, system-cost and technical-savings lines
are money that a budget, a utility or the balance of payments could
actually see: under a fifth of the benefits in the net-zero strategy and
under 5% in the NDC strategies. And the largest cost items
are wastewater treatment, efficient appliances, livestock management,
food waste and sanitation, not power: a budget view must therefore cover
the whole inventory, not only energy.

## How the results reach CPAT

The CPAT–CPM bridge links SISEPUEDE to CPAT, the World Bank–IMF carbon
pricing tool, on the principle that "prices, elasticities and money
cross between the models; tonnes of emissions never do". CPAT revenue
can be spent on SISEPUEDE transformations. Revenue $B_{j}$ assigned to
transformation $j$ buys doses:

$$u_{j} = \min\left( \frac{B_{j}}{c_{j}},\ u_{j}^{\max} \right)\quad\quad(3)$$

where $c_{j}$ is the module's cumulative technical cost per dose over
2022–2041. Each of CPAT's five uses of revenue may pay only for the cost
lines that belong to it: public investment for transformations that
leave an asset behind, current spending for programmes, transfers and
labour tax cuts for household costs, and corporate tax cuts for firm
costs. For Egypt, measures costing USD 17.2 billion need a carbon tax of
about USD 6.4 a tonne in 2040. CPAT's GDP effects come from fiscal
multipliers by instrument and lag (MFMod medians), and CPAT and
SISEPUEDE figures "are shown side by side and never added", because both
can value the same avoided fuel and pollution.

The bridge already sorts costs by who would pay them, but only
qualitatively, and its own documents state the gap: "The cost module
prices the resource cost of a transformation, not who disburses it…
Splitting each lever's cost between state, household and firm is what
this mapping needs and what neither model holds today." The 13 October
2026 scoping meeting left the same question open: "Separate running
subsidies from upfront public investment, show how a carbon tax reduces
each, and report dollars as well as marginal costs." The FY27 work plan
names the answer as its version 3: "efficiency of public investment and
energy fiscal costs and risks for finance ministries". The upgrades in
this note are that version.

# Evaluation

**How each feature is rated.** Table 3 sets each feature of SISEPUEDE's
cost-benefit method beside current good practice: the World Bank's
economic-analysis guidance (the "three questions", the 2016 discounting
note and the 2024 shadow price of carbon), the public-finance literature
on the cost and value of public funds, and IMF and World Bank practice on
public investment management (Appendices B and C). **G** (good): it
matches. **M** (medium): it is right in principle but off in one
respect. **P** (poor): it is missing or inconsistent.

**Table 3. SISEPUEDE's cost-benefit method against good practice**

| Feature | SISEPUEDE today | Good practice | Fit | Upgrade (step) |
|----------------------|------------------------------|------------------------------|------------------------------|------------------------------|
| Counterfactual | Strategy minus baseline, item by item | Measure against what would happen anyway | G | Keep; add private counterfactual (4) |
| Wider benefits | Health, pollution, congestion, crashes, ecosystems | Count non-market benefits at willingness to pay | G | Keep; never pass to GDP (11) |
| Uncertainty | About 1,000 futures; scenario discovery | Robust decision-making; switching values | G | Add discount rate and cost of capital to the futures (10) |
| Interactions | Rescaling weights | Measures interact; check in combination | M: weights do not match runs (heat pumps with insulation) | Family exclusivity; leave-one-out check (10) |
| Carbon | Excluded from headline; used in waste appendix | World Bank shadow price as a separate line | M: inconsistent | Carbon switch and memo line (2) |
| Unit factors | 2019 USD, LAC average, mostly US sources | Local prices and costs | M: one scaling for all countries | Harmonise prices and currency (Phase 0) |
| Sectors | IPCC sectors only | All competing uses of public money | M: climate only | Sector cards (10) |
| Discounting | None in module; 7% or 5% afterwards | One social rate, 6% (World Bank 2016) | P: ad hoc | Discount once at 6% (2) |
| Power capital | Pre-discounted by NemoMod at 0% or 5% | Discount once | P: discounted twice or inconsistently | Re-derive from capacity × unit cost (2) |
| Capital | Mixed into technical cost; straight-line in places | Gross capital shown; annualised at a rate | P: capital charge understated 40–120% at 6–15% | Capital share, asset life, capital recovery factor (1, 7) |
| Recurrent costs | Inside technical cost where present | Funded O&M and staffing per dollar of capital | P | Recurrent coefficients; maintenance first (7) |
| Payer | None | Who pays: state, utility, firm, household | P | Payer and financing-type tags (1) |
| Fiscal flows | None: no taxes, subsidies, fees | Fiscal impact reported with economic value | P | Fiscal ledger (5) |
| Cost of public funds | Not applied (λ = 1) | λ above 1 where taxes distort | P | MVPF against λ (6) |
| Revenue returns | Not modelled | Transfers in welfare; worth λ to the budget | P | Revenue rules (9) |
| Delivery | Every dollar becomes an asset on time | Efficiency, execution and overrun adjustments | P | Delivery haircuts (3) |
| Financing | One rate; no cost of capital; no contracts | Country and technology cost of capital; liabilities | P | Financing routes (8) |
| Macro feedback | None; GDP exogenous | Link to macro-fiscal and debt models | P | Macro bridge (11) |

**What this means.** SISEPUEDE is strong on what it was built for:
counting the physical and social effects of a transformation against a
baseline, across many futures. Its weaknesses are all on the money
side, and they share one cause: the module values resources for the
economy as a whole, with no owner, no financing and no budget. Three
consequences matter most.

- **The cost of capital is missing exactly where it bites.** At a 0%
  NemoMod rate and with straight-line unit factors, capital-intensive
  measures look cheaper than they are. At 6% the capital charge on a
  12-year asset is 1.43 times the straight-line charge; at 15% it is
  2.21 times. That is a bias in favour of renewables and electric
  vehicles in high-risk countries, not a neutral error.
- **The budget is invisible.** A transformation with a large net benefit
  can still need a large public outlay, return nothing to the budget and
  raise debt. Neither SISEPUEDE nor the bridge can say so today.
- **Ranking across uses of public money is impossible.** Without a
  public-funds test, other sectors or delivery losses, SISEPUEDE can
  rank climate strategies against each other, which is what it was
  designed for, but not against the alternatives a finance ministry
  faces.

The upgrades keep SISEPUEDE as it is and add these elements outside it.
That respects the partnership's division of labour and the contract's
end date, and it means every upgrade can be tested by reproducing
SISEPUEDE's own results when the new parameters are switched off.


# The upgrades: a Public Spending Value layer

## The idea

For every candidate use of public money (a *measure*), the Public
Spending Value (PSV) layer computes what society gets per dollar of
*net* public money. A measure can be a SISEPUEDE transformation, an NMIM
investment line, or a programme from a non-climate *sector card*. The
value is computed after three corrections: what the private sector would
have done anyway, how much spending turns into working assets or
services, and the money the measure brings back to the budget. The layer
then ranks the measures, picks a portfolio within the fiscal envelope
that the macro and debt models say is affordable, and passes the chosen
programme back to those models.

In one sentence, the upgrade to World Bank practice is: **economic
analysis, plus a fiscal ledger, plus λ**. It is the MVPF logic of
Hendren and Sprung-Keyser (2020) applied to a World Bank economic
analysis, with the Bank's and the IMF's own efficiency diagnostics
(PIMA, PEFA, BOOST and Herrera's frontier scores) as haircuts. Appendix B
sets out the literature behind each element.

**The decision metric.** Let $W_{j}$ be the present value of benefits to
everyone other than the budget, net of their own costs (willingness to
pay, counting any fees they pay as a cost), and $F_{j}$ the present
value of the net cost to the budget. Then:

$$ENPV_{j} = W_{j} - F_{j},\qquad MVPF_{j} = \frac{W_{j}}{F_{j}},\qquad NB_{\lambda,j} = W_{j} - \lambda F_{j}\quad\quad(4)$$

Fund measure $j$ if $MVPF_{j} > \lambda$, which is the same as
$NB_{\lambda,j} > 0$. If $F_{j} \leq 0$ the measure "pays for itself";
fund it if $W_{j} \geq 0$, because the binding issue is then financing,
not value. When the budget binds, rank by MVPF. With $\lambda = 1$ and no
budget limit, $NB = ENPV$: the World Bank's rule. In cash-short years
$\lambda_{t}$ can be set higher than $\lambda$, which is how the layer
sees a liquidity trap (step 6).

## Where it sits

The layer is a Python module (`psv.py`) with a workbook in CPAT layout,
sitting between the models the team already has.

**Table 4. Inputs, steps and outputs of the PSV layer**

| Inputs | Steps in the layer | Outputs |
|------------------------------|------------------------------|------------------------------|
| SISEPUEDE `cba_results.csv`; NMIM lines for 186 countries; sector cards | 1. Tag every flow | Measures tagged by payer, nature, NMIM type and budget function |
| World Bank discounting and carbon notes | 2. Discount once | Economic NPV, with and without carbon |
| PEFA PI-11 or PIMA; BOOST execution rates; Herrera frontier scores | 3. Delivery haircuts | Effective assets per dollar; delayed benefits |
| Private cost of capital; CPAT carbon price and subsidy reform | 4. Additionality and the price test | Public money needed; "price first" flags |
| Fees, fuel-subsidy savings, excise | 5. Fiscal ledger | Fiscal NPV, cash profile, payback |
| λ by country | 6. Decision metric | W, F, MVPF, NB_λ |
| Recurrent-cost coefficients; BOOST O&M | 7. Capital and current | Equivalent annual cost; maintenance-gap measure |
| Loan, concessional, PPA and guarantee terms | 8. Financing routes | Debt added, contract liabilities |
| Revenue capture shares | 9. Revenue returns | MVPF with returns in the denominator |
| Fiscal envelope from the macro and debt models | 10. Allocative frontier | Funded set, cut-off MVPF, reallocation gain |
| GIMF-, DIGNAD- and DIGNAR-lite; LIC-DSF-lite | 11. Macro bridge | Debt path, rating, GDP path, envelope and λ fed back |

## Step 1: tag every flow

Each SISEPUEDE line gets four tags:

- **payer or receiver:** budget, state-owned enterprise or utility,
  private firm, households, rest of the world;
- **economic nature:** capital, operations and maintenance, wages or
  other recurrent cost, transfer or subsidy, fuel, revenue;
- **NMIM financing type** (Table D2): P1 pure public, P2 regulated
  utility, P3 contracted revenue (PPAs, concessions), P4 viability gap,
  P5 pure private; NMIM's rules are the defaults, overridden by CCDR
  plans where they exist;
- **budget function** (COFOG), so the layer can be compared with BOOST.

The tags come from a lookup on the category field and a *fiscal
attribute table* keyed on the transformation code, which holds each
transformation's capital share, asset life, payer shares,
revenue-capture potential and budget line. Table 5 gives the proposed
default mapping, to be agreed with the SISEPUEDE team in Phase 0. It
turns the bridge's qualitative rule (public investment pays for
transformations that leave an asset; current spending for programmes;
households and firms for their own equipment) into numbers.

**Table 5. Default mapping of SISEPUEDE categories to payers and uses**

| SISEPUEDE category | Nature | Default payer | Use in the layer |
|-----------------------------------|------------------------------|------------------------------|------------------------------|
| `technical_cost` on asset-leaving transformations (power, wastewater, sanitation, solid waste, rail) | Capital plus O&M, split by capital share | By NMIM type: P1 budget, P2 utility, P3 private producer, P5 firms | Cost; capital share and asset life from the attribute table |
| `technical_cost` on household equipment (appliances, building shell, light vehicles) | Capital | Households (P5); budget only if subsidised | Cost to households; any subsidy to the ledger |
| `technical_cost` on programmes (livestock, crops, land use, diets) | Recurrent | Budget (current spending) or producers | Current spending, as in NMIM's split |
| `system_cost`, `technical_savings` | O&M, fuel | Owner of the system | Resource saving; budget share via θ |
| `fuel_cost`, `sector_specific:fuel_cost` | Fuel | Whoever bears fuel costs (θ) | Import bill; fiscal capture θ; energy savings to the macro model |
| `consumer_savings` | Saving | Households | W |
| Health, air, indoor air, road safety, congestion, water, land, environmental pollution, ecosystem services | Non-market benefit | Households, society | W only; never passed to GDP |
| `crop_value`, `lvst_value`, `ippu_value` | Market output | Firms, farmers | W; counts toward the sector return passed to the macro model |

## Step 2: discount once

All flows are discounted once, in the layer, at the World Bank social
rate:

$$ENPV_{j} = \sum_{t}^{}\frac{B_{j,t} - C_{j,t}}{(1 + r)^{t}} + s_{c}\sum_{t}^{}\frac{SPC_{t}\,\Delta E_{j,t}}{(1 + r)^{t}}\quad\quad(5)$$

where $r$ is 6% by default (3% and 10% as sensitivities), $SPC_{t}$ is
the World Bank shadow price of carbon (USD 40–80 a tonne in 2020,
50–100 in 2030, in 2017 dollars, rising 2.25% a year; World Bank 2024),
$\Delta E_{j,t}$ the avoided emissions and $s_{c}$ a switch, with the
carbon value always reported as a memo line. Power capital is
re-derived as capacity added times unit capital cost; the
`nemomod_*_discounted_*` series are never discounted again.

**The first regression test.** With λ = 1 and no haircuts, the layer
must reproduce the team's investment-needs model. For an NMIM line with
constant savings and co-benefits per dollar of capital over an asset
life $n$, the economic NPV times the capital recovery factor equals that
model's lens (c) result exactly: $ENPV_{j}\, CRF(6\%, n) = -IC_{j}$.

## Step 3: delivery haircuts

Public capital faces three separate effects, and the layer keeps them
apart:

- **Investment efficiency** $s_{j}$, the share of spending that becomes
  effective capital, from PIMA or from PEFA PI-11 (a score of 1 implies
  a 40% gap, 4 a 13% gap), otherwise from the IMF's estimates by income
  group (0.60, 0.73 and 0.87 for low-income, emerging and advanced
  economies; IMF 2015). It raises the cost of a unit of asset on the
  public share $\pi_{j}$ only.
- **Execution** $e_{j}$, the share of the budget actually spent, from
  BOOST. It delays benefits; it does not lose money, because unspent
  appropriations stay in the budget.
- **Optimism bias**: cost and time uplifts by project type (HM Treasury
  guidance), used only where no country data on public investment
  management exist.

$$C_{j}^{eff} = C_{j}\left\lbrack (1 - \pi_{j}) + \frac{\pi_{j}}{s_{j}} \right\rbrack,\qquad K_{j,t}^{eff} = (1 - \delta_{j})K_{j,t - 1}^{eff} + s_{j}\, e_{j}\left( I_{j,t}^{plan} + \text{backlog}_{j,t - 1} \right)\quad\quad(6)$$

For services such as health and education, frontier output-efficiency
scores $\varphi_{j}$ scale outcomes per dollar when unit costs come from
international norms (DCP3, "Smart Buys"); $\varphi_{j} = 1$ when unit
costs come from the country's own outturns, which already embed its
inefficiency.

**One convention: money in, assets out.** The layer budgets in money. A
public outlay $G_{j}$ buys effective assets $s_{j}G_{j}$, so the cost per
unit of asset is $c_{j}/s_{j}$. The bridge passes the outlay $G_{j}$ with
$s_{j}$ to the macro model, which accumulates the same $s_{j}G_{j}$. The
waste $(1 - s_{j})G_{j}$ is already inside $G_{j}$: it is never passed
again as extra spending, and $s$ is applied once. Whether a low
efficiency also lowers the return per effective dollar is contested
(Berg et al. 2019); holding the return per effective asset fixed is the
default and holding the output elasticity fixed is a sensitivity.

**Reform as a measure.** Stronger public investment management could
close up to two-thirds of the efficiency gap (IMF 2015). The layer
treats that as a measure in its own right: its value is the extra
effective capital on the whole programme, and its cost is the reform
programme, a parameter for which no source was found.

## Step 4: additionality and the price test

The private investor's NPV is computed at the market cost of capital and
private prices, including taxes. Public money pays only the gap:

$$G_{j} = \begin{cases} \text{full cost} & \text{P1, pure public} \\ \max\left( 0,\ -NPV_{j}^{priv} \right) & \text{P4, viability gap} \\ 0 \text{ up front; contingent only (step 8)} & \text{P2, P3, utility or contract} \\ 0 & \text{P5, pure private} \end{cases}\qquad B_{j}^{net} = a_{j}\, B_{j}^{gross}\quad\quad(7)$$

where $a_{j}$ is the additionality share. The viability-gap rule replaces
NMIM's flat 30% wherever the private NPV can be computed.

**The price test.** Could a carbon tax or fuel-subsidy reform from CPAT,
or a regulation, deliver the outcome at lower cost to the budget? If so,
the measure is flagged "price first". The literature gives the reason:
with costly public funds the best subsidy is below the gap between
social and private returns, and further below when most of the
subsidised units would have happened anyway, whereas a tax raises money
on those units instead of paying for them (equation B3 in Appendix B).

## Step 5: the fiscal ledger

Net budget flows are recorded by year:

$$F_{t} = \text{capex}_{t} - \text{loans}_{t} + DS_{t} + OM_{t}^{pub} + PPA_{t} + SUB_{t} - FEE_{t} - \theta\, SAV_{t} + XL_{t} - PIG_{t} + E\left\lbrack CALL_{t} \right\rbrack\quad\quad(8)$$

where $DS$ is debt service, $OM^{pub}$ public operations and maintenance,
$PPA$ contract payments, $SUB$ subsidies or viability-gap payments,
$FEE$ user fees and tariffs, $SAV$ avoided fuel costs of which the
budget or state utility keeps a share $\theta$, $XL$ fuel excise lost,
$PIG$ carbon or other corrective revenue earmarked to the measure, and
$E[CALL]$ expected calls on guarantees. The fiscal NPV is
$FNPV_{j} = -\sum_{t}F_{t}/(1 + i_{g})^{t}$ at the government's
borrowing rate $i_{g}$, and also at the concessional rate. The layer
reports the equivalent annual fiscal cost, the payback year and a
self-financing flag. Tax revenue induced by faster growth is left to the
macro model; only direct, contractual or near-mechanical effects enter
the ledger.

## Step 6: the decision metric

The layer computes equation (4) for every measure. λ defaults to **1.2**,
the average for 38 African countries (Auriol and Warlters 2012) and
Norway's official convention, and to 1.1 where the marginal tax is VAT.
A stress value of 1.5–2.0 applies where the macro and debt models show
that the country cannot borrow more. In cash-short years a
time-varying $\lambda_{t}$ applies:
$NB^{liq} = W - \sum_{t}\lambda_{t}F_{t}/(1 + r)^{t}$.

When the financiers are non-resident, $W - F$ is the *national*
economic NPV: the World Bank's financing-neutral ENPV minus a financing
premium, positive for an 8% loan or an 11% PPA and negative for a
concessional loan. With resident financiers the two coincide; the
worked example checks this. Optional distributional weights,
$w_{i} = (y_{ref}/y_{i})^{\eta}$ with $\eta = 1.3$, can use CPAT's
household data.

## Step 7: capital and current on one footing

Each capital outlay is turned into an equivalent annual cost and its
recurrent costs are added:

$$CRF(r,n) = \frac{r}{1 - (1 + r)^{- n}},\qquad EAC_{j} = K_{j}\, CRF(r, n_{j}) + r_{j}^{rc}K_{j}\quad\quad(9)$$

where $r$ is the social rate for the economic view, the government rate
for the fiscal view and the market cost of capital for private and PPA
routes, and $r^{rc}$ is the recurrent-cost coefficient (operations,
maintenance and staffing per dollar of capital a year). Current
programmes enter at their annual cost. Capital and current measures are
then compared on equivalent annual fiscal cost and on MVPF.

The end-of-year factor is the house convention, because debt service is
paid in arrears. CPAT's power model uses an annuity-due factor, which
makes its annual capital charge 8–11% lower at rates of 8–11%; the two
should be reconciled.

**Maintenance first.** From BOOST, the maintenance gap in sector $s$ is
the required spending less what is spent,
$r_{s}^{rc}K_{s,t} - OM_{s,t}^{exec}$. Closing it is a measure: its
fiscal cost is the gap, and its value is the rehabilitation it avoids,
three to five times the gap for roads (Harral and Faiz 1988), or the
more than 50% life-cycle saving reported in *Beyond the Gap* (Rozenberg
and Fay 2019). It enters every portfolio before new building of the same
asset class.

Recurrent-cost coefficients are the weakest parameters: 1–2% of capital
a year for solar, 2–3% for batteries, single digits for roads and
networks, and above 10–20% for health and education facilities because
of staffing (the last two †).

## Step 8: financing routes

Each measure can be run under six routes (Table 6).

**Table 6. Financing routes**

| Route | Payment stream | Headline debt | Debt-like or contingent liability |
|------------------------------|------------------------------|--------------------------|------------------------------|
| Budget, commercial loan (rate $i$, tenor $n$) | Debt service $K\,CRF(i,n)$ | +K on day one | The debt |
| Budget, concessional loan (IDA- or RST-type) | Interest during grace, then an annuity | +K on day one | Grant element $1 - PV(DS)/K$ |
| Utility on its balance sheet (P2) | Tariffs; utility debt service | Outside central government | Utility debt, as a contingent liability |
| Private producer with a PPA (P3), with or without a guarantee | Tariff × energy each year | 0 | Present value of committed payments; guarantee exposure |
| Viability-gap contract for difference (P4) | Top-up per unit | 0 | Present value of expected top-ups |
| Grant or climate finance | None | 0 | Opportunity cost at the budget's shadow price |

For a PPA, the tariff and the liability are:

$$T = \frac{\left( K + PV(\text{replacements}) \right)CRF(WACC, n) + OM}{E},\qquad L^{PPA} = \sum_{t}^{}\frac{P_{t}^{committed}}{(1 + i_{g})^{t}}\quad\quad(10)$$

The financing premium over public borrowing is $L^{PPA} - K$. The
liability is passed to LIC-DSF-lite. The DSA stress test also applies:
when the PPP capital stock exceeds 3% of GDP, 35% of it is added to
public debt (IMF and World Bank 2017). A guarantee is modelled as a
lower cost of capital (by an assumed 2–2.5 points) plus an exposure
equal to the guaranteed amount times the probability of a call. Every
PPA route must meet five guardrails: a competitive auction, sizing to
expected dispatch, a tariff ceiling below the avoided cost, matching
currencies, and entry in a register of contracts (PEFA PI-10.3).

## Step 9: revenue returns

Seven rules govern money that comes back:

1. In the economic NPV, fees and taxes are transfers and are left out,
   apart from real resource effects.
2. In the fiscal ledger they are counted.
3. They raise the MVPF through the denominator: each dollar recovered
   saves λ, not 1. A fee is never also added as a benefit, because
   users' willingness to pay already includes it.
4. The share recovered feeds the user-fee parameter of the DIG-family
   models.
5. Tax from faster growth is left to the macro model.
6. Corrective revenue, such as a carbon tax or subsidy reform from CPAT,
   is a measure in its own right on the same scale. It has a low
   welfare cost per dollar raised, so it is the natural first source of
   funds.
7. Spending and revenue-recycling options therefore compete on one MVPF
   ladder, which links CPAT's pricing to the spending side.

## Step 10: the allocative frontier and other sectors

**Sector cards.** Each card is one row: measure, unit cost, outcome per
dollar, money value of the outcome, efficiency source, recurrent
coefficient, payer type, fiscal externality, benchmark range, source and
confidence. Defaults come by benefit transfer and are replaced by
country CBAs when available. All cards share the same conversion
factors (social discount rate, value of a statistical life, value of a
learning-adjusted year of schooling, shadow price of carbon, λ), so no
measure gets a cheaper life than another. SISEPUEDE's transformations
are the energy and climate card. Table 7 gives the starting set.

**Table 7. Sector cards**

| Card | Unit cost and outcome | Money value | Efficiency source | Recurrent cost; payer | Fiscal externality | Benchmark | Confidence |
|----------------------|-------------------------|-------------------------|----------------------|----------------------|-----------------------|--------------------|--------------------|
| Health (DCP3 packages) | Essential package USD 79 per person (low income), USD 130 (lower-middle); DALYs averted | Deaths × value of a statistical life, transferred with income elasticity 1.5 | Frontier scores (health about 0.9) | High, staffing †; P1 | Labour supply and tax; small in low-income countries | Copenhagen Consensus at 8%: TB 46, maternal and newborn 87 | Medium-low |
| Education | Learning-adjusted years per USD 100: best about 3, many about 0 | Present value of a 9% earnings gain per year | Frontier scores (education about 0.8) | Wage-dominated †; P1 | Future tax on earnings | Not confirmed | Medium-low |
| Social protection | Cash transfer per dollar | MVPF about 1 (the cash benchmark); Mauritius unemployment insurance 1.23 | Administrative cost share | Low; P1 | Local tax revenue; means-test disincentives | MVPF 1; Kenyan local multiplier 2.5 goes to the macro layer only | Medium |
| Roads | Maintenance versus new works (HDM-4, RONET) | Avoided rehabilitation (3–5 times); vehicle operating cost and time | PIE-X efficiency | Single-digit % †; P1 | Fuel tax on traffic | Roads top per-rupee returns in rural India | Medium for maintenance |
| Water and sanitation | Coverage cost | Health and time saved | PIE-X; OECD water efficiency | Utility O&M; P1 or P2 | Tariffs | Sanitation 5.5, water 2.0 (global) | Medium |
| Resilience | Resilient-design premium (25% in DIGNAD-lite) | Avoided losses and disruption | PIE-X | As the asset; P1 | Avoided reconstruction; tax revenue | *Lifelines* median about 4; 2–10 | Medium |
| Agriculture | Research and extension versus input subsidies | Productivity value | Sector frontier | Low to medium; P1 | Small | Research about 60% average return; subsidies rank low | Medium |
| Energy and climate | SISEPUEDE transformations; NMIM lines | `cba_results.csv` categories; carbon switch | PIMA or PEFA; BOOST | By NMIM type | Fuel-subsidy savings; excise lost; carbon revenue | Costa Rica package about 2.1; island case below | Medium |

The benchmarks are sanity checks for computed values, not inputs; they
come from different discount rates and scopes (Appendix B.10).

**The frontier.** It is built in five moves:

1. **Within families.** Variants of one transformation (low, middle and
   high ambition) are mutually exclusive; incremental analysis keeps
   only the efficient ones.
2. **Rank and add up.** Measures are ranked by MVPF and cumulative
   present-value fiscal cost is plotted against cumulative value.
3. **The envelope.** The fiscal envelope $E_{t}^{*}$ comes from the macro
   and debt models: the largest programme for which the fiscal rule
   stabilises debt and the DSA rating does not worsen.
4. **Lumpy projects.** Indivisible projects need a knapsack (equation
   11 below).
5. **Risk.** SISEPUEDE's futures give the expected net benefit, the 10th
   percentile, the maximum regret and the share of futures in which the
   MVPF exceeds λ. Interactions are checked with the team's
   measure-alone and leave-one-out runs.

Equation 11 picks the portfolio:

$$\max_{x}\sum_{j}^{}x_{j}NB_{\lambda,j}\quad\text{s.t.}\quad\sum_{j}^{}x_{j}F_{j,t} \leq E_{t}^{*}\ \forall t;\quad\sum_{j \in g}^{}x_{j} \leq 1\ \forall g;\quad\sum_{j}^{}x_{j}I_{j,t} - I_{t - 1} \leq \Delta I^{\max};\quad\sum_{j}^{}x_{j}A_{j} \geq \text{target}\quad\quad(11)$$

where $x_{j}$ is 1 if measure $j$ is funded (or a share, for divisible
measures), $g$ indexes families of exclusive variants, $\Delta I^{\max}$
caps the speed of scale-up and $A_{j}$ is abatement. Floors protect
wages, pensions, interest and legal mandates.

Comparing the frontier with the current allocation in BOOST gives the
**reallocation gain** at the same budget, which is the bridge to Public
Finance Review practice. The cut-off MVPF is a diagnostic: well above λ
means the envelope is too small; below λ means it is too large.

## Step 11: the bridge to the macro-fiscal models

A small `psv_bridge.py`, parallel to the existing `nmim_bridge.py`,
passes yearly paths as shares of GDP and receives the macro and debt
results (Table 8).

**Table 8. What the bridge passes**

| From the layer | GIMF-lite | DIGNAD- or DIGNAR-lite | LIC-DSF-lite |
|------------------------------|-------------------|----------------------|----------------------------|
| Public capital by sector (outlay) | `ig_extra` | `prog` | Through the deficit |
| Efficiency (weighted) | `s` | `s` | |
| Return on capital, market-output benefits only | `Rg` | `Rg` | |
| Adaptation share | | `prog_bbb` | |
| Current spending | `g_extra` | `prog_spend` | |
| Energy savings | `sav` | `sav` (new channel) | |
| Fees and earmarked revenue | `rev_extra` | `rev` | |
| Financing shares | `dfs` | `sh_grant`, `sh_conc` | Loan terms |
| Contract liabilities, utility debt, guarantees | | | Contingent-liability shock |
| Execution delay, absorptive capacity | Spending path | `prog` path; cost curve | |

The bridge returns the debt path, the DSA rating, the fiscal envelope
and the GDP path, which feed λ and the envelope back into steps 6 and
10. The return passed as `Rg` counts only market-output benefits
(productivity, firms' and workers' time) per unit of effective capital.
Energy savings passed as `sav` are excluded from it, and non-market
benefits such as health never enter GDP. One iteration is normally
enough; the check is that the funded set does not change on a second
pass and λ moves by less than 0.05. Appendix D describes the macro
models and the known issues the bridge resolves.

## Low-capacity settings

In low-capacity countries the layer:

- uses a higher λ where informality is high, and a higher $\lambda_{t}$
  in cash-short years;
- applies efficiency haircuts to the public share of capital (from PIMA
  or PEFA PI-11), and never also to unit costs taken from local
  outturns;
- treats low BOOST execution as delay, not loss;
- funds maintenance first;
- prefers simple, standard, auctioned instruments, such as solar
  auctions with guarantees;
- makes complex programmes beat a cash transfer (an MVPF of about 1)
  after haircuts;
- caps the speed of scale-up and phases large programmes;
- requires a register of PPPs and PPAs before any contract route is
  scored.

## Key parameters

**Table 9. Core parameters of the layer**

The last column rates confidence in the default.

| Parameter | Symbol | Default | Range | Source | Confidence |
|--------------------------|---------------------|--------------------------|--------------------------|--------------------------|----------------------|
| Social discount rate | $r$ | 6% | 3%, 10% | World Bank 2016 | High, as Bank practice |
| Marginal cost of public funds | λ | 1.2 (1.1 if VAT-financed) | 1.0–1.5; stress 2.0; higher in cash-short years | Auriol and Warlters 2012; Norway | Medium |
| Shadow price of carbon | $SPC_{t}$ | USD 40/80 (2020) to 50/100 (2030), +2.25% a year, 2017 dollars | Low for low income, high for middle income | World Bank 2024 | High, as Bank practice |
| Government borrowing rate | $i_{g}$ | Private-creditor rate less 3 points, bounded 3–8% | 6–11% for small islands † | Team's calibration | Low-medium |
| Investment efficiency | $s_{j}$ | From PEFA PI-11, or 0.60 / 0.73 / 0.87 by income group | ±0.15; DIG uses 0.35–0.6 | IMF 2015; Berg et al. 2013 | Medium |
| Execution rate | $e_{j}$ | BOOST capital execution | By country | BOOST | Medium |
| Optimism bias | | HM Treasury upper bounds, only without country data | Lower bounds with evidence | HM Treasury | Medium |
| Service output efficiency | $\varphi_{j}$ | Country frontier scores; else health 0.9, education 0.8 | Bootstrap interval | Herrera and Pang 2005 † | Low-medium |
| Additionality | $a_{j}$ | 1 for public goods; 0.5–0.9 for subsidies | 0–1 | Assumption | Low |
| Fiscal capture of savings | θ | 0.5; 1 if the budget covers utility losses | 0–1 | Policy parameter | n.a. |
| User-fee recovery | $f_{j}$ | 0.5 of recurrent cost | 0–1 | Guinea DIG application | Low |
| Recurrent coefficient | $r^{rc}$ | By asset class (step 7) | Wide | Assumptions; Hood et al. 2002 † | Low |
| Asset life | $n_{j}$ | Generation, buildings, industry 25; grids 40; vehicles 12 years | ±5 years | NMIM | Medium |
| Private cost of capital; guarantee effect | WACC; $\Delta_{g}$ | Country WACC; 11% for small islands; guarantee 2–2.5 points | 7–13% | IEA; assumption | Low-medium |
| Concessional terms | | 1.5%, 30 years, 5 years' grace | 0.75–2% | Illustrative; IDA terms † | Low-medium |
| Absorptive capacity | $\Delta I^{\max}$ | Unit costs rise above about 10% of GDP of public investment (7% where efficiency is low) | | IMF 2020 † | Low |
| Distributional weights | η | Off; 1.3 when on | 0.8, 2.0 | UK Green Book | Medium |
| Value of a statistical life | | US value × (income ratio)^1.5; about 160 times income per person | Elasticity 1.0 | Robinson, Hammitt and O'Keeffe 2019 | Medium |
| DSA stress for PPPs | | 35% of PPP stock if above 3% of GDP | Under 2026 review | IMF and World Bank 2017 | High, as current rule |

Appendix I adds the macro-model defaults and reference capital recovery
factors.

## Outputs

For each measure the layer reports:

- **tags:** payer, nature, financing type, budget function, card;
- **value:** economic NPV with and without carbon; W, F and MVPF, with a
  "pays for itself" flag; $NB_{\lambda}$ at 1.2, at the stress value and
  with the liquidity profile;
- **fiscal profile:** fiscal NPV at the government and concessional
  rates; equivalent annual fiscal cost; the cash profile, payback year
  and self-financing flag;
- **switching values:** the λ, θ and efficiency at which the decision
  flips, and the fuel price at which a plant pays for itself;
- **liabilities:** headline debt added, contract present values, the DSA
  stress add-on, and net fiscal and external liabilities.

For the portfolio it reports the frontier and funded set, the cut-off
MVPF, the reallocation gain against BOOST, the robustness statistics,
and the macro and debt paths returned by the bridge.


# The upgrades at work: a small island escaping the oil trap

SISEPUEDE has not been run for a small island state, and its method
would judge an island solar plant on its economic NPV alone. This
example shows what the upgrades add. It applies steps 5–9 to one
illustrative plant with the script `sids_worked_example.py`, which
checks its own identities: the capital recovery factors, that loan
payments discounted at the loan rate equal the principal, that
$ENPV = W - F$ on every route, that financing is neutral when the
financiers are resident, that the ENPV does not change with θ, and that
$NB$ at λ = 1 equals the ENPV. Money is in USD million at constant
prices. Appendix E gives every assumption and result.

**The island and the plant.** The island uses 300 GWh a year, almost all
from diesel. GDP is USD 2 billion; public debt is 85% of GDP, at high
risk of distress; the only market loans have short tenors. The plant is
60 MW of solar with a 120 MWh battery. It costs USD 120 million (6% of
GDP), displaces 30% of diesel generation, and avoids USD 0.228 a kWh, or
USD 20.5 million a year at Brent USD 80 a barrel. Its levelised cost is
USD 0.134 a kWh at 6%. Before financing, its economic NPV is
USD 108 million, and it stays positive down to Brent at about USD 22.

**Table 10. Results by financing route (USD million, present value at
6%; Brent USD 80; the budget keeps half the fuel savings)**

| Route | ENPV | W | F | MVPF | NB at λ = 1.2 | NB, cash-short years | Payment, year 1 | Debt added (% of GDP) | Contract value / capex |
|------------------------|-----------:|----------:|----------:|--------------:|------------:|-----------------:|---------------:|---------------:|---------------:|
| R1a Commercial loan, 8%, 7 years | 100 | 131 | 31 | 4.18 | 93 | 28 | 24.8 | 6.0 | |
| R1b Commercial loan, 8%, 25 years (not on offer) | 85 | 131 | 46 | 2.82 | 75 | 63 | 13.0 | 6.0 | |
| R2 Concessional loan, 1.5%, 30 years | 165 | 131 | −34 | Pays for itself | 172 | 197 | 3.6 | 6.0 | |
| R3 PPA, 11% cost of capital, no guarantee | 49 | 131 | 82 | 1.59 | 32 | 3 | 16.7 | 0 | 1.48 |
| R4 PPA, 8.5%, World Bank or MIGA guarantee | 80 | 131 | 51 | 2.55 | 69 | 51 | 14.2 | 0 | 1.27 |

ENPV is the island's economic NPV, net of the financing premium paid to
foreign lenders or investors. "NB, cash-short years" sets λ to 2.0 in years 1–7 and 1.2 after. Carbon
at the World Bank's low shadow price adds USD 47 million to every route.

**What the upgrades reveal.**

- **The trap is about cash and debt statistics, not value.** With the
  only loan on offer, payments of USD 24.8 million a year exceed the
  USD 20.5 million fuel saving; even if the budget kept all the savings
  it would run a deficit of USD 4.4 million a year for seven years.
  Headline debt rises from 85% to 91% of GDP on day one. Liquidity
  (tenor), solvency (fiscal NPV) and the debt stock are three separate
  constraints with different fixes. SISEPUEDE's economic NPV sees none
  of them.
- **One constant λ cannot see the trap.** The 7- and 25-year loans have
  the same fiscal NPV at 8% (−USD 38 million), and at a constant λ the
  short loan even looks better, because the 2-point spread over the
  social rate is paid for less time. Only the cash-short λ reverses the
  ranking (28 against 63). The tool needs that profile next to the
  standard metric.
- **Concessional finance wins on every count, where it exists.** It has
  a 48% grant element, positive cash from year one and a positive fiscal
  NPV. It still adds 6% of GDP to headline debt.
- **A PPA turns capital into a running cost below the fuel bill, but
  moves the liability rather than removing it.** The guaranteed PPA
  costs only about USD 5 million more than sovereign borrowing at 8% and
  adds no headline debt. The unguaranteed one costs about USD 31 million
  more, halves the island's NPV, and fails at λ = 2.0, at Brent USD 60
  and with capital costs 30% higher. Either way the contract's payments
  are worth 1.27–1.48 times the plant, and the DSA stress test adds 2.1%
  of GDP.
- **The revenue return drives the MVPF, not the ENPV.** Moving θ, the
  share of fuel savings the budget keeps, from 0 to 0.5 shifts value
  from consumers to the budget one for one and raises $NB_{\lambda}$ by
  about USD 26 million on every route. At θ = 0 the plant is a
  budget-financed consumer subsidy. Tariff design is a fiscal lever
  worth λ − 1 per dollar.

# Tool upgrade plan

The plan follows the house style of the team's other tools: a method
note that describes the current method only, separate version notes, a
caveats entry for each completed task, a workbook in CPAT layout
alongside the Python, and ticks on the macro tool's TODO list as items
are delivered. File names are proposals. The calendar is set against the
FY27 plan: the SISEPUEDE integration window is 4–29 January 2027 and
the Tec de Monterrey contract ends on 20 March 2027, so the pieces that
need the SISEPUEDE team come first.

**Table 11. Phases**

| Phase | Duration (indicative) | Main deliverables | Macro-tool TODO items closed |
|------------------------------|------------------------------|------------------------------|----------------------------|
| 0. Specification and data audit | 2–3 weeks (late October to mid-November 2026) | Method note; category map (Table 5); fiscal attribute table; parameter sheet; discounting fix; pilot data audit | None (enables 1, 2, 8, 9) |
| 1. Core layer | 4–6 weeks (to late December 2026) | `psv.py` for steps 1–7 and 9; workbook; tests; runs on NMIM and the Uganda SISEPUEDE output | 8 (in part) |
| 2. Financing routes and macro bridge | 4–6 weeks (January to mid-February 2027) | Route module; `psv_bridge.py`; energy savings in DIGNAD-lite; island pilot | 1, 2, 3, 8, 9, 10 |
| 3. Sector cards and frontier | 6–8 weeks (mid-February to April 2027) | Seven cards; frontier and knapsack; BOOST comparison; λ feedback; dashboard pages | 16 (in part) |
| 4. Bolder options | Later | Option B; robust portfolios; distribution weights; AI-assisted BOOST tagging; DSA treatment net of savings | 4, 5, 6 |

## Phase 0: specification and data audit

- **Deliverables:** `PSV_Method_v0_1.md` and version notes; the category
  map (`cdpm_category_map.csv`); the fiscal attribute table
  (`fiscal_attributes.csv`, keyed on the transformation code: capital
  share, asset life, payer shares, revenue capture, budget line); the
  parameter sheet (`params_psv.csv`); and a written fix for discounting
  SISEPUEDE results once, with NemoMod power capital re-derived from
  undiscounted capacity additions.
- **Pilots:** St Lucia (a small island, using the NREL snapshot and CCDR
  data), Uganda (the October 2025 SISEPUEDE run) and Kenya (the macro
  tool's pilot).
- **Data:** SISEPUEDE outputs; NMIM and the dashboard panel; PEFA PI-11
  scores; BOOST extracts for the pilots, checking availability and
  licences; IMF macro-fiscal projections (only Morocco exists today).
- **Validation:** harmonise currency and price bases (SISEPUEDE 2019 PPP
  dollars, CPAT market dollars, CCDR tables discounted at 6%); confirm
  the Uganda NemoMod rate with the SISEPUEDE team.
- **Decisions for the team:** the λ default and stress rule; the
  end-of-year convention; the "money in, assets out" convention; the
  pilots; where the layer lives; and compatibility with the CPAT
  agreements with the IMF, which a reviewer has already queried.

## Phase 1: the core layer

- **Deliverables:** `psv.py` (tags, economic and fiscal NPVs, W, F,
  MVPF, $NB_{\lambda}$, equivalent annual cost, recurrent costs and the
  delivery haircuts); a workbook with inputs, calculations and results
  sheets; runs on NMIM and the Uganda output.
- **Tests:**
  1. $ENPV = W - F$ on every measure.
  2. With λ = 1, the layer reproduces the investment-needs model's lens
     (c): $ENPV\cdot CRF(6\%, n) = -IC$.
  3. With all haircuts at 1, the economic NPV equals SISEPUEDE's net
     present value at 6% after the discounting fix.
  4. Sign conventions are reconciled (costs negative in the CBA,
     positive in the abatement-cost file).
  5. No NemoMod discounted series is discounted again.
  6. The worked example's results file is a regression fixture.
- **Decisions:** approve the category map; decide whether
  $NB_{\lambda}$ and MVPF appear in the CPAT interface's macro and
  fiscal results sheet.

## Phase 2: financing routes and the macro bridge

- **Deliverables:** the route module (`psv_routes.py`) for commercial,
  concessional, utility, PPA with or without guarantee, contract for
  difference and grant; contract, utility and guarantee liabilities
  passed to LIC-DSF-lite; `psv_bridge.py`, which also delivers energy
  savings in DIGNAD-lite, sector returns, an absorptive-capacity cost
  curve, BOOST execution as a separate leak and utility debt as a
  contingent liability; the St Lucia pilot, using the worked example as
  its template.
- **Validation:** loan payments discounted at the loan rate equal
  principal; grant elements reproduced; the 35% DSA rule replicated; a
  zero programme reproduces the current integrated results; Kenya with
  energy savings in DIGNAD-lite compared with GIMF-lite; the bridge's
  convergence check passes.
- **Decisions:** whether to adopt the cash-short $\lambda_{t}$; whether
  the DSA view net of savings is shown as a sensitivity only.

## Phase 3: sector cards and the frontier

- **Deliverables:** seven sector cards plus SISEPUEDE's energy card, with
  defaults and confidence ratings; the frontier and knapsack (with
  `scipy.optimize.milp`) under envelope, family, scale-up, floor and
  emissions constraints; the BOOST comparison and reallocation gain; the
  λ feedback loop; dashboard pages.
- **Validation:** the knapsack equals the greedy solution for divisible
  measures; the frontier is concave; a report shows the share of BOOST
  spending that cannot be mapped; card values fall inside benchmark
  ranges or are flagged.
- **Data:** BOOST; DCP3; learning-adjusted years of schooling; ASPIRE;
  HDM-4 or RONET runs; and the Bank's spending-efficiency scores and
  code, to be requested from the Fiscal Policy unit.
- **Decisions:** which sectors go first; whether frontier results are
  shared with pilot governments.

## Phase 4: bolder options

Option B's multi-capital model and the efficiency-return switch; robust
portfolios over SISEPUEDE's futures, with the discount rate and cost of
capital added to the uncertain inputs; distribution weights from CPAT's
household module; AI-assisted BOOST tagging; the DSA treatment net of
savings; λ derived from the models; and the DIGNAR resource block for oil
producers such as Uganda after first oil (Appendix F). Each needs its own
method note and caveats entry.

## What SISEPUEDE itself should change

Most upgrades sit outside SISEPUEDE. Five changes inside it would make
them simpler and should be raised with the Tec de Monterrey team before
the contract ends:

1. align NemoMod's configured discount rate with the documented default,
   or export undiscounted power capital;
2. implement the technology interest rates, so the power mix reflects
   the country's cost of capital;
3. replace straight-line capital charges with capital recovery factors,
   and document the rate behind every levelised factor;
4. report gross capital separately from operating costs and savings,
   with an asset life per transformation;
5. report carbon as a separate line, and add the discount rate and cost
   of capital to the uncertain inputs of the futures.

The companion note on global investment needs sets out the same fixes in
more detail (its Appendix A.4).


# Appendix A. Answers to the nine questions

This note began as nine questions. Each answer points to where the
detail is.

**1. What rules should governments use?** Fund a measure when its value
to society per dollar of *net* public cost exceeds the cost of raising
that dollar: MVPF above λ, where λ is about 1.1–1.2 in African estimates
(Auriol and Warlters 2012). Net public cost is measured after the
private counterfactual, delivery losses and the money the measure
returns. Under a binding budget, rank by MVPF and fund down the list.
Add a fiscal test (cash profile, debt path, contingent liabilities),
because a measure of high value can still be unaffordable. With λ = 1
and no budget limit, the rule is the World Bank's net-present-value
test. Detail: Appendices B.1 and B.3; steps 5 and 6.

**2. Efficiency of spending, or the "Pigouvian" gap?** Neither alone.
The decision quantity is the social value per net public dollar,
*relative to what would happen anyway*. The gap between private and
social returns decides whether public money should be used at all, and
how much. Technical efficiency decides how much of that value survives
delivery. Across programmes, value per dollar varies by multiples, from
below 1 to "pays for itself", while technical efficiency typically
scales it by 0.6–0.9, so allocation is usually the bigger lever. Public
money should pay the gap (the viability gap), not the whole investment,
and a price instrument should be tested first. Detail: Appendices B.1
and B.2; step 4.

**3. What changes in low-capacity countries?** The rule stays; the
parameters change. Less spending becomes capital (an efficiency gap of
about 40% in low-income developing countries), execution is slow,
recurrent costs go unfunded, overruns are systematic, and λ is higher
where informality is high. The tool should apply efficiency and
execution haircuts and cost uplifts, put maintenance first, prefer
simple and auctioned instruments, cap the speed of scale-up, use a cash
benchmark and report switching values. One caution from the IMF's own
models: low efficiency does not by itself mean low returns, because
scarce capital earns more at the margin (Berg et al. 2019). Detail:
Appendix B.5; the section on low-capacity settings.

**4. What do the World Bank and the IMF use?** The World Bank uses
Schick's three-level framework (aggregate discipline, allocative and
technical efficiency), now inside the Public Finance Review with its 2024
guidance and "PFR Fundamentals" notes. Santiago Herrera (the "Santiago
Harrer" of the request) and co-authors lead its frontier work:
efficiency scores for education, health and infrastructure, a "potential
fiscal savings" method and budget-rigidity measures. The Bank also uses
BOOST, PEFA, the public investment management diagnostic, its
economic-analysis guidance, the Infrastructure Prioritization Framework,
*Beyond the Gap*, CCDRs and MFMod. The IMF uses PIE-X, PIMA and C-PIMA,
spending reviews, SDG costing, the DIG, DIGNAR, DIGNAD and GIMF models,
PFRAM and the LIC-DSF. Neither institution routinely measures allocative
efficiency *across* sectors as value per net public dollar. Detail:
Appendix C.

**5. Has CBA been extended beyond projects and beyond climate?** Yes, in
several strands that do not yet meet: cross-sector ranking (Copenhagen
Consensus); health packages and cost-effectiveness thresholds (DCP3);
education cost-effectiveness ("Smart Buys", learning-adjusted years of
schooling); the MVPF library for social policy; water, sanitation and
resilience benefit-cost ratios; general-equilibrium CBA; robust
decision-making for whole-economy packages (Costa Rica); and macro-linked
sector analysis in CCDRs. What is usually missing is the cost of public
funds, implementation risk and marginal rather than average returns.
Detail: Appendix B.10; step 10.

**6. How should capital and current spending be integrated?** Put both
on an annual footing. Turn each capital outlay into an equivalent annual
cost with a capital recovery factor, add the running costs it creates,
and compare with current programmes on annual fiscal cost and on value
per net public dollar. Treat "maintenance first" as a measure in its own
right: deferred road maintenance costs three to five times more later
(Harral and Faiz 1988). In the macro models, capital goes to public
capital with its efficiency and return, and current spending to
non-capital spending. Detail: Appendix B.6; step 7.

**7. Can PPPs or PPAs turn capital spending into a sensible running
cost?** They do not create fiscal space: over time a PPP costs the
budget much the same as public provision (Engel, Fischer and Galetovic
2013). But they can solve a *liquidity* problem and a *debt-statistics*
problem. In the worked example, a guaranteed solar PPA costs
USD 14.2 million a year against USD 20.5 million of diesel saved and
adds no headline debt. Its payment stream is worth 1.27 times the plant,
and it costs only about USD 5 million more in present value than
sovereign borrowing at 8%. Without a guarantee it barely passes. Long
concessional finance is better on every measure where it is available.
Detail: Appendices B.7, B.8 and E; step 8.

**8. How should a revenue return be treated?** In the economic analysis,
fees and taxes are transfers and are left out, apart from real resource
effects. In the fiscal ledger they are counted. Each dollar returned is
worth λ, not 1, because it avoids a dollar of distorting tax, so it
lowers the MVPF's denominator. Tax from faster growth is left to the
macro model. A revenue measure that corrects an externality, such as a
carbon tax or subsidy reform, sits on the same ladder as spending and is
usually the cheapest source of funds. Detail: Appendix B.3; step 9.

**9. Is there efficient-frontier work to integrate?** Three kinds.
*Technical* frontiers (Herrera's work; the IMF's PIE-X) give efficiency
haircuts. *Allocative* frontiers rank measures by value per public
dollar and add them up against the fiscal envelope; IFPRI's estimates
of marginal returns by spending category (Fan, Hazell and Thorat 2000)
are the empirical template. *Portfolio and robustness* frontiers
(Awerbuch; robust decision-making; *Lifelines*) add risk. The gap
between the current BOOST allocation and the frontier is the
"reallocation gain". Detail: Appendix B.9; step 10.

# Appendix B. The literature

This appendix reviews the literature behind the upgrades. Equations are
numbered B1, B2 and so on.

## B.1 Allocative and technical efficiency

The World Bank's public expenditure work still rests on Schick's (1998)
three objectives: aggregate fiscal discipline, allocative efficiency and
operational (technical) efficiency. The 2024 *Guidance for Public
Finance Reviews* keeps the distinction: allocative efficiency is getting
the most benefit per unit of cost; technical efficiency is delivering a
given output at the lowest spending (World Bank 2024a †).

Two terms are easily confused. Farrell's "allocative efficiency" (†)
concerns the *input* mix at given prices, whereas public-finance
allocative efficiency concerns the *output* mix across uses. The IMF's
public-investment "efficiency gap" is a Farrell-type technical measure;
the MVPF and CBA are about the output mix. Efficiency (outputs per
input, such as cost per kilometre) also differs from effectiveness
(outcomes per output, such as travel time saved). CBA and the MVPF value
outcomes at willingness to pay, so they capture both, provided benefits
are measured as outcomes.

**The decision rule.** For a pure public good with lump-sum finance, the
Samuelson condition equates the sum of marginal rates of substitution to
the marginal rate of transformation (†). With distorting taxes the
"modified Samuelson rule" scales the cost side by λ. Allocating a fixed
budget across uses equalises marginal social benefit per dollar across
funded uses, at a level μ that equals λ when the budget is itself set
optimally:

$$\sum_{i}^{}MRS_{i} = \lambda\, MRT,\qquad\frac{MSB_{j}}{MC_{j}} = \mu\ \text{for every funded}\ j\quad\quad(B1)$$

Modern practice makes this measurable with the MVPF. Hendren and
Sprung-Keyser (2020) divide each policy's benefit to recipients
(willingness to pay) by its net cost to government, long-run budget
effects included, and state that "comparing MVPFs across policies
provides a unified method of assessing their impact on social welfare".
Finkelstein and Hendren (2020) apply it across public finance, labour,
development, trade and industrial organisation. For a small tax cut,
willingness to pay equals the revenue cost, so the MVPF of a tax equals
its marginal cost of funds. A spending policy financed by a tax
therefore raises welfare if and only if its MVPF exceeds that tax's
marginal cost of funds. That is equation B1 in measurable form, and it
is the rule in equation (4).

Composition matters in its own right. Devarajan, Swaroop and Zou (1996)
show that whether shifting spending toward a component raises growth
depends "not just on the physical productivity of the different
components of public expenditure but also on the initial shares".
Marginal, not average, returns decide allocation.

**Which matters more?** Across 133 US policies, MVPFs range from below 1
to infinite: direct investments in low-income children's health and
education often "pay for themselves", while adult-targeted policies
"generally have smaller MVPFs, between 0.5 and 2" (Hendren and
Sprung-Keyser 2020). Technical-efficiency gaps in public investment
average about 30%, and 40% in low-income developing countries (IMF
2015); the most efficient investors are reported to get twice the growth
"bang" per "buck" of the least efficient (†). The spread in allocative
value is therefore much larger than the spread in technical efficiency,
so doing the right things is usually the bigger lever. No study was
found that formally splits welfare losses into the two. Technical
inefficiency is not second-order where it is extreme: Pritchett's (2000)
point that "the cost of public investment is not the value of public
capital" makes "can this state deliver this?" a first-order allocative
question in low-capacity settings. A compact way to see both effects,
with ψ a distributional weight and $e$ and $p$ delivery efficiency and
completion probability, is:

$$\text{welfare per public dollar} \approx \frac{\psi\,(MSB - \text{counterfactual value})\, e\, p}{\lambda\cdot\text{net fiscal cost per dollar}}\quad\quad(B2)$$

## B.2 Why the state spends: the counterfactual and the Pigouvian gap

The social value of a public intervention is the difference between
outcomes with and without it, *net of what private actors and other
policies would have done anyway*. The case for public provision rests on
a market failure (public goods, externalities, natural monopoly, missing
markets, information, coordination) or on equity.

**The counterfactual.** Devarajan, Squire and Suthiwart-Narueput (1997)
argued for moving World Bank appraisal away from precise rates of return
toward three questions: the rationale for public intervention, the
project's fiscal impact, and the fungibility of aid. Their companion
paper states that "the relevant counterfactual involves assessing what
the private sector would have otherwise provided" (Devarajan, Squire and
Suthiwart-Narueput 1999 †). Harberger (1997) replied that these steps
"fit quite easily within the inherited corpus of applied welfare
economics": the critique refines CBA rather than replacing it.
Fungibility extends the counterfactual to the budget: if aid finances
what the government would have done anyway, its marginal effect is
whatever the freed money funds.

These ideas became Bank policy. OP/BP 10.04 held that "no investment
projects are exempt from a net-benefit test" (IEG). The 2013 guidance
note asks of every project, "Is public sector provision or financing the
appropriate vehicle?" (World Bank 2013), and the current Directive on
Investment Project Financing keeps three questions: the project's
contribution to development, "the rationale for the public sector
provision" and the value added of the Bank's support (World Bank 2023).
A Bank transport note states that public contributions to PPPs "should
be justified on the basis of external benefits" (Mackie, Nellthorp and
Laird 2005 †). Whether current guidance *requires* a quantified
life-cycle fiscal impact could not be confirmed.

**The Pigouvian gap.** Take a subsidy $s$ on an activity with marginal
external benefit $e$, quantity $q$ and induced response $q' = dq/ds$.
With costly public funds, welfare is
$W = CS(s) + e\,q - \lambda\, s\, q$, and the first-order condition gives:

$$s^{*} = \frac{e - (\lambda - 1)\, q/q'}{\lambda}\quad\quad(B3)$$

With λ = 1 this is the textbook Pigouvian subsidy, $s^{*} = e$. With
λ > 1 the best subsidy is below the gap, and further below when
inframarginal units $q$ (those that would happen anyway) are large
relative to induced units $q'$. Value comes from the induced change
times the gap, while every inframarginal dollar costs λ − 1. The same
line explains why a *tax* on the externality usually beats a *subsidy*
for the alternative: the tax raises money on inframarginal units instead
of paying for them. Subsidies create negative fiscal externalities that
taxation cannot simply internalise (Luttmer 2022).

Two consequences follow, and step 4 applies both: public money should
pay the gap (the viability gap), not the whole investment; and a price
or regulation should be tested before spending. Where spending is
justified on distribution grounds, the comparison is the cheapest
alternative way of redistributing, such as a cash transfer.

## B.3 The cost and the value of public funds

**The marginal cost of public funds.** Raising USD 1 through distorting
taxes costs the private sector about USD λ, with λ > 1. Dahlby (2008)
gives the general framework, including borrowing and grants. Table B1
gives the main estimates.

**Table B1. Estimates and conventions for λ**

| Source | Estimate or convention | Note |
|------------------------------|------------------------------|------------------------------|
| Auriol and Warlters (2012), 38 African countries | About 1.2 for all five taxes; about 1.1 using each country's cheapest tax (usually VAT) | Informality, not income, drives it |
| Kleven and Kreiner (2006), 15 European countries | Around 2 in Scandinavian and some Continental countries | The participation margin matters |
| Norway (NOU 1997:27) | 1.2 in all CBAs, still recommended | Statistics Norway (2015): "no firm ground" for a point estimate |
| Statistics Norway Discussion Paper 925 | 1.06–1.16 when transfers ease participation distortions † | |
| France (1.2), Denmark (about 1.1) | Conventions † | |

A Dahlby-type formula for a proportional tax shows why λ can be high in
low-tax countries:

$$MCF = \frac{1 - t}{1 - t - t\,\varepsilon}\quad\quad(B4)$$

so λ rises with the elasticity ε of the taxed base. A large informal
sector raises the effective elasticity of a narrow formal base, which is
consistent with Auriol and Warlters. λ should therefore be set by country
(informality, tax mix), not by income group. Informality also lowers
fiscal multipliers (IMF 2022). One caveat: if much of a measured λ above
1 reflects redistribution, the distribution-corrected λ at an optimal
tax system is about 1 (Kaplow; Jacobs †). The MVPF sidesteps this by
comparing a policy with the *actual* financing instrument. Classic
appraisal (Little and Mirrlees; Squire and van der Tak; UNIDO †) used a
premium on uncommitted public income that plays the same role.

**The MVPF and revenue returns.** The MVPF is willingness to pay divided
by net cost, where net cost is the upfront cost less fiscal
externalities (future tax gains and benefit savings). Revenue returns
therefore enter the denominator, and a policy whose fiscal externalities
exceed its cost "pays for itself" (Hendren and Sprung-Keyser 2020).
Applications in low- and middle-income countries are few:

- unemployment benefits in Mauritius, with high informality, are
  consistent with an MVPF of 1.23 (Liepmann and Pignatti 2024 †);
- a Mexico property-tax study applies the MVPF to tax design;
- Kenyan deworming has a conservative financial return of 32% a year
  and may raise more future revenue than it costs (Baird et al. 2016);
  the 20-year follow-up reports a social return of 37%; the evidence is
  contested;
- for cash transfers in Brazil, local demand effects that raise tax
  revenue lift the MVPF well above 1.

No cross-programme MVPF library for low- and middle-income countries was
found. Hahn et al. extend the MVPF to environmental externalities.

**How returns are counted.** In economic CBA, fees and taxes are
transfers: the user's willingness to pay is the benefit, and the fee
moves money from user to state. With λ > 1, each dollar of net revenue
returned is worth an extra λ − 1, because it avoids a dollar of
distorting tax:

$$ENPV_{\lambda} = PV(B - C^{res}) - (\lambda - 1)\, PV(G^{net}),\qquad G^{net} = \text{capex} + OM + \text{subsidies} - \text{fees} - \text{induced tax} - \text{avoided public spending}\quad\quad(B5)$$

A USD 1 fee raises $ENPV_{\lambda}$ by exactly λ − 1 (0.20 at λ = 1.2).
A benefit-cost ratio that counts revenue as a benefit changes with that
classification; the MVPF fixes the convention by putting all budget
effects in the denominator. Revenue to a *different* budget (a utility,
another level of government) is valued at that budget's shadow price.
Adam and Bevan (2014) show why a separate fiscal analysis is still
needed in low-income countries: public investment requires the
recurrent-cost problem to be solved, taxation distorts, and the state
captures only part of the output it creates. A project pays for itself
fiscally only if fees plus the captured share of induced income cover
its capital, upkeep and debt service; in low-tax, high-informality
countries that share is small, so even projects with high economic value
can raise debt ratios.

## B.4 Discounting, carbon and distribution

**The discount rate.** The World Bank's 2016 note sets the social rate
with the Ramsey rule: "if per capita growth is expected to be y% over
the life of the project, the annual discount rate should be between y%
and 2y% per year", so 3% growth gives 6% and growth of 1–5% gives 2–10%,
with sensitivity analysis required (World Bank 2016). Before it, the
multilateral banks used 10–12%. The Asian Development Bank cut its
hurdle from 12% to 9% in 2017, with 6% for some environmental projects
(ADB 2017). About 85% of studies in the Global Health Cost-Effectiveness
Registry use 3% (CGD). The UK Green Book uses 3.5%, declining with
horizon (†). The philosophies differ: the World Bank's is a social rate
of time preference; ADB's 9% is closer to an opportunity cost of
capital. A tool must label which it uses.

High sovereign borrowing costs belong in the *fiscal* analysis, not in
the social rate. The present value at the social rate $r$ of debt service
on USD 1 borrowed for $n$ years at rate $i$ is:

$$\kappa = \frac{i}{1 - (1 + i)^{- n}}\cdot\frac{1 - (1 + r)^{- n}}{r}\quad\quad(B6)$$

At $i$ = 8%, $r$ = 6% and $n$ = 30, κ = 1.22 (1.47 at λ = 1.2); at 10%
over 20 years, 1.35; on concessional terms of 1.25% over 30 years, 0.55,
a grant element of about 45%. The Arrow–Lind case for discounting public
projects at a risk-free rate (†) fails where projects are large relative
to the economy or their returns move with GDP, as on small islands where
hurricanes hit both. The better fix is certainty-equivalent benefits,
not a higher rate.

**The shadow price of carbon.** The World Bank's 2024 note makes the
shadow price a requirement for investment projects subject to
greenhouse gas accounting. It uses the High-Level Commission corridor:
USD 40–80 a tonne in 2020, rising to USD 50–100 by 2030 (2017 dollars),
extrapolated at 2.25% a year to USD 78–156 in 2050 (World Bank 2024b).
Lower-income countries use the bottom of the range and middle-income
countries the top, and the price is "not intended as an automatic rule
to select projects" (†). Critics note it reflects the cost of meeting
the Paris goals rather than full damages (D+C). It belongs in the
economic analysis only, not in the fiscal ledger, unless carbon is
actually priced.

**Distributional weights.** The Green Book uses
$w_{i} = (y_{ref}/y_{i})^{\eta}$ with η = 1.3 by default and median income
as the reference, with 0.8 and 2.0 as sensitivities (†); 2021 Treasury
guidance cites a bottom-quintile weight of 2.4 (HM Treasury 2021).
Combined with λ, a transfer from the budget to group $i$ passes on
distribution grounds only if $w_{i} > \lambda$: with λ = 1.2 and
η = 1.3, only households below about 0.87 of the reference income
qualify. Acland and Greenberg (2022) review practice.

## B.5 Low-capacity countries: money spent is not capital built

**Efficiency gaps.** The IMF's 2015 frontier study finds an average
public-investment efficiency gap of about 30%: 40% in low-income
developing countries, 27% in emerging markets and 13% in advanced
economies. Stronger public investment management could close up to
two-thirds of it (IMF 2015). *Well Spent* says stronger infrastructure
governance could recover more than half of observed losses (Schwartz et
al. 2020 †). Unit costs of road projects rise sharply once public
investment passes about 10% of GDP, or about 7% in low-efficiency
countries (IMF 2020 †). In DIGNAR's calibration, the share of spending
that becomes capital falls from 0.5 to 0.35 when investment exceeds 1.6
times its average (Melina, Yang and Zanna 2016).

**Low efficiency does not mean low returns.** Efficiency-adjusted
public capital for 52 developing countries shows the marginal product of
public capital is *higher* in low-income countries (Gupta et al. 2014).
Berg et al. (2019) show that in standard growth models more investment
in inefficient countries need not have a smaller growth effect, because
efficiency and capital scarcity are inversely related. If the output
elasticity is held fixed, efficiency drops out of the growth effect; if
the return is held fixed (as from a CBA), the payoff per dollar scales
with efficiency. A tool must declare which it holds fixed; the macro
tool's TODO list already has this "efficiency-return switch".

**Composition, recurrent costs and overruns.** In 43 developing
countries over about 20 years, a higher *current* share of spending went
with higher growth and a higher *capital* share with lower growth:
"seemingly productive expenditures, when used in excess, could become
unproductive" (Devarajan, Swaroop and Zou 1996). Recurrent costs must be
funded for capital to yield services (Adam and Bevan 2014). Overruns are
systematic: HM Treasury's guidance tells appraisers to start from
upper-bound uplifts and reduce them only on "clear and tangible
evidence" (Table B2).

**Table B2. HM Treasury optimism-bias uplifts**

| Project type | Capital cost, upper / lower | Works duration, upper / lower |
|------------------------------|---------------------------|-----------------------------|
| Standard buildings | 24% / 2% | 4% / 1% |
| Non-standard buildings | 51% / 4% | 39% / 2% |
| Non-standard civil engineering | 66% (upper) | n.a. |
| Equipment and development | 200% / 10% | 54% / 10% |

**What follows.** With efficiency of 0.6, completion probability of
0.85 and additionality of 0.7, 100 of headline benefit becomes about 36
of expected benefit; with a cost uplift of 44–66%, many headline
benefit-cost ratios of 2–3 fall below 1. Switching values are therefore
more informative than point estimates. The literature supports six
adjustments:

1. haircut benefits for efficiency and completion, and uplift costs and
   durations, rather than raising the discount rate;
2. require funded upkeep and put maintenance first;
3. use a country-specific, often higher λ where informality is high;
4. prefer simple, rules-based, competitively tendered instruments, and
   make complex projects beat a cash benchmark;
5. scale up gradually;
6. keep appraisal simple: few robust parameters, switching values and
   reference-class uplifts.

The 1997 World Development Report's advice to match the state's role to
its capability, and the problem-driven iterative adaptation literature,
point the same way (†).

## B.6 Capital and current spending

**The recurrent-cost problem.** Heller's (1974) Kenyan study founded the
formal treatment: investment is constrained by the ability to fund the
recurrent costs projects create. Donor-biased design, in which donors
finance capital and recipients must fund upkeep, makes it worse. The
Bank's answer was budgeting with recurrent-cost coefficients (Hood,
Husband and Yu 2002), to avoid "chronic underfunding of maintenance and
operating costs"; their numbers could not be read. Typical values are
single-digit percentages of capital a year for roads and power, and much
higher for health and education facilities because of staffing (†).

**Maintenance has the highest returns.** Developing countries neglect
maintenance in favour of new building, and reallocating toward
maintenance raises GDP (Rioja 2003); the durability of public capital
depends on maintenance (Kalaitzidakis and Kalyvitis 2004). Across 85
countries' road networks, restoring deteriorated roads costs "three to
five times greater than the bill would have been for timely and
effective maintenance" (Harral and Faiz 1988). *Beyond the Gap* puts the
life-cycle saving from good maintenance at more than 50% (Rozenberg and
Fay 2019). DIG-Labor lets maintenance lower depreciation, and the 2018
PIMA update gives maintenance more weight. With the finding that
developing countries over-allocated to capital, this makes "maintenance
first" the most robust allocative rule in the literature.

**One footing.** Capital and current spending become comparable once
capital is annualised (equation 9). On a public balance sheet, which the
IMF assembled for 31 countries (assets of USD 101 trillion, 219% of GDP;
IMF 2018), debt-financed capital that creates an asset of matching value
leaves net worth unchanged at the start; net worth then moves with the
asset's NPV, any over-payment, and depreciation net of maintenance.
Current spending reduces net worth one for one. That is the formal case
for not treating a self-financing, well-maintained energy asset like
consumption, *provided* the asset is valued realistically.

## B.7 PPPs, PPAs and contingent liabilities

**No free fiscal space.** Engel, Fischer and Galetovic (2013) reject the
idea that PPPs are justified because they free public funds: under the
government's budget constraint over time, a PPP costs the budget much
the same as public provision. Any case rests on efficiency (bundling,
incentives, risk transfer). They warn that "pervasive renegotiations,
faulty fiscal accounting, and poor governance" threaten the model and
that efficiency gains "often prove elusive" (Engel, Fischer and
Galetovic 2014). The test is a financing premium: the present value at
the government's rate of the payment stream, less capital and upkeep.
That premium buys risk transfer and efficiency; if the gains are
smaller, the PPP destroys value even while it "saves" debt on day one.
The UK evidence is sobering: the National Audit Office found
GBP 199 billion of future PFI payments, finance costs 2–3.75 points above
government borrowing, and schools under PF2 costing about 40% more than
with government borrowing (†). Bundling can raise construction cost to
lower later upkeep (Blanc-Brude, Goldsmith and Välilä 2006).

**Accounting.** Under the European statistical rules, a PPP stays off
the government balance sheet only if the partner bears construction
risk *and* either availability or demand risk (Eurostat and EPEC 2016).
Under IPSAS 32, a government that recognises a concession asset also
recognises a liability, initially at the asset's value (IFAC). A private
producer selling to a state utility under a long-term PPA is
economically a concession. PFRAM covers guarantees, minimum revenue
guarantees, termination clauses and PPAs.

**When PPPs and PPAs add value:** bundling lowers whole-life cost;
construction and performance risk are really transferred; competitive
tendering reveals cost; and private upkeep is more reliable than that of
a cash-starved utility, because a PPA ring-fences maintenance funding,
which addresses the recurrent-cost problem directly.

**Good auctions.** IFC's Scaling Solar in Zambia (2016) cleared at 6.02
and 7.84 US cents a kWh, the first fixed for 25 years. The Maldives
ASPIRE programme, with IDA guarantees of USD 16 million, cut tariffs from
21 cents (2014) to about 10–11 cents (the two Bank sources differ) and
then 9.8 cents. Jamaica's competitive round selected 33.1 MW of solar at
8.54 cents.

**Bad contracts.** Ghana's capacity charges for unused take-or-pay
capacity were about USD 320 million in 2018, rising toward USD 620
million a year (ESMAP 2021); more than GH₵12 billion was paid for
unused power in 2017–21 (†). In Kenya, fixed capacity charges were 52%
of power-purchase costs in 2020/21, and a moratorium on new PPAs
followed (†). Pakistan's capacity payments are large, though the source
is weak (†). Across 39 African power sectors only 2 were financially
viable, and utility quasi-fiscal deficits averaged 1.5% of GDP (Kojima
and Trimble 2016).

What separates good from bad is not "PPA or public". It is competitive
price discovery, sizing to demand, the payment structure (solar
"take-and-pay" with deemed energy carries far less unconditional
liability than thermal capacity charges †) and credible off-taker
security. A World Bank, IDA or MIGA guarantee lowers the producer's cost
of capital, but it is backed by a sovereign indemnity: it prices and
shares the exposure rather than removing it.

## B.8 Small island states: an oil-import trap

- **Fuel bills.** More than 90% of small island states' energy comes
  from imported oil, up to 20% of their imports (IRENA 2014). Islands
  spend 2–4 times the world average share of GDP on fuel imports. The
  Maldives' oil imports were USD 555 million in 2014, close to 20% of
  GDP.
- **Island grids.** St Lucia generated 399 GWh in 2018, about 99% from
  diesel, with residential tariffs of USD 0.28 a kWh and fuel imports of
  4.9% of GDP; St Vincent and the Grenadines generated 136 GWh, with fuel
  imports of 6.2% of GDP (NREL). Eastern Caribbean tariffs of 26–37
  cents are reported as 3–4 times the emerging-market median (†).
- **The Pacific.** Fuel imports averaged 7.8% of GDP in 2018, and 12.9%
  in Palau (†).
- **The oil price.** EIA's October 2026 outlook, as reported, has Brent
  at about USD 105 in the fourth quarter of 2026, USD 96 for 2026 and
  USD 84 for 2027 after Middle East supply disruptions (†).

Renewables are cheap in principle: a global solar levelised cost of USD
44 a MWh, about USD 140 a kWh for a 4-hour battery, and firm
solar-plus-storage below USD 85 a MWh at good sites (IRENA 2026). Two
premia stand in the way. Island capital costs run well above global
averages: ASPIRE tariffs imply solar capex of about USD 1,040–1,170 a kW,
1.5–1.7 times IRENA's global USD 691. And the cost of capital is high:
median 2024 solar WACC was 8–9.4% in Southeast Asia against 5–6.5% in
advanced economies (IEA, via pv magazine †). Financing costs strongly
drive solar costs (Ondraczek et al. 2015).

Fiscal room is scarce: two-fifths of the 35 small developing states are
at high risk of, or in, debt distress (World Bank 2024c). Concessional
windows exist but are small. IDA's small-states exception serves about
23 states with about 3% of IDA's envelope (†); the IMF's Resilience and
Sustainability Trust lends at 20 years with 10½ years' grace, but no new
arrangements were reported in the second half of 2025 (†); and
debt-for-nature swaps show what credit enhancement can do (Belize bought
back USD 553 million of bonds at 55 cents; Barbados refinanced
USD 293 million with USD 300 million of IDB and EIB guarantees †). A
hedge value adds to the case: fixed-cost renewables can lower the risk
of a fuel-heavy portfolio at little or no expected cost (Awerbuch and
Berger 2003; Awerbuch and Yang 2007). The IMF has analysed Caribbean
energy costs and the debt effects of energy investment (McIntyre et al.
2016).

The trap has three separate constraints, and the worked example
quantifies each: **liquidity** (a short tenor makes early debt service
exceed the fuel saving); **solvency** (financing may cost more than the
asset returns); and **the debt stock** (the DSA and ratings score the
gross liability, not the self-financing asset behind it).

## B.9 Efficiency frontiers

**Technical frontiers.** Cross-country frontier studies consistently
find large inefficiency: in Africa (Gupta and Verhoeven 2001), in
industrial countries (Afonso, Schuknecht and Tanzi 2005), in health
(Grigoli and Kapsoli 2013) and in secondary education (Grigoli 2014), as
well as in Herrera's line of work (Appendix C.2). Simar and Wilson
(2007) show that naive second-stage regressions of efficiency scores
lack a coherent statistical basis and propose bootstrap procedures. For
a CBA tool, output-oriented scores are the natural haircut, because the
tool fixes the budget and asks what outcome it buys. A score should be
used once, as an outcome haircut, a unit-cost mark-up, or effective
capital passed to the macro model; if unit costs already come from the
country's own outturns, the score is already embedded.

**Allocative frontiers.** IFPRI's work is the empirical template for
marginal returns across spending categories. In rural India (1970–93),
roads and agricultural research had "much larger poverty impacts per
rupee spent than any other government investment", education came
third, and irrigation, health and rural development had "only modest"
effects (Fan, Hazell and Thorat 2000). Input subsidies mattered early in
the Green Revolution but now rank low (Fan, Gulati and Thorat 2008). In
China, education had the largest poverty effect and agricultural
research the largest growth effect (Fan, Zhang and Zhang 2002). The
average return to agricultural research in developing countries is about
60% (FAO 2012). These numbers are historical and local: priors and
checks, not transferable parameters. That early subsidies had high
returns that later fell argues for declining marginal-benefit curves,
not constant ratios.

**Portfolio and robust frontiers.** Robust decision-making chooses
near-term actions that hold up across "a vast range of plausible
futures" (Lempert, Popper and Bankes 2003). The closest precedent for
SISEPUEDE is the Costa Rica study: about USD 41 billion of net benefit
over 2020–2050 at 5%, from about USD 78 billion of benefits against USD
37 billion of costs (Groves et al. 2020). *Lifelines* finds that
resilient infrastructure yields about USD 4 per USD 1, with benefits
above costs in 96% of scenarios (Hallegatte, Rentschler and Rozenberg
2019); that share is a compact risk-adjusted statistic.

Marginal abatement cost curves are a static special case of the
frontier. They omit co-benefits, interactions, uncertainty and timing
(Kesicki and Ekins 2012), and with deployment limits and a long-term
target it can be optimal to start expensive, slow measures early
(Vogt-Schilb and Hallegatte 2014). A budget frontier therefore needs
interaction flags, co-benefits, deployment limits and a target, as
equation (11) has.

## B.10 Extending CBA across sectors and to the whole economy

**Cross-sector ranking.** The Copenhagen Consensus is the main precedent
for ranking interventions across sectors with harmonised assumptions.
Its 2023 set reports benefit-cost ratios from 18 (nutrition) to about
125 (e-procurement †), with a pooled ratio of 52 at an 8% discount rate
(Copenhagen Consensus 2023); its front matter says it "is not the
standard Journal of Benefit-Cost Analysis peer review process". Earlier
rounds used 3% and 5%, so results must be harmonised before pooling. For
a government tool the weaknesses are no cost of funds, average rather
than marginal ratios, and little attention to delivery. Climate packages
typically show ratios of about 1–5 (Costa Rica about 2.1; *Lifelines*
about 4), so they rank low against health "best buys" unless co-benefits
and carbon are valued on the same basis.

**Health.** DCP3's essential package of 218 interventions costs about
USD 79 a person a year in low-income and USD 130 in lower-middle-income
countries, about 8% and 4.2% of national income, and the highest-priority
subset about half that (Watkins et al. 2020). Thresholds based on the
health forgone elsewhere are far below the old rule of 1–3 times GDP
per person (Ochalek, Lomas and Claxton 2018; Woods et al. 2016).
Comparison across sectors needs money values: the reference case
transfers the value of a statistical life with an income elasticity of
about 1.5 and ratios to income of 80–170 (Robinson, Hammitt and O'Keeffe
2019).

**Education.** Across 150 evaluations in 46 countries, the most
cost-effective programmes deliver "the equivalent of three additional
years of high-quality schooling for just $100 per child", against zero
for others (Angrist et al. 2020). The "Smart Buys" tiers rank structured
pedagogy and teaching at the right level as "Great Buys" (GEEAP 2023).
Learning-adjusted years can be valued at the private return of about 9%
per year of schooling (Psacharopoulos and Patrinos 2018).

**Social protection.** A cash transfer with no distortions has an MVPF
of 1, the natural benchmark. Large transfers in rural Kenya produced a
local multiplier of 2.5 with little inflation (Egger et al. 2022 †); that
is an *output* multiplier, which belongs in the macro layer, not a
welfare ratio to be added to a CBA.

**Water, sanitation and resilience.** Global benefit-cost ratios are 5.5
for sanitation, 2.0 for drinking water and 4.3 combined (Hutton 2013).
The Global Commission on Adaptation reports that USD 1.8 trillion over
2020–2030 could yield USD 7.1 trillion of net benefits, with ratios of
2–10. These are global averages: priors and bounds, not country
parameters.

**General equilibrium and macro links.** Farrow and Rose (2018) argue
that modern computable general equilibrium models have narrowed the gap
between partial- and general-equilibrium welfare measures. In CCDRs,
sector models feed MANAGE and MFMod, and Argentina's CCDR pairs MFMod
with CPAT. UK transport guidance adds "wider economic impacts" such as
agglomeration (DfT 2025). The practical architecture is two-layered:
sector CBA computes welfare, and a macro-fiscal model receives the
investment path (scaled by efficiency), the market-productivity part of
benefits as a return, and the fiscal flows. Non-market benefits stay in
the welfare ledger so they are not counted again in GDP. General
equilibrium corrections are warranted only when a programme is large,
markets are distorted or network effects are plausible. Step 11 follows
this design.

## B.11 What is settled and what is not

**Table B3. Synthesis**

| Topic | Settled | Contested | Gap in World Bank and IMF practice | Upgrade |
|----------------------|------------------------------|------------------------------|------------------------------|--------------------|
| Decision rule | Value per net public dollar against λ | Size of λ; whether it is about 1 after redistribution | Appraisal uses ENPV with λ = 1 and no fiscal ledger | Step 6 |
| Counterfactual | Measure against what would happen anyway | Measuring deadweight | The rationale test is qualitative | Step 4 |
| Revenue returns | Transfers in CBA; worth λ − 1 extra to the budget | Induced tax in low-income countries | Fiscal NPV not reported with ENPV | Steps 5, 9 |
| Discounting and carbon | Social rate between g and 2g; 2024 shadow price | Time preference or opportunity cost; target- or damage-based carbon | SISEPUEDE discounted ad hoc; NemoMod pre-discounted | Step 2 |
| Technical efficiency | Large gaps; frontier tools exist | Mapping scores to project haircuts | Scores not used in appraisal or macro links | Step 3 |
| Low capacity | Haircut and phase; maintenance first | Whether inefficiency lowers marginal returns | No standard low-capacity rules | Low-capacity rules |
| Capital and current | Annualise; fund recurrent costs | Size of recurrent coefficients | Reviews report capital shares, not life-cycle upkeep | Step 7 |
| PPPs and PPAs | No free fiscal space; liabilities are debt-like | DSA treatment; credit for self-financing assets | The DSA's 35% shock is coarse; utility debt outside public debt | Step 8 |
| Allocative frontier | Rank by value per public dollar; knapsack for lumpy items | Transfer of marginal returns | Cross-sector allocation rarely quantified | Step 10 |
| Cross-sector CBA | Common conversion factors make it feasible | Benefit transfer; review quality | No common metric across sectors | Sector cards |
| Macro link | Sector CBA plus macro-fiscal model | General-equilibrium corrections | Sector returns not passed to DIG-type models | Step 11 |


# Appendix C. World Bank and IMF practice

## C.1 World Bank: from Public Expenditure Review to Public Finance Review

The Bank's first expenditure-review framework assessed the level and
composition of spending (Pradhan 1996), and Campos and Pradhan tied
budget institutions to "allocative and technical efficiency". Since
2024 the Public Expenditure Review has been replaced by the **Public
Finance Review** (PFR), which adds a revenue chapter; "mounting fiscal
and debt challenges have led the World Bank to elevate PFRs to one of
our core mandatory diagnostics" (World Bank PFR brief). The 2024
guidance organises a PFR into macro-fiscal, revenue and expenditure
sections; the expenditure chapter "should evaluate the level and
composition of expenditure to inform policy changes for achieving
development goals efficiently while maintaining fiscal sustainability"
(World Bank 2024a †).

The Fiscal Policy unit supports it with **PFR Fundamentals** how-to
notes (2024–2026) on spending efficiency, budget rigidity, cyclicality,
tax potential, the public wage bill (benchmarked with BOOST), policy
recommendations, tax expenditures, potential fiscal savings and fiscal
multipliers; the multipliers note proposes MFMod for country-specific
values (†). Country practice follows the template. Malawi's review
analyses "the allocative, technical efficiency, and equity of sectoral
public expenditures" for five sectors; a Gambia review emphasised
technical efficiency and, "to a lesser extent, allocative efficiency
within sectors" (†); Belize's 2024 review, a small-state precedent,
applies the Herrera–Olaberria budget-rigidity measure.

## C.2 Herrera's spending-efficiency work

Santiago Herrera, a World Bank Lead Economist and former Deputy Minister
of Finance and Budget Director of Colombia, is the main Bank author of
cross-country efficiency benchmarking (Table C1).

**Table C1. Herrera's spending-efficiency work**

| Work | Method and coverage | Main findings |
|------------------------------|------------------------------|------------------------------|
| Herrera and Pang (2005) | Free disposal hull (FDH) and data envelopment analysis (DEA) for health and education; 140 countries, 1996–2002 | Developing countries score 0.85–0.95 in output efficiency; secondary sources report about 0.8 for education and 0.9 for health † |
| Herrera and Ouedraogo (2018) | FDH and DEA, input and output efficiency; education, health, infrastructure; 175 countries, 2006–16 | Efficiency falls with spending and with the public-to-private financing ratio; capital-spending efficiency rises with regulatory quality and falls with corruption; "no causality may be inferred" |
| Herrera, Isaka and Ouedraogo (2025) | FDH, DEA and bootstrapped variants; 195 countries, 2010–2020 | Developing countries least efficient in infrastructure, moderate in education, better in health; efficiency falls with spending, rises with governance |
| PFR Fundamentals: Spending Efficiency (2024) | "The World Bank's comprehensive public expenditure efficiency tool": FDH, DEA, bootstrapped and conditional variants, stochastic frontiers, a composite score | Details differ between summaries † |
| PFR Fundamentals: Potential Fiscal Savings (Herrera and Isaka) | Actual spending against a structural benchmark "expected from long-term factors that policymakers don't directly control"; wage bill, pensions, capital, goods and services, social protection | Montenegro: about 2.8% of GDP of wage bill attributed to non-structural factors † |
| Herrera and Olaberria (2020); Herrera, Kouame and Mandon (2019) | Budget rigidity in Latin America; fiscal procyclicality | |

This work measures **technical efficiency** (distance to a frontier) and
**excess spending** (the gap to a structural benchmark). None of it, as
far as the searches found, estimates the marginal *social* return by
sector that cross-sector allocation needs. The negative link between
efficiency and spending does suggest diminishing returns, so frontier
slopes could approximate marginal returns (Option B2 in Appendix F).
The official tool's variables and peer rules are unverified; obtaining
its code from the Fiscal Policy unit would let the layer reproduce its
scores.

## C.3 BOOST, PEFA and public investment management

**BOOST** is "a Bank-wide collaborative effort launched in 2010" that
pulls transaction-level budget data from treasury systems, with "active
engagements in over 90 developing countries" and "over 40 BOOST
datasets" published (†). It holds approved, revised and executed amounts
by administrative, economic and functional classification, sometimes
also by programme, geography and funding source. The data are not
harmonised across countries, and licences vary (Brazil's prohibits
commercial use). A 2026 OECD note took water-sector inputs from BOOST
and observed that allocative efficiency in water and sanitation has had
"more limited" attention than technical efficiency (OECD 2026). No
harmonised cross-country BOOST was found, so the layer should assume
country extracts plus a crosswalk to COFOG and GFS economic codes, with
the unmappable remainder flagged.

**PEFA.** Indicators PI-1 and PI-2 measure aggregate and compositional
budget outturn against the approved budget and can be computed from
BOOST (PEFA 2016); the scoring thresholds were not re-checked (†). The
Bank's 2010 diagnostic sets eight "must-haves" for public investment
management, from guidance and screening through appraisal, selection,
implementation and operation to evaluation (Rajaram et al. 2010); its
questions were folded into PEFA PI-11. The 2020 *PIM Reference Guide*
is "not a rulebook" (Kim, Fallov and Groom 2020). PEFA Climate (2024)
adds 14 climate indicators, including climate-related liabilities.
Climate budget tagging and climate expenditure reviews track spending;
they do not measure returns.

## C.4 Project appraisal and portfolio tools

Three documents set the Bank's appraisal conventions: the three
questions (Appendix B.2), the 2016 discounting note and the 2024 shadow
price of carbon (Appendix B.4). The *Handbook on Economic Analysis of
Investment Operations* combines financial, economic and fiscal views.

- **Infrastructure Prioritization Framework** (Marcelo et al. 2016): for
  many small projects where full CBA is infeasible. It builds a
  social-environmental index and a financial-economic index, plots
  projects on a plane and imposes the sector budget. Piloted in Vietnam
  and Panama and adapted by Ukraine in 2023, it is the Bank's main
  bridge between project returns and a budget envelope.
- ***Beyond the Gap*** (Rozenberg and Fay 2019): moves the debate "from
  spending more to spending better". Needs run from 2% to 8% of GDP a
  year to 2030 and a policy mix meets the goals at 4.5%; a steady flow
  of maintenance is "a necessary condition", and good maintenance cuts
  life-cycle costs by more than 50%.
- **CCDRs** count only the incremental cost of climate action: USD 574
  billion a year (2.8% of GDP) for low- and middle-income countries
  excluding China. More than 80% of CCDRs since FY22 used MFMod, MANAGE
  or ENVISAGE.
- **Public-investment multipliers**: across 129 countries, 1% of GDP of
  public investment raises output by about 1.1% after five years, and up
  to 1.6% when spending is efficient and fiscal space ample (Adarov,
  Clements and Jalles 2024; World Bank 2024c).

## C.5 Sector tools

The Bank's sector tools come closest to quantified allocative efficiency,
but each stays inside its sector:

- **Health:** HIPtool allocates spending across interventions "to
  maximize DALYs averted" using DCP3 data; Optima has been used for HIV
  in 23 countries (†).
- **Education:** learning-adjusted years of schooling (Filmer et al.
  2018) and the "Smart Buys" (GEEAP 2023).
- **Social protection:** ASPIRE indicators of coverage, incidence and
  adequacy.
- **Roads:** HDM-4 and RONET for maintenance against new works
  (Archondo-Callao 2008).
- **Agriculture:** moving budget shares from private-good subsidies to
  public goods raises rural incomes (López and Galinato 2007; Goyal and
  Nash 2017).

## C.6 IMF diagnostics and spending reviews

**Efficiency diagnostics.** PIE-X relates the public capital stock to
indicators of infrastructure access and quality, scoring countries
between 0 and 1 by distance to the frontier; the 2015 paper covers 134
countries and finds the 30% average gap (IMF 2015). PIMA assesses 15
institutions across planning, allocation and implementation; the 2018
update gives more weight to maintenance, procurement and independent
review (IMF 2018b). It had been applied in 82 countries, including 37
low-income developing countries; C-PIMA (2021) adds five climate
institutions and had been carried out in more than 50 countries by
October 2024 (IMF 2025b). Ignoring inefficiency understates the growth
effect of capital (Crivelli 2017).

**Spending reviews and reallocation.** The October 2025 *Fiscal
Monitor* ("Spending Smarter") is the closest recent quantification of
cross-sector reallocation, and cites Herrera's work. It finds efficiency
gaps of about 30–40%, largest in infrastructure and R&D, and says
governments could get "one-third more value". Moving 1% of GDP from
government consumption to infrastructure raises output by about 1.5% in
advanced economies and 3.5% in emerging and developing economies over
about 25 years; reallocation plus efficiency could raise their GDP by
about 11% without more spending; about a third of spending is "locked
in" (IMF 2025a). Earlier work found that public investment raises output
more with slack and high efficiency, and that efficient debt-financed
projects can leave debt ratios unchanged (IMF 2014). The IMF's
spending-review note sets four stages (design; identifying savings;
deciding what enters the budget; implementation) and stresses
finance-ministry oversight (Doherty and Sayegh 2022). SDG costing
benchmarks cost drivers against strong performers; extra needs for 2030
are 18.7 points of GDP in Rwanda, 21.3 in Benin, 6.4 in Vietnam, 5.6 in
Indonesia and 11.5 in Guatemala (Gaspar et al. 2019).

## C.7 The DIG family and GIMF

These are the models the team's tool re-implements in simplified form
(Appendix D):

- **DIG** (Buffie et al. 2012). Public investment builds effective
  capital scaled by an efficiency parameter $s$. Absorptive capacity
  works as cost overruns that rise with the speed of the push.
  Recurrent costs are partly recovered by user fees set as a multiple of
  recurrent costs. A gradual tax-and-transfer reaction closes the fiscal
  gap, and three kinds of debt are tracked. Scaling up pays for itself
  only when effective returns are high, fees recover enough and
  adjustment is timely. Applications set fees at 50% of recurrent costs
  (Guinea), efficiency at 0.35–0.5 with 8% depreciation (Berg et al.
  2013), and net returns of 20–25% in low-efficiency low-income
  countries. A review of more than 65 applications finds that outcomes
  hinge on efficiency, the return, the financing and revenue capacity,
  and favours gradual scale-ups (Gurara, Melina and Zanna 2019).
  DIG-Labor adds segmented labour markets and lets maintenance lower
  depreciation (†); human-capital investment outperforms infrastructure
  in the long run, but only after 15 years or more (Buffie et al. 2020).
- **DIGNAR** (Melina, Yang and Zanna 2016) adds resource revenue and a
  resource fund; a smoothed investment path buffered by the fund is more
  stable than spending as revenue arrives.
- **DIGNAD** (Marto, Papageorgiou and Klyuev 2018) adds disasters and a
  costlier but more resilient adaptation capital stock. In Vanuatu,
  building resilience in advance lowers debt-distress risk at lower
  donor cost. The IMF runs it through an Excel toolkit (Aligishiev,
  Ruane and Sultanov 2023). For Dominica, adaptation raises long-run
  output, private investment and tax revenue (Fernandez-Corugedo,
  Gonzalez-Gomez and Guerson 2023).
- **GIMF** (Kumhof et al. 2010) is a multi-country model in which
  government investment builds infrastructure capital and government
  consumption is unproductive. Its key investment parameter is the
  output elasticity of public capital: 0.17 for core infrastructure in
  one IMF baseline, against meta-analytic values of 0.083 in the short
  run and 0.122 in the long run (Bom and Ligthart 2014).

**Table C2. How the models treat public investment**

| Feature | DIG, DIGNAR, DIGNAD | GIMF |
|------------------|------------------------------|------------------------------|
| Efficiency | $s$, the share of spending that becomes capital; DIGNAR lowers it with scale; DIGNAD has separate stocks | Scale the investment shock, or lower the elasticity |
| Return | Net return $R$ (20–25% in low-income calibrations), or elasticity $\psi = (R + \delta)z/Y$ | Output elasticity of public capital |
| User fees | Multiple of recurrent costs (Guinea 0.5) | No native block |
| Recurrent cost | Proportional to the capital stock; maintenance lowers depreciation (DIG-Labor) | Government consumption |
| Fiscal rule | Gradual tax and transfer adjustment, optional delay | Deficit rule with structural and cyclical terms |
| Financing | Concessional, external commercial and domestic debt; grants; resource fund | Deficit financing |

The equation forms in Table C2 are reconstructions consistent with the
papers' stated features, not checked line by line.

## C.8 PPPs and debt sustainability

PPPs sit outside these models. The IMF and World Bank PPP Fiscal Risk
Assessment Model (PFRAM, 2016; version 2.0, 2019) produces a debt
analysis with and without PPP projects, sensitivities and a risk matrix.
The 2018 LIC-DSF's contingent-liability stress adds 35% of the PPP
capital stock to public debt when that stock exceeds 3% of GDP, plus a
2%-of-GDP shock for state enterprises (IMF and World Bank 2017); Ghana's
DSA, for example, adds 1.44% of GDP for PPPs. A 2026 review is under
way, with the revised framework expected in summer 2027. The 2017
guidance has a realism tool for the investment–growth link, but no
verified IMF document credits an investment's own fiscal returns in DSA
projections: an open question for the review.

## C.9 Where practice is thinnest

- **Cross-sector allocative efficiency is rarely quantified.** The PFR
  asks the question, but its tools measure technical efficiency and
  excess spending, and the sector tools optimise within sectors.
- **Capital and recurrent spending are analysed apart**, and rarely
  linked to asset stocks and life-cycle upkeep.
- **Economic and fiscal returns are not reported together**, and project
  pipelines are not linked to debt paths.
- **Budget data are not harmonised across countries.**

The upgrades target these four gaps.

# Appendix D. The team's macro-fiscal tool and investment-needs model

The combined macro-fiscal tool lives in the team's `new-ai-tools`
repository (`MacroFiscalModels/`, with its method note
`MacroFiscalModels_Method_v0_1.md`); neither the CPAT-AI nor the
CPAT-CDPM repository contains GIMF, DIGNAD or DIGNAR code.

## D.1 MacroFiscalModels

**Table D1. Components of the macro-fiscal tool**

| File | Role |
|------------------------|------------------------------|
| `gimf_lite.py` | One-country GIMF. Climate inputs: public investment (`ig_extra`), private investment (`IX`), net energy saving as a value-added gain (`sav`), debt-financed share (`dfs`), spending that builds no capital (`g_extra`), earmarked revenue (`rev_extra`). Parameters include `psi` 0.25, `Rg` 0.15, `s` 0.7 |
| `dignad_lite.py` | DIGNAD with savers and hand-to-mouth households; standard and adaptation capital (premium `mu_a` 0.25); efficiency `s` 0.6; `Rg` 0.20; grant, concessional and commercial financing; programme inputs `prog`, `prog_bbb`, `prog_taper`, `prog_spend`, `rev`. With resource rents it becomes DIGNAR-lite |
| `lic_dsf.py` | LIC-DSF-lite (2018 framework); coefficients from memory, still to be checked |
| `nmim_bridge.py` | NMIM to the models: public spending split into capital and current; private investment; savings; power emissions; cost of capital |
| `calibration.py` | $s$ = 1 − gap, with the gap from PEFA PI-11 (score 1 → 40%, score 4 → 13%) or IMF (2015) by income group; `Rg` 20/17/15/10% from low to high income; borrowing cost = private-creditor rate less 3 points, bounded 3–8%; depreciation 7% (private) and 4% (public); model choice rule |
| `integrated.py` | Dashboard → NMIM → price feasibility → GIMF-, DIGNAD- or DIGNAR-lite → LIC-DSF-lite, for 186 countries |

## D.2 The investment-needs model and the dashboard

The global investment-needs method (195 economies) annualises capital
with a capital recovery factor under three lenses: (a) market WACC with
savings; (b) the World Bank's 6% with savings; (c) as (b) plus local
air-pollution co-benefits, with carbon at the shadow price as a memo
item. A PIMA adjustment applies to the public share only,
$I^{PIMA} = I\left\lbrack (1 - \pi) + \pi/(1 - gap) \right\rbrack$. BOOST
capital execution (104 economies) and PEFA PI-12.2 are reported but not
used in any formula. NMIM v0.2 (186 countries, 2024–2050) adds the "who
pays" typology in Table D2. Shares depend on cost recovery, the cost of
capital, market structure and fossil subsidies. Direct budget need is
P1 plus 30% of P4. Asset lives are 25 years (generation, buildings,
industry), 40 (grids) and 12 (vehicles).

**Table D2. NMIM's "who pays" typology**

| Type | Financed by | Fiscal role |
|---------------------|------------------------------|------------------------------|
| P1 Pure public | Taxes | Direct budget cost |
| P2 Regulated utility | Tariffs | Contingent (utility debt, arrears) |
| P3 Contracted revenue | PPAs, contracts for difference, concessions | Contingent (take-or-pay, guarantees, currency) |
| P4 Viability gap | Market revenue plus a public top-up | Direct for the top-up |
| P5 Pure private | Investors, households | None, beyond policy |

The Tax and Macro-Fiscal Dashboard has a "Can they build it?" block with
the BOOST capital execution rate, the PEFA PI-11 score and PEFA PI-12.2,
plus PEFA PI-10.3 (contingent liabilities). BOOST therefore already
enters the tool chain, but no formula uses it.

## D.3 Known limitations

- Energy savings enter GIMF-lite as a value-added gain, though for
  imported fuel they are a terms-of-trade gain; they drive most of
  Kenya's long-run GDP gain.
- GIMF-lite countries show a median +7.7% of GDP by 2050 against +0.7%
  for DIGNAD-lite countries, because only GIMF-lite has the savings
  channel.
- Utility (P2) investment enters as private investment, so state-utility
  debt is outside public debt.
- Five of 66 low- and lower-middle-income ratings worsen with the
  programme.

The tool's TODO list already asks for what the upgrades deliver: the
energy-savings channel in DIGNAD-lite (item 1, "most important of the
four"); a return by sector (2); absorptive-capacity costs (3); the
efficiency-return switch (4); fuller efficiency, including "execution
rates (BOOST) as a separate leak" (8); tariff revenue against public
return, with utility debt as a contingent liability (9); savings for
DIGNAD and DIGNAR countries (10); and the economic cost of tariff rises
(16).

## D.4 Issues across the tools and their fixes

**Table D3. Issues across SISEPUEDE, NMIM and the macro tool**

| Issue | Where | Consequence | Fix |
|------------------------------|------------------------------|------------------------------|------------------------------|
| CBA export undiscounted; rate ad hoc (7%, 5%) | SISEPUEDE output | Results not comparable | Discount once at 6% (step 2) |
| Power costs pre-discounted at an unknown rate | NemoMod series mapped to power capex and opex | Discounted once or twice | Re-derive from capacity × unit cost (step 2) |
| Straight-line capital in some factors | Electric-vehicle premium; levelised factors | Capital looks cheaper | Capital recovery factors (step 7) |
| Technical cost is not gross capital; mode shift uncosted | Technical-cost lines | No capital and running-cost split | Capital share and asset life (step 1) |
| No payer, no fiscal flows | SISEPUEDE; bridge | No fiscal view | Tags and ledger (steps 1, 5) |
| Opposite sign conventions | CBA file against abatement-cost file | Silent sign errors | Unit test (Phase 1) |
| Annuity-due factor in CPAT power, end-of-year in NMIM | CPAT power method; NMIM | Annual charge differs by $1/(1 + r)$ | End-of-year for fiscal flows (step 7) |
| Carbon excluded from headline, used in waste appendix | SISEPUEDE LAC study | Inconsistent benefits | Carbon switch and memo line (step 2) |
| Utility debt outside public debt | `nmim_bridge.py` | Fiscal risk understated | Contingent liabilities to LIC-DSF-lite (step 8) |
| Energy savings only in GIMF-lite | `gimf_lite.py` | 7.7% against 0.7% GDP gap is an artefact | Pass savings to DIGNAD-lite (step 11) |
| BOOST execution reported, not used | Dashboard | Execution and efficiency conflated | Execution as delay (step 3) |
| Two efficiency conventions | NMIM cost uplift against macro $s$ | Double counting risk | Money in, assets out (step 3) |
| Return by income group, not sector | `calibration.py` | Grids and land use earn the same | Sector returns from market-output benefits (step 11) |
| No absorptive capacity | Macro models | Front-loaded programmes overstated | Scale-up cap and cost curve (steps 10, 11) |
| Interaction weights do not match runs | SISEPUEDE post-processing | Double counting across transformations | Family exclusivity; leave-one-out check (step 10) |
| Currency and price bases differ | SISEPUEDE 2019 PPP; CPAT market dollars; CCDR tables at 6% | Mis-scaled ratios | Harmonisation (Phase 0) |
| No PPA or PPP liabilities anywhere | CPAT treats PPAs only as must-run shares | Hidden debt missed | Financing routes (step 8) |


# Appendix E. The worked example in full

The script `sids_worked_example.py` and its two output files
(`sids_worked_example_results.csv` and
`sids_worked_example_sensitivity.csv`) are in the folder alongside this
note. The script was re-run for this version and its outputs are
unchanged. Money is in USD million at constant prices; year 0 is
construction and years 1–25 are operation. Figures are rounded.

## E.1 Assumptions

**Table E1. The island and the plant**

| Assumption | Value | Source or status |
|------------------------------|------------------------------|------------------------------|
| Demand; diesel share | 300 GWh a year; 100% | Illustrative; anchored on St Lucia (399 GWh, 99% diesel) and St Vincent (136 GWh) |
| GDP; public debt | USD 2.0 billion; 85% of GDP | Illustrative |
| Plant | 60 MW solar, 120 MWh battery; USD 120 million (6% of GDP) | Illustrative |
| Solar capex | USD 1,200 a kW | IRENA global USD 691 × the 1.5–1.7 island premium implied by ASPIRE tariffs |
| Battery capex | USD 350 a kWh | Illustrative (IRENA global about USD 140 × island premium) |
| Integration and soft costs | 5% of capex | Illustrative |
| Capacity factor; delivered share | 18%; 95% | Illustrative (ASPIRE tariffs imply about 16.5%) |
| Energy displaced | 89.9 GWh a year (30% of diesel generation) | Derived |
| Upkeep; life; battery replacement | 1.5% of capex (USD 1.8 million a year); 25 years; year 15 at 60% of battery cost (USD 25.2 million) | Illustrative |
| Brent | USD 80 central; 60 and 110 | EIA October 2026 outlook as reported † |
| Diesel crack; delivery premium; efficiency | USD 25 a barrel; USD 0.15 a litre; 3.9 kWh a litre | Illustrative; efficiency from a vendor guide † |
| Avoided cost (fuel plus variable upkeep USD 0.02 a kWh) | USD 0.228 a kWh, USD 20.5 million a year (1.0% of GDP) | Derived |
| Emissions factor | 0.686 t a MWh (61.7 kt a year avoided) | IPCC defaults † |
| Shadow price of carbon | World Bank low path, USD 40 in 2020, +2.25% a year; high path twice that | World Bank 2024b (2017 dollars) |
| Social rate; government borrowing rate | 6%; 8% | World Bank 2016; 8% illustrative † |
| λ | 1.2 base; 2.0 stress; cash-short profile 2.0 in years 1–7, then 1.2 | Auriol and Warlters 2012; profile illustrative |
| Fiscal capture of fuel savings θ | 0.5 base; 0 and 1 | Policy parameter |
| Fuel excise on power diesel | 0 | Illustrative (often exempt) |
| Financiers | All non-resident | Illustrative |
| Reference rate for the present value of debt | 5% | Candidate value † |

**Table E2. Financing routes**

| Route | Financing | Terms |
|-------------|------------------------------|------------------------------|
| R1a | Budget, commercial loan | 8%, 7-year annuity: the only market tenor on offer |
| R1b | Budget, commercial loan | 8%, 25-year annuity: for comparison only |
| R2 | Budget, concessional (IDA- or RST-type) | 1.5%, 30 years, interest only in years 1–5 |
| R3 | Private producer, 25-year PPA, no guarantee | Cost of capital 11% |
| R4 | Private producer, 25-year PPA, World Bank or MIGA guarantee | Cost of capital 8.5% |

The plant's levelised cost is USD 0.134 a kWh at 6% (0.153 at 8%), far
below the USD 0.228 it avoids. Its financing-neutral economic NPV stays
positive down to Brent at about USD 22.

## E.2 Value

**Table E3. Value by route (USD million; present value at 6% except the
fiscal NPV at 8%; Brent USD 80; θ = 0.5)**

| Route | World Bank ENPV | Financing premium | Island ENPV | With carbon (low) | W | F | MVPF | NB, λ = 1.2 | NB, λ = 2.0 | NB, cash-short | Fiscal NPV at 8% |
|-------------|-------------:|----------------:|-------------:|-------------:|----------:|----------:|-------------:|----------:|----------:|-----------------:|-------------:|
| R1a | 108 | 9 | 100 | 146 | 131 | 31 | 4.18 | 93 | 68 | 28 | −38 |
| R1b | 108 | 24 | 85 | 131 | 131 | 46 | 2.82 | 75 | 38 | 63 | −38 |
| R2 | 108 | −57 | 165 | 212 | 131 | −34 | Pays for itself | 172 | 200 | 197 | +33 |
| R3 | 108 | 60 | 49 | 95 | 131 | 82 | 1.59 | 32 | −34 | 3 | −69 |
| R4 | 108 | 29 | 80 | 126 | 131 | 51 | 2.55 | 69 | 28 | 51 | −43 |

The carbon value is USD 47 million on the low path and USD 93 million
on the high path. The equivalent annual fiscal cost is USD 2.5 million
(R1a), 3.6 (R1b), −2.7 (R2), 6.4 (R3) and 4.0 (R4).

## E.3 Debt and liabilities

**Table E4. Debt and liabilities by route**

| Route | Headline debt added (% of GDP) | Debt after (% of GDP) | New debt, present value at 5% (% of GDP) | Contract value at 8% (% of GDP) | Contract value / capex | DSA PPP stress (% of GDP) | Net fiscal liability (USD m) | Net external liability (USD m) | Grant element at 6% |
|-------------|---------------:|---------------:|---------------:|---------------:|---------------:|---------------:|----------------:|----------------:|---------------:|
| R1a | 6.0 | 91.0 | 6.7 | 0 | | 0 | 38 | −71 | −7% |
| R1b | 6.0 | 91.0 | 7.9 | 0 | | 0 | 38 | −71 | −20% |
| R2 | 6.0 | 91.0 | 3.6 | 0 | | 0 | −33 | −142 | 48% |
| R3 | 0 | 85.0 | 0 | 8.9 | 1.48 | 2.1 | 69 | −41 | |
| R4 | 0 | 85.0 | 0 | 7.6 | 1.27 | 2.1 | 43 | −66 | |

The liabilities are present values at 8%. The net fiscal liability is
minus the fiscal NPV. A negative net external liability means the
payments for the plant are smaller, in present value, than the fuel
imports it avoids: every route cuts external liabilities, which is the
case for crediting such assets "net of savings" in a DSA, but only where
the savings are contractually secured.

## E.4 The trap

**Table E5. Year-1 payments against the avoided fuel bill**

| Route | Year-1 payment (USD m) | USD a kWh | Brent at which payment = avoided cost | Below the fuel bill at Brent USD 60 / 80 / 110? |
|------------------------------|---------------------:|------------:|-----------------------------:|------------------------------|
| R1a (debt service 23.0 + upkeep 1.8) | 24.8 | 0.276 | USD 110 | no / no / equal |
| R1b | 13.0 | 0.145 | USD 29 | yes / yes / yes |
| R2 (interest only in years 1–5; 7.6 a year from year 6) | 3.6 | 0.040 | Any price | yes / yes / yes |
| R3 (PPA tariff) | 16.7 | 0.186 | USD 54 | barely / yes / yes |
| R4 (PPA tariff) | 14.2 | 0.159 | USD 37 | yes / yes / yes |

The avoided fuel bill is USD 17.6 million, 20.5 million and 24.8 million
a year at Brent USD 60, 80 and 110.

**Table E6. Net cash to the budget or utility (USD million)**

| Route | θ = 0.5, each of years 1–7 | θ = 0.5, worst year | θ = 0.5, payback | θ = 1, years 1–7 | θ = 1, payback |
|-------------|-------------------------:|------------------:|----------------|---------------:|----------------|
| R1a | −14.6 (−102 over 7 years, 5.1% of GDP) | −16.8 (year 15) | Year 23 | −4.4 | Year 9 |
| R1b | −2.8 | −28.0 (year 15) | Never | +7.4 | Never negative |
| R2 | +6.6 (years 1–5), +2.6 (years 6–7) | −22.6 (year 15) | Never negative | +16.9 / +12.9 | Never negative |
| R3 | −6.4 | −6.4 | Never | +3.8 | Never negative |
| R4 | −4.0 | −4.0 | Never | +6.2 | Never negative |

Year 15 carries the USD 25.2 million battery replacement on the public
routes. In R2, debt service of USD 5.8 million a year continues in years
26–30, after the asset retires.

**Table E7. Switching values**

| Route | λ at which NB = 0 (the MVPF) | θ at which the plant pays for itself | Brent at which year-1 payment = avoided cost |
|-------------|---------------------------:|-----------------------------:|-----------------------------:|
| R1a | 4.18 | 0.62 | USD 110 |
| R1b | 2.82 | 0.68 | USD 29 |
| R2 | Pays for itself | 0.37 | Any price |
| R3 | 1.59 | 0.81 | USD 54 |
| R4 | 2.55 | 0.70 | USD 37 |

## E.5 Sensitivity

**Table E8. Sensitivity by route (θ = 0.5 unless stated)**

| Case | R1a | R1b | R2 | R3 | R4 |
|--------------------------|------------------|------------------|------------------|------------------|------------------|
| ENPV at Brent USD 60 / 80 / 110 | 62 / 100 / 155 | 47 / 85 / 140 | 128 / 165 / 221 | 12 / 49 / 104 | 43 / 80 / 135 |
| MVPF at Brent USD 60 / 80 / 110 | 2.25 / 4.18 / 44.9 | 1.73 / 2.82 / 8.54 | Pays for itself | 1.11 / 1.59 / 2.91 | 1.61 / 2.55 / 6.75 |
| NB (λ = 1.2) at Brent USD 60 / 80 / 110 | 53 / 93 / 154 | 34 / 75 / 136 | 131 / 172 / 233 | **−9** / 32 / 93 | 29 / 69 / 130 |
| ENPV at capex −30% / base / +30% | 148 / 100 / 51 | 138 / 85 / 31 | 194 / 165 / 136 | 113 / 49 / **−15** | 134 / 80 / 25 |
| MVPF at capex −30% / base / +30% | Pays / 4.18 / 1.64 | Pays / 2.82 / 1.31 | Pays (all) | 7.14 / 1.59 / **0.89** | Pays / 2.55 / 1.24 |
| MVPF at θ = 0 / 0.5 / 1 (ENPV unchanged) | 1.61 / 4.18 / pays | 1.48 / 2.82 / pays | 2.71 / pays / pays | 1.23 / 1.59 / pays | 1.44 / 2.55 / pays |
| Fiscal NPV at 8%, θ = 0 / 0.5 / 1 | −147 / −38 / 71 | −147 / −38 / 71 | −76 / 33 / 142 | −178 / −69 / 41 | −152 / −43 / 66 |

**Table E9. The PPA route by private cost of capital**

| Cost of capital | 7.0% | 8.5% | 11.0% | 13.0% |
|------------------------------|------------:|------------:|------------:|------------:|
| PPA tariff (USD a kWh) | 0.143 | 0.159 | 0.186 | 0.208 |
| ENPV | 97 | 80 | 49 | 22 |
| MVPF | 3.87 | 2.55 | 1.59 | 1.21 |
| NB at λ = 1.2 / 2.0 | 90 / 63 | 69 / 28 | 32 / −34 | 1 / −86 |
| Year-1 net cash | −2.6 | −4.0 | −6.4 | −8.5 |
| Contract value at 8% (% of GDP) | 6.9 | 7.6 | 8.9 | 10.0 |

**Table E10. The commercial loan by tenor (8%)**

| Tenor | 7 years | 15 years | 25 years |
|--------------------------|------------:|------------:|------------:|
| Year-1 payment (USD a kWh) | 0.276 | 0.176 | 0.145 |
| ENPV / fiscal NPV at 8% | 100 / −38 | 92 / −38 | 85 / −38 |
| NB at λ = 1.2 / cash-short | 93 / 28 | 84 / 59 | 75 / 63 |
| Year-1 net cash | −14.6 | −5.6 | −2.8 |

At 13% the PPA tariff is still below the avoided cost at Brent USD 80,
but above it at USD 60 (USD 0.196 a kWh). An earlier calculation with
slightly different assumptions (20-year PPAs, upkeep of USD 2.1
million) gave an economic NPV of USD 104 million at 6% and contract
values of 1.3–1.5 times capex, consistent with the results above.

## E.6 Further lessons

- **λ changes the go or no-go more than the ranking; carbon rescues
  marginal cases.** The switching λ equals the MVPF (1.59 to 4.18). At
  λ = 2.0 only the unguaranteed PPA fails. Carbon at the shadow price
  adds USD 47–93 million to every route without reordering them.
- **Fuel price risk is real but unpriced.** Each USD 10 a barrel moves
  the avoided bill by USD 1.45 million a year, a hedge the metrics do not
  value.
- **The unguaranteed PPA is fragile.** It fails at Brent USD 60, at
  capex +30% and at λ = 2.0.

## E.7 Caveats

- **Constant prices, nominal rates.** The 8%, 1.5% and 11% rates are
  nominal but applied to constant-price flows. This overstates financing
  costs, most for long tenors and PPAs. The carbon price is in 2017
  dollars and not inflated, which understates its value.
- **Who pays.** θ applies only to fuel savings; the plant cost falls
  wholly on the public sector because base tariffs are not raised.
- **The PPA liability is an upper bound.** It is treated as take-or-pay
  on expected output; many solar PPAs are take-and-pay with deemed
  energy.
- **The guarantee is not priced:** no fee and no expected call.
- **Benefits left out:** a foreign-exchange shadow price, the hedge
  value, local air pollution, avoided diesel capacity, solar
  degradation, demand growth, curtailment and integration costs above
  5%.
- **No delivery haircuts.** No efficiency haircut, execution delay or
  cost uplift is applied. In a low-capacity setting, an uplift on the
  public routes, but not on a competitively auctioned private producer,
  would narrow R1 and R2's lead.
- **Unverified inputs:** island capex, GDP, debt, the 8% rate, IDA
  terms, the 5% reference rate and the emissions factor.
- **DSA rules.** The 35% PPP stress applies under the 2018 LIC-DSF. A
  small island assessed under the framework for market-access countries
  faces different rules, and the 2026 review may change the treatment.
- **Timing.** There is no construction lag or interest during
  construction; concessional debt service runs to year 30, after the
  asset retires.

# Appendix F. Option B and wider upgrades to World Bank practice

## F.1 Option B: less constrained by SISEPUEDE

The PSV layer inherits SISEPUEDE's structure: one-at-a-time
transformations, physical doses and a cost module without payers. If
that proves too constraining, three alternatives carry the same
principles.

**B1. A multi-capital public-portfolio model.** This extends DIGNAD- and
GIMF-lite so that public capital has several types: energy, transport,
water, adaptation, and human capital (health and education) with a lag.
Each type carries an efficiency $s_{j}$, a return $R_{j}$ (or elasticity),
depreciation that responds to maintenance (as in DIG-Labor), a recurrent
coefficient and a user-fee share. Current spending gets its own
channels: transfers to hand-to-mouth households, and wages. Calibration
takes the starting composition from BOOST, efficiency from Herrera's
scores and PIMA, and returns from the literature and the sector cards.
The model then solves for the composition that maximises growth or
welfare under the fiscal rule and the DSA, which is the
Devarajan–Swaroop–Zou logic. It fits the tool's plan for "one model with
switches" (TODO item 5). DIG-Labor shows the human-capital channel
matters but pays off only after 15 years or more. *For:* no
project-level CBA is needed, and general-equilibrium effects (crowding
out, the real exchange rate, the fiscal reaction) are captured.
*Against:* returns by capital type are poorly identified, and the
efficiency-return ambiguity is sharper with several types.

**B2. Empirical allocative efficiency, PFR-style.** This estimates
marginal returns by function from BOOST panels and outcome data, in the
style of Fan, Hazell and Thorat, adding the slopes of Herrera-type
frontiers near each country's peers times money values of outcomes, and
Herrera and Isaka's potential savings. It would be a "PFR allocative
module" in the dashboard. It needs a cross-country panel (IMF GFS and
WEO, Bank wage-bill data), because BOOST is not harmonised. *For:*
closest to current Bank practice. *Against:* less structural;
second-stage correlations are not causal; no financing or liability
view.

**B3. Robust portfolios.** This runs robust decision-making across
futures (oil prices, disasters, growth, the cost of capital) and chooses
the portfolio with the least regret, or the highest 10th-percentile net
benefit, at each budget. It builds on SISEPUEDE's own heritage (about
1,000 futures and scenario discovery, as in Costa Rica) and adds the
discount rate and cost of capital to the uncertain inputs. B3 can wrap
either the PSV layer or B1.

**Table F1. The options compared**

| | PSV layer | B1 Multi-capital model | B2 PFR allocative module | B3 Robust portfolios |
|----------------------------|------------------------------|------------------------------|------------------------------|------------------------------|
| What it answers | Which measures to fund, by which route, within an affordable envelope | Which spending *composition* maximises growth or welfare under the fiscal rule | Where marginal returns per dollar are high or low; potential savings | Which portfolio holds up across futures |
| Data | SISEPUEDE and NMIM lines, sector cards, PIMA, PEFA, BOOST, route terms | BOOST composition, frontier scores, returns by type, macro calibration | Cross-country BOOST and GFS panels, outcomes, governance | Futures plus the layer or B1 |
| Effort | Medium (Phases 0–3) | High | Medium | Medium-high (computing) |
| Fit with World Bank practice | High: economic analysis plus a ledger and λ | Medium: IMF DIG-family style | Highest: extends PFR Fundamentals | High: *Lifelines*, CCDR practice |
| Main risk | Payer mapping; parameter transfer | Identifying returns | Correlation is not causation | Opacity; computing |

## F.2 Upgrades to World Bank practice

**Table F2. Incremental and radical upgrades**

| Idea | What changes | Data | Effort | Risk | Consistent with current guidance? |
|--------------------------|------------------------------|--------------------------|-------------------|--------------------------|--------------------------|
| **Incremental** | | | | | |
| Fiscal NPV and λ next to economic NPV in projects and PFRs | Every appraisal reports W, F, MVPF, $NB_{\lambda}$ and the cash profile | Project cost and revenue flows; λ by country | Low | Disputes over λ; gaming "pays for itself" | Yes: extends the three questions |
| One discount rate and one carbon price, applied consistently | SISEPUEDE, NMIM, CCDR and PFR numbers become comparable | 2016 rule; 2024 shadow price | Low | Restating past results | Yes: implements existing notes |
| PIMA, PEFA and BOOST haircuts, with efficiency kept apart from execution | Efficiency raises cost per asset; execution delays benefits | PI-11, PIMA, BOOST | Low-medium | Double counting if conventions slip | Yes: uses existing diagnostics |
| Whole-life costing with recurrent coefficients in PFRs | Capital shown with its upkeep and staffing tail; maintenance gap reported | BOOST goods and services; asset registers | Medium | Weak coefficients | Yes: *Beyond the Gap*; PIM must-haves |
| A register of PPAs and PPPs, with present-value liabilities in the DSA | Take-or-pay values and guarantees reported, beyond the 35% shock | Contracts; PFRAM | Medium | Data access; confidentiality | Yes: PEFA PI-10.3; PFRAM |
| Sector cards: one cross-sector metric in PFRs | Allocative efficiency measured across ministries | DCP3, learning-adjusted years, ASPIRE, HDM-4, water and resilience ratios | Medium | Benefit transfer | Partly: PFRs ask the question but have no tool |
| **Radical** | | | | | |
| λ derived from the macro and debt models | λ becomes the shadow price of fiscal space: the welfare cost of the adjustment the fiscal rule triggers per extra dollar | Macro-model runs | Medium | Model dependence | Not yet |
| DSA credit for self-financing climate assets | Liabilities backed by contractually secured savings shown net, with a register, independent valuation and ring-fenced savings | Utility accounts; contracts | Medium | Moral hazard; optimistic valuation | No: a candidate for the 2026 LIC-DSF review |
| Balance-sheet (net worth) appraisal | Capital judged by its effect on net worth, not gross debt | Asset valuations | High | Valuation error | Partly: IMF (2018a) advocates it |
| One MVPF ladder for revenue and spending | CPAT carbon tax and recycling options ranked against spending | CPAT; the layer | Low-medium | Mixing incidence and efficiency | Not yet; consistent with the MVPF literature |
| Distributional weights from CPAT's household module | Value weighted by decile | CPAT household data | Medium | Value judgements | Partly: UK practice, not Bank standard |
| AI-assisted BOOST tagging | Budget lines tagged to transformations, COFOG and climate, so actual-versus-frontier allocation is measured automatically | BOOST; tagging rules; human checks | Medium-high | Classification error; licences | Not yet; the 2026 WDR draft discusses AI for spending monitoring (World Bank 2026 †) |
| Real options and sequencing under deep uncertainty | Deployment limits, staged commitments, the value of waiting | SISEPUEDE futures | High | Complexity | Partly: *Lifelines*; Vogt-Schilb and Hallegatte |

# Appendix G. Risks, limitations and open questions

**Evidence.** All external sources were checked against abstracts,
records or summaries, not full texts. Items marked † must be checked
before outside use, including the details of the PFR spending-efficiency
tool, PEFA thresholds, the Green Book schedule, recurrent coefficients
and IDA terms (Appendix J).

**Parameters.** Four carry the most uncertainty:

- **λ** is uncertain and partly a value judgement. Only Norway's 1.2 is
  a confirmed official convention, and the Africa estimate rests on one
  general-equilibrium study.
- **Frontier scores mapped to efficiency** are a bounded prior, not a
  calibration: PIE-X gaps are distances to an output frontier, not
  shares of spending lost, and DIG applications use lower values.
- **Recurrent coefficients and additionality shares** are largely
  assumptions.
- **Benefit transfer** of the value of a statistical life, learning
  values and global ratios can be far from country truth.

**Double counting** can arise at four points: efficiency applied twice;
fees counted as benefits; energy savings in both the sector return and
`sav`; and non-market benefits passed to GDP. The conventions in steps 3,
9 and 11 and the Phase 1 tests are the guard. Under the bridge's
reporting rule, CPAT and SISEPUEDE values of the same avoided fuel or
pollution are never added.

**Model risks.** Energy savings enter the macro tool as value added
rather than as a terms-of-trade gain; the GDP gap between GIMF-lite and
DIGNAD-lite countries is partly an artefact; LIC-DSF-lite coefficients
are unverified. In SISEPUEDE, interaction weights do not match runs, and
the power model can return zeros without raising an error.

**Gaming.** "Pays for itself" claims invite optimism; the deworming
debate shows how contested such estimates can be. Switching values and
conservative defaults are the defence.

**Institutional and data risks.** BOOST is not harmonised and licences
vary; CCDR investment data are not formally released; CPAT is
proprietary and IMF-linked, and a reviewer has questioned the
partnership text's compatibility with the IMF and data-provider
agreements; DSA rules may change after the 2026 review.

**Open questions.**

1. Should λ be a fixed country parameter or derived from the macro
   model?
2. How can a finance ministry secure θ, the share of fuel savings the
   budget keeps, by contract?
3. Which DSA treatment of take-or-pay PPAs should the team propose to
   the 2026 review?
4. Can the Fiscal Policy unit share the spending-efficiency tool's code
   and peer rules?
5. Which recurrent coefficients should be used by asset class, pending
   Hood, Husband and Yu (2002)?
6. Should the layer sit in `new-ai-tools` or with SISEPUEDE, given that
   SISEPUEDE is open source and CPAT proprietary?


# Appendix H. Formula sheet

**Decision**

$$W_{j} = PV_{r}\left\lbrack \text{benefits to non-budget agents} - \text{their costs} \right\rbrack,\qquad F_{j} = PV_{r}\left\lbrack F_{t} \right\rbrack$$

$$ENPV_{j} = W_{j} - F_{j},\qquad MVPF_{j} = W_{j}/F_{j},\qquad NB_{\lambda,j} = W_{j} - \lambda F_{j},\qquad NB^{liq} = W - \sum_{t}^{}\frac{\lambda_{t}F_{t}}{(1 + r)^{t}}$$

Fund if $MVPF_{j} > \lambda$ (equivalently $NB_{\lambda,j} > 0$); if
$F_{j} \leq 0$, fund if $W_{j} \geq 0$; when the budget binds, rank by
MVPF.

**SISEPUEDE's cost-benefit module**

$$V_{k,t} = \left( x_{k,t}^{S} - x_{k,t}^{B} \right)m_{k}\, g_{k}^{\max(0,\, t - 8)},\qquad PV = \sum_{t}^{}\sum_{k}^{}\frac{V_{k,t}}{(1 + r)^{t - t_{0}}},\qquad u_{j} = \min\left( B_{j}/c_{j},\ u_{j}^{\max} \right)$$

**The Pigouvian gap and additionality**

$$s^{*} = \frac{e - (\lambda - 1)\, q/q'}{\lambda},\qquad B^{net} = a\, B^{gross},\qquad VG = \max\left( 0, - NPV^{priv} \right)$$

**Cost of funds and finance**

$$MCF = \frac{1 - t}{1 - t - t\,\varepsilon},\qquad\kappa = \frac{i}{1 - (1 + i)^{- n}}\cdot\frac{1 - (1 + r)^{- n}}{r},\qquad GE = 1 - \frac{PV_{r^{ref}}(DS)}{K}$$

$$ENPV_{\lambda} = PV(B - C^{res}) - (\lambda - 1)\, PV(G^{net})$$

**Annuities**

$$CRF(r,n) = \frac{r}{1 - (1 + r)^{- n}},\qquad EAC = K\, CRF(r,n) + r^{rc}K,\qquad LCOE = \frac{EAC}{E},\qquad EAFC = F\, CRF(r,n)$$

An annuity-due charge is $CRF\cdot K/(1 + r)$. The regression identity
with the investment-needs model's lens (c) is
$ENPV\cdot CRF(6\%, n) = -IC$.

**Efficiency and delivery**

$$C^{eff} = C\left\lbrack (1 - \pi) + \pi/s \right\rbrack,\qquad K_{t}^{eff} = (1 - \delta)K_{t - 1}^{eff} + s\, I_{t}^{act},\qquad I_{t}^{act} = e\left( I_{t}^{plan} + \text{backlog}_{t - 1} \right)$$

$$\Delta s_{t} = \tfrac{2}{3}(1 - s_{0})\,\text{ramp}_{t}\ \text{(reform dividend)},\qquad\psi = (R + \delta)\, z/Y\ \text{(return and elasticity)}$$

Free disposal hull input efficiency of unit $i$:
$\theta_{i} = \min_{j:\, y_{j} \geq y_{i}} x_{j}/x_{i}$, with savings
$(1 - \theta_{i})x_{i}$. Output-oriented DEA with variable returns:
$\max\eta$ subject to $\sum\lambda_{j}y_{j} \geq \eta\, y_{o}$,
$\sum\lambda_{j}x_{j} \leq x_{o}$, $\sum\lambda_{j} = 1$; the score is
$1/\eta$.

**Fiscal ledger**

$$F_{t} = \text{capex}_{t} - \text{loans}_{t} + DS_{t} + OM_{t}^{pub} + PPA_{t} + SUB_{t} - FEE_{t} - \theta SAV_{t} + XL_{t} - PIG_{t} + E\lbrack CALL_{t}\rbrack,\qquad FNPV = -\sum_{t}^{}\frac{F_{t}}{(1 + i_{g})^{t}}$$

**PPA route**

$$T = \frac{\left( K + PV(\text{replacements}) \right)CRF(WACC, n) + OM}{E},\qquad L^{PPA} = \sum_{t}^{}\frac{P_{t}^{committed}}{(1 + i_{g})^{t}},\qquad\text{premium} = L^{PPA} - K$$

DSA stress: if the PPP stock exceeds 3% of GDP, add 0.35 times the
stock to public debt.

**Maintenance**

$$OMgap_{t} = r^{rc}K_{t} - OM_{t}^{exec},\qquad W \approx m\cdot OMgap\ (m = 3\text{–}5\ \text{for roads})$$

**Carbon and distribution**

$$SPC_{t} \approx SPC_{2020}\cdot 1.0225^{\, t - 2020},\qquad w_{i} = \left( y_{ref}/y_{i} \right)^{\eta}$$

A transfer passes on distribution grounds if $w_{i} > \lambda$.

**Frontier**

$$\max_{x}\sum_{j}^{}x_{j}NB_{\lambda,j}\ \text{subject to the envelope, family, scale-up, floor and target constraints (equation 11)}$$

The reallocation gain is the net benefit of the frontier at the current
budget less that of the current BOOST allocation.

**BOOST and PEFA outturn**

$$\text{Aggregate deviation} = \left| \frac{\sum\text{actual}}{\sum\text{approved}} - 1 \right|,\qquad\text{Composition variance} = \frac{\sum_{k}\left| \text{actual}_{k} - \text{approved}_{k}\,\rho \right|}{\sum_{k}\text{approved}_{k}\,\rho},\quad\rho = \frac{\sum\text{actual}}{\sum\text{approved}}$$

# Appendix I. Parameters

Table 9 gives the layer's core parameters and Table E1 the worked
example's. Table I1 adds the macro-model defaults, literature anchors and
reference factors.

**Table I1. Macro-model defaults, literature anchors and reference
factors**

| Group | Parameter | Value | Source |
|--------------------|------------------------------|------------------------------|------------------------------|
| Macro tool (current) | DIGNAD-lite `s`, `Rg`, `mu_a`, `ig1`, `ig2` | 0.6, 0.20, 0.25, 0.06, 0.01 | `dignad_lite.py` |
| | GIMF-lite `s`, `Rg`, `psi` | 0.7, 0.15, 0.25 | `gimf_lite.py` |
| | Return by income group | 20 / 17 / 15 / 10% (low to high) | `calibration.py`, an assumption |
| | Depreciation, private and public | 7%, 4% | `calibration.py` |
| | Efficiency gap from PEFA PI-11 | Score 1 → 40%, score 4 → 13%, linear | `calibration.py` |
| DIG literature | Efficiency | 0.35–0.5 (Sub-Saharan Africa); 0.5; 0.6 | Berg et al. 2013; IMF working papers |
| | Net return on public capital (low income) | 20–25% | Berg et al. 2019 |
| | Output elasticity of public capital | 0.083 short run, 0.122 long run; 0.17 core infrastructure | Bom and Ligthart 2014; IMF |
| | User fees | 50% of recurrent cost | Guinea DIG application |
| | Depreciation | 8% | Berg et al. 2013 |
| Investment needs | Efficiency gap; public share | Advanced 13%, emerging 27%, low income 40%; public share: advanced 30%, China 50%, others 40% | IMF 2015; team's model |
| | Direct budget need | P1 + 30% of P4 | NMIM v0.2 |
| Sector conversion | Value of a statistical life | US value × (income ratio)^1.5; about 160 times income per person (80–170) | Robinson, Hammitt and O'Keeffe 2019 |
| | Learning-adjusted year | Present value of a 9% earnings gain | Psacharopoulos and Patrinos 2018 |
| | DCP3 essential package | USD 79 a person (low income), USD 130 (lower-middle), 2016 dollars | Watkins et al. 2020 |
| Reference factors | Capital recovery factor at (rate, years) | (1.5%, 25) 0.048; (4%, 25) 0.064; (6%, 25) 0.078; (8%, 7) 0.192; (8%, 25) 0.094; (8.5%, 25) 0.098; (11%, 25) 0.119; (13%, 25) 0.136; (6%, 40) 0.067; (6%, 12) 0.119 | Calculated |

# Appendix J. Sources and verification notes

**How the sources were checked.** The research could not open full
texts: the network blocked publisher and institutional sites. Every
external citation was checked against an abstract, a catalogue record,
a publisher page or a search-engine summary. Facts about the team's
tools come from files in the team's repositories, read directly. Items
marked † rest on one of the following and must be checked against the
primary text before outside use:

- a search-engine summary of a document that could not be opened;
- secondary coverage (press, a blog, or another paper citing the
  source);
- a weak source;
- standard bibliographic knowledge not re-checked in this work.

No unverified claim is presented as a fact.

**Points to note when citing.**

- **IMF (2015).** The 30% average gap and the income-group figures are
  from the paper; "twice the bang for the buck" could not be confirmed
  independently. Other IMF presentations give "27%" or "around
  one-third": presentation differences, not new estimates.
- **PFR Guidance and PFR Fundamentals.** Titles are confirmed; contents
  rest on search summaries, and two summaries of the spending-efficiency
  note disagree on its orientation and peer rules.
- **Herrera and Pang (2005).** The sector scores of about 0.8 and 0.9
  are from secondary sources.
- **Devarajan, Squire and Suthiwart-Narueput, *Reviving Project
  Appraisal*.** Catalogue records date it 1999; one gives 1995.
- **Devarajan, Swaroop and Zou (1996).** The journal version reports 43
  countries; the working paper 69.
- **SDG costing (Gaspar et al. 2019).** An average of about 15 points of
  GDP for low-income developing countries is reported in one review but
  not confirmed in another.
- **Maldives ASPIRE.** The phase-2 tariff is 10.2 or 10.9 cents in two
  Bank sources.
- **The World Bank's 6% rate.** One secondary source calls it a minimum;
  the primary note describes a range.
- **Copenhagen Consensus.** The malaria and e-procurement ratios are
  from secondary coverage.
- **DIG-Labor.** The passage on maintenance and depreciation needs
  confirmation.
- **Equation forms in Table C2** are reconstructions, not checked line
  by line.
- **LIC-DSF-lite** coefficients in the team's tool are from memory.
- **Unread numbers:** Hood, Husband and Yu's recurrent coefficients;
  PEFA scoring thresholds; the Green Book discount schedule; IDA terms.
- **The SISEPUEDE facts** come from the public code
  (`costs_benefits_ssp`, `sisepuede`), the Uganda run of October 2025,
  the CPAT–CPM methodology note and bridge deck, the FY27 work plan and
  the companion note on global investment needs. The NemoMod rate in
  the Uganda run, the currency year of its factors and the treatment of
  shifted rows for air pollution are not recorded in the files.

**Team files used.** SISEPUEDE's Uganda run (`cba_results.csv` and the
wide output, October 2025); `CPAT_CPM_Methodology_v0925.docx`;
`CPAT_CPM_bridge_map.pptx`; the FY27 work plan (with comments); the
October 2026 pathways scoping slides; *Global Investment Needs for
Climate Action: A Method Based on SISEPUEDE* (this folder); CPAT's power,
GDP and equations method notes (version 6.1); the `MacroFiscalModels`
and `InvestmentNeeds` folders and the dashboard's indicator list in
`new-ai-tools`; and the worked-example script and outputs in this
folder.

# Appendix K. Glossary

| Term | Meaning |
|------------------------------|------------------------------|
| Allocative efficiency | Spending on the right things in the right amounts: value per dollar equal across uses at the margin |
| Technical efficiency | Delivering a given output at least cost (distance to a frontier) |
| λ (marginal cost of public funds) | Welfare cost of raising USD 1 of public revenue |
| MVPF (marginal value of public funds) | Beneficiaries' willingness to pay divided by net cost to the budget, including fiscal externalities |
| W, F | Present value of net benefits to everyone but the budget; present value of net cost to the budget |
| $NB_{\lambda}$ | Net benefit adjusted for the cost of funds, $W - \lambda F$ |
| ENPV, FNPV | Economic NPV at the social rate; fiscal NPV at the government's borrowing rate |
| Viability gap | Public top-up needed to make a private investment viable |
| Additionality, deadweight | Share of benefits that would not happen without the measure; its complement |
| θ | Share of a measure's fuel savings kept by the budget or state utility |
| $s$, $e$, φ | Investment efficiency (spending to capital); execution rate (timing); output efficiency of services |
| Recurrent coefficient | Upkeep and staffing cost per dollar of capital a year |
| CRF, EAC | Capital recovery factor; equivalent annual cost |
| P1–P5 | NMIM's "who pays" types (Table D2) |
| PPA, IPP | Power purchase agreement; independent power producer |
| Take-or-pay, take-and-pay | Payment regardless of offtake; payment for energy delivered (plus deemed energy) |
| Transformation, strategy | A SISEPUEDE policy lever; a bundle of levers run against the baseline |
| Technical cost | SISEPUEDE's cost of carrying out a transformation, mixing capital, operating and avoided costs |
| NemoMod | The least-cost power model inside SISEPUEDE |
| PIMA, C-PIMA, PIE-X | IMF public investment management assessment; its climate module; the IMF's public investment efficiency frontier |
| PEFA PI-1, PI-2, PI-10.3, PI-11 | Budget outturn; composition outturn; contingent liabilities; public investment management |
| BOOST | World Bank budget microdata: approved, revised and executed spending by classification |
| FDH, DEA, SFA | Free disposal hull; data envelopment analysis; stochastic frontier analysis |
| PFR | Public Finance Review, which replaced the Public Expenditure Review in 2024 |
| LIC-DSF | Debt sustainability framework for low-income countries |
| PFRAM | PPP Fiscal Risk Assessment Model |
| CDPM, CPM | Names for SISEPUEDE in the team's work |
| NMIM | The team's national investment-needs model |
| PSV | Public Spending Value layer (this proposal) |


# References

Entries marked † were verified only through a search summary, secondary
coverage or a weak source, or were not re-checked (Appendix J).

- Acland, D. and Greenberg, D. (2022), [Principles and practices for
  distributional weighting: a new
  approach](https://gspp.berkeley.edu/assets/uploads/research/pdf/Acland,_Greenberg_(2022)_PRINCIPLES_AND_PRACTICES_FOR_DISTRIBUTIONAL_WEIGHTING--A_NEW_APPROACH.pdf).
  See also [NBER Working Paper
  31475](https://www.nber.org/system/files/working_papers/w31475/w31475.pdf).
- Adam, C. and Bevan, D. (2014), [Public investment, public finance, and
  growth: the impact of distortionary taxation, recurrent costs, and
  incomplete
  appropriability](https://www.imf.org/en/publications/wp/issues/2016/12/31/public-investment-public-finance-and-growth-the-impact-of-distortionary-taxation-recurrent-41518),
  IMF Working Paper 14/73. See also the [IGC Uganda
  memo](https://www.theigc.org/publications/public-investment-and-growth-implications-recurrent-costs-uganda-project-memo).
- Adarov, A., Clements, B. and Jalles, J. (2024), [Public investment
  multipliers](https://documents1.worldbank.org/curated/en/099719510222432022/pdf/IDU1fd4bd390139da14d001b6c910c4f56d49874.pdf),
  World Bank Policy Research Working Paper 10954.
- Afonso, A., Schuknecht, L. and Tanzi, V. (2005), [Public sector
  efficiency: an international
  comparison](https://ideas.repec.org/a/kap/pubcho/v123y2005i3p321-347.html),
  *Public Choice* 123.
- Aligishiev, Z., Ruane, C. and Sultanov, A. (2023), [A user manual for
  the DIGNAD
  toolkit](https://www.elibrary.imf.org/view/journals/005/2023/003/article-A001-en.xml),
  IMF Technical Notes and Manuals 2023/003.
- Angrist, N., Evans, D., Filmer, D., Glennerster, R., Rogers, H. and
  Sabarwal, S. (2020), [How to improve education outcomes most
  efficiently?](https://cgdev.org/sites/default/files/how-improve-education-outcomes-most-efficiently-comparison-150-interventions-using-new.pdf),
  World Bank Policy Research Working Paper 9450.
- Archondo-Callao, R. (2008), [Applying the HDM-4 model to strategic
  planning of road
  works](https://seal.matrade.gov.my/neuaxis-e/Record/okr-10986-17419),
  World Bank Transport Paper 20.
- Asian Development Bank (2017), [Guidelines for the economic analysis
  of projects](https://www.adb.org/documents/guidelines-economic-analysis-projects).
- Auriol, E. and Warlters, M. (2012), [The marginal cost of public funds
  and tax reform in
  Africa](https://publications.ut-capitole.fr/id/eprint/975/1/auriol_975.pdf),
  *Journal of Development Economics* 97.
- Awerbuch, S. and Berger, M. (2003), [Applying portfolio theory to EU
  electricity planning and policy-making](https://repositum.tuwien.at/handle/20.500.12708/186168),
  IEA working paper.
- Awerbuch, S. and Yang, S. (2007), [Efficient electricity generating
  portfolios for Europe](https://www02.eib.org/attachments/efs/eibpapers/eibpapers_2007_v12_n02_en.pdf),
  *EIB Papers* 12(2).
- Baird, S., Hicks, J., Kremer, M. and Miguel, E. (2016), [Worms at
  work: long-run impacts of a child health
  investment](https://www.nber.org/papers/w21428), *Quarterly Journal of
  Economics* 131(4); [20-year
  follow-up](https://ideas.repec.org/p/nbr/nberwo/27611.html), NBER
  Working Paper 27611.
- Berg, A., Buffie, E., Pattillo, C., Portillo, R., Presbitero, A. and
  Zanna, L.-F. (2019), [Some misconceptions about public investment
  efficiency and growth](https://onlinelibrary.wiley.com/doi/10.1111/ecca.12275),
  *Economica* 86(342); [IMF Working Paper
  15/272](https://www.imf.org/external/pubs/ft/wp/2015/wp15272.pdf).
- Berg, A., Portillo, R., Yang, S. and Zanna, L.-F. (2013), [Public
  investment in resource-abundant developing
  countries](https://www.imf.org/external/pubs/ft/wp/2012/wp12274.pdf),
  *IMF Economic Review* 61(1).
- Blanc-Brude, F., Goldsmith, H. and Välilä, T. (2006), [Ex ante
  construction costs in the European road sector: a comparison of
  public-private partnerships and traditional public
  procurement](https://www.eib.org/files/efs/efr_2006_v01_en.pdf), EIB
  Economic and Financial Report 2006/01.
- Bom, P. and Ligthart, J. (2014), [What have we learned from three
  decades of research on the productivity of public
  capital?](https://ucrisportal.univie.ac.at/en/publications/what-have-we-learned-from-three-decades-of-research-on-the-produc/),
  *Journal of Economic Surveys* 28(5).
- Buffie, E., Berg, A., Pattillo, C., Portillo, R. and Zanna, L.-F.
  (2012), [Public investment, growth, and debt
  sustainability](https://www.imf.org/external/pubs/ft/wp/2012/wp12144.pdf),
  IMF Working Paper 12/144.
- Buffie, E. and others (2020), [DIG-Labor](https://www.imf.org/-/media/files/publications/wp/2020/english/wpiea2020102-print-pdf.pdf),
  IMF Working Paper 20/102.
- Campos, E. and Pradhan, S., [Budgetary institutions and expenditure
  outcomes](https://www.nber.org/system/files/chapters/c8030/c8030.pdf),
  NBER chapter.
- *Cash transfers and the local economy: evidence from Brazil*,
  [*Econometrica*,
  forthcoming](https://www.econometricsociety.org/publications/econometrica/forthcoming-papers/0000/00/00/Cash-Transfers-and-the-Local-Economy-Evidence-from-Brazil/file/19856-4.pdf)
  (authors not confirmed).
- Center for Global Development, [Discount rates in global
  health](https://www.cgdev.org/node/3128144).
- Copenhagen Consensus (2023), [Halftime for the Sustainable Development
  Goals: introduction to the special
  issue](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/26AC5E41A3D76031B85178E84D070CD8/S2194588823000325a.pdf/save_42_million_lives_and_generate_11_trillion_in_economic_benefits_for_only_41_billion_introduction_to_the_special_issue_on_the_most_efficient_policies_for_the_sustainable_development_goals.pdf),
  *Journal of Benefit-Cost Analysis* 14(S1), with [front
  matter](https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/26B0DF6FAE8D35ADEEEA341F49B02848/S2194588823000386a.pdf/bca-volume-14-issue-s1-cover-and-front-matter.pdf)
  and papers on
  [tuberculosis](https://copenhagenconsensus.com/publication/halftime-sdgs-tuberculosis),
  [maternal and newborn
  health](https://copenhagenconsensus.com/sites/default/files/2023-03/Maternal%20and%20Newborn%20health%20Manuscript%20230211_1.pdf)
  and [agricultural
  research](https://copenhagenconsensus.com/sites/default/files/2023-03/Ag%20R&D%20Best%20Investment%20Manuscript%20230311.pdf).
  Earlier rounds: Anderljung, M., [Weighing the
  world](https://copenhagenconsensus.com/sites/default/files/documents/weighing_the_world-_cost-benefit_analyses_of_the_sustainable_development_goals_-_markus_anderljung_1.pdf).
- Crivelli, E. (2017), [Efficiency-adjusted public capital
  series](https://imf.org/-/media/Files/Publications/WP/2017/wp17168.ashx),
  IMF Working Paper 17/168.
- D+C, [All too modest goal: the World Bank's shadow price of
  CO2](https://www.dandc.eu/en/article/world-banks-plans-regarding-shadow-price-co2-are-oriented-towards-costs-mitigation-goals).
  †
- Dahlby, B. (2008), [*The Marginal Cost of Public
  Funds*](https://www.porchlightbooks.com/products/marginal-cost-of-public-funds-bev-dahlby-9780262042505),
  MIT Press.
- Devarajan, S., Squire, L. and Suthiwart-Narueput, S. (1997), [Beyond
  rate of return: reorienting project
  appraisal](https://ideas.repec.org:443/a/oup/wbrobs/v12y1997i1p35-46.html),
  *World Bank Research Observer* 12(1).
- Devarajan, S., Squire, L. and Suthiwart-Narueput, S. (1999), [Reviving
  project appraisal at the World
  Bank](https://library.au.int/node/322460) (one record dates it
  [1995](https://readily.ipb.ac.id/opac/detail-buku?id=14282)). †
- Devarajan, S., Swaroop, V. and Zou, H. (1996), [The composition of
  public expenditure and economic
  growth](https://academicnewsletter.sufe.edu.cn/info/281841), *Journal
  of Monetary Economics* 37(2); [World Bank Policy Research Working Paper
  1082](https://econpapers.repec.org/paper/wbkwbrwps/1082.htm).
- Doherty, L. and Sayegh, A. (2022), [How to design and institutionalize
  spending
  reviews](https://www.imf.org/en/publications/fiscal-affairs-department-how-to-notes/issues/2022/09/20/how-to-design-and-institutionalize-spending-reviews-523364),
  IMF How-To Note 2022/004. See also the [WCPP
  briefing](https://wcpporguk.cf.ac.uk/wp-content/uploads/WCPP-Spending-Reviews-International-Best-Practice-and-Key-Learning-Policy-Briefing.pdf).
- Egger, D., Haushofer, J., Miguel, E., Niehaus, P. and Walker, M.
  (2022), [General equilibrium effects of cash transfers: experimental
  evidence from
  Kenya](https://www.nber.org/system/files/working_papers/w26600/w26600.pdf),
  NBER Working Paper 26600. †
- Engel, E., Fischer, R. and Galetovic, A. (2013), [The basic public
  finance of public-private
  partnerships](https://ideas.repec.org/a/bla/jeurec/v11y2013i1p83-111.html),
  *Journal of the European Economic Association* 11(1).
- Engel, E., Fischer, R. and Galetovic, A. (2014), [*The Economics of
  Public-Private Partnerships: A Basic
  Guide*](https://ppp.worldbank.org/index.php/library/economics-public-private-partnerships-basic-guide),
  Cambridge University Press.
- ESMAP (2021), [Ghana PPA
  study](https://rise.esmap.org/data/files/library/ghana/Renewable%20Energy/Ghana_PPA%20study_2021.pdf).
  Excess-capacity charges: [Citi
  Newsroom](https://www.citinewsroom.com/2021/02/ghs12-billion-paid-for-power-not-used-the-cost-of-pay-or-take-contracts-article/)
  †.
- Eurostat and EPEC (2016), [A guide to the statistical treatment of
  PPPs](https://ec.europa.eu/eurostat/documents/1015035/7204121/epec-eurostat-statistical-guide-en.pdf).
- Fan, S., Gulati, A. and Thorat, S. (2008), [Investment, subsidies, and
  pro-poor growth in rural
  India](https://ideas.repec.org/a/bla/agecon/v39y2008i2p163-170.html),
  *Agricultural Economics* 39(2).
- Fan, S., Hazell, P. and Thorat, S. (2000), [Government spending,
  growth and poverty in rural
  India](https://ideas.repec.org:443/a/oup/ajagec/v82y2000i4p1038-1051.html),
  *American Journal of Agricultural Economics* 82(4).
- Fan, S., Zhang, L. and Zhang, X. (2002), [Growth, inequality, and
  poverty in rural China](https://ideas.repec.org/p/fpr/resrep/125.html),
  IFPRI Research Report 125.
- FAO (2012), [*The State of Food and Agriculture 2012*, chapter on
  returns to agricultural
  investment](https://www.fao.org/4/i3028e/i3028e05.pdf), citing Alston
  and others.
- Farrow, S. and Rose, A. (2018), [Welfare analysis: bridging the
  partial and general equilibrium
  divide](https://resolve.cambridge.org/core/journals/journal-of-benefit-cost-analysis/article/welfare-analysis-bridging-the-partial-and-general-equilibrium-divide-for-policy-analysis/6ECE243839186E36C848B0E83EAAA8CF),
  *Journal of Benefit-Cost Analysis* 9(1).
- Fernandez-Corugedo, E., Gonzalez-Gomez, A. and Guerson, A. (2023),
  [The macroeconomic returns of investment in resilience to natural
  disasters under climate
  change](https://www.imf.org/en/Publications/WP/Issues/2023/06/30/The-Macroeconomic-Returns-of-Investment-in-Resilience-to-Natural-Disasters-under-Climate-534579),
  IMF Working Paper 23/138.
- Filmer, D. and others (2018), [Learning-adjusted years of
  schooling](https://openknowledge.worldbank.org/handle/10986/30464),
  World Bank Policy Research Working Paper 8591.
- Finkelstein, A. and Hendren, N. (2020), [Welfare analysis meets causal
  inference](https://www.aeaweb.org/doi/10.1257/jep.34.4.146), *Journal
  of Economic Perspectives* 34(4).
- Gaspar, V. and others (2019), [Fiscal policy and development: human,
  social, and physical investment for the
  SDGs](https://www.sipotra.it/wp-content/uploads/2019/03/Fiscal-Policy-and-Development-Human-Social-and-Physical-Investment-for-the-SDGs.pdf),
  IMF Staff Discussion Note 19/03; [costing
  note](https://www.imf.org/-/media/files/topics/sdg/sdg-costing-un.pdf.md).
- GEEAP (2023), [Cost-effective approaches to improve global learning
  ("Smart
  Buys")](https://documents1.worldbank.org/curated/en/099008110232520373/pdf/IDU-9401bfdd-f4ff-486b-84b4-570be4f65543.pdf).
- Goyal, A. and Nash, J. (2017), [*Reaping Richer
  Returns*](https://openknowledge.worldbank.org/handle/10986/25996),
  World Bank.
- Grigoli, F. (2014), [A hybrid approach to estimating the efficiency of
  public spending on
  education](https://www.imf.org/external/pubs/ft/wp/2014/wp1419.pdf),
  IMF Working Paper 14/19.
- Grigoli, F. and Kapsoli, J. (2013), [Waste not, want not: the
  efficiency of health expenditure in emerging and developing
  economies](https://www.imf.org/en/publications/wp/issues/2016/12/31/waste-not-want-not-the-efficiency-of-health-expenditure-in-emerging-and-developing-economies-40899),
  IMF Working Paper 13/187.
- Groves, D., Syme, J., Molina-Pérez, E. and others (2020), [*The
  Benefits and Costs of Decarbonizing Costa Rica's
  Economy*](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA600/RRA633-1/RAND_RRA633-1.pdf),
  IDB and RAND.
- Gupta, S., Kangur, A., Papageorgiou, C. and Wane, A. (2014),
  [Efficiency-adjusted public capital and
  growth](https://econpapers.repec.org/paper/imfimfwpa/2011_2f217.htm),
  *World Development* 57.
- Gupta, S. and Verhoeven, M. (2001), [The efficiency of government
  expenditure: experiences from
  Africa](https://ideas.repec.org/a/eee/jpolmo/v23y2001i4p433-467.html),
  *Journal of Policy Modeling* 23(4).
- Gurara, D., Melina, G. and Zanna, L.-F. (2019), [Some policy lessons
  from country applications of the DIG and DIGNAR
  models](https://www.imf.org/en/Publications/WP/Issues/2019/03/18/Some-Policy-Lessons-from-Country-Applications-of-the-DIG-and-DIGNAR-Models-46665),
  IMF Working Paper 19/62.
- Hahn, R., Hendren, N., Metcalfe, R. and Sprung-Keyser, B., [A welfare
  analysis of policies impacting climate
  change](https://economics.mit.edu/sites/default/files/inline-files/MVPF%20Climate%20Policy%20Oct%2027.pdf),
  working paper.
- Hallegatte, S., Rentschler, J. and Rozenberg, J. (2019),
  [*Lifelines: The Resilient Infrastructure
  Opportunity*](https://openknowledge.worldbank.org/handle/10986/31913),
  World Bank.
- Harberger, A. (1997), [Comment on Devarajan, Squire and
  Suthiwart-Narueput](https://ideas.repec.org/a/oup/wbrobs/v12y1997i1p73-79.html),
  *World Bank Research Observer* 12(1).
- Harral, C. and Faiz, A. (1988), [*Road Deterioration in Developing
  Countries*](https://trid.trb.org/View/282593), World Bank.
- Heller, P. (1974), [Public investment in LDCs with recurrent cost
  constraint: the Kenyan
  case](https://ideas.repec.org/a/oup/qjecon/v88y1974i2p251-277..html),
  *Quarterly Journal of Economics* 88(2).
- Hendren, N. and Sprung-Keyser, B. (2020), [A unified welfare analysis
  of government
  policies](https://hendren.scholars.harvard.edu/publications/unified-welfare-analysis-government-policies),
  *Quarterly Journal of Economics* 135(3); [NBER Working Paper
  26144](https://www.nber.org/papers/w26144).
- Herrera, S., Isaka, H. and Ouedraogo, A. (2025), [Public spending
  efficiency](https://www.tandfonline.com/doi/full/10.1080/15140326.2025.2480985),
  *Journal of Applied Economics* 28(1).
- Herrera, S., Kouame, W. and Mandon, P. (2019), [Why some countries can
  escape the fiscal pro-cyclicality trap and others
  cannot](https://documents1.worldbank.org/curated/en/510041565102137832/pdf/Why-Some-Countries-Can-Escape-the-Fiscal-Pro-Cyclicality-Trap-and-Others-Cannot.pdf),
  World Bank Policy Research Working Paper 8963.
- Herrera, S. and Olaberria, E. (2020), [*Budget Rigidity in Latin
  America and the
  Caribbean*](https://documents1.worldbank.org/curated/en/181171586472396016/pdf/Budget-Rigidity-in-Latin-America-and-the-Caribbean-Causes-Consequences-and-Policy-Implications.pdf),
  World Bank.
- Herrera, S. and Ouedraogo, A. (2018), [Efficiency of public spending
  in education, health, and
  infrastructure](https://ideas.repec.org/p/wbk/wbrwps/8586.html), World
  Bank Policy Research Working Paper 8586.
- Herrera, S. and Pang, G. (2005), [Efficiency of public spending in
  developing
  countries](https://documents1.worldbank.org/curated/en/262621468135939068/pdf/wps3645.pdf),
  World Bank Policy Research Working Paper 3645; sector scores as
  reported in [ADB Economics Working Paper
  435](https://www.adb.org/sites/default/files/publication/161539/ewp-435.pdf)
  †.
- HM Treasury, [The Green
  Book](https://www.ohe.org/wp-content/uploads/2020/08/The_Green_Book.pdf);
  distributional weights as documented in the [`greenbook` R
  package](https://cran.r-project.org/web/packages/greenbook/greenbook.pdf)
  †.
- HM Treasury, [Supplementary Green Book guidance: optimism
  bias](https://assets.publishing.service.gov.uk/media/5a74dae740f0b65f61322c72/Optimism_bias.pdf);
  UK Department for Transport, [Optimism bias
  study](https://assets.publishing.service.gov.uk/media/5a74fbb140f0b6360e4726c2/dft-optimism-bias-study.pdf).
- HM Treasury (2021), [Wellbeing guidance for
  appraisal](https://assets.publishing.service.gov.uk/media/60fa9169d3bf7f0448719daf/Wellbeing_guidance_for_appraisal_-_supplementary_Green_Book_guidance.pdf).
- Hood, R., Husband, D. and Yu, F. (2002), [Recurrent expenditure
  requirements of capital
  projects](https://ideas.repec.org:443/p/wbk/wbrwps/2938.html), World
  Bank Policy Research Working Paper 2938 (coefficients not read).
- Hutton, G. (2013), [Global costs and benefits of reaching universal
  coverage of sanitation and drinking-water
  supply](https://susana.org/knowledge-hub/resources?id=3636), *Journal
  of Water and Health*.
- IEA Cost of Capital Observatory, as reported by [pv magazine, October
  2025](https://www.pv-magazine.com/2025/10/09/iea-says-cost-of-capital-for-solar-remains-high-in-southeast-asia/).
  †
- IEG, [Approach paper on cost-benefit analysis at the World
  Bank](https://ieg.worldbankgroup.org/node/3638).
- IFAC, [IPSAS 32 questions and
  answers](https://www.ifac.org/system/files/publications/files/IPSASB-32-Q-A-Document.pdf).
- IFC, [Scaling Solar Zambia press
  release](https://pressroom.ifc.org/all/pages/PressDetail.aspx?ID=25732).
- IMF (2014), [Is it time for an infrastructure
  push?](https://www.elibrary.imf.org/display/book/9781498331555/ch003.xml),
  *World Economic Outlook*, October, chapter 3. See also *Fiscal
  Monitor*, October 2020, [chapter
  2](https://www.imf.org/-/media/files/publications/fiscal-monitor/2020/october/english/ch2execsum.pdf.md).
- IMF (2015), [Making public investment more
  efficient](https://www.imf.org/external/pp/longres.aspx?id=4959),
  policy paper ([PDF](https://infrastructuregovern.imf.org/content/dam/PIMA/Forum/IGEUR/Resources/Making%20Public%20Investment%20More%20Efficient%202015.pdf);
  [PFM
  blog](https://blog-pfm.imf.org/pfmblog/2015/11/trapping-the-white-elephants-can-the-latest-public-investment-boom-avoid-the-mistakes-of-the-past.html);
  [slides](https://g24.org/wp-content/uploads/2023/10/IMF_Public-Investment-Management.pdf)).
- IMF (2018a), [*Fiscal Monitor*: Managing public
  wealth](https://www.imf.org/en/Publications/FM/Issues/2018/10/04/fiscal-monitor-october-2018),
  October.
- IMF (2018b), [Public investment management assessment: review and
  update](https://www.imf.org/en/Publications/Policy-Papers/Issues/2018/05/10/pp042518public-investment-management-assessment-review-and-update).
  Coverage from [How-To Note
  2025/001](https://www.imf.org/-/media/files/publications/howtonotes/2025/english/htnea2025001.pdf.md).
- IMF (2020), [On the capacity to absorb public investment: how much is
  too
  much?](https://www.imf.org/en/Publications/WP/Issues/2020/02/28/On-the-Capacity-to-Absorb-Public-Investment-How-Much-is-Too-Much-49039),
  IMF Working Paper 20/48. †
- IMF (2022), [Fiscal multipliers and
  informality](https://www.imf.org/-/media/files/publications/wp/2022/english/wpiea2022082-print-pdf.pdf),
  IMF Working Paper 22/82.
- IMF (2025a), [*Fiscal Monitor*: Spending
  smarter](https://www.imf.org/-/media/files/publications/fiscal-monitor/2025/october/english/ch1.pdf),
  October, chapter 1; [blog](https://www.imf.org/en/Blogs/Articles/2025/10/07/spending-smarter-to-boost-growth).
- IMF (2025b), [*C-PIMA
  Handbook*](https://www.imf.org/en/publications/books/issues/2025/11/10/c-pima-handbook-climate-public-investment-management-assessment-559283).
- IMF, [Guinea: DIG application](https://www.imf.org/external/pubs/ft/scr/2016/cr16262.pdf),
  Country Report 16/262.
- IMF, [The macroeconomic effects of public investment: evidence from
  advanced
  economies](https://infrastructuregovern.imf.org/content/dam/PIMA/Knowledge-Hub/Publications/pubdocuments/The%20Macroeconomic%20Effects%20of%20Public%20Investment%20Evidence%20from%20Advanced%20Economies.pdf),
  IMF Working Paper 15/95.
- IMF, [Establishment of the Resilience and Sustainability
  Trust](https://www.imf.org/en/news/articles/2022/04/18/pr22119-imf-executive-board-approves-establishment-of-the-rst),
  Press Release 22/119; ODI, [The IMF's Resilience and Sustainability
  Facility](https://odi.org/en/insights/the-imfs-resilience-and-sustainability-facility-underused-and-under-fire/)
  †.
- IMF and World Bank (2017), [LIC-DSF guidance
  note](https://documents1.worldbank.org/curated/en/513741518471205237/pdf/LIC-DSF-SGN-2017-Clean-Feb0718-02082018.pdf);
  [Ghana joint
  DSA](https://documents1.worldbank.org/curated/en/973971632340489819/pdf/Ghana-Joint-World-Bank-IMF-Debt-Sustainability-Analysis.pdf);
  [2026
  review](https://www.imf.org/en/topics/2026-review-of-low-income-countries-debt-sustainability-framework).
- IMF and World Bank, PFRAM: [PFM blog
  2016](https://blog-pfm.imf.org/en/pfmblog/2016/06/posted-by-maximilien-queyranne-isabel-rial-and-genevieve-verdier-1-the-pfram-dev);
  [PFRAM 2.0
  manual](https://infrastructuregovern.imf.org/content/dam/PIMA/Forum/IGEUR/Resources/PFRAM%202.0%20User%20Manual.pdf);
  [PPIAF](https://ppiaf.org/documents/5782).
- IRENA (2014), [IRENA and UNWTO to promote renewable energy in islands'
  tourism
  sector](https://www.irena.org/News/pressreleases/2014/Sep/IRENA-and-UNWTO-to-Promote-Renewable-Energy-in-Islands-Tourism-Sector);
  [IRENA's work on islands (CEM
  2015)](https://cleanenergyministerial.org/sites/default/files/documents/yao_zhao_150304_irenas_work_on_islands.pdf).
- IRENA (2026), [*Renewable Power Generation Costs in
  2025*](https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2026/Jul/IRENA_TEC_RPGC_in_2025_2026.pdf).
- Island and small-state sources: Maldives ASPIRE ([World Bank Results
  2023](https://www.worldbank.org/en/results/2023/03/14/powered-by-the-sunshine-achieving-cheaper-cleaner-and-sustainable-energy-in-the-maldives);
  [feature
  2021](https://www.worldbank.org/en/news/feature/2021/07/12/towards-a-sustainable-net-zero-future-in-maldives));
  [Maldives to UNSD
  2016](https://unstats.un.org/unsd/energy/meetings/2016iwc/25maldives.pdf);
  [Jamaica OUR media
  release](https://our.org.jm/wp-content/uploads/2021/04/final_media_release_our_selects_preferred_bidder_in_response_to_37mw_renewable_energy_project_002.pdf);
  [Belize swap, IMF F&D
  2022](https://www.imf.org/en/News/Articles/2022/05/03/CF-Belize-swapping-debt-for-nature);
  [Barbados swap, Cleary
  Gottlieb](https://clearygottlieb.com/news-and-insights/news-listing/barbados-launches-debt-transaction)
  †; [Ember on the
  Caribbean](https://ember-energy.org/latest-insights/renewable-caribbean-towards-energy-independence/)
  †; [WEF on the Pacific
  2026](https://www.weforum.org/stories/2026/05/pacific-island-states-renewables-energy/)
  †; [Lowy
  Institute](https://www.lowyinstitute.org/publications/world-bank-s-ida-vital-lifeline-pacific-islands-other-small-states)
  †; [CGD on IDA small
  states](https://www.cgdev.org/sites/default/files/how-can-world-bank-better-support-climate-vulnerable-lower-income-small-states-ida.pdf)
  †; EIA outlook as reported by
  [Trend.az](https://www.trend.az/business/4231907.html) †.
- Kalaitzidakis, P. and Kalyvitis, S. (2004), [On the macroeconomic
  implications of maintenance in public
  capital](https://ideas.repec.org/a/eee/pubeco/v88y2004i3-4p695-712.html),
  *Journal of Public Economics* 88.
- Kalra, N., Molina-Pérez, E., Syme, J. and others (2023), *The Benefits
  and Costs of Reaching Net Zero Emissions in Latin America and the
  Caribbean*, IDB and RAND (as reviewed in the companion note on global
  investment needs). †
- Kenya capacity charges, [Business
  Daily](https://www.businessdailyafrica.com/bd/economy/how-kenya-chained-itself-to-costly-power-deals--4329428).
  †
- Kesicki, F. and Ekins, P. (2012), [Marginal abatement cost curves: a
  call for caution](https://ideas.repec.org/a/taf/tcpoxx/v12y2012i2p219-236.html),
  *Climate Policy* 12(2).
- Kim, J., Fallov, J. and Groom, S. (2020), [*Public Investment
  Management Reference
  Guide*](https://ideas.repec.org/b/wbk/wbpubs/33368.html), World Bank.
- Kleven, H. and Kreiner, C. (2006), [The marginal cost of public funds:
  hours of work versus labor force
  participation](https://www.henrikkleven.com/research/published/kleven-kreiner_jpube2006.pdf),
  *Journal of Public Economics* 90.
- Kojima, M. and Trimble, C. (2016), [*Making Power Affordable for
  Africa and Viable for Its
  Utilities*](https://documents.banquemondiale.org/en/publication/documents-reports/documentdetail/293531475067040608),
  World Bank.
- Kumhof, M., Laxton, D., Muir, D. and Mursula, S. (2010), [The Global
  Integrated Monetary and Fiscal Model (GIMF): theoretical
  structure](https://www.imf.org/external/pubs/ft/wp/2010/wp1034.pdf),
  IMF Working Paper 10/34.
- Lempert, R., Popper, S. and Bankes, S. (2003), [*Shaping the Next One
  Hundred Years*](https://www.rand.org/pubs/monograph_reports/MR1626.html),
  RAND.
- Liepmann, H. and Pignatti, C. (2024), Welfare effects of unemployment
  benefits when informality is high, *Journal of Public Economics* 229,
  as summarised by
  [VoxDev](https://voxdev.org/topic/social-protection/unemployment-benefits-are-very-effective-highly-informal-labour-markets)
  and [*Economica*](https://economia.lse.ac.uk/articles/10.31389/eco.533). †
- López, R. and Galinato, G. (2007), [Should governments stop subsidies
  to private goods?](https://ideas.repec.org/a/eee/pubeco/v91y2007i5-6p1071-1094.html),
  *Journal of Public Economics* 91.
- Luttmer, E. (2022), [Can fiscal externalities be
  internalized?](https://www.nber.org/system/files/working_papers/w30213/w30213.pdf),
  NBER Working Paper 30213.
- Mackie, P., Nellthorp, J. and Laird, J. (2005), [World Bank transport
  note on public contributions to
  PPPs](https://documents1.worldbank.org/curated/en/234331468329400081/pdf/339270rev.pdf).
  †
- Marcelo, D., Mandri-Perrott, C., House, S. and Schwartz, J. (2016),
  [Prioritizing infrastructure
  investment](https://documents1.worldbank.org/curated/en/805021467996728921/pdf/WPS7674.pdf),
  World Bank Policy Research Working Paper 7674.
- Marto, R., Papageorgiou, C. and Klyuev, V. (2018), [Building
  resilience to natural disasters: an application to small developing
  states](https://www.ricardomarto.com/publication/pub_vanuatu/),
  *Journal of Development Economics* 135.
- McIntyre, A. and others (2016), [Caribbean energy: macro-related
  challenges](https://www.imf.org/en/publications/wp/issues/2016/12/31/caribbean-energy-macro-related-challenges-43776),
  IMF Working Paper 16/53.
- Melina, G., Yang, S. and Zanna, L.-F. (2016), [Debt sustainability,
  public investment, and natural resources in developing countries: the
  DIGNAR model](https://www.sciencedirect.com/science/article/pii/S0264999315002898),
  *Economic Modelling* 52(B).
- National Audit Office (2018), PFI and PF2, as reported by [Construction
  Enquirer](https://www.constructionenquirer.com/2018/01/18/nao-challenges-value-of-pfi-contracts/)
  and [TES](https://tes.com/news/schools-cost-40-cent-more-build-under-pfi-watchdog-reveals).
  †
- NREL, Energy snapshots: [St
  Lucia](https://research-hub.nrel.gov/en/publications/energy-snapshot-st-lucia/);
  [St Vincent and the
  Grenadines](https://research-hub.nrel.gov/en/publications/energy-snapshot-st-vincent-and-the-grenadines/).
- Ochalek, J., Lomas, J. and Claxton, K. (2018), [Estimating health
  opportunity costs in low-income and middle-income
  countries](https://pmc.ncbi.nlm.nih.gov/articles/PMC6231096), *BMJ
  Global Health*.
- OECD (2026), [Background note on public expenditure efficiency in
  water](https://www.oecd.org/content/dam/oecd/en/events/2026/09/14th-roundtable-on-financing-water/background-note-public-expenditure-efficiency.pdf).
- Ondraczek, J. and others (2015), [WACC the dog: the effect of
  financing costs on the levelized cost of solar
  PV](https://pure.iiasa.ac.at/11553), *Renewable Energy*.
- Pakistan capacity payments,
  [CSSPrepForum](https://cssprepforum.com/capacity-payment-of-ipps-and-pakistan-energy-crisis/).
  † (weak source)
- Parry, I. and others (2014), *Getting Energy Prices Right*, IMF (the
  source of SISEPUEDE's pollution, crash and congestion values). †
- PEFA (2016), [Framework for assessing public financial
  management](https://www.pefa.org/sites/pefa/files/resources/downloads/PEFA_2016_Framework_Final_WEB_0.pdf);
  stocktaking notes
  [B13](https://www.PEFA.org/sites/pefa/files/PEFA%202022%20Stocktaking%20-%20B13.pdf)
  and
  [D06](https://www.pefa.org/sites/pefa/files/2019-07/PEFA%202022%20Stocktaking%20-%20D06.pdf);
  [PEFA
  Climate](https://pefa.org/resources/supplementary-framework-assessing-climate-responsive-public-financial-management-what-you).
- Pradhan, S. (1996), [*Evaluating Public
  Spending*](https://ideas.repec.org:443/p/fth/wobadi/323.html), World
  Bank Discussion Paper 323.
- Pritchett, L. (2000), [The tyranny of concepts: CUDIE (cumulated,
  depreciated, investment effort) is not
  capital](https://ideas.repec.org:443/r/kap/jecgro/v5y2000i4p361-84.html),
  *Journal of Economic Growth* 5(4).
- Psacharopoulos, G. and Patrinos, H. (2018), [Returns to investment in
  education](https://ideas.repec.org/p/wbk/wbrwps/8402.html), World Bank
  Policy Research Working Paper 8402.
- Rajaram, A., Le, T., Biletska, N. and Brumby, J. (2010), [A diagnostic
  framework for assessing public investment
  management](https://ideas.repec.org/p/wbk/wbrwps/5397.html), World
  Bank Policy Research Working Paper 5397.
- Rioja, F. (2003), [Filling potholes: macroeconomic effects of
  maintenance versus new
  investments](https://ideas.repec.org:443/a/eee/pubeco/v87y2003i9-10p2281-2304.html),
  *Journal of Public Economics* 87.
- Robinson, L., Hammitt, J. and O'Keeffe, L. (2019), [Valuing mortality
  risk reductions in global benefit-cost
  analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC7473065/), *Journal
  of Benefit-Cost Analysis* 10(S1); [Reference case
  guidelines](https://content.sph.harvard.edu/wwwhsph/sites/2447/2019/05/BCA-Guidelines-May-2019.pdf).
- Rozenberg, J. and Fay, M., eds. (2019), [*Beyond the Gap: How
  Countries Can Afford the Infrastructure They Need while Protecting the
  Planet*](https://openknowledge.worldbank.org/handle/10986/31291), World
  Bank.
- Schick, A. (1998), [*A Contemporary Approach to Public Expenditure
  Management*](https://documents1.worldbank.org/curated/en/739061468323718599/pdf/351160REV0Contemporary0PEM1book.pdf),
  World Bank Institute.
- Schwartz, G. and others, eds. (2020), *Well Spent: How Strong
  Infrastructure Governance Can End Waste in Public Investment*, IMF, as
  presented [here](https://www.mof.go.jp/pri/research/seminar/fy2020/tff2020_publication_01.pdf).
  †
- Simar, L. and Wilson, P. (2007), [Estimation and inference in
  two-stage, semi-parametric models of production
  processes](https://research.dial.uclouvain.be/entities/publication/4ac5e6e9-969c-4278-8bb7-1d1aa03acfbe),
  *Journal of Econometrics* 136(1).
- SISEPUEDE code: [`jcsyme/sisepuede`](https://github.com/jcsyme/sisepuede)
  and [`milocortes/costs_benefits_ssp`](https://github.com/milocortes/costs_benefits_ssp)
  (including
  [`cb_calculate.py`](https://raw.githubusercontent.com/milocortes/costs_benefits_ssp/main/costs_benefits_ssp/cb_calculate.py)).
- Statistics Norway (2015), [The size of the marginal cost of public
  funds](https://www.ssb.no/en/offentlig-sektor/artikler-og-publikasjoner/the-size-of-the-marginal-cost-of-public-funds);
  [Discussion Paper
  925](https://www.ssb.no/en/forskning/discussion-papers/the-marginal-opportunity-cost-of-public-funds)
  †.
- *Taxing property in developing countries: theory and evidence from
  Mexico*, [working
  paper](https://www.jcsuarez.com/Files/MX_Property_Tax_Study.pdf)
  (authors and date not confirmed).
- UK Department for Transport (2025), [TAG unit A2.4: appraisal of
  productivity
  impacts](https://assets.publishing.service.gov.uk/media/6899e4c7ad0cbc0e2764320e/tag-unit-a2-4-productivity-impacts-may-25.pdf).
- Vogt-Schilb, A. and Hallegatte, S. (2014), [Marginal abatement cost
  curves and the optimal timing of mitigation
  measures](https://openknowledge.worldbank.org/server/api/core/bitstreams/64f0e470-8ce9-5ad6-9fcf-94992a1766d5/content),
  *Energy Policy* 66.
- Watkins, D. and others (2020), [Resource requirements for essential
  universal health coverage](https://pmc.ncbi.nlm.nih.gov/articles/PMC7248571),
  *Lancet Global Health*.
- Woods, B., Revill, P., Sculpher, M. and Claxton, K. (2016),
  [Country-level cost-effectiveness
  thresholds](https://eprints.whiterose.ac.uk/112025), *Value in Health*
  19(8).
- World Bank (2013), [Investment project financing: economic analysis
  guidance note](http://www.ampres.com.mx/assets/guidance_note_economic_analysis.pdf).
- World Bank (2016), [Discounting costs and benefits in economic
  analysis of World Bank
  projects](https://documents1.worldbank.org/curated/en/099610503022315638/pdf/IDU02e978a2a023f704c140bb1b082595e67e593.pdf).
- World Bank (2023), [Bank Directive: investment project
  financing](https://thedocs.worldbank.org/en/doc/a63d7e40de1c13802a096eddf6d105bb-0290012023/original/Bank-Directive-Investment-project-financing.pdf).
- World Bank (2024a), [Guidance for Public Finance
  Reviews](https://documents1.worldbank.org/curated/en/099053124144119039/pdf/P175240-590f330c-30d7-4fe7-bac5-9c0b0d6fcdb8.pdf);
  [PFR brief](https://www.worldbank.org/en/topic/fiscalpolicy/brief/public-finance-reviews);
  PFR Fundamentals notes on [spending
  efficiency](https://documents1.worldbank.org/curated/en/099053124144068167/pdf/P175240-9b995be0-4268-4da9-95c9-5fd84dd3c38e.pdf),
  the [public wage
  bill](https://documents1.worldbank.org/curated/en/099062325190034662/pdf/P506801-a3647740-b169-443a-b44a-a3eeccd12013.pdf),
  [potential fiscal
  savings](https://documents1.worldbank.org/curated/en/099021126140533503/pdf/P506801-b4e18138-d5b4-4d77-ae0f-5fb5e9b0b8b5.pdf)
  and [fiscal
  multipliers](https://documents1.worldbank.org/curated/en/099020426122037419/pdf/P506801-8137cefb-746a-4484-8aff-c659cc50d8af.pdf).
  †
- World Bank (2024b), [Guidance note on shadow price of carbon in
  economic
  analysis](https://documents1.worldbank.org/curated/en/099553203142424068/pdf/IDU1c94753bb1819e14c781831215580060675b1.pdf).
- World Bank (2024c), *Global Economic Prospects*, June: [chapter 3,
  Harnessing the benefits of public
  investment](https://openknowledge.worldbank.org/server/api/core/bitstreams/41681424-4459-4959-84d5-63709dee74dc/content);
  [full
  report](https://openknowledge.worldbank.org/server/api/core/bitstreams/d644659c-2e22-410e-98a5-b8a40dc6c183/content).
- World Bank (2026), [*World Development Report 2026*,
  draft](https://documents1.worldbank.org/curated/en/099090426145529770/pdf/P512385-5636baf0-fd26-410d-90c1-cf08125fe298.pdf).
  †
- World Bank country and programme documents: [Malawi
  PER](https://openknowledge.worldbank.org/entities/publication/078c36d5-25c7-57d0-8b67-b0f98ba2b7fb/full);
  [Gambia
  PER](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/783451591241640332)
  †; [Belize
  PER](https://thedocs.worldbank.org/en/doc/7b8bec6f9c262427c8b46dac4daaf3d8-0370012024/original/Belize-Public-Expenditure-Review.pdf);
  [BOOST](https://www.worldbank.org/en/programs/boost-portal/about-boost)
  †; [ASPIRE](https://www.worldbank.org/en/data/datatopics/aspire/about);
  [CCDR investment
  estimates](https://www.worldbank.org/en/news/feature/2024/05/01/what-you-need-to-know-about-ccdr-investment-estimates-and-the-role-of-the-private-sector);
  [macro-modelling and
  climate](https://www.worldbank.org/en/programs/economicpolicy-macro-modeling/macro-modeling-climate-change);
  [health benefits package
  studies](https://documents1.worldbank.org/curated/en/430691643352732370/pdf/Using-Allocative-Efficiency-Analysis-to-Inform-Health-Benefits-Package-Design-for-Progressing-towards-Universal-Health-Coverage-Proof-of-Concept-Studies-in-Countries-Seeking-Decision-Support.pdf);
  [Optima](https://openknowledge.worldbank.org/entities/publication/c8930a29-00bb-5da3-afee-4cba9a983a18)
  †; [climate budget
  tagging](https://documents1.worldbank.org/curated/en/779731613708891591/pdf/Technical-Annex-Overviews-of-Climate-Expenditure-Tagging-Frameworks.pdf);
  [Handbook on economic analysis of investment
  operations](https://preventionweb.net/quick/38589).

**Not re-checked in this work (†):** Arrow, K. and Lind, R. (1970),
*American Economic Review* 60(3); Farrell, M. (1957), *Journal of the
Royal Statistical Society A* 120(3); Jacobs, B. (2018), *International
Tax and Public Finance* 25; Kaplow, L. (1996), *National Tax Journal*
49(4); Little, I. and Mirrlees, J. (1974), *Project Appraisal and
Planning for Developing Countries*; Samuelson, P. (1954), *Review of
Economics and Statistics* 36(4); Squire, L. and van der Tak, H. (1975),
*Economic Analysis of Projects*; UNIDO (1972), *Guidelines for Project
Evaluation*; World Bank (1997), *World Development Report: The State in
a Changing World*; Andrews, M., Pritchett, L. and Woolcock, M. (2013),
*World Development* 51.

