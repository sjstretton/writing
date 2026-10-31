# 7.1 The Excise-Fiscal Diagnostic: Reading an Excise System Against Its Externalities

**Status (31 Oct 2026):** working paper v0.4 (peer-reviewed, references re-checked; about 7,900 words of body plus a 710-word executive summary) and a new policy brief v1.0, Climate Fiscal Policy Brief No. 7.1, "Read the Excise Schedule Whole, Against the Damage It Should Price" (key `CFPB71`; working paper key `StrettonWP71`). Ten-slide deck on the new builder. Companion paper to the Climate Fiscal AI Tools (private repository).

## Files

| File | What it is |
|---|---|
| `ExciseFiscalDiagnostic.qmd` | Working paper master, v0.4 |
| `ExciseFiscalDiagnostic.bib` | References, each verified 31 Oct 2026 (see `5.Notes/BibCheck-2026-10-31.md`) |
| `ExciseFiscalDiagnostic.docx` | Rendered with pandoc, the cross-reference and link filters and the Chicago author-date CSL |
| `1.Presentation/Brief-ExciseFiscalDiagnostic.qmd/.bib/.docx` | Policy brief master, v1.0, and its rendered Word file |
| `1.Presentation/slides.json`, `Slides-ExciseFiscalDiagnostic.pptx` | Ten-slide deck, built with `H Writing Instructions/Writing Standards/templates/make_deck.py` |
| `1.Presentation/figures/make_figures.py` | Makes `fig_corrective.png` and `fig_countries.png` for the paper, brief and deck |
| `2.Source/stylized_example.py` | Computes every number in the stylized example (Country A); output in `stylized_example_output.txt` |
| `2.Source/country_metrics.py` | Extracts the Sierra Leone and Liberia figures from the diagnostic's cross-country workbook; output in `country_metrics_SLE_LBR.csv` |
| `2.Source/africa_excise_benchmark.py` | Computes the African excise benchmark from OECD/AUC/ATAF *Revenue Statistics in Africa 2025*; output in `africa_excise_benchmark.csv` |
| `5.Notes/PeerReview-2026-10-31.md`, `BibCheck-2026-10-31.md` | Peer review of v0.3 and the reference check |
| `8.PreviousVersions/` | v0.1–v0.3 of the working paper, the v0.3 deck and figure scripts, and the superseded V06 briefing and "Proposal" deck (internal; not used, see below) |
| `3.RelatedPiecesAndLinks/`, `9.Archive/` | Background notes and archive, unchanged |

## Sources used

- Previous master v0.1 (Parts A–C, especially A2–A3 measures, B1 key questions, B4–B5 data needs and valuation spine).
- `climate-fiscal-ai-tools/ExciseDiagnostic/`: `Excise_Diagnostic_WorkingPaper_v0_9.docx` (Part I method: seven questions, typology, three measures, conversion rules, four levels, whole and sectoral runs, data step, lessons); `README.txt`; `process_files/excise_diagnostic_process.md` (standard schedule v1.0, quality rules, data-quality scale, comparator rule, workbook layout). Cross-country workbook: structure, and (from v0.3) the Sierra Leone and Liberia results in Section 7.
- `3.RelatedPiecesAndLinks/Background-ExtenalityDiagnosticQuestions.qmd` (climate–health questions). From v0.4, `Background-PoliticalEconomyMetric.qmd` is no longer used: it is headed "World Bank · Draft for discussion".
- Public references in the `.bib`.

## Now used (cleared by Stephen, 30 Oct 2026, as illustrative results from the diagnostic)

- **Sierra Leone and Liberia** (Section 7, Table 5): only the diagnostic's own measures and results, taken from `climate-fiscal-ai-tools/ExciseDiagnostic/Excise_Diagnostic_CrossCountry.xlsx` (sheets Country_Metrics, Std_Schedule, Parameters) by `2.Source/country_metrics.py`. Cited as @ExciseDiagnostic2026 ("Excise-Fiscal Diagnostic 2026"). Sierra Leone: Finance Act 2026, cut-off 27 April 2026. Liberia: Revenue Code as amended through December 2025, cut-off 29 September 2026. Peer-review counts (49 entries each) from the same sheet.
- The comparison of fuel rates with the spine's carbon component (USD 0.12/0.13 per liter at USD 50/tCO₂) is the author's calculation, labelled as such.

## Still held back

- Narrative text of the country documents: `Excise_Diagnostic_WorkingPaper_v0_9.docx` and `Example_SLE_Excise_Diagnostic.docx` ("Draft for discussion") and `Liberia_Excise_Diagnostic_v0.3.docx` ("Not for citation"). No sentence, quotation or interpretation is taken from them; only the workbook's measures and results.
- Uganda (Sierra Leone's comparator in the pilot): its run was not peer reviewed, so it is not used.
- Public Finance Review material of any kind: the PFR topic mapping in v0.9 and the PFR visualization tool. The paper no longer mentions public finance reviews.
- The v0.1 Tier 2 example's numbers (internally inconsistent and unsourced) and the v0.1 candidate-country lists.
- Internal platform details (the Bank's AI platform, account tiers) and the original prompts.
- The V06 briefing (`Briefing-ExciseExternalitiesPathwaysSummaryV06`) and the "Proposal — Draft for discussion" deck (`Pres-ExciseFiscalReportsProposalV06.pptx`, "World Bank · Fiscal Policy Unit"): internal proposal material with Uganda results, the v0.1 Tier 2 numbers and internal arrangements. Moved to `8.PreviousVersions/` on 31 Oct 2026; superseded by the brief; not used.
- The diagnostic's unsourced reference values ("African average 2.4", "OECD" fuel and alcohol ranges): replaced by verified public figures or dropped in v0.4.

## Changes from v0.1

Cut from 24,800 to about 5,500 words; one paper instead of a three-part report (Part C, the policy pathway, is reduced to Section 7.3); stylized Country A replaces the pilot countries; the corrective-benchmark arithmetic is now reproducible from `2.Source/`; unsourced defaults (VSL USD 4.7 million, carbon USD 75/t) replaced by sourced ones.

## Changes from v0.2 (30 Oct 2026)

New Section 7, "Two applications: Sierra Leone and Liberia" (Table 5), with the diagnostic's own results; abstract, introduction, roadmap and the peer-review paragraph in Section 8 updated to match; the public finance review sentence in Section 8.3 replaced by a generic one; stylized example and process text trimmed to keep the body near 6,000 words.

## Changes from v0.3 (31 Oct 2026)

Peer review and reference check first (`5.Notes/`). Executive summary added as chapter 1; section ids for every section. African benchmark replaced (OECD 2023 mean 1.32 percent of GDP, not 2.4); Liberia compared on a consistent definition (1.25 percent with fuel and road levies); Sierra Leone's reported collections set beside the OECD series (0.57 percent in 2023), reconciliation stated as open. Carbon value described as a policy floor, with a USD 185/t social-cost case; VSL transfer stated against Robinson et al. (2019) correctly; "largest unpriced externality" replaced by a decomposition of the corrective rate (two-thirds local); petrol CO2 factor recomputed from IPCC defaults (2.29 kg/l; carbon component USD 0.11). New section on the strongest objections (corrective versus optimal tax; AI error rate; standardization). Material from a World Bank draft-for-discussion removed. Title unchanged.
