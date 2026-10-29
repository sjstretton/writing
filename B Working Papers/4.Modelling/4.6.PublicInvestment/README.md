# 4.6 Public Investment in CPAT: Investment Needs and the Efficiency of Public Spending

**Status:** first full draft, version 0.1 (29 October 2026). One medium-length working paper (about 6,000 words of body), companion to the CPAT-AI repository. Awaiting Stephen's peer review. Series plan: `../SeriesArchitecture.md`.

**Question.** How can CPAT be extended to estimate climate investment needs by country and sector, price them at the cost of capital countries face, and test whether public money should pay for them?

**Answer.** Investment = physical change × unit capital cost × local price level, annualized with a capital recovery factor and read through three lenses (market WACC; 6 percent social rate; 6 percent plus co-benefits and carbon). Public spending is scored by the marginal value of public funds against the marginal cost of public funds (default 1.2), after additionality, delivery haircuts, a fiscal ledger, capex/opex on one footing and six financing routes. Propositions: break-even cost of capital (12.6 percent for a stylized asset; CPAT's LMIC default sits on it); the rule nests the World Bank ENPV test and prices revenue returns at λ − 1; tenor is not price; a PPA priced above the government's rate is debt in disguise.

## Files

| File | What |
|---|---|
| `PublicInvestment.qmd` / `.docx` / `.bib` | Working paper master (version 0.1), rendered with pandoc |
| `2.Source/investment_lenses.py` | Table 1 (three cost-of-capital lenses, break-even WACC, CPAT default WACCs) |
| `2.Source/sids_worked_example.py` | Table 2 (stylized small-island solar plant, five financing routes); writes the two CSVs beside it; asserts the accounting identities |
| `2.Source/sids_worked_example_results.csv`, `..._sensitivity.csv` | Script output |
| `3.RelatedPiecesAndLinks/` | Source notes (see below) |

Regenerate: `cd 2.Source && python3 investment_lenses.py && python3 -I sids_worked_example.py`, then from the folder root `pandoc PublicInvestment.qmd -f markdown --citeproc --bibliography=PublicInvestment.bib --csl=<chicago-author-date.csl> --resource-path=. -o PublicInvestment.docx`.

## Sources used

- `3.RelatedPiecesAndLinks/CDPM-GlobalInvestmentNeeds-SISEPUEDE.docx`: method (equations 1–7), the four definitional choices, three lenses. Global totals re-sourced to the public IHLEG third report.
- `3.RelatedPiecesAndLinks/CDPM-PublicSpendingEfficiencyAndCBA.docx` and the markdown folder: design brief, MCPF/MVPF theory, frontiers and cross-sector CBA, capex/opex/PPP/PPA notes, SIDS worked example (script copied unchanged to `2.Source/`).
- `climate-fiscal-ai-tools/MacFiscEnergyScenarioProto/InvestmentNeeds` (README): method only (allocation, lenses, PIMA haircut). No outputs used.
- CPAT public documentation (`cpat_ai/docs/CPAT_full_documentation_qmd/03_Mitigation.qmd`): power investment logit, income-group WACC defaults.

## Held back for confidentiality

- No country results from the private repository, World Bank program work or the SISEPUEDE country runs (the Uganda run results, the St Lucia/Kenya pilots and the Egypt CPAT figures in the source notes are not used).
- Files named `internal_*` (internal CDPM and macro tool, NMIM, internal macro-fiscal tool) were used for general design logic only; the paper names no internal tool, contract, team or partnership terms. The investment-needs model's internal name (NMIM) and the PSV module/bridge file names are not used.
- The renaming of SISEPUEDE inside the World Bank is not mentioned; the paper uses the public name.

## Open items for review

- The stylized savings rate (b = 0.133 per dollar a year) is calibrated to give a benefit-cost ratio of 1.70 at 6 percent, as in the source note's reading of the SISEPUEDE LAC results; check against Kalra et al. (2023) before outside use.
- Worked-example inputs are stylized (island premium on capex, battery cost, 8 percent sovereign rate, concessional terms). The IPCC diesel emission factor and the 5 percent PV-of-debt rate were not verified in the source notes.
- The CPAT annuity-due versus end-of-year CRF convention should be reconciled (Section 6).
- Body runs to about 6,100 words including tables; trim Section 4.3 if a shorter version is wanted.
