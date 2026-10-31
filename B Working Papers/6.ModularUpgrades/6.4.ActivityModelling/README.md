# 4.7 Activity Levels Across CPAT, SISEPUEDE, CBAM and FTT

**Status:** first full draft, version 0.1 (29 October 2026). One medium-length working paper (about 4,900 words of body), companion to the CPAT-AI repository. Awaiting Stephen's peer review. Series plan: `../SeriesArchitecture.md`. 30 Oct 2026: the CPAT road-transport passage (sections 1, 2 and 5) corrected to match CPAT-AI register issue I100 (co-benefits always use the engineer fleet model's vehicle-km); the earlier claims that the co-benefits module ignores electric vehicles and uses a driving elasticity twice the fleet model's are removed.

**Question.** How can the activity levels in CPAT, SISEPUEDE, the CBAM Policy Tool (paper 4.5) and FTT be put on one footing so that the four models can be linked?

**Answer.** A common activity layer: ten activities in common units, each grown by one constant-elasticity rule in population, income per person and the cost of the energy service, from one set of drivers (IMF WEO, UN WPP) and one base year, spliced onto each model's own data, with the price term applied only where the receiving model has none (SISEPUEDE, FTT). One sector concordance table (Table 1). Propositions: the population exponent matters only where the income elasticity is not 1; a price response applied in the layer and the model doubles; a car stock growing faster than travel needs a cap.

## Files

| File | What |
|---|---|
| `ActivityModelling.qmd` / `.docx` / `.bib` | Working paper master (version 0.1), rendered with pandoc |
| `2.Source/activity_layer.py` | Table 3 (stylized ten-year growth, β = 1 variant, price responses) and the Proposition 3 crossing times |
| `3.RelatedPiecesAndLinks/CDPM-ActivityLevels-SISEPUEDE-CPAT-CBAM-FTT.docx` | Source design note |

Regenerate: `python3 2.Source/activity_layer.py`, then from the folder root `pandoc ActivityModelling.qmd -f markdown --citeproc --bibliography=ActivityModelling.bib --csl=<chicago-author-date.csl> --resource-path=. -o ActivityModelling.docx`.

## Sources used

- The source design note (method, parameter tables, model appendices, worked example), condensed.
- CPAT public documentation: `cpat_ai/docs/CPAT_full_documentation_qmd/03_Mitigation.qmd` (fuel equation, income and price elasticities, power demand) and `07_Road_Transport.qmd`; CPAT-AI `docs/CPAT_ai_documentation_qmd/06_Transport.qmd` (engineer road model: Gompertz ownership, logit EV choice).
- SISEPUEDE: public IDB–RAND report (Kalra et al. 2023, DOI 10.18235/0005330) and the public repository github.com/jcsyme/sisepuede (existence verified; equations as read in the source note).
- FTT: public repository github.com/cpmodel/FTT_StandAlone and readthedocs (verified); Mercure (2012), Mercure et al. (2016, 2018), Knobloch et al. (2019), Vercoulen et al. (2023).

## Held back for confidentiality

- All Egypt figures in the source note (CBAM tool output and prices, CPAT Egypt workbook values, FTT's shipped Egypt baseline, Egypt SISEPUEDE elasticities) are omitted; the border-adjustment tool is described by method and its generic judgment elasticities only.
- The CPAT road transport methodology note "shared October 2026" (not public) is not cited; the fleet model is described from the public CPAT-AI documentation.
- Legacy CPAT workbook build numbers and country workbook values are not cited.

## Open items for review

- Price elasticities for steel, aluminum, fertilizer and clinker are the tool's judgment values; the paper says so. Paper 4.4 may want to cross-check.
- The −0.1 fuel-price elasticity of tonne-km is attributed to de Jong et al. (2010) via the source note; the report's headline figures are elasticities to total transport cost, so check the conversion.
- The claim that FTT has no car data for 21 of 71 regions and no standalone steel module comes from the source note's reading of the repository (commit 8cf4bfd); recheck against the current repository.
