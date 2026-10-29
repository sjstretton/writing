# 4.4 Are CPAT's Price Elasticities Right? A Check Against the Evidence

**Status:** working paper, version 0.1 (29 October 2026), first full draft for Stephen's review. About 5,600 words of body.

**Question and answer.** Are the default price elasticities in the Climate Policy Assessment Tool (CPAT) consistent with the published evidence? Mostly: seven of ten main fuel-sector pairs lie within the published long-run range; diesel in industry, gasoline in services and electricity in services are too high; road gasoline is double the publication-bias-corrected mean; natural gas sits at the inelastic end. The bigger problems are structural: CPAT applies the full long-run response in one year and has almost no cross-price terms.

## Files

| File | What it is |
|---|---|
| `ElasticityValidation.qmd` | Master (v0.1) |
| `ElasticityValidation.bib` | References; each entry's `note` says how it was verified |
| `ElasticityValidation.docx` | Rendered with pandoc (see below) |
| `2.Source/elasticity_check.py` | All analysis: CPAT totals, comparison and classification, income table, timing, TECP implications, both figures |
| `2.Source/tecp_core.py` | Paper 1.7's TECP model, copied unchanged so this folder runs alone |
| `2.Source/data/cpat_legacy_elasticities.csv` | CPAT default elasticities (legacy CPAT 1.0pre public release), copied from `cpat_ai/data/mvp_legacy_extracts/elasticities.csv` |
| `2.Source/data/CPATPriceElasticities.xlsx` | The simplified by-fuel set kept with CPAT's TECP validation files (`cpat_ai/other/tecp_and_validation`) |
| `2.Source/table_*.csv`, `2.Source/figures/` | Outputs of `elasticity_check.py` |

Run: `cd 2.Source && python3 elasticity_check.py` (numpy, matplotlib). Render: resolve the Quarto cross-references with a small pre-processor (the session used `xref.py`, which numbers sections, figures, tables and equations), then `pandoc <resolved>.md --citeproc --number-sections --bibliography=ElasticityValidation.bib --csl=chicago-author-date.csl -o ElasticityValidation.docx`. Quarto renders the qmd directly.

## Sources used

- CPAT-AI repository (public): `docs/CPAT_full_documentation_qmd/03_Mitigation.qmd` (fuel consumption dynamics, income and price elasticities, rebound, panel estimation of energy demand, Tables A–C), `data/mvp_legacy_extracts/elasticities.csv`, `other/tecp_and_validation/` (`CPATPriceElasticities.xlsx`, `All_data_TCP.xlsx`, `Total_Effective_Carbon_Price.pdf`).
- Paper 1.7 (Total Effective Carbon Price): CES demand system, partial adjustment, stylized economy and model code.
- Published evidence, each verified via Crossref and the abstract or an open working-paper version: Labandeira, Labeaga and López-Otero (2017); Havranek, Irsova and Janda (2012); Brons et al. (2008); Huntington, Barrios and Arora (2019, MPRA version read); Burke and Yang (2016); Burke and Liao (2015); Stern (2012); Zhu et al. (2018); Dahl (2012).
- Consistency with paper 4.3 (editor's note): panel estimates −0.19 (road gasoline) and −0.1 (residential electricity); ±2 SD elasticity sensitivity of the G20 cut from a $75 tax (29 percent; 7–39 percent). Default ranges from paper 4.1.

## Caveats and open items

- Labandeira et al.'s means are taken as reproduced in CPAT's documentation, and Dahl's survey values as reported by Huntington et al.; check against the originals before changing CPAT defaults.
- No coal evidence outside China and no biomass meta-analysis were found.
- Nothing confidential is used; the Total Carbon Price data are the World Bank's published dataset as kept in the public CPAT-AI repository.

## Rendering

Plain pandoc cannot resolve Quarto cross-references. Render with:

```bash
python3 2.Source/xref.py <Name>.qmd > /tmp/x.qmd   # numbers sections, tables, figures, equations
pandoc /tmp/x.qmd -f markdown --citeproc --bibliography=<Name>.bib --csl=chicago-author-date.csl --resource-path=. -o <Name>.docx
```

Check the script header for its exact usage.
