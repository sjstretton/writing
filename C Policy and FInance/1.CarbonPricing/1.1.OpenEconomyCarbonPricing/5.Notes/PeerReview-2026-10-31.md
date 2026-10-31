# Peer review of 1.1, working paper v0.3 and policy brief v1.0 (31 Oct 2026)

A referee-style review of both forms of 1.1 before the v0.4 working paper and v1.1 brief. The earlier reviews (`Review-2026-10-29.md`, `PeerReview-and-WPOutline-2026-10-29.md`) were of v0.2; most of their points are fixed in v0.3. This review is of what is there now.

## Summary judgement

The working paper has a clear question, a clear answer and a defensible contribution: a revenue-neutral feebate on production intensity plus a destination charge on consumption, with closed-form results on cost, crediting and exporter incentives, calibrated to the EU's default values for steel. It is close to the paper standard. The main problems are one proposition whose condition is misstated (Proposition 7), several small errors, about thirty citations whose metadata was confirmed but whose content was never checked against the claim, two calibration parameters without sources, and a missing non-technical summary. The brief is accurate in substance but is not a brief: at about 3,600 words with equations, propositions and a proofs appendix, it duplicates the working paper instead of summarizing it.

## Major points

**M1. Proposition 7 needs its real condition.** The proposition says each exporter's most competitive feebate rate equals the importer's charge, when the charge is levied on actual intensity. But if the importer charges each plant on its own verified intensity, the exporting firm already faces the marginal incentive $\tau$ on the units it ships, and chooses $e = e_0 - \tau/k$ without any policy at home. The home feebate then adds nothing for exported output. The proposition has bite in two cases, both important: (a) when the importer charges a value per country and sector (a default or a standardized value updated from verified national data), which no single firm can move, so only a national policy lowers the charge; and (b) when firms sell at home and abroad from the same plants, where a feebate extends the incentive to all output and leaves nothing to shuffle. Case (a) is exactly what the companion paper on CBAM recommends [CFPB14]. *Fix:* state Proposition 7 for a charge on the exporting country's sector intensity, and add a remark on plant-level charges.

**M2. The closest precedents need to be named and the contribution re-stated against them.** Holland (2012) is cited. Böhringer, Rosendahl and Storrøsten (2017) on output-based rebating combined with a consumption tax as a leakage policy should be checked and, if it says what I expect, cited as the closest precedent for Proposition 1. The contribution then rests on (i) the revenue-neutral, updated-benchmark feebate that needs no emissions trading system, (ii) the consumption track inside VAT, (iii) the closed-form cost and its calibration, (iv) crediting and (v) the country-level exporter incentive.

**M3. The paper needs a non-technical executive summary.** A finance-ministry reader will not get past the model. Add an executive summary as chapter 1 (plain words, no equations, the steel numbers), and link it to the policy brief.

**M4. Calibration parameters need sources.** The base price of \$600/t and the Armington elasticity of 4 are marked VERIFY. Both drive the race-to-the-top figures. Either source them or present them as stylized with a sensitivity check.

## Minor points

1. Section on equivalence: "Three qualifications matter" is followed by four. Change to four.
2. Proposition 3 in the brief gives the price ratio as $\Delta e / 2e_0$ (15 percent for a 30 percent cut). The working paper has it right: $\Delta e/(2e_0 - \Delta e)$, about 18 percent. The brief's stylized \$15 against \$85 is 17.6 percent, so the brief contradicts its own example.
3. The brief says carbon pricing covers "about a quarter" of global emissions; the 2025 *State and Trends* says about 28 percent. The deck says "~25%". Use 28 percent everywhere.
4. Cross-references between the forms are plain text ("A short version is Climate Fiscal Policy Brief No. 1.1"; "the companion paper shows"). On the website they should be links: from the brief into the working paper's sections for derivations and evidence, and from the working paper back to the brief.
5. The introduction lists four contributions; the literature section claims five. Make them one list.
6. The brief's stylized example ($e_0 = 2$, $p_0 = \$600$, $t = \$50$) differs from the working paper's calibration (EU default values, \$80/t). Use the calibrated numbers in the brief and the deck so that one set of numbers runs through the series.
7. "Net of what generators have already paid" (electricity): under a revenue-neutral feebate generators pay nothing net on average, so the deduction is zero on average. Say so, or the reader will think there is double payment to net out.
8. The model treats the feebate benchmark as the realized average; the implementation section says "the output-weighted average of the previous period". Both are fine, but say which the propositions assume and what the lag does (a one-period lag gives a small temporary net charge or rebate while intensity falls).
9. The crediting proposition assumes output is fixed. Under the feebate the output change is second order, so the result holds to first order; say so in one clause.
10. Appendix A repeats much of the related-literature section. Keep the appendix for the detail and the challenge table; shorten the section in the text to the gap.
11. The working paper's first line says "A short version is Climate Fiscal Policy Brief No. 1.1". Make it a link to the brief on the website.

## Citations

Two background checks were run on every source whose content had not been read, and on the new candidates. Their findings, and the changes made, are recorded in `BibCheck-2026-10-31.md`. Sources that could not be confirmed to say what the text claims are either re-worded to what they do say, replaced with a verified source, or cut.

## The brief

The brief should be the plain-language form: about 2,000 words, no equations, the lead sentence of each paragraph in bold (World Bank style), one figure, one table of numbers, a "What to do" section, and links into the working paper for the derivations and evidence. Its abstract and its "What to do" can stay close to the current text. The proofs appendix, the propositions and the design table move out (the working paper already has them).

## The deck

Four slides is too few for a paper with five results. Target about ten: title and message; the problem in numbers; why one price cannot do both jobs; the two tracks; what the feebate costs (the steel table); crediting; from leakage to a race to the top; design and objections; what to do; the series. Each slide carries one message in its title.

## Disposition

All major and minor points are addressed in working paper v0.4 and brief v1.1 (31 Oct 2026). See the version notes at the top of each master.
