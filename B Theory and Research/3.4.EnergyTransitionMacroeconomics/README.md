# 3.4 The Energy Transition Swaps a Fuel Bill for a Capital Bill

**Status:** work in progress, 20 November 2026 (Theory and Research Note No. 3.4, v0.1 not yet complete). New research awaiting Stephen's review; not on the website; no brief or deck. Joins `C Policy and FInance/3.FinanceAndRisk/` once reviewed.

Drafted so far: the Egypt estimates (script, output, three figures), the Egypt section, the institutions section and the method appendix. Still to come: the stylized-facts section and Appendix A (each fact with its evidence and a verdict), the abstract and key messages, the bibliography check and the rendered Word file. Every gap in the master is marked `[VERIFY: pending ...]`.

## Files

| File | What |
|---|---|
| `EnergyTransitionMacroeconomics.qmd` | Master (in progress) |
| `EnergyTransitionMacroeconomics.bib` | References (entries reused from papers 1.1, 1.2, 3.1 and 4.1 were checked there) |
| `2.Source/egypt_estimates.py`, `egypt_estimates_output.txt`, `egypt_*.csv` | The Egypt estimates: a rapid transition by sector at the local (10.3 percent) and de-risked (6 percent) cost of capital. Reads the investment model and macro models of the Climate Fiscal AI Tools read-only (`--tools` path); public data only |
| `2.Source/make_figures.py`, `2.Source/figures/` | Three figures, made from the CSVs |

## Egypt results: status and sources

Illustrative tool results on public data (IMF fossil fuel subsidies data 2024, Ember, IMF WEO, IRENA). Not official estimates. Not yet cleared by Stephen for publication. No World Bank internal material is used, and no result from the Climate Policy Assessment Tool's proprietary data.

One change to the tool's default: capital is priced at world prices (the tool scales it by the local price level, 0.41 for Egypt), following note 6.8 v0.3. The tool default is reported as a sensitivity; it changes the sign of the total at the local cost of capital.
