# TODO.md

The live task list. Agents take work from the top of "Now", mark progress here and commit the change with the work. Move done items to "Done" with the date.

Format: `- [ ] Task — owner — due — notes`. Owner is **S** (Stephen) or **A** (agent).

## Now

### Priority 1: PhD in climate policy (proposal 1, send ASAP)

Details for each item: `C Research Proposal/PhD-Application-Status.md`.

- [ ] **Next step:** email Dr Shrimali the cleaned proposal; ask him to confirm supervision in writing and about a co-supervisor — S — today (15 min)
- [ ] Settle the deadline on the live Oxford course page. Stephen's working deadline is Sat 31 Oct; the status notes found 13 Nov (early) and 26 Jan (final), unverified. Also check documents and the statement-of-purpose limit — S — 30 Oct — ox.ac.uk is blocked from cloud sessions
- [ ] Choose and ask 3 referees (at least 2 academic) — S — 13 Nov — highest risk item
- [ ] Proposal v2: narrow scope, name data sources, sharpen hypothesis — A drafts, S approves — 27 Nov
- [ ] Writing sample: cut 2.1 to ≤2,000 words — A drafts, S approves — 4 Dec
- [ ] Statement of purpose — A drafts, S approves — 11 Dec
- [ ] Submit — S — 8 Jan 2027

### Priority 2: PhD in systemic AI safety (proposal 3)

- [ ] Answer the open questions in `C Research Proposal/3-SystemicAISafety-Outline.md` (target programs, supervisors, core question) — S — 6 Nov
- [ ] Literature scan on systemic AI risk; verified sources only — A — 13 Nov
- [ ] First full draft of proposal 3 (~2,500 words) — A drafts, S revises — 27 Nov

### Priority 3: paper upgrades

- [ ] **1.1 Open Economy Carbon Pricing → paper standard** (Dirk asked for this first). Short version (v0.2) is now the master `1.1/OpenEconomyCarbonPricing.qmd`; v0.1 in `8.PreviousVersions`. Next: Stephen reads it; verify every `VERIFY` entry in the bib; calibrate the steel illustration from CBAM default values; then expand to the 7,000-word research article per `5.Notes/Plan-v2-TwoTrackArchitecture-2026-10-29.md` — A — 12 Nov
- [ ] Decisions taken 29 Oct: title "Price Production and Consumption Separately: A Two-Track Architecture for Carbon Pricing in Open Economies"; consumption-charge revenue partly replaces VAT, with a forward-announced upstream liability as the preferred form; the consumption-tax paper is 1.6 (moved 29 Oct); 1.3 keeps its content (CBAM flaws incl. price recognition, plus scrap-shuffling solutions): retitle to match; US spelling for the series
- [ ] Confirm which file is master for 1.4 Rent Tax (qmd vs docx, H13) — S — before upgrading it. (1.1 and 1.7: the qmd is master, per Stephen 29 Oct)
- [ ] Draft concept paper 1: policy-equivalent carbon price — A — after 1.1

## Housekeeping (blocking or risky)

- [ ] **H2: remove the confidential Sustainability-Linked Lending PDF from the website**, `research.qmd` and the CV — A — now — conflicts with publishing rules
- [ ] H1: rotate the FTP password on the server. The old one is still in git history — S — now
- [ ] H3: resolve the 1.3 title/content mismatch — S decides, A edits
- [ ] H6: fix stale folder paths in `PaperTracker.xlsx` — A
- [ ] H5: update old paths in `8.Scripts` and `.gitignore` — A — before anyone runs the scripts again

- [ ] Run `B Working Papers/8.Scripts/Run/Download-Literature.bat` on your PC (23 free papers the cloud session can't reach) — S — when convenient
- [ ] Manual downloads, for later: `B Working Papers/8.Scripts/Reference/Literature-Downloads.md` (41: library login, browser-only or not found) — S — later

## Decisions needed from Stephen

- [ ] Confirm the specialisms and positioning paragraph in `STRATEGY.md`.
- [ ] Confirm the rankings in `PAPERS.md` and the positions P1–P8.
- [ ] Spelling: US for the carbon-pricing series (decided 29 Oct). Other papers: convert, or keep UK?
- [ ] Add 2–3 pieces you are proud of to `E Writing Standards/exemplars.md` ("Stephen's own").
- [ ] Is the fiscal unit's remit described correctly in `STRATEGY.md`?

## Done

- [x] 29 Oct 2026 — 4.1 (TECP) moved into the series as 1.7; qmd is master (v0.2) — A
- [x] 29 Oct 2026 — Section 1 reorganised: 1.6 created; `1B.OtherFiscalPolicy` holds 1.4 and 1.5; every series folder has `8.PreviousVersions` with v0.1/v0.2 labels, `3.RelatedPiecesAndLinks` and `RelatedWork.md`; series map in `1.ClimateAndFiscalPolicy/RelatedWork.md` — A
- [x] 29 Oct 2026 — Template paper for 1.1 read (Keen, Parry and Roaf 2021); notes in `1.1/5.Notes/Review-2026-10-29.md` §6 — A
- [x] 29 Oct 2026 — Proposal 1 cleaned: drafting text and appendices B–E removed; original kept in `C Research Proposal/PreviousVersions/` — A
- [x] 29 Oct 2026 — "Today" tab added to the master plan sheet (short daily view) — A
- [x] 29 Oct 2026 — Agent infrastructure set up: `AGENTS.md`, `NORMS.md`, `STRATEGY.md`, `PAPERS.md`, `TODO.md`, `E Writing Standards/`, proposals index — A
- [x] 29 Oct 2026 — FTP login removed from deploy scripts (H1) — S
