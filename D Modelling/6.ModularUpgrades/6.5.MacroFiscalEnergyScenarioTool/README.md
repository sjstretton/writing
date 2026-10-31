# 6.5 The Macro-Fiscal-Energy Scenario Tool

**Status (31 October 2026):** working paper version 0.2 (about 7,800 words of body including tables, executive summary of about 640 words as chapter 1) and policy brief version 1.0 (Climate Fiscal Policy Brief No. 6.5, key `CFPB65`; working paper key `StrettonWP65`), both peer-reviewed (`5.Notes/PeerReview-2026-10-31.md`) with every reference checked (`5.Notes/BibCheck-2026-10-31.md`); deck of 10 slides on the new builder. Version 0.1 (29 October 2026) is in `8.PreviousVersions/`. Companion paper to the Climate Fiscal AI Tools (private repository), tool version v0.7. Title unchanged; the subtitle now states the finding ("Financing and Efficiency, Not the Size of the Program, Decide What Climate Investment Does to Growth and Debt").

**Question.** Can the investment need, feasible carbon pricing, the growth effect and the debt test be run as one consistent, inspectable scenario for any country?

**Answer.** Yes, with simplified ("lite") versions of the parent models. The scenario says that the financing mix and investment efficiency move debt and growth more than the program's size, and that the binding political limit decides whether pricing raises revenue. For Kenya (illustrative): budget need 0.5 percent of GDP in 2030, mostly land use and non-CO₂; power-sector pricing covers about 5 percent; +7.2 points of GDP of debt by 2050 against debt held at its 2024 level; high risk of debt distress before and with the program, as in the published IMF-World Bank DSA.

## Files

| File | What it is |
|---|---|
| `MacroFiscalEnergyScenarioTool.qmd` / `.docx` / `.bib` | Working paper master (v0.2), rendered with pandoc (Chicago author-date); every `.bib` entry carries a `verified 31 Oct 2026` note |
| `1.Presentation/Brief-MacroFiscalEnergyScenarioTool.qmd` / `.docx` / `.bib` | Policy brief master (v1.0); its `.bib` is copied from the working paper's for the keys it cites |
| `1.Presentation/slides.json`, `Slides-MacroFiscalEnergyScenarioTool.pptx` | Deck (10 slides), built with `H Writing Instructions/Writing Standards/templates/make_deck.py` |
| `1.Presentation/figures/make_figures.py` | Makes `fig_stylized_run.png` and `fig_kenya_need.png` (numbers as the working paper) |
| `2.Source/stylized_run.py`, `stylized_run_output.txt` | Table 3 (and Table 4): runs the tool's GIMF-lite and DIGNAD-lite at their default illustrative calibrations. Imports the models read-only from the private repository (`MFM_PATH`); not re-run on 31 Oct 2026 (repository not reachable), so Table 3 rests on the saved output of 29 Oct |
| `2.Source/pricing_screen.py`, `pricing_screen_output.txt` | Table 4 and the pass-through sensitivity (peer review M7), with no dependence on the private repository |
| `2.Source/kenya_run.py`, `kenya_run_output.txt` | Table 5: reads the tool's Kenya results read-only from the private repository |
| `5.Notes/` | Peer review and reference check, 31 October 2026 |
| `8.PreviousVersions/` | Working paper v0.1 (qmd, docx, bib); deck v0.1 (pptx, json); old figure script and figure |

Render (from this folder; the brief the same way from `1.Presentation/`): `pandoc MacroFiscalEnergyScenarioTool.qmd -f markdown --lua-filter="<repo>/H Writing Instructions/Scripts/Website/quarto-xref.lua" --lua-filter="<repo>/H Writing Instructions/Scripts/Website/web-links.lua" --citeproc --bibliography=MacroFiscalEnergyScenarioTool.bib --csl="<repo>/E Website/chicago-author-date.csl" -o MacroFiscalEnergyScenarioTool.docx`.

## Sources used (all in `climate-fiscal-ai-tools/MacFiscEnergyScenarioProto/`)

- `README.md`, `VersionNotes.md`, `CAVEATS.md` (dashboard, levers, modules, build, caveats, checks).
- `MacroFiscalModels/MacroFiscalModels_Method_v0_1.md` (GIMF-lite, DIGNAD-lite, DIGNAR-lite and LIC-DSF-lite equations, calibration, model choice, integration, validation, open issues); `gimf_lite.py`, `dignad_lite.py` (defaults and docstrings).
- `PriceFeasibility/README.md` (abatement, feasibility metrics F1–F3, priors).
- `InvestmentNeeds/national_model/NMIM_Method_v0_2.md` (structure, payer typology P1–P5, budget need). NMIM's own method belongs to paper 6.3.
- Public papers for the parent models (GIMF, DIG, DIGNAD, DIGNAR, LIC-DSF), cited in the `.bib`.

## Now used (cleared by Stephen, 29 Oct 2026, as illustrative tool results)

- **Kenya run** (Section 7, Table 5; abstract): `MacFiscEnergyScenarioProto/MacroFiscalModels/results/integrated_results.csv` (row KEN: budget need, pricing screen, macro model, debt paths, GIMF-lite cross-check, debt rating); `InvestmentNeeds/national_model/results/nmim_summary_v0_2.csv` (row KEN: 2030 investment, payer split, emissions); `briefings/Kenya_briefing.md` (20 Oct 2026; sector split of the incremental need, DSF indicator table, reserve-cover sensitivity). Cited as @MFESTKenya2026. The briefing's "8.4% WACC" differs from the 9.66% in the model summary; the paper quotes neither.

## Still held back

- Other countries' results (Liberia, Angola, United States and others in README, CAVEATS and the method note; `results/*.csv` beyond Kenya) — not needed.
- The tool's Appendix E fiscal-risk inputs drawn from an internal-looking World Bank Climate Fiscal Risk Dashboard v1.5, including the Kenya backdrop in briefing section 6 (credit rating index, climate-PFM snapshot).
- Internal code names: the integrated tool's working name in the briefing and the investment model's acronym. The acronym, previously used five times in this paper, was replaced by "the investment model" on 29 Oct 2026.
- Open decisions for the owner listed in the tool's README (model choice for concessional borrowers, which channels to credit, hand-to-mouth proxy, trade data) are described in general terms only.

## Public sources used for the Kenya checks (31 Oct 2026)

Joint IMF-IDA DSA of December 2023 (IMF Country Report No. 24/13); LIC-DSF Guidance Note (2018) and Supplement (2024); IMF WEO database (debt); World Bank International Debt Statistics (creditor mix) and WDI (trade); Ember yearly electricity data; Kenya's updated NDC (December 2020). Not readable from the session: pefa.org (so Kenya's PEFA score is not quoted) and the Kenya Treasury website.

## Notes for the editor

- The tool's LIC-DSF-lite coefficients are flagged in its own docs as "as recalled from the 2018 Guidance Note". The paper now quotes the published cut-offs, thresholds and benchmarks (checked in the Guidance Note, Tables 5-7) and the CI coefficients appear in the IMF's Kenya DSA (Text Table 7: 0.385, 2.719, 4.052, -3.990, 2.022, 13.520); the tool's code should be checked against these.
- The tool's Kenya Composite Indicator (2.73) differs from the published 3.01 because the build assumes imports of 40 percent of GDP (WDI: 22-24 percent). Adding WDI trade data to the build would fix it.
- Paper 6.3 (Public Investment) describes the investment method; this paper only summarizes the payer typology and budget-need formula.
