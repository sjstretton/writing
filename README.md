# Stephen Stretton: planning and writing

One repo for two connected jobs. **Planning** decides what to do next: tasks, day and week plans, strategic plans and the master Google Sheet. **Writing** does the work that matters most: papers, the website, PhD proposals and the course. The planning part tracks tasks for every repo, including this one; the writing part holds the outputs.

Since 29 October 2026 the repo combines the former planning repo (`sjstretton/Planning`, earlier `PlanningPPTsAndGeneral`) with the writing repo (`sjstretton/writing`). Numbered folders (0–3) are planning; lettered folders (A–D) are writing.

## Start here

| If you want to… | Open |
|---|---|
| See this morning's briefing | `0 Morning Briefing/3-OnePriority.txt`: the one priority (the PhD application) and its next steps only |
| See the project plans | `0 Morning Briefing/4-HumanReadableProjectPlans.txt`: the priority project's plan, then the other projects, one line each |
| See today's plan and next step | `0 Morning Briefing/1-NextStep.txt`, or the **Dashboard** and **Today** tabs of the [master Google Sheet](https://docs.google.com/spreadsheets/d/1WEHemG3x0kJ3yk-u1RcSheqYsX0T2aAXmiba9veaQag/edit) |
| See every task, in every repo | `0 Morning Briefing/5-TaskContextAndProjectPlans.md` |
| See the strategic priorities | `E Writing Instructions/STRATEGY.md` (PhDs, papers, specialisms) and `2 Strategic Plans/` (work plan, master plan) |
| See my specialisms and the order for nailing them down | `SPECIALISMS.md` |
| See which papers come next | `E Writing Instructions/PAPERS.md` and `E Writing Instructions/TODO.md` |
| Work as an AI agent | `AGENTS.md` (this folder), then the part's own `AGENTS.md` |

## Layout

### Planning (folders 0–3)

| Folder | Contents |
|---|---|
| `0 Morning Briefing` | The morning briefing (start here), next steps, day and week plan, the master task file, the printable tracker and the weekly update |
| `1 Planning Instructions` | `README.md`, `AGENTS.md`, `NORMS.md` and `CLAUDE.md` for planning; `Scripts/` (`update.py`: sync with the Sheet, build the printable, check consistency, end of day; `make_printable.py`); `Context/` (routines, weekly log, repo directory, sync state); `CheckRepo.bat` |
| `2 Strategic Plans` | FY27 work plan, master plan (link to the Sheet and the last Excel copy), planning templates, past years (FY24, FY26) |
| `3 Archive` | Old versions and retired files, including printable versions |

### Writing (folders B–E)

| Folder | Contents |
|---|---|
| `E Writing Instructions` | `README.md`, `AGENTS.md`, `CLAUDE.md`, `NORMS.md`, `STRATEGY.md`, `PAPERS.md`, `TODO.md` and the paper status report for the writing; `Writing Standards/` (writing principles, writing types, the paper standard, AI tells, exemplars, the briefing-series specification and templates); `Templates and Info/` (Word templates: briefing, one-page pitch); `Claude + Scripts/` (shared Claude workspace: `Setup Claude/_admin/about-me.md` and `voice.md`, and scripts) |
| `B Working Papers` | The papers, by section; paper numbers follow the section folders (`E Writing Instructions/NUMBERING.md`). Each section folder holds its numbered paper folders and one `<N>.0.Overview` folder (overview, theme deck, section notes). 1 carbon pricing (1.1 overarching, 1.2 feebates, 1.3 CBAM, 1.4 carbon consumption tax); 2 other tax and fiscal policy (2.1 rent tax); 3 finance and risk; 4 sovereign incentives; 5 modelling (CPAT); 6 modular upgrades to CPAT (6.1 total effective carbon price, 6.2 CBAM tool, 6.3 public investment, 6.4 activity layer, 6.5 macro-fiscal-energy scenario tool); 7 additional analytics; 8 additional policy papers (8.1–8.7: other fiscal policy, finance, MDBs, analytics, books, philosophy, politics); 9 research tracking (source digests, trackers). `A.Website` holds the Quarto site. Scripts live in `E Writing Instructions/Scripts` (see its README); the two you need, `Compile-Website.bat` and `Deploy-Website.bat`, sit at the repo root |
| `C Research Proposal` | PhD research proposals and the application status |
| `D Climate Econ Course` | Climate-fiscal economics course materials, topics A–G |

Folders with their own `README.md` have local conventions; read it first.

## How the two parts connect

- **Tasks live in planning.** Writing tasks appear in `0 Morning Briefing/5-TaskContextAndProjectPlans.md` and the Sheet's Context tab (for example T13 PhD application, T46 writing upgrade). `E Writing Instructions/TODO.md` is the detailed working list for the writing; when a writing task finishes, update both.
- **Priorities are shared.** `E Writing Instructions/STRATEGY.md` and `2 Strategic Plans/Stephen_FY27_Work_Plan_v2.6_15thOct.docx` should agree; if they differ, ask Stephen.
- **One master per item.** Planning's rule (one home for each thing, kept in step by `1 Planning Instructions/Scripts/update.py`) applies to planning files and the Sheet. Writing files are mastered in the repo, with the `.qmd` as the master for each paper.
