# 7.2 A Global Fiscal Indicators Dashboard for Climate-Fiscal Analysis

**Status:** working paper, version 0.1, 29 October 2026 (first draft, for Stephen's peer review). Medium form, about 4,000 words of body. Companion paper to the Climate Fiscal AI Tools (private repository), dashboard version 1.3 (`TaxMacroFiscalDashboard/Global_fiscal_indicators_v1.3.xlsx`).

## Files

| File | What it is |
|---|---|
| `FiscalIndicatorsDashboard.qmd` | Master, v0.1 |
| `FiscalIndicatorsDashboard.bib` | References and dataset citations (URLs from the build's `config/sources.csv`; DOIs checked against Crossref) |
| `FiscalIndicatorsDashboard.docx` | Rendered with pandoc and the Chicago author-date CSL |
| `2.Source/illustrative_comparison.py` | Reproduces Table 2 (Colombia, Indonesia, Morocco, South Africa) and the 1–10 scores from the built panel (`PANEL` path into the private repository; the panel holds only public data). Output in `illustrative_comparison_output.txt` |

## Sources used (all in `climate-fiscal-ai-tools/TaxMacroFiscalDashboard/`)

- `README.md`, `VersionNotes.md`, `build/README.md`.
- `build/config/indicators.csv` and `sources.csv` (the 80 indicators, 12 blocks and their datasets: verified against what the build reads).
- `build/scripts/build_global_indicators.py` (stages, derived indicators, year handling) and `build_dashboard.py` (README sheet text, 5th–95th percentile scoring, thresholds, "do not build an index").
- `TaxMacroFiscalDashboard-user-guide.pptx` (reading order, five-step routine for adding a source with an AI coding assistant). The v1.0 deck was not needed.

## Verification of datasets the brief listed

Used: IMF WEO; IMF WoRLD 2026; IMF fossil fuel subsidies (2024 data); World Bank WDI, IDS, BOOST, PPI, RISE, CPIA; PEFA 2016; Ember; IRENA; Steffen et al. (2025); IEA Cost of Capital Observatory; OECD climate-related development finance (recipient); Power Sector Reform Tracker; IMF ICSD; Global Findex; Kose et al. fiscal space database.
Not used: IMF GFS and OECD Revenue Statistics (WoRLD is the revenue source); UNU-WIDER GRD (downloaded, held in `raw_data_not_used/`); World Bank Carbon Pricing Dashboard and OECD effective carbon rates (no carbon pricing data block yet; the paper names this as the main gap).

## Country profile: checked 29 Oct 2026, nothing added

Stephen cleared tool country results for use as illustrative results on 29 Oct 2026. The tool's only other country profile is the user guide's Kenya worked example (block verdicts: fiscal space 3.7, delivery 7.1, cost of capital 3.2, financing and risk 4.9, and the three context blocks). It was not added: the paper's four-country comparison (Table 2) is already built from the tool's own panel and is reproducible from `2.Source/`, whereas the guide's block scores cannot be traced to a stated panel version, and Kenya is now the country run in paper 6.5.

## Still held back

- Every Appendix D value (model output from the scenario tool; Kenya's is reported in paper 6.5 instead).
- The `upgrades/` folder: CBAM dashboard and the Egypt CBAM workbooks (Egypt emission factors are now used in paper 6.2, not here), the political economy note, and the World Bank Climate Fiscal Risk Dashboard v1.5 with its exemplars and statistical annex (internal-looking World Bank compilation). The paper says only that part of Appendix C and Appendix E are read from "a World Bank climate fiscal risk compilation" whose underlying series are public, and recommends reading those series directly in a public release.
- The private GitHub address in the user guide.

## Note for the editor

The illustrative values are public data as compiled by the pipeline; they were not re-checked against each publisher's current release. Before publication, spot-check Table 2 against the WEO, WoRLD and IMF subsidy releases (and consider dropping the excise-share row, whose WoRLD definition should be confirmed).
