# 5.2 CPAT-AI: Rebuilding a Policy Model as a Transparent, Testable Tool

**Status (31 October 2026):** working paper version 0.2 (about 6,400 words of body, executive summary as chapter 1) and policy brief version 1.0 (Climate Fiscal Policy Brief No. 5.2, key `CFPB52`), both peer-reviewed (`5.Notes/PeerReview-2026-10-31.md`) with every reference checked (`5.Notes/BibCheck-2026-10-31.md`); deck of 11 slides on the new builder. Companion paper to the public CPAT-AI repository (https://github.com/cpmodelai/cpat_ai). Version 0.1 (29 October 2026) is in `8.PreviousVersions/`. Series plan: `../5.0.Overview/SeriesArchitecture.md`.

**Scope (new, 29 October 2026): implementation only.** How legacy CPAT was rebuilt twice (Excel-AI and Coded CPAT) with AI assistance, under the rule "bugs are never replicated; issues are replicated and tracked"; what the rebuild found; the testing regime; what AI did and did not do; lessons for building and maintaining policy models. The former strands of this folder move elsewhere: the CPAT architecture and power-investment equations go to 5.1 (Mitigation Methods); the fiscal-application strand (SiSePuede–CCDR–CPAT framing, investment, fiscal risk, debt sustainability) moves to the extensions 6.3 (Public Investment) and 6.4 (Activity Modelling); validation goes to 5.3.

**Question.** Can a large spreadsheet policy model be rebuilt so that every step can be read and tested, and what does such a rebuild reveal?

**Answer.** Yes: two rebuilds with shared variable codes, one register and tests on every output code, built mostly by AI coding agents under written norms with every judgment kept by the model owner. The rebuild of CPAT found 228 legacy bugs (24 high priority), 135 issues, 35 departures, 14 upgrades and 20 documentation bugs; writing the model a second time in Python found 7 confirmed bugs in the Excel prototype.

## Files

| File | What |
|---|---|
| `CPATAIImplementation.qmd` / `.docx` / `.bib` | Working paper master (version 0.2), rendered with pandoc (Chicago author-date) |
| `1.Presentation/Brief-CPATAIImplementation.qmd` / `.docx` / `.bib` | Policy brief master (version 1.0); its `.bib` is copied from the working paper's for the keys it cites |
| `1.Presentation/slides.json`, `Slides-CPATAIImplementation.pptx` | Deck (11 slides), built with `H Writing Instructions/Writing Standards/templates/make_deck.py` |
| `1.Presentation/figures/make_figures.py` | Makes `fig_register.png` and `fig_growth.png` (numbers as the working paper) |
| `5.Notes/` | Peer review and reference check, 31 October 2026 |
| `8.PreviousVersions/` | Working paper v0.1 (qmd, docx, bib), deck v0.1 (pptx, json), old figure script |
| `3.RelatedPiecesAndLinks/` | Older background material (AI-assisted recoding notes; WB models; CPAT modelling of ETS; fiscal long-term strategy concept, now for 6.3/6.4) |
| `9.Archive/` | `CPAT_PricesModule_v1.10`, `v1.11` workbooks: the early prices-module record of the recoding |
| `CPATArchitectureRecodingAndFiscalApplication.xlsx` | Planning workbook from the old three-strand scope (kept; not used by the paper) |

Render (from this folder; the brief the same way from `1.Presentation/`): `pandoc CPATAIImplementation.qmd -f markdown --lua-filter="<repo>/H Writing Instructions/Scripts/Website/quarto-xref.lua" --lua-filter="<repo>/H Writing Instructions/Scripts/Website/web-links.lua" --citeproc --bibliography=CPATAIImplementation.bib --csl="<repo>/E Website/chicago-author-date.csl" -o CPATAIImplementation.docx`.

## Sources used

All public. The CPAT-AI repository was read on 31 October 2026 (its git history was restarted on 30 October, so release 1.0.2 was read from the versioned files in `excel_ai/bugs_and_legacy/register/releases/` and from the first commit after the restart):

- The register: `Tracking_Legacy_Bugs_v1.0.2.xlsx` (tabs Bugs and Issues; every count in Table 1 recomputed) and `Legacy_CPAT_Bugs_v1.0.2.docx`; the current `excel_ai/core/BUGS.md` and `ISSUES.md` (release 1.1.0 totals).
- `excel_ai/NORMS.md` (now `excel_ai/core/NORMS.md`) and `coded/NORMS.md`; `excel_ai/core/CAVEATS.md` (task log); `coded/README.md`, `coded/CHANGELOG.md`; `docs/CPAT_ai_documentation_qmd/01_Project_Overview.qmd`; `docs/CPAT_coded_documentation_qmd/06_Testing.qmd` and `_test_status.md`; `coded/cpat_testing/compare/legacy_comparison.md`.
- The CPAT Documentation (foreword and the mitigation chapter, `docs/CPAT_full_documentation_qmd/`), published on https://cpmodelai.github.io/cpat_ai/.
- External sources, each checked against the source: see `5.Notes/BibCheck-2026-10-31.md`.

## Held back (confidentiality)

- No proprietary CPAT data or values derived from it. The paper uses register counts, test statistics and the effects of bugs as stated in the repository's shareable documents (bug document, deck), which by the repo's own rule hold no proprietary data.
- No Egypt policy-scenario results (carbon tax packages, revenue, welfare) are reproduced, although the public deck shows some.
- Nothing from the private Climate Fiscal AI Tools repository (the v0.1 count of 126 bugs from one of its slides is replaced by the public task log's counts).
- The overview deck `excel_ai/CPAT-AI_Overview_v1.0.0.pptx` is not used as a source from v0.2, because its title slide says "prototype for discussion"; its numbers are taken from the register and the task log instead.
- The folder's `CPATArchitectureRecodingAndFiscalApplication.xlsx` (it holds a copy of CPAT domestic price data) is not used.

## Notes for Stephen

- Credits (resolved 29 Oct 2026): the first footnote credits Paulina Schulz-Antipa for CPAT's air-pollution module, and the CPAT team and the mitigation documentation authors. Distribution (Faustyna Gawryluk) and transport co-benefits (Alexandra Campmas) are credited through the documentation authorship.
- AI assistance (resolved 29 Oct 2026, Stephen's decision): described as "Claude Code and GitHub Copilot".
- Egypt figures (resolved 29 Oct 2026, Stephen's decision): the deck's 185 million and "+0.5% compounding to about +10%" are dropped; the paper cites the UN World Population Prospects 2024 projection for Egypt (147.0 million in 2041, medium variant) and describes the GDP bug (L24) without a size.
- The count of legacy bugs that are "fixed, or the feature not built" differs slightly between documents (docx stock table: 220 fixed, 8 not built; BUGS.md: 20 marked out of scope); the paper avoids the split.
- The papers keep release 1.0.2 (29 October 2026) as their dated snapshot; by release 1.1.0 (30 October) the register held 231 legacy bugs (still 24 high). Update the counts when the paper is next revised.
