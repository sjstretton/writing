# Planning

Personal context repo: plans, tasks for **all** repos, and planning documents.

Built to feed Einstein, not a CEO: one priority (get the next paper out), less code, more writing, for an AAAA person (anxious-avoidant, easily overwhelmed, holistic and detail-oriented, ADHD). The rules are in `NORMS.md` ("Who this is for" and "Focus").

**Start here each morning:** `0A Daily and Weekly Task Lists/3-OnePriority.txt` (the one priority and its next steps), the **Dashboard** tab of the Sheet, or page 1 of the printable.

**One rule: each thing has one home, and every copy is kept in step by `Scripts/update.py`.** The repo files and the master Google Sheet hold the same plan, tasks and lists; whichever side Stephen changed is the master for that item (see "Keeping everything consistent" in `NORMS.md`).

## Files

Planning now lives in the combined repo `sjstretton/writing`, alongside the writing work (see the root `README.md`). The planning part is the four numbered folders; paths below are from the repo root.

```
.
├── 0A Daily and Weekly Task Lists/        3-OnePriority.txt (the one priority and its next steps),
│                              1-NextStep.txt (next steps), 2-DayWeekPlan.txt (today and this week),
│                              4-HumanReadableProjectPlans.txt (the priority project's plan; other projects one line each),
│                              5-TaskContextAndProjectPlans.md (all tasks with context and points; project plans; daily decisions; parked tasks),
│                              Me-Printable-Tracker.docx (printable tracker, page 1 the morning briefing; built by Scripts/update.py; no version in the name,
│                              so links stay; versions in 3 Archive/Printable versions/),
│                              Me-Weekly.docx (page 1: update for the boss; page 2: my week)
├── 4 Planning Instructions/   README.md (this file), NORMS.md (how to work: the rules), AGENTS.md, CLAUDE.md,
│                              CheckRepo.bat (runs the consistency check),
│                              Scripts/ update.py (sync, build, check, render, eod), make_printable.py (the Word layout),
│                              Context/ routines.md (regular lists), 3-Me-WeeklyLog.md, 6-RepoDirectory.md,
│                              sync-state.json (last agreed state)
├── 2 Strategic Plans/         Stephen_FY27_Master_Plan_v3.3.url (link to the master Google Sheet),
│                              Stephen_FY27_Master_Plan_v3.2.xlsx (last Excel version, 25 Oct: Gantt, funding, leave, calendar),
│                              Stephen_FY27_Work_Plan_v2.6_15thOct.docx (FY27 work plan), AIClimate-FiscalTools_v2.5.pptx,
│                              Planning Templates/, FY24/, FY26/
└── 3 Archive/                 old versions and retired files; Printable versions/ holds each printable layout version
```

Run the scripts from `4 Planning Instructions/` (for example `python3 Scripts/update.py check`, or `CheckRepo.bat`).

**Master Google Sheet** ([open](https://docs.google.com/spreadsheets/d/1WEHemG3x0kJ3yk-u1RcSheqYsX0T2aAXmiba9veaQag/edit)), laid out for a desktop PC (wide columns, wrapped text, frozen headers):

| Tab | What it holds | Copy in the repo |
|---|---|---|
| Dashboard | The morning game, one screen: project picker with its two next steps; priority picker with its burndown; quick rewards with deadlines and the morning routine (tick to score); decide tonight (for tomorrow) and already decided. Column G (hidden) holds the sync keys | Dashboard selections and Daily decisions in `0A Daily and Weekly Task Lists/5-TaskContextAndProjectPlans.md`; quick rewards from `1-NextStep.txt`; routine from `Context/routines.md` |
| Track 2 | Track 1 is the main coded effort (the Strategic Year Gantt in the master plan); Track 2 is everything else, in the same layout as that Gantt (code, task, dates, status, weekly bars, ◆ milestones, this week highlighted), for everything except the main coded effort: PhD application, Open Economy Carbon Pricing paper for Climate Policy (low priority, in parallel), Klaus and Phil updates, work frameworks plan, WPA and invoices, AI safety proposal, automated blogging. Edited by hand, not synced | - |
| Plan | Same order as the printable: summary, here and now, quick wins (do now, do later), to plan, done; today; this week, decisions, done; strategic priorities, avoided projects, milestone burndown, key decisions. Tick boxes; points looked up from Context. Column I (hidden) holds the sync keys: do not edit it | `0A Daily and Weekly Task Lists/1-NextStep.txt`, `0A Daily and Weekly Task Lists/2-DayWeekPlan.txt`, tables in `0A Daily and Weekly Task Lists/5-TaskContextAndProjectPlans.md` |
| Tracker | One wide tab: points score; this week's five goals (tick tasks to score); milestone % (personal first); weeks ahead in the same five goals; daily tracker (CPAP, Kriya, gym) | - |
| Strategic plan | FY27 Gantt rows and milestones in date order | - |
| Context | **The master task table.** Every task: ID, task, points, energy, Q, status, %, milestone, next action. Then milestones (1000 points each), projects, parked tasks, recently completed | `0A Daily and Weekly Task Lists/5-TaskContextAndProjectPlans.md` |
| Regular lists | The lists that rarely change: morning, gym, evening, sleep protocol, main bag, grab bag; tick boxes | `Context/routines.md` |
| Updateable lists | The lists that change: buy, home, online, admin, ask AI (each item with its task and points), then task scripts | Lists by place and Task scripts in `0A Daily and Weekly Task Lists/5-TaskContextAndProjectPlans.md` |
| Links | Tap-to-open links to the sheet, the text files, the Word documents and a zip of the repo | - |

The last Excel version of the master plan, `Stephen_FY27_Master_Plan_v3.2.xlsx` (Gantt, funding, leave, calendar; synced 25 Oct 2026), is in `2 Strategic Plans/`; older versions are in `3 Archive/`.

## Norms

The rules for working in this repo (points, tasks, repos, standard requests, keeping the repo and the Sheet consistent) are in `NORMS.md`.
