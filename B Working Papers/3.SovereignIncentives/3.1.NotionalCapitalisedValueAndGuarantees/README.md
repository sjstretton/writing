# 3.1 Notional Capitalized Value and Guarantees

**Status:** first full draft, version 0.1 (29 October 2026). Working paper and Climate Fiscal Policy Brief No. 3.1 written; awaiting Stephen's review. Flagship of series 3 (Sovereign Incentives).

**Title:** Reward the Stock as Well as the Flow: Notional Capitalized Value and Guarantee-Based Climate Incentives.

**Question.** How can the international system give a government a large, early and credible incentive to protect carbon stocks and cut emissions, without a cash transfer that donors will not vote for?

**Answer.** Credit each country with a notional capitalized value: a balance opened by its carbon stock (at a low stock price) and debited for every tonne emitted above an agreed allowance (at a higher, uniform debit price). The balance sets guarantee capacity on eligible green borrowing; the country gains the spread saved, donors bear expected loss on a buffer they hold. Capacity declining at the rate technology costs fall is the cheapest schedule that makes acting now beat waiting.

## Files

| File | What |
|---|---|
| `NotionalCapitalisedValueAndGuarantees.qmd` | Working paper master, version 0.1 (about 8,600 words of body) |
| `NotionalCapitalisedValueAndGuarantees.bib` / `.docx` | Bibliography; rendered Word file |
| `1.Presentation/Brief-NotionalCapitalisedValueAndGuarantees.qmd` / `.bib` / `.docx` | Climate Fiscal Policy Brief No. 3.1 (about 2,700 words) |
| `1.Presentation/figures/make_figures.py` | Draws the brief's two figures (reuses `2.Source`) |
| `2.Source/model.py` | All calibration numbers (prints them) |
| `2.Source/make_wp_figures.py` | Working paper figures, written to `2.Source/figures/` |
| `2.Source/render.py` | Renders a qmd to docx with pandoc, resolving Quarto cross-references (Quarto is not installed) |
| `5.Notes/` | Working notes |

Render: `python3 2.Source/render.py NotionalCapitalisedValueAndGuarantees.qmd NotionalCapitalisedValueAndGuarantees.bib <chicago-author-date.csl>`. The brief has no cross-references and renders with plain pandoc.

## Lineage and sources

- *Time and Chance* ch. 21 (Notional Capitalized Carbon Value, the only worked version), ch. 20 (interest on a notional Amazon value), chs 14, 16, 18 (guarantee stack, concessionality, dynamic incentives).
- *The Right Policy at the Wrong Time* chs 5–7 (international feebate needs a trust; forest valuation; an emission as a capital requirement).
- Research page abstract (`7.Website/research.qmd`), and the Oxford DPhil proposal (three quantities; act-now incentives; climate allowance of guarantee capacity).
- Supersedes the working title "Guarantee-Based International Incentives for the Delivery of Strong NDCs".
- No co-authors. Buffer and loss parameters are shared with 3.2 (Climate Investment Trust).

Related: 3.2 Climate Investment Trust (the buffer fund), 3.3 Sustainability-Linked Lending (delivery channel).
