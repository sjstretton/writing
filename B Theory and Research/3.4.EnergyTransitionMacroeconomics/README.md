# 3.4 The Energy Transition Swaps a Fuel Bill for a Capital Bill

**Status:** Theory and Research Note No. 3.4, v0.3 (20 November 2026). A review of the literature on 32 stylized facts of the energy transition and what they mean for macroeconomic policy. Peer-reviewed twice by an independent referee (v0.1 and v0.2; reports and responses in `5.Notes/`). New research awaiting Stephen's review; not on the website; no brief or deck. Joins `C Policy and FInance/3.FinanceAndRisk/` once reviewed. A lead-in to the work on a global green deal.

**Question.** What do the stylized facts of the energy transition imply for macroeconomic policy, for carbon pricing and for development finance?

**Answer.** The transition swaps a fuel bill for a capital bill, so energy moves from the current account to the balance sheet and the cost of capital becomes the price of energy. Investment follows the relative price that is expected to last, and policy uncertainty makes waiting valuable. Price rises have diminishing returns; deployment has increasing returns. The first-best carbon price is a benchmark; the pragmatic price is one part of a package that also lowers the cost of capital and turns promises into contracts (seven rules in Section 5). Finance is the binding constraint in developing countries. Three simple products the World Bank could offer follow, from papers 3.1, 3.2 and 4.1–4.3: a payment guarantee on the power contract, a refinancing guarantee, and a guarantee line that grows with reform, with a buffer fund of donor capital behind them. Ten indicators track an economy that is moving from a fuel bill to a capital bill.

**Form.** Executive summary two pages; report twelve pages (eight sections); references; Appendix A (the 32 facts with evidence and a verdict on each); Appendix B (first estimates for Egypt by sector at a local and a de-risked cost of capital). The modeling is in Appendix B only.

## Files

| File | What |
|---|---|
| `EnergyTransitionMacroeconomics.qmd` | Master (v0.3) |
| `EnergyTransitionMacroeconomics.bib` | References. Entries reused from papers 1.1, 1.2, 3.1, 4.1, 6.3 and 6.5 keep the verification notes made there; new entries were checked on 20 Nov 2026 and each note says what was read |
| `EnergyTransitionMacroeconomics.docx`, `.pdf` | Rendered in the house format (the PDF is made from the Word file with LibreOffice, because Quarto is not installed in the cloud session) |
| `2.Source/egypt_estimates.py`, `egypt_estimates_output.txt`, `egypt_*.csv`, `returns_illustration.csv` | The Egypt estimates and the price-versus-deployment illustration. Reads the investment model and the macro models of the Climate Fiscal AI Tools read-only (`--tools` path); public data only. Every Egypt number in the note is in the output file |
| `2.Source/make_figures.py`, `2.Source/figures/` | Figures made from the CSVs (Figures 1 to 3 are used; the power unit-cost figure is spare) |
| `5.Notes/EvidenceCheck-2026-11-20-*.md` | What each cited data source says: stylized facts, Egypt, development finance, learning rates and scale. Items tagged [S] were seen only in search summaries and are not relied on |
| `5.Notes/LiteratureCheck-2026-11-20-*.md` | What each cited paper says, from its abstract or text: carbon pricing theory (40 items); expectations, investment under uncertainty and macroeconomic effects (55 items) |
| `5.Notes/PeerReview-2026-11-20.md`, `PeerReview2-2026-11-20.md`, `ResponseToReviews-2026-11-20.md` | The two referee reports and what was done about each point |
| `8.PreviousVersions/` | v0.1 (first draft, advocacy and modeling in the body) and v0.2 (the literature-review rewrite, before the second review) |

## Render

From the paper folder (pandoc with the cross-reference filter, then the house filter and styles; `render_docx.py` in `B Theory and Research` does not yet apply the cross-reference filter):

```bash
F="../../H Writing Instructions/Scripts/Website"; EXT="../../H Writing Instructions/Writing Standards/templates/_extensions/working-paper"
# shim for the two Quarto functions the house filter calls, as in ../render_docx.py
pandoc EnergyTransitionMacroeconomics.qmd -f markdown --lua-filter="$F/quarto-xref.lua" --lua-filter=<shim + $EXT/working-paper.lua> \
  --citeproc --csl="../../E Website/chicago-author-date.csl" --reference-doc="$EXT/reference.docx" -o EnergyTransitionMacroeconomics.docx
soffice --headless --convert-to pdf EnergyTransitionMacroeconomics.docx
```

Regenerate the numbers and figures: `cd 2.Source && python3 egypt_estimates.py --tools <path to climate-fiscal-ai-tools> && python3 make_figures.py`.

## Egypt results: status and sources

The author's illustrative calculations on public data (the IMF's fossil fuel subsidies dataset, Ember, the IMF World Economic Outlook, IRENA). Not official estimates of any institution. **Not yet cleared by Stephen for publication**: the note is on a working branch of a public repository and is not on the website. No World Bank internal material is used, and no result from the Climate Policy Assessment Tool's proprietary data (its Egypt run sits on a proprietary data edition and was left out for that reason).

Both costs of capital are in real terms: local 8.2 percent (10.3 percent in nominal dollars, from two IRENA figures for solar in Egypt, less 2 percent inflation) and de-risked 3.9 percent (6 percent nominal, the upper end of an IBRD loan of the longest maturity in November 2026). The de-risked rate is a bound, not a forecast.

Three choices differ from the tool's defaults, each reported as a sensitivity in Appendix B:

1. **Capital at world prices.** The tool scales capital costs by the local price level (0.41 for Egypt after the 2024 float). Note 6.8 v0.3 drops price-level scaling, and Egyptian contract costs match world costs. At the tool default the program is a net saving at either cost of capital.
2. **No new gas plant on either path.** The tool replaces a thirtieth of the fossil fleet each year; Egypt has about 61 GW of capacity against a 40 GW peak, so the tool would credit the transition with avoiding plant that is not needed this decade.
3. **Gas at the import price, \$12 per million British thermal units.** Egypt has been a net importer since 2024 and paid about \$13 in the first half of 2026; the tool's data hold the IMF's 2024 supply cost of \$8.8.

## Open items for Stephen

- Clear (or not) the Egypt estimates for a public repository and for the website.
- Confirm the number (3.4) and the series line.
- Confirm the three choices above, and whether the tool itself should change.
- Facts 22 (currency swaps between developing countries) and 23 (pension funds) have the thinnest evidence; decide whether they stay as facts or become questions for the global green deal paper.
- The import share of one-half is an assumption; a published split would replace it.
- Three checks before the estimates are used: Egyptian plant data for industry and buildings; an hourly power model for storage and grids; reconciliation with the budget and the state energy companies' accounts.
- The claims that rest on working-paper versions of published articles are marked in the bibliography notes (Aghion et al. 2016; Li, Linn and Muehlegger 2014; Labandeira et al. 2017). Check the published numbers before the note goes further.
