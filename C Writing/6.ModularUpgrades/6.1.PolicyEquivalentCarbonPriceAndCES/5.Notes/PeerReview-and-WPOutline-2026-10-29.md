# Paper 1.7: peer review of the brief, and outline of the working paper

Review of *Climate Fiscal Policy Brief No. 1.7*, "Measure Carbon Pricing by the Emissions It Cuts" (`1.Presentation/Brief-PolicyEquivalentCarbonPriceAndCES.qmd`, Oct 2026), written as a referee report. The outline is the plan for the academic working paper (master `PolicyEquivalentCarbonPriceAndCES.qmd`, to become v0.3; the current v0.2 moves to `8.PreviousVersions/`).

## Part 1. Referee report

**Summary.** The brief defines the Total Effective Carbon Price (TECP): the uniform economy-wide carbon tax that would cut emissions by as much as a given mix of instruments. It weights each instrument's price effect by sector and fuel semi-elasticities from a nested CES energy-demand model, and it extends the metric to non-price instruments through shadow prices or backed-out emission effects. It corrects the switching semi-elasticity in all earlier versions, which carried an extra $(1-w)$ factor. The metric fills a real gap: existing metrics (OECD Effective Carbon Rates, IMF and World Bank explicit-plus-implicit prices) measure prices, not emission effects.

**Major comments**

1. **Make the correction a stated result.** Derive the first-order emission response under nested CES from the cost function: the switching semi-elasticity $\tilde\varepsilon_{\text{int}} = \sigma (e/p - \kappa)$ and the demand semi-elasticity $\tilde\varepsilon_{\text{ext}} = |\eta| \kappa$, where $\kappa$ is cost-share-weighted emissions per dollar of energy spending. Show that a uniform tax conserves energy within a sector under this form and not under the old one. State plainly that v0.2 and earlier contained the extra factor, and fix the double-counting in v0.2's Appendix A.7 and A.9.
2. **Linear versus nonlinear.** The first-order TECP misses the full-model value by about 10 percent when coal prices rise sharply ($33.2 against $36.9 in the brief's example). Give the second-order correction or an exact iterative definition (solve for the uniform tax that matches the full-model emission cut), and say when the linear formula is good enough.
3. **Non-price instruments need theory, not just two routes.** For a binding tradable standard the shadow price is the permit price. For a non-tradable standard, the relevant price is the marginal compliance cost, which varies across firms, so the TECP needs the emission-weighted average. For procurement rules and legal obligations, back out the price from a modeled emission effect. Formalize each and state the identification assumptions. This is what makes the metric usable for policy crediting (1.1) and CBAM recognition (1.3).
4. **Elasticities and uncertainty.** Calibrate from meta-analyses (Labandeira et al. 2017; Stern 2012 for interfuel substitution), with short- and long-run values and their spread, and propagate the uncertainty into the TECP: a band, not a point.
5. **Comparison with existing metrics.** One table setting the TECP beside the OECD Effective Carbon Rate, IMF explicit and implicit prices, and the World Bank's total carbon price (Agnolucci et al. 2024) on the same stylized economy: what each counts, what each misses.
6. **Partial adjustment.** v0.2's Part II (CES and isoelastic forms; partial adjustment) is the dynamic foundation. Keep it, corrected, and show the TECP's short-run and long-run values.

**Minor comments**

7. State the TECP's uses with one paragraph each: crediting (1.1, Proposition 6), CBAM recognition (1.3), country diagnostics. Note that "the switching-margin price equals the feebate rate" holds only where routes make the same product.
8. Replace the workbook example (two sectors, renewables at $2/GJ, the old form). Update the workbook in `2.Source/` or flag it as superseded.
9. Clear the VERIFY items (EU 2023/956 Articles 3 and 9; Marcantonini and Ellerman volume).

**Recommendation:** major revision. The correction, the nonlinear treatment, non-price theory, uncertainty and the comparison table.

## Part 2. Outline of the working paper (about 8,000–10,000 words plus appendices)

**Front matter.** Title as the brief: "Measure Carbon Pricing by the Emissions It Cuts: The Total Effective Carbon Price". Personal capacity. Abstract of about 150 words. JEL (H23, Q41, Q48, Q54, Q58, C43).

1. **Introduction** (900 words). Headline prices mislead; what the TECP measures; contributions: the corrected CES derivation, non-price extension, uncertainty, comparison; uses in the series.
2. **Related literature and existing metrics** (1,000 words; Appendix A for the full review). Table 1: metrics compared.
3. **Energy demand: nested CES with partial adjustment** (1,500 words). Notation; cost function; fuel shares; the isoelastic form; partial adjustment.
4. **The TECP** (1,500 words). Definition (exact and first-order); Proposition 1 (first-order TECP formula); Proposition 2 (uniform-tax energy conservation within sectors; the old form violates it); decomposition by sector and margin; Figure 1.
5. **Beyond first order** (800 words). Second-order term or exact iterative definition; accuracy (Figure 2).
6. **Non-price instruments** (1,300 words). Tradable standards; non-tradable standards with heterogeneous compliance costs; mandates and procurement rules; legal obligations; Propositions 3–4; identification.
7. **Calibration and uncertainty** (1,000 words). Elasticities from meta-analyses (Table 2); Monte Carlo band for the worked example (Figure 3).
8. **Worked example** (1,000 words). The three-sector economy: tax, subsidy, standard; TECP against explicit-price metrics (Table 3).
9. **Uses** (700 words). Crediting, CBAM recognition, country diagnostics.
10. **Conclusion** (300 words).

**Appendices.** A: literature review (from `5.Notes/LiteratureAppendix-draft.md`). B: derivations and proofs, including the correction to v0.2. C: CES and isoelastic forms; partial adjustment (corrected from v0.2 Part II). D: code and calibration.
