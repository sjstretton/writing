# 6.2 The CBAM Policy Tool

**Status (31 Oct 2026):** working paper v0.2 (about 5,200 words of body, 700-word executive summary) + Climate Fiscal Policy Brief No. 6.2 v1.0 (`1.Presentation/Brief-CBAMPolicyTool.qmd`, key CFPB62) + ten-slide deck. Peer-reviewed (`5.Notes/PeerReview-2026-10-31.md`) and every citation checked (`5.Notes/BibCheck-2026-10-31.md`). v0.1 files are in `8.PreviousVersions/`. Egypt application added 29 Oct 2026, after Stephen cleared tool country results for use as illustrative results; corrected 31 Oct 2026 (see below). Moved here from `6.Additional` (old number 4.3).

**Egypt corrections (31 Oct 2026).** The review found that the tool's Egypt workbook (v1.2) deducts the CO₂ bound in urea, which the CBAM rules count as emitted (Impl. Reg. 2025/2547, Annex II B.8.2), counts only half the ammonia in ammonium nitrate, and uses its own EU export volumes, which differ widely from Eurostat. `2.Source/egypt_example.py` applies the corrections and uses Eurostat volumes; the headline moves from €595m/€177m (default/verified) to €793m/€480m a year at 2025 volumes (€982m/€445m at 2024 volumes). The corrections should be carried into the tool itself (Egypt_CBAM_EF v1.3), with its steel factors reconciled (merchant DRI 1.38 t/t vs DRI-EAF steel 0.73 t/t; per tonne of crude steel, not of product).

**What the paper does.** (v0.1 description; numbers updated in v0.2.) Describes the CBAM Policy Tool (part of the Climate Fiscal AI Tools): what it computes (embedded emissions by component, the gap to EU default values, the CBAM charge per tonne and in total year by year, the capture price, the effect of a domestic carbon price split into abatement and credit), its method in five equations, its public data sources, a worked example with public data only: three Turkish exports to the EU (CN 7208, 7214 20 00, 7601), Commission default values and Eurostat 2025 trade; and a country application (section 7): the tool's Egypt emission factors for seven products against the Commission's default values, with the full-phase-in charge at €80 (about €595 million a year at default values, €177 million at the tool's estimates, 2024 volumes). Links to papers 1.1 (two-track architecture), 1.4 (carbon price recognition and routing), 6.1 (TECP) and 5.4 (elasticities).

## Files

| File | What it is |
|---|---|
| `CBAMPolicyTool.qmd` | Working paper master (v0.2) |
| `CBAMPolicyTool.bib` | References, verified 31 Oct 2026 (EU law entries kept identical to paper 1.4's) |
| `CBAMPolicyTool.docx` | Rendered with pandoc and the site's `quarto-xref.lua` and `web-links.lua` filters |
| `1.Presentation/Brief-CBAMPolicyTool.qmd/.bib/.docx` | Policy brief master (v1.0); its bib is copied from the working paper's |
| `1.Presentation/slides.json`, `Slides-CBAMPolicyTool.pptx` | Ten-slide deck (make_deck.py) |
| `1.Presentation/figures/make_figures.py` | Reruns both scripts, copies Figure 1, draws the Egypt chart |
| `2.Source/cbam_example.py` | Worked example: charge per tonne 2026–2034, aggregates, figure. `--refetch` re-queries Eurostat |
| `2.Source/data/default_values_turkiye.csv` | Default values used (from the Commission's "DVs as adopted" workbook, 4 Feb 2026) |
| `2.Source/data/eurostat_eu_imports_from_tr.csv` | EU imports from Türkiye, 2024–2025, Eurostat Comext DS-045409 (retrieved 29 Oct 2026) |
| `2.Source/table_example.csv`, `table_aggregate.csv`, `figures/fig1_charge_path.png` | Outputs |
| `2.Source/egypt_example.py`, `table_egypt.csv`, `table_egypt_sensitivity.csv`, `data/eurostat_eu_imports_from_eg.csv` | Egypt application (Tables 4–6): tool factors from `Egypt_CBAM_EF_v1.2.xlsx` with the two CBAM-rule corrections, Commission defaults, Eurostat volumes (`--refetch` re-queries) |
| `CBAM_policy_dashboard_v1.0_guide.qmd/.docx`, `Egypt_CBAM_EF_v1.1_guide.qmd/.docx` | Source guides (method used; the guides themselves are not published) |
| `CBAM_dash_v1.6.xlsx`, `cbam_data.xlsx`, `cbam_global_data.xlsx`, `Egypt_CBAM_EF_v1.2.xlsx`, `Egypt_CBAM_EmissionsFactors_v1.1.xlsx` | Source workbooks (Egypt EF v1.2 used; see below) |
| `DVs as adopted_v20260204_.xlsx` | The Commission's public default-value workbook |

Run: `cd 2.Source && python3 cbam_example.py && python3 egypt_example.py`. Render: `python3 xref.py CBAMPolicyTool.qmd r.md` (scratchpad cross-reference resolver), then `pandoc r.md --citeproc --number-sections --bibliography=CBAMPolicyTool.bib --csl=chicago.csl -o CBAMPolicyTool.docx`.

## Sources used

- Folder guides: `CBAM_policy_dashboard_v1.0_guide.qmd` (scope, sheets, formula, data sources) and `Egypt_CBAM_EF_v1.1_guide.qmd` (emission-factor method only).
- `climate-fiscal-ai-tools/CBAMPolicyTool`: `CBAM_Policy_Tool_Guide_v3.0.docx`, `Egypt/Egypt_Methodology_v3.0.docx` (equations only: output, fuel and process responses; the abatement-versus-credit split).
- Public: Regulation (EU) 2023/956 and 2025/2083; Implementing Regulations 2025/2547, 2025/2548, 2025/2620, 2025/2621; the Commission's default-value workbook; Eurostat Comext; IPCC 2006 Guidelines.

## Now used (cleared by Stephen, 29 Oct 2026, as illustrative tool results)

- **Egypt emission factors** (section 8, Table 4): `Egypt_CBAM_EF_v1.2.xlsx`, sheet EF Section C (CBAM-equivalent intensity by CN line; the tool's line volumes are used only as route-mix weights; EU volumes now from Eurostat), sheet Quality_Assurance (v1.1 to v1.2 corrections, ammonium nitrate N₂O range, aluminum PFCs). Cited as @CBAMToolEgypt2026 ("CBAM Policy Tool 2026"). Defaults compared are the Commission's (`DVs as adopted_v20260204_.xlsx`, Egypt sheet; "other countries" sheet for carbon steel, where Egypt has no value), not the tool's own reference defaults, which differ (e.g. the tool uses 1.82 for gas-based steel and 1.58 for clinker).

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

From the folder each master is in (as for every series paper):

```bash
F="/home/user/writing/H Writing Instructions/Scripts/Website"; CSL="/home/user/writing/E Website/chicago-author-date.csl"
pandoc CBAMPolicyTool.qmd -f markdown --lua-filter="$F/quarto-xref.lua" --lua-filter="$F/web-links.lua" --citeproc --bibliography=CBAMPolicyTool.bib --csl="$CSL" -o CBAMPolicyTool.docx
```

Same for `1.Presentation/Brief-CBAMPolicyTool.qmd`. Deck: `python3 "H Writing Instructions/Writing Standards/templates/make_deck.py" slides.json Slides-CBAMPolicyTool.pptx`. (`2.Source/xref.py` was the v0.1 route and is no longer needed.)
