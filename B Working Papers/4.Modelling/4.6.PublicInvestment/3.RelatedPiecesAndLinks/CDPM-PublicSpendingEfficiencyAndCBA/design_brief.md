# Design brief for the report (coordinator's design decisions)

The report writer must follow this brief. It fixes:
- the structure of the report;
- the proposal (Option A, Option B, upgrades);
- the worked example;
- the upgrade plan.

The literature notes in this folder supply the evidence. Where the notes contradict this brief, the notes win on facts; flag the conflict.

## 0. The user's request (verbatim intent)

The user, a World Bank climate-fiscal modeller working on CPAT, wants investigative work on the **allocative efficiency** (main focus) and **technical efficiency** of public spending. CDPM, formerly SISEPUEDE, has a cost-benefit framework for climate transformations. The questions are:

1. What rules do governments use, or should they use?
2. Is the right test the efficiency of public spending per se, or the "Pigouvian" difference between what the private sector does and the optimum?
3. How does the thinking change in low-capacity countries?
4. What frameworks does the World Bank use in public expenditure reviews (especially the fiscal unit and Santiago Herrera, whom the user calls "Santiago Harrer"), and what does the IMF use?
5. Has there been work on extending CBA? (The sentence is cut off. Read it as extending CBA from projects to programmes, sectors and the whole economy, and from climate and energy to other sectors.)
6. How should capital and current spending be integrated?
7. Can PPPs or PPAs change the picture by turning capital spending into an ongoing expense that makes sense? Use the case of a small island state with room for renewable energy, no fiscal space and high oil import costs: it is "trapped".
8. How should a measure that gives a revenue return be treated?
9. Is there efficient-frontier work that can be integrated?

Deliverables:
- a detailed methodology literature review;
- a proposed simple addition to "our combined GIMF DIGNAD DIGNAR tool" that extends the CBA in CDPM/SISEPUEDE to other sectors and is consistent with current thinking and practice;
- an Option B, less constrained by the SISEPUEDE method, in case Option A proves too constraining.

The proposal must:
- be practical and integrable;
- be able to include BOOST data (the World Bank budget microdata);
- be consistent with how the World Bank already thinks;
- suggest incremental upgrades to that thinking, and some more radical options.

Two more requirements:
- a **very simple executive summary**, readable by a smart non-specialist (short sentences, no jargon, no formulas; do not mention IQ);
- a **plan for the tool upgrade**.

## 1. Report structure (use these headings, numbered)

0. **Executive summary (plain language).** About one page, 10-14 short paragraphs or bullets.
   - What the problem is.
   - The one rule we recommend.
   - Why low-capacity countries need extra care.
   - How capital and running costs are put on the same footing.
   - The small-island trap and how to get out of it.
   - How revenue returns count.
   - What we would add to the tool.
   - The plan in four steps.

   Use a concrete image or two, for example: "a dollar the budget gets back is worth more than a dollar"; "a solar farm paid by the kilowatt-hour instead of up front".
1. **Purpose, scope and status of evidence.** Say plainly that:
   - full texts could not be opened (the sandbox network blocked publisher sites);
   - citations were checked against abstracts, catalogue records and search extracts;
   - items marked unverified need checking before external use.

   Give a compact legend for verification tags.
2. **Short answers to the questions.** One short paragraph per question 1-9 above, each pointing to the section with the detail.
3. **Methodology literature review.** Dense, cited, about 45-55% of the report. Subsections:
   - 3.1 Allocative and technical efficiency: definitions and the decision rule.
   - 3.2 Why the state spends at all: market failures, additionality and the "Pigouvian" wedge. Show how the counterfactual and fungibility critique (Devarajan, Squire and Suthiwart-Narueput 1997) changes appraisal.
   - 3.3 The cost of public funds and the value of public funds: MCPF, MVPF, shadow price of public income. Include how revenue returns are treated, the discount rate, the shadow price of carbon and distributional weights.
   - 3.4 Low-capacity countries: efficiency gaps, absorptive capacity, execution, optimism bias, "matching role to capability", maintenance first, cash benchmark.
   - 3.5 World Bank practice:
     - PER to PFR (2024 guidance);
     - the PFR Fundamentals notes;
     - Herrera's frontier work and the potential-savings method;
     - BOOST; PEFA; the PIM framework;
     - economic-analysis guidance (three questions, discounting note 2016, shadow price of carbon note 2024);
     - the Infrastructure Prioritization Framework; Beyond the Gap; CCDRs and MFMod; sector tools.
   - 3.6 IMF practice:
     - PIE-X, PIMA and C-PIMA; spending reviews; SDG costing;
     - the DIG family (DIG, DIGNAR, DIGNAD) and GIMF, including how they represent efficiency, returns, user fees, recurrent costs and fiscal rules;
     - PFRAM; the LIC-DSF treatment of PPPs and SOEs.
   - 3.7 Capital and current spending: the recurrent-cost problem, maintenance, composition and growth, annuitisation, the balance-sheet view.
   - 3.8 PPPs, PPAs and contingent liabilities:
     - the Engel-Fischer-Galetovic irrelevance result;
     - accounting (Eurostat, IPSAS 32);
     - when PPPs add value;
     - PPAs and take-or-pay contracts;
     - good auctions (Scaling Solar, Maldives ASPIRE) and bad ones (Ghana, Kenya excess capacity).
   - 3.9 Small island states: the oil-import trap (the evidence and numbers in the notes).
   - 3.10 Efficiency frontiers:
     - technical (FDH/DEA/SFA);
     - allocative (marginal returns across sectors, e.g. Fan, Hazell and Thorat);
     - portfolio (Markowitz and Awerbuch);
     - robust decision making and Pareto frontiers; MACC critique.
   - 3.11 Extending CBA across sectors and to the economy:
     - Copenhagen Consensus, DCP3 / HTA, education Smart Buys and LAYS, MVPF of cash;
     - water, sanitation and resilience BCRs;
     - general-equilibrium CBA (Farrow and Rose);
     - CGE and macro linking in CCDRs;
     - the UK Green Book and spending reviews.
   - 3.12 Synthesis: what is settled, what is contested, and the gaps in World Bank and IMF practice that the proposal targets (a table).
4. **Where our tools stand today.**
   - CDPM CBA (from `internal_cdpm_and_macro_tool.md`).
   - InvestmentNeeds lenses and NMIM P1-P5 typology, MacroFiscalModels and the dashboard (from `internal_macrofiscal_tool_and_nmim.md`).
   - A table of hooks and of gaps or inconsistencies, including:
     - CDPM CBA export undiscounted;
     - NemoMod costs pre-discounted;
     - straight-line annualisation;
     - no payer split and no fiscal flows;
     - CPAT power model annuity-due versus CRF;
     - utility debt outside public debt;
     - energy savings only in GIMF-lite;
     - BOOST execution not used in formulas.
5. **Option A (recommended): the Public Spending Value (PSV) layer.** Design per section 2 of this brief, with equations, a parameter table (default, range, source, confidence), outputs, and an ASCII or Mermaid flow diagram of how it slots between CDPM / NMIM / sector cards and MacroFiscalModels.
6. **Worked example: a small island escaping the oil trap.** Per section 3 of this brief, with tables of results produced by a script that you write and run.
7. **Option B (less constrained by the CDPM method).** Per section 4 of this brief.
8. **Upgrades to World Bank thinking: incremental and radical.** A table per section 5 of this brief.
9. **Tool upgrade plan.** Per section 6 of this brief: phases, deliverables, tests, links to `MacroFiscalModels/TODO.md` items, data, risks.
10. **Risks, limitations and open questions.**
11. **References**, each with its verification status.

Appendix A: formula sheet. Appendix B: parameter defaults. Appendix C: glossary.

Length: detailed, about 13,000-18,000 words in total. Prefer tables for parameters and comparisons. Use LaTeX-style inline math sparingly and plain-text equations in code blocks where clearer. Write for World Bank and IMF economists in the body; keep the executive summary plain.

## 2. Option A: the Public Spending Value (PSV) layer — design to write up

**Core idea.** For every candidate use of public money ("measure"), the layer computes what society gets per dollar of *net* public money. A measure can be:
- a CDPM transformation;
- an NMIM investment line;
- a programme from a non-climate "sector card".

The figure is computed after three corrections:
- (i) what the private sector would do anyway;
- (ii) how much spending turns into working assets or services;
- (iii) the money the measure brings back to the budget.

It then:
- ranks the measures;
- picks a portfolio within the fiscal envelope that the macro and debt models say is affordable;
- passes the chosen programme back to the macro models.

This is MVPF logic applied to a World Bank economic analysis, with the World Bank's existing efficiency diagnostics (PIMA, PEFA, BOOST, Herrera frontier scores) as haircuts.

Steps (write each with its equations and defaults):

**Step 1 — Tag every flow.** Tags:
- Payer or receiver: budget, SOE or utility, private firm, households, rest of world.
- Economic nature: capex, O&M, wage or recurrent, transfer or subsidy, fuel, revenue.
- NMIM type P1-P5: reuse NMIM's rules as defaults; override with CCDR plans.
- COFOG function, so the layer can map to BOOST.

CDPM CBA lines (`cb:<sector>:<category>:...`) need a lookup table from category to payer and nature.

**Step 2 — Economic NPV, made consistent.**
- Discount once, in this layer, at the World Bank rate (default 6%; range y to 2y; sensitivity at 3% and 10%).
- Fix the pre-discounted NemoMod lines.
- Carbon at the WB shadow price, as a switch and a memo item.
- ENPV_j as the World Bank would compute it, so that with λ = 1 and no haircuts the layer reproduces the InvestmentNeeds lens (b)/(c) (regression check).

**Step 3 — Efficiency and delivery haircuts (technical efficiency).** For public capex, three separate effects:
- PIMA or PEFA efficiency `s_j`: cost uplift 1/s on the public share, as InvestmentNeeds already does.
- BOOST execution rate `e`: timing delay of benefits, not lost money.
- Optional optimism-bias uplift where no country PIM data exist.

For service sectors, use Herrera-type FDH/DEA output-efficiency scores (health, education, infrastructure) to scale outcomes per dollar.

State clearly how to avoid double counting:
- in the CBA, efficiency raises cost per unit of asset;
- in the macro bridge, `s` is passed and the CBA cost uplift is *not* also passed as extra spending;
- pick one convention and document it.

Add the "reform dividend" as a measure in its own right: closing two-thirds of the efficiency gap (IMF 2015), with a cost.

**Step 4 — Additionality and the Pigouvian wedge.**
- Social NPV versus private NPV. Private NPV uses the market WACC (lens a) and private prices, including taxes.
- The public money needed is the *viability gap*: max(0, −private NPV) for P4, the full cost for P1, contingent only for P2 and P3, and zero for P5.
- An "instrument test": could a price (CPAT carbon tax or subsidy reform) or a regulation deliver the outcome at lower fiscal cost? If so, flag "price first".
- An additionality factor a_j for benefits that would happen anyway (deadweight).

This is how the "Pigouvian difference" enters operationally. Public money should pay the wedge, not the whole investment.

**Step 5 — Fiscal ledger and fiscal NPV.** Net budget flows by year:

| Sign | Flow |
|---|---|
| − | public capex, by financing route |
| − | public O&M (recurrent-cost coefficient) |
| − | subsidies or viability gap |
| + | user fees and tariffs captured |
| + | fuel-subsidy savings |
| − | fuel excise lost (e.g. displaced diesel) |
| + | carbon or other Pigouvian revenue earmarked |
| ± | contingent flows (expected calls on guarantees) |

Also report:
- FNPV at the government's marginal cost of borrowing (and at the concessional rate);
- the equivalent annual fiscal cost;
- the cash profile and payback year;
- a "self-financing" flag.

Leave growth-induced tax revenue to the macro model, to avoid double counting. Only direct, contractual or near-mechanical fiscal effects belong in the ledger.

**Step 6 — The decision metric.** Let:
- W_j = PV of benefits to everyone other than the budget, net of their costs (willingness to pay);
- F_j = PV of the net fiscal cost.

Then:
- ENPV_j = W_j − F_j;
- MVPF_j = W_j / F_j;
- the λ-adjusted net benefit is NB_λ = W_j − λ·F_j.
- Rule: fund if MVPF_j > λ, equivalently NB_λ > 0. If F_j ≤ 0 (the measure pays for itself), fund if W_j ≥ 0; the binding issue is then financing, not value.

λ is the marginal cost of public funds (default 1.2: Auriol-Warlters Africa average; Norway uses 1.2). Use a stress value of 1.5-2.0 where the macro and debt test shows the country cannot raise more debt. The radical version derives λ from the macro model; see section 5.

For portfolio ranking under a binding budget, rank by NB_λ per dollar of PV fiscal cost. Show that with λ = 1 and no constraint this collapses to the World Bank ENPV rule. **This is the main "incremental upgrade": World Bank economic analysis plus a fiscal ledger plus λ.**

**Step 7 — Capital and current on one footing.**
- Each capex line becomes an equivalent annual cost: EAC = capex × CRF(r, n). Use r = SDR for the economic view, the government's rate for the fiscal view, and the WACC for private or PPA routes.
- Add a recurrent-cost coefficient (Heller's r-coefficient): O&M or staffing per dollar of capex per year, by sector, with defaults and ranges from the notes. Mark values as unverified where they are.
- Current programmes (health, education, social protection) are measured per year directly. Both are compared on annual fiscal cost and on MVPF.
- "Maintenance first": an O&M-gap measure built from BOOST (O&M needed from the asset stock times r_j, minus O&M executed) with its own high BCR.
- In the macro bridge:
  - capex goes to public capital (`prog`, `ig_extra`) with `s_j` and `Rg_j`;
  - current spending goes to `prog_spend` / `g_extra`;
  - human-capital spending is flagged for Option B (a lagged human-capital channel).

**Step 8 — Financing route switch (PPP, PPA, concessional).** Routes:
- budget, commercial borrowing (tenor matters);
- budget, concessional (IDA or RST-type terms; grant element);
- utility on balance sheet (P2);
- IPP with a PPA (P3), with or without a WB or MIGA guarantee;
- viability-gap CfD (P4);
- grant or climate finance.

For each route, compute:
- the payment stream;
- the effect on the debt stock and on debt service;
- the PV of contingent or debt-like liabilities;
- a value-for-money test against the public route.

PPA tariff: T = [capex·CRF(WACC_IPP, n) + O&M] / E. The saving per kWh is the avoided cost minus T. The take-or-pay PV at the government rate is the debt-like liability; pass it to LIC-DSF-lite as a contingent liability, using the PPP stress rule in the notes.

Guardrails:
- competitive auction;
- size to expected dispatch;
- a tariff ceiling below avoided cost;
- FX matching;
- a PPA register (PEFA PI-10.3).

**Step 9 — Revenue returns (rules to state clearly).**
1. In the economic NPV, fees and taxes are transfers. They are excluded, apart from real resource effects.
2. In the fiscal ledger, they are included.
3. They raise MVPF through the denominator: each dollar recovered saves λ.
4. Appropriability share f_j feeds the user-fee parameter of the DIG models.
5. Do not count growth-induced tax revenue in the layer; the macro model does that.
6. Pigouvian revenue (CPAT carbon tax, subsidy reform) is itself a "measure" on the same scale. A tax that corrects an externality has a low welfare cost per dollar raised, so it is the natural first source of funds.
7. Spending and revenue-recycling options compete on the same MVPF ladder. This links CPAT (pricing and revenue recycling) to the spending side.

**Step 10 — Allocative efficient frontier.**
- Rank measures by NB_λ per public dollar.
- Cumulate PV fiscal cost against cumulative W to get the allocative frontier.
- The fiscal envelope comes from MacroFiscalModels and LIC-DSF-lite: the largest programme for which the fiscal rule stabilises debt and the DSF rating does not worsen.
- Use knapsack for lumpy projects.
- Constraints: absorptive capacity (maximum yearly scale-up), sector floors, the emissions target (Pareto: cost versus emissions).
- A risk layer: the CDPM / SISEPUEDE uncertainty ensembles, and RDM regret. Add Awerbuch portfolio logic for oil-price risk in islands.
- Compare the frontier portfolio with the current allocation from BOOST (COFOG by economic classification) to get a "reallocation gain". This is the bridge to PER and PFR practice.

**Step 11 — Bridge to MacroFiscalModels** (a small `psv_bridge.py`, parallel to `nmim_bridge.py`). It passes per year:
- `pub_cap` by sector, with `s_j`;
- `Rg_j` from the CBA, counting only market-output benefits (TODO item 2);
- the adaptation share (`prog_bbb` / `ig2`);
- `pub_spend`;
- `sav` (energy savings, also into DIGNAD-lite: TODO items 1 and 10);
- `rev` (fees and carbon revenue);
- financing shares (grant, concessional, commercial);
- contingent liabilities (PPA, PPP and utility: TODO item 9);
- execution leak and absorptive capacity (TODO items 3 and 8).

It returns the debt path, the DSF rating, the fiscal envelope and the GDP path, which feed λ and the envelope back. One iteration is normally enough; document the convergence check.

**Sector cards (how CBA extends to other sectors).** Each card is one row: measure, unit cost, outcome per dollar, monetisation factor, efficiency source, recurrent coefficient, payer type, fiscal externality, default BCR range, source, confidence. Defaults by benefit transfer, replaced by country CBAs when available.

| Sector | What the card uses (from the notes) |
|---|---|
| Health | DALYs × VSLY (Robinson-Hammitt reference case); DCP3 packages; opportunity-cost thresholds |
| Education | LAYS per $100 (Angrist et al. 2020) valued with returns to schooling |
| Social protection | Cash benchmark, MVPF; local multiplier as a macro effect only |
| Roads | Maintenance (Harral-Faiz; RONET / HDM-4) |
| Water and sanitation | Hutton BCRs |
| Resilience | Lifelines, GCA, DIGNAD |
| Agriculture | R&D versus input subsidies (Fan et al.; Goyal-Nash; Copenhagen) |
| Energy and climate | CDPM itself |

Include a starter table with default values from the notes, with confidence tags.

**Low-capacity rules (summarise as a box):**
- higher λ;
- `s` haircuts;
- execution delays;
- O&M first;
- prefer simple, standardised, auctioned instruments;
- cash transfers as the benchmark;
- scale-up limits;
- a PPP and PPA register.

## 3. Worked example spec (write, run and report a Python script)

Save the script and its CSV output as `sids_worked_example.py` and `sids_worked_example_results.csv` in this notes folder. You may start from `/tmp/claude-0/-home-user/10f05c0e-3ad4-522f-ac5a-3e36970d0c23/scratchpad/sids_example.py` (written by a researcher), but the final script must implement the PSV metrics.

**Island:**
- demand 300 GWh a year, almost all diesel;
- GDP USD 2 bn;
- public debt about 85% of GDP, at high risk of debt distress (illustrative);
- no market access beyond short-tenor commercial loans.

**Project:**
- 60 MW PV plus a 120 MWh battery;
- capex USD 120 m (about 6% of GDP), using island-premium unit costs from the notes;
- displaces 90 GWh a year;
- O&M about 1.5% of capex;
- life 25 years.

Avoided diesel cost: fuel plus variable O&M, about USD 0.23/kWh at Brent $80. Sensitivity at $60 and $110; the notes report Brent above $100 in late 2026.

Fuel excise on power diesel is a parameter, default 0 (often exempt). Fiscal capture share θ of fuel savings: 1 if the state utility's losses are covered by the budget; 0.5 base.

**Routes:**
- R1: budget, commercial loan at 8%, with a 7-year tenor, and also a 25-year tenor for comparison.
- R2: budget, concessional (IDA-like or blended): about 1.5% interest, 30 years, 5-10 years' grace.
- R3: IPP with a PPA, WACC 11% without a guarantee.
- R4: IPP with a PPA, WACC 8.5% with a WB or MIGA guarantee.

**Metrics for each route:**
- ENPV at 6%, without and with carbon at the WB shadow price;
- FNPV at the government rate;
- W, F and MVPF;
- NB_λ at λ = 1.2 and at 2.0;
- year-1 to year-7 net cash flow to the budget or utility;
- headline debt added (% GDP);
- PV of the PPA take-or-pay liability (% GDP);
- LIC-DSF contingent-liability stress add-on (% GDP);
- the "net fiscal liability", meaning the PPA PV minus the PV of avoided fuel imports or subsidies.

**Show the trap explicitly.** With a short-tenor commercial loan, debt service in the early years exceeds the fuel savings (liquidity trap), and headline debt jumps by about 6% of GDP (DSA trap). Concessional finance or a PPA with long tenor turns capex into an annual payment smaller than the fuel bill it replaces. Note the risks (take-or-pay, oversizing, FX).

**Sensitivity table:** oil price, capex ±30%, WACC, tenor, θ.

State every assumption with its source, or "illustrative". Do not invent sources.

## 4. Option B (less constrained by the CDPM method)

**B1. Multi-capital public-portfolio model.** Extend DIGNAD-lite / GIMF-lite so public capital has J types:
- energy;
- transport;
- water;
- adaptation;
- human capital (health, education), with a lag.

Each type carries `s_j`, `Rg_j` (or ψ_j), δ_j (responsive to maintenance), recurrent r_j and user fee f_j. Current spending types have their own channels: transfers to hand-to-mouth households, and wages.

Calibrate:
- the starting composition from BOOST (COFOG by economic classification);
- efficiency from the Herrera frontier and PIMA;
- returns from the literature and the sector cards.

Then solve for the growth- or welfare-maximising composition subject to the fiscal rule and the DSF (the Devarajan-Swaroop-Zou and Agénor logic). Pros: no need for project-level CBA; captures general equilibrium. Cons: identification of returns; data.

**B2. Empirical allocative efficiency, PFR-style.** Marginal returns by function, from BOOST panels and outcome data (Fan-Hazell-Thorat style), plus Herrera-Isaka potential savings and FDH frontiers. Package it as a "PFR allocative module" in the dashboard. Less structural, close to current World Bank practice.

**B3. Robust portfolios.** RDM across futures (oil prices, disasters, growth, cost of capital), choosing the portfolio with the least regret. This uses SISEPUEDE's own RDM heritage.

Compare A and B in a table: data, effort, consistency with World Bank practice, what each answers.

## 5. Upgrades to World Bank thinking

**Incremental:**
- Fiscal NPV and λ alongside ENPV in project and PFR work.
- One discount rate and one carbon price, applied consistently.
- PIMA, PEFA and BOOST haircuts, with efficiency kept separate from execution.
- Whole-life costing with recurrent coefficients in PERs.
- A PPA and PPP register, with PV liabilities in the DSA.
- Sector cards giving a common cross-sector metric in PFRs (fills the "allocative efficiency rarely quantified" gap).

**Radical:**
- λ derived endogenously from the macro and DSF models (the shadow price of fiscal space).
- DSA credit for self-financing climate assets ("net-of-savings" liabilities), with safeguards.
- Public-sector balance-sheet (net worth) appraisal (IMF FM 2018).
- One MVPF ladder for revenue and spending options (CPAT carbon tax and recycling versus spending).
- Distributional weights from the CPAT distribution module.
- AI-assisted BOOST tagging of budget lines to CDPM transformations, COFOG and climate tags, to measure the actual-versus-frontier allocation automatically.
- Real options and sequencing under deep uncertainty.

Present this as a table: idea, what changes, data, effort, risk, and whether it is consistent with current guidance.

## 6. Tool upgrade plan (phased; map each item to files and TODO items)

**Phase 0 (2-3 weeks): specification and data audit.**
- Category-to-payer lookup for CDPM CBA lines.
- Fix discounting in the CDPM CBA post-processing (one discount step; NemoMod lines).
- Parameter sheet with sources.
- Pilot countries: one SIDS (e.g. St Lucia, with data in the notes) plus Uganda (has a CDPM CBA run) plus Kenya (the MacroFiscalModels pilot).

**Phase 1 (4-6 weeks): PSV core.**
- `psv.py` plus a CPAT-layout workbook: tags, ENPV, FNPV, W, F, MVPF, NB_λ, EAC and recurrent costs, PIMA / BOOST haircuts.
- Runs on NMIM lines (186 countries) and on the Uganda CDPM output.
- Tests:
  - the ENPV identity;
  - λ = 1 reproduces InvestmentNeeds lens (b)/(c);
  - zero-haircut equivalence;
  - sign conventions (the CDPM CBA uses negative = cost; the MAC file uses the opposite).

**Phase 2 (4-6 weeks): financing routes and macro bridge.**
- PPA / PPP / concessional route module; contingent liabilities into LIC-DSF-lite.
- `psv_bridge.py` delivering TODO items 1, 2, 3, 8 and 9 (energy savings in DIGNAD and DIGNAR, sector `Rg_j`, absorptive capacity, BOOST execution leak, utility and tariff contingent liabilities).
- The SIDS pilot.

**Phase 3 (6-8 weeks): sector cards and frontier.**
- Seven sector cards with defaults and confidence ratings.
- Frontier and knapsack with constraints.
- BOOST comparison (actual versus frontier).
- λ feedback loop.
- Dashboard pages.

**Phase 4 (later): radical options and Option B.**
- Multi-capital model.
- RDM.
- Distribution weights.
- AI BOOST tagging.
- DSA net-of-savings treatment.

For each phase give deliverables, validation checks, data needed, risks, and the decision the user must take. House style: method note (current method only), version notes kept separate, a CAVEATS entry per task, and a CPAT-layout workbook alongside the Python. These are the norms of CPAT-AI and new-ai-tools.

## 7. Style

- Plain, precise English. Short paragraphs. Tables for comparisons and parameters.
- In the body, state each claim with a citation, or label it "our inference" or "illustrative".
- Mark unverified items with the tag from the notes.
- Do not invent numbers or sources. Where the notes conflict, say so.
- No change-history language: the methodology describes the proposal as it would be.
- Do not mention the AI tools, agents or the research process beyond the evidence-status note in section 1.
