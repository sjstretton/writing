# 5.1 The CPAT Mitigation Module: Methods in Brief

**Status:** draft v0.1 (29 Oct 2026), written by an AI agent overnight for Stephen's review. Not yet peer reviewed; not for publication until reviewed.

**Question and answer.** What does the CPAT mitigation module actually compute? A chain of six blocks, each a few equations long: a price identity with a carbon charge; constant-elasticity fuel demand with usage and efficiency margins; an engineering power model (logit dispatch, stock-flow capacity, logit investment within scale-up limits, storage charge); emissions and revenue identities; and a one-year-lagged fiscal-multiplier rule for GDP. The paper states the corrected method (Excel-AI / Coded CPAT) and proposes a penalty-based alternative to the logit investment rule.

## Files

| File | What |
|---|---|
| `CPATMitigationMethods.qmd` | Master (v0.1), about 9,100 words to the references plus 800 in two appendices |
| `CPATMitigationMethods.bib` | References, each checked on 29 Oct 2026 (Crossref or live public URL) |
| `CPATMitigationMethods.docx` | Rendered with pandoc + citeproc (Chicago author-date) |
| `2.Source/worked_examples.py` | Demand-response table (Table 1) and logit vs velocity investment shares (Table 2); also checks the background note's example |
| `2.Source/make_figures.py` | Figure 1 (module flow) and Figure 2 (investment shares vs carbon price) into `2.Source/figures/` |
| `3.RelatedPiecesAndLinks/PowerInvestmentEquations/` | Background note on penalty-based investment allocation (source for Section 7 and Appendix B) |

Render: from this folder, `pandoc CPATMitigationMethods.qmd -f markdown --citeproc --bibliography=CPATMitigationMethods.bib --csl=<chicago-author-date.csl> --resource-path=. -o CPATMitigationMethods.docx`. Regenerate figures first with `python3 2.Source/make_figures.py`.

## Sources used

- Public CPAT documentation (cpmodel.github.io/cpat_public), chapters 2 (Summary) and 3 (Mitigation), via `cpat_ai/docs/CPAT_full_documentation_qmd/02_Summary.qmd` and `03_Mitigation.qmd`.
- CPAT-AI (public repo `cpmodelai/cpat_ai`): `docs/CPAT_ai_documentation_qmd/04_Prices`, `05_Power`, `06_Transport`, `07_Emissions`; `docs/CPAT_coded_documentation_qmd/A_Equations`, `08_Mitigation_blocks`; `excel_ai/BUGS.md` (incl. documentation bugs DOC1-DOC20), `excel_ai/ISSUES.md`; legacy elasticity extract `data/mvp_legacy_extracts/elasticities.csv`.
- Background note `3.RelatedPiecesAndLinks/PowerInvestmentEquations/Background-Index.qmd` (2025).
- Published references: IMF/World Bank CPAT papers (Black et al. 2023; CPAT Technical Notes 2022; IMF 2019 Paris policy paper; Black et al. 2022), Labandeira et al. 2017, Burke and Csereklyei 2016, Gertler et al. 2016, Dimitropoulos et al. 2018, Malla and Timilsina 2014, Bogdanov et al. 2019, Ricke et al. 2018, Mercure 2012, Bauer et al. 2025, IPCC 2006.

**Credits.** Mitigation chapter authors (Campmas, Bastidas, Lelouch, Gawryluk, Agnolucci, Stretton); earlier work by Parry, Black, Zhunussova, Vernon, Mylonas; power engineer model with Phillip Hannam. Credited in the first-page footnote.

## Corrections found while writing

- The background note's proportional renormalization of negative velocity-rule shares is not the minimizer of its own objective; the exact active-set solution differs (its example: 40/30/20/10 percent, not 36.4/28.8/21.2/13.6). Section 7 and Appendix B use the exact rule.
- The background note's bib has wrong DOIs/volumes for Mercure (2012) and Bauer, Hallegatte and McIsaac (2025); corrected in this paper's bib.

## Held back

- No country results from CPAT runs; the worked examples use stylized prices and costs (labelled) with IPCC default emission factors and legacy default elasticities. Excel-AI's Egypt test numbers are not reproduced.
- The SharePoint links to internal CPAT methodological notes that appear in `02_Summary.qmd` are not cited.
- No unverified markers remain.
