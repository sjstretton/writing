
*Theory and Research Note No. 6.7, November 2026. Stephen J. Stretton, writing in a personal capacity. The views expressed are the author's own and do not represent those of any institution with which he is or has been affiliated.*

# Introduction

The textbook says: price the externality. A carbon tax at the social cost of carbon, applied everywhere, corrects the market failure and lets the economy find the cheapest abatement. The Pigouvian framework is correct as far as it goes, but it goes almost nowhere in practice, because it assumes away the problem it claims to solve. Climate change is a global commons problem, and no country has an incentive to price its own emissions at the global social cost. Each country's emissions are a fraction of the global total; the benefit of its own abatement accrues overwhelmingly to others. The Nash equilibrium is a carbon price well below the social cost of carbon in every country, and this is approximately what we observe.

What drives mitigation in practice is a different set of forces: industrial competitiveness, energy security, fiscal relief from subsidy reform, access to international capital and markets, and technology learning that makes clean energy cheaper than dirty regardless of any carbon price. China did not deploy 600 GW of solar to correct an externality; it did so to dominate a global industry. The European Union did not accelerate renewables after 2022 for climate reasons alone; it did so because Russian gas was a strategic vulnerability. Developing countries do not adopt clean energy because the social cost of carbon tells them to; they adopt it when international finance makes it cheaper than the alternative.

A modelling framework for climate policy must start from these realities. This paper builds one in three layers. Section 2 sets out the national model: a binary investment choice between clean and dirty capital, with the cost gap determined by fuel prices, capital costs, carbon prices, subsidies and international support. Section 3 adds the global layer: a learning curve that couples countries through technology cost, creating the leader-follower dynamic that structures the actual energy transition. Section 4 identifies six deviations from the textbook that each require an additional policy instrument, building incrementally from the base case to a realistic multi-instrument portfolio. Section 5 classifies international instruments by their incentive channel and quantifies their current contribution. Section 6 decomposes the 8–12 GtCO$_2$/yr of current policy-driven emissions avoidance into locked-in and marginal components, proposing a total-versus-marginal TECP as a diagnostic. Section 7 asks which instruments satisfy all three criteria of investment friendliness, political durability and compatibility with international augmentation.

The framework is designed to be simple enough to implement in a spreadsheet and rich enough to capture the essential dynamics. It complements paper 6.1, which derives the Total Effective Carbon Price from a CES model of energy demand, by placing the TECP in a global context where technology learning, capital market failures and political economy determine what policies are feasible and what they achieve. It provides the analytical underpinning for the Global Incentives Model planned in paper 6.6.


# The national model: investing in clean or dirty capital

## The one equation that matters

In a putty-clay world, almost all abatement comes from the investment margin. Existing capital is locked into its fuel: you cannot convert a gas boiler to a heat pump, or a diesel truck to an electric one. The aggregate fuel mix changes only as old capital retires and new capital replaces it. The central variable is therefore $\phi_t$, the clean share of new investment in year $t$:

$$
\phi_t = \frac{1}{1 + \exp\!\big(\beta\,\Delta_t\big)},
$$

where $\Delta_t = c^C_t - c^D_t$ is the cost gap between clean and dirty technologies and $\beta$ is the price sensitivity of the investment decision. This is a logit share model, equivalent to a CES for a binary choice. When clean is cheaper ($\Delta < 0$), $\phi \to 1$; when dirty is cheaper, $\phi \to 0$. The parameter $\beta$ encodes the breadth of the taste distribution: high $\beta$ means a sharp switch near cost parity (utilities making rational calculations); low $\beta$ means a gradual transition with diverse preferences (households choosing vehicles).

## What enters the cost gap

The total cost of delivering one unit of energy service from technology $j$ is:

$$
c^j_t = k^j_t \cdot a(r_t) + \frac{p^j_t}{\eta^j},
$$

where $k^j$ is the capital cost per unit of service capacity, $a(r) = r/(1-(1+r)^{-T})$ is the annualisation factor at discount rate $r$ over asset lifetime $T$, $p^j$ is the fuel price and $\eta^j$ is the technical efficiency (energy service per unit of fuel). The cost gap is:

$$
\Delta_t = \underbrace{(k^C_t - k^D_t)\cdot a(r_t)}_{\text{capital gap}} + \underbrace{\big(p^C_t/\eta^C - p^D_t/\eta^D\big)}_{\text{fuel gap}} - \underbrace{\tau_t\,(e^D - e^C)}_{\text{carbon price}} - \underbrace{s_t}_{\text{subsidy}} - \underbrace{g_t}_{\text{intl augmentation}}.
$$

Every national policy instrument enters through exactly one term: a carbon tax increases $\tau$; a CfD or RE auction reduces $c^C$ through guaranteed revenue (lowering effective $k^C$); a vehicle standard acts as a mandate on $\phi$ directly, overriding the logit; a subsidy reduces $s$; a fuel excise increases $p^D$; and international derisking reduces $r$, which reduces $a(r)$, which narrows the capital gap.

## Capital stock evolution

The stock evolves by vintage accounting:

$$
S^C_t = (1-\delta)\,S^C_{t-1} + \phi_t \cdot I_t,
$$

where $\delta$ is the retirement rate and $I_t$ is total new investment (replacement of retired stock plus demand growth). The clean share of the operating stock is $w^C_t = S^C_t/(S^C_t + S^D_t)$. Emissions follow:

$$
E_t = (1 - w^C_t) \cdot Q_t \cdot \frac{e^D}{\eta^D},
$$

where $Q_t$ is total service demand. The national model has four equations: investment choice (eq. logit), cost gap (eq. gap), stock evolution (eq. stock) and emissions (eq. emissions).

## The TECP in this model

The Total Effective Carbon Price is the carbon tax that, acting alone (with $s = g = 0$), would produce the same $\phi_t$ as the actual policy mix:

$$
\tau^* = \frac{\Delta_{\text{baseline}} - \Delta_{\text{policy}}}{e^D - e^C}.
$$

This converts the entire multi-instrument portfolio into one number. Paper 6.1 derives the same object from the CES cost function and extends it to multiple fuels and sectors; the logit version makes the investment-choice interpretation transparent.


# The global model: technology learning and diffusion

## Two equations couple countries

The global model adds one state variable: the technology cost $k^C_t$, which falls with cumulative global deployment:

$$
k^C_t = k^C_0 \cdot \left(\sum_i \sum_{\tau \le t} \phi_{i,\tau}\, I_{i,\tau}\right)^{-\gamma},
$$

where $\gamma$ is the learning elasticity ($\gamma \approx 0.3$ for solar, meaning cost falls about 20 percent per doubling of cumulative capacity). The sum runs over all countries: deployment anywhere reduces costs everywhere.

Each country's adoption responds to its local cost gap:

$$
\phi_{i,t} = \frac{1}{1 + \exp\!\big(\beta_i\,\Delta_{i,t}\big)},
$$

where the cost gap includes the global technology cost $k^C_t$, local fuel prices, local carbon prices, subsidies and international augmentation $g_i$.

These two equations create the leader-follower dynamic. Leaders (large $\tau_i$, large $s_i$, low $r_i$) adopt early, contributing to cumulative deployment, which drives $k^C$ down globally. Followers (small $\tau_i$, high $r_i$) adopt later, but at lower cost because leaders have driven the learning curve. International instruments ($g_i$, CBAM raising $\tau_i$, MDB guarantees reducing $r_i$) accelerate follower adoption by closing the residual cost gap.

## The tipping point

The tipping point for country $i$ is when $\Delta_{i,t} = 0$: clean cost equals dirty cost. After this, $\phi > 0.5$ and the transition is self-sustaining. The time at which each country tips depends on global technology cost (driven by leaders), local financing cost and local policy:

$$
t^{\text{tip}}_i: \quad k^C_{t} \cdot a(r_i) + p^C_i/\eta^C = k^D \cdot a(r_i) + p^D_i/\eta^D + \tau_i(e^D - e^C) + s_i + g_i.
$$

Countries with low $r_i$, high $\tau_i$ and high $g_i$ tip first. Countries with high $r_i$, low $\tau_i$ and no $g_i$ tip last. The diffusion lag — the time between first and last tipping — is the central variable for global climate outcomes. International instruments compress this lag.

## The complete model on one page

Three equations, six parameters:

| Equation | Role | Parameters |
|---|---|---|
| $\phi_{i,t} = 1/(1+e^{\beta_i\Delta_{i,t}})$ | Adoption | $\beta_i$ (price sensitivity) |
| $\Delta_{i,t} = (k^C_t - k^D)a(r_i) + (p^C_i/\eta^C - p^D_i/\eta^D) - \tau_i(e^D-e^C) - s_i - g_i$ | Incentives | $r_i$ (discount rate), $\eta$ (efficiency) |
| $k^C_t = k^C_0 \cdot (\sum_{i,\tau} \phi_{i,\tau}I_{i,\tau})^{-\gamma}$ | Technology | $\gamma$ (learning rate) |

: The global model. National policy enters through $\tau_i$ and $s_i$. International instruments enter through $g_i$ (subsidies, CfDs), $r_i$ (derisking) and $\tau_i$ (CBAM). Stock evolution and emissions follow from eq. stock and eq. emissions.

The national model is the first two equations. The global model adds the third. The TECP is the $\tau$ that makes the incentives equation produce the observed $\phi$ without $s$ or $g$.


# From textbook to reality: six deviations

The base model assumes rational agents, one externality and no frictions. Real economies deviate in six ways, each adding an instrument to the optimal portfolio. The deviations are additive: each can be incorporated independently, and the full realistic model includes all six.

## A. Capital is clay

Fuel choice is locked at investment; the aggregate mix changes only through capital turnover. This does not change the optimal instrument (a carbon tax is still correct) but changes what makes a carbon tax effective: it must be expected to persist over the asset lifetime, not just exist today. A carbon price with a 30 percent reversal probability has an effective investment signal of roughly half its face value. Durable instruments — technology standards, CfDs with 15–20-year contracts — outperform fragile ones even at lower nominal rates, because investors believe them.

## B. Consumers are myopic

Households use implicit discount rates of 20–30 percent for vehicle and appliance choices, far above the social rate of 3–5 percent. They overweight upfront cost and underweight future fuel savings. A carbon tax alone under-delivers because even at the correct rate, consumers do not adopt clean technology fast enough. The Tinbergen rule applies: two market failures (externality plus behavioural bias) require two instruments. Add a technology standard alongside the price.

## C. Technology learning creates spillovers

Deploying clean technology today reduces its cost for everyone tomorrow, but the deployer captures only the private benefit, not the social value of cost reduction. This is a second externality beyond emissions. A carbon tax prices the emissions externality; a deployment subsidy prices the learning externality. The subsidy can be temporary: once the technology crosses the tipping point ($\Delta = 0$), the market sustains deployment without it. This is the theoretical case for front-loaded RE subsidies, and empirically it has been vindicated by solar, where costs fell 90 percent in 15 years and deployment is now self-sustaining.

## D. Capital markets fail

Clean investment faces higher financing costs than dirty in many markets, especially developing countries. The same wind turbine costs \$40/MWh in Germany (5 percent WACC) and \$80/MWh in Nigeria (15 percent WACC). The technology is identical; the risk premium doubles the cost. No carbon price, however high, compensates for a financing wedge of this size. Derisking instruments — MDB guarantees, concessional lending, blended finance — close the WACC gap and are the highest-leverage intervention available globally.

## E. Coordination failures block adoption

EV charging networks, hydrogen pipelines and district heating require infrastructure that no individual investor will build without assured demand, and no consumer will adopt without assured infrastructure. This is a coordination failure with multiple equilibria; the low-adoption equilibrium is stable and no price signal alone shifts it. Public infrastructure investment or coordination mandates are needed. This is the one deviation that breaks the continuous CES/logit framework and requires a discrete threshold model.

## F. Political economy constrains instrument choice

Carbon pricing creates concentrated, visible losers and diffuse, invisible winners. The maximum feasible explicit carbon price is well below the social cost in most jurisdictions. Standards and feebates can operate at higher implicit rates because the costs are hidden in product prices. The optimal instrument in a politically constrained world is not the Pigouvian tax but the portfolio that achieves the most abatement while remaining politically sustainable.

## The incremental build

| Base | Complication | What changes | Instrument added |
|---|---|---|---|
| CES / logit over fuel prices | — | — | Carbon tax = SCC |
| + A | Putty-clay capital | Signal must persist over asset life | Durable instruments (CfDs, standards) |
| + B | Myopic consumers | Signal is discounted by high $r_c$ | Technology standard |
| + C | Learning spillovers | Early deployment is underprovided | Deployment subsidy (temporary) |
| + D | Capital market failure | WACC gap inflates clean cost | Derisking (guarantees, concessional finance) |
| + E | Coordination failure | Price signal can't shift equilibrium | Infrastructure investment |
| + F | Political economy | Max feasible $\tau \ll$ SCC | Less visible instruments (standards, feebates) |

: Incremental build from textbook to reality. Each row adds one complication and one instrument. Base+A+B is the core for consumer sectors. Base+A+C+D for power. Base+A+B+C+D+F is the full stack, implementable in a single framework. E requires a bolt-on threshold model.


# International instruments: channels and magnitudes

## Three channels

International instruments create mitigation incentives through three mechanisms: risk reduction (lowering the cost of capital for clean investment), revenue transfer (paying for emissions reductions directly) and conditionality (attaching decarbonisation requirements to financial flows).

## Quantification

| Channel | Annual flows | Avoided emissions | Implied \$/tCO$_2$ |
|---|---|---|---|
| Risk reduction (MDB guarantees, concessional lending, blended finance) | \$35–55bn | 200–600 Mt/yr | \$15–40 |
| Revenue transfer (carbon markets, results-based finance, grants) | \$15–20bn | 100–300 Mt/yr | \$5–15 |
| Conditionality (green bonds, SLLs, policy lending, CBAM) | \$150–250bn | 100–500 Mt/yr | \$2–10 |
| **Total** | **\$200–325bn** | **400–1,400 Mt/yr** | **\$5–20 avg** |

: International instruments by channel. Source: author's estimates from IEA, World Bank, ICAP, IRENA and national sources. [VERIFY: ranges are order-of-magnitude estimates developed in conversation, November 2026; each row needs primary-source verification.]

The leverage varies enormously across instruments. A dollar of MDB guarantee capital avoids 10–20 times more emissions than a dollar of carbon credit purchase, because the guarantee unlocks private investment while the credit buys abatement directly. CBAM has infinite leverage: zero fiscal cost to the imposing country and a carbon price signal equal to the EU ETS permit price on exporting countries' industrial emissions.

## Where international instruments enter the model

Each instrument maps to a specific term in the cost gap (eq. gap):

- Leader-country deployment (China solar, US IRA): reduces $k^C_t$ through the learning curve.
- MDB guarantees and concessional lending: reduces $r_i$, lowering the annualised capital cost.
- CfDs backed by international finance: reduces effective $k^C_i$ through guaranteed revenue.
- CBAM: raises $\tau_i$ in exporting countries (the importing country's carbon price minus the exporter's).
- Subsidy reform via MDB policy lending: raises $p^D_i$ by removing fossil fuel subsidies.
- Carbon market credit purchases: adds to $s_i$ as a direct revenue transfer.


# Total versus marginal TECP

## Definitions

The **total TECP** measures the full emissions reduction attributable to all policies relative to a static-shares baseline — a frozen fuel mix scaled to current GDP and population. It answers: what has the full policy portfolio achieved?

The **marginal TECP** measures what would be lost if all policies were removed today, holding technology costs at current levels. It answers: how much of the transition still depends on ongoing policy?

The **locked-in TECP** is the difference: the portion that would persist even without policy, because technology has crossed the tipping point or capital stock is physically committed.

## Estimated decomposition

| Sector | Total (GtCO$_2$/yr) | Marginal (GtCO$_2$/yr) | Locked-in (GtCO$_2$/yr) | Locked-in share |
|---|---|---|---|---|
| Power | 3–4 | 1–2 | 1.5–2.5 | ~55% |
| Transport | 2–3.5 | 1.2–2.2 | 0.8–1.3 | ~35% |
| Industry | 1.5–2.5 | 0.5–1.2 | 1–1.5 | ~55% |
| Buildings | 1–2 | 0.2–0.5 | 0.8–1.5 | ~70% |
| **Energy total** | **7.5–12** | **3–6** | **4–7** | **~50%** |

: Total versus marginal emissions avoidance by sector. Source: author's estimates from IEA Global Energy Review 2025, IPCC AR6, ICCT, UNEP Emissions Gap. [VERIFY: ranges are order-of-magnitude estimates developed in conversation, November 2026.]

Converting to TECP units (dividing by a global $\Lambda$ of approximately 0.3–0.4 GtCO$_2$ per \$/tCO$_2$), the total TECP is roughly \$28/tCO$_2$ (range \$20–35), the marginal TECP roughly \$13 (range \$8–18) and the locked-in TECP roughly \$15 (range \$10–20).

## Reversibility by instrument type

The most reversible instruments are price signals on flow decisions: fuel excise taxes, carbon prices affecting dispatch, biofuel mandates. These are high-marginal, low-locked-in. Removing them causes immediate behavioural reversion.

The least reversible are standards on stock decisions: building codes, appliance efficiency standards, the LED lighting phase-out, vehicle emission standards for the already-purchased fleet. These are high-locked-in, low-marginal. Their contribution accumulates irreversibly as capital stock turns over.

The policy design implication: **price instruments need to be permanent because their effect is largely marginal and reversible; standards can be temporary if they push technologies past tipping points.** The gap between total and marginal TECP is a measure of policy success — transitions that policies triggered but no longer need to sustain.


# Which instruments satisfy all criteria?

A useful instrument for coordinated climate policy must satisfy three criteria simultaneously: it must be investment-friendly (creating a bankable signal that private capital responds to), politically durable within the adopting country (surviving electoral cycles), and compatible with international augmentation (providing a structure that MDB guarantees or international finance can attach to). The interaction of these criteria with putty-clay capital dynamics and policy reversal risk narrows the field.

## First-division instruments

**Contracts for difference and power purchase agreements.** Investment-friendly: they guarantee revenue, eliminating merchant risk. Politically durable: they do not raise consumer prices (and can lower them when the strike is below wholesale). Compatible with international augmentation: the CfD contract is exactly the instrument that MDB guarantees backstop; the guaranteed cash flow, not the government's policy, is what the guarantee attaches to.

**Destination-based carbon pricing (CBAM and variants).** Investment-friendly: the price signal is enforced at the border of the importing market, durable regardless of the exporting country's politics. Politically durable in the imposing country: it protects domestic industry. Compatible with international augmentation: CBAM revenue (or the avoidance of it) creates a natural funding source and incentive for industrial decarbonisation in exporting countries.

**Closed-economy green industrial policy (for large countries).** The US IRA, China's solar and EV industrial strategy, the EU Green Deal Industrial Plan. Investment-friendly by design. Politically durable: framed as jobs and competitiveness, not climate. Internationally augmenting through global technology learning: domestic scale-up drives cost reductions that benefit every country.

## Second-division instruments

Explicit carbon taxes (investment-friendly but politically fragile); ETS with output-based allocation (politically durable but weakly compatible with international finance); vehicle emission standards (durable but no international augmentation hook); technology-specific subsidies (investment-friendly but dependent on annual budget appropriations). Each missing one criterion.

## Implication for the framework

The modelling framework should evaluate instruments not only by their TECP — the emissions they reduce — but by their durability (credibility at the investment decision point) and their compatibility with the international instruments that accelerate diffusion to follower countries. The TECP measures the destination. The policy portfolio analysis measures whether the road gets there.


# Conclusion

The textbook answer to climate change is a carbon tax. The practical answer is a portfolio of instruments, each correcting a different market failure, chosen for political durability and designed to be compatible with international finance. This paper provides the analytical framework for evaluating such portfolios.

Three equations suffice: an investment-choice logit (equivalent to a CES), a cost-gap equation through which all policy instruments enter, and a global learning curve that couples countries. Six deviations from the textbook — putty-clay capital, behavioural myopia, learning spillovers, capital market failures, coordination failures and political economy — each add an instrument but never remove the carbon price. The total-versus-marginal TECP decomposes cumulative policy achievement into locked-in transitions and ongoing effort. About half of what current policies have delivered is now locked in, mainly through installed renewable capacity and efficient building and appliance stock.

The main limitation is that none of this is yet computed for real countries. The next step is to calibrate the model to the energy balances, fuel prices and policy instruments that paper 6.1's TECP framework already handles, add the learning curve and leader-follower dynamics, and compute the total and marginal TECP for a panel of countries. Paper 6.6 sets out the plan for the full Global Incentives Model that would do this.


# References




# Appendix A: Non-price instruments — conversion methodology

Every non-price policy reduces to the same question: what is the cost of the action the regulation forces, divided by the emissions it avoids? The answer, in \$/tCO$_2$, enters the TECP on the same footing as an explicit carbon tax. For instruments that mandate outcomes directly (RE targets, coal phase-out dates), the cleaner route is to observe the emissions reduction and back out the equivalent carbon price: $\tau^{\text{eq}} = \Delta E / \Lambda$, using a static-shares baseline. tbl. nonprice gives the conversion methodology for each instrument class.

| Instrument | TECP channel | Implicit \$/tCO$_2$ | Simplest estimation |
|---|---|---|---|
| Vehicle emission standard | Intensive | \$50–200 | Non-compliance penalty / lifetime emissions |
| Power sector emission standard | Intensive | \$0–50 | LCOE gap / emission factor gap |
| Building energy code | Extensive | \$−20 to \$80 | Construction cost uplift / lifetime savings |
| Appliance MEPS | Extensive | \$−50 to \$20 | Efficiency \% uplift $\times C_s/\bar{e}_s$ |
| Renewable portfolio standard | Intensive | \$0–60 | REC price / marginal fossil emission factor |
| EV / heat pump subsidy | Intensive | \$40–250 | Subsidy / lifetime emissions saving |
| Technology ban / phase-out | Intensive | \$5–$\infty$ | Stranded asset cost / avoided emissions |

: Non-price instruments: conversion to TECP-equivalent carbon prices. Source: author's estimates from ICCT, IEA, CLASP and national sources. [VERIFY: ranges are order-of-magnitude estimates.]


# Appendix B: Policy typology — national instruments

See the companion tables (available as PDF: `Policy_Framework_Tables.pdf`) for the full national and international policy typology with modelling structure, optimal instrument, deviation from the Pigouvian optimum and practical implications.
