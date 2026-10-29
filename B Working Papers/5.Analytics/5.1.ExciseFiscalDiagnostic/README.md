# 5.1 The Excise-Fiscal Diagnostic: Reading an Excise System Against Its Externalities

**Status:** working paper, version 0.2, 29 October 2026 (draft for Stephen's peer review). Medium form, about 5,500 words of body. Companion paper to the Climate Fiscal AI Tools (private repository).

## Files

| File | What it is |
|---|---|
| `ExciseFiscalDiagnostic.qmd` | Master, v0.2 |
| `ExciseFiscalDiagnostic.bib` | References (all checked against Crossref or the publisher's page) |
| `ExciseFiscalDiagnostic.docx` | Rendered with pandoc and the Chicago author-date CSL |
| `2.Source/stylized_example.py` | Computes every number in Section 6 (Country A, stylized); output in `stylized_example_output.txt` |
| `8.PreviousVersions/ExciseFiscalDiagnostic-v0.1.qmd/.docx` | The 24,800-word three-part draft (May 2026) this version replaces |
| `1.Presentation/`, `3.BackgroundPapers/`, `9.Archive/` | Earlier briefing, deck, background notes and archive, unchanged |

## Sources used

- Previous master v0.1 (Parts A–C, especially A2–A3 measures, B1 key questions, B4–B5 data needs and valuation spine).
- `climate-fiscal-ai-tools/ExciseDiagnostic/`: `Excise_Diagnostic_WorkingPaper_v0_9.docx` (Part I method: seven questions, typology, three measures, conversion rules, four levels, whole and sectoral runs, data step, lessons); `README.txt`; `process_files/excise_diagnostic_process.md` (standard schedule v1.0, quality rules, data-quality scale, comparator rule, workbook layout). Cross-country workbook used for structure only.
- `3.BackgroundPapers/Background-PoliticalEconomyMetric.qmd` (six drivers, Section 7.3) and `Background-ExtenalityDiagnosticQuestions.qmd` (climate–health questions, Section 4.4).
- Public references in the `.bib`.

## Country application: checked 29 Oct 2026, still held back

Stephen cleared tool country results for use as illustrative results on 29 Oct 2026, except material marked "Confidential", "internal", "not for circulation" or draft-for-comment. Every source of a real country application for this tool carries such a marking, so the paper keeps stylized Country A:

- **Sierra Leone** (and Uganda as its benchmark): `climate-fiscal-ai-tools/ExciseDiagnostic/Excise_Diagnostic_WorkingPaper_v0_9.docx` (cover: "World Bank · Draft for discussion · v0.9 · September 2026"), `country_results/SierraLeone/Example_SLE_Excise_Diagnostic.docx` and `3.BackgroundPapers/SLE_Excise_Diagnostic.qmd` (both "Draft for discussion · July 2026"). The cross-country workbook carries no marking itself, but its Sources sheet takes every Sierra Leone and Uganda value from the v0.8 "draft for discussion" working paper (Uganda: "not peer reviewed").
- **Liberia**: `country_results/Liberia/Liberia_Excise_Diagnostic_v0.3.docx` ("Draft v0.3 for review. Not for citation.").
- **Indonesia**: no application exists. The v0.1 master (itself "Draft for discussion · May 2026") names Indonesia only as a candidate country and in a list of failed reforms.

**Decision for Stephen:** if "Draft for discussion" is not meant to count as draft-for-comment, the Sierra Leone application (Finance Act 2026 schedule, legal cut-off 27 April 2026, benchmarked against Uganda) is the one to add, from the cross-country workbook's Std_Schedule_Code and Country_Metrics sheets, cited as "Excise-Fiscal Diagnostic, Sierra Leone application, 2026". Its rates are public law, so a clean alternative is to re-run the diagnostic on the published Finance Act.

## Still held back

- All country results from the pilots (Sierra Leone, Uganda, Liberia), for the reason above. The paper mentions only that pilots ran on three sub-Saharan African schedules and one process statistic (about a third of reviewed entries corrected in one pilot).
- Public Finance Review material: the PFR topic mapping table in v0.9 and any reference to the PFR visualization tool. The paper says only that the diagnostic can feed the excise chapter of a public finance review.
- The v0.1 Tier 2 example's numbers (internally inconsistent and unsourced) and the v0.1 candidate-country lists.
- Internal platform details (the Bank's AI platform, account tiers) and the original prompts.

## Changes from v0.1

Cut from 24,800 to about 5,500 words; one paper instead of a three-part report (Part C, the policy pathway, is reduced to Section 7.3); stylized Country A replaces the pilot countries; the corrective-benchmark arithmetic is now reproducible from `2.Source/`; unsourced defaults (VSL USD 4.7 million, carbon USD 75/t) replaced by sourced ones.
