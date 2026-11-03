# Stephen Stretton: planning and writing

One repo for two connected jobs. **Planning** decides what to do next: tasks, day and week plans, strategic plans and the master Google Sheet. **Writing** does the work that matters most: papers, the website, PhD proposals and the course. The planning part tracks tasks for every repo, including this one; the writing part holds the outputs.

Since 29 October 2026 the repo combines the former planning repo (`sjstretton/Planning`, earlier `PlanningPPTsAndGeneral`) with the writing repo (`sjstretton/writing`). Numbered folders (1–4) are planning; lettered folders (A–H) are writing. Papers in sections 5–7 (`D Modelling`) are due to move to a repo of their own.

## Start here

| If you want to… | Open |
|---|---|
| See this morning's briefing | `0A Daily and Weekly Task Lists/3-OnePriority.txt`: the one priority (the PhD application) and its next steps only |
| See the project plans | `0A Daily and Weekly Task Lists/4-HumanReadableProjectPlans.txt`: the priority project's plan, then the other projects, one line each |
| See today's plan and next step | `0A Daily and Weekly Task Lists/1-NextStep.txt`, or the **Dashboard** and **Today** tabs of the [master Google Sheet](https://docs.google.com/spreadsheets/d/1WEHemG3x0kJ3yk-u1RcSheqYsX0T2aAXmiba9veaQag/edit) |
| See every task, in every repo | `0A Daily and Weekly Task Lists/5-TaskContextAndProjectPlans.md` |
| See the strategic priorities | `H Writing Instructions/STRATEGY.md` (PhDs, papers, specialisms) and `2 Strategic Plans/` (work plan, master plan) |
| See my specialisms and the order for nailing them down | `A Specialisms, Theory and Research Profile/SPECIALISMS.md` |
| See which papers come next | `H Writing Instructions/PAPERS.md` and `H Writing Instructions/TODO.md` |
| Browse the papers and their files | `C Policy and FInance/index.html` and `D Modelling/index.html` (open in a browser; rebuilt by `Compile-Website.bat`) |
| Work as an AI agent | `AGENTS.md` (this folder), then the part's own `AGENTS.md` |

## Layout

### Planning (folders 1–4)

| Folder | Contents |
|---|---|
| `0A Daily and Weekly Task Lists` | The morning briefing (start here), next steps, day and week plan, the master task file, the printable tracker and the weekly update |
| `0B Quick Wins and Next Milestone` | The quick win list, the latest next-milestone plan (2A), the list of next milestones Stephen has chosen, and a link to the master Google Sheet; the other milestone plans are in `Other Milestones/` |
| `4 Planning Instructions` | `README.md`, `AGENTS.md`, `NORMS.md` and `CLAUDE.md` for planning; `Scripts/` (`update.py`: sync with the Sheet, build the printable, check consistency, end of day; `make_printable.py`); `Context/` (routines, weekly log, repo directory, sync state); `CheckRepo.bat` |
| `2 Strategic Plans` | FY27 work plan, master plan (link to the Sheet and the last Excel copy), planning templates, past years (FY24, FY26) |
| `3 Archive` | Old versions and retired files, including printable versions |

### Writing (folders A–H)

| Folder | Contents |
|---|---|
| `A Specialisms, Theory and Research Profile` | `SPECIALISMS.md`, the research overview and the paper tracker |
| `B Theory and Research` | The research behind the PhD and the papers: thesis plan, overview paper, research notes, Global Incentives Model documentation (all in the house template) |
| `C Policy and FInance` | Papers in sections 1–4, one folder per section with its numbered paper folders and one `<N>.0.Overview` folder (overview, theme deck, notes). 1 carbon pricing (1.1 two-track architecture, 1.2 feebates, 1.3 converting VAT into a destination carbon tax, 1.4 CBAM recognition); 2 other tax and fiscal policy (2.1 rent tax); 3 finance and risk; 4 sovereign incentives. Two books sit with their sections (`8.5.2` in 1, `8.5.3` *Plucked!* in 2) and *Time and Chance* is `3.3`. Paper numbers: `H Writing Instructions/NUMBERING.md` |
| `D Modelling` | Papers in sections 5–7: 5 modelling (CPAT); 6 modular upgrades to CPAT (6.1 total effective carbon price, 6.2 CBAM tool, 6.3 public investment, 6.4 activity layer, 6.5 macro-fiscal-energy scenario tool); 7 additional analytics. Due to move to its own repo |
| `E Website` | The Quarto site: tabs Policy and Finance (`index.qmd`, `policy/`), Modelling and Analytics (`modelling/`) and About. `PaperArchive/` holds every published file; `papers/` only the ones the pages link to. Run `Compile-Website.bat`, then `Push-Website.bat` (or `Deploy-Website.bat` for both), at the repo root |
| `F Other Writing` | Writing outside the series, not on the website: other fiscal policy, The Sollar, MDB papers, political economy, philosophy and politics |
| `G Climate Econ Course` | Climate-fiscal economics course materials, topics A–G |
| `H Writing Instructions` | `README.md`, `AGENTS.md`, `CLAUDE.md`, `NORMS.md`, `STRATEGY.md`, `PAPERS.md`, `NUMBERING.md`, `TODO.md` and the paper status report; `Writing Standards/` (writing principles, writing types, the paper standard, AI tells, exemplars, the briefing-series specification, publishing log, templates); `Templates and Info/` (Word templates); `Claude + Scripts/` (`Setup Claude/_admin/about-me.md` and `voice.md`); `Scripts/` (website scripts and the paper automation engine; see its README) |

Folders with their own `README.md` have local conventions; read it first.

## How the two parts connect

- **Tasks live in planning.** Writing tasks appear in `0A Daily and Weekly Task Lists/5-TaskContextAndProjectPlans.md` and the Sheet's Context tab (for example T13 PhD application, T46 writing upgrade). `H Writing Instructions/TODO.md` is the detailed working list for the writing; when a writing task finishes, update both.
- **Priorities are shared.** `H Writing Instructions/STRATEGY.md` and `2 Strategic Plans/Stephen_FY27_Work_Plan_v2.6_15thOct.docx` should agree; if they differ, ask Stephen.
- **One master per item.** Planning's rule (one home for each thing, kept in step by `4 Planning Instructions/Scripts/update.py`) applies to planning files and the Sheet. Writing files are mastered in the repo, with the `.qmd` as the master for each paper.
