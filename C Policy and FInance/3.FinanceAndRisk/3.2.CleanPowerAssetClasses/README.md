# 3.2 From Projects to Asset Classes: Two-Stage Finance and Synthetic Sovereign Bonds for Clean Power

**Status:** working paper v0.2 and policy brief v1.0 (31 October 2026), upgraded to the 1.1 standard: peer review (`5.Notes/PeerReview-2026-10-31.md`), sources checked (`5.Notes/BibCheck-2026-10-31.md`), executive summary, ten-slide deck. Previous versions in `8.PreviousVersions/`. Series plan: `../3.0.Overview/SeriesArchitecture.md`.

**Main change in v0.2.** The pool refinances each plant's senior debt (80 percent of its cost); the sponsor's equity stays below it. The saving on the price of solar power is therefore about a fifth (19 percent), not about a quarter (27 percent) as in v0.1. With a cushion as thick as real deals carry (30 percent, as in Bayfront 2018), it is 14 percent.

**Question.** Once payment risk is removed, how do individual clean power projects become standard securities that institutional and domestic savers will buy at low cost?

**Answer.** Split each project at commissioning (construction loans against a contingent power purchase agreement; operating plants refinanced), pool operating plants across countries under one standard contract, and tranche the pool: first-loss equity (Climate Investment Trust regional funds), a thin mezzanine or sovereign co-guarantee, and a senior synthetic sovereign bond. Tiered conditional bond guarantees cover grids and storage; a local-currency senior tranche serves domestic savers.

## Files

| File | What |
|---|---|
| `CleanPowerAssetClasses.qmd` / `.docx` / `.bib` | Working paper master (version 0.2), rendered with pandoc |
| `1.Presentation/Brief-CleanPowerAssetClasses.qmd` / `.docx` / `.bib` | Policy brief, Climate Fiscal Policy Brief No. 3.2 (version 1.0) |
| `1.Presentation/slides.json`, `Slides-CleanPowerAssetClasses.pptx` | Ten-slide deck, built with `make_deck.py` |
| `1.Presentation/figures/make_figures.py` | Brief and deck figures (reuses the working-paper code) |
| `2.Source/model.py` | LCOE, two-stage refinancing with project equity, Vasicek first-loss sizing, finite pools, agency-style structure, two-factor host-country model, tiered guarantee; prints every table (needs SciPy) |
| `5.Notes/` | Peer review and reference check, 31 Oct 2026 |
| `2.Source/make_wp_figures.py`, `2.Source/figures/` | Working-paper figures |
| `3.RelatedPiecesAndLinks/` | Source material (synthetic sovereign bonds note; "A Solar Economy Financing System" with Jasper Zimmermann) |

Regenerate: `python3 2.Source/model.py`, `python3 2.Source/make_wp_figures.py`, `python3 1.Presentation/figures/make_figures.py`, then pandoc (see `H Writing Instructions/Writing Standards/briefing-series-spec.md`) and `make_deck.py`.

## Lineage and co-authors

- Two-stage finance, tiered bond guarantee and regional equity funds: "A Solar Economy Financing System" (Stephen Stretton and **Jasper Zimmermann**), `3.RelatedPiecesAndLinks/StandardizedTwoStage/`. Credited in the working paper's first footnote and the brief's small print.
- Synthetic sovereign bonds: `3.RelatedPiecesAndLinks/Background-SyntheticSovereignBonds.qmd` and *Time and Chance* chs 7–8, 10, 14–15, 23.
- First-loss provider: Equity De-risking for Clean Energy, now part of 4.2 (`4.SovereignIncentives/4.2.ClimateInvestmentTrust/8.PreviousVersions/EquityDeRiskingForCleanEnergy.qmd`).
- Payment intermediary: paper 3.1 (cited, summarized in one paragraph).

## Open items

- Pool default, recovery and correlation parameters are stylized but anchored to Moody's (2017) project finance data (year 4–10 default rate about 2.8 percent; lower-middle-income stress 10.2 percent and 72 percent recovery); recalibrate to GEMs loan-level data when available.
- The 3.0 overview still quotes v0.1 numbers ("5 to 10 percent" subordination, "about a quarter" off the price of solar): it should say 5 to 8 percent in a large pool, and about a fifth (14–19 percent).
- Senior "near-AAA / investment grade" labels are indicative, not rating-agency mappings.
