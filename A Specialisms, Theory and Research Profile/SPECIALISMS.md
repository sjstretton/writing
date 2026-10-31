# Strategic Academic Specialisms

Stephen Stretton · draft of 29 Oct 2026, built from the papers in this repo and the notes on Google Drive. **Internal working document.** Some sources are World Bank internal or "Official Use Only"; use them for orientation only, and don't quote them outward.

This page maps what Stephen can credibly claim as expert ground, in five groups. Each specialism has a short abstract of the argument he already makes, a strength rating and where the material is. The executive summary sets out an order for nailing the specialisms down. `E Writing Instructions/STRATEGY.md` gives the shorter positioning; this page is the detail behind it.

**Strength key:** ●&nbsp;written up (a draft paper or book chapter states the argument) · ◐&nbsp;partial (notes, a section or a deck) · ○&nbsp;thin (a heading or a planned paper only).

---

## Executive summary: a sequenced approach

**Everything here is one argument.** Climate policy fails less for want of the right price than for want of feasibility under three constraints: political (who wins and who loses), financial (the cost of capital and fiscal space) and energy-system (slow capital stock, electrification). Finance ministries and development banks can relax all three. That is the through-line ("climate statecraft"), and every specialism below is one piece of it. The stylized-facts papers (section 3) are where the through-line is stated outright.

**A specialism is "nailed down" when it has four things:** a one-sentence position, one paper at the paper standard, one concept paper that gives colleagues a term to use, and one 10-minute deck. Today only Risk and Finance and the TECP come close.

**Order.** Each step follows the priorities in `STRATEGY.md`, and each reuses what the step before it built.

| Step | When | Specialism | Why now | Done when |
|---|---|---|---|---|
| 1 | Now to 31 Oct | **Risk and finance** (section 4) | It is the subject of PhD proposal 1. The material is the strongest in the portfolio. | The proposal goes out, with the 3.1 writing sample cut to 2,000 words. |
| 2 | Nov | **Systemic AI risk** (section 5) | PhD priority 2, and the thinnest specialism. It needs to be built from the strengths Stephen already has, not started from zero. | The questions in the proposal 3 outline are answered (6 Nov) and the first draft exists (27 Nov). |
| 3 | Nov–Jan, in parallel (AI drafts) | **Fiscal unit core:** the TECP and the basis of tax (sections 1 and 2.2) | Paper 1.1 is already the top priority paper, and November's main work goal is CPAT-LTS, so this specialism advances in work hours anyway. | 1.1 is submitted to *Climate Policy*. 6.1 has a country application. Concept paper 1 (policy-equivalent carbon price) is out. |
| 4 | Jan–Mar 2027 | **Stylized facts** (section 3) | One synthesis paper turns six thin items into one strong one and becomes the 0.0 introductory paper. It is only credible once steps 1–3 exist to point to. | "From Stylized Facts to Policy Design" (5.4) is sourced and at standard. |
| 5 | Spring 2027 | **Wider tax:** property tax, Olson, measuring investment (sections 2.1, 2.3, 2.4) | The ideas are mature in draft but sit off the critical path. | 2.1 *Taxing Rent, Not Effort* is at standard. Two short notes exist (Olson and reform; measuring investment). |
| Parked | After both PhD applications | **Philosophy and McGilchrist** (section 6) | This is the long game. It enriches the AI proposal (agency, metaphor) without competing with it. | Proposal 2 restarts. |

**Three decisions** (each unblocks one step). *All three decided yes by Stephen, 29 Oct 2026.*

1. Is the "three constraints" through-line right? **Yes.** The 0.0 introductory paper and the website "About" page both use it.
2. For systemic AI risk, which angle should lead? **Incentive and institutional design, with systemic financial risk as the analogy.** It reuses the sovereign-incentives work and the 2014 systemic-risk review (section 5).
3. Should the politics essays (8.1–8.3) and the *Finding Frodo* deck stay off the academic profile? **Yes, for now.** Revisit later (section 7).

---

## 1. Fiscal unit specialisms: what Stephen can do there

These are the things the climate fiscal team can call on Stephen for. Stephen named the first; the rest are added from the material.

**1.1 Quantitative modeling of policy: the Total Effective Carbon Price (TECP).** ●
The TECP is the uniform, economy-wide carbon tax that would cut emissions as much as a country's actual policy mix does. Existing metrics, including CPAT's Total Carbon Price ("broadly revenue raised divided by carbon emitted"), measure the price signal, not what it achieves. The TECP weights each instrument by how strongly emissions respond to it, split into fuel switching and demand reduction, using a nested CES demand model calibrated once per country from the energy balance, prices and elasticities. It runs in a spreadsheet. In the stylized example (working paper v0.3) a mix that explicit-price metrics rate at $21/t has a long-run TECP of $37/t ($32–38 across calibrations) and $28/t after one year. A fuel standard with a $166/t credit price adds only about $1/t, because the price is high but its base is small and unresponsive. Uses include paying for policies under policy crediting, recognition of carbon prices under CBAM, and country diagnostics. An earlier Drive note frames the same idea as an "effectiveness-weighted total carbon price" for setting donor willingness to pay and baselines for results-based climate finance.
*Sources:* 6.1 brief and working paper (`B Working Papers/6.ModularUpgrades/6.1.PolicyEquivalentCarbonPriceAndCES/`); Drive: `WTP and Baseline Project.docx`.

**1.2 Models a finance ministry can audit (CPAT architecture).** ◐
Policy models should be small enough for a ministry to check, and AI-assisted recoding now makes that achievable. Paper 5.2 replaces CPAT's hard renewable-investment constraint with shadow prices, rebuilds CPAT's core in code, and links it to fiscal strategy (SiSePuede, CCDR, CPAT). On Drive, the CPAT strategy adds a common policy framework (a carbon tax plus feebates), technoeconomic power and transport modules, derisking inside CPAT and an extension to 2070.
*Sources:* `5.Modelling/5.0.Overview/5.0.OverviewModelling.docx`, 5.2 README; Drive: `WorkProgramMainPPT.pptx`, `CPAT_Key_Equations_SiSePuede.docx` (internal).

**1.3 Feebates and output-based rebating.** ● *(added)*
A feebate keeps the full carbon price at the margin without the carbon bill. It is a sectoral emissions-intensity benchmark plus a price on deviation from it, so it changes behavior without raising average costs. In the stylized coal case a carbon tax raises generation cost by 87% and a feebate by 0%. Feebates suit governments that cannot sustain a headline carbon tax: Canada removed its consumer fuel charge in April 2025 and kept its industrial output-based system. It belongs alongside the TECP as a core fiscal-unit offer.
*Sources:* 1.2 brief and draft (`1.2.FeebatesAndOutputBasedRebating/`).

**1.4 CBAM analysis and reform.** ● *(added)*
The EU border carbon adjustment should "credit the price signal, not the payment". As drafted, it fails to recognize feebates and other implicit carbon prices, and it can be gamed by "scrap shuffling" in steel. The material includes a near-final consultation note and an Egypt emission-factor CBAM dashboard.
*Sources:* 1.4 (`1.4.IronSteelCBAM/`), 6.2 (`6.2.CBAMPolicyTool/`).

**1.5 Excise and externality diagnostics.** ● *(added)*
A ministry should read its excise system as a whole, against a common "externality spine" that puts carbon, air pollution, accidents, congestion and road damage on one scale. Diagnostics should run on data ministries already hold. The Sierra Leone report is the worked case (draft, 24,800 words).
*Sources:* 7.1 (`7.AdditionalAnalytics/7.1.ExciseFiscalDiagnostic/`).

**1.6 Climate fiscal risk and climate PFM.** ◐ *(added)*
Climate-informed public finance reviews, fiscal buffers used as collateral, climate debt sustainability, and extending fiscal-risk analysis to extreme shocks. The work-plan decks and course module G hold the material; no paper yet.
*Sources:* `D Climate Econ Course/G. Climate PFM…`; Drive: `WorkProgramMainPPT.pptx` (internal).

---

## 2. Wider tax and fiscal specialisms

Stephen's own FY26 work plan already names this ground: "Taxation theory, especially property taxation, excise taxes. The basis of taxation and how this affects international tax cooperation. Macro-fiscal accounting, including risk." (`2 Strategic Plans/FY26/Stephen-UpdatedWPAFY26_v5.docx`).

**2.1 Property, land and wealth tax.** ◐
Tax what cannot move or does not respond: land, rent, monopoly and externalities. In Stephen's words, "taxation is a corrective to the system of property rights". The case for a land value tax works at rates near 100%, but such rates are unfair and disruptive in transition. Stephen's fix is two-parameter taxation, a marginal rate plus a "norm". First replace council tax and business rates like for like, then tax all of the *increase* in land rent (Mill's "unearned increment"). Paper 2.1 extends the idea into a "reverse wealth tax" on land, meaning an allowance with land value tax above it, and into corporate tax on supernormal profit above a normal-return allowance. All of it is compatible with free movement of capital and people. A Drive note adds an "unproductive-wealth tax", citing Kalecki's argument that a wealth tax need not reduce investment. The design is strong in draft; property tax as such (valuation, administration, developing-country practice) is thin.
*Sources:* 2.1 *Taxing Rent, Not Effort* (`2.OtherTaxAndFiscalPolicy/2.1.RentTax/RentTax.qmd`; master file to confirm, H13); Drive: `A0-Writing100 Ideas.txt` (ideas 25, 31–47), `Operating_system_CW_Edits.docx`.

**2.2 The basis of tax and the game theory of tax policy.** ●
An origin-based tax on a mobile base invites a race to the bottom; a destination-based tax can turn it into a race to the top. VAT moved taxation to a destination basis, and carbon pricing should follow. Origin-based carbon pricing makes one rate do two jobs, the production incentive and the consumption signal. Separate them: a feebate on production and a destination charge on consumption, collected through VAT or a forward obligation on energy suppliers. Under destination charges "each exporter's most competitive feebate rate equals the charge in its markets", so raising the charge pulls exporters' rates up. The same logic applies to profit taxes: consumer locations are "pretty much fixed", as land is. This is the core of the 1.1 journal paper.
*Sources:* 1.1 (`1.1.OpenEconomyCarbonPricing/OpenEconomyCarbonPricing.qmd`), `Background-DesigningARaceToTheTop.qmd`, 1.4 carbon consumption tax; Drive: 100 Ideas (ideas 13, 23, 28).

**2.3 Olsonian political economy: how tax change happens.** ●
"A policy is politically feasible when its benefits are concentrated and its costs diffuse" (after Olson, 1965). Carbon taxes have exactly the wrong shape. Feebates have the right one, because they create winners inside the industry who defend them. Reform follows phases: subsidies first, then feebates and auctions, and a carbon tax with revenue recycling last. "Attempting a phase-three instrument in a phase-one world is the characteristic error." A carbon price consolidates a transition rather than starting it. Reform windows and bundling matter; Sweden's 1991 reform is the example. The constructive corollary (essay 7.2) is to build organized constituencies for the alternative. A short standalone note would make this citable.
*Sources:* Book 8.5.2 *Carbon Pricing: The Right Policy at the Wrong Time* (ch. 1, 10, 11); 7.1 `Background-PoliticalEconomyMetric.qmd`; 1.2 brief; 8.6.2.

**2.4 Measuring investment.** ○
Climate investment-needs estimates are exogenous and linear. They ignore that policy reform changes the needs, assume fixed public and private shares, and treat crowding-in inconsistently. Stephen proposes tagging climate investment in BOOST public-expenditure data and separating "pseudo-investment" in land from real investment. The critique is clear; there is no paper.
*Sources:* Drive: `A3 Research Plan.docx` ("The role of investment"), `WorkProgramMainPPT.pptx`, 100 Ideas (idea 11).

**2.5 Coal contracts and stranded assets.** ◐ *(added)*
Retiring legacy coal power purchase agreements saves money before any climate benefit is counted. The leftover capital can be settled through securitized bonds. India is the case. Background notes only.
*Sources:* 8.1.1 (`8.AdditionalPolicyPapers/8.1.OtherFiscalPolicy/8.1.1.StrandedByContractReformingLegacyCoalPPAs/`).

---

## 3. Wider World Bank climate specialisms: stylized facts

**The section as a whole.** The facts imply that any workable solution must cover four things: return, risk, financial scaling, and political economy, both internal and external. The planned synthesis "From Stylized Facts to Policy Design" (draft tables in 5.4) is the vehicle. Its numbers are not yet sourced. On Drive, the same synthesis is planned as an introduction on "Stylized Facts about Climate Mitigation, Political Economy, Macroeconomics and Finance".
*Sources:* `8.AdditionalPolicyPapers/8.4.Analytics/8.4.3.CarbonPricingPoliticalEconomyAndOptimality/Policy_Framework_Tables.pdf` and `Toy_Model_Global_Mitigation.pdf`; Drive: `A1 Research Agenda.docx`, `A3 Research Plan.docx`.

**3.1 Energy transition stylized facts.** ◐
Decarbonization means shifting the energy vector to electricity. It happens in open economies. Elasticities are highest between close substitutes. The capital stock is fixed at the point of investment and adjusts slowly, so it needs long-term incentives. Learning by doing creates tipping points. Shallow decarbonization runs on prices and elasticities; deep decarbonization needs forward-looking investment and phase-outs. This was the theme of Stephen's master's thesis, and it is his critique of macro models built only on elasticities.
*Sources:* `1.1/1.Presentation/Pres-UpdatingCarbonPricing.pptx` (slide 2); 5.4 tables; Drive: `WhoAmI.txt`.

**3.2 Macro stylized facts.** ◐
Clean power is capital-intensive, so its price is mostly the price of money: on Stephen's numbers solar costs about 80% more at a 12% cost of capital than at 4%. Debt that builds revenue-earning assets differs from consumption debt, but debt sustainability frameworks treat them alike. "The macroeconomic effects of carbon pricing are underwhelming." An illustrative IHLEG figure (debt up about 70 points of GDP at market rates against about 10 at World Bank rates) needs a checked source before use. [VERIFY: IHLEG source and figure.]
*Sources:* Book 6.1 *Time and Chance* (preface, ch. 24–25); `2 Strategic Plans/FY24/3. Investment Needs and Green Growth/FiscallyPrudentMacroFiscalPolicy.docx`.

**3.3 Implications for a politically feasible tax mix.** ●
Instrument choice is "mostly determined by constraints, not by efficiency rankings". The feasible mix uses feebates where taxes stall, destination pricing for revenue and rent taxes alongside, and chooses each instrument for durability. Policy reversal is a real risk: an announced tax may deliver only part of its headline effect. Pooled rebating turns the dirtiest firms into lobbyists for the policy, because they gain most from improving.
*Sources:* `1.CarbonPricing/1.0.Overview/1.0.OverviewClimateAndFiscalPolicy.docx`; Book 8.5.2 (ch. 4); 8.4.3 tables; Drive: `A3 Research Plan.docx`.

**3.4 Implications for a politically feasible role for the finance minister.** ◐
The finance minister's main lever is expectations: setting long-term price floors and revenue certainty, and reducing risk for long-term investment, as the UK's contracts for difference do. Mitigation investment can also offset a contractionary fiscal consolidation. The binding problem is timing, because a minister who waits gets cheaper equipment and cheaper money, so incentives must reward acting now. Book 6.1 frames this as "Four Questions a Finance Minister Would Ask". A planned "CREDOS" mitigation dashboard for finance ministers exists in outline.
*Sources:* Book 8.5.1 (ch. 16); `FiscallyPrudentMacroFiscalPolicy.docx`; `4.SovereignIncentives/4.0.Overview/4.0.OverviewSovereignIncentives.docx`; Drive: `A2 Tools Plan.docx`, `WhoAmI.txt` (internal).

**3.5 Collective action stylized facts.** ●
Climate is three collective action problems, not one: between countries, within countries and over time. Economics has focused almost entirely on the first. The "double incentive problem" follows: countries need an incentive to impose incentives on themselves. Technology diffuses from leaders to followers (the toy model), and the "tragedy of the horizons" adds the time dimension to the prisoner's dilemma. "I will if you will" commitment auctions are one design response.
*Sources:* `A.Website/papers/GeoprosperityIntro.docx` (appendix C.3); course module D; 5.4 toy model; Drive: `A3 Research Plan.docx`, `Geoprosperity_WorkingPaperSeries.docx` (Official Use Only).

**3.6 Internal political economy stylized facts.** ◐
Six drivers decide whether carbon pricing survives in a country: fiscal pressure, salience, vested interests, distributive design, institutional quality and energy structure. Concentrated losers block reform, and reversal risk discounts the effective price. The material proposes a metric built on these drivers.
*Sources:* 7.1 `Background-PoliticalEconomyMetric.qmd`; 8.4.3 tables.

**3.7 A solution for low-fiscal-space, low-investment-capacity countries.** ●
Deliver clean energy as a service at a declining price, so the country takes on an energy bill, not a debt. Lower the cost of capital at source, so that investment does not use up scarce fiscal space. The tools are synthetic sovereign bonds rated on developed-country guarantees, pay-as-you-go energy for debt-distressed countries, fiscal buffer funds held as collateral, green savings accounts where bond markets are thin, and a "notional capitalized value" (a climate balance a country can borrow against). Small island states are proposed as pilots.
*Sources:* 3.1; 4.1; Book 8.5.1 (ch. 18); `GeoprosperityIntro.docx`.

---

## 4. Risk and finance

The strongest group, and the subject of PhD proposal 1. Stephen's FY26 work plan names it "finance and risk… especially those that reduce the cost of capital or provide mitigation incentives".

**4.1 Why risk matters.** ●
"The cost of capital, not the cost of technology, holds back clean power" in developing countries. Reducing risk is the cheapest available way to reduce the price of clean electricity. The cost of capital is several distinct risks: payment (offtaker), construction, currency, policy and the scarcity of equity. Each needs its own fix. "A risk mechanism decides who bears a loss. An incentive instrument changes whether the loss happens."
*Sources:* `3.FinanceAndRisk/3.0.Overview/3.0.OverviewMobilisingPrivateCapital.docx`; 3.1; Book 8.5.1 (ch. 3).

**4.2 What this means for investment policy.** ●
Contracts beat prices. Auctions and long-term power purchase agreements coordinate investment across time and cut the cost of capital in a way a carbon price cannot. "Well-functioning capital markets and reasonable borrowing costs are powerful climate instruments." A planned paper would estimate the carbon-price elasticity of power investment at different interest rates.
*Sources:* Book 6.1 (ch. 4); Book 6.2 (claims 3–4); Drive: `ResearchAgenda.docx`, `A1 Research Agenda.docx`.

**4.3 Why MDBs matter.** ●
Multilateral development banks are trusted, repeat lenders whose AAA rating "can be lent without being spent". That is the theory of concessionality behind guarantees. Capital adequacy decides what MDBs can do and their mandate decides what they may do. They should reward policy, not only projects, through a separate envelope for global public goods. A draft claim that MDB guarantee capital avoids far more CO₂ per dollar than carbon credits needs sourcing before use. [VERIFY: 5.4 tables, "10–20×", unsourced.]
*Sources:* Book 6.1 (ch. 16); 3.4 *MDB Climate Envelope*; 3.5 *Reforming MDBs*; 5.4 tables.

**4.4 Financial structures for derisking.** ●
- **Payment intermediary.** A facility on the model of India's SECI pays generators on time, backed by a guarantee waterfall that runs from distributor to subnational government, national government and finally a multilateral (3.1).
- **Synthetic sovereign bonds.** Bonds rated at developed-sovereign level because developed countries co-guarantee them (3.1).
- **Climate Investment Trust.** Leveraged equity that both invests and stands as first loss for others (4.2).
- **Three-tier guarantee.** The AAA rating is "used but not used up" (GeoProsperity appendix A).
- **"Super-leverage".** Guarantees cut funding costs by far more than they cost, and the resulting AAA bonds suit pension funds and central banks.
- **The Sollar.** A solar-backed claim (2.3).

*Sources:* 3.1, 4.2, 8.2.1 (The Sollar); Drive: `WP6-SyntheticSovereignBonds.docx`, `GeoProsperity Pitches`.

**4.5 RST-like structures for scale.** ◐
The IMF's Resilience and Sustainability Trust (RST) shows that a contribution can be structured as an investment rather than an expenditure: SDRs capitalized the RST, and the same model can hold an equity buffer behind policy lending. Buffer funds hold rather than disburse, and that is where the leverage comes from. The Climate Investment Trust takes the RST as its comparator. The analogy is stated but the RST itself is not yet analyzed; a short note comparing structures would close the gap.
*Sources:* 4.2 `ClimateInvestmentTrust.qmd`; Book 8.5.1 (ch. 18, 20); 4.0 overview; `8.AdditionalPolicyPapers/8.3.SovereignIncentives/8.3.1.MDBClimateEnvelope/3.RelatedPiecesAndLinks/Background-ScalingUpPolicyLendingAndPolicyIncentivesNoteForEFI.qmd` (internal).

**4.6 Macroeconomics of investment.** ◐
Debt that builds revenue-earning assets is not consumption debt. The crowding-out, stimulus and stranded-asset narratives each miss part of the picture. "Financial tipping points" and reinforcing loops explain why investment, once started, can sustain itself.
*Sources:* Book 6.1 (ch. 24–25); Drive: `A3 Research Plan.docx`.

**4.7 How derisking can unlock growth.** ◐
A green safe asset steers cheap money into building rather than land. Supply-chain finance credits and green-growth thresholds turn lower risk into higher output. "Getting the financing right is a necessary and sufficient condition" for rapid decarbonization. A sectoral TFP diagnostic (8.4.2) is planned but not drafted.
*Sources:* Book 6.1 (preface, ch. 12, 16); Drive: `Paper3-FinancialOptionsForDecarbonisation.docx`.

**4.8 Sovereign incentives and policy crediting.** ● *(added; this is the PhD topic)*
Reward sovereigns, not projects. Pay governments with balances and guarantees they can borrow against, not cash transfers for counterfactuals no one can observe. Avoid perverse "wait to be paid" incentives. Notional capitalized value credits a country for its carbon stocks, and business-as-usual emissions use it up. Sustainability-linked instruments (SLIDIs, the original KPI-linked sovereign debt idea) tie the cost of debt to results. The PhD frames the trade-off as mitigation effect versus the incentive needed versus the cost to the MDB, with dynamic incentives to act now.
*Sources:* 4.0, 4.1, SLIDIs (in `4.3.SustainabilityLinkedLending/3.RelatedPiecesAndLinks/`); `C Research Proposal/Oxford_DPhil_Research_Proposal_Sovereign_Incentives_Derisking.docx`. (The World Bank discussion paper *Sustainability-Linked Lending*, in `4.3…/9.Archive`, is World Bank confidential: don't cite it outward.)

---

## 5. Systemic AI risk ○

**The weakest specialism and the second PhD priority, so it gets step 2 in the sequence.** The proposal 3 outline holds only questions. The transferable assets are real, though:

- **Incentive and institutional design.** The sovereign-incentives question ("what would make a government choose differently?") carries over directly to the organizations that build and deploy AI.
- **Systemic financial risk.** Sewell and Stretton (2014) is a literature review of systemic risk in finance, written for HSBC. It supplies the analogy, contagion and correlated failure, and its review method. (Client work: check what can be cited.)
- **Corporations as artificial agents.** In the 100 Ideas draft (idea 71), corporations are "a sort of artificial intelligence entity". AI is "a replay" of the same problem, which suggests human supervisory boards for AI entities.
- **Hands-on practice.** The AI-assisted recoding of CPAT (5.2) is practical evidence of working with AI systems.

**Proposed one-sentence position (agent draft):** AI risk is a systems problem as much as a model problem, and the tools that govern systemic financial risk (capital buffers, liability, insurance and incentive design) are the place to start. This matches position P7 in `PAPERS.md`.
*Sources:* `C Research Proposal/3-SystemicAISafety-Outline.md`; `2 Strategic Plans/Overall Pitch.pptx` (slide 7, internal); Drive: `systemic-risk.tex`, `A0-Writing100 Ideas.txt`.

---

## 6. Other academic specialisms

**6.1 Philosophy of law and order: *Order Without Ordinance* (7.1).** ●
The method is to look for the metaphor doing the work. Western law is a sovereign's command; the Chinese *li* is the grain in wood; dharma "is not made; it is known". India had a developed legal system with the amendment mechanism deliberately left out. Austin's definition of law broke Indian law, and Hart's later analysis vindicates it. Durable order comes from aligned incentives and shared meaning, not command (position P8).
*Sources:* `8.AdditionalPolicyPapers/8.6.Philosophy/8.6.0.OverviewPhilosophy.docx`, 8.6.1.

**6.2 McGilchrist and the philosophy of religious language (7.3, proposal 2).** ◐
Religious language is vocative, not propositional: it addresses rather than describes. This is drawn from McGilchrist's two modes of attention, Nietzsche, Advaita, Daoism and Vedic psychology. A Drive essay links McGilchrist to *wu wei*: self-command shuts down the fluid, creative right-hemisphere mode. Proposal 2's topic is still "to be defined" and is parked.
*Sources:* 7.3 *The Vocative Case*; `C Research Proposal/README.md`; Drive: `WhyIsProcrastinationSoTiring.docx`.

**6.3 Institutions and reform: *The Politics of Life Logic* (7.2).** ●
Policy should work with existing forces. Reform succeeds by creating organized constituencies for the alternative, the Olsonian point in section 2.3 turned constructive, and the essay applies this to the World Bank itself.
*Sources:* 7.2.

**6.4 Philosophy of action.** ◐ *(added)*
A six-level model of human action: being, moral vision, emotion, instrumental reason, intention and movement. A socio-economic variant runs from needs to culture to incentives. It was drafted for *Synthese* in 2013 and bears directly on agency questions in AI.
*Sources:* Drive: `PhilosophyPaper-Notes.docx`.

**6.5 Game theory of cooperation.** ● *(added)*
The prisoner's dilemma, the tragedy of the commons and of the horizons, the race to the top, dynamic incentives to act now rather than later, and auctioned commitments. This runs through sections 2.2, 3.5 and 4.8.
*Sources:* Book 6.2 (ch. 12); 1.1; Drive: `A3 Research Plan.docx`.

**6.6 Political economy of capitalism (books in draft).** ◐ *(added)*
*The Operating System of Capitalism* (2018) and *100 Ideas* (2019) set out the wider program: tax inelastic bases, land value capture (the Singapore and Hong Kong "prosperity loop"), a citizen's dividend, transitional justice in reform, and a "strategic tax review" instead of budget-day secrecy. They are the seedbed for sections 2.1 and 2.3.
*Sources:* Drive: `Operating_system_CW_Edits.docx`, `A0-Writing100 Ideas.txt`.

**Physics.** Stephen holds master's degrees in philosophy, economics and physics. The material has no physics specialism as such. [Stephen: add one if there is.]

---

## 7. Notes and cautions

- **Keep off the academic profile:** the politics essays (8.1 *Manifesto*, 8.2 the World Trade Center collapse, 8.3 voting patterns) and the Drive deck `Finding Frodo.pptx`. They contain strong partisan claims and would weaken both PhD applications and the World Bank profile. *(Decided 29 Oct, for now; decision 3 above.)*
- **Confidential or internal:** the World Bank discussion paper *Sustainability-Linked Lending* (in `4.3…/9.Archive`) is World Bank confidential, yet `9.ResearchTracking/CV-UnpublishedWorks.docx` still lists its URL. `GeoprosperityIntro.docx`, including the copy in the website's `_site/papers/`, has an appendix D marked "not intended for external circulation". The Drive `Geoprosperity_WorkingPaperSeries.docx` is marked "Official Use Only". The work plans, team workshop notes and EFI note are internal.
- **Numbers to verify before outward use:** the IHLEG debt figure (the confidential SLL discussion paper, numbered 3.2 before 29 Oct), the MDB guarantee multiple (numbered 4.3 before 29 Oct), and everything in the 8.4.3 tables.
- **Mismatch (resolved 31 Oct 2026):** the old combined overview (now in `8.AdditionalPolicyPapers/8.0.Overview/8.PreviousVersions`) described Rent Tax (now 2.1) as resource and locational rent "alongside carbon pricing", which does not match the qmd; the new 2.0 and 8.0 overviews follow the qmd.
