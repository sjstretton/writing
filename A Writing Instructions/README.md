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
| `B Working Papers` | Main body of research and the public-facing website, organized as: |
| &nbsp;&nbsp;`1.ClimateAndFiscalPolicy` | The carbon-pricing series: 1.1 (overarching), 1.2 feebates, 1.3 CBAM, 1.6 carbon consumption tax, 1.7 total effective carbon price. See its `RelatedWork.md`. |
| &nbsp;&nbsp;`1B.OtherFiscalPolicy` | Fiscal-policy papers outside the series (rent tax, legacy coal PPAs). |
| &nbsp;&nbsp;`2.FinanceAndRisk` | Climate finance intermediation, climate investment trust, and risk work. |
| &nbsp;&nbsp;`3.SovereignIncentives` | Sovereign incentives, notional capitalised value and guarantees. |
| &nbsp;&nbsp;`4.Modelling` | CPAT architecture recoding, fiscal application, and background modelling papers (the TECP paper moved to 1.7). |
| &nbsp;&nbsp;`5.Analytics` | Excise-fiscal diagnostics and related analytics. |
| &nbsp;&nbsp;`6.Additional` | Papers outside the main portfolio, books, philosophy and politics. |
| &nbsp;&nbsp;`7.Website` | Quarto site source (`*.qmd`, `_quarto.yml`) that publishes the research. |
| &nbsp;&nbsp;`8.Scripts` | Automation engine (`Engine`, `Reference`, `Run`, `Steps`) used to generate reports. |
| &nbsp;&nbsp;`9.ResearchTracking` | CV, paper tracker, and research overview documents. |
| `C Research Proposal` | PhD research proposals and application status (see its `README.md`). |
| `D Climate Econ Course` | Materials for a climate-fiscal economics course, organized by topic (A–G). |

Most subfolders that need extra explanation have their own `README.md` — check
there first for folder-specific conventions.

## Getting started

- Browse a topic folder under `B Working Papers` for the relevant papers.
- The website source lives in `B Working Papers/7.Website`; see its
  `render.bat`/`preview.bat`/`deploy.bat` scripts for building and publishing.
- The `8.Scripts` folder contains the engine used to run/generate reports —
  see `8.Scripts/Run/README.md` and `8.Scripts/Steps/README.md` for usage.
- `A Writing Instructions/Claude + Scripts/Setup Claude` documents the shared Claude workspace
  conventions (projects, inputs/working/outputs, archive).
