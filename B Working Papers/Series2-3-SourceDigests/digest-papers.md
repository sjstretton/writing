# Source digest for restructuring Series 2 (Finance and Risk) and Series 3 (Sovereign Incentives)

Prepared 29 Oct 2026. Nothing in the repo was edited. The source texts are in `scratchpad/src/`. Converted archive text is in `scratchpad/arch/`, `scratchpad/slidi/` and `scratchpad/more/`.

**Conventions.** "Master" means the current 2.1 `ClimateFinanceIntermediationForCleanPower.qmd` or 2.2 `ClimateInvestmentTrust.qmd`. **[CHECK]** marks a claim, number or citation to verify before reuse. **[CONFLICT]** marks a disagreement with a master or between sources. **[INTERNAL]** marks material that must not go into outward-facing papers. Word counts are approximate.

---

## 0. Headline findings

1. **NCV exists in four distinct formulations.** No source reconciles them, so the 3.1 paper will have to choose (detail in §3.1):
   - (a) Archived CIT (2024): interest on a notional value is paid into a beneficiary account.
   - (b) GeoProsperity intro: a notional value is "rewarded by a small interest rate". It covers forests *and* coal reserves (Amazon $1tn; China's and India's coal $1tn).
   - (c) *Time and Chance* ch. 21, "NCCV": stock × $/t, minus emissions each year. It works as *guarantee capacity* that lowers the cost of capital and includes a worked example.
   - (d) research.qmd and README: a "notional climate balance" based on carbon stocks *and* long-run emissions. It is translated into guarantee support and used up by business-as-usual (BAU) emissions.
   - The DPhil appendix (pre-cleanup) calls it a "long-term climate allowance or notional carbon-stock value linked to MDB guarantee capacity".
2. **The richest unused material for both series is the book *Time and Chance*** (`6.Additional/6.Books/6.1.TimeAndChance/TimeAndChance.qmd`, ~50k words). The most useful chapters:
   - ch. 7: forms of guarantees, and the IBRD indemnity as a "commitment device".
   - ch. 9: SECI facts and failures.
   - ch. 14: LCOE table, a seven-layer guarantee stack, and tail sizing.
   - ch. 15: ten-year sizing table.
   - ch. 16: theory of concessionality.
   - ch. 18: policy-lending fund and dynamic incentives.
   - ch. 19: Climate Investment and Insurance Fund (CIIF).
   - ch. 21: NCCV.

   Ch. 14 explicitly **retracts** the claim that the structures add nothing to host-government liabilities. That claim still appears in the masters and the older briefs (§5).
3. **The CIT numbers differ across versions.** The private-investor fee is 25% in the archive, master and book, but 10% in the technical summary and Climate Café note. The equity return is 10% or 15%. Doubling takes 2 years or 3. The global-tax illustration reads $50tn/$10tn in the original and $5tn/$1tn after correction. The master uses the corrected 25% / 10% / $20bn / $5tn figures.
4. **The SECI description is inconsistent** (§5). Some sources say SECI draws on "credit lines with the Reserve Bank of India". The book's ch. 9 describes a Payment Security Fund (2016), a tripartite agreement among the RBI, the centre and the states (2017) and letters of credit (2019). It also reports persistent distribution-company (Discom) arrears and two central liquidity injections. The 2.1 master uses the "credit lines" wording. **[CHECK]**
5. **SLL material splits into two kinds.**
   - Generic design logic from the internal note can be restated safely. Its strongest ideas: the KPI framework gap, the absence of a pricing method, step-down-only for sovereigns, the "runway problem", and credit enhancement vs direct payment.
   - SLIDIs (`33slidis.txt`) and the earliest "bonds with KPI" draft (Estevão) are public-safe. They give the fixed-coupon / third-party-rebate design and the trusted-intermediary model.

---

## 1. Series 2 sources (Finance and Risk)

### 1.1 `21repif.txt`: REPIF policy brief (Zimmermann and Stretton, 11 Nov 2024)
*~1,100 words.*

**Core argument.** Regional Renewable Energy Payment Intermediary Facilities (REPIFs), administered by a multilateral development bank (MDB), buy power from generators under standardised power purchase agreements (PPAs) at a fixed $/MWh for about 15 years. They resell it immediately under long-term Power Sales Agreements (PSAs) to Discoms or large industrial parks. The only purpose is to move non-payment and late-payment risk from the generator to the REPIF. A REPIF cannot become insolvent "by charter", because any shortfall is automatically covered by its guarantors.

**Guarantee waterfall, in order:**
1. The REPIF chases the Discom.
2. The subnational government that owns the Discom pays, under a pre-agreed condition of the REPIF operating in the region.
3. The national government pays, also pre-agreed.
4. In extraordinary cases the debt is added to the national debt stock and MIGA makes the REPIF whole.
5. Alternatively, a new MIGA-administered contingency account is funded by willing developed countries.

**Other mechanisms.**
- Technical partners help fix the causes of Discom arrears: ESMAP, REN21, the International Solar Alliance (ISA), IRENA, GiZ and AFD.
- Contingent PPAs can be signed **before construction**. The developer borrows at market rates (example: a Senegal solar developer borrowing from AfDB), then refinances after grid connection because offtake risk is now near zero. This is the seed of two-stage finance.
- One REPIF per major region, e.g. ECOWAS; North Africa and sub-Saharan Africa as separate REPIFs.

**Precedent.** SECI and its standard PPA (link given).

**Conflicts.** None with 2.1; this text is merged into it.

### 1.2 `21spifa.txt`: SPIFA brief (Apollo II / Geoprosperity series)
*~660 words, brochure format.*

**Core argument.** A Solar Payments Intermediary and Finance Agency (SPIFA) is a SECI-type institution aimed at small island developing states (SIDS) and sub-Saharan Africa. It addresses three problems: low creditworthiness, debt burden and scaling.

**Three components:**
- **(i) Renewable-energy contract intermediary, run by MIGA.** It guarantees revenue through capacity-tariff auctions and contracts for difference (CfDs).
- **(ii) Two-stage project finance, run by MIGA or IFC.** Equity plus loans during construction, then bonds secured on guaranteed cash flows, with pension funds buying the securitised flows.
- **(iii) Energy contracts for debt-distressed countries.** A "pay-as-you-go" energy service contract, with "the preferred creditor arrangement of the WBG" protecting investors from losses.

**Chart.** Investment needs, current vs 2030, for the world and EMDEs (CPI 2023; IMF 2023). No numbers are legible in the text.

**[CONFLICT]** SPIFA puts the intermediary in **MIGA**. REPIF and 2.1 describe a regional facility with MIGA as last resort. The preferred-creditor claim for a pay-as-you-go contract is asserted without any mechanism. **[CHECK]**

### 1.3 `21ssb.txt`: Synthetic Sovereign Bonds, standalone version
*~2,900 words. Also in the repo at `2.1/3.BackgroundPapers/Background-SyntheticSovereignBonds.qmd`.*

**Core argument.** Clean power is expensive because capital is expensive. The price-setting risk is the offtaker's credit, so **guarantee the contract, not the debt**. A debt guarantee protects the lender but leaves the cause untouched and usually ends the claim on whoever caused the loss. A contract guarantee removes the risk at source and keeps recourse alive, because the Discom still owes the money.

**Proposed structure.** A SECI-type central counterparty, national in big markets (Nigeria, Brazil) and regional for groups of small states. Contracts underwritten this way back "synthetic sovereign bonds" rated at developed-sovereign level. They are partly co-guaranteed by a developed-country consortium (a "climate club"), with MDBs arranging but not holding the risk.

**Design points:**
- **§6.1 Declining tariffs (worked example).** A flat real 5c/kWh from 2023 to 2043 vs solar at 2.5c by 2030 means paying double for 13 years. The alternative is 6c falling to 3c by 2030, with the "same present value". **[CHECK]** The present-value equality is asserted, not computed.
- **§6.2 Currency.** A hard-currency PPA moves devaluation risk to the state. Local currency narrows the investor base, so domestic savings are the natural funder.
- **Appendix A.1** Securitisation routes cash flows straight to bondholders.
- **Appendix A.2** Banks carry construction; bonds refinance operating plants.
- **Appendix A.3** The intermediary's guarantee alone will not earn the top rating. It needs a **dual-use equity fund** that co-invests and, for a fee, cross-guarantees other projects' bonds (first loss), with a final guarantor above it: a developed sovereign, Swiss Re or Munich Re.
- **Appendix B** Import content and the trade balance; build industrial capability.

**Justification for the developed-country guarantee.** The carbon value of the investment, citing "paragraph 108 of the Paris decision" on the social value of mitigation, via a GCF report. **[CHECK]** Para 108 of decision 1/CP.21 does refer to the "social, economic and environmental value of voluntary mitigation actions"; confirm the wording.

**Figures.** IEA 2021a/b: about $3tn a year of clean-energy investment by 2030, one third on supply, split roughly equally between China, developed and developing countries.

**SECI backing.** "Credit lines with the RBI and long-term indemnities from state governments". **[CONFLICT/CHECK]** See §5.

**Note.** This is the source of the "contract not debt" principle. It sits awkwardly beside the StandardizedTwoStage tiered *bond* guarantee (§1.10); the README resolves this by domain: guarantee the contract where one exists, the bond where none does.

### 1.4 `22bcit.txt`: CIT brochure
*~475 words.*

**Core argument.** Three functions: insurance in exchange for sovereign commitments, investment in early-stage renewables, and incentives. Donor-funded and WBG-managed, under Trust Fund Policy (2021).

**Mechanism.** National beneficiary accounts are allocated to specific populations or projects and serve as collateral. Funds "could be partially reclaimed" if a policy is reversed.

**Stakeholders.** Donors hold the voting shares. Private investors pay a percentage of returns as a fee. After 2050 the recipient countries are the beneficiaries. Charts cite CPI 2023 and IMF 2023.

**Note for Series 3.** The **clawback on reversal** is the clearest early statement of the asymmetric, persistence-rewarding feature that NCV also needs.

### 1.5 `22tech.txt` (technical summary) and `22cafe.txt` (Climate Café short, 2024)
*~1,750 and ~1,690 words. Near-identical; the Café version adds a DPF/KPI option.*

**Core argument.** The same three pillars. Profits are shared into post-2050 beneficiary accounts according to KPIs. The Café version allows "predefined baselines or, innovatively, DPFs with KPI-oriented repayment amounts".

**Mechanisms:**
- **Insurance.** The CIT is a **second-loss buffer** behind client-government first loss. It pays out only if a government defaults to covered bondholders or investors.
- **Investment.** Construction-stage equity, sold on after grid connection and refinancing.
- **Beneficiary accounts.** Doubling as loss-absorbing collateral for national loans. Protected from other fiscal uses until 2050.

**Numbers, all illustrative and unsourced:**
- Trust $5bn: $1bn donors plus $4bn recipient co-investment through development policy financing (DPF).
- $95bn from sovereign wealth funds, giving $100bn of equity and supporting $400bn of debt.
- A two-year construction cycle gives $250bn a year ($500bn over two years).
- Equity return 15%, fee 10% of profits, giving $1.5bn a year into accounts and "doubling every 3 years".
- Seven regional child funds (China, SAR, ECA, EAP, Africa, North America, South America) add $1.75tn a year, for $2tn a year in total and $4tn over two years.
- Incentive: cut emissions 10% a year at $100/tCO₂.
- The text also says "average project lifetime of two years", meaning the construction period.

**FAQ uses** of the insurance: surety on PPAs (SECI); de-risking **KPI-related sovereign bonds**; trusted-intermediary infrastructure lending; mobile-app deposits; arbitrage between DFI and sovereign bonds.

**[CONFLICT]** The master and the archive use a fee of about 25%, a 10% return and $20bn a year on $800bn of equity; these briefs use 10% and 15%. **[CHECK]** The arithmetic: $1.5bn a year on a $5bn trust is about 30% a year, so doubling takes roughly 2.6 years.

### 1.6 `22equity.txt`: Equity De-risking for Clean Energy (standalone, later folded into 2.2)
*~2,100 words.*

**Core argument.** Every de-risking tool makes debt cheaper but assumes equity underneath, and that equity is the constraint that binds last. The proposal is regional equity funds, set up with MDBs and RDBs, doing three jobs:
- **(1) Development-stage co-investment.** This signals quality and crowds in other investors. The fund also gathers failure-mode information it later uses to price first loss.
- **(2) First loss** in holding companies that own portfolios of operating assets. This makes their debt near risk-free. The cost saving comes from *combining* this layer with guaranteed contracts.
- **(3) Cross-guarantees** of bonds for projects the fund does not own. The diversification benefit is sold as fee income.

**Outcomes:** leverage where there is no local capital market; a deposit-equivalent green instrument in local currency; capital that is returned rather than granted.

**Design questions:**
- Governance: an investment committee with MDB and asset-manager members, published criteria, uniform due diligence.
- Price of first loss: it must be explicit and published, or the fund subsidises lenders.
- Recycling: holding to maturity finances a fixed *stock*; selling down finances a *flow*. The latter needs a secondary market.

Credited to two-stage work with Jasper Zimmermann. No numbers, no citations. Consistent with 2.2.

### 1.7 `22solar.txt`: Global Solar Economy Financing System (Sept 2023)
*Stretton, N. Zimmermann, Pablo Salas, Claudio Forner. ~6,400 words.*

**Core argument.** Three linked components:
- (i) **WB guarantees** to countries that run renewable auctions.
- (ii) An **SEFS-SPV**, housed in IFC, AfDB, DEG, Proparco or an investment bank. It lends *only* to refinance completed, operating parks, never construction. The debt-service share of PPA payments goes **directly from offtaker to SPV**, so the generator cannot divert it. The SPV securitises these flows into green bonds and matches bond currencies to PPA currencies.
- (iii) A **Global Solar Economy Equity Fund (GSEEF)** that co-invests in development, recycles capital and is the final loss-absorber. Its stated purpose is to avoid "privatised gain, socialised risk".

**Guarantor facility, Appendix 2 (the "IPPAGF").** It either lends temporarily to independent power producers (IPPs) to cover arrears, or **buys the IPP's claim on the Discom plus a late fee**. Recovery is first from the Discom, then the regional or national government, with the GSEEF as final layer. Operating costs come from a per-MWh surcharge, but payouts are *not* priced into tariffs. OECD donors back it.

**Other design points:**
- Declining or sunset tariffs, possibly indexed to an international PV cost index (§2.3).
- Pre-approved, pre-connected sites, including repurposed coal-plant grid connections. Cites Jindal and Shrimali 2022, *Energy Policy*, and Shrimali 2022 on Tamil Nadu (Climate Risk Horizons).
- A pay-as-you-go deal for SIDS utilities, e.g. 6c then 5.9c/kWh.

**Profit-sharing.** Reinvest everything at first. Later: 25% to adult citizens per capita (a "universal solar dividend"), 25% to investors, 50% reinvested until a 2050 target of 45 MWh per person per year. After that, 80% is paid out.

**Option example.** On a $1m project (80% SPV debt, 20% developer equity), the fund receives an option to buy 15% for $150k at completion. This avoids construction risk.

**Appendix 4 numerical example** (1 MW, $1m, 20% capacity factor, 1,752 MWh, 25 years):

| | Without de-risking | De-risked: more profit | De-risked: lower price |
|---|---|---|---|
| Debt rate (lower-middle income) | 12.5% | 7.5% | 7.5% |
| Price | $74/MWh | $74/MWh | $51/MWh |
| Interest | $100k | $60k | $60k |
| Equity required return | 15% ($30k) | 15% | 15% |
| Profit | $30k | $70k | $30k |
| Equity value | $200k | $467k (+133%) | $200k |
| Tariff change | – | – | −31% |

The 5-point rate cut is built from −2 (PPA guarantee), −2 (SPV securitisation) and −1 (political risk guarantee). Income-group rate assumptions: developed 7.5%→2.5%; middle-income 10→5; lower-middle 12.5→7.5; conflict 15→10. **[CHECK]** Interest-only perpetuity framing with no amortisation, and the rate cuts are asserted.

**Citations:**
- IRENA 2023, *The Cost of Financing for Renewable Power*: WACC 1.1% in Germany to >10% for PV in Ukraine; 4.4–5.4% in mature markets; up to 8.2% in the Middle East and Africa.
- IEA–IFC 2023: EMDE clean-energy spend must rise from $770bn (2022) to $2.8tn by the early 2030s.
- Ameli et al. 2021: Africa reaches net zero about 10 years earlier with lower WACC.
- Jäger-Waldau 2017, WACC-vs-LCOE chart.
- 2020 Joint MDB Climate Finance Report.

**Note.** The best source for the "standardised asset class" story: four investment classes, Pay-as-you-go wrapper, standard sites.

### 1.8 `23sollar.txt`: The Sollar (2.3)
*~3,050 words.*

**Core argument.** "Removes the borrower." One Sollar is an undivided share in installed solar capacity across a multi-country portfolio of parks.

**Definition.** One watt of *mean* output, or 8.8 kWh a year, which is about 5–10 Wp depending on site.

**Mechanism:**
- Revenue, net of an operator fee of about 10% that is performance-linked and cut when output falls short of the guaranteed annual output, is reinvested, so capacity per unit grows.
- After a lock-up of at least 5 years, holders may convert on one date a year into a fixed claim paying a dollar dividend. The dividend declines with panel degradation of about 0.5% a year.
- The conversion right is the value floor.
- Developers borrow Sollars from an institutional reserve held by IFC or IBRD, pay suppliers in them, and repay by issuing Sollars against the finished park. The rate in Sollar terms is low, zero or negative.
- The paper states plainly that this is **equity issuance, not free money**.

**What it does not solve:** offtaker payment risk (so it should be paired with 2.1), policy risk, currency risk (three denomination options: dollar, local or a basket), and the redemption pressure it creates (a queue, cap or market maker is needed). Custody and title are open.

**Ownership retention.** Incentives should favour domestic and retail holders. Issuing in developed countries against non-solar assets would make ownership flow both ways.

**Precedent.** IFC local-currency green bonds in India.

**Worked figures (Appendix A).** 44c revenue a year per unit at 5c/kWh, about 40c reinvested. **[CHECK]** The growth rate depends on installed $/Wp; the text itself says to redo the numbers.

**Guarantee layers (Appendix B):** the operator guarantees output; the purchaser guarantees price; the intermediary guarantees payment; the administrator guarantees conversion; international institutions guarantee the scheme in its early years.

**[CONFLICT, minor]** *Time and Chance* ch. 13 calls it a "solar-panel-backed currency"; the 2.3 paper rejects the currency label.

### 1.9 Repo: `2.2/8.PreviousVersions/StandardizedTwoStage/StandardizedTwoStage-previous.qmd` and README
*Stretton and Jasper Zimmermann. ~1,600 words.*

**README.** The paper was split on 17 Sep 2026:
- part (i), multi-tier *bond* guarantees, became 2.1 §3.4, for system assets with no PPA: transmission, EV charging, factories;
- part (ii), regional equity funds, became "2.4 Equity De-risking", now in `2.2/8.PreviousVersions/EquityDeRiskingForCleanEnergy.qmd`.

**[CONFLICT]** The README still says "2.4"; the numbering has since moved to 2.2.

**Core argument.** About $4tn a year globally and over $1tn in EMDEs (IEA 2021). Finance must be priced near IBRD lending rates (an IDA terms image is cited).

**(i) Up to three loss-absorbing tiers on green bonds** issued by regional or national clean-energy system authorities:
- tier 1 is the government responsible for energy regulation, e.g. an Indian state or Mozambique;
- tier 2 is the national government where states regulate;
- tier 3 is a donor-backed SPV (an OECD consortium or a WBG multi-donor trust fund);
- the result is rated "AAA".

**Conditionality.** Standard PPAs and a coal phase-out schedule. Local-currency debt becomes possible.

**(ii) Regional equity funds.** Development-stage co-investor and first-loss core equity for buy-and-hold holding companies. Cross-guarantor. Diverse investors, including rich governments investing on behalf of poorer regions.

**Roadmap links:** IFC Warehouse-Enabled Securitization Platform (WESP) as exit route; the private-sector concessionality trust fund; co-financing funds; Global Priority Programs. All cite the Evolution Roadmap §38. Also cites WBG April 2023, *Scaling Up to Phase Down* (Report AUS0003306).

**Note.** This is the cleanest statement of a **tiered, standardised guarantee** as an asset-class generator.

### 1.10 Repo: `2.1/8.PreviousVersions/SyntheticSovereignBonds/README.md`
Synthetic sovereign bonds (SSBs) are "not a separate proposal". They are the refinancing instrument that sits on top of the intermediary: "the same architecture stated twice". They are merged into 2.1 §3.2 and Appendix A. If SSBs become a separate Series 2 paper again, this reasoning has to be revisited, e.g. by separating the *bond and asset-class design* from the *institution*.

### 1.11 Archive `2.1/9.Archive/WP2-A Solar Payment Guarantor-SSAdjustmentsAnd-Acepted Changes.docx`
*~8,200 words, a working file (the unadjusted version is ~1,100 words).*

**Contents:**
- An expanded REPIF brief that bundles three instruments: REPIF, SLIDIs and regional Sustainable Technology Equity Funds (STEFs).
- **The SLIDI variant here:** refunds are calculated retroactively as a percentage of interest paid in the previous assessment period, e.g. every three years over a 12-year loan. A note suggests "e.g., half" of interest refunded.
- **REPIF scope:** the payment-guarantee function only, not SECI's tendering and advisory roles. Advisory work is left to partners (GiZ, ISA, seconded SECI staff).
- **REPIF green asset-backed securities (ABS):** state- or cooperative-owned plants that have earned revenue for at least a year are securitised, and the proceeds are *legally required* to be reinvested as equity in new projects. This is a "virtuous cycle" with no use of fiscal space.
- **SECI notes** (look AI-generated; footnotes such as `【100†source】`): introduced around 2013 under the National Solar Mission phase II; tripartite agreement letting withholding of central transfers; "over 50 GW"; Miniratna Category-I status; and the SECI/IREDA relationship.
- **Citation:** Ketkar and Ratha 2001, "Securitization of future flow receivables" (real; Ratha's book is also referenced). Avinash Persaud is quoted (3% vs 12.5% solar WACC, Europe vs Brazil) along with the Bridgetown Global Climate Mitigation Trust ($500bn SDRs).
- **Drafting notes:**
  - Discoms pay bondholders first via the SSB issuer, then generators via the "SPIFF".
  - House both facilities in MIGA.
  - MIGA backed by government indemnity, then reinsurance (Swiss Re), then an equity fund.
  - A "points system" in which SLIDI participation helps qualify for the SPIFF: an early link between Series 2 and 3.

**[CHECK]** The SECI start date (other sources say 2011), "50 GW" and "40 GW by 2023" are unsourced. The reference list (e.g. "World Bank, *Financing Climate Action…*: A Guide for Policymakers"; "IFC, *Securitization of Renewable Energy Assets in Emerging Markets*") **looks unverifiable or generic**.

### 1.12 Archive `2.2/9.Archive`

**`The Climate Incentives Trust.docx` (~3,900 words; tracked version Apr–May 2024 ~4,100).**
- This is the origin of NCV (§3.1). Key ideas:
  - **Universal vs additionality-based incentives**: additionality invites strategic delay.
  - **Trusts with beneficiary accounts**: allocate on policy action, tax back on reversal; current finance is sized by the account.
  - **Dynamic incentives**: act now or miss out, with renewable auctions' falling prices as the analogy.
  - **"Dual indemnification"**: a AAA guarantee protected two or three times, by the government, then the global equity fund, then the WB or another AAA entity.
  - **The insurance-company / Berkshire Hathaway analogy**: returns on insurance float.
  - **Comparison to the IMF Resilience and Sustainability Trust (RST)** investment accounts.
- **Private investor fee** about 25%, with voting rights only on the investment side.
- **Numbers:**
  - Eight funds give $800bn of equity, of which $40bn is beneficiary accounts.
  - A 10% return with 2.5% to the trust gives $20bn a year, "doubling every two years".
  - Incentive: $100/t × 10 Gt × 10% = about $100bn a year.
  - The tracked version corrects the $100/t global-tax illustration to about $5tn raised and about $1tn from China (the original had $50tn and $10tn) and the subsidy to about $500bn a year (originally $5tn).
- **Condition:** net national beneficiary returns must always be positive (an incentive to join), plus a within-scheme incentive to outperform.
- **"Grand deal" scope:** a net-zero plan plus procurement auctions, a "broader renewable auction".
- Cites "Estevão 2023" for KPI bonds.

**`TrackedChangesVersion/TechnicalSummary…docx`.** Same as `22tech`.

**`0. MobilisingPrivateFinanceForClimateBriefingPaperSeries.docx` (~1,900 words).** A plan for a briefing series. It lists six failures: weak policy; high cost of capital; low capacity; no time-dynamic incentives, with high USD rates, early carbon markets and falling technology costs all encouraging delay; scarce core capital; and unclear buildout targets. Papers in the plan:
- **KPI bonds.**
- **A trusted intermediary.** Poor performers pay roughly their *normal sovereign rate*; good performers pay the *intermediary's rate*. This is a clean pricing rule for SLL design.
- **A multi-tier portfolio loan guarantee.** Tier 1 is the host government, which holds lenders harmless or adds the default to its WB debt. **Tier 2 is the country's CIT buffer account**, funded by fund profits, HDC carbon taxes, the IMF RST or donors. Tier 3 is the WB or an HDC-backed multilateral.
- **The CIT.**
- **The IFC clean-energy model:** pay-as-you-go per MWh.
- **"100% Clean Energy Transition Program Assistance".**

This is the clearest early statement of **"guarantee plus country balance"**, the core of NCV and guarantees.

**`Structured Finance for Global Clean Energy Abundance.docx` (~1,100 words).**
- **"Virtual capital":** structure like an insurer, not a bank. An insurance fund with paid-in plus callable capital, a "coalition of the willing", guarantees lending so it uses no WB or SPV capital.
- **Two institutions:** a "SECI for Africa", perhaps a regional arm of MIGA, with the WB and IMF as "advisors but also debt collectors"; and a Clean Energy Fund.
- **The fund has three accounts:** a Global Public Goods account (donors, absorbs risk); country-allocated trust accounts (reward and enforce commitments); and **fiscal resilience buffer funds** that countries pledge as collateral to cut sovereign borrowing costs.
- **Four investment classes:** initial equity, initial debt, final equity, final debt. This is the explicit "standard asset classes" taxonomy.
- Missing in the WBG: a high-risk, high-return arm.

**`SubstitutingPPAs.docx` (~470 words).** Legacy coal PPAs should be turned into financial contracts that any source, including solar plus storage, can satisfy. India's two-part tariffs (variable plus sunk) make this tractable; refinance the sunk part. Citations:
- Bais 2022: 22% of Indian capacity is non-performing assets, $40–60bn. **[CHECK]**
- Lim et al. 2012.
- A Ministry of Power bundling scheme, Nov 2021.

Relevant to 1.5, and to the coal side of NCV.

**`SuperHeroFund.docx`.** A plain-language CIT pitch with nothing new.

**`IndiaNote-V1.0.docx` (~33k words; also the 1.5 background).** Relevant passages:
- IREDA and PFC lending to renewables at about 10% in 2021.
- Union and state co-guarantee of PPAs (via the UDAY scheme) to deter unilateral PPA changes.
- PPA securitisation as "novel in India", needing credible 25-year guarantees.
- A standard due-diligence "gold-standard" certification for lower-rate loans (cites Schwarz 2020).
- An SECI-affiliated SPV as a risk-free intermediary.
- NaBFID issuing sovereign-backed green bonds for refinancing.
- **Two-phase lending:** development-phase lending by banks and IREDA, then securitised refinancing.
- Standardised storage financing packages.

---

## 2. *Time and Chance* (book 6.1). Highest-value unsummarised source
`6.Additional/6.Books/6.1.TimeAndChance/TimeAndChance.qmd`, ~50k words. Chapters most relevant to the two series:

**Ch. 3: "Green superseniority".** Make green lending structurally senior to other sovereign or utility claims. It needs no new money, but other creditors become junior, so it must be set before other debt is issued or negotiated in a restructuring.

**Ch. 7: Forms of guarantees.**
- Guarantee *only* the risks the market misprices: policy, payment and political risk. "A guarantee against everything is an equity investment with extra steps."
- A sovereign guarantee is a contingent liability that runs out fastest where it is most needed.
- **MIGA** reinsures, so the risk leaves its balance sheet.
- **IBRD** guarantees are backed by a state indemnity. The long-term relationship makes the guarantee a **commitment device**: the state guarantees its own state-owned enterprise at a *higher* rating by routing the promise through an institution it cannot afford to let down. "Concessionality generated not by spending money but by borrowing credibility."
- SECI is "the IBRD principle applied domestically".
- SPV order of payments: bondholders before equity.

**Ch. 9: What the record shows.**
- **SECI** was set up in 2011:
  - 25-year PPA plus back-to-back PSA;
  - Payment Security Fund (2016), funded by the centre and topped up by Discom payments and developer penalties;
  - 2017 tripartite agreement among the RBI, the centre and the states, allowing transfers to be withheld;
  - letters of credit required since 2019;
  - SECI auction tariffs about Rs 2.44/kWh by 2017.
- **Failures:** Discom dues Rs 1.32tn in mid-2022 and Rs 779bn in March 2024 (about Rs 273bn overdue). Central liquidity injections of Rs 90,000 crore in 2020, raised to Rs 135,000 crore. The regulator ordered SECI to pay change-in-law claims first.
- **South Africa REIPPPP:** real equity returns 17% in round 1 and about 9.5% in round 4. Tariffs fell about 70% over three rounds. Treasury guarantee behind Eskom. The 2017 attempt to renegotiate round-4 contracts damaged credibility.
- **Zambia Scaling Solar:** an IDA partial risk guarantee; bid of 6.02c/kWh vs 12c unsolicited a year earlier.
- **Cost-of-capital decomposition:** an "Observatory" study for Kenya and Senegal finds the sovereign base rate is 60–90% of solar cost of capital in Africa, 35% in China and about 10% in advanced economies. So guarantees address the sector premium, and only safe intermediaries address the base rate. **[CHECK]** This is presumably the IEA Cost of Capital Observatory; verify.
- **"Long-term relationships and credit ledgers":** a missed payment becomes a ledger entry, not a default.

**Ch. 10: Criteria and worked scheme.**
- Three criteria: **cost–risk effectiveness**, including whether the guarantee acts as a commitment device; **capital efficiency**, with the warning that efficiency won by hiding where the risk sits "is the 2008 financial crisis"; and **system-dynamic potential** (self-financing, a commons fund).
- The scheme combines the SPV, the equity fund with a $100k cap per individual investor, 25% profit-sharing, and the option example.
- **Who gains:** in one deal, about three quarters of the equity uplift goes to the developer and one quarter to the public fund. Consumers gain through later auctions.

**Ch. 14: Where the risk goes (key for 2.1/2.2).**
- **LCOE table** ($800/kW, 20% capacity factor, $12/kW-yr O&M, 25 years). At 4% / 6% / 8% / 10% / 12% / 15%: 3.6 / 4.3 / 5.0 / 5.7 / 6.5 / 7.8 c/kWh. The finance share of LCOE rises from 30% to 68%.
- **IEA Cost of Capital Observatory:** finance is about half of solar LCOE in EMDEs in 2021, vs 25–30% in advanced economies and China. Median solar WACC just under 10% in India and Mexico and about 13% in Brazil. One percentage point less across EMDEs saves about $150bn a year. Merchant projects carry a higher WACC; about 90% of projects have contract support.
- **Three cases:**
  - Construction risk is about two years and bounded, so two-stage finance confines it.
  - Guarantees buy a lower cost of capital *with flexibility*. The government, offtaker, developer and guarantor each give something up.
  - Currency risk can be hedged. **TCX** (2007) covers more than 140 currencies and had supported more than $10bn of local-currency funding on about $1.8bn of capital by 2024, with $3.5bn laid off privately. Frontier hedges cost 600–1,200 bp.
- **Correlated-shock sizing:** a $100bn guaranteed portfolio, a 5% equity buffer, 15% of offtakers in arrears and a 25% FX loss give about $15bn of loss. The buffer covers $5bn and the AAA guarantor bears $10bn with recovery rights. "Used but not used up" is true in expectation and false in the tail.
- **Retraction:** the claim that the structure "adds nothing to developing country government liabilities" is withdrawn. It adds a contingent liability, but one that is *conditional on the government's own conduct*.
- **Interest-rate robustness:** what matters is the *gap* between rates, not their level.
- **One equity pool, five names:** GCREF (ch. 10), clean-energy fund (ch. 11), policy-lending fund (ch. 18), CIIF (ch. 19), CIT (ch. 20).
- **Seven-layer stack:**
  1. contract (declining, currency-matched);
  2. offtaker guarantee (SECI-like or MDB-routed sovereign guarantee);
  3. two-stage finance;
  4. ring-fenced SPV paying bondholders first;
  5. sovereign first loss by indemnity, as a ledger entry;
  6. equity buffer as second loss;
  7. AAA sovereign, MDB or reinsurer for the tail.

  This is the best single frame for Series 2.

**Ch. 15: Overcoming the balance-sheet limit.**
- A guarantee that "combines the best of MIGA and IBRD": a sovereign indemnity *plus* reinsurance of the residual.
- AAA green debt as a *new asset class* that opens the investment-grade universe.
- Funding vs financing.
- **Ten-year sizing, solar in EMDEs excluding China:**
  - investment $2.0–2.5tn, of which investment-grade debt $1.6–2.0tn at 80% gearing;
  - equity buffer $80–100bn at 5%, recycling;
  - AAA contingent reserve $160–200bn, about 10%;
  - 20–30 SECI-scale intermediaries;
  - hedging capacity $300–400bn.
- **Toolkit:** superseniority, indemnification, finance-ready policy, securitisation of policy guarantees, credit lines, off-balance-sheet treatment.
- WBG climate finance of $21bn over 2018–22, about 40% of MDB climate finance. **[CHECK]** This looks low; it may mean a single year.

**Ch. 16: The safe-intermediary theory of concessionality.**
- Two keys: a AAA institution does the borrowing, and the long-term relationship does the risk reduction.
- Guarantee the **state agency** (a repeat player), not the one-off developer.
- Concessionality can be *manufactured* from ratings, relationships and diversification.
- Answer to "socialised risk, privatised return": a public equity fund in the same capital structure captures the upside.
- Supply-chain financing credits per MW installed, kept out of carbon markets.

**Ch. 17: Why the World Bank.**
- Four barriers: the capital-adequacy framework (G20 CAF panel 2022), shareholder politics, a risk culture in which "a guarantee never called looks unneeded", and missing functions.
- Design principle: off balance sheet, separately capitalised, additional to the envelope.

**Ch. 18: Scaling up policy lending.**
- A WB-managed equity fund absorbs the risk of an *additional* policy-lending envelope (cites Heine et al. 2023, unpublished EFI note), MIGA-style or like RST investment accounts.
- **Dynamic incentive:** fund returns above a cap are distributed as **new shares to early-acting countries**, diluting the impact investors down to their agreed maximum return.
- National reward funds are conditional on policy *and* on the sovereign taking first loss in its own territory.
- Governance: the WB keeps control; rule changes need a shareholder super-majority.
- Low-capacity countries: energy as a service at declining prices (Wright's law).
- **Green savings accounts** where there is no bond market.
- **Worked example:** $1m project, 80/20 debt/equity, debt at 8%, equity at 18%, $100k revenue. Refinancing at 4% raises equity income from $36k to $68k. At 12% construction debt and 8% refinancing, it goes from $4k to $36k.

**Ch. 19: CIIF as a Financial Intermediary Fund (FIF).**
- Government guarantees the price per MWh; the fund is second guarantor; the WB is final.
- The fund raises equity through AAA green bonds and **green deposit certificates**.
- It acts as an insurer for a fee.
- Priorities: coal replacement, and a JET-P package for *every* coal plant.
- **Cited:** the "LSE study" that debt/GDP rises 70pp at market rates vs 10pp at WB rates. **[CHECK]** The EFI note's footnote is an FT link; locate the underlying study.
- Also cited: G20 Triple Agenda 2023 ($3tn a year additional by 2030, of which $1.8tn climate); the Bridgetown Global Climate Mitigation Trust.

**Ch. 20: CIT,** matching the archive, plus:
- **"Who speaks for 2050":** rules fixed in advance with super-majority protection; transparent balances; the beneficiary country has a voice on rules and audit rights but no investment vote; independent trustees.
- **Closing line:** an account held in trust "grows when the country acts and shrinks when it retreats", which "creates a constituency for persistence".

**Ch. 21: NCCV.** See §3.1.

**Chs 22–29.** The offtaker's own economics, transmission (the hardest case), the debt trap, the debt sustainability framework with ten recommendations, coal buy-and-retire with securitisation, and Vietnam as a case study (an unbankable PPA clause and curtailment). Not summarised here; useful for the hard-cases sections.

---

## 3. Series 3 sources (Sovereign Incentives)

### 3.1 Notional Capitalised Value: every formulation found

**(a) Archived CIT (2024; also 2.2 master l.90 and *Time and Chance* ch. 20).** Applies "where incentives needed are greater than funds available for profit sharing". Define, say, the remaining Amazon as worth $1tn and pay the *interest* on it into the beneficiary account. Each country holds two accounts: the beneficiary account and the NCV account. Declared "beyond scope".

**(b) GeoProsperity intro (`7.Website/papers/GeoprosperityIntro.docx`, appendix C).**
- "Recognize notional climate assets, starting with forests and coal… rewarded by a small interest rate." Brazil's Amazon at $1tn, "as might China's and India's coal reserves".
- Framed as recognising **long-term stock effects** in strategic country partnerships, alongside an all-in energy rate and a "global long-term borrowing facility, akin to a global treasury".
- Appendix A of the same document holds the three-tier guarantee, in which the WB rating is "used but not used up".

**(c) *Time and Chance* ch. 21, "Notional Capitalized Carbon Value (NCCV)". The only worked mechanism.**
- **Problem:** stock-rich countries cannot turn natural wealth into finance. Leaving fossil fuels in the ground earns nothing. A country that kept its forest gets nothing, while one that clears and replants is paid.
- **Definition:** forest stock 100 MtCO₂ × $100/t = **NCCV $10bn**. Each year it falls by the notional cost of net emissions: 1 Mt a year × $100 = **−$100m a year**.
- It is a **stock** measure (it rewards preservation, not change) and **notional** (a basis for an entitlement, not a sale price).
- **Use:**
  - Release over 10 years, about $1bn a year of NCCV capacity.
  - MDB guarantees cut the cost of capital by about 3% per dollar guaranteed, so $1bn of guarantees a year gives $30m a year of interest savings, "$300m over ten years".
  - One third is earmarked for forest protection: a 3% WACC cut minus a 1% fee gives a net 2%. The fee makes the scheme partly self-financing and screens out projects that do not need support.
- **Tipping-point refinement:** the next 10–20% of forest near an ecological threshold gets a *leveraged* value, because of forest–rain feedback.
- **Triple role:** a reward for keeping stocks (forest and unburned fossil fuel), a tax-like signal because emissions shrink it, and an allowance for cost-of-capital cuts.
- **The low fiscal cost** comes from the MDB indemnification structure: "a guarantee is not a grant".
- **The resource being spent** is the gap between the risk the WB actually bears and the risk the market prices. It needs no appropriation.
- **[CHECK]** Is the $1bn a year of capacity a *flow* of new guarantees or a *stock* cap on outstanding exposure? If guaranteed loans are long-dated, savings build up beyond $300m. The 3% saving per guaranteed dollar is asserted. The chapter cites the companion volume for the claim that the forest's value exceeds offset prices.

**(d) Research page (`7.Website/research.qmd` l.76–78) and `3.1…/README.md`.**
- The problem: marginal reductions measured against an unobservable counterfactual neglect absolute emissions, long-run stock–flow performance and **stocks never cut**.
- The proposal: a notional climate balance tied to carbon stocks *and* long-run emissions performance, turned into guarantee support rather than cash, and used up by BAU emissions.
- **The balance is borrowable and avoids the fiscal-transfer problem** in donor capitals. It **decays if nothing is done**, so the incentive exists from year 1.
- The README notes it replaces the working title "Guarantee-Based International Incentives for the Delivery of Strong NDCs".
- `A Writing Instructions/PAPERS.md` calls 3.1 "the core idea behind proposal 1" (the DPhil).

**(e) DPhil pre-cleanup appendices (`C Research Proposal/PreviousVersions/…before-cleanup.docx`).**
- Appendix B4: "long-term climate allowance or notional carbon-stock value linked to MDB guarantee capacity", to be kept "as one experimental dynamic-incentive design rather than assumed to be the thesis's final solution".
- Appendix C's "dynamic incentives" layer: "time-varying concessionality; performance-linked guarantee capacity; experimental climate allowance / carbon-stock credit". The quantities to model are timing, credibility, persistence and **moral hazard**.
- Appendix D turns planning claims ("nearly free", "inherently profitable", "scales to trillions") into **hypotheses** to test: expected losses, capital usage, additionality.

**Supporting logic elsewhere:**
- *MDB envelope note (§3.4):* results-based payment rewards whoever governs later, arrives about 4 years after the reform cost is paid, and rewards weak NDCs.
- *Reforming MDBs (§3.5):* universal, declining incentives.
- *Klaus/WTP project (§4):* three baseline approaches.
- *CIT:* the clawback on reversal.
- *SPECIALISMS.md 3.7, 4.8:* "pay governments with balances and guarantees they can borrow against"; small island states as pilots.

**Design questions the 3.1 paper must settle, none of them resolved in any source:**
- **Stock base:** forest carbon only, or also fossil reserves? The coal case rewards a country for *not* extracting, which brings valuation and moral-hazard problems.
- **Decrement:** gross or net emissions? Against what trajectory?
- **Reward form:** interest paid into an account (a), or guarantee headroom (c/d)?
- **Earning and loss:** is NCV a cap on guarantee exposure, a fee rebate, or a first-loss layer? How is it earned back or lost on policy reversal (the CIT clawback)?
- **Valuation and leverage:** the price per tonne, and the leverage weighting near tipping points.
- **Link to NDCs:** see the MDB-envelope point on NDC-stringency incentives.

### 3.2 `32sll.txt`

*Removed: summary of a World Bank internal document. Not for use in public text.*

### 3.3 `33slidis.txt`: SLIDIs (Estevão, IIF; Stretton; N. Zimmermann; personal capacity)
*~6,900 words. Repo copy `6.Additional/3.SovereignIncentives/3.3.SLIDIs/SLIDIs.qmd` is identical. Presented at the Public Debt Management conference.*

**Core argument.** Sustainability-linked bond (SLB) issuance has fallen since its 2021 peak because of complexity, greenwashing and **variable coupons that investors dislike**. Sustainability-Linked Intermediated Debt Instruments (SLIDIs) **separate investor return from sovereign incentive**: investors get a fixed coupon, and the borrower's *effective* rate depends on KPIs through a third party.

**Option 1, side payments:**
- The sovereign issues a fixed-coupon KPI bond at market rates.
- A WB results-based payment or a donor trust fund pays a **rebate at maturity** if the KPIs are met.
- Payment can be made conditional on a minimum level of private participation.
- The WB buys **about 1% of each issue** to signal "senior" status: the halo effect.
- Scale: rebates of "tens of billions a year" for a $2tn-a-year portfolio, possibly funded by **levies on bulk fossil-fuel sales in donor countries**.

**Option 2, trusted intermediary (recommended):**
- An SPV or the WB, co-guaranteed by a coalition of developed countries, issues low fixed-coupon bonds.
- It on-lends at a higher fixed nominal rate as SLLs.
- If KPIs are met at maturity, or at milestone years for long bonds, **part of the interest already paid is refunded**.
- The spread makes the vehicle self-sustaining, "a specialised development bank".
- GiZ or AFD provide MRV and technical assistance.

**Risk.** A WB "symbolic" purchase links default on *any* approved bond to the relationship with the preferred creditor (cross-default deterrence), making the bonds effectively "super-senior".

**KPI types:** policy reform (carbon pricing, feebates, auctions); clean infrastructure (national renewable share); forest cover.

**Rules:** standardised baselines to stop weak baselining; capacity assessment; SMART KPIs; WB regional KPI norms; private-participation thresholds.

**Numbers:**
- IEA 2023: $2tn a year for developing countries, $5tn a year globally by 2030.
- WB 2023: private sector supplies 80% (90% excluding China).
- OECD: $34bn in 2022 vs the $100bn pledge.
- Sovereign SLBs 0.9% of issuance (CBI 2024).
- Average step-up 25 bp, which may be inadequate (CBI 2024).
- A debt-for-nature swap example: $85m guarantee plus $656m political-risk insurance, savings "$323m".
- WB climate share target 45% (FY25).

**Citations given:** Ahren 2024 (*Environmental Finance*); Bhattacharya, Songwe, Soubeyran and Stern 2023; Bouzidi and Papaioannou 2021; Bolton, Gulati and Erlandsson 2022; Cassimon and Essers 2013; Chowdhury and Tadjoeddin 2022; CBI 2024; Diwan, Kessler and Songwe 2024; Giráldez and Fontana 2022 ("OUP vol 17(1) 8–19"; probably *Capital Markets Law Journal* **[CHECK]**); Hurrell 2024 (*OxREP*); IEA 2023; IMF 2023 blog; Kölbel and Lambillon 2022; Lefournier 2023 (Institut Louis Bachelier); Maplecroft 2024; McGeady and Baskaran 2023 (CSIS); McKinsey 2022 and 2023; OECD 2024a; OECD 2024b (Horrocks et al.); Silva 2021; the Uruguay SSLB framework (2022); World Bank 2023 *Detox Development*; World Bank 2024 climate finance.

**[CONFLICT]**
- `combined.txt` calls SLIDIs "Sustainability-Linked *Development* Instruments" whose "coupon or concessionality steps with progress". The paper's design is a *fixed* coupon with *refunds*.
- The same swap's savings are given as $323m here and roughly $1.1bn over 17 years in the internal note. These may be different measures. **[CHECK]**
- The text says "Figure 1" but the figure is captioned "Figure 2".

**Earlier SLIDI archive (`3.3.SLIDIs/9.Archive`), public-safe:**
- **"bonds with kpi.docx"** (Estevão; ~2,200 words), the origin:
  - Fixed coupon set by the market.
  - KPIs negotiated with a development partner, either achieved *during* the bond's life (Model 1, like a Program-for-Results) or as a *precondition* (Model 2, like a DPO).
  - On achievement the issuer gets a **concessional, longer-maturity loan** disbursement, so bond plus loan cost less in present value than a vanilla bond.
  - De-risking: halo effect; using the proceeds to retire expensive debt; MIGA cover of coupon non-payment; a minimum private-participation threshold.
  - Optional "fines" for missed KPIs go into a capacity-building fund.
  - Public SLB facts: Uruguay Oct 2022, 188 investors (21% new), $3.96bn of demand for a $1.5bn issue, a 170 bp spread over USTs, up to 30 bp narrowing.
  - Cites Yilmaz et al. 2022 ($3.4–8.1tn a year), UNCTAD June 2023, and Ameli et al. 2021 (*Nature Communications* 12:4046).
- **"v2 Trusted HDC Backed Intermediaries…docx"** (Estevão and N. Zimmermann):
  - National Sustainable Infrastructure Funds (SIFs), as FIFs, in three modes: (a) high-income-country (HDC) sovereign green bonds on-lent; (b) LMIC-guaranteed plus HDC back-up guarantee, rated about AA; (c) HDC-owned direct equity, with a for-profit global portfolio question.
  - Hypothetical "Xanadu" grid example with Germany and GIZ co-authorisation.
  - **Fixed coupon. A missed KPI triggers a 1–2% surcharge paid into a corrective trust fund that the partner agency spends on getting back on track**, rather than paying bondholders. A met KPI unlocks further concessional SIF finance.
- **`Background-SLIDISept2024Final.qmd`.** An earlier draft of the same paper. It adds that incentive lending "needs to be beyond the 'envelope'".
- **Also present but not read in full:** `WP1_SLIDI.docx` (~6,600 words), `Literature Review.docx`, `Background Info for Paper.docx`, KPI Bonds and SLIDI pptx decks, Aug 2024 outlines, and `Outline/Outline.txt`.

### 3.4 `34env.txt`

*Removed: summary of a World Bank internal document. Not for use in public text.*

### 3.5 `35mdb.txt` = `6.Additional/3.SovereignIncentives/3.5.ReformingMDBs/ReformingMDBs.qmd` (Stretton)
*~2,800 words.*

**Core argument.** The MDB comparative advantage is borrowing cheaply and on-lending, through **super seniority**. A chart (unsourced) shows the debt "bomb" at market rates vs IBRD rates. IEA puts needs at about $4tn a year (about $1tn China, $2tn other EMDEs).

**Five features:** super seniority; the **envelope system**; scale; retained vs distributed risk; debt-only vs equity.
- The envelope system limits conditionality, because the envelope is fixed and investment and policy lending substitute for each other.
- On retained vs distributed risk: options are MIGA-style transfer, syndication or securitisation, parallel institutions outside the envelope, and risk-absorbing equity funds.

**"Weak" vs "strong" Paris compliance:** a project aligned with Paris vs a country policy that would deliver 1.5°C if universal.

**Additionality-based incentives cause waiting**, including keeping assets open longer in order to be paid to close them.

**Universal incentive proposal:**
- Define policy strength, e.g. a carbon price of $100/t rising to $200/t.
- **A country delivering x% of 1.5°C-consistent action gets x% of the required investment financing.** Policy "price" rations finance.
- **Action threshold** (e.g. only carbon prices above $50/t), on norm-setting and demonstration grounds.
- **Double effectiveness**: the investment effect plus the reform effect.
- An additional envelope outside country allocations.
- **Dynamic incentives:** Dixit–Pindyck real options. "Generous but declining" terms, with grants giving first movers better terms. Oversubscribed countries get priority later.
- **Rationing tools:** a sectoral start (power), a country class, a region (southern Africa) as a demonstration.
- Debt from long-term SSBs, loss-absorbing equity, grants.

**[CONFLICT]** `combined.txt` describes 3.5 as covering "balance sheet optimisation, callable capital recognition, guarantee capacity, hybrid capital" against the mandate question. The actual text covers almost none of that; the CAF, callable-capital and mandate material sits in *Time and Chance* ch. 17 and `Background-MDBsMandate.qmd`.

**`3.5…/3.BackgroundPapers/Background-MDBsMandate.qmd`** (~1,000 words; no author; reads like a shareholder or French-style position note, so **[CHECK]** provenance).
- CPI Oct 2022: $850bn of flows in 2021 vs $4.3tn needed.
- Bridgetown asks.
- ODA concessionality rules are GDP-per-capita based, which is a mismatch for systemic emerging-market emitters.
- Proposes a "New Deal" concentrating concessional resources in strategic sectors for ambitious decarbonisation; climate as a top MDB priority with binding targets; shared indicators to prioritise countries (emissions path, risk exposure, cost of capital, investment per capita, fossil dependence).

### 3.6 `combined.txt`: combined overview
*~4,200 words.* The overview of all sections. Points to note:
- It lists 3.1 NCV and 3.2 SLL as active, and 3.3–3.5 as retained.
- It says SLIDIs are "superseded by the codified treatment in 3.2 and the collateral structure in 2.2".
- *Time and Chance* is described as the long-form source of Series 2 and 3; the "safe intermediary theory of concessionality" is its organising idea.
- 5.2's folder holds the "Trusted intermediary model" material (Trillions to Billions).

**[CONFLICT]** The 3.3, 3.4 and 3.5 descriptions do not match their texts (above). It also still points readers to 3.2, which is confidential.

---

## 4. Repo search: other relevant material (paths relative to `/home/user/writing`)

| Path | Relevance |
|---|---|
| `B Working Papers/6.Additional/6.Books/6.1.TimeAndChance/TimeAndChance.qmd` | **Key.** Guarantees (ch. 7), SECI record (ch. 9), criteria (ch. 10), risk stack and tail (ch. 14), sizing (ch. 15), concessionality (ch. 16), policy-lending fund (ch. 18), CIIF (ch. 19), CIT (ch. 20), **NCCV (ch. 21)**. |
| `…/6.1.TimeAndChance/3.BackgroundPapers/Background-ResponseToPeerReview.qmd`, `6.Books/Archive/Peer_Review_Time_and_Chance.qmd` | Peer-review critiques of the guarantee and incentive claims (not read in full). Check before reusing book claims. |
| `…/6.Books/Archive/Combined_Manuscript_Archive.qmd`; `6.1…/9.Archive/TimeAndChance-MarkdownEdition.*` | Older book manuscripts with the same NCCV chapter (numbered 11 in the archive). |
| `B Working Papers/6.Additional/6.Books/6.2.CarbonPricingRightPolicyWrongTime/CarbonPricingRightPolicyWrongTime.qmd` | Companion book. Grep hits on guarantees, SLL and CfDs. Claimed source of the "forest value exceeds offset price" and tipping-point marginal-hectare arguments. |
| `B Working Papers/7.Website/papers/GeoprosperityIntro.docx` | NCV for forests *and coal* ($1tn each); appendix A three-tier guarantee ("used but not used up"); appendix B 100% clean-energy programme; series plan (Papers 5–8). |
| `B Working Papers/3.SovereignIncentives/3.1.NotionalCapitalisedValueAndGuarantees/README.md` | 3.1 status: no draft. Former title "Guarantee-Based International Incentives for the Delivery of Strong NDCs". |
| `B Working Papers/3.SovereignIncentives/3.2.SustainabilityLinkedLending/SustainabilityLinkedLending.pdf` | **[INTERNAL]** PDF of 32sll. TODO H2: remove from the web server by hand. |
| `C Research Proposal/PreviousVersions/Oxford_DPhil_…-before-cleanup.docx` | Appendices B–D: "climate allowance … linked to MDB guarantee capacity"; analytical layers; claims turned into hypotheses. |
| `2 Strategic Plans/FY24/5. Klaus Project/WTP and Baseline Project.docx` | RBCF baselines. **Three baseline options: no-action, feebate, national-interest zero point** (Parry et al.). Willingness to pay vs willingness to accept. Effectiveness-weighted total carbon price as an effort metric. Ties to NCV decrement and KPI pricing. |
| `2 Strategic Plans/FY24/5. Klaus Project/Klaus Project proposal.docx` | Short; WTP/WTA definitions. |
| `2 Strategic Plans/FY24/5. Klaus Project/B6-RBCF and WTPCM/Summary-ClimateIncentivesTrust SStretton2023(JSCOMFeb24).docx`, `The Climate Incentives Trust.docx` | CIT summaries (same as 22cafe and the archive). Also an RBCF event agenda and a ToR for welfare-optimal mitigation. |
| `B Working Papers/6.Additional/3.SovereignIncentives/3.4.MDBClimateEnvelope/3.BackgroundPapers/Background-ScalingUpPolicyLendingAndPolicyIncentivesNoteForEFI.qmd` | **Stretton note for EFI.** Equity fund as buffer for beyond-envelope policy lending (like the RST); excess returns as dilutive shares for early movers; "CfD approach to agreed policy" as a commitment device; CIIF three-layer stack; green savings accounts; SWF investors (Norway, Singapore, UAE); super-majority rule. Cites the 70pp/10pp debt study via an FT link. |
| `…/3.4…/3.BackgroundPapers/Background-DraftListOfTransformationalClimatePolicyReformsBacked.qmd`, `Background-ClimateRelatedPriorActions…qmd`, `Background-ExamplesOfRecentDPOsWithClimateReformsJA.qmd`, program-document PDFs, xlsx/csv | The reform-archetype list and DPF prior-action evidence (the country examples the overview attributes to 3.4). Largely WB internal; **[INTERNAL]** check before use. |
| `…/3.4…/3.BackgroundPapers/Background-DirkCourse.qmd`, `Background-FiscalReformsBMZworkshop.qmd`, `Background-FiscalPolicyInstruments.qmd` | Heine course and workshop notes on policy-based climate finance. |
| `…/3.5.ReformingMDBs/3.BackgroundPapers/Background-MDBsMandate.qmd` | Mandate "New Deal" note (§3.5 above). |
| `…/3.5.ReformingMDBs/4.ExternalPapers/` | Strand 2023 (international mitigation finance), Lee 2023 (ideal climate MDB), Fankhauser 2023, Gregory 2023 (MDB/DFI innovations), FDL 2024 Bridging Program. |
| `…/3.3.SLIDIs/9.Archive/bonds with kpi.docx`; `AdditionalWork/v2 Trusted HDC Backed Intermediaries….docx`; `Older/Trusted Intermediaries … for discussion.docx`; `WP1_SLIDI.docx`; `KPI Bonds.pptx`; `SLIDIs-*.pptx` | KPI-bond origin; SIF bonds with a corrective surcharge; trusted-intermediary pricing. |
| `…/3.3.SLIDIs/9.Archive/Older/EFI Staff Discussion Note … - Copy.docx` | Another copy of the Heine note. **[INTERNAL]** |
| `…/3.3.SLIDIs/4.ExternalPapers/` | Kölbel and Lambillon 2022; Löfqvist et al. 2023 (forest restoration finance); Rojas-Marchini and Carmona 2024 (biodiversity offsets); MIGA ED engagement 2023 and Brookings MIGA/Roadmap 2023 (likely internal); "Funding low-carbon investments in the absence of a carbon tax". |
| `B Working Papers/2.FinanceAndRisk/2.2.ClimateInvestmentTrust/9.Archive/0. MobilisingPrivateFinance…docx` | **Trusted intermediary pricing rule; tier-2 = country CIT buffer account.** |
| `…/2.2…/9.Archive/Structured Finance for Global Clean Energy Abundance.docx` | "Virtual capital"; four investment classes; three fund accounts incl. fiscal-resilience collateral. |
| `…/2.2…/9.Archive/SubstitutingPPAs.docx`; `1B.OtherFiscalPolicy/1.5…/3.BackgroundPapers/Background-IndiaNote.qmd`, `Background-ShortIndiaNote.qmd` | Coal PPA substitution; India guarantees and securitisation. |
| `…/2.2…/1.Presentation/Briefing-CIT.qmd`, `Briefing-TechnicalSummaryCIT.qmd`; `…/3.BackgroundPapers/Background-ShortClimateCafe.qmd`, `Background-GlobalSolarEconomy.qmd` | Repo copies of 22bcit, 22tech, 22cafe and 22solar. |
| `…/2.1…/1.Presentation/Briefing-REPaymentIntermediaryFacility.qmd`; `8.PreviousVersions/REPIF-PolicyBrief-merged.qmd`, `SPIFA-Brief-previous.qmd`, `ClimateFinanceIntermediationForCleanPower-2026-09-17.qmd` | REPIF and SPIFA copies; the pre-merge 2.1. |
| `…/2.1…/4.ExternalPapers/Ratha-Innovative-financing-for-development.pdf` | Ratha on future-flow securitisation (the ABS precedent). |
| `B Working Papers/6.Additional/5.Analytics/5.2.ClimateFiscalFinancial/3.BackgroundPapers/TrillionsToBillions/` | "Policies → projects → AAA products"; **"investible policy guarantees … an operationalization of 'conditional NDCs'"**; superseniority; scaling dynamic. Notes and decks in `5.Notes/`. |
| `SPECIALISMS.md` §3.7, §4.3–4.8 | Positions: "reward sovereigns not projects"; NCV as a "climate balance a country can borrow against"; RST analogy unanalysed; the "10–20×" claim flagged unsourced. |
| `A Writing Instructions/PAPERS.md`, `STRATEGY.md`, `TODO.md`, `Writing-Status-Report.md` | 3.1 status (idea; core of DPhil proposal 1); confidentiality task H2. |
| `D Climate Econ Course/F. Global Mechanisms and Finance/F - Global Mechanisms and Finance.pptx` | A slide on KPI-linked fixed-return bonds (SLIDI summary). `WB_2023_WBClimateFrameworkGovernance.docx`. |
| `D Climate Econ Course/C. Net Zero Investment Roadmap/Derisking and Stimulating Investment/` | External de-risking readings: UNDP DREI 2013/2014/2017/2018/2019; Tilotia 2023 (currency de-risking); IHLEG 2022; Stanford 2017; IEA 2021; GDPC 2021 debt relief. |
| `3 Archive/` | Only planning, task and charge-code files. **No relevant content found.** |
| `B Working Papers/4.Modelling/` | CPAT architecture paper only. **No relevant guarantee or incentive material** beyond the total carbon price as a possible effort metric. |

**Search terms with no hits** anywhere in .qmd/.md/.txt: "early-action premium", "results-based buffer" and "climate allowance". The last appears only in the DPhil pre-cleanup docx. "Guarantee capacity" appears in combined.txt (3.5) and the DPhil docx. The *concept* of an early-action premium appears as "dynamic incentives", "generous but declining" and dilutive shares for early movers (35mdb; book ch. 18; CIT).

---

## 5. Conflicts and fact-check list against the 2.1/2.2 masters

1. **How SECI is backed.** The 2.1 master (l.30, l.152), SSB and book ch. 14 say "credit lines with the RBI and state indemnities". Book ch. 9 says Payment Security Fund 2016, RBI–centre–state tripartite withholding 2017, letters of credit 2019. WP2-A says around 2013 under National Solar Mission phase II, with a tripartite agreement. **Resolve.** The tripartite agreement makes the RBI a deducting agent; it is not evidently a credit line.
2. **Host-government liabilities.** 2.1 says the structure works "without consuming the host country's fiscal space"; GSE says it "does not increase developing country government liabilities"; book ch. 10 says the same. Book **ch. 14 retracts this**: there is a contingent liability, conditional on the government's own conduct. The masters should adopt the ch. 14 wording.
3. **SECI is not a clean success.** 2.1 calls SECI "worked well" and "demonstrated". Book ch. 9 documents persistent Discom arrears and two central bailouts: the risk was "moved, not eliminated".
4. **CIT parameters.** The master uses a 25% fee, 10% return and $20bn a year on $800bn. 22tech and 22cafe use a 10% fee, 15% return, $1.5bn a year and 3-year doubling. The archive original's $50tn/$10tn and $5tn are superseded by $5tn/$1tn and $500bn. The term "average project lifetime two years" means the construction period.
5. **Where the intermediary sits.** SPIFA says MIGA; REPIF and 2.1 say a regional facility with MIGA as last resort. WP2-A notes suggest housing both the SSB issuer and the intermediary in MIGA, or splitting them between MIGA and IFC. Book ch. 7 contrasts MIGA reinsurance with IBRD indemnity.
6. **Contract vs debt guarantee.** 2.1 favours the contract. StandardizedTwoStage, the briefing series' tier system and CIIF guarantee *debt* or loans. The README resolves this by domain; Series 2 should state the rule.
7. **Two-stage finance ownership.** SPIFA assigns it to MIGA or IFC. GSE's SEFS-SPV refinances only. India note uses IREDA then NaBFID. The book uses construction equity and short debt, then guaranteed paper. These are consistent in substance; only the named institutions differ.
8. **Combined overview descriptions** of 3.3 (SLIDI mechanics), 3.4 (author, content, country cases) and 3.5 (CAF and hybrid capital content) do not match the texts.
9. **SLIDI numbering and description.** "Intermediated Debt" vs "Development" Instruments; fixed coupon vs "coupon steps".
10. **Unsourced or unverifiable items:**
    - the 70pp/10pp debt study (an FT link only);
    - 10–20× credit-enhancement leverage;
    - 3% cost-of-capital saving per guaranteed dollar (NCCV);
    - GSE rate decomposition (−2/−2/−1);
    - SSB "same present value" claim;
    - Bais 2022 (22% of Indian capacity as non-performing assets);
    - the WP2-A reference list and its AI-style `【†source】` markers;
    - WBG climate finance "$21bn 2018–22";
    - the "Observatory" Kenya and Senegal decomposition;
    - "Paris decision para 108".

---

## 6. Confidentiality summary

- **Do not use outward:**
  - `32sll.txt` and its PDF, beyond the generic logic in §3.2;
  - the Heine EFI note (`34env.txt` / `MDBClimateEnvelope.qmd`, its SLIDI-archive copy, and the 3.4 background program documents and prior-action data), beyond the generic logic in §3.4;
  - MIGA ED engagement and Brookings decks in `3.3/4.ExternalPapers`, until checked.
- **Safe and own work:** SLIDIs, the KPI-bond and trusted-intermediary drafts (personal capacity; co-authors Estevão and N. Zimmermann need crediting), *Time and Chance*, GeoProsperity, CIT, GSE, Sollar, SSB and REPIF material.
- **Note:** `research.qmd` still carries a 3.2 abstract, without a link, describing World Bank SLL work. Decide whether the public abstract should describe it as generic sovereign SLL design rather than as the World Bank's internal portfolio.
