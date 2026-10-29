# Climate Fiscal Policy Briefs: series specification

The briefing-paper series for the carbon-pricing papers in `B Working Papers/1.ClimateAndFiscalPolicy`. Each brief is a 2,000–3,000-word policy paper that a busy official can act on. Each has a fuller academic working paper behind it. This file fixes the format, the shared terms and the files, so that the briefs read as one series.

## Format

**Title page**
- Series line: `Climate Fiscal Policy Brief No. 1.x` (x = the paper number), month and year.
- Title that states the finding or proposal; a subtitle may add the setting.
- Author: `Stephen J. Stretton`, with the note *Writing in a personal capacity.* No institutional affiliation on the title page.
- **Abstract of about 100 words** (90–110). One paragraph: the problem, the proposal, the main result, the implication.
- Disclaimer (as a footnote or small print on the title page): *The views expressed are the author's own and do not represent those of any institution with which he is or has been affiliated.*

**Executive summary of about 400 words** (350–450), on its own page after the title page. Signposted short paragraphs, not bullets. A reader who stops here knows the problem, the proposal, why it works, what it costs and what to do next.

**Body.** About 2,000–2,500 words, so the whole brief is 2,000–3,000 words excluding references and appendices. Numbered sections. Paragraphs open with their claim. At least one table, figure or worked numerical example; label stylized numbers as stylized.

**Close.** A short "What to do" section with concrete recommendations, then "Related papers in this series", then references.

## Style

Follow `A Writing Instructions/NORMS.md`, `E Writing Standards/writing-principles.md` and `ai-tells.md`. In particular:
- US spelling.
- Dense and economical. No throat-clearing, no roadmap paragraphs, no summary ending that repeats the executive summary.
- Every factual claim cited. Never invent a citation. Unverified entries carry `note = {VERIFY: ...}` in the `.bib`; claims you cannot source are cut or marked `[VERIFY: ...]` in the text.
- Chicago author-date, from a `.bib` beside the brief.

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
| 1.3 | Carbon price recognition under CBAM, and scrap shuffling | `1.3.IronSteelCBAM` |
| 1.6 | Carbon Consumption Tax through VAT | `1.6.CarbonConsumptionTax` |
| 1.7 | The Total Effective Carbon Price | `1.7.PolicyEquivalentCarbonPriceAndCES` |

Cite sibling briefs as `@CFPB11`, `@CFPB12`, `@CFPB13`, `@CFPB16`, `@CFPB17`, with these bib entries (copy them into each brief's `.bib`):

```bibtex
@techreport{CFPB11, author={Stretton, Stephen J.}, title={Price Production and Consumption Separately: A Two-Track Architecture for Carbon Pricing in Open Economies}, institution={Climate Fiscal Policy Briefs}, number={1.1}, year={2026}}
@techreport{CFPB12, author={Stretton, Stephen J.}, title={Feebates: Pricing Carbon Without Raising Average Costs}, institution={Climate Fiscal Policy Briefs}, number={1.2}, year={2026}}
@techreport{CFPB13, author={Stretton, Stephen J.}, title={Carbon Price Recognition under CBAM}, institution={Climate Fiscal Policy Briefs}, number={1.3}, year={2026}}
@techreport{CFPB16, author={Stretton, Stephen J.}, title={Carbon Consumption Tax: A Destination-Based Carbon Price through VAT}, institution={Climate Fiscal Policy Briefs}, number={1.6}, year={2026}}
@techreport{CFPB17, author={Stretton, Stephen J.}, title={The Total Effective Carbon Price}, institution={Climate Fiscal Policy Briefs}, number={1.7}, year={2026}}
```

(Titles of 1.2, 1.3, 1.6 and 1.7 may be refined; the cross-review pass updates the bib entries everywhere.)

## Files

In each paper folder, under `1.Presentation/`:
- `Brief-<PaperName>.qmd`, its `Brief-<PaperName>.bib`, and the rendered `Brief-<PaperName>.docx`.
- Figures in `1.Presentation/figures/`, generated by a script saved beside them (`make_figures.py`), so they can be regenerated.

YAML header:

```yaml
---
title: "..."
subtitle: "..."
series: "Climate Fiscal Policy Brief No. 1.x"
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

Render to Word (Quarto is preferred; pandoc works if Quarto is missing):

```bash
pandoc Brief-<PaperName>.qmd -f markdown --citeproc --bibliography=Brief-<PaperName>.bib \
  --csl=/tmp/chicago.csl -o Brief-<PaperName>.docx
```

(`/tmp/chicago.csl` is the Chicago author-date style downloaded from `https://www.zotero.org/styles/chicago-author-date`; delete the `csl:` line from a temporary copy if pandoc complains.)
