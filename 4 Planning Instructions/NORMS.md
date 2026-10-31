# NORMS

How to work in this repo: what to do in general. Repo layout: `README.md`. Step-by-step procedures for AI agents: `AGENTS.md`.

## Who this is for: Einstein, not a CEO

This system is **not a PA feeding a CEO**: more meetings, more briefings, more throughput, every hour filled. It is **feeding Einstein**: someone brilliant who does his best work when wandering and wondering, and who needs one thing from the system: **get the next paper out** (the PhD application first this week). That is the point of the whole exercise. Everything here either serves the next paper or gets out of its way.

Stephen describes himself as **AAAA**: **a**nxious-**a**voidant, easily overwhelmed, both holistic and detail-oriented (he needs the whole picture *and* the exact next action), and **A**DHD. So:

- **One priority at a time.** There is always exactly one: the PhD application this week, then the next paper (see Focus, below). Name it at the top of list 1, the Dashboard and the morning briefing. Its next step is Do now (AI may work on the second in parallel), unless something someone else depends on is due within 2 working days. Everything else waits, is batched or is delegated.
- **Simplify before adding.** Before adding a task, list, tab, column or rule, remove or park one. A new idea goes to Parked by default; a new task needs a reason it cannot wait.
- **Protect the wandering.** Unscheduled thinking time is the work, not a gap to fill. Don't pack free time with quick wins; a day with one paper step done is a full day.
- **Clear the path, don't push.** The next paper step is a physical action that can start in under a minute (which file, which section, the first sentence), not a project. Take friction away (admin, logistics, decisions) so he can stay in the thinking.
- **Little at a time.** Lists of 2-3 for now, then 2-3 for later; short lines. If he says he is tired, give only the first item.
- **Whole picture, one glance; then one action.** The Dashboard tab and page 1 of the printable show both.
- **Quick rewards with deadlines.** Every item shows its points and, where it helps, a deadline ("By 7pm: ...").
- **Decide the night before.** Tomorrow's 1-3 questions are written and answered in the evening (Daily decisions), so the morning has no decisions in it.
- **Avoided things get a 15-minute first step** and, where useful, a word-for-word script. Never a big ask.
- **No guilt.** Rest counts as a done day; a missed deadline rolls to the next slot without comment. One sanctioned distraction is fine when it still moves the writing (e.g. redoing a paper).

## Focus: less code, more writing (from 29 Oct 2026)

1. **PhD application.** This week; the one priority. Deadline Sat 31 Oct (confirmed by Stephen, 29 Oct).
2. **The next paper:** *Open Economy Carbon Pricing to Climate Policy*, for the journal *Climate Policy*. Next after the PhD; AI can work on it in parallel (journal format, what is left, drafts).

Job applications are dropped from the priorities for now (29 Oct): PhD first.

- These two are H. Writing that feeds them (writing samples, the priority-paper sequence, proposals) is the same work.
- **November exception: CPAT-LTS (2e_m2) is the main goal for November** because the other coded work is ahead of schedule (Python 75%, Excel-AI MVP 100%). It runs in work hours, after the PhD application (31 Oct) and alongside the paper. From December coded work shrinks again.
- **Coded work shrinks to the minimum** (CPAT, Python, Excel-AI, Shiny, integrations: PR1 and PR2). Keep the commitments others depend on. Delegate the rest to Kacper, and give AI long, all-day tasks with limited interaction (one clear brief, review at the end). Work hours only: never evenings or weekends, and never ahead of the paper unless a date someone depends on is within 2 working days. Don't propose new coded projects; park them.
- **Tie-break:** writing beats code.
- Personal priorities continue alongside, outside work hours: get a girlfriend; celebrate others, birthdays included.

## General rules

- **Everything earns points (the one points scheme).** Task 100 (quick) or 200. Milestone 1000 when complete, plus a **4000 bonus if it is completed in its target (due) week**: 5000 in all (e.g. the PhD application in the week of 26 Oct). Completed **before** its due week: an early bonus of half the milestone, **+500** (1500 in all; e.g. Final Python, 29 Oct, six weeks early). Kriya 10 x current streak (days), daily. CPAP 1 point per minute. Gym session 100. On the Dashboard's morning score: 10 per morning-routine step and per quick reward with no task. Every task and milestone carries its points on the Context tab; daily wellbeing points are on the Tracker tab.
- **Structure.** Projects (PR1...) hold milestones (1000 each, +4000 if done in the due week); milestones are reached through tasks (100-200). Each task row names its milestone.
- **Same change, both places.** Edit either side; `Scripts/update.py` brings the other side in line before each push to main (see below). Edit the Sheet in place: same file, same link. The Tracker, Track 2, Strategic plan and Links tabs are not synced: keep them in line by hand.
- **Here and now.** The top of `0 Morning Briefing/1-NextStep.txt` (and the Plan tab) lists what fits where I am right now, e.g. `HERE AND NOW (home, at a desk, Sun evening)`. Rewrite it whenever the context changes; each item carries its task ID so its points show.
- **One priority (morning briefing).** `0 Morning Briefing/3-OnePriority.txt` is the first thing to read each morning, on one screen, plain text: the one priority named at the top (now the PhD application), then its next steps only (3-4, each with a time and its value), and a script if one helps. Nothing about other projects. Rewrite it every evening for the next morning.
- **Project plans.** `0 Morning Briefing/4-HumanReadableProjectPlans.txt`: the plan for the priority project (numbered steps with dates, to the milestone), then a simple list of the other projects, one line each with its next step. Update it when the plan or a project's next step changes.
- **Next step (list 1) stays tiny.** Quick wins only at the top: Do now (one task: the next paper step, unless something someone depends on is due within 2 working days) and Do later (up to four options). Then To plan and Decide. Every item says its value in a few words.
- **Printable tracker.** `0 Morning Briefing/Me-Printable-Tracker.docx` is built: run `python3 Scripts/update.py build`. The name never changes, so links stay; each build also copies it to `3 Archive/Printable versions/Me-Printable-Tracker_v<version>.docx`. Bump `VERSION` in `Scripts/make_printable.py` when the layout changes. If Stephen edits the .docx by hand, that edit is the master: the build refuses until the edit is folded into the sources or the layout. Proper Word headings; clickable check boxes; every task shows its points. Page 1: the **morning briefing**, the Dashboard on paper on one page: points line, quick rewards (list 1, with deadlines), the morning routine, the focus project's two next steps, the priority milestone's burndown, today and this week (list 2), decide tonight and already decided. Page 2: contents (with page numbers), Immediate steps, Today, This week (from the .txt files). Then strategic priorities, avoided projects and milestone burndown; key decisions (closed ones struck through); last week's retrospective; buy, indoors, online quick wins, admin and ask-AI lists; then morning, evening and bags. It reads `0 Morning Briefing/5-TaskContextAndProjectPlans.md`, `0 Morning Briefing/1-NextStep.txt` (tag each item with its task ID, e.g. `(T14)`), `0 Morning Briefing/2-DayWeekPlan.txt`, `Context/3-Me-WeeklyLog.md` and `Context/routines.md`, so rebuild it whenever any of them changes.
- **Dashboard tab (the morning game).** The first tab of the Sheet; built by `Scripts/update.py render` like the other tabs, so never edit its layout by hand. Two pickers: a **project** (its two next open tasks show, Q1 first) and a **priority milestone** (done vs time used, due date, status, next step); the choices live in "Dashboard selections" in the task file and are synced. **Quick rewards** are list 1's Here and now, Do now and Do later items; start an item with `By <time>:` (e.g. `By 7pm: book the hotel (T45)`) to give it a deadline. **Morning routine** comes from the Morning list in `Context/routines.md`. The morning score adds the points of what is ticked. Ticks there count as done at the end of day, and a new day starts with no ticks. **Decide tonight / Already decided** is the "Daily decisions" table in the task file (synced both ways): in the evening, type 1-3 questions for tomorrow with a recommended answer in the empty rows, answer them and set Status to Decided; the end of day deletes decided rows older than that day.
- **Links.** When a file is added, renamed, moved or deleted, or a Sheet tab changes, update the Links tab of the master Sheet and the file tree above in the same session.
- **Strategic priorities:** the two in Focus (the next paper, PhD application), then get a girlfriend (follow up with people I know, journal my priorities, send messages) and celebrate others, birthdays included. Track them as personal milestones, first on the Tracker and in the burndown.
- **Keep it readable.** The Sheet is read on a desktop: wide columns, wrapped text; still keep the text short.
- **Five goals.** Every week uses the same five: 1 Work, 2 Strategic, 3 Family and relationships, 4 Personal, 5 Rest and health.
- **Where am I.** Each task has a context (home, online, at a desk, out, ask AI); its list is on the Updateable lists tab.
- **Weekly roll-up.** On the Tracker: type the finished week's task points into its "Week of" row (column F) if it isn't linked, rewrite This week from the top row of Weeks ahead, and add a row at the end of Weeks ahead; then set Tracker B17 (banked tasks this week) back to 0. Then rewrite `0 Morning Briefing/Me-Weekly.docx` (page 1 for the boss: done, in prospect, risks and asks; page 2: my week), add an entry to `3-Me-WeeklyLog.md`, delete Recently completed rows older than 14 days, refresh `6-RepoDirectory.md`, and run the consistency procedure below.

## Keeping everything consistent

Before every push to main (Claude does this; AGENTS.md has the steps):

1. **Snapshot** the Dashboard, Plan, Context, Regular lists, Updateable lists and Tracker tabs, and run `check-sheet`: consistency inside the Sheet (IDs, ticks, milestone % on Context, Plan and Tracker) and against the repo.
2. **Sync**: `python3 Scripts/update.py sync --snapshot S.json --apply`. Each item (a plan section, a task row, a list, a table) is compared three ways: repo, Sheet, last agreed state (`Context/sync-state.json`). Changed on one side only: that side wins. Changed differently on both sides: a conflict; nothing is applied and Stephen is asked.
3. **Build** the printable: `python3 Scripts/update.py build`.
4. **Render** the five synced tabs from the repo (`render`) and write them to the Sheet, then record the agreed state (`baseline`).
5. **Check**: `python3 Scripts/update.py check` (also runs on GitHub on every push to main, and locally with `CheckRepo.bat`).

**End of day** (the last item on the Evening list): tick what is done anywhere, then Claude runs `python3 Scripts/update.py eod`. Done anywhere is done everywhere: ticked items are deleted from the plan, the Dashboard, the Updateable lists and the Tracker's week grid; done tasks and milestones move to Recently completed; closed decisions go (and daily decisions settled before that day); the Tracker banks the points already scored (row 17); the Regular lists' ticks reset; and the plan is rewritten for the next morning. Milestone % has one source, the burndown table on the Plan tab: Context and the Tracker look it up.

## Standard requests

Answer from the Context tab. Each item shows its points and the one thing needed to start (link, number or ready-to-send text).

- **"What's next?"** (the default when Stephen asks what to do): the one priority (PhD application, then the paper), its one next physical step (file, section, first sentence) and how long it takes. Nothing else.

- **"Give me the quick win list"**: 2-3 quick wins for now, then 2-3 for later. Quick win = decided, under about 15 minutes, low energy. Match the day: on a weekend, leave out weekday-only tasks (office-hours calls, work tasks).
- **"Give me the decide and plan list"**: 2-3 for now, then 2-3 for later. Each: the question, the recommended answer, the milestone it unblocks.
- **"What is the quickest thing to make a priority milestone?"**: the priority milestone (1000), its %, and the single next task (with points) that moves it most.
- **The WhatsApp briefing** (also "the accountability update" or "short retrospective for the day": the same thing, for my accountability contact): ready to paste into WhatsApp. **The points are the point:** every item shows its points, grouped where they share a value, and line c) ends with the day's total. Extremely concise: a date line, then three lines, no other text.
  - **When.** Two a day, in Stephen's local time (now the Philippines, UTC+8). A request **before 7am** is most likely the start-of-day briefing; a request **after 11:55pm** is most likely the end-of-day briefing, for the day just ending. Otherwise ask which.
  - a) CPAP (last night: hours, 1 point per minute), Kriya streak (days, 10 x streak) and the morning routine (10 per step, `Context/routines.md`), from the Tracker's daily tracker; "not logged" if not given. Log what Stephen gives (see Morning update).
  - b) Milestones (1,000; 5,000 if done in the due week; 1,500 if done early); "none" if there are none.
  - c) Tasks (100-200), then the total.
  - **End of day: count everything.** Before totalling, check the day's commits in every repo (AI work counts: papers updated, code finished) and ask "Anything else done today?"; record what is missing as done tasks or milestones first. Never send a total from the ticks alone.
  - **Start of day: potential points**, from the morning briefing; line a) gives the morning routine in a few words (wake, stretch, drink, do; Kriya + breakfast 8-9), and c) ends "Potential total". **End of day: points actually scored**: only what was done (Recently completed with that day's date, and ticks), total scored against the morning's total if there was one; what wasn't done is left out, no comment. Example:
  ```
  Mon 19 Oct - start of day briefing
  a) CPAP 3h30 (210 pts) · Kriya streak day 2 (20 pts)
  b) Milestones: Edmundo on track (1,000)
  c) Edmundo prep, integration slide (2 × 200) · CPAT sent to Edmundo, new CPAT-CDPM repo, meeting notes (3 × 100) · Total 1,930 pts
  ```
- **Morning update** (Stephen gives last night's CPAP and the Kriya day): log them on the Tracker's daily tracker against the right day. Check the Kriya day against the streak (the day after day n is day n+1; a missed day resets to 1) and say if his number differs; check points as CPAP minutes and 10 x streak.
- **"Ask me for the milestones and update"**: one short message listing the open priority milestones with their current %; ask for the new figures; then update the Context tab and `0 Morning Briefing/5-TaskContextAndProjectPlans.md`, and report the points earned.

## Tasks (all repos)

- **One list.** Every task, in any repo or personal, has a row in the Context tab (master) and `0 Morning Briefing/5-TaskContextAndProjectPlans.md` (copy), with the next ID (IDs are never reused), points, energy, its milestone and a physical next action.
- **Importance:** H moves the next paper or the PhD application, or meets a deadline someone depends on; other coded work is M at most; M useful; L nice to have.
- **Urgency** (from the due date): U1 within 2 working days; U2 within 10; U3 later or no date.
- **Quadrant:** Q1 Do now (H+U1); Q2 Schedule (H+U2/U3); Q3 Batch or delegate (M/L+U1/U2); Q4 Not now (M/L+U3): move it to Parked tasks.
- **Order** Open by Q, then due date. The next step and day plan come from Q1; the week plan from Q1 and Q2.
- **Status:** Open, Now (at most one work and one personal), Blocked (say on what), Done (move to Recently completed with date and evidence).

## Repos

- `Context/6-RepoDirectory.md` lists every repo. Add a repo the first time a task names it; mark a guessed purpose with (?).
- Work in another repo: at the end of the session, update its rows in `0 Morning Briefing/5-TaskContextAndProjectPlans.md` here (or put the update in the final message if this repo can't be reached).
