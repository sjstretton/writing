# AGENTS.md

Instructions for AI agents, including Claude Code (`CLAUDE.md` points here), working anywhere in this repo. Read this file first. Then read the instructions for the part you are working in; they take precedence for that part.

## The repo has two parts

| Part | Folders | Read before working | What it is for |
|---|---|---|---|
| **Planning** | `0 Morning Briefing`, `1 Planning Instructions`, `2 Strategic Plans`, `3 Archive` | `1 Planning Instructions/AGENTS.md`, then its `NORMS.md` | Tasks for every repo, day and week plans, strategic plans, the printable tracker, and the master Google Sheet kept in step with the repo |
| **Writing** | `A Writing Instructions` (with `Writing Standards`, `Templates and Info`, `Claude + Scripts`), `B Working Papers`, `C Research Proposal`, `D Climate Econ Course` | `A Writing Instructions/AGENTS.md`, then its `NORMS.md` | Papers, briefs and decks, the website, PhD proposals, the course |

`README.md` (this folder) maps the layout. Each part's `README.md` gives the detail.

## Who this is for

Stephen is easily overwhelmed by volume, so planning output must stay short and simple (see "Who this is for" and "Focus" in `1 Planning Instructions/NORMS.md`). Writing for outside readers follows `A Writing Instructions/NORMS.md`: for a busy reader, self-contained, the claim first in every paragraph, sourced.

## Rules for both parts

- Make the changes asked for. Don't reorganise, rename or delete files unless asked.
- Read a file before editing it, and match its style.
- Don't invent citations, figures, quotes or results. Mark anything uncertain.
- Don't commit secrets or credentials. The website's FTP login stays on Stephen's PC (`B Working Papers/8.Scripts/Reference/_ftp.txt`, git-ignored).
- Treat World Bank internal or confidential material as non-public.
- Paths in instructions are from the repo root unless the file says otherwise. Planning scripts run from `1 Planning Instructions/` (for example `python3 Scripts/update.py check`).

## Connecting the two parts

- **When you finish work in any part**, update the task in `0 Morning Briefing/3-TaskContextAndProjectPlans.md` (planning's rule). For writing work, also update `A Writing Instructions/TODO.md` and, for papers, `A Writing Instructions/PAPERS.md`.
- **Before pushing a change to planning files**, follow the consistency procedure in `1 Planning Instructions/AGENTS.md` ("Before every push to main"), which keeps the repo and the master Google Sheet in step. A push that touches only writing files does not need it.
- **Priorities.** `A Writing Instructions/STRATEGY.md` and the FY27 work plan in `2 Strategic Plans/` should agree. If they conflict, ask Stephen.

## Git

- Push to `main` when Stephen asks for it (he has, for overnight writing runs); otherwise work on the branch you were assigned.
- Write clear, descriptive commit messages.
- Don't open pull requests unless asked.
- Don't commit generated output unless the repo already tracks it (the website's `_site/` is tracked on purpose, because `deploy.bat` uploads it).

## Publishing

Stephen has given standing authorization to publish to his own website, under the conditions in `A Writing Instructions/AGENTS.md` ("Publishing"). Anything else outward-facing (email, social media, other sites) needs his approval each time.
