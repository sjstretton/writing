# 3.4 The Energy Transition Swaps a Fuel Bill for a Capital Bill

**Status:** Theory and Research Note No. 3.4, v0.2 (20 November 2026), after a referee-style peer review of v0.1 (`5.Notes/PeerReview-2026-11-20.md`). New research awaiting Stephen's review; not on the website; no brief or deck. v0.1 is in `8.PreviousVersions/`. Joins `C Policy and FInance/3.FinanceAndRisk/` once reviewed. A lead-in to the work on a global green deal.

**Question.** What do the stylized facts of the energy transition imply for macroeconomic policy, and what should the World Bank offer in response?

**Answer.** The transition swaps a fuel bill for a capital bill, so the cost of capital becomes the price of energy. Thirty stylized facts, each checked against evidence, give five implications: (1) the cost of capital is the macroeconomic variable; (2) price rises have diminishing returns while deployment has increasing returns; (3) the fiscal question moves from subsidies to guarantees; (4) the external accounts worsen before they improve; (5) a high cost of capital hides the cost of waiting, and the capacity to move fast must come from outside consortia. For Egypt (illustrative tool results on public data), a rapid transition costs a net 1.8 percent of GDP a year by 2035 at a 10.3 percent cost of capital and 0.2 percent at 6 percent. Five simple World Bank products follow, from papers 3.1, 3.2, 4.1, 4.2 and 4.3: a payment guarantee, a refinancing bond, a grid loan, a reform-linked guarantee line and a currency window, with a buffer fund behind them.

**Length.** Executive summary two pages; report twelve pages; then references and two appendices (evidence by fact; method).

## Files

| File | What |
|---|---|
| `EnergyTransitionMacroeconomics.qmd` | Master (v0.2) |
| `EnergyTransitionMacroeconomics.bib` | References. Entries reused from papers 1.1, 1.2, 3.1, 4.1, 6.3 and 6.5 keep the verification notes made there; new entries were checked on 20 Nov 2026 and each note says what was read |
| `EnergyTransitionMacroeconomics.docx`, `.pdf` | Rendered in the house format (the PDF is made from the Word file with LibreOffice, because Quarto is not installed in the cloud session) |
| `2.Source/egypt_estimates.py`, `egypt_estimates_output.txt`, `egypt_*.csv`, `returns_illustration.csv` | The Egypt estimates and the diminishing-returns illustration. Reads the investment model and the macro models of the Climate Fiscal AI Tools read-only (`--tools` path); public data only. Every Egypt number in the note is in the output file |
| `2.Source/make_figures.py`, `2.Source/figures/` | Four figures made from the CSVs (three are used in the note; the power unit-cost figure is spare) |
| `5.Notes/EvidenceCheck-2026-11-20-*.md` | The record of what each cited source says: stylized facts, Egypt, development finance, learning rates and scale. Items tagged [S] were seen only in search summaries and are not relied on in the note |
| `5.Notes/PeerReview-2026-11-20.md` | The peer review of v0.1, and what v0.2 did about each point |
| `8.PreviousVersions/` | v0.1 (qmd, docx, pdf) |

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

Illustrative tool results on public data (the IMF's fossil fuel subsidies dataset, Ember, the IMF World Economic Outlook, IRENA). Not official estimates. **Not yet cleared by Stephen for publication**: the note is on a working branch of a public repository and is not on the website. No World Bank internal material is used, and no result from the Climate Policy Assessment Tool's proprietary data (its Egypt run sits on a proprietary data edition and was left out for that reason).

Two changes to the tool's defaults for Egypt, both reported as sensitivities in Appendix B:

1. **Capital at world prices.** The tool scales capital costs by the local price level (0.41 for Egypt after the 2024 float). Note 6.8 v0.3 drops price-level scaling, and Egyptian contract costs match world costs. At the tool default the program is a net saving at either cost of capital.
2. **No new gas plant on either path.** The tool replaces a thirtieth of the fossil fleet each year; Egypt has about 61 GW of capacity against a 40 GW peak, so the tool would credit the transition with avoiding plant that is not needed this decade.

## Open items for Stephen

- Clear (or not) the Egypt estimates for a public repository and for the website.
- Confirm the number (3.4) and the series line.
- Confirm the two changes to the tool's defaults, and whether the tool itself should change.
- The currency window (product 5) and pensions (fact 21) have the thinnest evidence; decide whether they stay.
- Three checks before the estimates are used: Egyptian plant data for industry and buildings; an hourly power model for storage and grids; reconciliation with the budget and the state energy companies' accounts.
