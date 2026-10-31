# 5.4 Are CPAT's Price Elasticities Right? A Check Against the Evidence

**Status (31 Oct 2026):** working paper v0.2 (peer-reviewed, references re-checked, executive summary added); policy brief v1.0 (Climate Fiscal Policy Brief No. 5.4, key `CFPB54`; working paper key `StrettonWP54`); ten-slide deck. About 6,600 words of body.

**Question and answer.** Are the default price elasticities in the Climate Policy Assessment Tool (CPAT) consistent with the published evidence? Mostly, and often on the cautious side: eight of ten main fuel-sector pairs lie within the published long-run range, six below the median estimate; diesel in industry and gasoline in services (about −1.05) are too high, electricity in services is at the elastic edge, and road gasoline is twice the estimate corrected for publication bias. The bigger problems are structural: CPAT applies the full long-run response in one year (overstating five-year responses by about 30–110 percent, 45–72 percent in the central case) and has almost no cross-price terms.

## Files

| File | What it is |
|---|---|
| `ElasticityValidation.qmd` | Working paper master (v0.2) |
| `ElasticityValidation.bib` | References; each entry's `note` says what was read and when |
| `ElasticityValidation.docx` | Rendered with pandoc (see below) |
| `1.Presentation/Brief-ElasticityValidation.qmd`, `.bib`, `.docx` | Policy brief master (v1.0); its `.bib` is copied from the working paper's |
| `1.Presentation/figures/make_figures.py` | Regenerates the working paper's figures and copies them for the brief |
| `1.Presentation/slides.json`, `Slides-ElasticityValidation.pptx` | Deck (ten slides), built with `H Writing Instructions/Writing Standards/templates/make_deck.py` |
| `2.Source/elasticity_check.py` | All analysis: CPAT totals, evidence register and classification, income table, timing with bounds, TECP implications, both figures |
| `2.Source/tecp_core.py` | Paper 6.1's TECP model (v0.3), copied unchanged so this folder runs alone |
| `2.Source/data/cpat_legacy_elasticities.csv` | CPAT default elasticities (legacy CPAT 1.0pre public release), from the CPAT-AI repository |
| `2.Source/data/CPATPriceElasticities.xlsx` | The simplified by-fuel set kept with CPAT's TECP validation files (`cpat_ai/other/tecp_and_validation`) |
| `2.Source/table_*.csv`, `2.Source/figures/` | Outputs of `elasticity_check.py` |
| `5.Notes/PeerReview-2026-10-31.md`, `5.Notes/BibCheck-2026-10-31.md` | Peer review of v0.1 and the reference check |
| `8.PreviousVersions/` | v0.1 working paper (qmd, docx, bib), old deck and slides.json, old script and figure |

Run: `cd 2.Source && python3 elasticity_check.py` (numpy, matplotlib).

## Rendering

From this folder (and the same from `1.Presentation/` for the brief):

```bash
F="<repo>/H Writing Instructions/Scripts/Website"; CSL="<repo>/E Website/chicago-author-date.csl"
pandoc ElasticityValidation.qmd -f markdown --lua-filter="$F/quarto-xref.lua" --lua-filter="$F/web-links.lua" \
  --citeproc --bibliography=ElasticityValidation.bib --csl="$CSL" -o ElasticityValidation.docx
```

`2.Source/xref.py` is the older pre-processor used for v0.1; the shared `quarto-xref.lua` filter replaces it.

## Sources and confidentiality

Only public sources: the public CPAT-AI repository (documentation `docs/CPAT_full_documentation_qmd/03_Mitigation.qmd`, public data under `data/`, `other/tecp_and_validation/`), the World Bank's publicly disclosed CPAT Technical Notes (August 2022), the IMF working paper by Black et al. (2022), and published articles. No country results are used. The Total Carbon Price figures are the World Bank's published dataset as kept in the CPAT-AI repository.

## Open items

- The 2017 Labandeira et al. article could not be read in full; the paper reports CPAT's reproduction and the authors' 2016 published summary side by side.
- No coal evidence outside China and no biomass meta-analysis were found.
