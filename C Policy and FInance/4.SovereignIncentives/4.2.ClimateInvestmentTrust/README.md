# 4.2 The Climate Investment Trust: Hold Capital, Lend Its Strength

Series 4 (Sovereign Incentives) flagship, paired with 4.1 (notional capitalized value and guarantee capacity). Moved here from the finance series (then numbered 2.2) on 29 Oct 2026.

## Status (31 Oct 2026)

- Working paper `ClimateInvestmentTrust.qmd` (master), version 0.3, rendered to `ClimateInvestmentTrust.docx`: executive summary added (about 700 words); body about 9,900 words. Peer review and changes in `5.Notes/PeerReview-2026-10-31.md`; sources in `5.Notes/BibCheck-2026-10-31.md`.
- Brief `1.Presentation/Brief-ClimateInvestmentTrust.qmd`, Climate Fiscal Policy Brief No. 4.2, version 1.0 (series format, about 2,100 words), rendered to `.docx`.
- Deck `1.Presentation/Slides-ClimateInvestmentTrust.pptx`, ten slides, built from `slides.json`.
- Headline numbers: about 80 dollars of interest savings per donor dollar on the MDB record (63 at a 2 percent carry); 2.7 in the stress case (2.3); about 13 while the stress-case buffer is held (2 percent carry); \$5bn supports about \$1tn on paper, about \$390bn if calls are paid in cash before recovery, \$54bn in the stress case. Growth is now reported with the stress-case buffer held (\$34bn after 10 years on the record with \$95bn of private co-investment; levels off near \$28bn in the stress case). The v0.2 long-run figure of \$57bn is retired.

## Files

| File | What |
|---|---|
| `ClimateInvestmentTrust.qmd`, `.bib`, `.docx` | Working paper master, v0.3 |
| `1.Presentation/Brief-ClimateInvestmentTrust.*` | Brief No. 4.2, v1.0 |
| `1.Presentation/slides.json`, `Slides-ClimateInvestmentTrust.pptx` | Deck (ten slides) |
| `5.Notes/` | Peer review and reference check, 31 Oct 2026 |
| `1.Presentation/figures/make_figures.py` | Brief figure (uses `2.Source/model.py`) |
| `2.Source/model.py` | Buffer sizing, growth dynamics, allocation rule; prints every number used |
| `2.Source/make_wp_figures.py`, `2.Source/figures/` | Working-paper figures |
| `1.Presentation/Briefing-CIT.*`, `Briefing-TechnicalSummaryCIT.*`, `Pres-Introduction.pptx` | Older briefings (2024), source material only |
| `3.RelatedPiecesAndLinks/` | Global Solar Economy and Climate Café notes (source material) |
| `8.PreviousVersions/` | Working paper v0.1 (Sept 2026) and v0.2; brief, slides and model v0.1/v0.2 |
| `8.PreviousVersions/EquityDeRiskingForCleanEnergy.*` | Standalone equity de-risking paper, folded into v0.1 |
| `9.Archive/` | The Climate Incentives Trust (May 2024) and related notes |

Render (from the folder holding the qmd), as in `H Writing Instructions/Writing Standards/briefing-series-spec.md`:
`pandoc X.qmd -f markdown --lua-filter="<repo>/H Writing Instructions/Scripts/Website/quarto-xref.lua" --lua-filter="<repo>/H Writing Instructions/Scripts/Website/web-links.lua" --citeproc --bibliography=X.bib --csl="<repo>/E Website/chicago-author-date.csl" -o X.docx`

## Lineage

- First proposed as the **Climate Incentives Trust** (May 2024; `9.Archive/The Climate Incentives Trust.docx` and tracked version), with a technical summary and Climate Café note (2024).
- *Time and Chance* (book manuscript): ch. 14 ("One Structure, Several Views": one pool under five names), ch. 18 (policy-lending fund, dynamic incentives), ch. 19 (Climate Investment and Insurance Fund), ch. 20 (Climate Incentives Trust).
- *The Right Policy at the Wrong Time*, ch. 5: the international feebate needs a trust to hold the pot.
- Equity de-risking / regional fund design: joint two-stage climate project finance work with **Jasper Zimmermann** (credited in both papers).

## Settled in v0.2

One name (Climate Investment Trust); one fee rule and return (25% of private investment returns, 10% gross return); first-/second-loss vocabulary (policy guarantees: government first loss, Trust second loss, AAA entity behind; portfolios: regional fund holds the first-loss tranche, as in 3.2); the $4bn country stake is borrowed through development policy lending.
