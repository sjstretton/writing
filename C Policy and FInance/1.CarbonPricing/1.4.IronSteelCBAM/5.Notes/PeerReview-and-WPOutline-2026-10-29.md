# Paper 1.3: peer review of the brief, and outline of the working paper

Review of *Climate Fiscal Policy Brief No. 1.3*, "Credit the Price Signal, Not the Payment" (`1.Presentation/Brief-IronSteelCBAM.qmd`, Oct 2026), written as a referee report. The outline is the plan for the academic working paper (master `IronSteelCBAM.qmd`, to become v0.3; the current v0.2, the June 2026 consultation submission, moves to `8.PreviousVersions/`).

## Part 1. Referee report

**Summary.** The brief identifies two flaws in CBAM's plant-by-plant design: it recognizes only explicit carbon prices "effectively paid", so feebates, rebated taxes, subsidy reform and non-price instruments earn nothing; and it rewards routing low-carbon (scrap-based) output to the EU. It proposes measuring the foreign price signal by country and sector, alongside the price paid, using a carbon-price-equivalent metric. The legal grounding is careful and current (Regulation 2023/956 as amended by 2025/2083). The working paper needs the formal analysis behind both flaws and the fix.

**Major comments**

1. **Model the shuffling.** Set up an exporter with two routes (blast furnace at $e_B$, scrap-based electric arc furnace at $e_S < e_B$), capacities $K_B$, $K_S$, and two markets: the EU with charge $\tau$ on embodied carbon, and the rest of the world with none. Show (i) under plant-level measurement the exporter allocates scrap-based output to the EU up to $\min(K_S, Q_{EU})$, lowering its CBAM bill by $\tau (e_B - e_S)\min(K_S, Q_{EU})$ with no change in its total emissions; (ii) if scrap supply is fixed globally, world emissions do not change either: the reported cut is pure reallocation; (iii) under country-sector average measurement the bill is independent of allocation. Calibrate the magnitude with public data and cite the evidence on resource shuffling (California electricity imports; Sandbag on steel).
2. **Define the "price signal" precisely.** The recognized price should be the marginal incentive on intensity that the exporting country's instruments create, measured as a carbon-price equivalent (paper 1.7): for a feebate at rate $t$ it is $t$; for a non-price standard it is the shadow price. Write the proposed CBAM liability as a formula. For example, certificates per tonne of product equal $\max(0,\ \tau - t^{\text{signal}}_{c,s}) \times \bar e_{c,s}$ under country-sector measurement, with $t^{\text{signal}}_{c,s}$ the TECP for country $c$, sector $s$. Show that it is invariant to shuffling and that, combined with paper 1.1's best-response result, it gives exporters the incentive to set $t = \tau$.
3. **The trade-off the brief omits.** Country-sector measurement removes the individual clean plant's reward for verifying its own low intensity, the very incentive plant-level measurement creates. A hybrid is possible: plant-level verified intensity for the embodied-carbon side, with an anti-shuffling rule (e.g. verified intensity counts only if the plant's whole output, not only EU-bound output, is covered), and country-sector measurement for the price side. Analyze the options and recommend one.
4. **Legal pathway.** Article 9(4) admits a default carbon price only "where a carbon price was set by the rules applicable in the third country" and nets rebates. Analyze whether recognition of feebates and implicit pricing fits within a broad reading of "compensation" or needs amendment at the December 2027 review. Add WTO analysis: country-level defaults differ by origin (MFN, GATT I and III; Article XX).
5. **Quantification across exporters.** Use the public default values (Implementing Regulation 2025/2621; the Commission's workbook in the repo) for steel and aluminum by country to show (a) CBAM liabilities per tonne at, for example, €80/t, (b) the value of recognizing a domestic feebate at the same rate, and (c) the shuffling gain for exporters with scrap capacity. Do not use the World Bank dashboard or Egypt workbook numbers (internal).

**Minor comments**

6. Explain the mark-up on default values (10/20/30 percent for steel, 2026–2028) and its incentive role.
7. Aluminum: the same shuffling logic with secondary (recycled) aluminum; brief treatment.
8. Revenue-financed decarbonization support should not reduce the recognized price; offsetting subsidies should. State the test.
9. Clear the VERIFY items: the May 2026 draft implementing regulation, COM(2025) 989 and IEA route intensities. EUR-Lex PDFs are in the download batch file.
10. Currency: euros throughout for CBAM; state it in tables.

**Recommendation:** major revision. The two flaws are real and the fix is sound; the paper needs the models, the liability formula, the verification trade-off, the legal pathway and calibration.

## Part 2. Outline of the working paper (about 8,000–10,000 words plus appendices)

**Front matter.** Title as the brief: "Credit the Price Signal, Not the Payment: Carbon Price Recognition and Scrap Shuffling under the EU's Carbon Border Adjustment Mechanism". Personal capacity. Abstract of about 150 words. JEL (F13, F18, H23, Q54, Q58). A note that legal texts are as of 29 October 2026.

1. **Introduction** (900 words). CBAM's two purposes; the two flaws; the fix; contributions: the shuffling model, the liability formula, the verification trade-off, the calibration; place in the series (1.1, 1.7).
2. **CBAM as legislated** (900 words). Table of legal texts and status: 2023/956, 2025/2083, 2025/2621, the May 2026 draft implementing regulation on carbon prices paid, COM(2025) 989. Article 9 and the default carbon price.
3. **Related literature** (900 words; Appendix A for the full review).
4. **A model of route shuffling** (1,500 words). Propositions 1–3 (major comment 1), with proofs in Appendix B. Figure 1.
5. **Recognizing the price signal** (1,500 words). Price paid versus price signal; Proposition 4 (a feebate earns nothing under price-paid recognition); the liability formula; Proposition 5 (invariance to shuffling; incentive to set $t = \tau$, linking to 1.1). Measurement by TECP (1.7), price and non-price instruments.
6. **Verification versus anti-shuffling: the design trade-off** (900 words). Options and a recommendation.
7. **Calibration across exporters** (1,200 words). Default values by country; liabilities; value of recognition; shuffling gains. Table 2, Figure 2.
8. **Legal pathway** (900 words). Article 9(4) and 9(5); December 2027 review; WTO.
9. **Limits** (500 words).
10. **Conclusion and recommendations** (400 words).

**Appendices.** A: literature review (from `5.Notes/LiteratureAppendix-draft.md`). B: proofs. C: legal texts and status. D: calibration data and code.
