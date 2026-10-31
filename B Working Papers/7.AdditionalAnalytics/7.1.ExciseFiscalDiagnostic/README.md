# 5.1 The Excise-Fiscal Diagnostic: Reading an Excise System Against Its Externalities

**Status:** working paper, version 0.3, 30 October 2026 (draft for Stephen's peer review). Medium form, about 6,050 words of body. Version 0.3 adds Section 7, applications to Sierra Leone and Liberia, after Stephen cleared the diagnostic's own results for use (30 Oct 2026). Companion paper to the Climate Fiscal AI Tools (private repository).

## Files

| File | What it is |
|---|---|
| `ExciseFiscalDiagnostic.qmd` | Master, v0.3 |
| `ExciseFiscalDiagnostic.bib` | References (all checked against Crossref or the publisher's page) |
| `ExciseFiscalDiagnostic.docx` | Rendered with pandoc and the Chicago author-date CSL |
| `2.Source/stylized_example.py` | Computes every number in Section 6 (Country A, stylized); output in `stylized_example_output.txt` |
| `2.Source/country_metrics.py` | Extracts the Sierra Leone and Liberia figures in Section 7 (Table 5) from the diagnostic's cross-country workbook; output in `country_metrics_SLE_LBR.csv` |
| `8.PreviousVersions/ExciseFiscalDiagnostic-v0.1.qmd/.docx` | The 24,800-word three-part draft (May 2026) |
| `8.PreviousVersions/ExciseFiscalDiagnostic-v0.2.qmd/.docx` | Version 0.2 (29 Oct 2026), stylized example only |
| `1.Presentation/`, `3.BackgroundPapers/`, `9.Archive/` | Earlier briefing, deck, background notes and archive, unchanged |

## Sources used

- Previous master v0.1 (Parts A–C, especially A2–A3 measures, B1 key questions, B4–B5 data needs and valuation spine).
- `climate-fiscal-ai-tools/ExciseDiagnostic/`: `Excise_Diagnostic_WorkingPaper_v0_9.docx` (Part I method: seven questions, typology, three measures, conversion rules, four levels, whole and sectoral runs, data step, lessons); `README.txt`; `process_files/excise_diagnostic_process.md` (standard schedule v1.0, quality rules, data-quality scale, comparator rule, workbook layout). Cross-country workbook: structure, and (from v0.3) the Sierra Leone and Liberia results in Section 7.
- `3.BackgroundPapers/Background-PoliticalEconomyMetric.qmd` (six drivers, Section 8.3) and `Background-ExtenalityDiagnosticQuestions.qmd` (climate–health questions, Section 4.4).
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

## Changes from v0.1

Cut from 24,800 to about 5,500 words; one paper instead of a three-part report (Part C, the policy pathway, is reduced to Section 7.3); stylized Country A replaces the pilot countries; the corrective-benchmark arithmetic is now reproducible from `2.Source/`; unsourced defaults (VSL USD 4.7 million, carbon USD 75/t) replaced by sourced ones.

## Changes from v0.2 (30 Oct 2026)

New Section 7, "Two applications: Sierra Leone and Liberia" (Table 5), with the diagnostic's own results; abstract, introduction, roadmap and the peer-review paragraph in Section 8 updated to match; the public finance review sentence in Section 8.3 replaced by a generic one; stylized example and process text trimmed to keep the body near 6,000 words.
