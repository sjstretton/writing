# AGENTS

This system feeds Einstein, not a CEO: one priority (get the next paper out), less code, more writing (PhD and job applications next). Stephen is AAAA (anxious-avoidant, easily overwhelmed, holistic and detail-oriented, ADHD). Read "Who this is for" and "Focus" in `NORMS.md` first; simplify before adding anything.

Before editing `Day and Week Plans/1-Me-NextStep.txt` or `Day and Week Plans/2-Me-DayWeekPlan.txt`, read the norms:

- Format: `Strategic Plans/Planning Templates/1-AI-NextStep.txt` and `Strategic Plans/Planning Templates/2-AI-DayWeekPlan.txt`
- Rules (including keeping the master Google Sheet in step): `NORMS.md`
- Master: `Strategic Plans/Stephen_FY27_Work_Plan_v2.6_15thOct.docx`; master plan: the Google Sheet linked in `Strategic Plans/Stephen_FY27_Master_Plan_v3.3.url` (https://docs.google.com/spreadsheets/d/1WEHemG3x0kJ3yk-u1RcSheqYsX0T2aAXmiba9veaQag/edit); edit it in place with the Google Sheets connector, keeping the same file and link

This is the personal context repo. Tasks for **every** repo are tracked in `Day and Week Plans/3-TaskContextAndProjectPlans.md`, and other repos are listed in `Context/6-RepoDirectory.md`; their rules are in "Tasks" and "Repos" in `NORMS.md`. When a session finishes work in any repo, update `Day and Week Plans/3-TaskContextAndProjectPlans.md`.

When Stephen asks for the quick win list, the decide and plan list, the quickest route to a priority milestone, or a milestone update, follow "Standard requests" in `NORMS.md`: 2-3 items now, 2-3 later, each with points.

## Before every push to main: keep the repo, the Sheet and the printable consistent

Stephen's change is the master wherever he made it (a repo file, a Sheet tab or the printable). If both sides changed the same item differently, ask him which to keep; never pick one yourself.

1. `git pull` main.
2. Read the Dashboard, Plan, Context, Regular lists, Updateable lists and Tracker tabs with `get_values` (range `A1:K400` each) and save them as one JSON file in your scratchpad: `{"Dashboard": values, "Plan": values, "Context": values, "Regular lists": values, "Updateable lists": values, "Tracker": values}`. Then `python3 Scripts/update.py check-sheet --snapshot <file>` and tell Stephen what it finds (consistency inside the Sheet and against the repo).
3. `python3 Scripts/update.py sync --snapshot <file> --apply`. Exit code 2 means conflicts: show Stephen each one (repo vs Sheet) and stop until he decides; then make his choice in the repo and run sync again. Exit code 4 means a tab is missing from the snapshot.
4. If the printable was edited by hand, `build` refuses: fold Stephen's edit into the sources or into `Scripts/make_printable.py` first, then `python3 Scripts/update.py build --force`. Otherwise `python3 Scripts/update.py build`.
5. `python3 Scripts/update.py render --out <payload> --snapshot <file>`. If the Sheet has no Dashboard tab (sheetId 120), add it first as the first tab: `addSheet` with `{"sheetId": 120, "title": "Dashboard", "index": 0}`. For each tab in the payload: send its `requests` with `update_spreadsheet`, then write its `values` from A1 with `update_values` (replace any empty row `[]` with `[""]`). Then write each entry of `Tracker ranges` with `update_values`. Read the tabs back into a new snapshot and run `check-sheet` on it: it must say "Sheet consistent".
6. `python3 Scripts/update.py baseline`, then `python3 Scripts/update.py check` (it must print OK).
7. Commit and push. GitHub Actions runs the same check on main.

## End of day (Stephen asks for "the end-of-day tidy", or it is the last session of the day)

Done anywhere is done everywhere, and done items are deleted, not left ticked.

1. Steps 1-3 above (pull, snapshot including the Tracker, `check-sheet`, `sync --apply`).
2. `python3 Scripts/update.py eod --snapshot <file>` (dry run): show Stephen the tasks and milestones it will close and anything it is unsure of; then run it again with `--apply`. It deletes ticked items from the plan, the Updateable lists and the Tracker's week grid; empties the DONE sections; moves done tasks and milestones to Recently completed (deleting rows older than 14 days); clears closed decisions; banks the Tracker points already scored; and resets the Regular lists' ticks.
3. Get ready for the next day: make sure tomorrow's questions are in Daily decisions (ask Stephen for his answers if they are still open); rewrite `Day and Week Plans/1-Me-NextStep.txt` (date, Here and now for tomorrow morning's context, quick wins that suit that day, e.g. weekday calls on a weekday) and the Today section of `Day and Week Plans/2-Me-DayWeekPlan.txt` from the week plan and the Context tab.
4. Steps 4-7 above with `build --date <tomorrow>`, then delete the temporary file Context/.eod-tracker.json (it is git-ignored).
