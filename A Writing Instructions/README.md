# Writing

The writing part of the combined repo: papers, the Quarto website and its scripts, PhD proposals, the climate-economics course and the writing standards. The repo root `README.md` describes both parts; planning lives in folders 0–3.

## Start here

| File (in this folder) | Purpose |
|---|---|
| `AGENTS.md` | Instructions for AI agents working on the writing part (`CLAUDE.md` points to it). |
| `NORMS.md` | The overarching writing norms. |
| `STRATEGY.md` | Strategic priorities and specialisms. |
| `PAPERS.md` | Prioritised papers, introductory, concept and position papers. |
| `TODO.md` | The writing task list. |
| `Writing-Status-Report.md` | Audit of every paper and the housekeeping issues (29 Oct 2026). |
| `SyncRepo.bat` | Sync script for Stephen's PC. |

## Folders (paths from the repo root)

| Folder | Contents |
|---|---|
| `A Writing Instructions` | This folder: instructions, norms, strategy, paper list and task list for the writing; `Writing Standards/` (principles, writing types, the paper standard, exemplars, Quarto templates), `Templates and Info/` (Word templates) and `Claude + Scripts/` (shared Claude workspace and scripts; see its README). |
| `B Working Papers` | Main body of research and the public-facing website. Each section folder holds numbered paper folders and one `<N>.0.Overview` folder; numbers follow `NUMBERING.md`. Organized as: |
| &nbsp;&nbsp;`1.CarbonPricing` | Section 1, the carbon-pricing series: 1.1 (overarching), 1.2 feebates, 1.3 CBAM, 1.4 carbon consumption tax. See `1.0.Overview/RelatedWork.md`. |
| &nbsp;&nbsp;`2.OtherTaxAndFiscalPolicy` | Section 2: Rent Tax (2.1). |
| &nbsp;&nbsp;`3.FinanceAndRisk` | Section 3: the payment intermediary (3.1) and clean-power asset classes (3.2). |
| &nbsp;&nbsp;`4.SovereignIncentives` | Section 4: notional capitalized value (4.1), the Climate Investment Trust (4.2), sustainability-linked lending (4.3). |
| &nbsp;&nbsp;`5.Modelling` | Section 5: companion papers to CPAT-AI (5.1 methods, 5.2 implementation, 5.3 validation, 5.4 elasticities). |
| &nbsp;&nbsp;`6.ModularUpgrades` | Section 6: modular upgrades to CPAT (6.1 total effective carbon price, 6.2 CBAM tool, 6.3 public investment, 6.4 activity layer, 6.5 macro-fiscal-energy scenario tool). |
| &nbsp;&nbsp;`7.AdditionalAnalytics` | Section 7: analytics tools (7.1 excise diagnostic, 7.2 fiscal indicators dashboard). |
| &nbsp;&nbsp;`8.AdditionalPolicyPapers` | Section 8: papers outside the main sections, in subsections 8.1–8.7 (other fiscal policy, finance, MDBs, analytics, books, philosophy, politics). |
| &nbsp;&nbsp;`9.ResearchTracking` | Source digests and trackers. |
| &nbsp;&nbsp;`A.Website` | Quarto site source (`*.qmd`, `_quarto.yml`) that publishes the research. |
| &nbsp;&nbsp;`B.Scripts` | Automation engine (`Engine`, `Reference`, `Run`, `Steps`) used to generate reports. |
| `C PhD Application` | PhD research proposals and application status (see its `README.md`). |
| `D Climate Econ Course` | Materials for a climate-fiscal economics course, organized by topic (A–G). |

Most subfolders that need extra explanation have their own `README.md` — check
there first for folder-specific conventions.

## Getting started

- Browse a topic folder under `B Working Papers` for the relevant papers.
- The website source lives in `B Working Papers/A.Website`; see its
  `render.bat`/`preview.bat`/`deploy.bat` scripts for building and publishing.
- The `B.Scripts` folder contains the engine used to run/generate reports —
  see `B.Scripts/Run/README.md` and `B.Scripts/Steps/README.md` for usage.
- `A Writing Instructions/Claude + Scripts/Setup Claude` documents the shared Claude workspace
  conventions (projects, inputs/working/outputs, archive).
