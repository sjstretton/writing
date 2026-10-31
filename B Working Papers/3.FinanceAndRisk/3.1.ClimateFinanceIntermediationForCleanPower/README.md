# 3.1 Guarantee the Contract, Not the Debt: A Payment Intermediary for Clean Power

Series 3 (Finance and Risk) flagship. Climate Fiscal Policy Brief No. 3.1 and its working paper.

**Question.** How can a developing country remove the payment risk that sets the cost of capital for clean power, at the lowest contingent cost to the state?
**Answer.** A payment intermediary facility buying under one standard power purchase agreement, backed by a guarantee waterfall contracted in advance; guarantee the contract, not the debt, and pair it with utility reform.

## Status (29 Oct 2026)

| File | Version | Status |
|---|---|---|
| `ClimateFinanceIntermediationForCleanPower.qmd` (master), `.bib`, `.docx` | 0.2 | Full draft, about 7,800 words of body; awaiting Stephen's review |
| `1.Presentation/Brief-ClimateFinanceIntermediationForCleanPower.qmd`, `.bib`, `.docx` | 1.0 | Full draft, about 3,000 words |
| `2.Source/model.py` | – | Model and calibration; prints every number quoted |
| `2.Source/make_wp_figures.py`, `2.Source/figures/` | – | Working-paper figures 1–4 |
| `2.Source/render.py` | – | Renders the master to docx with pandoc, resolving Quarto cross-references |
| `1.Presentation/figures/make_figures.py` | – | Brief figure 1 |

Render the brief from `1.Presentation/` with pandoc and `--citeproc`; render the working paper with `python3 2.Source/render.py <chicago.csl>`.

## Versions

- v0.2 (Oct 2026): rewrite to the paper standard and the series 3 architecture. New model (offtaker default episodes, contract vs debt guarantee, waterfall and liquidity buffer), calibration, SECI and NBET facts verified from public sources. Synthetic sovereign bonds and two-stage finance moved to Paper 3.2.
- v0.1 (Sept 2026): consolidation of REPIF, SPIFA and the synthetic sovereign bonds note. In `8.PreviousVersions/ClimateFinanceIntermediationForCleanPower-v0.1.*`. The `-2026-09-17` files there are the pre-merge draft.

## Lineage and co-authors

- REPIF policy brief (regional renewable energy payment intermediary facilities), written with **Nils Zimmermann**, Nov 2024: `1.Presentation/Briefing-REPaymentIntermediaryFacility.*`, `8.PreviousVersions/REPIF-PolicyBrief-merged.*`. Source of the guarantee waterfall.
- SPIFA (solar payments intermediary and finance agency), developed by **Evie Davey**: `1.Presentation/Briefing-SPIFA.pdf`, `8.PreviousVersions/SPIFA-Brief-previous.*`. Source of the treatment of small and debt-distressed states.
- *Time and Chance* (book manuscript, `8.AdditionalPolicyPapers/8.5.Books/8.5.1.TimeAndChance`), chs 7–9, 14, 16, 22: the layered stack, "guarantee the offtaker, not the loan", the SECI record, the retraction of the "adds nothing to liabilities" claim.

## Facts corrected from earlier drafts

- SECI is not backed by "credit lines with the Reserve Bank of India". The RBI is the debiting agent under the tripartite agreement (SECI a beneficiary since Oct 2016); plus letters of credit (MoP order 28 June 2019) and a payment security fund (ICRA, July 2025).
- The structure is not free to the host: the exposure becomes smaller, contingent and contracted.
- Energy as a service is still a fiscal commitment; the "energy bill, not a debt" and preferred-creditor claims are dropped.
- The "6c falling to 3c has the same present value as a flat 5c" example is wrong at 8%; the PV-equal path is 7.74c falling to 3.87c.
- Dropped as unsourced: 3% cost-of-capital saving per guaranteed dollar, 10–20x leverage, "Paris decision paragraph 108".
