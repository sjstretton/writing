# 5.5 Carbon Prices Cut Emissions: Evidence from Ten Natural Experiments

**Status (1 Nov 2026):** working paper v0.1, first draft, not yet peer-reviewed. About 11,000 words of body including tables (14 tables, 1 figure); PDF 28 pages. No brief or deck yet.

**Question and answer.** When governments or markets have raised fuel prices, what happened to emissions, and how much per dollar? In every one of ten well-evaluated cases, emissions from the covered fuels fell: by about 1–2 percent per US$10 a tonne in road transport and heating over 5–15 years, and five to ten times more per dollar in power where coal could switch to gas (Britain's carbon price floor, the EU ETS). Taxes moved demand more than equal market price changes, exemptions and offsetting tax cuts weakened the effect, and short, very large shocks (Germany's 2022 gas crisis, Indonesia's subsidy reform) gave small cuts per dollar.

**The ten cases.** Sweden 1991 (motor fuels), Sweden 2001–04 (heating fuels), Germany 1999–2003 (eco-tax on road fuels), US state gasoline taxes 1966–2008, British Columbia 2008–2025, Switzerland's heating-fuel levy 2008–, the EU ETS 2005–2012, Britain's carbon price floor 2013–2017, Indonesia's subsidy reform 2013–15, Germany's 2022 gas shock. For each: the price path over time, the retail price increase, the carbon price or carbon-price equivalent (US$/t), and the ex post cut. Eleven further episodes (Finland, Norway, Australia 2012–14, UK fuel duty escalator, RGGI, France, Saudi Arabia, Iran, Nigeria, Germany's BEHG, Ireland) are in Table 13 with the reason each was left out.

**Place in the series.** Companion to 5.3 (which recommends back-casting CPAT against natural experiments) and 5.4 (CPAT's elasticities). Section 7 compares the cases with CPAT: the gasoline long-run elasticity (−0.64) is within the ex post range; the residential natural gas elasticity (−0.70) is above it (−0.15 to −0.45).

## Files

| File | What it is |
|---|---|
| `CarbonPriceNaturalExperiments.qmd` | Working paper master (v0.1) |
| `CarbonPriceNaturalExperiments.bib` | References; each entry's `note` says what was read (full text, working paper or abstract) and the numbers taken from it. Every DOI checked against Crossref on 1 Nov 2026 |
| `CarbonPriceNaturalExperiments.pdf`, `.docx` | Rendered from the master (see below) |
| `2.Source/natural_experiments.py` | Case data for the figure and Table 12 (price, cut, horizon, source), the per-US$10 yardstick, Figure 1 |
| `2.Source/table_per10.csv`, `2.Source/figures/fig1_effect_vs_price.png` | Outputs of the script |
| `5.Notes/research/*.md` | Six research fact files (Nordic taxes, British Columbia, power sector, industry and buildings, road-fuel taxes, subsidy reform and price shocks), with every number linked to its source and marked full text, working paper, abstract or snippet |

Run: `cd 2.Source && python3 natural_experiments.py` (matplotlib).

## Rendering

The PDF and Word files use the working-paper format:

```bash
python "H Writing Instructions/Scripts/Website/render_pdfs.py" "D Modelling/5.Modelling/5.5.CarbonPriceNaturalExperiments/CarbonPriceNaturalExperiments.qmd" --docx
```

This needs Quarto 1.9 or later: the template calls `content-to-string`, which Quarto 1.6 and 1.8 do not provide (v0.1 was rendered with Quarto 1.9.20). The master carries one raw Typst line that lets this paper's long tables break across pages; the shared template is unchanged.

## Open items before v0.2

- Peer review and a second citation check against the published versions (several numbers are from working-paper versions; the bib notes say which).
- `[VERIFY]` markers: Germany's 2022 national emissions (UBA early estimate seen only in summary); the CPS removal announcement (news report, not the Treasury document); Dussaux (2020) full text; author given names for Yu, Arcila and Baker, Ott and Weber, Fauceglia et al., Fernando.
- Gaps the paper states openly: no sourced 1991 Swedish pump price; no Swedish heating-oil retail price for 2000–2004; no ex post estimate of the British carbon price floor's effect on retail electricity prices; Indonesian electricity carbon-price equivalent by consumer group not computed.
- Decide whether to add a brief (Climate Fiscal Policy Brief No. 5.5) and a ten-slide deck, and whether to add the paper to the website (`WEB_PAPERS`).
- Overview 5.0 still lists papers 5.1–5.4; add 5.5 when it is next revised.

## Sources and confidentiality

Public sources only: journal articles, working papers, official statistics and government documents. No World Bank internal material and no CPAT country results.
