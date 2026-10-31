# Climate Fiscal Policy Briefs: series specification

The briefing-paper series for the carbon-pricing papers in `C Policy and FInance/1.CarbonPricing` (and the Total Effective Carbon Price, now paper 6.1 in `6.ModularUpgrades`). Numbers follow `H Writing Instructions/NUMBERING.md`. Each brief is a policy paper of about 2,000 words that a busy official can act on. Each has a fuller academic working paper behind it. The two are separate drafts with separate masters: the brief (`1.Presentation/Brief-<PaperName>.qmd`) is plain, concise and simple; the working paper (`<PaperName>.qmd`) is comprehensive. Neither is made from the other. On the website the brief is the paper's page and the working paper sits one level below it, and each links to the other. This file fixes the format, the shared terms and the files, so that the briefs read as one series.

The pattern was set on 1.1 (31 Oct 2026, brief v1.1 and working paper v0.4): use it as the model.

## Format

**Title page**
- Series line: `Climate Fiscal Policy Brief No. X.Y` (the paper's number: section, then place in the section), month and year.
- Title that states the finding or proposal; a subtitle may add the setting.
- Author: `Stephen J. Stretton`, with the note *Writing in a personal capacity.* No institutional affiliation on the title page.
- **Abstract of about 100 words** (90–110). One paragraph: the problem, the proposal, the main result, the implication.
- Disclaimer (as a footnote or small print on the title page): *The views expressed are the author's own and do not represent those of any institution with which he is or has been affiliated.*

**Key messages** (first section, about 150 words): four or five paragraphs of one or two sentences each, the first sentence in bold. A reader who stops here knows the problem, the proposal, why it works and what to do.

**Body.** About 2,000 words in all, excluding references. Short sections with headings that state a claim. **World Bank style: the first sentence of every paragraph states the paragraph's claim and is set in bold**, so that reading the bold sentences alone gives the whole argument. No equations, no propositions, no proofs: those belong in the working paper, and the brief links to the section that has them. At least one table or figure with real numbers, the same numbers as the working paper; label stylized numbers as stylized.

**Close.** A short "What to do" section with concrete recommendations, then "Related papers in this series", then references.

**The working paper's executive summary.** The working paper opens with its own non-technical executive summary as chapter 1 (about 600 words, bold lead sentences, no equations), written for the same reader as the brief. Keep the two short and different in purpose: the brief argues the policy; the executive summary summarizes the paper's results.

**Cross-references.** Link the two forms and the other papers with short targets, which the website build turns into links and the Word filter turns into plain text: `[working paper, crediting](wp:sec-crediting)`, `[the brief](brief:)`, `[Brief 1.3](paper:1.3)`. Give every working-paper section an identifier (`{#sec-...}`) so the brief can link to it. Refer to sections by name, not number: the web and Word versions number them the same, but names survive renumbering.

## Style

Follow `H Writing Instructions/NORMS.md`, `H Writing Instructions/Writing Standards/writing-principles.md` and `ai-tells.md`. In particular:
- US spelling.
- Dense and economical. No throat-clearing, no roadmap paragraphs, no summary ending that repeats the executive summary.
- Every factual claim cited. Never invent a citation. Check every cited source against the source itself (abstract at minimum, the passage for a specific number), record what was read in the entry's `note`, and keep a short record in `5.Notes/BibCheck-<date>.md`. Claims you cannot source are cut or marked `[VERIFY: ...]` in the text.
- Chicago author-date. The brief's `.bib` is copied from the working paper's verified `.bib` (only the keys the brief cites), so the two cannot drift apart.

## Shared terms (use exactly these)

| Term | Meaning |
|---|---|
| production track | Pricing what a country makes, measured as emissions intensity (per tonne of physical output, or per dollar of output where products differ), with a revenue-neutral feebate |
| consumption track | Pricing what a country consumes: a carbon component of VAT on goods (imported or domestic, exports zero-rated), plus a forward-announced legal obligation on the few large firms that supply domestic energy and transport |
| feebate | A charge $t(e_i - \bar e)$ per unit of output on intensity above a benchmark $\bar e$ and a rebate below it; revenue-neutral when $\bar e$ is the sector average. Output-based rebating is the same instrument seen from a carbon tax |
| emissions intensity | Emissions per unit of output, $e$ |
| embodied carbon | Emissions released in producing a good, along its supply chain |
| carbon-price equivalent; Total Effective Carbon Price (TECP) | The uniform carbon tax that would cut emissions by as much as a given instrument or policy mix, price-based (tax, feebate, subsidy) or not (standard, procurement rule, legal obligation) |
| destination basis | Taxing where a good is consumed, as VAT does; the opposite of origin (source) basis |
| CBAM | The EU Carbon Border Adjustment Mechanism, Regulation (EU) 2023/956 |
| policy crediting | International payment per tonne for emission cuts induced by a policy, measured as a carbon-price equivalent, rather than for individual projects |

## Series numbering and cross-references

| No. | Short title | Folder |
|---|---|---|
| 1.1 | Price Production and Consumption Separately (the two-track architecture) | `1.1.OpenEconomyCarbonPricing` |
| 1.2 | Feebates (power and industry) | `1.2.FeebatesAndOutputBasedRebating` |
| 1.3 | Converting a VAT into a destination carbon tax | `1.3.CarbonConsumptionTax` |
| 1.4 | Carbon price recognition under CBAM, and scrap shuffling | `1.4.IronSteelCBAM` |
| 6.1 | The Total Effective Carbon Price | `6.ModularUpgrades/6.1.PolicyEquivalentCarbonPriceAndCES` |

Cite sibling briefs as `@CFPB11`, `@CFPB12`, `@CFPB14`, `@CFPB13`, `@CFPB61`, with these bib entries (copy them into each brief's `.bib`):

```bibtex
@techreport{CFPB11, author={Stretton, Stephen J.}, title={Price Production and Consumption Separately: A Two-Track Architecture for Carbon Pricing in Open Economies}, institution={Climate Fiscal Policy Briefs}, number={1.1}, year={2026}}
@techreport{CFPB12, author={Stretton, Stephen J.}, title={Feebates: The Full Carbon Price at the Margin, Without the Carbon Bill}, institution={Climate Fiscal Policy Briefs}, number={1.2}, year={2026}}
@techreport{CFPB14, author={Stretton, Stephen J.}, title={Credit the Price Signal, Not the Payment: Carbon Price Recognition and Scrap Shuffling under the {EU}'s Carbon Border Adjustment Mechanism}, institution={Climate Fiscal Policy Briefs}, number={1.4}, year={2026}}
@techreport{CFPB13, author={Stretton, Stephen J.}, title={Converting a {VAT} into a Destination Carbon Tax: A Carbon Component in {VAT} and a Forward Obligation on Energy Suppliers in the {European Union}}, institution={Climate Fiscal Policy Briefs}, number={1.3}, year={2026}}
@techreport{CFPB61, author={Stretton, Stephen J.}, title={Measure Carbon Pricing by the Emissions It Cuts: The Total Effective Carbon Price}, institution={Climate Fiscal Policy Briefs}, number={6.1}, year={2026}}
```

(These are the final titles from each paper's YAML; if a title changes, update the bib entries everywhere. Keys follow the paper number: `CFPB<section><paper>`, working papers `StrettonWP<section><paper>`.)

## Files

In each paper folder, under `1.Presentation/`:
- `Brief-<PaperName>.qmd`, its `Brief-<PaperName>.bib`, and the rendered `Brief-<PaperName>.docx`.
- Figures in `1.Presentation/figures/`, generated by a script saved beside them (`make_figures.py`), so they can be regenerated.

YAML header:

```yaml
---
title: "..."
subtitle: "..."
series: "Climate Fiscal Policy Brief No. X.Y"
version: "1.0"
author:
  - name: "Stephen J. Stretton"
    note: "Writing in a personal capacity."
date: "October 2026"
abstract: |
  (about 100 words)
bibliography: Brief-<PaperName>.bib
csl: https://www.zotero.org/styles/chicago-author-date
format:
  docx: default
---
```

Render to Word with Quarto where it is installed, adding the link filter:

```bash
quarto render Brief-<PaperName>.qmd --to docx -L "<repo>/H Writing Instructions/Scripts/Website/web-links.lua"
```

Where only pandoc is available, add the cross-reference filter too, before `--citeproc` (it numbers sections, figures, tables and equations as Quarto would):

```bash
F="<repo>/H Writing Instructions/Scripts/Website"
pandoc Brief-<PaperName>.qmd -f markdown --lua-filter="$F/quarto-xref.lua" --lua-filter="$F/web-links.lua" \
  --citeproc --bibliography=Brief-<PaperName>.bib --csl="<repo>/E Website/chicago-author-date.csl" -o Brief-<PaperName>.docx
```

The working paper renders the same way. The deck is made from `1.Presentation/slides.json` (about ten slides, each title a full-sentence message) with `python "H Writing Instructions/Writing Standards/templates/make_deck.py" slides.json Slides-<PaperName>.pptx`.

## Sections 3 and 4 (added 29 Oct 2026; renumbered 31 Oct 2026)

The same series, format and files cover the finance-and-risk papers (3.1, 3.2) and the sovereign-incentives papers (4.1, 4.2, 4.3): `Climate Fiscal Policy Brief No. 3.1` and so on. Each section's plan, shared terms and citation keys (`CFPB31`, `CFPB32`, `CFPB41`, `CFPB42`, `CFPB43`; working papers `StrettonWP31` … `StrettonWP43`) are in `C Policy and FInance/3.FinanceAndRisk/3.0.Overview/SeriesArchitecture.md` and `C Policy and FInance/4.SovereignIncentives/4.0.Overview/SeriesArchitecture.md`. Shared terms there extend the table above; where a term appears in both, use one meaning across all three sections.
