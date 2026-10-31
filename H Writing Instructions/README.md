# Writing

The writing part of the combined repo: papers, the Quarto website and its scripts, PhD proposals, the climate-economics course and the writing standards. The repo root `README.md` describes both parts; planning lives in folders 1–4.

## Start here

| File (in this folder) | Purpose |
|---|---|
| `AGENTS.md` | Instructions for AI agents working on the writing part (`CLAUDE.md` points to it). |
| `NORMS.md` | The overarching writing norms. |
| `NUMBERING.md` | Paper numbers and citation keys. |
| `STRATEGY.md` | Strategic priorities and specialisms. |
| `PAPERS.md` | Prioritised papers, introductory, concept and position papers. |
| `TODO.md` | The writing task list. |
| `Writing-Status-Report.md` | Audit of every paper and the housekeeping issues (29 Oct 2026). |
| `Scripts/SyncRepo.bat` | Sync script for Stephen's PC. |

## Folders (paths from the repo root)

| Folder | Contents |
|---|---|
| `H Writing Instructions` | This folder: instructions, norms, strategy, paper list and task list for the writing; `Writing Standards/` (principles, writing types, the paper standard, exemplars, Quarto templates, publishing log), `Templates and Info/` (Word templates), `Claude + Scripts/` (shared Claude workspace) and `Scripts/` (website scripts and the paper automation engine; see its README). |
| `C Policy and FInance` | Papers in sections 1–4. Each section folder holds numbered paper folders and one `<N>.0.Overview` folder; numbers follow `NUMBERING.md`. `index.html` lists every paper with links to its files. |
| &nbsp;&nbsp;`1.CarbonPricing` | 1.1 two-track architecture, 1.2 feebates, 1.3 converting VAT into a destination carbon tax, 1.4 CBAM recognition; also the book *The Right Policy at the Wrong Time* (`8.5.2`). See `1.0.Overview/RelatedWork.md`. |
| &nbsp;&nbsp;`2.OtherTaxAndFiscalPolicy` | 2.1 rent tax; also the book *Plucked!* (`8.5.3`). |
| &nbsp;&nbsp;`3.FinanceAndRisk` | 3.1 the payment intermediary, 3.2 clean-power asset classes; the book *Time and Chance* (`3.3`). |
| &nbsp;&nbsp;`4.SovereignIncentives` | 4.1 notional capitalized value, 4.2 the Climate Investment Trust, 4.3 sustainability-linked lending. |
| `D Modelling` | Papers in sections 5–7, due to move to a repo of their own. `index.html` lists every paper with links to its files. |
| &nbsp;&nbsp;`5.Modelling` | Companion papers to CPAT-AI: 5.1 methods, 5.2 implementation, 5.3 validation, 5.4 elasticities. |
| &nbsp;&nbsp;`6.ModularUpgrades` | 6.1 total effective carbon price, 6.2 CBAM tool, 6.3 public investment, 6.4 activity layer, 6.5 macro-fiscal-energy scenario tool. |
| &nbsp;&nbsp;`7.AdditionalAnalytics` | 7.1 excise diagnostic, 7.2 fiscal indicators dashboard. |
| `E Website` | The Quarto site: Policy and Finance (`index.qmd`, `policy/`), Modelling and Analytics (`modelling/`), About. `PaperArchive/` holds every published file, `papers/` only the linked ones. |
| `F Other Writing` | Writing outside the series and not on the website (8.1–8.7). |
| `B PhD Application` | PhD research proposals and application status (see its `README.md`). |
| `G Climate Econ Course` | Materials for a climate-fiscal economics course, organized by topic (A–G). |

Most subfolders that need extra explanation have their own `README.md` — check
there first for folder-specific conventions.

## Getting started

- Browse the papers with `C Policy and FInance/index.html` or `D Modelling/index.html`.
- Build the website with `Compile-Website.bat` and put it online with `Push-Website.bat` (or `Deploy-Website.bat` for both), at the repo root. `Scripts/README.md` explains them.
- `H Writing Instructions/Claude + Scripts/Setup Claude` documents the shared Claude workspace
  conventions (projects, inputs/working/outputs, archive).
