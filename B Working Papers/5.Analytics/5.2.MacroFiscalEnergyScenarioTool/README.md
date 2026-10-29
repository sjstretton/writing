# 5.2 The Macro-Fiscal-Energy Scenario Tool

**Status:** working paper, version 0.1, 29 October 2026 (first draft, for Stephen's peer review). Medium form, about 6,300 words of body after the Kenya run (Section 7, Table 5) was added on 29 Oct 2026. Companion paper to the Climate Fiscal AI Tools (private repository), tool version v0.7 (`Macro_Fiscal_Energy_Scenario_Tool_v0.7.xlsx`).

## Files

| File | What it is |
|---|---|
| `MacroFiscalEnergyScenarioTool.qmd` | Master, v0.1 |
| `MacroFiscalEnergyScenarioTool.bib` | References (checked against Crossref or the publisher's page) |
| `MacroFiscalEnergyScenarioTool.docx` | Rendered with pandoc and the Chicago author-date CSL |
| `2.Source/stylized_run.py` | Produces Tables 3 and 4: runs the tool's GIMF-lite and DIGNAD-lite at their default illustrative calibrations on a stylized program, and the PriceFeasibility formulas on a stylized power sector. Imports the models read-only from the private repository (`MFM_PATH`); output in `stylized_run_output.txt` |
| `2.Source/kenya_run.py`, `kenya_run_output.txt` | Section 7 (Table 5): reads the tool's Kenya results read-only from the private repository |

## Sources used (all in `climate-fiscal-ai-tools/MacFiscEnergyScenarioProto/`)

- `README.md`, `VersionNotes.md`, `CAVEATS.md` (dashboard, levers, modules, build, caveats, checks).
- `MacroFiscalModels/MacroFiscalModels_Method_v0_1.md` (GIMF-lite, DIGNAD-lite, DIGNAR-lite and LIC-DSF-lite equations, calibration, model choice, integration, validation, open issues); `gimf_lite.py`, `dignad_lite.py` (defaults and docstrings).
- `PriceFeasibility/README.md` (abatement, feasibility metrics F1–F3, priors).
- `InvestmentNeeds/national_model/NMIM_Method_v0_2.md` (structure, payer typology P1–P5, budget need). NMIM's own method belongs to paper 4.6.
- Public papers for the parent models (GIMF, DIG, DIGNAD, DIGNAR, LIC-DSF), cited in the `.bib`.

## Now used (cleared by Stephen, 29 Oct 2026, as illustrative tool results)

- **Kenya run** (Section 7, Table 5; abstract): `MacFiscEnergyScenarioProto/MacroFiscalModels/results/integrated_results.csv` (row KEN: budget need, pricing screen, macro model, debt paths, GIMF-lite cross-check, debt rating); `InvestmentNeeds/national_model/results/nmim_summary_v0_2.csv` (row KEN: 2030 investment, payer split, emissions); `briefings/Kenya_briefing.md` (20 Oct 2026; sector split of the incremental need, DSF indicator table, reserve-cover sensitivity). Cited as @MFESTKenya2026. The briefing's "8.4% WACC" differs from the 9.66% in the model summary; the paper quotes neither.

## Still held back

- Other countries' results (Liberia, Angola, United States and others in README, CAVEATS and the method note; `results/*.csv` beyond Kenya) — not needed.
- The tool's Appendix E fiscal-risk inputs drawn from an internal-looking World Bank Climate Fiscal Risk Dashboard v1.5, including the Kenya backdrop in briefing section 6 (credit rating index, climate-PFM snapshot).
- Internal code names: the integrated tool's working name in the briefing and the investment model's acronym. The acronym, previously used five times in this paper, was replaced by "the investment model" on 29 Oct 2026.
- Open decisions for the owner listed in the tool's README (model choice for concessional borrowers, which channels to credit, hand-to-mouth proxy, trade data) are described in general terms only.

## Notes for the editor

- The tool's LIC-DSF-lite coefficients are flagged in its own docs as "as recalled from the 2018 Guidance Note"; the paper quotes only the PV of external debt to GDP thresholds (30/40/55) and says the rest must be checked against the current note.
- Paper 4.6 (Public Investment) describes the investment method; this paper only summarizes the payer typology and budget-need formula.
