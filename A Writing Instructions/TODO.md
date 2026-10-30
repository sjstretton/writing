# TODO.md

The live task list. Agents take work from the top of "Now", mark progress here and commit the change with the work. Move done items to "Done" with the date.

Format: `- [ ] Task — owner — due — notes`. Owner is **S** (Stephen) or **A** (agent).

## Now

### Priority 1: PhD in climate policy (proposal 1, send ASAP)

Details for each item: `C PhD Application/PhD-Application-Status.md`.

- [ ] **Next step:** email Dr Shrimali the cleaned proposal; ask him to confirm supervision in writing and about a co-supervisor — S — today (15 min)
- [ ] Settle the deadline on the live Oxford course page. Stephen's working deadline is Sat 31 Oct; the status notes found 13 Nov (early) and 26 Jan (final), unverified. Josh's information sheet (`C PhD Application/PhD-Information-Sheet.md`, 30 Oct) gives no Oxford date; "before start of November" there is UCL's February-intake rule, the likely source of 31 Oct. Also check whether a statement of purpose is needed (Josh's five Oxford inputs omit it) — S — 30 Oct — ox.ac.uk is blocked from cloud sessions
- [ ] Find two academic referees: Josh's sheet lists Dirk and Carolyn (both World Bank) and no third — S — 13 Nov
- [ ] Find the transcripts (possibly in a box in the UK); order official copies if not — S — 20 Nov
- [ ] Choose and ask 3 referees (at least 2 academic) — S — 13 Nov — highest risk item
- [ ] Proposal v2: drafted 31 Oct (`C PhD Application/Oxford_DPhil_Research_Proposal_Sovereign_Incentives_Derisking-v2.docx`; changes and open placeholders in `Proposal-v2-ChangeLog.md`). Review it and resolve the [STEPHEN TO DECIDE] and [VERIFY] notes — S — 27 Nov
- [ ] Writing sample: drafted 31 Oct, 1,983 words, cut from 2.1 v0.2 (`C PhD Application/Oxford-WritingSample-ClimateFinanceIntermediation.docx`). Review it; check the Azura paraphrase and decide US or UK spelling — S — 4 Dec
- [ ] Statement of purpose — A drafts, S approves — 11 Dec
- [ ] Submit — S — 8 Jan 2027

### Priority 2: PhD in systemic AI safety (proposal 3)

- [ ] Answer the open questions in `C PhD Application/3-SystemicAISafety-Outline.md` (target programs, supervisors, core question) — S — 6 Nov
- [ ] Literature scan on systemic AI risk; verified sources only — A — 13 Nov
- [ ] First full draft of proposal 3 (~2,500 words) — A drafts, S revises — 27 Nov

### Housekeeping

- [ ] Only one session syncs the master Sheet at a time (two did on 29 Oct and overwrote each other's tabs). Before any Sheet sync, check no other session is mid-sync; at the next sync, confirm Context still has T54-T62 and the Tracker still has C9_m1 — A — next sync

### Priority 3: paper upgrades

- [ ] **Carbon-pricing series (1.1, 1.2, 1.3, 1.6, 1.7): read and approve.** Done 29 Oct by agents: five Climate Fiscal Policy Briefs, five working papers (1.1 v0.3, 1.2 v0.3, 1.3 v0.3, 1.6 v0.2, 1.7 v0.3) with models, proofs, calibrations and literature appendices, five 4-slide decks, all in `B Working Papers/7.Website/papers/` — S reads, starting with 1.1 for Dirk — 5 Nov
- [ ] **Finance-and-risk and sovereign-incentives series (2.1, 2.2, 3.1, 3.2, 3.3): read and peer review.** Done 29 Oct by agents: five briefs (Climate Fiscal Policy Briefs 2.1–3.3) and five working papers with models and verified bibliographies; overviews 2.0 and 3.0 rewritten; CIT moved to 3.2, SLL to 3.3. No decks or peer-review notes yet. Start with 3.1 and 2.1 (proposal 1) — S reads, A peer-reviews and upgrades — 13 Nov
- [ ] Decks for the five series 2–3 papers and two theme decks: done 29 Oct. Referee reports still to do — A — after Stephen's read
- [ ] **Sections 4 (CPAT) and 5 (analytics tools): read.** Done 29 Oct by agents: ten medium-length papers (4.1–4.7, 5.1–5.3) and overviews 4.0, 5.0. Decide whether any country results from the private tools repository may be used; answer the README questions (AI tools used, Egypt figures in 4.3, air-pollution module credit) — S — 13 Nov
- [x] 29 Oct 2026 — Sections 4 and 5: consistency pass, ten paper decks and two theme decks, website pages (ready to deploy); series 3 now leads with the MDB loss record (~80 per donor dollar; 2.7 stress case); TFFF cited to its Concept Note 3.0 — A
- [x] 30 Oct 2026 — Rule on "Draft for discussion" / "Not for citation" sources: Stephen ruled the excise diagnostic's own results usable, PFR and not-for-citation/draft-for-discussion documents excluded. 5.1 v0.3 adds Sierra Leone and Liberia (Section 7); PFR mention and 3.3's draft-for-discussion source (Estevão–Zimmermann surcharge) removed; rule in `4.Modelling/SeriesArchitecture.md` — A
- [x] 30 Oct 2026 — CBAM checks in 4.5 cleared from the Publications Office texts: benchmarks read in Regulation 2025/2620 (rebar is 1.364, not 1.370; example rerun), phase-out read in Directive 2023/959, 2026/1740 and COM(2026) 616 read and cited; 3.2's Vasicek page range confirmed; no markers left in sections 2–5 — A
- [ ] Run render.bat then deploy.bat to put sections 2–5 live — S — after reading
- [ ] Run `deploy.bat` to put the series live (source pushed to main 29 Oct) — S — Fri 30 Oct (T59)
- [ ] Clear remaining `VERIFY` entries in the five working-paper bibs (about 45 across the series; court judgments and EU texts need EUR-Lex, which the cloud cannot reach) — A, with S downloads — 12 Nov
- [ ] Flag: the 1.7 TECP formula in all earlier versions and in the xlsx workbook carries an extra (1−w) factor; v0.3 corrects it and marks the workbook superseded. Rebuild the workbook or retire it — S decides
- [ ] Submit 1.1 to *Climate Policy* (research article) after Stephen's read — S — Nov
- [ ] Confirm which file is master for 1.4 Rent Tax (qmd vs docx, H13) — S — before upgrading it. (1.1 and 1.7: the qmd is master, per Stephen 29 Oct)

## Housekeeping (blocking or risky)

- [ ] **H2: confidential Sustainability-Linked Lending PDF.** Removed from `research.qmd`, `papers/` and `_site/` (29 Oct). Still to do: delete `papers/SustainabilityLinkedLending.pdf` on the web server by hand (deploy.bat syncs without deleting), and remove it from the CV — S
- [ ] H1: rotate the FTP password on the server. The old one is still in git history — S — now
- [ ] H6: fix stale folder paths in `PaperTracker.xlsx` — A

- [ ] Run `B Working Papers/8.Scripts/Run/Download-Literature.bat` on your PC (100 open-access papers the cloud session could not fetch, across all five working papers) — S — Fri 30 Oct (T59)
- [ ] Manual downloads, for later: `B Working Papers/8.Scripts/Reference/Literature-Downloads.md` (125: library login, browser-only or not found) — S — later

## Decisions needed from Stephen

- [ ] Confirm the specialisms and positioning paragraph in `STRATEGY.md`.
- [ ] Confirm the rankings in `PAPERS.md` and the positions P1–P8.
- [ ] Spelling: US for the carbon-pricing series (decided 29 Oct). Other papers: convert, or keep UK?
- [ ] Add 2–3 pieces you are proud of to `A Writing Instructions/Writing Standards/exemplars.md` ("Stephen's own").
- [ ] Is the fiscal unit's remit described correctly in `STRATEGY.md`?

## Done

- [x] 29 Oct 2026 — Abstracts of 1.3 (recommendation, relocation cost of full recognition) and 1.7 (IMF precedent, uses, headline $37) revised; 1.7 brief and deck aligned — A
- [x] 29 Oct 2026 — Carbon-pricing series: briefs, working papers, decks, cross-review, website publish (ready to deploy) — A
- [x] 29 Oct 2026 — Repo combined: planning (0–3) and writing (A–F) under one README/AGENTS — A
- [x] 29 Oct 2026 — `SPECIALISMS.md` written. Stephen decided: "three constraints" through-line yes; AI-risk angle is incentive and institutional design with systemic financial risk as the analogy; politics essays (8.1–8.3) and the *Finding Frodo* deck stay off the academic profile for now — A/S
- [x] 29 Oct 2026 — 4.1 (TECP) moved into the series as 1.7; qmd is master (v0.2) — A
- [x] 29 Oct 2026 — Section 1 reorganised: 1.6 created; `1B.OtherFiscalPolicy` holds 1.4 and 1.5; every series folder has `8.PreviousVersions` with v0.1/v0.2 labels, `3.RelatedPiecesAndLinks` and `RelatedWork.md`; series map in `1.ClimateAndFiscalPolicy/RelatedWork.md` — A
- [x] 29 Oct 2026 — Template paper for 1.1 read (Keen, Parry and Roaf 2021); notes in `1.1/5.Notes/Review-2026-10-29.md` §6 — A
- [x] 29 Oct 2026 — Proposal 1 cleaned: drafting text and appendices B–E removed; original kept in `C Research Proposal/PreviousVersions/` — A
- [x] 29 Oct 2026 — "Today" tab added to the master plan sheet (short daily view) — A
- [x] 29 Oct 2026 — Agent infrastructure set up: `AGENTS.md`, `NORMS.md`, `STRATEGY.md`, `PAPERS.md`, `TODO.md`, `A Writing Instructions/Writing Standards/`, proposals index — A
- [x] 29 Oct 2026 — FTP login removed from deploy scripts (H1) — S
