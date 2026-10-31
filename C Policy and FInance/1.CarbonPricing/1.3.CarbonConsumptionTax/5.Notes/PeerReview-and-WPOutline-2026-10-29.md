# Paper 1.6: peer review of the brief, and outline of the working paper

Review of *Climate Fiscal Policy Brief No. 1.6* (`1.Presentation/Brief-CarbonConsumptionTax.qmd`, Oct 2026), written as a referee report. The outline that follows is the plan for the academic working paper (master `CarbonConsumptionTax.qmd`, to become v0.2; the current v0.1 moves to `8.PreviousVersions/`).

## Part 1. Referee report

**Summary.** The brief proposes a carbon component of VAT on all goods consumed in the EU, with rebuttable product-category defaults for imports, plus a forward-announced obligation on energy suppliers for fuel burned at home. It is careful on arithmetic and candid on the legal basis. As a policy brief it works. The working paper needs five things the brief cannot carry.

**Major comments**

1. **The economics of a carbon component inside VAT are asserted, not shown.** Show formally that a per-tonne charge credited through the VAT chain taxes each firm's carbon *added*, so the final consumer bears the full embodied carbon of the good. That is the analogue of VAT taxing value added, and it is the central mechanism. State the conditions: full input crediting, a correct default intensity at each stage, and no exempt stage breaking the chain. Exempt sectors such as financial services and housing break the credit chain for VAT and will break it for carbon. Say what happens at an exemption.
2. **Default intensities are the whole design, and the brief has no numbers.** The working paper needs a table of product-category intensities (kg CO₂ per euro) from an input–output source such as EXIOBASE, or the consumption-based accounts used by Steininger et al. or Pollitt, Neuhoff and Lin, for perhaps 15–20 categories. It also needs a calculation of the break-even basket intensity for the actual EU VAT base. Without it the neutrality rule cannot be calibrated.
3. **Incidence and distribution.** VAT is mildly regressive on income and close to proportional on lifetime consumption. A carbon component shifts the burden toward carbon-intensive budget shares: energy, food and transport for lower deciles. Present the distributional effect by decile from household budget data, or from published estimates, and show how the value-component cut offsets it.
4. **The interaction with the production track and with CBAM needs a precise statement.** Each tonne should bear one price: the carbon component deducts carbon prices paid upstream (ETS, CBAM, the energy obligation, recognized foreign prices). Write this as a formula, and show that a good produced under a revenue-neutral feebate is charged in full at consumption. That is the two-track architecture of paper 1.1, and the link should be explicit.
5. **Legal analysis.** The brief's treatment of Art. 113 and Art. 192(2)(a) TFEU, Art. 97 and Art. 401 of the VAT Directive, and GATT III:2 is right in direction but needs sources and a fuller argument, for example the Court's case law on what counts as a turnover tax under Art. 401. Mark clearly what is settled and what is not.

**Minor comments**

6. Drop references to "the working paper" as a separate earlier document: the working paper is now the paper itself. Earlier versions can be cited as v0.1 in a footnote if needed.
7. The forward obligation: compare explicitly with ETS2 (Directive 2023/959) and the Fuel Quality Directive, and say what is new: a published price floor fixed a decade ahead.
8. Fraud: VAT carousel fraud is large; say why a carbon column adds limited new risk (defaults by customs category, rebuttal audited) and where it adds real risk (misdeclared categories).
9. The time-inconsistency argument should cite the credibility literature (Kydland and Prescott; Helm, Hepburn and Mash; Chiappinelli and Neuhoff on carbon contracts for difference) and be tied to the oligopoly structure of fuel supply.
10. Several bib entries still carry VERIFY (EU legal texts, ETS2 start date, the IPCC gas factor). Resolve them; the EUR-Lex PDFs are in the download batch file.

**Recommendation:** major revision. The core design is sound and novel in its combination; the paper needs the VAT-chain theorem, calibrated defaults, distribution and the legal analysis.

## Part 2. Outline of the working paper (about 8,000–10,000 words plus appendices)

**Front matter.** Title as the brief: "Carbon Consumption Tax: A Carbon Component in VAT and a Forward Obligation on Energy Suppliers". Personal capacity. Abstract of about 150 words. Keywords, JEL (H23, H25, F18, Q54, Q58).

1. **Introduction** (900 words). The unpriced carbon in EU consumption (consumption versus territorial accounts); the two-part proposal; contributions: the VAT-chain result, calibrated defaults, the neutrality rule, the legal map; the series (1.1).
2. **Related literature** (900 words; full review in Appendix A). Consumption-based accounting; consumption charges on materials (the "climate contribution"); destination-based taxation and VAT; border adjustments; credibility of carbon policy.
3. **The carbon component in the VAT chain** (1,500 words). A model of an $n$-stage supply chain with a value tax rate $v$ and a carbon charge $P$ on default intensity. **Proposition 1:** with full crediting, each firm pays $P$ times its carbon added, and the consumer bears $P$ times the good's embodied carbon. **Proposition 2:** an exempt stage breaks the chain: carbon upstream of it is charged to the exempt firm as a cost and cascades. **Proposition 3:** deduction of upstream carbon prices gives one price per tonne. Worked example with three stages.
4. **Default intensities and rebuttal** (1,300 words). Product-category defaults from input–output data, with Table 1 (calibrated intensities for 15–20 categories; sources). Same for every origin; rebuttal by verified data; incentives for exporters (link to 1.1, Proposition 7). Trade law: GATT III:2 and like products.
5. **Fiscal design: the carbon charge partly replaces VAT** (1,200 words). Break-even intensity; Table 2 (revenue by basket intensity); the neutrality rule (the value cut equals the previous year's carbon receipts); Art. 97's 15 percent floor; Figure 1 (effective rates by intensity, 2027–2037).
6. **Distribution** (900 words). Incidence by decile; offset through the value cut; options for targeted rebates.
7. **The forward obligation on energy suppliers** (1,200 words). Market structure of fuel supply; time inconsistency and credibility; design as ETS2 with a published price floor; interaction with the VAT component and with the power-sector feebate (1.2).
8. **Legal basis** (1,000 words). Art. 113 versus Art. 192(2)(a); the CBAM precedent; Art. 401; coalition routes.
9. **Administration and fraud** (600 words).
10. **Conclusion** (300 words).

**Appendices.** A: literature review (from `5.Notes/LiteratureAppendix-draft.md`). B: proofs of Propositions 1–3. C: calibration of defaults (data and code). D: recomputation of the v0.1 numbers (what held, what did not), from `1.Presentation/figures/make_figures.py`.
