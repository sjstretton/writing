# 6.3 Public Investment in CPAT: Investment Needs and the Efficiency of Public Spending

**Status:** working paper v0.2, brief v1.0 (Climate Fiscal Policy Brief No. 6.3, "Price the Capital, Then Test the Budget") and a ten-slide deck, 31 October 2026, after a peer review (`5.Notes/PeerReview-2026-10-31.md`) and a reference check (`5.Notes/BibCheck-2026-10-31.md`). v0.1 and the old deck are in `8.PreviousVersions/`. Companion to the CPAT-AI repository. Series plan: `../SeriesArchitecture.md`.

**Question.** How can CPAT be extended to estimate climate investment needs by country and sector, price them at the cost of capital countries face, and test whether public money should pay for them?

**Answer.** Investment = physical change × unit capital cost × local price level, annualized with a capital recovery factor and read through three lenses (market WACC; 6 percent social rate; 6 percent plus co-benefits and carbon). Public spending is scored by the marginal value of public funds against the marginal cost of public funds (default 1.2), after additionality, delivery haircuts, a fiscal ledger, capex/opex on one footing and six financing routes. Propositions: break-even cost of capital (12.6 percent for a stylized asset; CPAT's optional income-group rate for LMICs, 12.5 percent, sits on it; CPAT's default is a country rate plus a technology premium); the rule nests the World Bank ENPV test and prices revenue returns at λ − 1; tenor is not price; a PPA priced above the government's rate is debt in disguise. Section 6 (added 29 Oct 2026) adds country runs: the investment-needs tool's 2030 results for Kenya, Uganda and St Lucia (Table 3: investment 4.0–4.7% of GDP; incremental cost a net cost at market rates and 6% in Kenya and Uganda, a gain with co-benefits; a gain at any rate in St Lucia) and the October 2025 SISEPUEDE run for Uganda (net-zero NPV $161bn at 6%; cash-visible benefits 18% of the total; power 6% of technical cost).

## Files

| File | What |
|---|---|
| `PublicInvestment.qmd` / `.docx` / `.bib` | Working paper master (version 0.2), rendered with pandoc |
| `1.Presentation/Brief-PublicInvestment.qmd` / `.docx` / `.bib` | Policy brief master (version 1.0); figures copied by `1.Presentation/figures/make_figures.py` |
| `1.Presentation/slides.json`, `Slides-PublicInvestment.pptx` | Ten-slide deck (built with the shared `make_deck.py`) |
| `2.Source/make_figures.py` | Figures: break-even, island routes, lenses (writes `2.Source/figures/`) |
| `2.Source/investment_lenses.py` | Table 1 (three cost-of-capital lenses, break-even WACC, CPAT default WACCs) |
| `2.Source/sids_worked_example.py` | Table 2 (stylized small-island solar plant, five financing routes); writes the two CSVs beside it; asserts the accounting identities |
| `2.Source/sids_worked_example_results.csv`, `..._sensitivity.csv` | Script output |
| `2.Source/country_runs.py` | Section 6: reads the investment-needs workbook and the SISEPUEDE Uganda run directly (paths to the two private repos as arguments); writes `country_runs_lenses.csv`, `country_runs_uganda.csv` |
| `3.RelatedPiecesAndLinks/` | Source notes (see below) |

Regenerate: `cd 2.Source && python3 investment_lenses.py && python3 -I sids_worked_example.py && python3 make_figures.py && python3 country_runs.py`, then from the folder root `pandoc PublicInvestment.qmd -f markdown --citeproc --bibliography=PublicInvestment.bib --csl=<chicago-author-date.csl> --resource-path=. -o PublicInvestment.docx`.

## Sources used

- `3.RelatedPiecesAndLinks/CDPM-GlobalInvestmentNeeds-SISEPUEDE.docx`: method (equations 1–7), the four definitional choices, three lenses. Global totals re-sourced to the public IHLEG third report.
- `3.RelatedPiecesAndLinks/CDPM-PublicSpendingEfficiencyAndCBA.docx` and the markdown folder: design brief, MCPF/MVPF theory, frontiers and cross-sector CBA, capex/opex/PPP/PPA notes, SIDS worked example (script copied unchanged to `2.Source/`).
- `climate-fiscal-ai-tools/MacFiscEnergyScenarioProto/InvestmentNeeds` (README): method (allocation, lenses, PIMA haircut).
- CPAT public documentation (`cpat_ai/docs/CPAT_full_documentation_qmd/03_Mitigation.qmd`): power investment logit, income-group WACC (described as the default there). The model's actual default (country WACC plus technology premium) is from `cpat_ai/excel_ai/mitigation/docs/methods/Power.md` §1.4, §2.5, §6.

## Now used (cleared by Stephen, 29 Oct 2026, as illustrative tool results)

- **Kenya, Uganda, St Lucia investment needs, 2030** (Table 3): `climate-fiscal-ai-tools/MacFiscEnergyScenarioProto/InvestmentNeeds/Mitigation_Investment_Needs_v1.1.xlsx`, sheet Results_Country. Cited as @InvNeedsTool2026. A Tier 3 allocation of group totals, labelled as such.
- **Uganda SISEPUEDE run, October 2025** (Section 6 text): `cpmodelai/CPAT-CDPM/MainProjectFolder/9. CPAT-LTS Project/CCDR Example Data/sisepuede_run_2025-10-29T19;49;25.722413/cba_results.csv` (and the run's input-output file for GDP). Recomputed from the raw file, not copied from the source note (whose Table 2 has 136.0 for NDC 2020 indoor air pollution; the raw file gives 133.0). Cited as @SISEPUEDEUganda2025.

## Still held back

- The St Lucia and Kenya *pilots* in the source note are plans, not runs; nothing from them is used. No Kenya or St Lucia SISEPUEDE run exists in the material.
- The Uganda NDC 3.0 technical memo in the same run folder (`SiSEPUEDE_analysis-Uganda v2025_10_16.docx`) is an unfinished draft ("FIGURE HERE"); not used.
- The Egypt CPAT figures in the source notes (not needed here).
- Files named `internal_*` (internal CDPM and macro tool, NMIM, internal macro-fiscal tool) were used for general design logic only; the paper names no internal tool, contract, team or partnership terms. The investment-needs model's internal name (NMIM) and the PSV module/bridge file names are not used; the national stock-and-flow model's results are not used.
- The renaming of SISEPUEDE inside the World Bank is not mentioned; the paper uses the public name. The FY27 work plan is not used.

## Open items for review

- The stylized savings rate (b = 0.133 per dollar a year) is calibrated to give a benefit-cost ratio of 1.70 at 6 percent, as in the source note's reading of the SISEPUEDE LAC results; check against Kalra et al. (2023) before outside use.
- Worked-example inputs are stylized (island premium on capex, battery cost, 8 percent sovereign rate, concessional terms). The IPCC diesel emission factor and the 5 percent PV-of-debt rate were not verified in the source notes.
- CRF convention: resolved in v0.2 by stating both (break-even 12.6 percent end-of-year, 14.8 percent with CPAT's year-zero convention); the extension should adopt one convention with the core model.
- v0.2 body about 7,800 words including tables; executive summary about 700 words; brief about 2,100 words.
- Section 6 country numbers could not be recomputed on 31 Oct 2026 (the two private repositories were not available in that session); they are unchanged from v0.1.
