# 4.5 The CBAM Policy Tool

**Status:** working paper, version 0.1 (29 October 2026), first full draft for Stephen's review. About 4,600 words of body. Moved here from `6.Additional` (old number 4.3).

**What the paper does.** Describes the CBAM Policy Tool (part of the Climate Fiscal AI Tools): what it computes (embedded emissions by component, the gap to EU default values, the CBAM charge per tonne and in total year by year, the capture price, the effect of a domestic carbon price split into abatement and credit), its method in five equations, its public data sources, and a worked example with public data only: three Turkish exports to the EU (CN 7208, 7214 20 00, 7601), Commission default values and Eurostat 2025 trade. Links to papers 1.1 (two-track architecture), 1.3 (carbon price recognition), 1.7 (TECP) and 4.4 (elasticities).

## Files

| File | What it is |
|---|---|
| `CBAMPolicyTool.qmd` | Master (v0.1) |
| `CBAMPolicyTool.bib` | References (EU law entries copied from paper 1.3's verified bib) |
| `CBAMPolicyTool.docx` | Rendered with pandoc after resolving cross-references (as in 4.4) |
| `2.Source/cbam_example.py` | Worked example: charge per tonne 2026–2034, aggregates, figure. `--refetch` re-queries Eurostat |
| `2.Source/data/default_values_turkiye.csv` | Default values used (from the Commission's "DVs as adopted" workbook, 4 Feb 2026) |
| `2.Source/data/eurostat_eu_imports_from_tr.csv` | EU imports from Türkiye, 2024–2025, Eurostat Comext DS-045409 (retrieved 29 Oct 2026) |
| `2.Source/table_example.csv`, `table_aggregate.csv`, `figures/fig1_charge_path.png` | Outputs |
| `CBAM_policy_dashboard_v1.0_guide.qmd/.docx`, `Egypt_CBAM_EF_v1.1_guide.qmd/.docx` | Source guides (World Bank team documents; not for publication) |
| `CBAM_dash_v1.6.xlsx`, `cbam_data.xlsx`, `cbam_global_data.xlsx`, `Egypt_CBAM_EF_v1.2.xlsx`, `Egypt_CBAM_EmissionsFactors_v1.1.xlsx` | Source workbooks (internal; see below) |
| `DVs as adopted_v20260204_.xlsx` | The Commission's public default-value workbook |

Run: `cd 2.Source && python3 cbam_example.py`.

## Sources used

- Folder guides: `CBAM_policy_dashboard_v1.0_guide.qmd` (scope, sheets, formula, data sources) and `Egypt_CBAM_EF_v1.1_guide.qmd` (emission-factor method only).
- `climate-fiscal-ai-tools/CBAMPolicyTool`: `CBAM_Policy_Tool_Guide_v3.0.docx`, `Egypt/Egypt_Methodology_v3.0.docx` (equations only: output, fuel and process responses; the abatement-versus-credit split).
- Public: Regulation (EU) 2023/956 and 2025/2083; Implementing Regulations 2025/2547, 2025/2548, 2025/2620, 2025/2621; the Commission's default-value workbook; Eurostat Comext; IPCC 2006 Guidelines.

## Held back for confidentiality

- **All Egypt numbers**: the Egypt emission-factor matrix (product and CN-line factors, gaps to defaults, volumes, quality-assurance results) and the Egypt policy results (scenarios 1A–3C: emission cuts, revenue, border-charge changes, deaths avoided). The paper describes the Egypt emission-factor application in method terms only.
- **Dashboard outputs**: the five-country results (capture prices, CBAM gross, total revenue) and the model-versus-default intensity tables in the dashboard guide and workbooks. The countries covered are not named in the paper.
- The tool's own reference values for default values and benchmarks were **not** used as data (several look approximate); the worked example uses the Commission's workbook directly, except the two benchmarks below.

## Open items ([VERIFY] in the paper)

- CBAM benchmarks for CN 7208, 7214 20 00 (route C, 1.370) and 7601 (route K, 1.423) are as entered in the tool; check against Implementing Regulation 2025/2620. They affect 2026–2033 results only.
- Free-allocation schedule (97.5% in 2026 … 14% in 2033, zero from 2034) confirmed only from secondary sources; check the consolidated ETS Directive, Art. 10a(1a).
- Implementing Regulation (EU) 2026/1740 (correction of default values) and the proposal COM(2026) 616 (slower phase-out) are reported but not read.
- The conversion of a carbon price paid into certificates is in a draft implementing act; the example deducts the price paid per tonne.
