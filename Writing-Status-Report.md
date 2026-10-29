# Writing Status Report

Prepared 29 October 2026 for T13 ("PhD application + submit a paper to a journal"). Read-only review: no existing file was changed, moved or deleted.

**Method.** Word counts come from `pandoc`/`pdftotext` and are rough (they include headings, equations and appendices). "Last content change" is the most recent commit that added or modified the file, following renames (`git log --follow --diff-filter=AM`). The plain `git log` date is **2026-10-16** for almost every file, because commit `a5920cc "Folder changes"` renamed 734 files, so that date tells you nothing. "Maturity" and "Readiness" come from `B Working Papers/9.ResearchTracking/PaperTracker.xlsx` (as at 17 Sep 2026). "Status" is my own reading of the files.

---

## 1. Inventory

### A Geoprosperity Overview

| Item | Format | Words | Last content change | Status |
|---|---|---|---|---|
| Geoprosperity_WorkingPaperSeries | docx | ~3,300 | 2026-09-30 | Pitch document for the whole series. It lists 1.1–3.2 and still uses the old 1.3 title |
| Canva-GraphicalOverviewOfIdeas | pdf (+ Canva .url) | ~4,800 | 2026-09-16 | Visual overview |

### B Working Papers — active portfolio (sections 1–5)

| No. | Title (as in master file) | Folder | Master format(s) | Words | Last content change | Tracker maturity / readiness | Status (my reading) |
|---|---|---|---|---|---|---|---|
| 1.0 | Overview: Climate and Fiscal Policy | `1.ClimateAndFiscalPolicy/` | docx | 1,800 | 09-17 | ++ / 4 | Section overview |
| 1.1 | Open Economy Carbon Pricing: A Trade-Based Framework… | `1.1.OpenEconomyCarbonPricing` | qmd + .bib, docx, tex | 4,000 (+8,900 consumption-tax background paper) | qmd 05-11; docx 09-17 | ++ / 5 | **Draft with a literature review and 41 references.** Formal appendices A–D, but the models are sketches |
| 1.2 | Feebates and Output-Based Rebating | `1.2.FeebatesAndOutputBasedRebating` | qmd, docx | 6,700 | 09-17 | ++ / 2 | Full draft. The qmd is a raw Word conversion (bold headings, images inside headings, manual table of contents) |
| 1.3 | *Research page:* "Iron, Steel, CBAM and the Limits of Point-Source Carbon Pricing". *Actual file:* "Carbon Price Recognition under CBAM" | `1.3.IronSteelCBAM` | qmd, docx | 3,300 | 09-17 | ++ / 5 | Near-final **consultation submission** to the European Commission, not a journal paper. Content does not match the title or abstract (see H3) |
| 2.0 | Overview: Mobilising Private Capital | `2.FinanceAndRisk/` | docx | 3,100 | 09-17 | ++ / 4 | Section overview |
| 2.1 | Climate Finance Intermediation for Clean Power | `2.1.ClimateFinanceIntermediationForCleanPower` | qmd, docx | 4,400 | 09-17 | +++ / 5 | Good policy draft with **no citations** (merged from three sources) |
| 2.2 | The Climate Investment Trust | `2.2.ClimateInvestmentTrust` | qmd, docx | 4,200 | 09-17 | +++ / 5 | Good policy draft. Has a References heading but no citation keys |
| 3.0 | Overview: Sovereign Incentives | `3.SovereignIncentives/` | docx | 2,300 | 09-17 | ++ / 4 | Section overview |
| 3.1 | Notional Capitalised Value and Guarantees | `3.1.NotionalCapitalisedValueAndGuarantees` | README only | 70 | – | + / 1 | **Idea.** It has an abstract on the research page but no draft |
| 3.2 | Sustainability-Linked Lending at the World Bank | `3.2.SustainabilityLinkedLending` | pdf only (17 pp.) | 6,700 | 09-16 | ++++ / 2 | Near-final, but it is a **World Bank internal discussion paper marked "Confidential"** (see H2). Not a journal candidate |
| 4.0 | Overview: Modelling | `4.Modelling/` | docx | 1,500 | 09-17 | ++ / 4 | Section overview |
| 4.1 | The Total Effective Carbon Price (folder: PolicyEquivalentCarbonPriceAndCES) | `4.1.PolicyEquivalentCarbonPriceAndCES` | qmd, docx, tex, xlsx (+TECP.tex) | 4,100 | qmd 05-11; docx 09-17; TECP.tex 09-30 | ++++ / 4 | **Technically complete draft** (derivation, calibration, implementation). Literature and references are almost absent |
| 4.2 | CPAT: Architecture, Recoding, Fiscal Application | `4.2.CPATArchitectureRecodingAndFiscalApplication` | README + background (qmd/pdf/xlsx) | 0 for the master (~13,000 + 15,000 in background) | 09-17 | ++ / 1 | **Notes and background only.** No master document |
| 5.0 | Overview: Analytics | `5.Analytics/` | docx | 900 | 09-17 | ++ / 4 | Section overview |
| 5.1 | Automated Excise-Fiscal Reports | `5.1.ExciseFiscalDiagnostic` | qmd, docx | 24,800 | 09-17 | ++ / 5 | Long technical report (Sierra Leone application). Report-length rather than paper-length |

### B Working Papers — 6.Additional (retained and outside portfolio)

| No. | Title | Format | Words | Status |
|---|---|---|---|---|
| 1.4 | Rent Tax | qmd, docx, tex, pdf | 4,000 | Full draft. The abstract is in the index but not in the paper |
| 1.5 | Stranded by Contract: Legacy Coal PPAs | background only | 0 (India notes ~33,000 / 6,000) | Notes |
| 2.3 | The Sollar | qmd, docx | 3,000 | Draft. The `2.Source` copy is a different, older 1,500-word version |
| 3.3 | SLIDIs | qmd, docx | 6,900 | Draft. Superseded by 3.2 and 2.2 |
| 3.4 | MDB Climate Envelope | qmd, docx | 11,000 | Draft with a large background set |
| 3.5 | Reforming MDBs | qmd, docx | 2,800 | Short draft |
| 4.3 | CBAM Dashboard and Emission Factors | xlsx + guides | ~7,200 (guides) | A tool, not a paper |
| 5.2 | Climate-Fiscal-Financial | README + Trillions to Billions background | ~4,900 (background) | Notes |
| 5.3 | Green Growth and Sectoral TFP | README | 60 | Idea |
| 5.4 | Carbon Pricing: Political Economy and Optimality | 2 pdfs | ~3,800 | Notes / toy model |
| 6.1 | Time and Chance (book) | qmd, docx | 50,000 (+37,000 working papers) | Full manuscript, with a response to peer review |
| 6.2 | Carbon Pricing: Right Policy, Wrong Time (book) | qmd, docx | 15,000 | Full manuscript |
| 7.1 / 7.2 / 7.3 | Order Without Ordinance / Politics of Life-Logic / The Vocative Case | qmd, docx | 11,700 / 4,700 / 8,800 | Philosophy drafts |
| 8.1 / 8.2 / 8.3 | Manifesto / NineEleven / Voting Patterns | qmd, docx (+tex) | 700 / 2,500 / 6,700 | Politics pieces |
| 6.0, 9.0 + section overviews 6–8 | Combined and section overviews | docx | 700–4,200 | Overviews |

### Cross-check: tracker vs research.qmd vs files

- The research page lists 11 papers: 1.1–1.3, 2.1–2.2, 3.1–3.2, 4.1–4.2 and 5.1. That is **11, not the 10 the tracker records**. 3.1 and 4.2 are listed with abstracts but have no paper.
- The tracker says the "Outside portfolio" items are "not published". However, `7.Website/papers/` and `_site/papers/` contain Manifesto, NineEleven, VotingPatterns, TimeAndChance, the philosophy essays, RentTax and others. Because `_quarto.yml` publishes `papers/**`, these are probably publicly reachable even though no page links to them (unverified).
- Every folder path in the tracker is stale. Examples: `6.OverviewAndAdditional\9.AdditionalPapers\…`, `3.SovereignIncentivesAndMDBs\…`, `0.Website`, `7.Scripts`. Its Key also says it lives at "the root of A Writing".

---

## 2. Housekeeping problems (listed only, nothing fixed)

Ordered by priority.

| # | Problem | Where |
|---|---|---|
| **H1** | **The FTP host, username and password are committed in plain text.** The `.gitignore` entry meant to exclude `deploy.bat` points at the old `A Writing/7.Website/deploy.bat` path, so it protects nothing. If the GitHub repo is public or shared, the password should be rotated and the file untracked. | `B Working Papers/7.Website/deploy.bat`, `7.Website/batch/deploy.bat`, `.gitignore` |
| **H2** | **A document marked "Confidential — Internal Discussion Draft" (World Bank, March 2026) is published on the public site.** It is linked from `research.qmd` and from `CV-UnpublishedWorks.docx`. | `3.2.SustainabilityLinkedLending/SustainabilityLinkedLending.pdf`, `7.Website/papers/`, `_site/papers/` |
| **H3** | **Paper 1.3: the title and abstract do not match the content.** `research.qmd`, the Geoprosperity overview, the CV and the tracker all describe a paper on scrap-based steel and opportunity-cost adjustment. The master file is "Carbon Price Recognition under CBAM", a consultation submission that mentions scrap only twice. | `1.3.IronSteelCBAM/*`, `7.Website/research.qmd` |
| H4 | The root `README.md` and `AGENTS.md` name folders that no longer exist: "B Research and Website", "C Research Proposal", "D Climate Econ Course" and "E Templates and Info". The actual folders are B Working Papers, C Climate Econ Course, D Templates and Info and E Research Proposal. AGENTS.md points to `B Research and Website/7.Website`. | `README.md`, `AGENTS.md` |
| H5 | Old paths are hard-coded in about 20 automation scripts and in `.gitignore`: `A Writing`, `0.Website`, `0.Overview`, `7.Scripts`, `9.Scripts`. The Start-Day/End-Day workflow will probably fail or act on the wrong paths (not tested, because they are Windows `.bat`/`.ps1` files). | `8.Scripts/Run/*.bat`, `8.Scripts/Steps/*.ps1`, `8.Scripts/Engine/*.ps1`, `8.Scripts/Reference/README.md`, `_PaperFolderLayout.md` |
| H6 | All folder paths in the paper tracker are stale (see the cross-check above). | `9.ResearchTracking/PaperTracker.xlsx` |
| H7 | There is a second `PaperTracker.xlsx` (plus `PaperReadiness.xlsx`), and it differs from the master. The tracker's own Key says there should be only one copy. | `F Claude + Scripts/Claude outputs/` |
| H8 | Stale "Contents to move in here" note. It lists four CPAT xlsx files to move in. Three of them are now in `4.2/9.Archive` and one is at the 4.2 root. Separately, the 4.2 README says all four belong at the top level. | `4.2/3.BackgroundPapers/AIAssistedCPATRecodingNotes/README.md`, `4.2/README.md` |
| H9 | Two "This folder can be deleted once you are satisfied nothing was lost" folders are still present. The first also refers to a "2.4 Equity De-risking" paper that has since been absorbed into 2.2. | `2.1/8.PreviousVersions/SyntheticSovereignBonds/`, `2.2/8.PreviousVersions/StandardizedTwoStage/` |
| H10 | Folder READMEs carry old numbers and titles: the 5.4 folder's README is titled "5.3 Instrument Diagnostic"; 5.2's is titled "5.6 … Dashboard"; FiscalLongTermStrategy says "4.5"; the 3.1 README cites "3.3 Climate Investment Trust" (now 2.2). Several say "Abstract in research.qmd" for papers that are no longer on that page (5.2, 5.3, 5.4, 4.5). | READMEs in `6.Additional/5.Analytics/*`, `4.2/…/FiscalLongTermStrategy`, `3.1` |
| H11 | Broken references in 4.1: it cites `@labandeira2017` and `@stern2012`, but there is no `bibliography:` field and no `.bib` file, so the References section renders empty. | `4.1/PolicyEquivalentCarbonPriceAndCES.qmd` |
| H12 | 1.1 has text and reference defects: a truncated sentence ("…demonstrate that customs-based climate policy"), a misspelt bib key (`Pauwlyn2007`), and references to "Part I/II/III", which the paper does not have. | `1.1/OpenEconomyCarbonPricing.qmd` |
| H13 | The qmd and docx versions have diverged. For 1.1, 4.1 and 1.4, the qmd was last changed in May 2026 and the docx in September 2026, and the word counts differ (1.1: 4,030 vs 3,690). It is unclear which file is the master. `Sync-Masters.ps1` retires a docx older than its qmd, so check before running it. | 1.1, 4.1, 1.4 |
| H14 | Mislabelled or stub copies in `2.Source`: 2.1's `2.Source` docx has 564 words against the master's 4,366, and 2.3's `2.Source` copy is an older version. | `2.1/2.Source`, `2.3/2.Source` |
| H15 | Messy conversions: 1.2's qmd has bold or image headings and a manual table of contents. 5.1's qmd has a duplicated "Contents" heading. | `1.2/…qmd`, `5.1/…qmd` |
| H16 | Generated output is tracked: `7.Website/_site/` and `8.Scripts/Reports/*.txt`. AGENTS.md tolerates this only if it is deliberate, and the `.gitignore` entry for Reports points to the old `A Writing/9.Scripts/Reports/` path. | `_site/`, `8.Scripts/Reports/` |
| H17 | The section overviews (x.0) are loose files at section level, while the tracker gives them folder paths. | `1.0`, `2.0`, `3.0`, `4.0`, `5.0` |

---

## 3. Papers closest to journal submission

The 2.x papers are good, but they are uncited policy proposals, so they fit policy outlets and briefs better than peer review. 3.2 is confidential internal material. 1.3 is a consultation response. 5.1 is report-length. That leaves two candidates.

### Recommendation 1 (primary): 1.1 Open Economy Carbon Pricing

Why this one: it is the only portfolio paper with a structured literature review, a complete working bibliography (all 41 citation keys resolve to the `.bib`), and formal appendices. At about 4,000 words it is within the article-length limits of the journals below.

| Journal | Fit | Verified? | URL |
|---|---|---|---|
| **Climate Policy** (Taylor & Francis) | All aspects of climate mitigation policy, accessible style, judged on policy relevance. Article types: research article (7,000 words), policy analysis (5,000), viewpoint (3,000). The journal invites short pre-submission summaries. | Yes (journal page) | https://www.tandfonline.com/journals/tcpo20/about-this-journal |
| Economics of Energy & Environmental Policy (IAEE) | Policy-oriented. Listed topics include climate policy instruments, emission trading, and taxation and fiscal policy. | Yes (IAEE scope page) | https://iaee.org/publications/eeep/eeep-aims-and-scope |
| Journal of Environmental Economics and Policy (T&F) | Applied environmental economics with clear policy recommendations. It excludes purely theoretical work and requires "Key Policy Highlights", so the models would need some quantification. | Yes (journal page) | https://www.tandfonline.com/journals/teep20/about-this-journal |

An alternative for the WTO/destination-basis angle is *World Trade Review* (CUP), https://www.cambridge.org/core/journals/world-trade-review. The journal exists, but its fit with trade-and-environment topics is **unverified**: the search did not confirm it. It would need the WTO appendix written out in full.

**What is left before submission:**
1. **Verify every bib entry.** I spot-checked two and could not find either: `Summerfield2019` ("Carbon Footprint Pricing at the Retail Level", *Ecological Economics*) and `VogtSchilb2022` ("Carbon Pricing on Electricity Bills", *Energy Economics*). Treat both as possibly non-existent until they are checked. Several others look doubtful and should also be checked: `ElectriciteDeFrance2019`, `MoranWood2020` (title and venue), `Brandi2023`, and `BoehringerLange2005` (cited for feebates). Remove or replace anything that cannot be found.
2. Fix the H12 defects. Give a source for, or remove, the unsourced claim that "feasible prices remain in the €30–€60/tCO₂ range". The same applies to the "10% / 2–3%" transfer example.
3. Turn Appendix A/B "Results 1–4" into stated propositions with their conditions. For example, revenue neutrality of the feebate needs a fixed output mix, and "no leakage" needs a consumption charge equal to the embodied emissions. As written, they are asserted rather than derived.
4. Decide what happens to the 8,900-word Carbon Consumption Tax background paper: cut it to a short appendix or leave it out. The tracker suggests splitting. Appendix D (WTO) is currently three sentences: either expand it or cut it.
5. Choose the article type. A Climate Policy *policy analysis* has a 5,000-word cap, which suits the current length. Add policy highlights, apply journal formatting (the qmd already uses Chicago author-date), and write a cover letter.
6. Check the employer's rules on outside publication. The paper carries a World Bank affiliation and disclaimer, and the clearance requirement is not verified here.

**PhD writing sample:** 1.1, once steps 1–3 are done, because it shows a literature review, argument and formal modelling. 4.1 is the more technical alternative.

### Recommendation 2: 4.1 The Total Effective Carbon Price

Why this one: the tracker rates it "most complete" (++++). It contains a full derivation, a CES demand model, partial adjustment, calibration and implementation, and it has a clear contribution relative to the OECD Effective Carbon Rate and the IMF effective carbon price.

| Journal | Fit | Verified? | URL |
|---|---|---|---|
| **Energy Economics** (Elsevier) | Economic and econometric modelling of energy systems. Scope was confirmed only through aggregator sites, because ScienceDirect is blocked from this session. | Exists; scope **partly verified** | https://www.sciencedirect.com/journal/energy-economics |
| Energy Policy (Elsevier) | Papers must explicitly address policy issues in energy supply or use, including the effectiveness of market-based approaches. | Yes (Elsevier shop listing) | https://shop.elsevier.com/journals/energy-policy/0301-4215 |
| Climate Policy (T&F) | Comparing instruments across countries suits its "wider lessons" emphasis. | Yes | https://www.tandfonline.com/journals/tcpo20/about-this-journal |

**What is left before submission:**
1. Create a `.bib` and add the `bibliography:` field (H11). Write a short literature section that positions the paper against the OECD ECR, the IMF ECP and the policy-equivalence or shadow-price literature. Only use sources he has actually checked.
2. Source the calibration table, which is titled "…from the empirical literature" but cites nothing. Show the arithmetic behind the worked example's "roughly $75".
3. Add at least one real country application. CPAT or the Sierra Leone excise data are possible bases. Energy Economics and Energy Policy reviewers will expect empirical content, not only a framework.
4. Reconcile the qmd (May), the docx (September) and `TECP.tex` (30 September), and decide which is the master (H13).

The realistic timeline for 4.1 is 4–8 weeks, against 2 weeks for 1.1. That is why 1.1 comes first.

---

## 4. Order of work for the next 2 weeks (29 Oct – 12 Nov 2026)

| When | Task | Output |
|---|---|---|
| Day 1 | **H1:** rotate the FTP password and untrack `deploy.bat`. **H2:** take the confidential SLL PDF off the site, `research.qmd` and the CV. | Repo and site safe |
| Day 1–2 | **H3:** retitle 1.3 or restore the scrap paper. **H4/H6:** fix README, AGENTS.md and tracker paths (about an hour). | Consistent index |
| Day 2–4 | 1.1: verify all 41 references one by one (step 1) and fix the H12 defects. | Clean bibliography |
| Day 4–5 | Email Climate Policy a short pre-submission summary of 1.1 (the journal invites this). Decide between policy analysis and research article. | Scope check |
| Week 2, days 6–8 | 1.1: write the propositions in Appendix A/B, source or cut the unsourced numbers, and settle the consumption-tax appendix and Appendix D. | Submission draft |
| Week 2, days 9–10 | Check the employer's publication-clearance rules. Write the policy highlights, cover letter and formatting. **Submit 1.1**, or send it to the fallback journal (EEEP) if the editor's reply suggests poor fit. | Submitted |
| Background, ~1 hr/day | 4.1: create the `.bib` and source the calibration table. Pick the data for a country application. | Ready for a December push |
| Defer | H5 script paths, H7–H10 and H13–H17. Run `Audit-Papers.bat` (read-only) once H5 is fixed. | – |

**Sources used for journal checks:**
- [Climate Policy – aims and scope](https://www.tandfonline.com/journals/tcpo20/about-this-journal)
- [JEEP – aims and scope](https://www.tandfonline.com/journals/teep20/about-this-journal)
- [EEEP – aims and scope](https://iaee.org/publications/eeep/eeep-aims-and-scope)
- [Energy Policy – Elsevier](https://shop.elsevier.com/journals/energy-policy/0301-4215)
- [Energy Economics – aggregator listing](https://www.editage.com/research-solutions/journal/energy-economics/13247)
- [World Trade Review – author instructions](https://www.cambridge.org/core/journals/world-trade-review/information/author-instructions)
