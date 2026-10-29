# 4.2 CPAT-AI: Rebuilding a Policy Model as a Transparent, Testable Tool

**Status:** first full draft, version 0.1 (29 October 2026). One medium-length working paper (about 5,000 words of body), companion paper to the CPAT-AI repository (https://github.com/cpmodelai/cpat_ai). Awaiting Stephen's peer review. Series plan: `../SeriesArchitecture.md`.

**Scope (new, 29 October 2026): implementation only.** How legacy CPAT was rebuilt twice (Excel-AI and Coded CPAT) with AI assistance, under the rule "bugs are never replicated; issues are replicated and tracked"; what the rebuild found; the testing regime; what AI did and did not do; lessons for building and maintaining policy models. The former strands of this folder move elsewhere: the CPAT architecture and power-investment equations go to 4.1 (Mitigation Methods); the fiscal-application strand (SiSePuede–CCDR–CPAT framing, investment, fiscal risk, debt sustainability) moves to the extensions 4.6 (Public Investment) and 4.7 (Activity Modelling); validation goes to 4.3.

**Question.** Can a large spreadsheet policy model be rebuilt so that every step can be read and tested, and what does such a rebuild reveal?

**Answer.** Yes: two rebuilds with shared variable codes, one register and tests on every output code, built mostly by AI coding agents under written norms with every judgment kept by the model owner. The rebuild of CPAT found 228 legacy bugs (24 high priority), 135 issues, 35 departures, 14 upgrades and 20 documentation bugs; writing the model a second time in Python found 7 confirmed bugs in the Excel prototype.

## Files

| File | What |
|---|---|
| `CPATAIImplementation.qmd` / `.docx` / `.bib` | Working paper master (version 0.1), rendered with pandoc (Chicago author-date) |
| `3.BackgroundPapers/` | Older background material (AI-assisted recoding notes; WB models; CPAT modelling of ETS; fiscal long-term strategy concept, now for 4.6/4.7) |
| `9.Archive/` | `CPAT_PricesModule_v1.10`, `v1.11` workbooks: the early prices-module record of the recoding |
| `CPATArchitectureRecodingAndFiscalApplication.xlsx` | Planning workbook from the old three-strand scope (kept; not used by the paper) |

Render: from this folder, `pandoc CPATAIImplementation.qmd -f markdown --citeproc --bibliography=CPATAIImplementation.bib --csl=<chicago-author-date.csl> --resource-path=. -o CPATAIImplementation.docx`.

## Sources used

All from the public CPAT-AI repository, release 1.0.2 / 1.0.2p1.1 (29 October 2026), read-only clone at `/home/user/cpmodelai/cpat_ai`:

- `README.md`, `AGENTS.md`, `NORMS.md` (section 0, the replication rule; sections 3, 6, 6b, 7), `CAVEATS.md` (task log, 2–29 October 2026), `CHANGELOG.md`.
- `excel_ai/README.md`, `excel_ai/BUGS.md`, `excel_ai/ISSUES.md` (Table 1 counts computed from these), `excel_ai/Legacy_CPAT_Bugs_v1.0.2.docx` (stock table), `excel_ai/CPAT-AI_Overview_v1.0.0.pptx` (formula count, file size, high-priority bug effects).
- `coded/README.md`; `docs/CPAT_ai_documentation_qmd/` chapters 01, 02, 03, 05, 06, 10, 13, 14, 16; `docs/CPAT_coded_documentation_qmd/` 06 Testing (with `_test_status.md`), 07 Architecture, 11 Versions, H Norms; `coded/cpat_testing/compare/legacy_comparison.md`.
- `HumanReadme-QuickStart.docx` (how the AI works; module owners; data security).
- `climate-fiscal-ai-tools/CPAT-AI-tool+ppt_only/CPAT-AI-Mitigation-MVP_Overview_v6.3.pptx` (126 legacy bugs at v0.6.3, 20 October 2026).
- Mitigation documentation authorship: `docs/CPAT_full_documentation_qmd/03_Mitigation.qmd` (first footnote).
- External references verified on Crossref: Panko (1998), Herndon, Ash and Pollin (2014), Wilson et al. (2014), Sargent (2013), Chang and Li (2015), Korinek (2023), Black et al. (2023, IMF WP 2023/128).

## Held back (confidentiality)

- No proprietary CPAT data or values derived from it. The paper uses register counts, test statistics and the effects of bugs as stated in the repository's shareable documents (bug document, deck), which by the repo's own rule hold no proprietary data.
- No Egypt policy-scenario results (carbon tax packages, revenue, welfare) are reproduced, although the public deck shows some.
- Nothing from the private Climate Fiscal AI Tools repository except the count of 126 bugs on a public-facing overview slide.

## Notes for Stephen

- Credits: the first footnote credits the CPAT team and the mitigation documentation authors. The air-pollution module owner (Paulina) is not named because her surname is not in the sources; add if wanted. Distribution (Faustyna Gawryluk) and transport co-benefits (Alexandra Campmas) are credited only through the documentation authorship.
- The paper says the agents worked "mainly through Claude Code" (from `CLAUDE.md`, branch names and the set-up guide). Confirm.
- "Egypt's population in 2041: 185 million instead of 147 million" and "+0.5% GDP compounding to about +10%" are from the v1.0.0 deck; confirm they are the Egypt run.
- The count of legacy bugs that are "fixed, or the feature not built" differs slightly between documents (docx stock table: 220 fixed, 8 not built; BUGS.md: 20 marked out of scope); the paper avoids the split.
