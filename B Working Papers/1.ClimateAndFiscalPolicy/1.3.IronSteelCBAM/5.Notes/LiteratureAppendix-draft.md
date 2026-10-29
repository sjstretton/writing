# Literature appendix (draft): Carbon price recognition under CBAM

For: *Carbon Price Recognition under CBAM* (`IronSteelCBAM.qmd`, v0.2, 10 June 2026). The paper is a consultation submission on draft implementing regulation Ref. Ares(2026)4841230, with appendices on the exporter trilemma, production-route shuffling and benchmarks, and accreditation.

Compiled 29 October 2026. Bibliography: `LiteratureAppendix.bib` (same folder). The status tags are the same as in the 1.2 appendix:

- **[Full text]**: PDF obtained; abstract, introduction and conclusions read, plus targeted reading.
- **[Abstract]**: abstract only.
- **[Metadata only]**: record confirmed, content not read; numbers marked VERIFY.

Where I add my own inference, it is labeled **Note:**.

---

## 0. Current legal texts and status (as of 29 October 2026)

The status list comes from the EU Publications Office SPARQL index, queried 29 Oct 2026, for acts whose title cites Regulation (EU) 2023/956 or the CBAM. Texts were fetched from the Publications Office cellar (EUR-Lex HTML returned a bot challenge). The draft act's status comes from the Commission's "Have Your Say" API (initiative 14830). The index may lag the Official Journal by a few weeks.

| Act | Subject | Adopted | OJ reference | Status |
|---|---|---|---|---|
| Regulation (EU) 2023/956 | Establishes CBAM | 10 May 2023 | OJ L 130, 16.5.2023, p. 52 | In force. Definitive period from 1 Jan 2026. Art. 9 replaced by 2025/2083 |
| Implementing Reg. (EU) 2023/1773 | Transitional-period reporting | 17 Aug 2023 | OJ L 228, 15.9.2023, p. 94 | Transitional period ended 31 Dec 2025. Swedish version corrected by 2024/2649 |
| Implementing Reg. (EU) 2024/3210 | CBAM registry | 18 Dec 2024 | OJ L, 2024/3210, 30.12.2024 | In force. Amended and corrected by 2025/2550 (10 Dec 2025) |
| Implementing Reg. (EU) 2025/486 | Authorized CBAM declarants | 17 Mar 2025 | OJ L, 2025/486, 18.3.2025 | In force. Amended and corrected by 2025/2549 (10 Dec 2025) |
| **Regulation (EU) 2025/2083** ("Omnibus" simplification) | 50-tonne single mass threshold; new Art. 9 (default carbon prices); certificate sales from 1 Feb 2027 | 8 Oct 2025 | OJ L, 2025/2083, 17.10.2025 | In force |
| Implementing Reg. (EU) 2025/2210 | Goods brought to the continental shelf or EEZ | 31 Oct 2025 | OJ L, 2025/2210, 3.11.2025 | In force |
| Delegated Reg. (EU) 2025/2551 | Accreditation of verifiers | 20 Nov 2025 | OJ L, 2025/2551, 22.12.2025 | In force (EP non-objection 16 Dec 2025) |
| Implementing Reg. (EU) 2025/2546 | Verification principles for embedded emissions | 10 Dec 2025 | OJ L, 2025/2546, 22.12.2025 | In force |
| **Implementing Reg. (EU) 2025/2547** | Methods for calculating embedded emissions | 10 Dec 2025 | OJ L, 2025/2547, 22.12.2025 | In force |
| Implementing Reg. (EU) 2025/2548 | Calculation and publication of CBAM certificate price | 10 Dec 2025 | OJ L, 2025/2548, 22.12.2025 | In force |
| Implementing Reg. (EU) 2025/2619 | Information from customs authorities | 16 Dec 2025 | OJ L, 2025/2619, 22.12.2025 | In force |
| **Implementing Reg. (EU) 2025/2620** | Free-allocation adjustment (CBAM benchmarks by production route) | 16 Dec 2025 | OJ L, 2025/2620, 22.12.2025 | In force |
| **Implementing Reg. (EU) 2025/2621** | Default values (country-specific, with mark-ups) | 16 Dec 2025 | OJ L, 2025/2621, 31.12.2025 | Applies from 1 Jan 2026. Must be revised by Dec 2027 at the latest (Art. 2), with a revision "already" in 2026 sought (recital 11) |
| COM(2025) 783 | Commission report on the application of CBAM (Art. 30 review) | 16 Dec 2025 | not OJ | Published |
| **COM(2025) 989**, 2025/0419(COD) | Proposal: extension to downstream goods, anti-circumvention, pre-consumer scrap as precursor | 17 Dec 2025 | not OJ | Pending in co-decision. EESC opinion 19 Mar 2026. No adopted act in the index at 29 Oct 2026 |
| **Draft Implementing Reg., Ares(2026)4841230** | Carbon price paid in a third country: conversion, evidence, independent persons | draft published 13 May 2026 | not OJ | Feedback 13 May–10 Jun 2026 (177 responses). Stage "adoption workflow". **Not adopted** at 29 Oct 2026 |
| Draft acts (Have Your Say, published 19 Feb 2026) | CBAM declarations (Ares(2026)1634728); free-allocation adjustment rules (Ares(2026)1634857) | — | — | Initiatives listed. Status not checked further |
| Council Decision (EU) 2026/2240 | EEA Joint Committee position: CBAM into EEA Agreement Annex XX | 24 Sep 2026 | OJ L, 2026/2240 | Adopted |

**Provisions that bear directly on the paper:**

- **Reg. 2023/956, Art. 3(29)** (unchanged): "carbon price" means the monetary amount paid "in the form of a tax, levy or fee or in the form of emission allowances under a greenhouse gas emissions trading system". Implicit pricing through excises or subsidy removal is outside the definition. This confirms the paper's §1.2.
- **Art. 9 as replaced by 2025/2083:**
  - Art. 9(1): a deduction based on carbon price actually paid is available only where embedded emissions use *actual* values. Any "rebate or other form of compensation" must be netted.
  - Art. 9(4): the new default route. A deduction by reference to yearly default carbon prices "may be claimed only where a carbon price was set by the rules applicable in the third country". Where emissions use *default* values, *only* the default carbon price can be used. "As from 2027, the Commission **may**, for third countries where carbon pricing rules are in place, determine and make available ... the default carbon prices ... and publish the methodology for their calculation", based on "the best available data from reliable, publicly available information and information provided by those third countries".
  - **Note:** this confirms the paper's central claim. The default is discretionary ("may"). It is limited to countries "where carbon pricing rules are in place". It is therefore zero by construction for a country with only excises or subsidy reform. The *methodology* is to be published alongside the default prices, but no consultation is required. One nuance the paper should add: the law ties methodology publication to the defaults themselves, so "no published methodology" is a statement about timing (2027 onward), not a legal gap.
- **Draft implementing regulation Ares(2026)4841230, as read:**
  - Recital 8: only mechanisms that are "binding in nature and impose compliance obligations on all operators active in the relevant sectors ... without discrimination". This matches the paper.
  - Art. 6: the formula ReductionActual = (€EFF_CP / RefPrice) × Q. The default-price route is (€DCP × SEE / RefPrice) × Q. This matches the paper's "Article 6" description.
  - **Art. 8(1)(b)(ii): emissions "below an emission intensity baseline under a baseline-and-credit emissions trading system" count as compensation.** **Note:** this is the provision that zeroes recognition for a feebate or OBPS-type instrument. Recognized price is roughly $t(e_i - \bar e)$ for above-benchmark installations, and nil below. It is the strongest textual support for the paper's §1.3 (CPEP versus RCP). The paper should quote it.
  - Art. 8(1)(c): indirect-cost compensation is netted.
  - **Art. 8(2):** revenue-funded subsidies are *not* netted if four conditions hold: (a) all installations eligible "irrespective of the price paid"; (b) application required; (c) public decision; (d) objective is emission reduction at the beneficiary installation. This matches the paper's §2.4 exactly.
  - Recital 7: a 5% tolerance between the emissions boundaries of the mechanism and of CBAM.
  - Recitals 12–13: domestic credits are accepted without extra criteria. International credits are accepted only as Paris Art. 6.2 or 6.4 units, capped at **10%** of covered emissions. The paper does not mention this; it is relevant for countries pairing a carbon tax with offsets.
  - Art. 9: independent persons must be accredited under EN ISO/IEC 17029:2019 by a national accreditation body. They must be independent of the operator, EU and Member State authorities, and the third-country authority. This supports the paper's Appendix C. I did not check Art. 11 of the draft, which the paper cites for documentation requirements. VERIFY its article numbering.
- **Implementing Reg. 2025/2621 (default values):**
  - Defaults are **country-specific averages**, plus mark-ups for iron and steel, aluminium and cement of **10% (2026), 20% (2027) and 30% (2028 onward)**, and 1% for fertilisers.
  - Each CN line carries an "underlying production route determining the CBAM benchmark" code (e.g., (C) BF/BOF, (E) scrap/EAF), used for the free-allocation adjustment under 2025/2620.
  - Hot-rolled flat steel (CN 7208), direct-emissions default before mark-up: **India 4.280, Türkiye 2.428, China 3.187 tCO₂/t**, all with route code (C).
  - Where no reliable data exist, defaults are the average of the **ten highest-intensity exporters** (recital 2). Where the country of a precursor is unknown, the highest country default applies.
  - **Note:** the paper's Appendix B says 2025/2621 "assigns countries to production route categories". More precisely, it assigns a route code per CN line per country for the *benchmark*, while the default *value* is a country average across routes. For a mixed-route exporter, the country-average default is itself a shuffling opportunity. A high-intensity BF/BOF plant in a country with much scrap-EAF (e.g., Türkiye) can declare the low country default rather than its actual value.
- **COM(2025) 989** proposes to add to the Art. 27(2) circumvention list "(c) artificially adjusting the supply chains to make the goods benefit from lower default values". It would add pre-consumer (not post-consumer) scrap as a CBAM precursor, and widen the Art. 30 review to cover default-value methods and mark-ups. Resource shuffling already appears in the Art. 30 review list of 2023/956. Neither the regulation nor the proposal addresses *installation-level routing* under actual values. **Note:** that is the paper's Appendix B point, and it remains open.

---

## 1. CBAM and border carbon adjustment design

**KeenParryRoaf2022**: Keen, M., Parry, I. & Roaf, J. (2022). Border carbon adjustments: rationale, design and impact. *Fiscal Studies* 43(3): 209–234. [Abstract this session; working paper read in full in the 1.1 session]
BCAs are potentially the most effective domestic instrument against competitiveness loss and leakage, but design is critical. Limit coverage to EITE sectors. Initially benchmark on *domestic* emission intensities to ease the transition for emission-intensive partners. Decide how to treat partners with different mitigation approaches, and how to treat exports. BCAs alone do not solve free-riding, but may ease it and be a step toward an international carbon price floor.
*Use in 1.3:* Supports the paper's call to recognize non-explicit approaches. The IMF working paper's "feebate equivalence" (cited in 1.1) is the bridge to 1.2.

**Cosbey2019**: Cosbey, A., Droege, S., Fischer, C. & Munnings, C. (2019). Developing guidance for implementing border carbon adjustments: lessons, cautions, and research needs from the literature. *REEP* 13(1): 3–22. [Abstract]
A review of the regulatory choices: scope, carbon-content methodology, adjustment price, modification scenarios, use of revenue, and compliance with trade and climate law.
*Use in 1.3:* The standard citation that BCA design must account for foreign policy effort. It frames "modification scenarios" (the recognition question) as a recognized design choice.

**Mehling2019**: Mehling, M. A., van Asselt, H., Das, K., Droege, S. & Verkuijl, C. (2019). Designing border carbon adjustments for enhanced climate action. *AJIL* 113(3): 433–481. [Full text obtained; abstract, introduction and design sections skimmed]
A comprehensive legal-economic analysis proposing a design that balances legal, administrative and environmental considerations. It reviews the 2008 Commission proposal that would have exempted partners taking "comparable action".
*Use in 1.3:* The legal pedigree of "equivalence" or "comparable action" tests. It shows the current per-tonne price-paid test is one choice among several.

**MehlingRitz2023**: Mehling, M. A. & Ritz, R. A. (2023). From theory to practice: determining emissions in traded goods under a border carbon adjustment. *Oxford Review of Economic Policy* 39(1): 123–133. [Full text]
A BCA based only on *default* intensities distorts abatement incentives. An "individual adjustment mechanism" (IAM) using actual intensities restores them and improves WTO prospects, but adds complexity and creates **resource shuffling** risk. With defaults only, there is no shuffling incentive. California prohibited reshuffling of electricity imports, but the ban "has been difficult to enforce". The authors judge reshuffling to be "perhaps most acute for electricity markets" and **likely less pronounced for industrial goods**, whose flows are easier to track. They suggest a company-level rather than installation-level point of regulation, noting complications for groups and state-owned enterprises.
*Use in 1.3:* This is the key citation for Appendix B, and a partial **qualification**: the authors expect industrial shuffling to be smaller than electricity shuffling. Their company-level remedy is an alternative to the paper's country-sector RCP.

**KortumWeisbach2017**: Kortum, S. & Weisbach, D. (2017). The design of border adjustments for carbon prices. *National Tax Journal* 70(2): 421–446. [Abstract]
Covers which goods, which emissions and which countries a BA should apply to. BAs "will impose high administrative costs and need stronger welfare justifications".
*Use in 1.3:* Background for the trilemma in Appendix A, which is about export-side treatment.

**ClausingWolfram2023**: Clausing, K. A. & Wolfram, C. (2023). Carbon border adjustments, climate clubs, and subsidy races when climate policies vary. *Journal of Economic Perspectives* 37(3): 137–162. [Full text, NBER w31310]
The paper separates two spillovers: free-riding by low-ambition countries, and competitive disadvantage of *price-based* jurisdictions against *subsidy-based* ones. When approaches differ, "one policy alone will not be able to address both". About 25% of GHG emissions are embodied in trade. Lower-income countries produce more carbon-intensive goods than they consume. Divergent approaches risk subsidy races.
*Use in 1.3:* Direct support for §1.4 (a carbon tax offset by subsidies is indistinguishable from a real one). It is also the counterpart problem: the EU recognizes only price-based effort, while major partners (US IRA-style subsidies) use non-price instruments.

**BrangerQuirion2014**: Branger, F. & Quirion, P. (2014). Would border carbon adjustments prevent carbon leakage and heavy industry competitiveness losses? *Ecological Economics* 99: 29–39. [Full text, HAL]
A meta-analysis of 25 studies (310 estimates). Leakage ratios are typically **5–25% (mean 14%)** without BCAs and **−5% to 15% (mean 6%)** with them. BCAs cut leakage by about 6 percentage points, all else equal. Coverage of all sectors and export rebates are the most effective features.
*Use in 1.3:* Benchmark for how much is at stake. The finding that export rebates matter supports Appendix A: CBAM has no export adjustment.

**Boehringer2022NCC**: Böhringer, C., Fischer, C., Rosendahl, K. E. & Rutherford, T. F. (2022). Potential impacts and challenges of border carbon adjustments. *Nature Climate Change* 12: 22–29. [Metadata only]
A multi-region CGE assessment of BCA impacts. Publisher blocked; VERIFY findings. An author correction exists (doi 10.1038/s41558-022-01300-0).
*Use in 1.3:* Standard modeling citation for incidence on partners.

**FischerFox2012**: Fischer, C. & Fox, A. K. (2012). Comparing policies to combat emissions leakage: border carbon adjustments versus rebates. *JEEM* 64(2): 199–216. [Metadata only; already in the 1.1 bib]
*Use in 1.3:* Links CBAM to output-based rebating. Cite it where the paper argues a rebated tax is the "politically survivable" design.

## 2. Incidence and exposure of developing countries

**Beaufils2023**: Beaufils, T., Ward, H., Jakob, M. & Wenz, L. (2023). Assessing different European Carbon Border Adjustment Mechanism implementations and their impact on trade partners. *Communications Earth & Environment* 4: 131. [Full text]
Uses throughflow accounting on EORA MRIO data to compare implementation options, and quantifies how a CBAM channels the EU carbon price to partners. Middle- and low-income countries for which the EU is an important market are hit disproportionately, even under conservative options. The paper explores international revenue-recycling rules (by population, GDP and regional damages) to make the CBAM inclusive.
*Use in 1.3:* Evidence for the paper's premise that the countries CBAM is meant to influence are poorer and more exposed. Revenue recycling is a complement to the recognition fix.

**Magacho2024**: Magacho, G., Espagne, E. & Godin, A. (2024). Impacts of the CBAM on EU trade partners: consequences for developing countries. *Climate Policy* 24(2): 243–259. [Abstract]
In absolute terms Russia, China, Türkiye and Ukraine are most exposed. In relative terms, many developing economies have more than 2% of exports and 1% of production affected. The Western Balkans, Mozambique, Zimbabwe and Cameroon are most exposed externally; Morocco and Tajikistan are added on socio-economic criteria.
*Use in 1.3:* Names the countries for which the default carbon price is the only route.

**Eicke2021**: Eicke, L., Weko, S., Apergi, M. & Marian, A. (2021). Pulling up the carbon ladder? Decarbonization, dependence, and third-country risks from the European carbon border adjustment mechanism. *Energy Research & Social Science* 80: 102240. [Abstract]
A risk index combining export structure, emissions intensity, targets and **institutional MRV capacity**. Most high-risk countries are in Africa. Case studies cover Mozambique, Bosnia and Herzegovina, and Morocco, with emphasis on MRV.
*Use in 1.3:* The best published source for Appendix C. MRV and verification capacity is itself a risk dimension.

**PerdanaVielle2022**: Perdana, S. & Vielle, M. (2022). Making the EU Carbon Border Adjustment Mechanism acceptable and climate friendly for least developed countries. *Energy Policy* 170: 113245. [Abstract]
CGE analysis. CBAM cuts leakage by about one-third by 2040, but LDCs suffer welfare losses from lower exports. *Exempting* LDCs increases leakage more than the alternatives. CBAM revenue redistributed to clean energy in LDCs improves their welfare, cuts leakage and is cost-efficient for the EU.
*Use in 1.3:* Support for capacity-building finance (Appendix C). It is also a counterpoint to blanket exemptions, which the paper does not propose.

**ZhongPei2022**: Zhong, J. & Pei, J. (2022). Beggar thy neighbor? On the competitiveness and welfare impacts of the EU's proposed carbon border adjustment mechanism. *Energy Policy* 162: 112802. [Metadata only]
VERIFY findings.

**Gaps (not obtained):**
- *World Bank Relative CBAM Exposure Index* (2023 data tool). The World Bank Documents API found no matching paper; the record and authors need verifying.
- *UNCTAD (2021)*, A European Union CBAM: implications for developing countries. unctad.org returned 403.
- *CGD: Lowe (2021)*. The cgdev.org URL returned 404.
- ODI and Brookings CBAM notes, and "Sato et al." on CBAM exposure: not located this session. Ask Stephen which Sato paper is meant.

A World Bank policy note on North Macedonia (Sep 2024) and an Argentina CCDR background note on CBAM exposure (Nov 2022) are listed in World Bank Documents and could serve as country examples (not read).

## 3. Resource shuffling and benchmark design

**Fowlie2009**: Fowlie, M. (2009). Incomplete environmental regulation, imperfect competition, and emissions leakage. *AEJ: Economic Policy* 1(2): 72–112. [Full text, NBER w14421]
When regulated producers are cleaner than unregulated ones, incomplete regulation can raise emissions above the no-regulation level. The paper simulates California electricity under source-based cap-and-trade. Exempting out-of-state producers achieves **about one-third of the reductions** of complete regulation at **more than twice the cost per tonne**.
*Use in 1.3:* The foundational quantitative estimate for incomplete coverage in electricity.

**CaronRauschWinchester2015**: Caron, J., Rausch, S. & Winchester, N. (2015). Leakage from sub-national climate policy: the case of California's cap-and-trade program. *The Energy Journal* 36(2): 167–190. [Abstract]
A calibrated CGE model. Without restrictions on imported electricity, California's program raises out-of-state emissions by **45% of the domestic reduction**. With imports in the cap and resource shuffling *banned* as legislated, overall leakage is **9%**.
*Use in 1.3:* The cleanest number for what shuffling rules are worth. **Note:** the 9% assumes the ban is effective. Mehling and Ritz (2023) report it has been hard to enforce, so the true figure lies between 9% and 45%.

**BushnellChenZaragozaWatkins2014**: Bushnell, J., Chen, Y. & Zaragoza-Watkins, M. (2014). Downstream regulation of CO₂ emissions in California's electricity sector. *Energy Policy* 64: 313–323. [Metadata only]
Analyzes reshuffling of contracts for imported electricity under AB32's first-deliverer point of regulation. The publisher and EI@Haas working-paper (WP-236) copies returned 403. **VERIFY** the reshuffling magnitudes before citing any number. From prior knowledge only: the paper argues that contract reshuffling could largely offset the apparent emission reductions from imports.
*Use in 1.3:* The classic electricity-shuffling reference, alongside Caron et al.

**FowlieReguant2022**: see 1.2 appendix. Leakage-risk measures and calibrated output subsidies.
*Use in 1.3:* Benchmarks for the free-allocation adjustment should reflect leakage risk, not only intensity.

**Gap: steel-specific shuffling evidence.** No empirical paper on scrap-EAF and BF-BOF routing to the EU was found through Crossref. The only hit was a 2026 SSRN paper on CBAM electricity accounting and private grids (Apaydın, doi 10.2139/ssrn.7601183; unread, SSRN blocked). This is a gap in the literature, not only in this search. The paper's Appendix B is therefore a contribution, but it needs either a stylized calculation or trade data. One candidate: Türkiye's EAF share in EU-bound exports against its BF-BOF share, using the 2025/2621 country defaults quoted above.

## 4. Recognition of foreign carbon pricing, implicit prices and equivalence

**Agnolucci2023**: Agnolucci, P., Fischer, C., Heine, D., Montes de Oca Leon, M., Pryor, J., Patroni, K. & Hallegatte, S. (2023). *Measuring Total Carbon Pricing.* World Bank PRWP 10486. Published in *World Bank Research Observer* 39(2): 227–258 (2024). [Full text, PRWP version]
Develops a Total Carbon Price (TCP) combining direct pricing (taxes, ETS) with indirect pricing: fuel excises net of subsidies, measured against supply-cost benchmarks. Computed for 142 countries, 1991–2021. Direct pricing covers about a quarter of global emissions, but the global TCP "is not that much higher than it was in 1994". Indirect pricing still makes up "the lion's share" and has stagnated. Many developing countries, especially net fuel importers, "contribute substantially to global carbon pricing" once indirect pricing counts. Average carbon-tax rates have stayed between US$30 and 45 per tCO₂.
*Use in 1.3:* This is the ready-made methodology for the paper's §2.1–2.2. The paper's "World Bank, IMF and OECD frameworks" should cite this specifically, along with the IMF fuel-price benchmarks (Black et al. 2023). The OECD Effective Carbon Rates series could not be accessed (OECD iLibrary blocked).

**Black2023**: see 1.2 appendix. IMF efficient-price benchmarks: $7 trillion in subsidies in 2022, and 80% of coal priced below half its efficient level.
*Use in 1.3:* The benchmark source for "implicit prices are signed quantities" (§1.2). Negative implicit prices are the norm for coal.

**Hagem2020 / Art. 8(2) link**: Hagem, Hoel and Sterner (2020) (1.2 appendix) analyze *expenditure-based refunding*, which refunds in proportion to abatement spending. **Note:** that is the economic content of the draft's Art. 8(2) carve-out. Their result: EBR needs a *lower* fee than a tax to reach the same abatement, and overweights technology relative to output. Citing it would ground the paper's §2.4 claim that the carve-out "strengthens rather than dilutes the signal".

**Gap: fuel-subsidy reform evidence** (Indonesia, India). The paper asserts that Indonesia's and India's reforms moved implicit prices "by amounts comparable to explicit carbon taxes". No source was obtained this session. Agnolucci et al. (2023) country series and the IMF subsidy database are the places to verify it. [VERIFY before submission.]

---

## Synthesis (about 650 words)

**Where the paper sits.** The CBAM literature has three strands. The design literature (Cosbey et al. 2019; Mehling et al. 2019; Keen, Parry and Roaf 2022; Kortum and Weisbach 2017) treats recognition of foreign effort as a design choice and generally recommends crediting it. The incidence literature (Eicke et al. 2021; Perdana and Vielle 2022; Beaufils et al. 2023; Magacho, Espagne and Godin 2024) shows that exposure, relative to the size of the economy, falls on middle- and low-income exporters with weak MRV capacity. The measurement literature (Agnolucci et al. 2023; Black et al. 2023) shows that indirect carbon pricing, through excises net of subsidies, is most of the world's carbon price and is especially important in developing net fuel importers. The paper joins these strands at one point that none addresses: the *default carbon price* in amended Article 9(4) and the draft implementing regulation.

**What is new.** Four contributions stand up against the literature and the legal texts.

1. *The default is the operative instrument.* The law confirms the default is discretionary ("may"), starts in 2027, and is limited to countries "where carbon pricing rules are in place". For a country with only implicit pricing, it is zero by construction.
2. *Implicit prices are invisible.* The Art. 3(29) definition confirms this. A methodology already exists to fix it (Agnolucci et al. 2023).
3. *CPEP versus RCP.* The draft's Art. 8(1)(b)(ii) explicitly nets emissions "below an emission intensity baseline". A feebate or output-based pricing system is therefore recognized only on above-benchmark emissions, though its marginal signal is the full rate. No paper found states this. It is the paper's sharpest point and links directly to 1.2.
4. *Real versus nominal prices.* Clausing and Wolfram (2023) give the general theory that one border instrument cannot handle both price-based and subsidy-based approaches. The paper's SOE and offsetting-subsidy cases are concrete instances.

**What needs qualifying.**

- The paper says the default methodology "has not been published". The law ties its publication to the defaults themselves, from 2027. The real gap is that there is no consultation and no criteria.
- The draft's Art. 8(2) carve-out is a form of expenditure-based refunding. Hagem, Hoel and Sterner (2020) show it can be designed to sharpen incentives, which supports §2.4.
- The draft's 10% cap on Article 6 credits and its 5% boundary tolerance are omitted from the paper and should be mentioned.

**Shuffling magnitudes.** The only quantitative evidence is from electricity:

- Without import rules, California's program leaks 45% of domestic reductions. With imports capped and shuffling banned on paper, leakage is 9% (Caron, Rausch and Winchester 2015).
- Exempting imports achieves only a third of the reductions (Fowlie 2009).
- The ban has been hard to enforce (Mehling and Ritz 2023).

Mehling and Ritz expect industrial shuffling to be *smaller* than electricity shuffling, because material flows are easier to trace. That cuts against the emphasis of the paper's Appendix B, and the paper should engage with it. Two features of the actual texts cut the other way:

- Default values in 2025/2621 are *country averages* across routes. In a mixed-route country, a high-intensity BF/BOF exporter can declare the low country default instead of its actual value. Türkiye's hot-rolled default (2.43 tCO₂/t before mark-up) sits far below India's (4.28). This is adverse selection into defaults, a cousin of shuffling. The rising mark-ups (10%, 20%, 30%) only partly offset it.
- The Commission's own anti-circumvention proposal, COM(2025) 989, targets "artificially adjusting the supply chains to ... benefit from lower default values" and adds pre-consumer scrap as a precursor. It does not touch installation-level routing under *actual* values, which is the paper's case.

The paper's recommendation to develop the embedded-emissions defaults and the recognition defaults together is therefore well aimed, and the December 2027 revision of 2025/2621 is the right venue. The evidence base for steel specifically is thin. A stylized calculation from the published defaults, and from EU import data by route, would turn Appendix B from assertion into evidence.

**Status of the evidence on the paper's numbers.** The paper's worked example (a 20% gross cost becomes about a 2% net cost) and its claims about Indonesia and India are unsourced. They should be either sourced (Agnolucci et al. 2023 country series; IMF subsidy data) or labeled stylized.
