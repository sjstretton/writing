# Peer review of 5.2, working paper v0.1 (31 Oct 2026)

A referee-style review of *CPAT-AI: Rebuilding a Policy Model as a Transparent, Testable Tool*, working paper v0.1 (29 Oct 2026, about 5,000 words of body), written before the v0.2 revision and the first policy brief (v1.0). Every number in the paper was checked against the public CPAT-AI repository (`cpmodelai/cpat_ai`, public on GitHub; read 31 Oct 2026 from the files of release 1.0.2 kept in `excel_ai/bugs_and_legacy/register/releases/` and from the first commit after the history restart of 30 Oct 2026), and every external source against the source itself (see `BibCheck-2026-10-31.md`).

## Summary judgement

The paper has a clear question (can a large spreadsheet policy model be rebuilt so that every step can be read and tested, and what does the rebuild reveal?) and a clear answer (yes: two rebuilds with shared codes, one register and tests on every output found 228 legacy bugs, 24 of high priority, and the second rebuild found seven bugs in the first). The register counts in Table 1 are right: I recomputed all of them from the release 1.0.2 tracker. The design (the replication rule, shared codes, build twice) is well described and is the paper's real contribution.

Four things keep it below the standard. (i) Several factual statements are wrong or rest on the wrong source, including one example that the register contradicts. (ii) Three sources are not public in the sense the series requires: a slide deck labelled "prototype for discussion" and a slide from the private tools repository carry numbers the paper uses, and one bug count comes from the private repository. (iii) The contribution is stated against spreadsheet-risk and scientific-computing work, but not against the closest prior work on the paper's two central ideas: N-version programming (building twice) and government model quality assurance (the UK's Macpherson review recommends "parallel build"). The strongest objection, common-mode error, is stated, but without the evidence that bears on it (Knight and Leveson 1986; a 2026 replication with AI coding agents). (iv) It has no executive summary, and the claim about the pace AI made possible rests on a counterfactual ("a comparable rebuild by hand would have taken a team many months") with no evidence either way.

## Major points

**M1. One example contradicts the register.** Section 4 says fourteen issues depart from legacy by owner decision, "for example using corrected Egypt electricity prices". The register says the opposite: issue I99 (electricity price data differ from legacy) is *replicated*, closed by the user decision of 29 Oct 2026 to use legacy prices, because legacy 465 already holds the corrected Egypt block. *Fix:* use a real departure, for example I110 (legacy computes subsidies for scenario 1 only; the prototype computes them in every scenario group, with group 1 equal to legacy).

**M2. The equation for the replication rule overstates it.** Section 3.2 says "the rule sets $P(x) = I(x)$ everywhere". It does not: a departure decided by the owner (35 LegacyDiff rows, 14 issues that depart by decision) makes the prototype differ from both legacy and legacy's intention. The closure property, equation (2), is right; the sentence before it is not. *Fix:* $P = I$ except at registered departures; state the closure property as a numbered claim with its conditions (every difference is registered, and codes are never reused).

**M3. Sources that are not clearly public, or are mis-attributed.**

- *The overview deck* (`CPAT-AI_Overview_v1.0.0.pptx`) is in the public repository but its title slide says "prototype for discussion". The series excludes documents marked for discussion. Every number the paper takes from it can be sourced elsewhere: the effects of the high-priority bugs from the bug register, file size from the task log, and the formula count from the task log (497,541 formulas in the 1.1.0 workbook; the deck's 452,164 is for 1.0.0). *Fix:* drop the deck as a source.
- *126 legacy bugs at v0.6.3* comes from a slide in the private tools repository. The public task log gives a different count for the same version: 159 (128 mitigation, 31 distribution) on 20 Oct 2026, and 64 after v0.4.12 on 18 Oct. *Fix:* use the public log's counts.
- *"More than 180 countries"* is cited to Black et al. (2023), which says "over 200 countries". The CPAT documentation says "more than 180". *Fix:* cite the documentation (the series uses "more than 180").
- *"Documented in some 400 pages"* and *"spreadsheet-based with data and formulas readily accessible"* are from the foreword of the CPAT Documentation, not from its mitigation chapter, which the paper cites. *Fix:* add an entry for the documentation as a whole.

**M4. Numbers that do not match their source.**

| Paper v0.1 | Source says | Fix |
|---|---|---|
| "about 250 finished tasks between 2 and 29 October" | The task log has 241 entries dated 2–29 Oct 2026 (269 to 31 Oct) | "241" |
| Road engineer reference reproduces legacy "to 3.8 × 10⁻¹⁴" | Task log: "to 4e-14" | "about 4 × 10⁻¹⁴" |
| "The Python suite has 64 tests" (release 1.0.2p1.1) | 64 at 1.0.0p1.0; 65 at 1.0.2p1.1 (Coded CPAT changelog) | "65" |
| "one task split the remaining 54 plans across five agents" | Not in the public task log (the history was restarted on 30 Oct 2026) | Cut |
| M16: feebate "valued at the diesel truck's distance" | "at the ICEV truck's distance" | "the combustion-engine truck's" |
| "four of CPAT's data tables are proprietary" | Repository: six proprietary tables; issue I90 lists seven tables held for Egypt only in the legacy file without proprietary data | Name the problem, not the number |
| "The independent recomputation of the full mitigation block is being repaired" | The full check runs again since 29 Oct 2026; some power rows added in 0.9.0 have no independent recomputation and are listed as such | Re-word |
| Base-year energy use and CO₂ "agree closely" with legacy | Legacy comparison: in 2022 all 15 CO₂ rows within 5 percent, 91 percent of 129 energy rows within 5 percent; only 48 percent of 128 price rows within 5 percent | Give the numbers |

All other numbers check: 228 legacy bugs (21/42/86 core mitigation; 3/10/16 power engineer; 0/9/8 road engineer; 31 distribution; 1 inputs; 1 data; 24/62/142 by priority); legacy 465 status 52/9/2/165; 22 prototype bugs (21 fixed, 1 withdrawn; 8 suspected by Coded CPAT, 7 confirmed); 20 documentation bugs (3/7/10); 135 issues (109/13/9/4 by area; 35 major, 97 minor, 3 very or extremely high; 93 replicated, 16 limitations, 14 departures, 10 out of scope, 2 other); 35 departures; 14 upgrades (3/4/7); 7,472 reference codes (7,458 with values); 1,684 distribution codes; 123 key codes per stored scenario; 0 of 15,086 codes changed at 1.0.0; 0.8 seconds; 208 power rows; 80 price rows to 5.6 × 10⁻¹⁷; distribution to 4 × 10⁻⁴; 147.0 million (UN WPP 2024, medium variant, 2041, checked in the CSV); eight green-investment bugs among the 24 high-priority ones (L205–L207, L209–L213).

**M5. The contribution needs to be stated against the closest prior work.** Three bodies of work are missing.

- *N-version programming.* "Build it twice" is the old idea of independently developed versions run against each other. Its classic test (Knight and Leveson 1986: 27 versions, one million tests) found far more coincident failures than independence predicts. A 2026 replication with 48 versions written by AI coding agents (Ron, Baudry and Monperrus) again finds substantial common-mode failure, much of it where the specification is ambiguous, but shows that voting across versions still cuts failures sharply. This evidence is exactly what the paper's strongest objection needs, and it cuts both ways: it supports building twice and warns that agent-built versions are not independent.
- *Government model quality assurance.* The UK Treasury's review of quality assurance of government analytical models (Macpherson 2013), written after the West Coast franchise error, found just under 500 business-critical models, and lists "parallel build" among developer testing methods; it recommends quality assurance of inputs, method and outputs and a single senior owner per model. CPAT-AI's design (an owner who decides every departure, a second build, a register) is an instance of that framework, applied to a cross-country policy model by a small team.
- *Open energy and climate models.* Pfenninger et al. (2017) argue that energy-policy models and their data should be open for quality, less duplicated effort and a better science-policy boundary, and list the valid reasons they are not (including data licensing). CPAT's proprietary tables are a case in point (issue I90).

*Fix:* add these to the context section and restate the contribution: not the ideas, which are known, but (a) the replication rule that makes a rebuild faithful and every difference traceable, (b) shared codes that make the second build cheap to compare, (c) counts of what this found in a model in active policy use, and (d) evidence on what AI agents did and did not change.

**M6. The claims about AI productivity need evidence, both ways.** "A comparable rebuild by hand would have taken a team many months" is an unsupported counterfactual. The experimental evidence is mixed: in a controlled task, developers with GitHub Copilot finished 55.8 percent faster (Peng et al. 2023), while in a randomized trial with experienced developers on their own mature projects, early-2025 AI tools made them 19 percent slower, although they believed they were faster (Becker et al. 2025). *Fix:* report what the log shows (241 logged tasks in four weeks; a register of 454 entries), cite both studies, and state the counterfactual as the author's judgement, with the reason (the project had one economist owner and no software team).

**M7. The strongest objection is stated; the answer is too confident.** "Three features limit this risk" is right, but the reader should know the evidence on how far a second, agent-written implementation is independent (M5) and that the second build here was written from the first build's equation list and stored values, which by construction shares the first build's reading of legacy. The answer is the first level of testing (which ties each block to legacy's own cached results, which no agent wrote) and validation (5.3, 5.4). *Fix:* say so.

**M8. No executive summary, and the brief does not exist.** *Fix:* add an executive summary as chapter 1 and write the policy brief (v1.0).

## Minor points

1. The abstract says the rebuild found "seven further bugs in the first rebuild"; the introduction says Python found seven bugs "in the first rebuild" and Table 1 says "8 suspected (7 confirmed)". Keep "seven" and explain the eighth (withdrawn on review, M18) once.
2. The register's counts moved after release 1.0.2: by release 1.1.0 (30 Oct 2026) it held 231 legacy bugs, still 24 of high priority, and still 135 issues. Say once that the paper's numbers are a dated snapshot and give the later total.
3. Repository paths changed on 30 Oct 2026 (`excel_ai/BUGS.md` is now `excel_ai/core/BUGS.md`; the release 1.0.2 tracker and bug document are in `excel_ai/bugs_and_legacy/register/releases/`). The `.bib` URLs point to paths that no longer exist. Cite the versioned release files.
4. "Fuel use in 16 sectors and 8 fuels": the repository's own deck gives both 8 and 9 fuels, and paper 5.1 says "16 end-use subsectors plus power". Use 5.1's wording.
5. Panko (1998) is cited for "people ... rarely catch [errors] by inspection". Its abstract says errors occur in a few percent of cells, so a large spreadsheet's question is how many errors it has, not whether, and that testing after development matters more than development disciplines. Re-word, and add Powell, Baker and Lawson (2008), who show the error-rate estimates are poorly standardized (the counter-evidence).
6. Herndon, Ash and Pollin (2014): the spreadsheet error excluded five countries; the corrected mean growth for debt above 90 percent of GDP (2.2 percent, not −0.1) comes from all three corrections together. State it that way.
7. "Shared codes turn comparison into a join ... the single design decision that made the rest affordable" is the author's judgement; say so.
8. The section on testing calls its four steps "levels" but numbers them as "First ... Fourth" in prose; a small table (level, question, reference, tolerance, what it found) reads faster.
9. Equation numbers are typed by hand; use cross-reference labels so Word and web number them.
10. "The rebuild inherits a structural problem" (road transport): keep the wording agreed across 5.0–5.3 (three descriptions not consistent; issue I100; paper 6.4).
11. The first footnote names colleagues; keep as is (Stephen's decision of 29 Oct 2026).

## What the brief needs

A policy brief for finance ministries, development-bank teams that run CPAT, and anyone who commissions a policy model: what was found (228 bugs, 24 high; the kinds of error), why it matters for decisions (latent bugs fire when a ministry asks a non-default question; verification is not validation), and what to do (require a codes map, keep one register, build twice and regression-test, keep judgment with a named owner, use AI agents as builders under written norms). About 2,000 words, bold lead sentences, one table (the register) and one figure, links into the working paper's sections for the evidence, no equations.

## What the deck needs

The old deck has four slides on the old builder. Target about ten on `make_deck.py`: title and message; the problem (size of legacy, how errors hide); the rule; shared codes and two builds; what the rebuild found (figure); the high-priority bugs (table); the four test levels; building twice found bugs, and the common-mode limit; what AI did and did not do; what to do.

## Disposition

All major points (M1–M8) and minor points (1–11) are addressed in working paper v0.2 and brief v1.0 (31 Oct 2026). The overview deck and the private-repository slide are no longer sources. The counterfactual about pace is stated as the author's judgement with the evidence on both sides.
