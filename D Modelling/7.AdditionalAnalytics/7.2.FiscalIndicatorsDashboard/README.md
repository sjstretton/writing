# 7.2 A Global Fiscal Indicators Dashboard for Climate-Fiscal Analysis

**Status (31 Oct 2026):** working paper v0.2 (about 6,100 words of body plus a 680-word executive summary) and policy brief v1.0 (Climate Fiscal Policy Brief No. 7.2, about 1,900 words), both written after the peer review in `5.Notes/PeerReview-2026-10-31.md`; every reference checked (`5.Notes/BibCheck-2026-10-31.md`); 10-slide deck on the new builder. Subtitle changed in v0.2 (title unchanged). v0.1 (29 Oct 2026) and the old deck are in `8.PreviousVersions/`. Companion paper to the Climate Fiscal AI Tools (private repository), dashboard version 1.3 (`TaxMacroFiscalDashboard/Global_fiscal_indicators_v1.3.xlsx`).

## Files

| File | What it is |
|---|---|
| `FiscalIndicatorsDashboard.qmd` | Working paper master, v0.2 |
| `FiscalIndicatorsDashboard.bib` | References and dataset citations, each with a `note` recording what was checked on 31 Oct 2026 |
| `FiscalIndicatorsDashboard.docx` | Rendered with pandoc (quarto-xref and web-links filters, Chicago author-date CSL) |
| `1.Presentation/Brief-FiscalIndicatorsDashboard.qmd`, `.bib`, `.docx` | Policy brief master, v1.0 (key CFPB72), its bib (copied from the working paper's) and Word render |
| `1.Presentation/slides.json`, `Slides-FiscalIndicatorsDashboard.pptx` | 10-slide deck, built with `H Writing Instructions/Writing Standards/templates/make_deck.py` |
| `1.Presentation/figures/make_figures.py` | Makes `fig_profiles.png` (Figure 1 of both forms) and `fig_renewables.png` (working paper Figure 2) from the papers' numbers |
| `2.Source/illustrative_comparison.py` | Reproduces Table 2 and the 1–10 scores from the built panel (`PANEL` path into the private repository; the panel holds only public data). Output in `illustrative_comparison_output.txt` (v0.1 run; prints one decimal, so the table's gasoline prices are not visible in it; the script now prints two) |
| `2.Source/check_public_sources.py` | Rechecks Table 2 against the publishers' public releases (IMF DataMapper, IMF WoRLD API, Ember). Output in `check_public_sources_output.txt` |
| `5.Notes/` | Peer review and reference check, 31 Oct 2026 |

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

Table 2 was spot-checked against the WEO/Fiscal Monitor, WoRLD, the IMF's 2025 subsidy update and Ember on 31 Oct 2026 (`2.Source/check_public_sources.py`). Tax, net interest over revenue and the excise share reproduce exactly; the excise share is excises over WoRLD total revenue, so v0.2 adds excise revenue as a share of GDP. Findings for the tool's next version (not changed here): rename "interest-to-revenue" to net interest and keep net creditors; add excise revenue as a share of GDP; read the renewable share from Ember (the panel's CPAT-based shares are 5–19 points off); state that subsidy shares use WEO GDP; check why the panel holds subsidy values for 185 economies when the IMF's 2025 update covers 170.
