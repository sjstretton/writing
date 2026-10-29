# Plan for 1.1, version 2: the two-track architecture (29 Oct 2026)

Stephen's brief (29 Oct): make 1.1 the overarching paper in its series. It should argue one architectural point: carbon pricing of **production** (in the economic and trade sense) should be separate from carbon pricing of **consumption**. Production is priced with a revenue-neutral feebate; consumption with a destination-based charge. The paper derives the cost of the feebate, shows that international payments can make that cost negative (which justifies policy crediting), and shows that production then moves toward the countries that price carbon most strongly. Four companion papers carry the detail.

This note records what the repo already holds, the revised argument and outline, and the derivations. It supersedes sections 2 and 4 of `Review-2026-10-29.md`. The reference list and template notes in that file still stand.

## 1. What the repo already holds

| Role in the series | Where | State | Use |
|---|---|---|---|
| **Overarching paper (this one)** | `1.1/OpenEconomyCarbonPricing.qmd` | ~4,000 words; framework, sketch models | Rebuild around the architecture below |
| Earlier framings of the same idea | `1.1/1.Presentation/Briefing-OpenEconomyCarbonPricingAbstract.txt`, `Briefing-UpdatingCarbonPricing.qmd`, `5.Notes/Notes-CarbonPricingVersionTwo.txt` | Abstracts and outlines | The 2025 abstract already says "with concessional support… net" and "international support shift manufacturing toward cleaner producers": the seeds of results 2 and 3 |
| Race to the top | `1.1/3.RelatedPiecesAndLinks/Background-DesigningARaceToTheTop.qmd` | 690-word stub | Source for the destination-basis argument and the corporate-tax analogy |
| **Companion C1: the consumption side (EU VAT as a carbon tax)** | `1.6.CarbonConsumptionTax/CarbonConsumptionTax.qmd` (moved 29 Oct) | 8,900 words; a full proposal with numbers | Now paper 1.6. It already argues the split: production instruments (ETS free allocation, CBAM) "can coexist fully" with the consumption tax |
| **Companion C2: feebates in detail** | `1.2/FeebatesAndOutputBasedRebating.qmd` (power sector); `1.2/3.RelatedPiecesAndLinks/IndustrialFeebates/Background-IndustrialFeebates.qmd` (industry, 6,100 words) | Drafts | Power-sector and household feebates stay here, not in 1.1. The industrial background paper is closest to 1.1's production track |
| **Companion C3: carbon-price equivalents** | `4.1/PolicyEquivalentCarbonPriceAndCES.qmd` (Total Effective Carbon Price) | Technically complete draft | Supplies the measure that lets a feebate count as a carbon price at the border and in crediting |
| **Companion C4: updating CBAM** | `1.3/IronSteelCBAM.qmd` ("Carbon Price Recognition under CBAM") | Near-final consultation submission | Its recommendation 2.2 ("recognise implicit carbon pricing") is the institutional hinge of 1.1: without it, a feebate country's exporters get no credit at the EU border |
| Toy model of global incentives | `6.Additional/5.Analytics/5.4…/Toy_Model_Global_Mitigation.pdf` | Working draft | Logit investment share, leader–follower diffusion, and international "augmentation" through carbon-credit purchases and payments: a dynamic version of results 2 and 3 |
| Book | `6.Additional/6.Books/6.2…/CarbonPricingRightPolicyWrongTime.qmd` | 15,000 words | Chapters 1–2 (why feebates beat carbon taxes), 5 (pricing across borders) and 11 (the sequence). Position paper P1 |
| Political feasibility metric | `5.1/3.BackgroundPapers/Background-PoliticalEconomyMetric.qmd`; 1.2 Part 3 | Drafts | Optional evidence for the political-economy constraint |

Nothing in the repo yet covers **policy crediting**. Only the CBAM dashboard guide mentions crediting. Klaus Oppermann (policy crediting, per `about-me.md`) is the natural contact.

## 2. The argument in one paragraph

Carbon pricing does two jobs that pull against each other in an open economy. Pricing what a country **produces** pushes firms to cut emissions per unit of output, but a tax on the full level of emissions also raises average costs, so exporters and import-competing firms lose share and the tax stays low. Pricing what a country **consumes** cuts demand for carbon-intensive goods and raises revenue, and on a destination basis it treats imports and domestic goods alike. One instrument cannot do both jobs well, so the paper separates them. Production is priced with a revenue-neutral feebate: it gives the full marginal incentive to cut intensity at zero cost to the treasury, and raises the producer price only by the resource cost of abatement, about half the intensity cut times the rate. Consumption is priced with a destination-based charge, administered through VAT. For developing countries, production is what matters: they are building heavy industry and export capacity, and their consumption base is small. A feebate's small residual cost can be more than covered by international payments per tonne reduced, which turns policy crediting into a self-interested reason to adopt one. And once importers price consumption by embodied carbon, each exporter does best by setting its feebate rate equal to the carbon charge in its markets, so production moves toward the countries that price carbon most strongly. That is the reverse of leakage.

## 3. Scope: one meaning of "production"

Stephen's brief separates two meanings of production. Making both arguments would confuse the paper.

- **In scope: production versus consumption in the trade sense.** The difference between them is net exports. The architectural argument is about who bears the carbon charge when goods cross borders.
- **Out of scope: primary versus tertiary production** (power generation and fuels versus services). The case for feebates in power is about capital turnover, pass-through and household prices, not trade. It belongs to 1.2. 1.1 mentions it in one paragraph and points to 1.2.
- Also moved out: the "two-plus-one functions" and the remediation function (to a concept paper), and the primary–tertiary section (to 1.2).

## 4. Results and derivations

### Setup

A competitive sector produces output $Q$ at unit cost $c(e) = c_0 + \tfrac{k}{2}(e_0 - e)^2$, where $e$ is emissions per unit of output, $e_0$ the unpriced intensity and $k$ the slope of the marginal cost of cutting intensity. The baseline price is $p_0 = c_0$. Demand (domestic plus export) has price elasticity $\eta$. Two instruments are compared at the same rate $t$ per tonne:

- **Carbon tax:** the firm pays $t\,e$ per unit.
- **Feebate:** the firm pays $t\,(e - \bar e)$ per unit, with the benchmark $\bar e$ equal to the sector average, so payments sum to zero.

All results below were checked symbolically.

### Result 1: the residual cost of a revenue-neutral feebate

Both instruments give the same intensity response, because the marginal incentive is $t$ in each case: $e^* = e_0 - t/k$.

They differ in what happens to the price:

$$
p_{\text{feebate}} - p_0 = \frac{t^2}{2k} = \tfrac{1}{2}\,t\,\Delta e,
\qquad
p_{\text{tax}} - p_0 = t\,e_0 - \frac{t^2}{2k}.
$$

- **Treasury cost:** zero, by construction.
- **Production cost:** the feebate raises the producer price by the resource cost of abatement, $\tfrac12 t\,\Delta e$: half the intensity cut times the rate. A tax raises it by roughly the full carbon bill, $t\,e_0$. The ratio is $\Delta e/(2e_0)$, half the proportional intensity cut. A feebate that cuts intensity by 30 percent raises the price by 15 percent as much as a tax at the same rate.
- **Output (export) loss:** $\Delta Q/Q \approx -\eta\,t^2/(2k\,p_0)$ under the feebate, which is second order in $t$. Under the tax it is $-\eta\,t\,e_0/p_0$, which is first order. Higher elasticity scales up both. For trade-exposed goods, where $\eta$ is high because foreign suppliers are close substitutes, that is the leakage the tax causes and the feebate avoids.

**The efficiency cost: where elasticity enters.** The feebate gives up the output channel, so it cuts fewer tonnes at a given rate. To match the emissions cut of a tax at rate $t_T$ (to first order), a feebate needs

$$
t_F = t_T\left(1 + \frac{\eta\,k\,e_0^2}{p_0}\right).
$$

The premium rises with demand elasticity $\eta$, with carbon intensity per unit of value ($e_0/p_0$) and with the steepness of abatement costs ($k$). This is Stephen's conjecture ("higher for higher elasticity"), now derived. Two points limit it:

1. In a trade-exposed sector, most of the tax's "output channel" is foreign suppliers replacing domestic ones. That is leakage, not abatement, so from a global view the premium mostly vanishes.
2. The consumption track restores the genuine demand channel. Together the two tracks reproduce both margins of a first-best carbon tax: intensity through the feebate and quantity through the consumption charge. This is the architectural result.

Related literature: intensity standards and output-based rebating implicitly subsidize output (Holland, Hughes and Knittel 2009, *AEJ: Economic Policy*; Fischer 2001, RFF discussion paper; Fischer and Fox 2012). Keen, Parry and Roaf (2021) classify feebates and output-based rebates as cutting intensity but not output. [VERIFY all four before citing.]

**Illustration** (stylized, not sourced; replace with calibrated values): a steel-like sector with $e_0 = 2$ tCO₂/t, $p_0 = \$600$/t, $t = \$50$/tCO₂ and a 30 percent intensity cut ($\Delta e = 0.6$, so $k \approx 83$). The feebate raises the price by \$15/t (2.5 percent). A tax at the same rate raises it by \$85/t (14 percent). The equal-abatement premium factor is $1 + 0.56\,\eta$.

### Result 2: international payments can make the feebate net-beneficial

Suppose an international buyer pays $\pi$ per tonne of emissions cut below the unpriced baseline. This is policy crediting, results-based climate finance or an Article 6 purchase. With the linear marginal cost above, the country's net cost of a feebate at rate $t$ is

$$
\text{Net cost} = \underbrace{\frac{Q\,t^2}{2k}}_{\text{resource cost}} - \pi\,\underbrace{\frac{Q\,t}{k}}_{\text{tonnes cut}} = \frac{Q\,t\,(t - 2\pi)}{2k}.
$$

- The net cost is **negative whenever $\pi > t/2$**: the payment per tonne exceeds the average abatement cost, which with any rising marginal cost is below the marginal cost $t$.
- The country's best response is **$t = \pi$**: it sets its feebate rate equal to the crediting price and keeps a surplus of $Q\pi^2/(2k)$.

So a crediting price of $\pi$ induces a self-interested feebate at rate $\pi$, with no treasury cost and a net gain to the country. This is the case for **policy crediting**: paying for the policy, measured as a carbon-price equivalent (companion C3), rather than for projects. Two questions remain: additionality (the baseline $e_0$) and who pays. [Literature on policy crediting and Article 6 to be found and verified.]

### Result 3: production moves to the countries that price carbon most

Let an importing market price consumption at $\tau$ per tonne of embodied carbon, through a destination-based charge (C1) or a CBAM that measures actual intensity and recognizes feebates (C4). An exporter running a feebate at rate $t_i$ delivers at cost

$$
D_i = c_0 + \frac{t_i^2}{2k} + \tau\left(e_0 - \frac{t_i}{k}\right),
$$

which is minimized at **$t_i = \tau$**. Each exporter's most competitive feebate rate equals the carbon charge in its export markets. As importers raise $\tau$, exporters raise $t_i$, and market share shifts toward the producers with the lowest embodied carbon, which are those with the strongest production pricing. Under source-based carbon pricing the opposite happens: production moves to the country with the lowest tax. Crediting (Result 2) adds to the same push. The leader–follower model in `5.4/Toy_Model_Global_Mitigation.pdf` is the dynamic version.

**Condition:** this needs import charges based on actual (verified or default) intensity that give feebate countries credit for lower intensity. Under CBAM as it stands, a revenue-neutral feebate has no explicit "carbon price paid", which is the gap C4 addresses.

## 5. Revised outline

Working title: **"Price Production and Consumption Separately: A Two-Track Architecture for Carbon Pricing in Open Economies"** (alternative: keep "Open Economy Carbon Pricing" as the subtitle). About 7,000 words, World Bank working paper form, with Keen, Parry and Roaf (2021) as the structural template.

1. **Introduction.** Carbon prices are low and narrow (*State and Trends*, latest edition). The reason in open economies is that one instrument carries two jobs. The answer: two tracks. Contribution: the architecture, the feebate cost result, the crediting result and the race-to-the-top result. State the series and the four companions.
2. **Why one carbon price cannot do both jobs.** Production versus consumption in the trade sense; net exports as the wedge; competitiveness, leakage and political limits; evidence. One paragraph on why power and other non-traded production is a different argument (see 1.2).
3. **The two-track architecture.** Definitions (template: Keen, Parry and Roaf's definition paragraph). Track 1: a revenue-neutral production feebate. Track 2: a destination-based consumption charge (detail in C1). How they combine to reproduce both margins of a first-best price.
4. **What a feebate costs.** Result 1 with the illustration and figure. Why developing countries should start here.
5. **International payments and policy crediting.** Result 2. Measurement through carbon-price equivalents (C3).
6. **From leakage to a race to the top.** Result 3. What CBAM must change (C4). Origin versus destination responsibility and the Paris Agreement (raised by Keen, Parry and Roaf).
7. **Design table and objections.** Table: design choices against objectives. Objections: benchmark setting and updating; verification; WTO subsidy rules for the feebate; revenue use, picking one; administration in low-capacity countries.
8. **Policy implications** for developing-country exporters, the EU (free allocation phase-out, CBAM review, VAT) and development banks (crediting).
9. **Conclusion.**

Appendix A: the model and proofs of Results 1–3. Appendix B: political feasibility (shortened from the current B). Appendix C: implementation at the border (shortened from the current C, pointing to C1 and C4).

## 6. The companion papers

| | Companion | Folder | What 1.1 takes from it | What it needs |
|---|---|---|---|---|
| C1 | Turning EU VAT into a carbon consumption tax | `1.6.CarbonConsumptionTax/` | Track 2's administration; numbers on effective rates | Promoted to 1.6 on 29 Oct. Upgrade to the standard |
| C2 | Feebates and output-based rebating | `1.2` (+ industrial background) | Track 1 design; power sector, kept out of 1.1 | Split into power (1.2) and industry? Clean the conversion (H15) |
| C3 | Policy-equivalent carbon prices (TECP) | `4.1` | The measure for crediting and border recognition | Literature, calibration, a country case (already rank 2) |
| C4 | Updating CBAM: recognizing carbon prices | `1.3` | Border recognition of feebates; the trilemma for developing-country exporters (its Appendix A) | Resolve the title mismatch (H3); retitle to match its content |

## 7. Decisions for Stephen

1. Title: the new working title, or keep "Open Economy Carbon Pricing"?
2. Revenue use for the consumption charge: household rebates, remediation or general revenue? The current draft spends it three times.
3. Promote the consumption-tax background to its own paper (1.6)?
4. Rename 1.3 to "Carbon Price Recognition under CBAM" so it matches its content and the C4 role?
5. Spelling: US or UK for this series?
