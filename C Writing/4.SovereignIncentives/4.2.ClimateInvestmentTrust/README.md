# 4.2 The Climate Investment Trust: Hold Capital, Lend Its Strength

Series 4 (Sovereign Incentives) flagship, paired with 4.1 (notional capitalized value and guarantee capacity). Moved here from the finance series (then numbered 2.2) on 29 Oct 2026.

## Status (29 Oct 2026)

- Working paper `ClimateInvestmentTrust.qmd` (master), version 0.2, rendered to `ClimateInvestmentTrust.docx`. First full draft in PRWP form (about 7,600 words of body): three propositions with proofs, calibrated model, verified comparators. Awaiting Stephen's review.
- Brief `1.Presentation/Brief-ClimateInvestmentTrust.qmd`, Climate Fiscal Policy Brief No. 4.2, rendered to `.docx` (about 3,000 words including table and captions).
- Vasicek (2002) page range confirmed 30 Oct 2026 (Risk 15(12): 160–162); no unverified markers remain.

## Files

| File | What |
|---|---|
| `ClimateInvestmentTrust.qmd`, `.bib`, `.docx` | Working paper master, v0.2 |
| `1.Presentation/Brief-ClimateInvestmentTrust.*` | Brief No. 4.2 |
| `1.Presentation/figures/make_figures.py` | Brief figure (uses `2.Source/model.py`) |
| `2.Source/model.py` | Buffer sizing, growth dynamics, allocation rule; prints every number used |
| `2.Source/make_wp_figures.py`, `2.Source/figures/` | Working-paper figures |
| `1.Presentation/Briefing-CIT.*`, `Briefing-TechnicalSummaryCIT.*`, `Pres-Introduction.pptx` | Older briefings (2024), source material only |
| `3.RelatedPiecesAndLinks/` | Global Solar Economy and Climate Café notes (source material) |
| `8.PreviousVersions/ClimateInvestmentTrust-v0.1.*` | Previous master (Sept 2026, written as a series 2 mechanism paper) |
| `8.PreviousVersions/EquityDeRiskingForCleanEnergy.*` | Standalone equity de-risking paper, folded into v0.1 |
| `9.Archive/` | The Climate Incentives Trust (May 2024) and related notes |

Render (from the folder holding the qmd):
`pandoc X.qmd -f markdown --citeproc --bibliography=X.bib --csl=chicago.csl --resource-path=. -o X.docx`

## Lineage

- First proposed as the **Climate Incentives Trust** (May 2024; `9.Archive/The Climate Incentives Trust.docx` and tracked version), with a technical summary and Climate Café note (2024).
- *Time and Chance* (book manuscript): ch. 14 ("One Structure, Several Views": one pool under five names), ch. 18 (policy-lending fund, dynamic incentives), ch. 19 (Climate Investment and Insurance Fund), ch. 20 (Climate Incentives Trust).
- *The Right Policy at the Wrong Time*, ch. 5: the international feebate needs a trust to hold the pot.
- Equity de-risking / regional fund design: joint two-stage climate project finance work with **Jasper Zimmermann** (credited in both papers).

## Settled in v0.2

One name (Climate Investment Trust); one fee rule and return (25% of private investment returns, 10% gross return); first-/second-loss vocabulary (policy guarantees: government first loss, Trust second loss, AAA entity behind; portfolios: regional fund holds the first-loss tranche, as in 3.2); the $4bn country stake is borrowed through development policy lending.
