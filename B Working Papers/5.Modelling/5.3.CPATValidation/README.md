# 4.3 Validating CPAT: Baselines, Back-Casts and Model Comparisons

**Status:** first full draft, version 0.1 (29 October 2026). One medium-length working paper (about 5,100 words of body including five tables), companion paper to the CPAT-AI repository (https://github.com/cpmodelai/cpat_ai). Awaiting Stephen's peer review. Series plan: `../SeriesArchitecture.md`.

**Question.** How well does CPAT's mitigation module fit base-year data, history and other models, and do its reimplementations reproduce it?

**Answer.** Well enough for ranges and policy comparisons, not for point forecasts. Base-year fit is by calibration; back-casts from 2000 track trends (normalized RMSE of greenhouse gases 0.05 Australia, 0.10 United States, 0.92 China); baselines and price responses are of the same order as IEA STEPS, Enerdata and EPM; the short-run response to a $10 carbon price (−2.4 percent) is at the top of the 0–2 percent per year ex-post range; results are most sensitive to price elasticities (a $75 tax cuts G20 CO2 by 7 to 39 percent across ±2 standard deviations, 29 percent by default); the rebuilt models reproduce legacy blocks to 1e-14 or better. All published checks predate the 228 legacy bug fixes and should be rerun on Coded CPAT for every country.

## Files

| File | What |
|---|---|
| `CPATValidation.qmd` / `.docx` / `.bib` | Working paper master (version 0.1), rendered with pandoc (Chicago author-date) |
| `1.Presentation/`, `2.Source/`, `3.RelatedPiecesAndLinks/`, `5.Notes/` | Empty (no figures or code needed: every number is the documentation's own) |

Render: from this folder, `pandoc CPATValidation.qmd -f markdown --citeproc --bibliography=CPATValidation.bib --csl=<chicago-author-date.csl> --resource-path=. -o CPATValidation.docx`.

## Sources used

From the public CPAT-AI repository (read-only clone at `/home/user/cpmodelai/cpat_ai`):

- `docs/CPAT_full_documentation_qmd/03_Mitigation.qmd`: "Testing and validation summary" (line ~211), "Validation" (line ~2761: overview and test runs; panel estimation of energy demand; model comparisons with IEA STEPS, Enerdata and EPM; ex-post studies and CPAT semi-elasticities; hindcasting; parameter sensitivity), Appendix H (EPM, line ~4942).
- `docs/CPAT_full_documentation_qmd/06_Air_pollution.qmd`: "Validation: comparison with other models" (line ~2376) and caveats.
- `docs/CPAT_ai_documentation_qmd/05_Power.qmd` (validation sections), `06_Transport.qmd` (check results; legacy match), `07_Emissions.qmd` (section 5; calibration of energy CO2 to the inventory), `10_Distribution_Tab.qmd` (checks).
- `docs/CPAT_coded_documentation_qmd/06_Testing.qmd` and `coded/cpat_testing/compare/legacy_comparison.md` (Coded CPAT against legacy's cached Egypt baseline).
- `excel_ai/BUGS.md` and the v1.0.0 deck (high-priority bugs that affect baselines).
- External references verified on Crossref: Sargent (2013), Huntington, Weyant and Sweeney (1982), Craig, Gadgil and Koomey (2002), Koomey et al. (2003), Green (2021), Rafaty, Dolphin and Pretis (2020), Pesaran (2006), GBD 2019 Risk Factors Collaborators (2020), Vohra et al. (2021), Black et al. (2023).

## Held back (confidentiality)

- No proprietary CPAT data. Egypt numbers used are public: the UNFCCC inventory values and calibration factor in the public CPAT-AI documentation, and summary statistics of the Coded CPAT versus legacy comparison (shares of rows within 1 and 5 percent, median gaps), not the underlying values.
- No Egypt policy-scenario results.

## Notes for Stephen

- **Documentation error found:** in `03_Mitigation.qmd`, Hindcasting, the RMSE table under "Coal prices (historical vs CPAT)" repeats the energy CO2 table exactly. Candidate for a new DOC entry in the CPAT-AI register (not registered here: the repo is read-only for this task).
- The paper reads CPAT's short-term semi-elasticity (−2.4 percent for $10/t) as "at or above the top" of Green's 0–2 percent per year range, where the documentation says "comparable". Check you agree with the stricter reading.
- The validation chapter's comparisons with IEA STEPS, Enerdata and EPM report charts only; the paper says so and does not invent numbers from the charts.
- The version used for the model comparisons is not stated in the documentation; only the back-cast's (CPAT 1.0pre_043).
- Elasticities are summarized only as far as needed; full treatment is paper 4.4.
