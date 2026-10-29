# 5.2 The Macro-Fiscal-Energy Scenario Tool

**Status:** working paper, version 0.1, 29 October 2026 (first draft, for Stephen's peer review). Medium form, about 5,000 words of body. Companion paper to the Climate Fiscal AI Tools (private repository), tool version v0.7 (`Macro_Fiscal_Energy_Scenario_Tool_v0.7.xlsx`).

## Files

| File | What it is |
|---|---|
| `MacroFiscalEnergyScenarioTool.qmd` | Master, v0.1 |
| `MacroFiscalEnergyScenarioTool.bib` | References (checked against Crossref or the publisher's page) |
| `MacroFiscalEnergyScenarioTool.docx` | Rendered with pandoc and the Chicago author-date CSL |
| `2.Source/stylized_run.py` | Produces Tables 3 and 4: runs the tool's GIMF-lite and DIGNAD-lite at their default illustrative calibrations on a stylized program, and the PriceFeasibility formulas on a stylized power sector. Imports the models read-only from the private repository (`MFM_PATH`); output in `stylized_run_output.txt` |

## Sources used (all in `climate-fiscal-ai-tools/MacFiscEnergyScenarioProto/`)

- `README.md`, `VersionNotes.md`, `CAVEATS.md` (dashboard, levers, modules, build, caveats, checks).
- `MacroFiscalModels/MacroFiscalModels_Method_v0_1.md` (GIMF-lite, DIGNAD-lite, DIGNAR-lite and LIC-DSF-lite equations, calibration, model choice, integration, validation, open issues); `gimf_lite.py`, `dignad_lite.py` (defaults and docstrings).
- `PriceFeasibility/README.md` (abatement, feasibility metrics F1–F3, priors).
- `InvestmentNeeds/national_model/NMIM_Method_v0_2.md` (structure, payer typology P1–P5, budget need). NMIM's own method belongs to paper 4.6.
- Public papers for the parent models (GIMF, DIG, DIGNAD, DIGNAR, LIC-DSF), cited in the `.bib`.

## Held back for confidentiality

- All country results from the tool: the Kenya briefing (`briefings/Kenya_briefing.md`), every country figure in the README, CAVEATS and method note (Kenya, Liberia, Angola, United States and others), `results/*.csv`, and NMIM's world and country-group totals. The paper uses only default illustrative calibrations and stylized inputs.
- The tool's Appendix E fiscal-risk inputs drawn from an internal-looking World Bank Climate Fiscal Risk Dashboard v1.5 (mentioned in 5.3 only by its public underlying series).
- Open decisions for the owner listed in the tool's README (model choice for concessional borrowers, which channels to credit, hand-to-mouth proxy, trade data) are described in general terms only.

## Notes for the editor

- The tool's LIC-DSF-lite coefficients are flagged in its own docs as "as recalled from the 2018 Guidance Note"; the paper quotes only the PV of external debt to GDP thresholds (30/40/55) and says the rest must be checked against the current note.
- Paper 4.6 (Public Investment) should describe NMIM in full; this paper only summarizes the payer typology and budget-need formula.
