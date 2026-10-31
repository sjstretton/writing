# 6.4 Activity Levels Across CPAT, SISEPUEDE, CBAM and FTT

**Status:** working paper v0.2 and policy brief v1.0 (Climate Fiscal Policy Brief No. 6.4, key CFPB64; working paper key StrettonWP64), 31 Oct 2026, after a referee-style peer review (`5.Notes/PeerReview-2026-10-31.md`) and a full reference check (`5.Notes/BibCheck-2026-10-31.md`). v0.1 (29 Oct 2026, agent draft) and its three-slide deck are in `8.PreviousVersions/`.

**Question.** How can the activity levels in CPAT, SISEPUEDE, the CBAM Policy Tool (paper 6.2) and FTT be put on one footing so that the four models can be linked?

**Answer.** A common activity layer: ten activities in common units, each grown by one constant-elasticity rule in population, income per person and the cost of the energy service, from one set of drivers (IMF WEO, UN WPP 2024) and one base year, spliced onto each model's own data, with the price term applied only where the receiving model has none (SISEPUEDE, FTT). One sector concordance (Table 1). Three checks: the population exponent matters only where the income elasticity is not 1 (up to 0.4 points a year); each activity's price response sits in exactly one model (including CPAT's engineering road model); car travel must be checked against total travel every year, because it overtakes it even under CPAT's saturating Gompertz ownership curve (year 54 from a 30 percent share).

## Files

| File | What |
|---|---|
| `ActivityModelling.qmd` | Working paper master (v0.2): executive summary (about 670 words), about 6,000 words of body, Appendix A (proofs) |
| `ActivityModelling.bib` | References, each checked on 31 Oct 2026 against the source; the `note` says what was read. CPAT entries share keys with paper 5.1 |
| `ActivityModelling.docx` | Rendered with pandoc + quarto-xref.lua + web-links.lua + citeproc (Chicago author-date) |
| `1.Presentation/Brief-ActivityModelling.qmd`, `.bib`, `.docx` | Climate Fiscal Policy Brief No. 6.4 (v1.0, new); `.bib` copied from the working paper's for the keys it cites |
| `1.Presentation/figures/make_figures.py`, `fig_activity.png` | Brief and deck figure (ten-year growth by activity), from `2.Source/activity_layer.py` |
| `1.Presentation/slides.json`, `Slides-ActivityModelling.pptx` | Ten-slide deck on the shared builder (`make_deck.py`) |
| `2.Source/activity_layer.py` | Every number in the worked example: Table 3, CPAT's income factor, Proposition 3 crossing times (constant elasticities and CPAT's Gompertz curve), the Gompertz-versus-line check, the steel and clinker example |
| `3.RelatedPiecesAndLinks/CDPM-ActivityLevels-SISEPUEDE-CPAT-CBAM-FTT.docx` | Source design note |
| `5.Notes/` | Peer review and reference check of 31 Oct 2026 |
| `8.PreviousVersions/` | v0.1 working paper (qmd, docx, bib), deck, slide spec, figure and scripts |

Render (from this folder; the brief the same way from `1.Presentation/`):

```bash
F="/home/user/writing/H Writing Instructions/Scripts/Website"; CSL="/home/user/writing/E Website/chicago-author-date.csl"
python3 2.Source/activity_layer.py; python3 1.Presentation/figures/make_figures.py
pandoc ActivityModelling.qmd -f markdown --lua-filter="$F/quarto-xref.lua" --lua-filter="$F/web-links.lua" --citeproc --bibliography=ActivityModelling.bib --csl="$CSL" --resource-path=. -o ActivityModelling.docx
```

## Sources used (all public)

- CPAT-AI (public repository `cpmodelai/cpat_ai`, commit 108f976): `docs/CPAT_model_documentation_qmd/` (03 Energy demand, 04 Power, 05 Road transport, A Equations), `data/Public01/tidy/xai_elasticities.csv`, `excel_ai/core/ISSUES.md` (I71, I100); the public CPAT documentation (2023 text) and its corrected edition of 31 Oct 2026.
- SISEPUEDE (public repository `jcsyme/sisepuede`, commit 9bf976c): `docs/source/`, `sisepuede/models/energy_consumption.py`, `ippu.py`, `utilities/_toolbox.py`, `ref/examples/input_data_frame.csv`; Kalra et al. (2023), DOI 10.18235/0005330.
- FTT (public repository `cpmodel/FTT_StandAlone`, commit 896a3ce): README, settings, mathematics documentation, update manuals, variable listing, `Inputs/S0/`, freight and sector-coupling code.
- Published references: see the `.bib`.

## Held back for confidentiality

- No country results. All Egypt figures in the source note (CBAM tool output and prices, CPAT Egypt workbook values, FTT's shipped Egypt baseline, Egypt SISEPUEDE elasticities) are omitted; the CBAM Policy Tool is described by method, and its output elasticities are stated as the author's judgment values. Egypt is among FTT's 21 regions without car data but is not named.
- The CPAT road transport methodology note (not public) is not cited; the fleet model is described from the public CPAT-AI documentation.
- SISEPUEDE country calibrations are not public; the paper reports only the public example (Costa Rica) and states the layer's household and industrial elasticities as the author's assumptions.

## Corrections made in v0.2 (see the peer review)

- CPAT electricity income elasticity: 0.8 (legacy), 0.92 at \$3,000, 0.48 above \$22,000 (was 0.75, 0.83, 0.43).
- Km per car: income elasticity 0.1 (CPAT fleet model's legacy value; 0.05 is the unused alternative). Vans and trucks' −0.2 now from de Jong et al. only.
- Car-ownership curve attributed to CPAT's Gompertz constants; shape to Dargay and Gately (1999); Dargay, Gately and Sommer (2007) for saturation only.
- Passenger travel elasticity 1.0 (Schäfer and Victor 2000), not 1.24; travel grows 35 percent in ten years (was 41).
- Proposition 3 restated; crossing after 56 years (constant elasticities) and year 54 with CPAT's Gompertz curve (was 76 years, with saturation said to solve it).
- Steel-versus-cement paragraph rewritten: with the tool's elasticities output falls about the same (6.0 and 5.0 percent, stylized).
- CBAM Policy Tool equation matched to paper 6.2; "border-adjustment tool" renamed.
- FTT: E3ME claim re-worded; sector coupling adds changes against the baseline run; transport data year added.
- Liddle (2014) re-worded; Helgesen and Tomasgard re-scoped; Riahi et al. (2017) and Wene (1996) added as the closest prior work.

## Open items for the coordinator

- PAPERS.md and the website need the new brief (CFPB64). Suggested series bib entry: `@techreport{CFPB64, author={Stretton, Stephen J.}, title={Activity Levels Across {CPAT}, {SISEPUEDE}, {CBAM} and {FTT}}, institution={Climate Fiscal Policy Briefs}, number={6.4}, year={2026}}`. The title is unchanged.
