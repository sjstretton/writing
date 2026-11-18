# 5.1 The CPAT Mitigation Module: Methods in Brief

**Status:** working paper v0.3 (18 Nov 2026: Appendix B's active-set rule for the acceleration and combined rules corrected, found in the peer review of note 6.8; v0.2 in `8.PreviousVersions/`) and policy brief v1.0 (31 Oct 2026), after a referee-style peer review (`5.Notes/PeerReview-2026-10-31.md`) and a full reference check (`5.Notes/BibCheck-2026-10-31.md`). v0.1 (29 Oct 2026, agent draft) is in `8.PreviousVersions/`.

**Question and answer.** What does the CPAT mitigation module actually compute? A chain of six blocks and fourteen equations: a price identity with a carbon charge (with an asymmetric pass-through floor); constant-elasticity fuel demand with usage and efficiency margins; an engineering power model (logit dispatch, stock-flow capacity, logit investment within build-rate caps, storage charge); emissions and revenue identities; and a one-year-lagged fiscal-multiplier rule for output. The paper states the corrected method (Excel-AI / CPAT Python), shows that CPAT's investment logit is an entropy-penalized cost minimum, and proposes a quadratic-penalty (sparsemax) rule as a switchable alternative.

## Files

| File | What |
|---|---|
| `CPATMitigationMethods.qmd` | Working paper master (v0.2): executive summary, about 9,700 words of body to the references, two appendices |
| `CPATMitigationMethods.bib` | References, each checked on 31 Oct 2026 against the source; the `note` says what was read |
| `CPATMitigationMethods.docx` | Rendered with pandoc + quarto-xref.lua + web-links.lua + citeproc (Chicago author-date) |
| `1.Presentation/Brief-CPATMitigationMethods.qmd`, `.bib`, `.docx` | Climate Fiscal Policy Brief No. 5.1 (v1.0, new); `.bib` copied from the working paper's for the keys it cites |
| `1.Presentation/figures/make_figures.py` | Brief figure (investment shares, logit vs quadratic penalty), from `2.Source/worked_examples.py` |
| `1.Presentation/slides.json`, `Slides-CPATMitigationMethods.pptx` | Ten-slide deck on the shared builder (`make_deck.py`) |
| `2.Source/worked_examples.py` | Table 1 (demand response), Table 2 (logit vs velocity shares), the background-note example and the checks quoted in the text (entropy weight, irrelevant and duplicated technologies) |
| `2.Source/make_figures.py` | Figure 1 (module flow, with both lagged feedbacks) and Figure 2 (investment shares vs carbon price) into `2.Source/figures/` |
| `3.RelatedPiecesAndLinks/PowerInvestmentEquations/` | Background note on penalty-based investment allocation (source for the proposal and Appendix B) |
| `5.Notes/` | Peer review and reference check of 31 Oct 2026 |
| `8.PreviousVersions/` | v0.1 working paper (qmd, docx, bib), v0.1 deck and spec, v0.1 figures |

Render (from this folder; the brief the same way from `1.Presentation/`):

```bash
F="/home/user/writing/H Writing Instructions/Scripts/Website"; CSL="/home/user/writing/E Website/chicago-author-date.csl"
python3 2.Source/make_figures.py; python3 1.Presentation/figures/make_figures.py
pandoc CPATMitigationMethods.qmd -f markdown --lua-filter="$F/quarto-xref.lua" --lua-filter="$F/web-links.lua" --citeproc --bibliography=CPATMitigationMethods.bib --csl="$CSL" --resource-path=. -o CPATMitigationMethods.docx
```

## Sources used (all public)

- Public CPAT documentation, 2023 edition (cpmodel.github.io/cpat_public), chapters 2–4, read in the copy in the public CPAT-AI repository (`docs/CPAT_full_documentation_qmd/`), and its corrected edition of 31 Oct 2026 (Corrections chapter).
- CPAT-AI (public repository `cpmodelai/cpat_ai`, commit 108f976, Excel-AI release 1.2.1): `docs/CPAT_model_documentation_qmd/A_Equations.qmd`; `excel_ai/mitigation/docs/` (Equations, methods notes); `excel_ai/core/BUGS.md`, `ISSUES.md`, `CHANGELOG.md`; `data/Public01/tidy/xai_elasticities.csv`.
- Background note `3.RelatedPiecesAndLinks/PowerInvestmentEquations/Background-Index.qmd` (2025).
- Published references: see the `.bib`.

**Credits.** Mitigation chapter authors (Campmas, Bastidas, Lelouch, Gawryluk, Agnolucci, Stretton); earlier work by Parry, Black, Zhunussova, Vernon, Mylonas; power engineer model with Phillip Hannam; air-pollution module by Paulina Schulz-Antipa. Credited in the first-page footnote.

## Correction made in v0.3 (18 Nov 2026)

- Appendix B: when a technology that had a share last year drops out, the acceleration and combined rules must carry its lost share, $\lambda_a(1 - S_A)/|A|$; v0.2 omitted the term and gave shares summing to less than one (91.8 percent in the check case). New equation for the combined rule on an active set; one sentence after the combined rule in the main text; `2.Source/worked_examples.py` now computes the exact minimizer and checks it (46.7, 36.7, 16.7 percent). Results in the tables and figures are unchanged: they use the velocity rule, which was right.

## Corrections made in v0.2 (see the peer review)

- The documentation errors are now described as errors of the 2023 edition, corrected in the CPAT-AI edition of 31 Oct 2026.
- Register facts updated: 231 legacy bugs (was 228), paths and versions current; L6 re-described, L4, L15, L170 coded.
- Default cost of capital: the model uses a country rate plus a technology premium; the income-group rates (7.5–15 percent) are the documentation's description and an option. **Papers 5.0 and 6.3 repeat the income-group rates as the default and need the same fix.**
- Wind and solar caps: 2 points a year in most countries, higher for China and India in the current data; caps apply to effective capacity.
- The asymmetric floor on existing taxes (pass-through), the policy efficiency term and the recycled-revenue impulse added.
- The penalty rule restated against the logit as an entropy-penalized optimum (Anderson, de Palma and Thisse 1988) and sparsemax (Martins and Astudillo 2016); a wrong drawback (irrelevant technologies) replaced by the real one (duplicated technologies).
- Bauer, Hallegatte and McIsaac (2025) cut (content could not be read).
- "About eighteen equations" is now "fourteen" (the module; the proposal adds four). **Paper 5.0 still says "about eighteen equations".**

## Held back

- No country results from CPAT runs; the worked examples use stylized prices and costs (labelled) with IPCC default emission factors and legacy default elasticities. The public data edition holds perturbed Egypt values; nothing from it is reported.
- Internal CPAT methodological notes linked from the documentation's summary chapter, and a Public Finance Review mentioned there, are not cited.
- No unverified markers remain.
