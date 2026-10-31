# 6.3 Public Investment in CPAT: Investment Needs and the Efficiency of Public Spending

**Status:** first full draft, version 0.1 (29 October 2026). One medium-length working paper (about 6,000 words of body), companion to the CPAT-AI repository. Awaiting Stephen's peer review. Series plan: `../SeriesArchitecture.md`.

**Question.** How can CPAT be extended to estimate climate investment needs by country and sector, price them at the cost of capital countries face, and test whether public money should pay for them?

**Answer.** Investment = physical change × unit capital cost × local price level, annualized with a capital recovery factor and read through three lenses (market WACC; 6 percent social rate; 6 percent plus co-benefits and carbon). Public spending is scored by the marginal value of public funds against the marginal cost of public funds (default 1.2), after additionality, delivery haircuts, a fiscal ledger, capex/opex on one footing and six financing routes. Propositions: break-even cost of capital (12.6 percent for a stylized asset; CPAT's LMIC default sits on it); the rule nests the World Bank ENPV test and prices revenue returns at λ − 1; tenor is not price; a PPA priced above the government's rate is debt in disguise. Section 6 (added 29 Oct 2026) adds country runs: the investment-needs tool's 2030 results for Kenya, Uganda and St Lucia (Table 3: investment 4.0–4.7% of GDP; incremental cost a net cost at market rates and 6% in Kenya and Uganda, a gain with co-benefits; a gain at any rate in St Lucia) and the October 2025 SISEPUEDE run for Uganda (net-zero NPV $161bn at 6%; cash-visible benefits 18% of the total; power 6% of technical cost).

## Files

| File | What |
|---|---|
| `PublicInvestment.qmd` / `.docx` / `.bib` | Working paper master (version 0.1), rendered with pandoc |
| `2.Source/investment_lenses.py` | Table 1 (three cost-of-capital lenses, break-even WACC, CPAT default WACCs) |
| `2.Source/sids_worked_example.py` | Table 2 (stylized small-island solar plant, five financing routes); writes the two CSVs beside it; asserts the accounting identities |
| `2.Source/sids_worked_example_results.csv`, `..._sensitivity.csv` | Script output |
| `2.Source/country_runs.py` | Section 6: reads the investment-needs workbook and the SISEPUEDE Uganda run directly (paths to the two private repos as arguments); writes `country_runs_lenses.csv`, `country_runs_uganda.csv` |
| `3.RelatedPiecesAndLinks/` | Source notes (see below) |

Regenerate: `cd 2.Source && python3 investment_lenses.py && python3 -I sids_worked_example.py && python3 country_runs.py`, then from the folder root `pandoc PublicInvestment.qmd -f markdown --citeproc --bibliography=PublicInvestment.bib --csl=<chicago-author-date.csl> --resource-path=. -o PublicInvestment.docx`.

## Sources used

- `3.RelatedPiecesAndLinks/CDPM-GlobalInvestmentNeeds-SISEPUEDE.docx`: method (equations 1–7), the four definitional choices, three lenses. Global totals re-sourced to the public IHLEG third report.
- `3.RelatedPiecesAndLinks/CDPM-PublicSpendingEfficiencyAndCBA.docx` and the markdown folder: design brief, MCPF/MVPF theory, frontiers and cross-sector CBA, capex/opex/PPP/PPA notes, SIDS worked example (script copied unchanged to `2.Source/`).
- `climate-fiscal-ai-tools/MacFiscEnergyScenarioProto/InvestmentNeeds` (README): method (allocation, lenses, PIMA haircut).
- CPAT public documentation (`cpat_ai/docs/CPAT_full_documentation_qmd/03_Mitigation.qmd`): power investment logit, income-group WACC defaults.

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
- The CPAT annuity-due versus end-of-year CRF convention should be reconciled (Section 7).
- Body runs to about 6,000 words of prose (6,700 including tables) after the country runs were added and earlier sections trimmed.
