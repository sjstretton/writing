# 2.2 From Projects to Asset Classes: Two-Stage Finance and Synthetic Sovereign Bonds for Clean Power

**Status:** first full draft, version 0.1 (29 October 2026). Working paper and Climate Fiscal Policy Brief No. 2.2. Awaiting Stephen's peer review. Series plan: `../SeriesArchitecture.md`.

**Question.** Once payment risk is removed, how do individual clean power projects become standard securities that institutional and domestic savers will buy at low cost?

**Answer.** Split each project at commissioning (construction loans against a contingent power purchase agreement; operating plants refinanced), pool operating plants across countries under one standard contract, and tranche the pool: first-loss equity (Climate Investment Trust regional funds), a thin mezzanine or sovereign co-guarantee, and a senior synthetic sovereign bond. Tiered conditional bond guarantees cover grids and storage; a local-currency senior tranche serves domestic savers.

## Files

| File | What |
|---|---|
| `CleanPowerAssetClasses.qmd` / `.docx` / `.bib` | Working paper master (version 0.1), rendered with pandoc |
| `1.Presentation/Brief-CleanPowerAssetClasses.qmd` / `.docx` / `.bib` | Policy brief, Climate Fiscal Policy Brief No. 2.2 |
| `1.Presentation/figures/make_figures.py` | Brief figures (reuses the working-paper code) |
| `2.Source/model.py` | LCOE, two-stage refinancing, Vasicek first-loss sizing, two-factor host-country model, tiered guarantee; prints every table |
| `2.Source/make_wp_figures.py`, `2.Source/figures/` | Working-paper figures |
| `3.RelatedPiecesAndLinks/` | Source material (synthetic sovereign bonds note; "A Solar Economy Financing System" with Jasper Zimmermann) |

Regenerate: `python3 2.Source/model.py`, `python3 2.Source/make_wp_figures.py`, `python3 1.Presentation/figures/make_figures.py`, then pandoc (see `A Writing Instructions/Writing Standards/briefing-series-spec.md`).

## Lineage and co-authors

- Two-stage finance, tiered bond guarantee and regional equity funds: "A Solar Economy Financing System" (Stephen Stretton and **Jasper Zimmermann**), `3.RelatedPiecesAndLinks/StandardizedTwoStage/`. Credited in the working paper's first footnote and the brief's small print.
- Synthetic sovereign bonds: `3.RelatedPiecesAndLinks/Background-SyntheticSovereignBonds.qmd` and *Time and Chance* chs 7–8, 10, 14–15, 23.
- First-loss provider: Equity De-risking for Clean Energy, now part of 3.2 (`3.SovereignIncentives/3.2.ClimateInvestmentTrust/8.PreviousVersions/EquityDeRiskingForCleanEnergy.qmd`).
- Payment intermediary: paper 2.1 (cited, summarized in one paragraph).

## Open items

- Pool default, recovery and correlation parameters are stylized but bracketed by Moody's (2017) project finance data and the GEMs (2024) recovery statistics; recalibrate to GEMs loan-level data when available.
- Senior "near-AAA / investment grade" labels are indicative, not rating-agency mappings.
