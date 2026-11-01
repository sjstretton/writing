# TODO.md

The live task list. Agents take work from the top of "Now", mark progress here and commit the change with the work. Move done items to "Done" with the date.

Format: `- [ ] Task — owner — due — notes`. Owner is **S** (Stephen) or **A** (agent).

## Now

### Priority 1: PhD in climate policy (proposal 1, send ASAP)

Details for each item: `B PhD Application/Oxford/PhD-Application-Status.md`.

- [ ] **Next step:** email Dr Shrimali the cleaned proposal; ask him to confirm supervision in writing and about a co-supervisor — S — today (15 min)
- [ ] Settle the deadline on the live Oxford course page. Stephen's working deadline is Sat 31 Oct; the status notes found 13 Nov (early) and 26 Jan (final), unverified. Josh's information sheet (`B PhD Application/Shared/PhD-Information-Sheet.md`, 30 Oct) gives no Oxford date; "before start of November" there is UCL's February-intake rule, the likely source of 31 Oct. Also check whether a statement of purpose is needed (Josh's five Oxford inputs omit it) — S — 30 Oct — ox.ac.uk is blocked from cloud sessions
- [ ] Find two academic referees: Josh's sheet lists Dirk and Carolyn (both World Bank) and no third — S — 13 Nov
- [ ] Find the transcripts (possibly in a box in the UK); order official copies if not — S — 20 Nov
- [ ] Choose and ask 3 referees (at least 2 academic) — S — 13 Nov — highest risk item
- [ ] Proposal v2: drafted 31 Oct (`B PhD Application/Oxford/Oxford_DPhil_Research_Proposal_Sovereign_Incentives_Derisking-v2.docx`; changes and open placeholders in `Proposal-v2-ChangeLog.md`). Review it and resolve the [STEPHEN TO DECIDE] and [VERIFY] notes — S — 27 Nov
- [ ] Writing sample: drafted 31 Oct, 1,983 words, cut from 3.1 v0.2 (`B PhD Application/Oxford/Oxford-WritingSample-ClimateFinanceIntermediation.docx`). Review it; check the Azura paraphrase and decide US or UK spelling — S — 4 Dec
- [ ] Statement of purpose — A drafts, S approves — 11 Dec
- [ ] Submit — S — 8 Jan 2027

### Priority 2: PhD in systemic AI safety (proposal 3)

- [ ] Answer the open questions in `B PhD Application/AI-Safety/3-SystemicAISafety-Outline.md` (target programs, supervisors, core question) — S — 6 Nov
- [ ] Literature scan on systemic AI risk; verified sources only — A — 13 Nov
- [ ] First full draft of proposal 3 (~2,500 words) — A drafts, S revises — 27 Nov

### Housekeeping

- [x] 31 Oct 2026 — **Paper upgrades, sections 1–7, done** (Stephen: work in order, push to main as each is done). Every paper and section overview peer-reviewed, every citation checked, working paper with an executive summary as chapter 1, a short brief as its web page, a deck of about ten slides; all on the website (`WEB_PAPERS`), ready to deploy. Open items from the reviews: 6.1 needs a real-country application; the CBAM tool workbook needs the 6.2 corrections (v1.3); 7.1 Sierra Leone collections to reconcile with the OECD series; 6.3, 6.5 and 7.2 tables rest on saved outputs of the private tools repository (not rerun); 7.2 build to publish. Instructions used: `Writing Standards/paper-upgrade-brief.md` — A
- [ ] **Website restructure (on main since 31 Oct):** run Compile-Website.bat, then check the 1.1 pages: the policy brief is now the paper's page (`E Website/_site/policy/1-carbon-pricing/OpenEconomyCarbonPricing/index.html`) and the working paper is below it (`working-paper.html`); then Push-Website.bat. The two 1.1 `[VERIFY]` markers are resolved (31 Oct) — S — 7 Nov
- [ ] **PDF working-paper format (1 Nov):** look at the 1.1 example (`OpenEconomyCarbonPricing.pdf` and `1.Presentation/Brief-OpenEconomyCarbonPricing.pdf`) and the matching Word files. If you like it, run Compile-Website.bat: it now renders a PDF of every web paper and brief first (`Scripts/Website/render_pdfs.py`; needs Quarto 1.5+, which includes Typst) and the site links PDFs instead of Word files; then Push-Website.bat. Format: `Writing Standards/templates/_extensions/working-paper/` — S — 7 Nov
- [ ] Change the website FTP password: it was committed in the 31 Oct "Restructure" commit (now untracked, but still in git history) — S — soon
- [ ] If the 1.1 web page works, add the other papers to `WEB_PAPERS` in `H Writing Instructions/Scripts/Website/site_config.py` (one line each) — A — after S approves
- [ ] Decks to about eight slides (new norm, `NORMS.md` §8) as each is next revised — A — ongoing

- [ ] Only one session syncs the master Sheet at a time (two did on 29 Oct and overwrote each other's tabs). Before any Sheet sync, check no other session is mid-sync; at the next sync, confirm Context still has T54-T62 and the Tracker still has C9_m1 — A — next sync

### Priority 3: paper upgrades

- [ ] **Paper 2.2 (Let Land Pay for the City): read v0.1.** Then: clear the VERIFY notes in `LandPaysForTheCity.bib` (DOIs, India property-tax figure from the RBI municipal finance report, Banzhaf–Lavery magnitudes, Oates–Schwab full text, Lall et al. page number); decide whether to add a brief and deck; on the website since 31 Oct (run Compile-Website.bat then Push-Website.bat to deploy) — S reads, A clears notes — after the PhD application
- [ ] **Carbon-pricing papers (1.1, 1.2, 1.3, 1.4, and 6.1 the TECP): read and approve.** Done 29 Oct by agents: five Climate Fiscal Policy Briefs, five working papers (1.1 v0.3, 1.2 v0.3, 1.3 v0.3, 1.4 v0.2, 6.1 v0.3) with models, proofs, calibrations and literature appendices, five 4-slide decks, all in `E Website/papers/` — S reads, starting with 1.1 for Dirk — 5 Nov
- [ ] **Finance-and-risk and sovereign-incentives series (3.1, 3.2, 4.1, 4.2, 4.3): read and peer review.** Done 29 Oct by agents: five briefs (Climate Fiscal Policy Briefs 3.1–4.3) and five working papers with models and verified bibliographies; overviews 3.0 and 4.0 rewritten; CIT now 4.2, SLL 4.3. No peer-review notes yet. Start with 4.1 and 3.1 (proposal 1) — S reads, A peer-reviews and upgrades — 13 Nov
- [ ] Decks for the five section 3–4 papers and two theme decks: done 29 Oct. Referee reports still to do — A — after Stephen's read
- [ ] **Sections 5 (CPAT), 6 (modular upgrades) and 7 (analytics tools): read.** Done 29 Oct by agents: ten medium-length papers (5.1–5.4, 6.2–6.5, 7.1–7.2) and overviews 5.0, 7.0 (6.0 added 31 Oct). Decide whether any country results from the private tools repository may be used; answer the README questions (AI tools used, Egypt figures in 5.3, air-pollution module credit) — S — 13 Nov
- [x] 29 Oct 2026 — Sections 4 and 5: consistency pass, ten paper decks and two theme decks, website pages (ready to deploy); series 3 now leads with the MDB loss record (~80 per donor dollar; 2.7 stress case); TFFF cited to its Concept Note 3.0 — A
- [x] 30 Oct 2026 — Rule on "Draft for discussion" / "Not for citation" sources: Stephen ruled the excise diagnostic's own results usable, PFR and not-for-citation/draft-for-discussion documents excluded. 5.1 v0.3 adds Sierra Leone and Liberia (Section 7); PFR mention and 3.3's draft-for-discussion source (Estevão–Zimmermann surcharge) removed; rule in `4.Modelling/SeriesArchitecture.md` — A
- [x] 30 Oct 2026 — CBAM checks in 4.5 cleared from the Publications Office texts: benchmarks read in Regulation 2025/2620 (rebar is 1.364, not 1.370; example rerun), phase-out read in Directive 2023/959, 2026/1740 and COM(2026) 616 read and cited; 3.2's Vasicek page range confirmed; no markers left in sections 2–5 — A
- [ ] Run render.bat then deploy.bat to put sections 1–7 live, then `remove-old-files.bat` — S — after reading
- [ ] Run `deploy.bat` to put the series live (source pushed to main 29 Oct) — S — Fri 30 Oct (T59)
- [ ] Clear remaining `VERIFY` entries in the five working-paper bibs (about 45 across the series; court judgments and EU texts need EUR-Lex, which the cloud cannot reach) — A, with S downloads — 12 Nov
- [ ] Flag: the 6.1 TECP formula in all earlier versions and in the xlsx workbook carries an extra (1−w) factor; v0.3 corrects it and marks the workbook superseded. Rebuild the workbook or retire it — S decides
- [ ] Submit 1.1 to *Climate Policy* (research article) after Stephen's read — S — Nov
- [ ] Confirm which file is master for 2.1 Rent Tax (qmd vs docx, H13) — S — before upgrading it. (1.1 and 6.1: the qmd is master, per Stephen 29 Oct)

## Housekeeping (blocking or risky)

- [ ] **H2: confidential Sustainability-Linked Lending PDF.** Removed from `research.qmd`, `papers/` and `_site/` (29 Oct). Still to do: delete `papers/SustainabilityLinkedLending.pdf` on the web server by hand (deploy.bat syncs without deleting), and remove it from the CV — S
- [ ] H1: rotate the FTP password on the server. The old one is still in git history — S — now
- [ ] H6: fix stale folder paths in `PaperTracker.xlsx` — A

- [ ] Run `H Writing Instructions/Scripts/Papers/Run/Download-Literature.bat` on your PC (100 open-access papers the cloud session could not fetch, across all five working papers) — S — Fri 30 Oct (T59)
- [ ] Manual downloads, for later: `H Writing Instructions/Scripts/Papers/Reference/Literature-Downloads.md` (125: library login, browser-only or not found) — S — later

## Decisions needed from Stephen

- [ ] *Plucked!* has two chapters numbered 13: the short draft *The Global Perspective* (file `13-ThePerfectStormReturns.Rmd`, not in the 2020 book) and *Conclusions*. Drop the draft chapter from the book and site, or keep it and renumber Conclusions as 14? — S

- [ ] Confirm the specialisms and positioning paragraph in `STRATEGY.md`.
- [ ] Confirm the rankings in `PAPERS.md` and the positions P1–P8.
- [ ] Spelling: US for the carbon-pricing series (decided 29 Oct). Other papers: convert, or keep UK?
- [ ] Add 2–3 pieces you are proud of to `H Writing Instructions/Writing Standards/exemplars.md` ("Stephen's own").
- [ ] Is the fiscal unit's remit described correctly in `STRATEGY.md`?

## Done

- [x] 31 Oct 2026 — New working paper 2.2 *Let Land Pay for the City* (property taxes, public land and land value capture for green urban infrastructure in developing countries; Hong Kong and Singapore; green development model and health; best-practice fiscal code), v0.1, about 8,200 words, in `C Policy and FInance/2.OtherTaxAndFiscalPolicy/2.2.LandPaysForTheCity/` (qmd, bib, docx); overview 2.0, `NUMBERING.md`, `PAPERS.md` and the folder index updated — A
- [x] 31 Oct 2026 — Research portfolio slide deck, structured like the website (overview, Part I and II dividers, a divider per section, one slide per paper, books): `A Specialisms, Theory and Research Profile/Slides-ResearchPortfolio.pdf` and `.pptx` (slides as pictures), also in `E Website/papers/` and `PaperArchive/`, linked from the About page. Stephen to run `Compile-Website.bat` then `Push-Website.bat` — A
- [x] 31 Oct 2026 — Tax book 8.5.3 retitled *Plucked! A guide to a fair, simple, efficient and politically feasible tax and benefits system* (was *Screwed?! Getting our future back with tax and benefit reform*): folder now `8.5.3.Plucked`, master `Plucked.qmd`/`.docx`/`.bib`; chapter files, overview 2.0, website pages and scripts, READMEs and `NUMBERING.md` updated; book text otherwise unchanged. Old `papers/Screwed.docx` must be deleted on the server by hand when deploying — A
- [x] 31 Oct 2026 — *Plucked!* readable on the website chapter by chapter (`WEB_BOOKS` in `site_config.py`; pages generated from the master on every compile). Stephen to run `Compile-Website.bat` then `Push-Website.bat`; Push removes the old Screwed.docx itself — A
- [x] 31 Oct 2026 — Papers renumbered to the section folders (`NUMBERING.md`): paper folders, overview files, citation keys (CFPB/StrettonWP), series lines, related-paper lists, decks and the research page now use the new numbers; each section has one `<N>.0.Overview` folder; section 8 renumbered 8.1–8.7; new overviews 2.0 (Rent Tax), 6.0 (modular upgrades) and 8.0; 5.0 and 7.0 rescoped; docx and decks re-rendered; website ready to deploy — A

- [x] 29 Oct 2026 — Abstracts of 1.3 (recommendation, relocation cost of full recognition) and 1.7 (IMF precedent, uses, headline $37) revised; 1.7 brief and deck aligned — A
- [x] 29 Oct 2026 — Carbon-pricing series: briefs, working papers, decks, cross-review, website publish (ready to deploy) — A
- [x] 29 Oct 2026 — Repo combined: planning (0–3) and writing (A–F) under one README/AGENTS — A
- [x] 29 Oct 2026 — `SPECIALISMS.md` written. Stephen decided: "three constraints" through-line yes; AI-risk angle is incentive and institutional design with systemic financial risk as the analogy; politics essays (8.1–8.3) and the *Finding Frodo* deck stay off the academic profile for now — A/S
- [x] 29 Oct 2026 — 4.1 (TECP) moved into the series as 1.7; qmd is master (v0.2) — A
- [x] 29 Oct 2026 — Section 1 reorganised: 1.6 created; `6.Additional/1.OtherFiscalPolicy` holds 1.4 and 1.5; every series folder has `8.PreviousVersions` with v0.1/v0.2 labels, `3.RelatedPiecesAndLinks` and `RelatedWork.md`; series map in `1.ClimateAndFiscalPolicy/RelatedWork.md` — A
- [x] 31 Oct 2026 — Section 4 overview and theme deck revised (80-to-1 headline qualified: 27 net of the default option, carry, liquidity). 5.1–5.4 upgraded (peer review, citations checked, public sources only, executive summaries, first briefs, decks; on the web). 5.1: checked against the public cpat_ai code; default cost of capital corrected; penalty-rule section rebuilt. 5.2: private-repository slide and a 'prototype for discussion' deck removed as sources. 5.3: ex-post comparison put on one basis; documentation errors found (for the CPAT-AI register). 5.4: circular check removed; timing (long-run response in year one) found to be the bigger problem — A
- [x] 31 Oct 2026 — 4.3 upgraded (peer review, citations checked, public sources only, executive summary, brief, 10-slide deck; on the web). Proposition 2 restated (the label premium must cover the policy cost, which explains easy targets); bond-pricing evidence read correctly (Feldhütter et al. 2024); Uruguay, Chile, Thailand facts corrected and Slovenia (2025) added; an unpublished 'for discussion' note cut as a source — A
- [x] 31 Oct 2026 — 4.1 and 4.2 upgraded (peer review, citations checked, executive summary, brief, 10-slide deck; on the web). 4.1: gain net of the default option about 27 per dollar (1.9 stress) beside the 80 budget ratio; Harstad (2016) as the strongest objection; Hess, TFFF and Gabon facts corrected. 4.2: multiplier with carry (about 13 when holding the stress buffer at 2%), liquidity (\$5bn supports about \$390bn without a liquidity line), growth recomputed (\$57bn retired) — A
- [x] 31 Oct 2026 — 2.1 Rent Tax upgraded from an April sketch: peer review, a bibliography of 55 checked sources (none before), working paper v0.2 with an executive summary, a first brief (CFPB 2.1) and deck; on the web. Design corrected: the destination layer is now a sectoral cash-flow tax (was a tax on gross revenue), a cap stops the sales layer exceeding a firm's rent, revenue re-estimated from sourced inputs (land 1.0–2.7% of GDP; corporate layers 2.3–6.3%; was 5.5–11.5% unsourced) — A
- [x] 31 Oct 2026 — 3.2 upgraded (peer review, citations checked, executive summary, brief, 10-slide deck; on the web). Saving corrected from 27% to about a fifth (14–19%): only the 80% senior debt is refinanced at the pool rate; robustness to real-deal cushions (Bayfront 2018) added; closest prior work named — A
- [x] 31 Oct 2026 — 3.1 upgraded (peer review, citations checked, executive summary, brief, 10-slide deck; on the web). Headline corrected: a contract guarantee saves about \$2 per dollar of expected public cost, not \$5.3 (waterfall payments had been counted as recovery); debt guarantee compared on offtaker risk only; single-buyer critique and Zambia/ATI/SECI precedents added — A
- [x] 31 Oct 2026 — 1.3 and 1.4 upgraded the same way (peer review, citations checked, executive summary, short brief, 10-slide deck; on the web). 1.3: one default schedule for every origin, like-for-like import comparison, obligation base 691 Mt, ETS2 delayed to 2028. 1.4: Proposition 3 corrected (a plant keeps only its share of the country's incentive), phase-in tied to the free-allocation factor — A
- [x] 31 Oct 2026 — 1.2 upgraded the same way (`5.Notes/PeerReview-2026-10-31.md`, `BibCheck-2026-10-31.md`): working paper v0.4 (dispatch proposition's condition stated, Fischer 2011 credited for the dominant-firm result, Burtraw et al. 2001 added, a section on why power belongs on the production track, Canada's May 2026 price path), brief v1.1, 10-slide deck; on the web — A
- [x] 31 Oct 2026 — 1.1 upgraded: peer review (`5.Notes/PeerReview-2026-10-31.md`), every cited source checked (`5.Notes/BibCheck-2026-10-31.md`), working paper v0.4 with an executive summary as chapter 1, brief v1.1 rewritten short and plain, 10-slide deck; web build makes a brief page and a working-paper page for each paper — A
- [x] 29 Oct 2026 — Template paper for 1.1 read (Keen, Parry and Roaf 2021); notes in `1.1/5.Notes/Review-2026-10-29.md` §6 — A
- [x] 29 Oct 2026 — Proposal 1 cleaned: drafting text and appendices B–E removed; original kept in `B PhD Application/Oxford/PreviousVersions/` — A
- [x] 29 Oct 2026 — "Today" tab added to the master plan sheet (short daily view) — A
- [x] 29 Oct 2026 — Agent infrastructure set up: `AGENTS.md`, `NORMS.md`, `STRATEGY.md`, `PAPERS.md`, `TODO.md`, `H Writing Instructions/Writing Standards/`, proposals index — A
- [x] 29 Oct 2026 — FTP login removed from deploy scripts (H1) — S
