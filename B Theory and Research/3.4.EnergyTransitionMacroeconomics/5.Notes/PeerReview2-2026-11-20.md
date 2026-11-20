# Referee report on Note 3.4, v0.2 (20 November 2026)

Independent referee report on *The Energy Transition Swaps a Fuel Bill for a Capital Bill* (Theory and Research Note No. 3.4, v0.2; master saved 14:06 UTC; 31-page PDF).

## What I checked, and how

1. I read the master, all 31 PDF pages as images, every bibliography note, the four evidence files, the two literature files, the script, its output and CSVs, the house rules and writing standards, the v0.1 review, and the passages of briefs 3.1, 3.2 and 4.3 that the note quotes.
2. I ran a scratch copy of `egypt_estimates.py` against the tools repository (macro models not re-run). It reproduces the first 180 lines of the output file and all eight CSVs exactly. Numbers marked "my re-run" come from extra lines added to that scratch copy. No file in the note folder or the tools repository was changed.
3. I checked about 80 cited claims against the bibliography notes and the evidence record, and every Egypt number in the executive summary, Sections 5 to 8 and Appendix B against the output file.
4. Works I name as missing were each confirmed today on Crossref (DOI lookup or title search). One abstract (Hirth and Steckel) was read on OpenAlex. Queries used titles, authors and DOIs only.

## Summary judgement

1. v0.2 is a different and much better paper. It is now a literature review: the body is about 6,350 words on 12 pages, the modelling sits in Appendix B, the products take one paragraph and one table, and the critics of de-risking are quoted. Every Egypt number I traced matches the output file to rounding, the tables add up, and the note and its source folder are in step.
2. The page budget is met. The executive summary runs 1.4 pages (pp. 2–3). The body runs 11.5 pages (pp. 4–15).
3. It is not yet at the standard of a careful working-paper series, for six reasons. (a) The review of expectations stops short of optimal policy, which is what the author asked for (M1). (b) The second-best pricing section leaves out the public-finance second best and gives no level or conditions (M2). (c) Seven of the author's own points are thin or missing (M3). (d) Four pieces of economics need repair: the cost of waiting, the guarantee ratio, the external accounts, and the comparison of rates across currencies (M6–M9). (e) The note states an evidence standard that about twenty citations do not meet, a dozen of them materially and one of them flagged in the v0.1 review (M12). (f) The Egypt headline is a bound that no product delivers, on a gas price taken from a war-spike half-year (M13).
4. Of the eleven major points in the v0.1 review (its own M1 to M11), I count its M1, M3, M8 (mostly), M10 (mostly) and M11 as fixed, and its M2, M4, M5, M6, M7 and M9 as partly fixed. The specific leftovers are listed under the points below.

## A. Fit to the brief

### Coverage of the author's points

| Author's point | Where treated | Verdict |
|---|---|---|
| Electrification of a fuel-based system | Fact 1; Section 3 ¶1–2 | Adequate |
| Renewables are always run | Fact 4; Section 3 ¶4 | Curtailment covered. Missing: zero marginal cost lowers the price renewables earn as their share rises, which is the link to long contracts |
| Long investment needs long contracts | Fact 17; Section 6 ¶1 | Adequate |
| Carbon pricing volatile and often reversed | Fact 9; Section 4 ¶4 | Thin: one episode (EU, 2026), no price range, no count of reversals |
| Carbon pricing works for spot changes | Fact 8; Section 4 ¶1 | Adequate |
| Investment takes a long time | Facts 6, 30 | Adequate |
| Fuel price rises are unpopular | Fact 10 | Adequate |
| Cross-sectoral; dual-level expectations of reversible situations | Fact 14; Section 4 ¶5 | Thin: one paragraph, two sources, no coordination literature |
| Energy costs and risks are material | Fact 24; Section 3 ¶6 | Adequate |
| Renewables cheap; storage roughly doubles cost | Fact 5 | Adequate; two slips (C2, C3) |
| Cost of capital and fiscal space | Fact 18; Section 6 ¶2 | Adequate |
| Preferred creditor status and low expected loss | Fact 20; Section 6 ¶3 | Adequate; the step from this to the products is not made (M7) |
| Grid is strategic: "How can we quantify this?" | Section 3 ¶5 | Half answered: three methods, one Egypt number, no benefit-cost ratio, no grid row in Table 4 |
| 50/50 local versus China; fine; comparable to energy infrastructure | Fact 26; Section 7 ¶3 | Thin and unsourced (C1); the comparison is one sentence with no number |
| GDP impact front-loaded | Fact 27; Section 7 ¶1 | Rests on the author's model and one IEA sentence |
| Currency swaps, south-south, Indian credit market | Fact 22; Section 6 ¶5 | Thin; India is absent; the product was dropped; the rate comparison is unsound (M9) |
| De-risking, the SECI model | Fact 21; Section 6 ¶4 | Thin: two sentences, the institution is never named |
| GDP impact potentially huge (IEA) | Section 7 ¶1 | Adequate |
| Net cost negative, more so de-risked | Fact 28 | Adequate |
| De-risking may be near free | Section 6 ¶4 | Treated; the ratio is unsound (M7); better evidence sits unused in the record |
| Public pension funds | Fact 23; Section 6 ¶5 | Missing in substance: two sentences, "theory only" |
| State-owned enterprises dominant | Fact 19; Section 6 ¶1 | Adequate; the consequence for carbon pricing is not drawn |
| Effectiveness is in switching | Fact 3 | Adequate |
| Second best: politically and fiscally feasible | Fact 15; Section 5 | Political side adequate; fiscal side thin (M2) |
| Fossil fuel consumption is fungible | Fact 16; one row of Table 2; Section 8 | Thin: no paragraph in the body and no number |
| Overall: may come too late even if it pays | Section 8 ¶2 only | Absent from the executive summary |
| Expectations of long-run relative prices and investment, and optimal policy under uncertainty | Section 4 | Good review; no bridge to optimal policy (M1) |
| Diminishing versus increasing returns | Section 4 ¶7; Figure 1 | Partly argued (M5) |
| Cost of waiting | Section 4 ¶6; Section 7 ¶6; Appendix B | Treated; economics needs repair (M6) |
| Capacity from outside consortia | Section 7 ¶5 | Under-argued (M3) |
| Simple products, the author's own | Section 6 ¶6; Table 3 | Simple: yes. Own: not set against existing instruments (M7) |
| Lead-in to a global green deal | Section 8 ¶3 | Present, one paragraph |
| Egypt imports gas now | Executive summary; Table 4; Appendix B | Done |

### Major points

**M1. The review of expectations never reaches optimal policy.** Section 4 reviews option value, credibility and time inconsistency well. Section 5 then starts from the first-best price as if Section 4 had not been written. The author asked for "the importance of expectations of long term relative prices and of investment in determining optimal climate policy in uncertain contexts". Four things are missing.

1. *Instrument choice under uncertainty.* Weitzman (1974) is in the note's bibliography and is not cited. Add it with Roberts and Spence (1976) and Pizer (2002): under uncertainty a hybrid (a quantity with a price floor and ceiling) beats either pure instrument. That is the theory behind rule 4.
2. *The optimal path under uncertainty.* Daniel, Litterman and Wagner (2019) find that with risk aversion and learning the optimal price starts high and falls. Dietz and Venmans (cited) find it starts high and rises. A reader needs one sentence on why they differ.
3. *Optimal policy without commitment.* The note states the problem (Kydland and Prescott; Helm, Hepburn and Mash; Kalkuhl and others) and not the answer. Harstad (2020) and Acemoglu and Rafey (2023) model policy without commitment directly: expected future taxes drive investment today, and investment in technology becomes the means of commitment. Fried, Novan and Peterman (2022) show that the mere risk of a future price moves capital today. Lemoine (2017) is in the bibliography, unused: the evidence file records that anticipated pricing raised emissions.
4. *A number.* The sentence "a carbon price that a later government can reverse is discounted by investors" (executive summary ¶3) can be quantified in one line: a price P that is repealed with hazard h a year is worth P·r/(r+h) to an investor with discount rate r. At r = 8 percent and h = 10 percent, 44 cents on the dollar (my arithmetic). Put that next to rule 5.

Also separate two things the section runs together. The private investor's reason to wait (¶3, policy risk) is a risk of transfer, with no social counterpart. The planner's reasons (¶6) are real. That wedge is the best argument for the state to carry policy risk by contract, and the note does not make it. Arrow and Lind (1970) is the standard reference.

For "dual-level expectations" (¶5), the natural literatures are absent: Murphy, Shleifer and Vishny (1989) and Cooper and John (1988) on complementarity, and Li, Tong, Xing and Zhou (2017) and Springel (2021) on chargers and electric cars. Confirm with the author that "dual-level" means policy and system, as the note reads it.

**M2. The second-best pricing section is sound as far as it goes and stops early.** Table 2 is the best thing in the note. Five gaps.

1. *The public-finance second best is absent.* For a finance ministry, second-best carbon pricing means first the interaction with other taxes: Bovenberg and de Mooij (1994), Bovenberg and Goulder (1996), Goulder (1995), Barrage (2020). For developing countries add Bento, Jacobsen and Liu (2018) on informality and Dorband and others (2019) on incidence. "Fiscally feasible" is in the author's brief and has no literature behind it here.
2. *No level.* The section gives the first-best range and the price in force, and never says what a pragmatic price or path is, or how it moves with the cost of capital. Hirth and Steckel's abstract says it: countries with dear capital need a higher carbon price for the same result. Say so, and show Egypt's whole effective price under rule 1.
3. *Rule 2 does not fit a gas system.* "Price operations where the capital already exists" rests on Britain's switch from coal to gas. Egypt's power is 76 percent gas. State the condition: a cleaner plant must be idle and available.
4. *Rule 6 contradicts Section 4.* "Announce the sequence" follows a section that shows announcements are discounted, and Section 8 says "investors discount announcements". Reword as "legislate and contract the sequence".
5. *State companies.* Section 6 cites Kornai on soft budgets. The consequence belongs in Table 2: under a single state buyer with tariffs below cost, a carbon price on power lands in the utility's deficit and reaches neither dispatch nor demand.

Add to each rule the condition under which it fails, as the paper standard asks.

**M3. Seven of the author's points are thin or missing.**

1. *SECI (Section 6 ¶4).* Two sentences, and the Solar Energy Corporation of India is never named. The record has the mechanism (back-to-back contracts; the agreement that lets the Reserve Bank of India debit a state's account; a payment security fund; a margin of Rs 0.05–0.07 a unit) and a risk (some state agreements expire in October 2026). Write one paragraph: what it removes, what it costs, what it does not fix. The margin, 2 to 2.5 percent of the tariff, is the cleanest evidence in the file for "near free".
2. *The 50/50 split (Section 7 ¶3; fact 26).* The author's claim is about who gets the GDP benefit, that the split is fine, and that it matches conventional energy infrastructure. The note turns it into an import share, supports it with three numbers that are not in the record (C1), and gives the comparison one sentence. Source the import shares, give the import content of a gas plant or of investment in general, and argue "fine" (cheap equipment is a terms-of-trade gain; the local half is construction, grids and installation).
3. *South-south swaps and the Indian credit market (Section 6 ¶5).* India does not appear. Egypt's renminbi bond of 2023, guaranteed by two development banks, is the closest case to the author's idea; it is in the bibliography (`AIIB2023Panda`) and unused. State the mechanism and its limit: a swap does not make money cheap, since a hedged rupee or renminbi loan costs about the dollar rate. The gain is access, a match with equipment priced in the supplier's currency, and central-bank liquidity. Bahaj and Reis ("Jumpstarting an International Currency") study exactly the renminbi swap lines.
4. *Pensions (fact 23).* The v0.1 review's request, "do the check or drop the fact", is still open, and the README still lists pensions as undecided. The record has Egypt's treasury payments to the social insurance fund (EGP 238.55 billion in 2025/26). The literature exists: Inderst and Stewart (2014) and Della Croce and Yermo (2013) on pension funds and infrastructure; Barr and Diamond (2006) for the caution that funding alone does not raise saving.
5. *Fungibility (fact 16).* No paragraph in the body. The record already holds Harstad (cited), Fæhn and others (2017), and the Erickson and Lazarus citation. Add Böhringer, Balistreri and Rutherford (2012) for model ranges, and say what fungibility means for a gas importer such as Egypt: saved imports lower the world price a little and leave Egypt's gain intact.
6. *Grid quantification (Section 3 ¶5).* The output file answers the author's question and the note does not use it. Grids and storage cost $23 per megawatt-hour of extra wind and solar at the local rate, against $101 of fuel and running cost saved. On my re-run, the grid for one year's additions costs $0.3–0.4 billion a year, and a year's delay in connecting them burns $1.8 billion of gas: about five to one. Add a grid row to Table 4.
7. *Outside consortia (Section 7 ¶5).* One paragraph, resting on one project's debt share. The record has a full example (trade press, one source each): the Suez wind farm, with a Chinese contractor and turbine maker and six development lenders. Say what a consortium is, why program-scale tenders lower cost, and what the risks are. The paragraph also undercuts itself: agreements for 17.4 gigawatts in 2027–28 are 8.7 a year, above the path's 7.5.

Put the overall message, "a transition that pays may still come too late", in the executive summary. It was the author's closing point and the v0.1 review asked for it.

**M4. The indicators are three lists that do not meet, with no theory.** Section 3 ¶6 names four indicators. Section 4 ¶8 names six proxies. Table 4 gives ten. One item (cost of capital) is common to them. Apart from that item, none of the four or the six has an Egypt value. The author asked for "macroeconomic indicator theory". Give one table. Define each indicator by an identity (for example: external effect = fuel saved − imported equipment − interest on program debt; energy bill = fuel bill + capital charge). Say what a ministry should read from each, and date every Egypt value. Several rows of Table 4 have no year (interest at 73 percent of revenue is fiscal 2024/25; the evidence file's own ratio for 2025/26 is 95 percent).

**M5. The returns contrast still rests on a functional form, and the "mix" is not shown.** (Section 4 ¶7; Figure 1; executive summary ¶4.) Partly fixed since v0.1: the terms are defined and the spillover is stated.

1. Figure 1 still has two panels on different axes. The left panel is a constant-elasticity curve extended to $353, about three times the highest price ($125) that the v0.1 review says the author's own study observes.
2. "Returns to scale" is the wrong term for a price. The standard statement is: with technology fixed, the marginal cost of abatement rises; with cumulative deployment, unit cost falls.
3. The left panel has no backstop. Once the price passes the point at which an electric car is cheaper, the response is large, so returns to price are not diminishing there. Deployment lowers that point. That is the precise form of the author's argument. Goulder and Mathai (2000) is the reference for abatement whose cost falls as it accumulates.
4. The note has the numbers to show the mix and does not: a 30 percent cut in road fuel by price alone needs $350 a tonne (Figure 1); the Egypt run cuts transport emissions at −$134 a tonne in 2035 (Appendix B). Set them side by side.
5. The learning evidence is read one way. Grubb and others are cited for causation from deployment. Nordhaus (2014), Nemet (2006) and Kavlak, McNerney and Trancik (2018) are the critical side. For one country the world's learning curve is a reason to wait for others. The national increasing return is local: the record has IRENA's learning rates for Africa (21.9 percent solar, 9.6 percent wind) and the note already cites Egli and others on lenders' experience.
6. Logic: rising marginal cost is not a market failure. The abstract's "therefore" (price has diminishing returns, so the first-best price is a benchmark) does not follow. The spillover does the work.

**Minor (A).**

1. The products are simple. They are not shown to be the author's own. Section 6 ¶6 says they "differ in three ways" from current practice and does not name the nearest existing instruments. The record has three: the World Bank guarantee behind Argentina's renewable fund, Scaling Solar, and the Regional Liquidity Support Facility (all [S]: read them first).
2. Table 3 renames each product without giving the source paper's name (payment intermediary facility; synthetic sovereign bonds; Climate Investment Trust). The house norm is one term across papers.
3. "For the third, $3.3 billion of guarantee capacity is worth $772 million to a government" needs "at a saving of 300 basis points" (brief 4.3).
4. The green-deal paragraph does not say what a global green deal is. One sentence, and Nordhaus (2015) on climate clubs, would do.
5. "Renewables are always run": add Hirth (2013) on falling capture prices.
6. "Volatile and often reversed": give a price range and more than one reversal from sources that were read.

## B. Economics

**M6. The cost of waiting confuses the discount rate with the financing rate.** (Section 7 ¶6; Section 8 ¶2; Appendix B "The cost of waiting"; fact 31.)

1. The lead "A high discount rate hides the cost of waiting" is not what the numbers show. Both figures ($6 billion and $32 billion) use the same 6 percent discount rate. What separates them is the financing rate. On my re-run, moving the discount rate from 3.9 to 8.2 percent moves the cost of waiting from $44 billion to $23 billion (de-risked) and from $8 billion to $5 billion (local). The output file's own "investor" lines for local financing give +$5 billion for all sectors and +$16 billion for power and transport, against +$6 billion and +$23 billion at 6 percent. "Sees little loss in waiting" is not supported.
2. The headline present values embed a financing gain and loss. Annuitizing capital at 3.9 percent and discounting at 6 percent values a dollar of 25-year capital at 81 cents; at 8.2 percent, at $1.22 (my arithmetic). With capital at par (financed and discounted at 6 percent real), the program is worth +$51 billion and waiting costs $20 billion (my re-run). The note's −$14 billion and +$108 billion sit either side of that. "The difference is finance" is true by construction. Report the par case as the benchmark.
3. Say that 6 percent is real, where it comes from (a public source), and why it lies above the de-risked borrowing rate. "6 percent" is also the nominal de-risked rate, so one number names two things.
4. The de-risked case charges nothing for the risk moved to the guarantor and the state. That makes +$108 billion an upper bound. Say so in Section 8.
5. With local financing the program as a whole has a negative present value, so delaying it "costs a further $6 billion" only because it nets $23 billion lost in power and transport against $16 billion gained elsewhere. Lead with power and transport.
6. The answer to the falling-cost objection is incomplete (Section 4 ¶6; Appendix B). Waiting a year saves the price fall and also a year's return on the outlay. The rule is to build when the first year's saving exceeds (r + rate of price fall) × cost. For one year's additions in 2030 that is $1.15 billion at the local rate against $1.8 billion of gas (my re-run). The result holds, by a margin of about 1.6 to 1, not the 6 to 1 or more that "a few percent cheaper" suggests. Dixit and Pindyck, already cited, give the rule.
7. "Of which $35 billion is in power and transport" of a $32 billion total: a part larger than the whole. Write "$35 billion lost in power and transport, less $3 billion gained elsewhere".

**M7. The comparison of expected loss with interest saved is not sound.** (Section 6 ¶4, "De-risking is cheap and not free".)

1. The two halves of the ratio come from different worlds. The 1.4 points is brief 3.1's premium for a utility that defaults about once in six to seven years. The 0.4 percent expected loss uses a default rate of 2.61 percent a year on development-bank loans to public borrowers. A utility that seldom defaults would not carry a 1.4-point premium.
2. Brief 3.1's own ratio for the same guarantee is 2.0 dollars saved per dollar of expected cost (3.6 with better recovery), on an expected cost of 0.6 percent of capital a year. The note cites 3.1 and reports "about four".
3. Exposure is not defined. The saving is per dollar of capital. The loss is per dollar guaranteed. A guarantee of a year's payments exposes about an eighth of the capital; a termination guarantee exposes all of it. The ratio runs from about 4 to about 30 on that choice alone (my arithmetic).
4. The loss record is for loans, which enjoy lenders' seniority in practice. A power contract's payments are delayed far more often than a development bank's loan is defaulted on.
5. Expected loss is not the cost. The premium that investors charge is expected loss plus a price for bearing risk. If the guarantor loses less because it is paid first, part of the saving is a transfer from other creditors. The v0.1 point that senior claims raise the cost of the borrower's other debt is still missing. Only Gabor's general caution stands in for it.
6. The step from preferred creditor status to the three products (executive summary ¶6: "follow from the facts") is not made. Brief 3.1 says of earlier claims that the arrangement was outside the debt stock and protected by the World Bank Group's preferred creditor status: "neither claim survives scrutiny, and this paper drops both". State whether each product carries a counter-guarantee from the government. If yes, the sovereign record applies and the whole liability is the state's. If no, preferred status does not apply.
7. Better evidence is in the record and unused: MIGA has paid no claim for breach of contract or non-honoring of public debt, and SECI's margin is 2 to 2.5 percent of the tariff.
8. Two v0.1 requests remain open: the saving per dollar of capital used, and the size of the buffer fund for Egypt.
9. "It removes the whole risk premium" (Section 6 ¶6) means the offtaker premium, 1.4 points, a third of the 4.3-point gap in Appendix B. As written it reads as the whole gap.

**M8. The external-account reasoning is a lower bound, and the fiscal J is not shown.** (Section 7 ¶3; Table 1; Appendix B "Time path and external accounts"; Figure 3.)

1. The calculation counts only equipment imports, on an assumed share of one-half. Section 7 ¶5 says Egypt saves 8 percent of GDP and that the finance must come from outside. If so, the local half is foreign-financed too. On my re-run, with all capital spending financed abroad and fuel savings used to repay, the effect on the external balance turns positive in 2044 at the local rate (program debt reaches 57 percent of GDP by 2045) and in 2035 de-risked (debt peaks at 34 percent in 2040). The note reports 2034 and 2032, and 7–8 percent. Show both bounds. They make the note's case better than the current figure does: the cost of capital decides whether the external accounts recover.
2. By 2035, interest at the local rate on all program spending ($282 billion) is $23 billion a year, the same size as the fuel saved ($23.9 billion) (my arithmetic). The title is literal at the local rate. Say so.
3. The measure leaves out imports induced by the local half, and the identity that the current account is saving less investment.
4. All saved gas is valued at the import price. On my re-run the path saves 10 billion cubic meters in power and industry in 2030, 26 in 2035, 51 in 2040 and 88 in 2045, against net imports of 21 in 2025 and output of 42. Through the 2030s the saved gas is plausibly all imported. In the 2040s it exceeds any plausible import volume, and the right value is the export netback or domestic cost. The present values to 2050 are affected. Show the gas balance.
5. "A J-curve in the external and fiscal accounts" (Table 1). No fiscal path is shown. The only fiscal numbers rise: budget need 2.2 percent of GDP in 2030 and 2.5 percent in 2035 at the local rate. Lost fuel tax and saved subsidy are not estimated for Egypt. Show a fiscal path or drop "fiscal".
6. "Energy moves from the current account to the balance sheet" (four uses). Interest paid abroad is in the current account. The exact statement is: from the trade balance to the income balance and the external balance sheet.
7. The note proposes guarantees to the power buyer while Egypt's IMF program cuts guarantees to the state oil company by a quarter (evidence file, Egypt item 24). Flagged in v0.1 and still unanswered.

**M9. Rates are compared across currencies, dates and types without adjustment.** (Section 6 ¶5; Table 4; Appendix B "The two rates".)

1. Section 6 ¶5 sets Treasury bills at 26 percent beside yen bonds at 2.9–3.5 percent and concludes "money in the supplier's currency can be cheap with a guarantee". Inflation is 13.9 percent, so the real bill rate is about 11 percent. Yen rates are low because yen inflation is low; unhedged yen debt is not cheap in pounds or dollars. The evidence file itself warns "this is not currency-adjusted". Japan is also not the supplier of Egypt's solar equipment.
2. "Local" means two things: the dollar cost of capital for a project in Egypt (Appendix B) and Egyptian-pound money (Section 6).
3. The real-terms fix from v0.1 is done and correct (10.3 and 6.0 percent nominal, less 2 percent, give 8.2 and 3.9). Three problems remain. The local rate is a 2020 figure and the de-risked rate a November 2026 one; dollar base rates were near zero in 2020 and the reference rate is 3.90 percent now, so at constant spreads the local rate today is several points higher. The de-risked rate floats and the local rate is a fixed project return. And the upper end of the IBRD range (6.0 percent) is pricing group D; the record could not map Egypt to a group, and the other groups pay 5.4 to 5.8 percent.
4. One rate is applied to private solar, the state grid, factories, boilers and cars. The note concedes the de-risked rate is "a bound". Say the same of the local rate for the grid, which the state already finances on sovereign terms.
5. A decomposition would help: base rate, sovereign spread, project and offtaker premium, each from a public source.

**M10. The carbon-price equivalent of de-risking is computed correctly and interpreted too broadly.** (Section 5 rule 5; Appendix B "What the sectors show".)

1. The arithmetic is right: $19–20 per megawatt-hour divided by 0.446 tonnes per megawatt-hour gives $43–46.
2. It is the equivalent of full de-risking, from a project return to a sovereign loan rate. Rule 5 does not say so. A payment guarantee alone closes 34 percent of the gap (output file), about $15 a tonne. Plain solar without grids gives $22 (output file).
3. "Worth as much to the investor" is wrong for a plant on a fixed-price contract, which gains nothing from a carbon price. It is the same cost gap between new clean power and gas-fired power.
4. A carbon price also changes dispatch and demand and raises revenue. De-risking does none of these and creates a contingent liability.
5. The house series defines a carbon-price equivalent as the tax that cuts emissions by as much. In the model the power mix "follows target dates and does not respond to the cost of capital", so no emissions equivalent can be computed. Call this a cost-parity equivalent.
6. By the note's own Section 4, a carbon price that may be repealed is worth less than its face value. The equivalent believed price is therefore higher than $45. That strengthens rule 5 and joins the two halves of the note.

**M11. The macroeconomic reading is selective in places, and a specialist will miss several works.**

1. Section 7 ¶1: "The split has a pattern ... its sign turns on the cost of capital" is the note's thesis stated as a finding, with no source. A demand-led gain needs slack. Egypt has financing needs of 42 percent of GDP and a current account deficit above 4 percent. The two models in Appendix B differ by a factor of six (0.9 and 5.6 percent), one reaching +33 percent by 2050. "They agree on the sign" is thin. Name the model types and cite their public originals (Kumhof and others 2010; Berg, Buffie and others 2012; Marto, Papageorgiou and Klyuev 2018).
2. "Much more in developing ones" (executive summary ¶7; fact 25) has no GDP share behind it, and the record holds a contrary figure (C15).
3. The monetary paragraph (Section 7 ¶4) is three sentences. Del Negro, di Giovanni and Dogra (2023) is the obvious addition.
4. The damage range "$31 to $185" is two point estimates. Moore and others (2024) and Bilal and Känzig (2024) report much higher values.
5. Missing works, by subject. All confirmed on Crossref today unless noted.
   - Instrument choice and timing under uncertainty: Roberts and Spence (1976, *Journal of Public Economics* 5); Pizer (2002, *Journal of Public Economics* 85); Daniel, Litterman and Wagner (2019, *PNAS* 116); Harstad (2020, *Journal of Political Economy* 128); Acemoglu and Rafey (2023, *Journal of Public Economics* 219); Fried, Novan and Peterman (2022, *European Economic Review* 147); Gollier (2024, *JEEM* 128); Arrow and Lind (1970, *American Economic Review* 60; Crossref returns the reprints).
   - Coordination: Murphy, Shleifer and Vishny (1989, *JPE* 97); Cooper and John (1988, *QJE* 103); Li, Tong, Xing and Zhou (2017, *JAERE* 4); Springel (2021, *AEJ: Economic Policy* 13).
   - Public-finance second best: Bovenberg and de Mooij (1994; Crossref returns the reprint); Bovenberg and Goulder (1996; Crossref returns NBER Working Paper 4897 and the reprint); Goulder (1995, *International Tax and Public Finance* 2); Barrage (2020, *Review of Economic Studies*); Bento, Jacobsen and Liu (2018, *JEEM* 90); Dorband, Jakob, Kalkuhl and Steckel (2019, *World Development* 115).
   - Learning: Goulder and Mathai (2000, *JEEM* 39); Nordhaus (2014, *Energy Journal* 35); Nemet (2006, *Energy Policy* 34); Kavlak, McNerney and Trancik (2018, *Energy Policy* 123).
   - Value of renewables: Hirth (2013, *Energy Economics* 38).
   - Cost of capital and de-risking: Steffen (2020) and Calcaterra and others (2024), both in the evidence file and unused; Egli, Steffen and Schmidt (2019, *Nature Communications* 10); Steckel and Jakob (2018, *International Economics* 155); Perraudin, Powell and Yang (2016, Inter-American Development Bank working paper) on preferred creditor status and ratings.
   - Leakage: Böhringer, Balistreri and Rutherford (2012, *Energy Economics* 34); Erickson and Lazarus (2014, *Nature Climate Change* 4).
   - Currency and swap lines: Eichengreen, Hausmann and Panizza (2007, in *Capital Controls and Capital Flows in Emerging Economies*); Bahaj and Reis (2022, *Review of Economic Studies* 89; and "Jumpstarting an International Currency", listed by Crossref in the same journal, 2026).
   - Pensions: Barr and Diamond (2006, *Oxford Review of Economic Policy* 22; Crossref lists Barr only); Inderst and Stewart (2014, World Bank Policy Research Working Paper 6780); Della Croce and Yermo (2013, OECD working paper; Crossref lists the title without authors).
   - Macroeconomics: IMF (2020), *World Economic Outlook*, October, chapter 3; Del Negro, di Giovanni and Dogra (2023, SSRN record); Moore and others (2024, *PNAS* 121); Bilal and Känzig (2024, NBER Working Paper 32450; Crossref also lists *QJE* 141, 2026); Nordhaus (2015, *American Economic Review* 105); Adrian, Bolton and Kleinnijenhuis (2022, IMF Working Paper 22/107).

**Minor (B).**

1. Section 4 ¶1 cites emission cuts of 5 to 21 percent. The same source gives 4 to 15 percent after correcting for publication bias (bibliography note). Use both.
2. Executive summary ¶5: "a price set too low costs more than one set too high" is credited to the second-best literature. It is one result on errors of belief in a standard model.
3. Section 4 ¶7: Way and others are cited without the standard objection (continued learning is assumed).
4. Appendix B: the gas heat rate (7.95 gigajoules per megawatt-hour) is a fleet average. Wind and solar displace the marginal plant.

## C. Accuracy

**M12. Twenty-two claims fall short of the standard the note sets for itself; a dozen matter.** The introduction says "a source is cited for a number only where its text or abstract was read for this note". I checked about 80 cited claims across all sections and both appendices. About 60 match the record. Mismatches follow, with the most serious first.

| # | Location | Claim | What the record says |
|---|---|---|---|
| C1 | Section 7 ¶3; fact 26 | Modules and inverters about 35 percent of solar cost; turbines about three-quarters of wind cost; China over 75 percent of batteries (IRENA 2025) | None of the three is in the bibliography note (which records only $691 per kilowatt) or in any evidence file. The finance file says "Batteries and wind turbines: NOT FOUND" and "Capex split ...: NOT FOUND". The battery figure was flagged in v0.1 |
| C2 | Fact 5 | Shifting half of solar output "adds $33–43 per megawatt-hour" | Adds about $33, giving $76 against $43 for solar alone. $43 is the cost of solar |
| C3 | Fact 5; Section 3 ¶4 | "Solar in every hour costs $104" | $104 gets "97% of the way" in Las Vegas; "cloudier sites reach far less" |
| C4 | Appendix B "The two rates"; Table 4 | "IRENA reports 9.7 percent in nominal dollars for solar power in Egypt ... and a benchmark of 8.8 percent" | Both evidence files: Egypt's value NOT FOUND in the report. The bibliography note: read from a third-party database held in the tools repository. "Dollars" is recorded nowhere |
| C5 | Appendix B "A check against contracts" | Contracts at 2.4–2.5 cents "with sovereign guarantees and development-bank debt" | The two projects with a tariff show "Not stated" for the guarantee. The one with a guarantee and such debt has no disclosed tariff. Flagged in v0.1 |
| C6 | Section 5 rule 4 | "A floor makes the price harder to reverse" (Wood and Jotzo) | The record has three ways to build a floor and nothing on reversal |
| C7 | Section 5 rule 6 | "The price rises on a path set in law" (three sources) | Not in the record for any of them |
| C8 | Table 2, last row | In industry "leakage has not been found after the fact" | "No consistent evidence of significant emissions leakage" (medium evidence, medium agreement). Appendix A has it right |
| C9 | Section 3 ¶5 | van der Weijde and Hobbs treat a line "as an option, whose value rises with uncertainty" | Stochastic planning; the cost of ignoring uncertainty is about £100 million for Great Britain. The stylized-facts file lists option valuations as NOT FOUND |
| C10 | Table 2, row 3 | Hirth and Steckel: at 15 percent "almost none" | The bibliography note has only the 3 percent case; the 15 percent case is [S]. It is correct (abstract read on OpenAlex today). Update the note |
| C11 | Section 6 ¶1 | Policy schemes, "mostly auctions" | The passage read gives 84 percent for policy schemes. The auction share is [S] |
| C12 | Section 6 ¶4 | "About 42 gigawatts more were awarded with no distributor signing", of India's intermediary | The record gives 42 gigawatts awarded without sale agreements and speaks of "implementing agencies" in the plural. It does not say the figure is this institution's alone |
| C13 | Executive summary ¶5 | Paris-consistent prices "are $50 to $100 by 2030" | "At least" (kept in Section 5; the quotation there matches the source) |
| C14 | Executive summary ¶5; Section 5 ¶1 | Damage estimates "run from $31 to $185" | $31 is in 2010 dollars for 2015; $185 is in 2020 dollars with a 5–95 percent range of $44–413 |
| C15 | Executive summary ¶7; fact 25 | Investment "much more in developing ones" | The cited report "gives no share of GDP" (bibliography note). The finance file records a World Bank average of 1.4 percent of GDP, above 5 percent in poorer countries |
| C16 | Section 5 ¶2 | Lipsey and Lancaster, for four specific conditions | "Citation metadata only" |
| C17 | Section 6 ¶4 | A development bank "holds capital against a guarantee as against a loan" (present tense) | A 2014 source; "Whether this still holds in 2026 was not checked" |
| C18 | Section 5 rule 4 | A contract "cut the break-even price ... from about 93 euros to 66" | A model case study, not an event |
| C19 | Section 4 ¶7; fact 11 | "Supported" by the author's unpublished paper and a constant elasticity | The learning file: "the rising-marginal-cost half: NOT FOUND". An assumed curve is not evidence. Verdict should read "by assumption" |
| C20 | Section 4 ¶7 | Gillingham and Stock: cheap "once the fall in cost they cause is counted" | The abstract names spillovers; "learning" is marked NOT CONFIRMED |
| C21 | Table 4 | "61 gigawatts against 40" | 60.8 gigawatts and a 38-gigawatt peak are fiscal 2024/25; 40 is August 2026; Ember gives 63.5 for end-2025 |
| C22 | Section 4 ¶5 | Campiglio and others "(2026)", "a recent model" | First issued December 2022; updated 2026 |

Two record-keeping points. The finance file tags Persaud's 2.2 points and Cordella and Powell as [S], while the literature file and the bibliography record them as read; reconcile. Eleven bibliography entries are not cited, among them Weitzman, Lemoine and the renminbi bond, all of which the note needs.

**Egypt numbers.** Every number in the executive summary, Sections 5 to 8 and Appendix B is in the output file and matches to rounding. Rows of Table 6 add up (net = charge + other − fuel saved; totals differ from column sums by 0.1 from rounding). Figures 2 and 3 agree with Tables 6 and 7 and the text. Table 7's title matches its rows. The count of verdicts (19, 11, 2) is right. Discrepancies and ambiguities:

| # | Location | Note says | Output or other value |
|---|---|---|---|
| E1 | Section 6 ¶6 | "$13.5 billion of power investment a year (Appendix B)" | Appendix B gives $118 billion extra over ten years ($11.8 billion a year). $13.5 billion is the gross figure (135 over ten years), which the appendix never states |
| E2 | Executive summary ¶8; Section 7 ¶5; Appendix B "Scale" | "The path adds 7.5 gigawatts of wind and solar a year" | 7.5 is the 2026–30 average. My re-run: 12.7 a year in 2031–35, 19.8 in 2036–40, 28.9 in 2041–45. Output: 44 gigawatts in 2030, 95 in 2035, 170 in 2040, 272 in 2045 |
| E3 | Table 6 "Capital" against Appendix B text | Table: 123, 21, 27, 94, total 266. Text: 118, 20, 25, 88, 16, total 266 | Capital in service in 2035 (includes 2025, excludes other measures) and investment over 2026–35. Two quantities with one total. The text's items sum to 267 |
| E4 | Appendix B "Growth and debt" | GDP "by 0.9 percent and by 5.6 percent"; debt "91 percent without the program in the first model" | The 91 percent baseline belongs to the model that gives 5.6 percent, which is listed second |
| E5 | Appendix B "A check against contracts" | Contracts at 2.4–2.5 cents "equal the model's de-risked cost" | Solar: 2.47 cents against $24. Wind: 2.4 cents against $29, 17 percent below. Contract prices are nominal and fixed; model costs are real |
| E6 | Executive summary ¶8 | External balance "better from 2032 to 2034" | Turns positive in 2032 (de-risked) or 2034 (local). As written it reads as three good years |
| E7 | Appendix B "The cost of waiting" | "$32 billion, of which $35 billion" | 31.6 = 34.9 − 3.3 |
| E8 | Table 7, last row | "Faster: fossil-free power by 2040" | The case also has all new vehicles electric by 2035 |
| E9 | Table 4 against Appendix B | Net gas imports 21; "imports of 22" | 22.2 gross less 1.1 exports. Label each |
| E10 | Section 7 ¶1 and ¶5 | "5 to 6 percent of GDP"; "the program is 6 percent of GDP" | 5.3 percent is the increment; 6.2 percent is gross investment on the path |
| E11 | Appendix B "Method" | Batteries $250 per kilowatt-hour | Output unit costs use a range of $125–250; the record has $192 (IRENA, 2024) and $125 (Ember, 2025) |
| E12 | Fact 5 | Storage adds about three-quarters | The output's own Egypt figure, not in the note, is 1.8 to 2.7 times plain solar |

## D. House style and presentation

All Minor unless marked.

1. **Bold lead sentences.** Present for every paragraph of the executive summary and body. Appendix B uses bold labels ("The program.", "Who pays.", "Scale."), which name a topic and state no point. The opening paragraphs of both appendices have none. "Egypt shows the orders of magnitude" states no finding.
2. **Introduction** (paper standard). It gives no number in the motivation, does not state the answer, names no prior work for the contribution, and spends six sentences on a roadmap where the standard allows one. The evidence-standard paragraph is about the writing, and M12 shows it is not met.
3. **Headings and titles.** Only one section heading states a claim ("Energy becomes capital"); the rest are topic labels. Tables 1–5 and Figures 1–3 have labels for titles; only Tables 6 and 7 state a finding. Tables 1 and 2 have no source line. Figure 2 repeats two columns of Table 6 (flagged in v0.1).
4. **Page rules.** Appendix B starts mid-page 27; the rule gives each appendix a new page. The Section 5 heading sits at the foot of page 8 with three lines under it. Table 1 splits a row across pages 4–5, and Table 2 across pages 9–10, leaving two lines at the top of page 10. In Table 5 the number column is too narrow, so "10" to "32" print on two lines. Table 7 sits alone on page 31, three paragraphs after its mention.
5. **US English.** "Modelling" (executive summary ¶1; Appendix B ¶1). "Dear" and "dearer" seven times read as British. "Mark-ups".
6. **One term for one thing.** Used two ways: "de-risked" (whole program at a sovereign loan rate; power only; a payment guarantee; today's sovereign-guaranteed projects); "the program" (increment; gross path); "local" (dollar project rate; pound money); "risk premium" (whole gap; offtaker part); "6 percent" (nominal loan rate; real discount rate). Named several ways: the external measure ("external balance", "external accounts", "trade balance", "current account"); the buyer ("public buyer", "state utility", "state distributors", "state company"); the lender ("development banks", "lenders who are paid first", "preferred lender", "the Bank"); the rate ("cost of capital", "financing cost", "discount rate", "rate"); a negative saving ("net savings ... of −$14 billion").
7. **Process residue.** "No project ... was found"; "no data on their size was found for this note"; "no published split was found"; "the tool's defaults"; "two macroeconomic models in the tools"; "was read for this note". State the gap as a fact about the literature or cut it.
8. **Tells.** None of the listed vocabulary and no em dashes. Two tics: the "X and not Y" contrast (seven times: "a review and not a model", "cheap and not free", "a bound and not a forecast"), and leads that count ("Three things are new", "Six implications", "Seven pragmatic rules", "Ten indicators", and a dozen more).
9. **Citations.** Name particles are dropped: "(Bergh and Savin 2021)", "(Weijde and Hobbs 2012)". The IPCC chapter prints as "(Dubash et al. 2022)". Chapter numbers print as "13 in". Twelve references are the author's own, and facts 11, 27, 28 and 31 rest on them. IMF is used in Section 5 before it is defined in Section 7.
10. **Advocacy.** Contained, with three slips. Products "follow from the facts" (executive summary ¶6). Section 8 ¶1 is six imperatives with no cost, risk or failing condition. "No fact about technology closes it" (Section 8 ¶2).
11. **Sentences a careful economist would stop at.** "Price and deployment have opposite returns to scale" (Section 4 ¶7). "The cost of capital becomes the price of energy" (three times, and once more as "an energy price"; it becomes the main cost). "Energy moves from the current account to the balance sheet". "Credibility becomes a macroeconomic variable" (Table 1). "The first-best carbon price is therefore a benchmark" (abstract). "Better from 2032 to 2034". "Of which $35 billion".
12. **README.** Out of step with v0.2: it says thirty facts, five products, and 1.8 and 0.2 percent of GDP.

## E. Tone and confidentiality

**M13. The Egypt results need three changes of framing.**

1. *The headline is a bound.* The executive summary's "saves 0.9 percent of GDP at a de-risked 3.9 percent" prices cars, boilers and factories at a sovereign loan rate. Appendix B says the products reach power only. The reachable results are in the output ($1.6 billion and −$1.1 billion): the net cost of 0.5 percent of GDP falls to 0.27 percent with a payment guarantee on power, and to a saving of 0.18 percent with all power de-risked (my arithmetic). Lead with those.
2. *The gas price is from a crisis.* Gas is valued at $12 "because ... imports cost about $13 in the first half of 2026". The evidence file records a war in the Middle East from March 2026, a cut in pipeline supply and cargo prices doubling. The note does not mention it and holds $12 in real terms to 2050. At the 2024 supply cost the 2035 net cost is $5.9 billion, not $3.0 billion (Table 7). Give a range, or make the lower price central.
3. *Egypt's own plans are understated.* The path reaches 38 percent renewable electricity in 2030; the government's target is 42 percent by 2028. Signed agreements imply 8.7 gigawatts a year in 2027–28. The executive summary sets the path only against "a record of 1.5". An Egyptian official will read that as a slight. "Which the government's balance sheet may not be able to carry" (Appendix B) is a judgment on a member's credit with no source; cite the IMF's planned cut in guarantees or drop it.

**M14. Four statements could be read as resting on non-public material or as speaking for the Bank.**

1. *"Open model".* The introduction says "an open model on public data" and Appendix B "the author's open tools". The script's first lines call the tools a "private repository". A reader cannot re-run the numbers, and the Egypt cost of capital comes from a database "held in the tools repository" (C4). Either publish the model and inputs or write "the author's model" and name the public file behind each input.
2. *"Public Investment in CPAT".* The model's documentation is cited as an unpublished paper with that title (reference list, p. 22). CPAT is an institutional tool. The v0.1 review flagged it. Cite a public description or retitle.
3. *The Bank's capital rule.* "A development bank holds capital against a guarantee as against a loan" is stated as current fact, from the author, on a 2014 think-tank source that the bibliography says was not re-checked (C17). Date it and source it to a current public document, or soften.
4. *The README.* It says the Egypt estimates are "not yet cleared by Stephen for publication" while note, script and output sit in a public repository. It also mentions a CPAT Egypt run "on a proprietary data edition". Even the existence of that run is better left out of a public file.

Otherwise the tone is careful. "Could offer" is used throughout, the disclaimer is in place, the reforms of 2025–26 are credited, the borrower-limit comparison is gone, and I found no internal figures. The World Bank letters cited are published inside IMF country reports.

## F. The ten changes that would most improve the note

1. **Repair the accuracy failures (M12).** Source or cut the three import shares (C1). Fix the contract check (C5, E5), the storage slips (C2, C3) and the origin of the Egypt rate (C4). Then keep or drop the sentence that states the evidence standard.
2. **Rebuild the present values and the cost of waiting (M6).** Benchmark with capital at par; separate the financing rate from the discount rate; lead with power and transport; add the timing rule; change the lead sentence.
3. **Redo the guarantee arithmetic (M7).** Define exposure. Use brief 3.1's own ratio or explain the difference. Say whether the state counter-guarantees. Add the MIGA record and SECI's margin.
4. **Build the bridge from expectations to optimal policy (M1).** Prices against quantities and the hybrid; policy without commitment; the hazard formula; private against social risk.
5. **Complete the second-best pricing section (M2).** Tax interaction, informality and incidence; state-company pass-through; a level or path; a failing condition for each rule; fix rules 2 and 6.
6. **Show the external accounts as a range (M8).** Half and all foreign-financed, at both rates; the gas balance; a fiscal path or no fiscal J.
7. **Fill the author's thin points (M3).** A SECI paragraph; the 50/50 split with sources and the comparison; swaps with the parity logic, the renminbi bond and India; pensions done or dropped; a fungibility paragraph; the grid benefit-cost ratio; the consortium example.
8. **Reframe Egypt (M13, M14).** Headline what the products reach; give a gas-price range; state the build rate by period (E2); credit the pipeline; settle "open" and the CPAT reference.
9. **One indicator table with definitions (M4).** Merge the four, the six and the ten; give identities, Egypt values and dates.
10. **Finish the returns argument and the summary (M5).** Technology fixed against a backstop; the mix shown with Egypt's own numbers; the critical learning literature; "may come too late" in the executive summary. Then the house-style pass: Appendix B leads, page breaks, one term for one thing.

## Checks I could not make

1. The macro models (not re-run), and any source behind a paywall.
2. The note's sources at first hand, apart from the Crossref and OpenAlex records named above. Section C tests the note against its own record, not against the originals.
3. Working paper 5.5 and working papers 6.3 and 6.5, which are unpublished.
4. Whether the tools repository is public, beyond what the script says.
5. The Bank's current capital treatment of guarantees, and which loan-pricing group applies to Egypt.
