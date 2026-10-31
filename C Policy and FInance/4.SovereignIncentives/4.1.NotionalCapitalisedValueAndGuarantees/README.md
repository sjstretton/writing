# 4.1 Notional Capitalized Value and Guarantees

**Status:** working paper v0.2 and Climate Fiscal Policy Brief No. 4.1 v1.0 (31 October 2026), after a peer review (`5.Notes/PeerReview-2026-10-31.md`) and a full reference check (`5.Notes/BibCheck-2026-10-31.md`); ten-slide deck rebuilt. v0.1 files are in `8.PreviousVersions/`. Flagship of series 4 (Sovereign Incentives).

**Title:** Reward the Stock as Well as the Flow: Notional Capitalized Value and Guarantee-Based Climate Incentives.

**Question.** How can the international system give a government a large, early and credible incentive to protect carbon stocks and cut emissions, without a cash transfer that donors will not vote for?

**Answer.** Credit each country with a notional capitalized value: a balance opened by its carbon stock (at a low stock price) and debited for every tonne emitted above an agreed allowance (at a higher, uniform debit price). The balance sets guarantee capacity on eligible green borrowing; the country gains the spread saved, donors bear expected loss on a buffer they hold. Capacity declining at the rate technology costs fall is the cheapest schedule that makes acting now beat waiting.

## Files

| File | What |
|---|---|
| `NotionalCapitalisedValueAndGuarantees.qmd` | Working paper master, version 0.2 (executive summary about 690 words; body about 10,300 words; appendices about 1,400) |
| `NotionalCapitalisedValueAndGuarantees.bib` / `.docx` | Bibliography; rendered Word file |
| `1.Presentation/Brief-NotionalCapitalisedValueAndGuarantees.qmd` / `.bib` / `.docx` | Climate Fiscal Policy Brief No. 4.1, brief version 1.0 (about 2,000 words of text) |
| `1.Presentation/slides.json` / `Slides-NotionalCapitalisedValueAndGuarantees.pptx` | Ten-slide deck, built with `H Writing Instructions/Writing Standards/templates/make_deck.py` |
| `1.Presentation/figures/make_figures.py` | Draws the brief's two figures (reuses `2.Source`) |
| `2.Source/model.py` | All calibration numbers (prints them) |
| `2.Source/make_wp_figures.py` | Working paper figures, written to `2.Source/figures/` |
| `2.Source/render.py` | Renders a qmd to docx with pandoc, resolving Quarto cross-references (Quarto is not installed) |
| `5.Notes/` | Working notes |

Render both forms with pandoc and the site filters (`quarto-xref.lua`, `web-links.lua`) as in `H Writing Instructions/Writing Standards/briefing-series-spec.md`. `2.Source/render.py` is the older route and is superseded.

## Lineage and sources

- *Time and Chance* ch. 21 (Notional Capitalized Carbon Value, the only worked version), ch. 20 (interest on a notional Amazon value), chs 14, 16, 18 (guarantee stack, concessionality, dynamic incentives).
- *The Right Policy at the Wrong Time* chs 5–7 (international feebate needs a trust; forest valuation; an emission as a capital requirement).
- Research page abstract (`A.Website/research.qmd`), and the Oxford DPhil proposal (three quantities; act-now incentives; climate allowance of guarantee capacity).
- Supersedes the working title "Guarantee-Based International Incentives for the Delivery of Strong NDCs".
- No co-authors. The guarantee loss and buffer parameters are shared with 4.2 (Climate Investment Trust) and 4.3 (Sustainability-Linked Lending). Since 29 Oct 2026 the base case is the MDB sovereign loss record (GEMs 2025: 0.77% annual calls, 4.9% loss, 0.5% buffer, ratio about 80; about 27 net of the default option the borrower gives up, added 31 Oct 2026); the middle case is 3% calls × 10% loss (2.5% buffer, ratio 10) and the stress case 3% calls × 37% loss (Cruces and Trebesch 2013; 9.3% buffer, ratio 2.7). All use 20 programs, correlation 0.2 and a 1% annual chance of exhausting the buffer.

Related: 4.0 series overview; 4.2 The Climate Investment Trust (the buffer fund); 4.3 Sustainability-Linked Lending (delivery channel); 3.1 and 3.2 (structures the guarantee capacity can stand behind). Cross-review of both series: `../4.0.Overview/CrossReview-Notes.md`.
