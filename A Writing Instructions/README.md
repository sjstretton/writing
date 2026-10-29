# Research

Personal research workspace covering climate-fiscal economics, sovereign risk,
and related modelling/analytics — including the underlying papers, a Quarto
website, scripting engine, and a shared Claude workspace.

## Start here

| File | Purpose |
|---|---|
| `AGENTS.md` | Instructions for AI agents (Claude Code reads it via `CLAUDE.md`). |
| `NORMS.md` | The overarching writing norms. |
| `STRATEGY.md` | Strategic priorities and specialisms. |
| `PAPERS.md` | Prioritised papers, introductory, concept and position papers. |
| `TODO.md` | The live task list. |
| `Writing-Status-Report.md` | Audit of every paper and the housekeeping issues (29 Oct 2026). |

## Repository layout

| Folder | Contents |
|---|---|
| `A Research Proposal` | PhD research proposals and application status (see its `README.md`). |
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
| `C Climate Econ Course` | Materials for a climate-fiscal economics course, organized by topic (A–G). |
| `D Templates and Info` | Shared Word templates (briefings, one-pagers). |
| `E Writing Standards` | Writing principles, writing types, the paper standard, exemplars and Quarto templates. |
| `F Claude + Scripts` | Shared workspace and scripts for working with Claude (see its own README). |

Most subfolders that need extra explanation have their own `README.md` — check
there first for folder-specific conventions.

## Getting started

- Browse a topic folder under `B Working Papers` for the relevant papers.
- The website source lives in `B Working Papers/7.Website`; see its
  `render.bat`/`preview.bat`/`deploy.bat` scripts for building and publishing.
- The `8.Scripts` folder contains the engine used to run/generate reports —
  see `8.Scripts/Run/README.md` and `8.Scripts/Steps/README.md` for usage.
- `F Claude + Scripts/Setup Claude` documents the shared Claude workspace
  conventions (projects, inputs/working/outputs, archive).
