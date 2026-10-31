# 6.2 The CBAM Policy Tool

**Status:** working paper, version 0.1 (29 October 2026), first full draft for Stephen's review. About 5,450 words of body. Egypt application added 29 Oct 2026, after Stephen cleared tool country results for use as illustrative results. Moved here from `6.Additional` (old number 4.3).

**What the paper does.** Describes the CBAM Policy Tool (part of the Climate Fiscal AI Tools): what it computes (embedded emissions by component, the gap to EU default values, the CBAM charge per tonne and in total year by year, the capture price, the effect of a domestic carbon price split into abatement and credit), its method in five equations, its public data sources, a worked example with public data only: three Turkish exports to the EU (CN 7208, 7214 20 00, 7601), Commission default values and Eurostat 2025 trade; and a country application (section 7): the tool's Egypt emission factors for seven products against the Commission's default values, with the full-phase-in charge at €80 (about €595 million a year at default values, €177 million at the tool's estimates, 2024 volumes). Links to papers 1.1 (two-track architecture), 1.3 (carbon price recognition), 6.1 (TECP) and 5.4 (elasticities).

## Files

| File | What it is |
|---|---|
| `CBAMPolicyTool.qmd` | Master (v0.1) |
| `CBAMPolicyTool.bib` | References (EU law entries copied from paper 1.4's verified bib) |
| `CBAMPolicyTool.docx` | Rendered with pandoc after resolving cross-references (as in 5.4) |
| `2.Source/cbam_example.py` | Worked example: charge per tonne 2026–2034, aggregates, figure. `--refetch` re-queries Eurostat |
| `2.Source/data/default_values_turkiye.csv` | Default values used (from the Commission's "DVs as adopted" workbook, 4 Feb 2026) |
| `2.Source/data/eurostat_eu_imports_from_tr.csv` | EU imports from Türkiye, 2024–2025, Eurostat Comext DS-045409 (retrieved 29 Oct 2026) |
| `2.Source/table_example.csv`, `table_aggregate.csv`, `figures/fig1_charge_path.png` | Outputs |
| `2.Source/egypt_example.py`, `2.Source/table_egypt.csv` | Egypt application (Table 4): reads `Egypt_CBAM_EF_v1.2.xlsx` and the Commission workbook directly |
| `CBAM_policy_dashboard_v1.0_guide.qmd/.docx`, `Egypt_CBAM_EF_v1.1_guide.qmd/.docx` | Source guides (method used; the guides themselves are not published) |
| `CBAM_dash_v1.6.xlsx`, `cbam_data.xlsx`, `cbam_global_data.xlsx`, `Egypt_CBAM_EF_v1.2.xlsx`, `Egypt_CBAM_EmissionsFactors_v1.1.xlsx` | Source workbooks (Egypt EF v1.2 used; see below) |
| `DVs as adopted_v20260204_.xlsx` | The Commission's public default-value workbook |

Run: `cd 2.Source && python3 cbam_example.py && python3 egypt_example.py`. Render: `python3 xref.py CBAMPolicyTool.qmd r.md` (scratchpad cross-reference resolver), then `pandoc r.md --citeproc --number-sections --bibliography=CBAMPolicyTool.bib --csl=chicago.csl -o CBAMPolicyTool.docx`.

## Sources used

- Folder guides: `CBAM_policy_dashboard_v1.0_guide.qmd` (scope, sheets, formula, data sources) and `Egypt_CBAM_EF_v1.1_guide.qmd` (emission-factor method only).
- `climate-fiscal-ai-tools/CBAMPolicyTool`: `CBAM_Policy_Tool_Guide_v3.0.docx`, `Egypt/Egypt_Methodology_v3.0.docx` (equations only: output, fuel and process responses; the abatement-versus-credit split).
- Public: Regulation (EU) 2023/956 and 2025/2083; Implementing Regulations 2025/2547, 2025/2548, 2025/2620, 2025/2621; the Commission's default-value workbook; Eurostat Comext; IPCC 2006 Guidelines.

## Now used (cleared by Stephen, 29 Oct 2026, as illustrative tool results)

- **Egypt emission factors and EU export volumes** (section 7, Table 4): `Egypt_CBAM_EF_v1.2.xlsx`, sheet EF Section C (CBAM-equivalent intensity and 2024 EU exports by CN line), sheet Quality_Assurance (v1.1 to v1.2 corrections, ammonium nitrate N₂O range, aluminum PFCs). Cited as @CBAMToolEgypt2026 ("CBAM Policy Tool 2026"). Defaults compared are the Commission's (`DVs as adopted_v20260204_.xlsx`, Egypt sheet; "other countries" sheet for carbon steel, where Egypt has no value), not the tool's own reference defaults, which differ (e.g. the tool uses 1.82 for gas-based steel and 1.58 for clinker).

## Still held back

- **Egypt policy-scenario results** (scenarios 1A–3C: revenue, emission cuts, CBAM-obligation cuts, deaths avoided) in `climate-fiscal-ai-tools/CBAMPolicyTool/Egypt/EgyptResultsInitial_UpdatedResults_tracked_v3.0.docx` and `Egypt_CBAM_results_v3.0.xlsx`: the results note is a tracked-changes draft prepared for World Bank country work, so treated as draft-for-comment.
- **Dashboard outputs**: the five-country results (capture prices, CBAM gross, total revenue) and the model-versus-default intensity tables in the dashboard guide and workbooks (World Bank team outputs; not needed for the paper).
- Plant and company names from the Egypt workbook are not used.
- The tool's own reference values for default values and benchmarks were **not** used as data (several look approximate); both examples use the Commission's workbook and Implementing Regulation 2025/2620 directly.

## Checked 30 Oct 2026 (no unverified markers remain)

- CBAM benchmarks: read in Implementing Regulation (EU) 2025/2620, Annex point 5.3, Column B (full text from the Publications Office cellar, CELEX 32025R2620): CN 7208 route (C) 1.370, CN 7214 20 00 route (C) **1.364** (the tool had 1.370; `cbam_example.py` now uses per-product values, which moves the rebar 2026 and 2030 rows by €1 at most), CN 7601 route (K) 1.423.
- Free-allocation schedule (97.5% in 2026 … 14% in 2033, zero from 2034): read in Directive (EU) 2023/959, Art. 1, which inserted Art. 10a(1a) into the ETS Directive (CELEX 32023L0959).
- Implementing Regulation (EU) 2026/1740 of 20 July 2026 (OJ 31.7.2026, applies from 1 Jan 2026): read; it leaves the Türkiye values used unchanged.
- COM(2026) 616 final of 17 July 2026: read; it would set the CBAM factor at 91.5% in 2028 … 27% in 2033 and 15% in 2034–2037, zero from 2038. Cited as a proposal only.
- Still open (stated in the paper, not a marker): the conversion of a carbon price paid into certificates is in a draft implementing act; the example deducts the price paid per tonne.

## Rendering

Plain pandoc cannot resolve Quarto cross-references. Render with:

```bash
python3 2.Source/xref.py <Name>.qmd /tmp/x.qmd   # numbers sections, tables, figures, equations
pandoc /tmp/x.qmd -f markdown --citeproc --bibliography=<Name>.bib --csl=chicago-author-date.csl --resource-path=. -o <Name>.docx
```

Check the script header for its exact usage.
