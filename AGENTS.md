# AGENTS.md

Instructions for AI agents, including Claude Code (`CLAUDE.md` points here), working anywhere in this repo. Read this file first. Then read the instructions for the part you are working in; they take precedence for that part.

## The repo has two parts

| Part | Folders | Read before working | What it is for |
|---|---|---|---|
| **Planning** | `1 Morning Briefing`, `4 Planning Instructions`, `2 Strategic Plans`, `3 Archive` | `4 Planning Instructions/AGENTS.md`, then its `NORMS.md` | Tasks for every repo, day and week plans, strategic plans, the printable tracker, and the master Google Sheet kept in step with the repo |
| **Writing** | `A Specialisms, Theory and Research Profile`, `B PhD Application`, `C Policy and FInance` and `D Modelling` (the papers), `E Website`, `F Other Writing`, `G Climate Econ Course`, `H Writing Instructions` | `H Writing Instructions/AGENTS.md`, then its `NORMS.md` | Papers, briefs and decks, the website, PhD proposals, the course |

`README.md` (this folder) maps the layout. Each part's `README.md` gives the detail.

## Who this is for

Stephen is easily overwhelmed by volume, so planning output must stay short and simple (see "Who this is for" and "Focus" in `4 Planning Instructions/NORMS.md`). Writing for outside readers follows `H Writing Instructions/NORMS.md`: for a busy reader, self-contained, the claim first in every paragraph, sourced.

## Rules for both parts

- Make the changes asked for. Don't reorganise, rename or delete files unless asked.
- Read a file before editing it, and match its style.
- Don't invent citations, figures, quotes or results. Mark anything uncertain.
- Don't commit secrets or credentials. The website's FTP login stays on Stephen's PC in `FTP-Login.txt` at the repo root, which is git-ignored.
- Treat World Bank internal or confidential material as non-public.
- Paths in instructions are from the repo root unless the file says otherwise. Planning scripts run from `4 Planning Instructions/` (for example `python3 Scripts/update.py check`).

## Connecting the two parts

- **When you finish work in any part**, update the task in `1 Morning Briefing/5-TaskContextAndProjectPlans.md` (planning's rule). For writing work, also update `H Writing Instructions/TODO.md` and, for papers, `H Writing Instructions/PAPERS.md`.
- **Before pushing a change to planning files**, follow the consistency procedure in `4 Planning Instructions/AGENTS.md` ("Before every push to main"), which keeps the repo and the master Google Sheet in step. A push that touches only writing files does not need it.
- **Priorities.** `H Writing Instructions/STRATEGY.md` and the FY27 work plan in `2 Strategic Plans/` should agree. If they conflict, ask Stephen.

## Git

- Push to `main` when Stephen asks for it (he has, for overnight writing runs); otherwise work on the branch you were assigned.
- Write clear, descriptive commit messages.
- Don't open pull requests unless asked.
- Don't commit generated output unless the repo already tracks it (the website's `_site/` is tracked on purpose, because `deploy.bat` uploads it).

## Publishing

Stephen has given standing authorization to publish to his own website, under the conditions in `H Writing Instructions/AGENTS.md` ("Publishing"). Anything else outward-facing (email, social media, other sites) needs his approval each time.
