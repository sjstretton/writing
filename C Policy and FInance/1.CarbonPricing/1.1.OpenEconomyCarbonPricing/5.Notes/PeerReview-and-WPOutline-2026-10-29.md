# Paper 1.1: peer review of the brief, and outline of the working paper

Review of *Climate Fiscal Policy Brief No. 1.1* (`1.Presentation/Brief-OpenEconomyCarbonPricing.qmd`, v1.0, Oct 2026), written as a referee report for an economics journal. The outline that follows is the plan for the academic working paper (master `OpenEconomyCarbonPricing.qmd`, v0.3).

## Part 1. Referee report

**Summary.** The brief argues that carbon pricing in open economies should use two instruments: a revenue-neutral feebate on production intensity and a destination-based consumption charge. It derives five propositions in a one-sector partial-equilibrium model with quadratic abatement costs. The idea is clear and policy-relevant. The analysis is too thin for an academic paper in five places, and two claims need stronger support.

**Major comments**

1. **The central claim is asserted, not proved.** The brief says the two tracks together "reproduce both margins of a first-best price". That is the paper's main result and deserves a formal statement. In the model it is true and simple. The consumer price under the two tracks is $c(e^*) + \tau e^*$, the producer's intensity choice is $e^* = e_0 - t/k$, and with $t = \tau$ both equal the Pigouvian outcome for home consumption. The only difference is where revenue is collected: on consumption rather than production, a difference of $\tau e^*$ times net exports. State and prove this as the main theorem (Proposition 0 in the brief's numbering).

2. **Proposition 3 needs its sign condition.** Intensity standards can raise emissions when the implicit output subsidy is large (Holland, Hughes and Knittel 2009). In the brief's model, output rises only relative to the tax, never relative to no policy, because the feebate raises the price by $t^2/2k > 0$. Say so, and show where that stops holding: with heterogeneous firms and a benchmark below some firms' costs, marginal producers can expand.

3. **One sector, identical firms.** Benchmark windfalls, entry and exit, and the distribution of rebates among firms all need firm heterogeneity. Add an $N$-firm extension: firms differ in abatement cost $k_i$ and baseline $e_{0i}$; the benchmark is the output-weighted average.

4. **The race-to-the-top result ignores market shares.** Proposition 5 minimizes one exporter's delivered cost but says nothing about how share moves. Add a multi-exporter model (Armington or logit demand in the importing market) and simulate. Calibrate the intensities to the EU CBAM default values: hot-rolled flat steel runs from 2.1 tCO₂/t (Japan, Korea) to 4.3 (India) and 8.2 (Indonesia). Show feebate rates and market shares converging as the importer's charge rises.

5. **Policy crediting is underdeveloped.** Proposition 4 treats the baseline $e_0$ as known. In practice the country reports it, which invites inflation (moral hazard), and a buyer pays only if additionality is credible. Add the buyer's side: the buyer's cost per tonne is $\pi$, worthwhile if $\pi$ is at or below the buyer's marginal damage or its own marginal abatement cost. Then add baseline-setting rules (a historical benchmark, or a benchmark tied to the TECP measurement) and the literature on sectoral crediting.

**Minor comments**

6. Mixed regimes: imports from a country with an explicit origin carbon tax would pay twice, once at origin and once at destination, unless the origin country zero-rates its exports. Discuss the transition, and CBAM's "carbon price paid" deduction as a stopgap.
7. The steel illustration is stylized. Use the default values and a sourced steel price.
8. The WTO treatment is one sentence. The feebate's rebate leg needs a subsidy (SCM) analysis, and the consumption charge raises the "like products" question for carbon-differentiated internal taxes.
9. Distribution of the VAT carbon component: consumption-based carbon shares by income decile. Cite or flag.
10. The political-economy constraint is described but not modeled. Bring back a compact version of v0.1's Appendix B: industry and voter tolerances giving $t^{\max}$.
11. Origin versus destination under the Paris Agreement: a paragraph, citing Keen, Parry and Roaf.
12. References: run every entry through Crossref (the literature agent is doing this).

**Recommendation:** major revision. The core idea is publishable; the paper needs the theorem, heterogeneity, a calibrated multi-country example and a fuller crediting section.

## Part 2. Outline of the working paper (v0.3, about 9,000–11,000 words plus appendices)

**Front matter.** Title as the brief. Personal capacity. Abstract of about 150 words. Keywords, JEL (F18, H23, Q54, Q58, H87).

1. **Introduction** (900 words). The problem in numbers; one instrument, two jobs; the answer; four contributions (the equivalence theorem, the feebate cost results, crediting, the race to the top); the series.
2. **Related literature** (900 words; full review in Appendix A). Leakage and border adjustment; output-based rebating and intensity standards; destination-based taxation; consumption-based charges; crediting and clubs. One paragraph saying what is new.
3. **Model** (1,200 words). Two countries, then $N$ exporters. Technology $c(e) = c_0 + \tfrac{k}{2}(e_0 - e)^2$; demand; instruments: an origin tax, a feebate, a destination charge.
4. **The equivalence theorem** (800 words). Proposition 0: a feebate at $t$ plus a destination charge at $\tau = t$ replicates the Pigouvian allocation for home consumption and production intensity, with no leakage; revenue is collected on consumption. Corollary: the revenue difference equals $\tau e$ times net exports. Figure 1: the two tracks as a wedge diagram.
5. **What a feebate costs** (1,200 words). Propositions 1–3, the sign condition (minor comment 2), and the $N$-firm extension with benchmark windfalls.
6. **Calibrated illustration: steel** (1,000 words). Default values by exporter, sourced price, Table 1 (price effect of tax versus feebate by country), Figure 2.
7. **International payments and policy crediting** (1,200 words). Proposition 4; the buyer's side; baselines and moral hazard; measurement by carbon-price equivalent (1.7). Figure 3.
8. **From leakage to a race to the top** (1,200 words). Proposition 5 generalized; Armington simulation with calibrated intensities; Figure 4 (feebate rates and market shares as $\tau$ rises).
9. **Implementation** (1,000 words). VAT carbon component (1.6); forward-announced obligations on energy-chain firms; border treatment and CBAM reform (1.3); WTO.
10. **Objections and limits** (700 words). Distribution; double charging in mixed regimes; capacity; origin-based Paris accounting; general equilibrium.
11. **Conclusion** (300 words).

**Appendices.** A: literature review (from `5.Notes/LiteratureAppendix-draft.md`). B: proofs of Propositions 0–5 and the $N$-firm results. C: calibration data (`2.Source/CBAM-default-values-steel-aluminium-cement.csv`) and the simulation code. D: political-economy model.
