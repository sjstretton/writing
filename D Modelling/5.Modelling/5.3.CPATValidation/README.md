# 5.3 Validating CPAT: Baselines, Back-Casts and Model Comparisons

**Status (31 October 2026):** working paper v0.2 and policy brief v1.0 (Climate Fiscal Policy Brief No. 5.3), peer-reviewed and with every reference checked; ten-slide deck. Previous versions in `8.PreviousVersions/`. Series plan: `../5.0.Overview/SeriesArchitecture.md`.

**Question.** How well does CPAT's mitigation module fit base-year data, history, other models and ex-post evidence, and does independent code reproduce it?

**Answer.** Well enough for ranges and policy comparisons, not for point forecasts. Base-year fit is by calibration (and can carry a data break: Egypt's baseline 16–32 percent below the 2022–2024 inventory). Back-cast level errors over 2000–2017 are 5 percent of mean emissions for Australia and 92 percent for China. Baselines and price responses are of the same order as IEA STEPS, Enerdata and EPM; the response to a $10 price, put on a growth-rate basis (0.7–0.8 percent a year), is of the same order as the best cross-country estimate (0.5 percent), and the ex-post literature is too wide to test it. A $75 tax cuts G20 CO₂ by 29 percent in 2030, 7 to 39 percent as the price elasticities move ±2 standard deviations. Independent code reproduces legacy blocks to 1e-13 or better. Every published check predates the bug fixes (231 legacy bugs at release 1.1.0) and should be rerun.

## Files

| File | What |
|---|---|
| `CPATValidation.qmd` / `.docx` / `.bib` | Working paper master (v0.2) with executive summary (chapter 1) and Appendix A (which numbers are the documentation's, recomputed or new) |
| `1.Presentation/Brief-CPATValidation.qmd` / `.docx` / `.bib` | Policy brief master (v1.0); `.bib` copied from the working paper's for the keys it cites |
| `1.Presentation/slides.json`, `Slides-CPATValidation.pptx` | Deck (10 slides), built with `H Writing Instructions/Writing Standards/templates/make_deck.py` |
| `2.Source/make_figures.py`, `2.Source/figures/` | Figures 1 (back-cast errors) and 2 (sensitivity), from the published CPAT numbers |
| `1.Presentation/figures/make_figures.py` | Regenerates the figures and copies them for the brief and deck |
| `5.Notes/PeerReview-2026-10-31.md`, `BibCheck-2026-10-31.md` | Referee review of v0.1 and the reference check |

Render (pandoc), from the folder of each master:
`pandoc <Name>.qmd -f markdown --lua-filter="<repo>/H Writing Instructions/Scripts/Website/quarto-xref.lua" --lua-filter="<repo>/H Writing Instructions/Scripts/Website/web-links.lua" --citeproc --bibliography=<Name>.bib --csl="<repo>/E Website/chicago-author-date.csl" -o <Name>.docx`

## Sources used (all public)

- CPAT methodology, 2023 edition corrected online 31 Oct 2026 (https://cpmodelai.github.io/cpat_ai/): chapter 3 (Mitigation), "Testing and validation summary", "Validation" and Appendix H; chapter 6 (Air pollution), "Validation" and "Caveats". Repository copy: `docs/CPAT_full_documentation_qmd/`.
- CPAT-AI repository, release 1.1.0 (https://github.com/cpmodelai/cpat_ai, commit 108f976): `docs/CPAT_model_documentation_qmd/` (04_Power, 05_Road_transport, 06_Emissions_and_ETS, 08_Distribution: check sections), `docs/CPAT_coded_documentation_qmd/` (01_Using_the_model, B_Project), `coded/cpat_testing/compare/legacy_comparison.md`, `coded/CHANGELOG.md`, `excel_ai/core/BUGS.md` and `ISSUES.md`.
- Published literature, each verified (see `5.Notes/BibCheck-2026-10-31.md`).

## Held back (confidentiality)

- No proprietary CPAT data. Egypt numbers used are those printed in the public CPAT-AI documentation (UNFCCC inventory values, the calibration factor, the summary shares of the Coded CPAT versus legacy comparison), not the underlying tables. The public data edition perturbs Egypt's proprietary rows within ±3 percent.
- No Egypt policy-scenario results; no Public Finance Review or internal material.

## Notes for Stephen

- **Source errors found (for the CPAT-AI register; not registered here):** (1) in the methodology's Hindcasting section the coal-price RMSE table repeats the energy CO₂ table; (2) the same section says projected coal prices were "above" observed while describing their ratio as "under 1"; (3) the CPAT-AI emissions documentation's "16–29 percent" Egypt gap is 16–32 percent (2023 is 31.6 percent).
- **Conclusions changed from v0.1:** CPAT's response to a carbon price is no longer called "at or above the top" of the ex-post range (different metrics; Döbbeling-Hildebrandt et al. 2024 added), and the gasoline elasticity is now "uncertain" rather than "too high" (Brons et al. 2008); residential electricity and services remain the clearer gaps. Check you agree.
- **Bug count:** the series used 228 (release 1.0.2); the register now lists 231 (release 1.1.0). This paper gives both once and uses 231 elsewhere.
- The version used for the model comparisons is not stated in the documentation; only the back-cast's (CPAT 1.0pre_043).
