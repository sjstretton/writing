# 6.8 Pricing the Measures: Investment Needs, Abatement Costs and Public Money in CPAT

**Status:** methodology note v0.3 (Theory and Research Note No. 6.8), 18 Nov 2026. v0.2 took in a referee-style peer review (`5.Notes/PeerReview-2026-11-18.md`). v0.3 (Stephen, 18 Nov): capital costs follow legacy CPAT (country unit costs where data exist, else the source value, no price-level scaling); a paragraph on CPAT's price pass-through (new policies in full for fuels; price controls only on supply-cost changes, by a global setting; electricity by the power pass-through setting); interim assumption defaults accepted. New research awaiting Stephen's review; not on the website; no brief or deck. v0.1 and v0.2 are in `8.PreviousVersions/`. Joins `D Modelling/6.ModularUpgrades/` once reviewed.

**Question.** How should CPAT estimate the investment each mitigation measure needs, what each tonne it abates costs, and how much of that falls on the budget, through public investment, green subsidies, fees outside energy and public-private partnerships?

**Answer.** Every cost is a physical change times a SISEPUEDE unit cost factor, localized and discounted once. Capital is separated from running cost and split by payer type (P1–P5, as in paper 6.5). Each measure gets four abatement costs:

- **Private:** at the investor's cost of capital and retail prices.
- **Resource:** at 6 percent and supply-cost prices.
- **Social:** the resource cost less local co-benefits.
- **Public money:** the social cost plus (λ − 1) times the budget's cost per tonne. This is paper 6.3's funding rule per tonne (Proposition 1).

A viability gap is the investor's loss at retail prices. Energy measures enter CPAT as level scalars by sector and fuel, with CPAT's rebound, plus a fuel-switch term and a subsidy shadow price p·σ/(1 − σ). Non-energy measures and fees act on emissions through a capped linear uptake rule. A partnership switch converts a P1 capital item into an availability payment over the contract at i_g + ρ, with a break-even construction saving (Proposition 3). In power, measures change costs and one-sided penalties inside paper 5.1's combined penalty rule.

## Where each part of the brief is answered

| Brief item | Section |
|---|---|
| 1. Investment need, upfront capital, abatement cost of public investment and green subsidies, by sector | 2 (accounting), 3 (investment need, four abatement costs), 4 (public need, ledger), 5 (subsidies), Appendix A (factors by sector) |
| 2. Fees and payments in non-energy sectors | 6 |
| 3. Capital vs running taxonomy; partnership switch (annuity, contract length, risk premium) | 7 |
| 4. Mapping CPAT to SISEPUEDE transformations, with gaps and many-to-one matches | 8 |
| 5. Integration into CPAT; six rules against double counting with paper 6.3 | 9 |
| 6. Power: limits of the current module; plug-in to the combined penalty rule of paper 5.1 | 10 |

## Files

| File | What |
|---|---|
| `InvestmentAndAbatementCosts.qmd` | Master (v0.3) |
| `InvestmentAndAbatementCosts.bib` | References. Entries reused from papers 5.1, 6.3 and 6.4 were checked there. Added here: the SISEPUEDE cost-benefit documentation and code, the SISEPUEDE docs, and IPCC 2006 Vol. 4 |
| `InvestmentAndAbatementCosts.docx` | Rendered in the house format |
| `2.Source/worked_examples.py`, `worked_examples_output.txt` | Section 11 examples (electric-car subsidy, cattle methane payment, partnership conversion) and the partnership table, plus a check of the corrected active-set rule |
| `5.Notes/PeerReview-2026-11-18.md` | The peer review of v0.1 |
| `8.PreviousVersions/` | v0.1 (qmd, docx, code), v0.2 (qmd, docx) |

Render from the repository root. Equation and table numbers need the cross-reference filter as well as the house filter:

```bash
python "B Theory and Research/render_docx.py" "B Theory and Research/6.8.InvestmentAndAbatementCosts/InvestmentAndAbatementCosts.qmd"
```

`render_docx.py` does not yet apply `H Writing Instructions/Scripts/Website/quarto-xref.lua`. Until it does, run pandoc with `--lua-filter=quarto-xref.lua` before the house filter; that is how the v0.2 docx was made.

## Sources

The SISEPUEDE cost-benefit documentation, every page, and the module's public code and factor database (commit adc22ba). The SISEPUEDE documentation. Papers 5.1, 6.1, 6.3, 6.4 and 6.5. The public CPAT-AI repository for CPAT's equations. Internal and unpublished material was read for method only and is not cited.

## How the peer review was taken in (v0.2)

All eleven major and 23 minor points were accepted. The main changes:

- **M1:** the viability gap is max(0, −NPV) at retail prices, so taxes are no longer subtracted twice. The "price first" flag applies when the private cost is at or below zero. The power cost uses fuel before carbon charges plus the explicit carbon price.
- **M2:** the public-money cost is built on the social cost. Proposition 1 is restated with co-benefits and positive tonnes.
- **M3:** the electric-car example uses the Latin American factor throughout (premium 7,020 dollars), nets electricity tax and uses the 10.5 percent private rate.
  - The headline is now a budget cost of about 550 dollars per tonne for abatement with a resource cost of −150.
  - Abstract and summary updated.
- **M4:** subsidies are paid on total uptake, and inframarginal uptake is reported separately. Uptake is capped by the maximum uptake. The cattle example now uses a results-based payment, with the share of emissions left corrected. A per-head fee is shown to buy nothing.
- **M5:** the partnership has its own delivery efficiency, equal to the public one by default.
  - A switched P2 asset becomes P3 with a contingent liability.
  - New table: break-even saving by contract length.
  - The investment multiplier applies to publicly financed capital only.
- **M6:** the caps stay, as in paper 5.1.
  - Corrected active-set solution, checked in code.
  - Corrected share response.
  - Targets become investment-share paths with one-sided penalties.
  - Grid term lagged; storage counted once; public grids stay in the system's cost.
  - Public builds use max(0, ·) and feed realized shares forward.
  - The plug-in changes terms inside CPAT's investment cost; capital recovery factors are averaged across financing routes.
- **M7:** CPAT's α⁺ is too coarse, so efficiency measures enter as level scalars with CPAT's rebound (the exact α⁺ form is given for a future code change). Switches run on the unswitched path. The shadow-price equivalence is restated as exact under constant returns. The electric-car shadow price was removed.
- **M8:** factor cards corrected and moved to Appendix A, with a Database column.
  - Heat factors: database values 1.67 and 5.0 per MWh thermal.
  - Parity statement corrected.
  - Diets are a saving; ending open dumping is a benefit; biogas is a unit conversion; the rice factor is per acre; material efficiency is a running saving.
  - Industrial capture: annual change 0, flagged.
  - Incremental-only and capital-not-yet-deliverable limits are stated in the executive summary.
- **M9:** this README cut to one line on unpublished material.
  - YAML comment cleaned; the "new interface" and project references cut.
  - SISEPUEDE used throughout.
  - Payer types and γ = 0.3 cited to paper 6.5. χ and the vehicle efficiency ratio are labelled assumptions from paper 6.5's tool.
  - The green public investment block is described as report-only, citing CPAT-AI R5.
- **M10:** the ledger explains the omitted earmarked-revenue term. Grants are always SUB. The haircut applies to P1 only. Pass-through defaults to 1, as in paper 6.3, with 0.5 as sensitivity. θ and additionality are labelled assumptions. Rule 1's additionality is clarified as overlap on the same margin.
- **M11:** notation table added and symbols renamed (k, h, d, ℓ, F^bud, ν, V, s^PIM, χ, o and others). Cards moved to an appendix; co-benefit rows CPAT supplies removed; snapshot abatement cost cut.
- **Minor 1–23:** all taken in. Straight-line wording; "returns undiscounted flows"; transformation counts; climate (not mitigation) investment; vintage sum over j; feebate neutrality; land-use stock path; Proposition 2 wording; one term for the 5.1 rule; abstract 200 words with CPAT and SISEPUEDE defined; ramp width a fixed 50 dollars; P2 reported as public-sector investment; captions state messages; ledger rate note; grant-subsidy rate and period; transmission wording; code fixes.

## Open items for review

- Interim defaults, accepted by Stephen on 18 Nov 2026 until calibrated: partnership risk premium (3 points), contract length (20 years) and delivery efficiency (equal to public); uptake ramp width (50 dollars per tonne); permanence discount (0.8); χ (0.6); lives marked "a" in Appendix A.
- Price level: this note follows legacy CPAT (no price-level scaling; country unit costs where data exist). Papers 6.3 (full price level) and 6.5's tool (half) differ and should be aligned when next revised.
- SISEPUEDE factors to settle before use: the nine documentation–database differences, the unit of the industrial capture factors, and the undocumented levelization rates of the heat and efficiency factors.
- The IPCC Tier 1 enteric factor (56 kg CH4 per head a year, Latin America, other cattle) is used from memory of Table 10.11; check against the table.
- Length: the body is about 11,000 words including tables. No brief or deck yet.
