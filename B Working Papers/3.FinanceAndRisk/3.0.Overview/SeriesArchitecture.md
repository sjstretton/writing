# Series 3 architecture: Finance and Risk

The plan for section 3 as one coherent series: its argument, its papers, their abstracts and outlines, and the terms they share. Agreed with Stephen on 29 Oct 2026. Every brief and working paper in the series follows it. The format rules for briefs are in `E Writing Instructions/Writing Standards/briefing-series-spec.md`; working papers follow `paper-standard.md`.

## The series argument

**Clean power in developing countries costs too much because its finance is bespoke and its risks sit with the wrong people. Standardize the contracts, remove the payment risk at source, and the projects become a few homogeneous asset classes, each sold to the investor who prices its risk most cheaply.**

1. The binding constraint is the cost of capital, not technology. Solar has no fuel cost, so its tariff is mostly the cost of the money that built it.
2. That cost is a stack of separable risks: offtaker payment, construction, currency, sovereign and policy, and the scarcity of loss-absorbing equity. Each has a cheapest holder.
3. Payment risk comes first because it prices everything downstream. A payment intermediary standing behind a standard power purchase agreement removes it at source (3.1).
4. Once payment risk is gone, a project's life splits cleanly: a construction asset that banks and development finance institutions can supervise, and an operating asset that bond investors can hold. Pool the operating assets, tranche them, and put first-loss equity underneath, and the senior paper can be rated at near developed-sovereign level (3.2).
5. Standardization is the multiplier: identical contracts make portfolios, portfolios make ratings, ratings make an asset class with a yield curve.
6. None of this removes the host state's exposure entirely. It converts open-ended, project-by-project fiscal risk into a contingent liability that is contracted, layered and conditional on the government's own conduct. Say so; never claim the structures are free to the host.

**Boundary with series 4.** Series 3 decides who bears a loss once a government has chosen to build. Series 4 changes what the government chooses. Conditional guarantees in series 3 are the point where the two meet; the large-scale incentive instruments (notional capitalized value, the Climate Investment Trust, sustainability-linked lending) belong to series 4. The Climate Investment Trust's regional funds are the natural provider of the first-loss equity tranche in 3.2; cite @CFPB42 for it.

**Out of scope.** The Sollar (`8.AdditionalPolicyPapers/8.2.FinanceAndRisk/8.2.1.TheSollar`) stays in section 8. The overview may mention it in one sentence as a non-credit alternative.

## Papers

| No. | Folder | Role | Brief and working paper title |
|---|---|---|---|
| 3.0 | `3.0.OverviewMobilisingPrivateCapital.docx` (rewritten as `3.0.OverviewMobilisingPrivateCapital.qmd`) | Series overview | Make Clean Power an Asset Class: Standardized De-risking for Developing Countries |
| 3.1 | `3.1.ClimateFinanceIntermediationForCleanPower` | **Flagship** | Guarantee the Contract, Not the Debt: A Payment Intermediary for Clean Power |
| 3.2 | `3.2.CleanPowerAssetClasses` (new) | Companion | From Projects to Asset Classes: Two-Stage Finance and Synthetic Sovereign Bonds for Clean Power |

### 3.1 Guarantee the Contract, Not the Debt: A Payment Intermediary for Clean Power

*Subtitle: Removing offtaker risk at source in developing-country power markets.*

**Question.** How can a developing country remove the payment risk that sets the cost of capital for clean power, at the lowest contingent cost to the state?

**Answer.** Put a creditworthy intermediary between generators and distribution companies. It buys power under one standard power purchase agreement, pays generators in full and on time whatever the distributor does, and is protected by a guarantee waterfall contracted in advance (distributor, subnational owner, national government, multilateral agency, donor contingency account). Guaranteeing the contract beats guaranteeing the debt: it covers every project selling into the same buyer, keeps the claim on the distributor alive, and costs the guarantor expected loss rather than face value. India's Solar Energy Corporation shows it can work, and also what goes wrong when distributor arrears are never fixed.

**Abstract (draft, about 150 words).** Solar and wind are cheap to build in most developing countries but expensive to finance, because lenders price the risk that a state-owned distribution company will not pay for the power. This paper proposes a payment intermediary facility: a national or regional institution that buys power from generators under a standard contract, pays them in full and on time whatever the distributor does, and recovers arrears itself, backed by a guarantee waterfall contracted in advance. I show that guaranteeing the contract dominates guaranteeing project debt when distributor defaults are temporary and recoverable, and I estimate the effect of offtaker risk on the levelized cost of solar power. India's Solar Energy Corporation shows that the design lowers tariffs, and its persistent distributor arrears show that the guarantee must be paired with utility reform. The state's exposure falls in size and becomes contingent, contracted and conditional, but it does not vanish.

**Brief outline (2,000–3,000 words).** Executive summary; 1 The cost of capital, not technology, prices clean power (LCOE vs WACC table); 2 The risk sits with the buyer of the power; 3 The intermediary and its waterfall; 4 Guarantee the contract, not the debt; 5 What India's Solar Energy Corporation shows, good and bad; 6 Design choices: declining tariffs, currency, national vs regional (ECOWAS), countries in debt distress (energy as a service); 7 What to do; Related papers.

**Working paper outline (6,000–10,000 words).** 1 Introduction. 2 Literature: renewable cost of capital (Steffen; Egli; Ameli et al.; Calcaterra et al.); de-risking frameworks (UNDP DREI); single-buyer and offtaker risk; payment security mechanisms. 3 Model: LCOE as a function of WACC; offtaker default as a hazard with partial, delayed recovery; Proposition 1 (offtaker risk premium in the tariff); Proposition 2 (contract guarantee vs debt guarantee: coverage, recovery, expected cost); Proposition 3 (expected loss of the facility under a layered waterfall; when it is insolvency-remote). 4 Calibration and illustration: stylized 100 MW solar plant at 5%, 8%, 12% WACC; India (SECI vs state-direct procurement, discom arrears from public sources); a regional facility example. 5 Precedents and failures: SECI (payment security fund, tripartite agreement, letters of credit; arrears and central liquidity schemes — check each from public sources), Nigeria's bulk trader NBET, others found. 6 Design: tariff profile, currency, national vs regional, energy-as-a-service for debt-distressed states, conditionality on utility reform. 7 Fiscal accounting: contingent liability, how to record and cap it. 8 Policy implications. 9 Conclusion. Appendices: proofs, calibration code.

### 3.2 From Projects to Asset Classes: Two-Stage Finance and Synthetic Sovereign Bonds for Clean Power

*Subtitle: Standard securities for construction, operation and first loss.*

**Question.** Once payment risk is removed, how do individual clean power projects become standard securities that institutional and domestic savers will buy at low cost?

**Answer.** Split each project at commissioning and standardize each side. Construction is financed by banks and development finance institutions against a contingent contract from the intermediary. Completed plants are pooled into portfolios and refinanced through tranched securities: first-loss equity from a regional fund, a thin mezzanine, and a senior "synthetic sovereign bond" whose rating comes from the guaranteed contracts, the equity cushion and a co-guarantee from highly rated sovereigns, not from the host. Where there is no contract to guarantee (transmission, storage, factories), a tiered bond guarantee does the same job, with explicit policy conditions. A local-currency senior tranche gives domestic savers a deposit-like green instrument.

**Abstract (draft, about 150 words).** Developing-country clean power projects are financed one at a time on bespoke terms, so each carries construction, payment, currency and sovereign risk to the same investors. This paper proposes turning them into a small number of standard asset classes. Construction is financed by banks and development finance institutions against a contingent offtake contract; on completion, plants are pooled and refinanced through tranched securities: first-loss equity, a thin mezzanine and a senior synthetic sovereign bond backed by guaranteed contracts and co-guaranteed by highly rated sovereigns. Using a one-factor portfolio loss model, I show how large the first-loss tranche must be for the senior bond to reach an investment-grade or near-AAA standard, and what refinancing saves on the levelized cost of power. Where no contract exists, as for transmission, a tiered and conditional bond guarantee plays the same role. Standardization, not subsidy, is what lowers the price.

**Brief outline.** Executive summary; 1 Bespoke finance is expensive finance; 2 Split at commissioning: two-stage finance; 3 Pool and tranche: first loss, mezzanine, senior synthetic sovereign bond; 4 Where there is no contract: tiered conditional bond guarantees; 5 Local currency and domestic savers; 6 What it saves (worked example); 7 What to do; Related papers.

**Working paper outline.** 1 Introduction. 2 Literature: project finance and renewables (Steffen 2018), securitization and asset-backed infrastructure debt, blended finance mobilization evidence, construction vs operating risk premia, green bonds and local-currency markets. 3 Framework: the two stages and the five asset classes (construction loan; operating senior bond; mezzanine; first-loss equity; local-currency senior tranche); Proposition 1 (refinancing gain from separating construction and operating risk); Proposition 2 (one-factor Vasicek portfolio: first-loss size needed for a target senior default probability, as a function of default correlation and recovery); Proposition 3 (standardization lowers the correlation-adjusted capital needed because portfolios diversify only when contracts are identical). 4 Calibration: stylized solar portfolio; table of first-loss sizes vs correlation and target rating; LCOE saving. 5 System assets without a contract: tiered bond guarantee with policy conditions. 6 Currency and domestic savings. 7 Precedents (verify each): IFC Managed Co-Lending Portfolio Program, Climate Investor One, GuarantCo, Brookfield-style operating-asset holding companies and yieldcos, IDB/AIIB infrastructure securitisations, India's IREDA and NaBFID. 8 Risks: correlated shocks (the host sovereign's crisis), moral hazard, rating agency treatment. 9 Policy implications. 10 Conclusion. Appendices: model derivations, code.

### 3.0 Overview (introductory paper, 3,000–4,000 words)

Rewritten last, after 3.1 and 3.2, so it states their results. Structure: the cost of capital is the barrier; the risk stack and who should hold each layer (table); the intermediary (3.1); the asset classes (3.2); how the pieces compose over a project's life; the boundary with series 4; the papers and their abstracts.

## Shared terms (series 3; use exactly these)

| Term | Meaning |
|---|---|
| cost of capital; WACC | The weighted average cost of capital of a project, in percent a year (real unless stated) |
| offtaker | The buyer of a project's power, usually a state-owned distribution company |
| payment risk (offtaker risk) | The risk that the offtaker pays late, partly or not at all |
| payment intermediary facility | A creditworthy institution that buys power from generators under a standard power purchase agreement, on-sells it to offtakers, and pays generators whatever the offtaker does |
| guarantee waterfall | The sequence of contracted guarantors behind the intermediary: offtaker, its subnational owner, the national government, a multilateral agency, a donor contingency account |
| standard power purchase agreement | One contract form used for every project the intermediary buys from |
| two-stage finance | Construction financed by banks and development finance institutions; refinancing into bonds once the plant operates |
| contingent power purchase agreement | An intermediary's commitment, made before construction, to buy the plant's power on completion |
| synthetic sovereign bond | A senior bond backed by guaranteed contracts on operating plants, a first-loss tranche and a co-guarantee from highly rated sovereigns, rated on that structure rather than on the host sovereign |
| first-loss tranche | Equity that absorbs portfolio losses before any debt does |
| tiered bond guarantee | A layered guarantee on bonds for system assets with no power contract (transmission, storage), conditional on agreed policy reforms |
| contingent liability | An obligation of the state that falls due only if a specified event occurs; the host's exposure under these structures |

## Citation keys for the series

```bibtex
@techreport{CFPB31, author={Stretton, Stephen J.}, title={Guarantee the Contract, Not the Debt: A Payment Intermediary for Clean Power}, institution={Climate Fiscal Policy Briefs}, number={3.1}, year={2026}}
@techreport{CFPB32, author={Stretton, Stephen J.}, title={From Projects to Asset Classes: Two-Stage Finance and Synthetic Sovereign Bonds for Clean Power}, institution={Climate Fiscal Policy Briefs}, number={3.2}, year={2026}}
@unpublished{StrettonWP31, author={Stretton, Stephen J.}, title={Guarantee the Contract, Not the Debt: A Payment Intermediary for Clean Power}, note={Working paper 4.1}, year={2026}}
@unpublished{StrettonWP32, author={Stretton, Stephen J.}, title={From Projects to Asset Classes: Two-Stage Finance and Synthetic Sovereign Bonds for Clean Power}, note={Working paper 4.2}, year={2026}}
```

Titles checked against each paper's YAML in the 29 Oct 2026 cross-review. The 3.2 working paper's YAML splits the title ("From Projects to Asset Classes") from the subtitle; the bib entries join them with a colon. Series 4 keys are in `4.SovereignIncentives/4.0.Overview/SeriesArchitecture.md`; series 1 keys in `briefing-series-spec.md`.

## Facts to settle in the series (from the source audit, 29 Oct 2026)

- **SECI's backing.** Older drafts say "credit lines with the Reserve Bank of India". *Time and Chance* ch. 9 describes a Payment Security Fund, a tripartite agreement (RBI, center, states) and letters of credit, with persistent discom arrears and central liquidity schemes. Use only what public sources confirm.
- **Fiscal space.** Do not claim the structures add nothing to host liabilities (*Time and Chance* ch. 14 withdraws that claim). Say the exposure is smaller, contingent and contracted.
- **Unsourced numbers in the old drafts.** The 3% cost-of-capital saving per guaranteed dollar, 10–20× credit-enhancement leverage, and "Paris decision paragraph 108". Source them, or cut or reframe them as assumptions.
- **Co-authors.** REPIF was written with Nils Zimmermann; SPIFA was developed by Evie Davey; the two-stage material came with Jasper Zimmermann. Acknowledge them in the working paper's first footnote.
