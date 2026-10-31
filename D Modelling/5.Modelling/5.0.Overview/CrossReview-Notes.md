# Cross-review of sections 4 and 5 (now sections 5–7): issues and resolutions

Editor's consistency pass over the ten papers (5.1–5.4, 6.2–6.4, 7.1, 6.5 and 7.2) and the two overviews (5.0, 7.0), applying Stephen's decisions of 29 October 2026. Every changed docx was re-rendered with pandoc and citeproc (Chicago author-date) with no citeproc warnings; 5.4 and 6.2 were rendered after resolving their Quarto cross-references with the session's `xref.py`.

## Facts aligned across all twelve documents

| Fact | What the documents said | Resolution | Source |
|---|---|---|---|
| CPAT country coverage | "150 or more" and "about 150" (5.1), "some 150" and "the 150 countries on which it is calibrated" (5.4), "about 200" (6.3, 6.4), "well over a hundred" (5.0), "more than 180" (5.2, 5.3) | **"more than 180 countries"** everywhere. The user guide's coverage table marks about 190 countries as covered (it heads the table "192 countries"); "calibrated on 150 countries" is an older sentence in the documentation summary chapter. "More than 180" is the CPAT-AI documentation's own wording. | `cpat_ai/docs/CPAT_full_documentation_qmd/01_User_Guide.qmd` §1.4; `docs/CPAT_ai_documentation_qmd/index.qmd` |
| CPAT's capital and investment | 6.3 said CPAT "does not multiply [capacity] out into a capital bill" and "reports no investment bill"; 5.1 lists investment spending among the outputs | 6.3 now says the power model reports investment spending by technology, and that outside power CPAT has no capital. Costs of capital: corrected 31 Oct 2026 against the public cpat_ai code. CPAT's default is a country cost of capital plus a technology premium; the income-group rates of 7.5/10/12.5/15 percent (high, upper-middle, lower-middle, low income) are an option. Stated this way in 5.1 v0.2, 6.3 v0.2 and 5.0 v0.3. | 5.1 Table 3; `excel_ai/BUGS.md` L5 |
| Road transport | Only 6.4 said CPAT describes road transport three times | One flag, same wording, added to 5.1 (limitations), 5.2 (limits of the approach), 5.3 (where CPAT fits poorly) and 5.0: a simple fuel equation, an engineering fleet model and a co-benefits module, not linked, disagreeing on how much drivers cut their driving when fuel prices rise; each cites paper 6.4. 6.4 keeps its fuller version. | 6.4 §2.1; `excel_ai/ISSUES.md` I100, I111 |
| Road engineer model "off by default" (5.2) | Inaccurate: legacy's template default is the engineer model; the Egypt run uses the elasticity road model | 5.2 now says the standard Egypt run uses the elasticity road model, so the 17 road-engineer bugs were latent in it | `excel_ai/ISSUES.md` LD59; `BUGS.md` L25–L41 |
| Bug and issue counts | 5.0 and 5.2 said "135 open issues"/"135 open questions" | Register at release 1.0.2: **228 legacy bugs (24 high, 62 medium, 142 low), 22 prototype bugs, 20 documentation bugs; 135 issues (14 data problems, counting legacy bug L170), 35 departures, 14 upgrades.** Not every issue is open, so "open" is dropped; 5.0 now also gives the 35 departures. | `excel_ai/BUGS.md`, `excel_ai/ISSUES.md` (v1.0.2), counted |
| Tool names | Consistent (CPAT, legacy CPAT, Excel-AI, Coded CPAT, CPAT-AI) | No change needed | SeriesArchitecture.md |
| Overview numbers | 5.0 lacked the new country examples; 7.0 lacked the Kenya run | 5.0 now gives the Egypt CBAM application (€595m to €177m on seven exports), the Kenya/Uganda/St Lucia investment needs (4–5 percent of GDP; under a fifth of Uganda's SISEPUEDE net-zero benefits reach the budget as cash) and the rebuild date (October 2026). 7.0 now gives the Kenya run (need 0.5 percent of GDP in 2030; pricing covers about 5 percent; +7 points of debt by 2050). All labelled illustrative tool results. | Papers 6.2 §7, 6.3 §6, 6.5 §7 |

## Stephen's decisions applied

1. **AI assistance (5.2, 5.0):** "mainly through Claude Code" replaced by "Claude Code and GitHub Copilot"; 5.0 names both.
2. **Egypt figures (5.3, and 5.2 for consistency):** the deck's 2041 population of 185 million and the compounding GDP effect (0.5 percent to about 10 percent) are dropped. Both papers now cite the UN World Population Prospects 2024, medium variant: Egypt 147.0 million in 2041 (checked in `WPP2024_TotalPopulationBySex.csv`, https://population.un.org/wpp/). 5.2 still describes the GDP bug (L24, in the public register) but without a size.
3. **Paulina Schulz-Antipa:** credited for CPAT's air-pollution module in the acknowledgment footnotes of 5.1, 5.2 and 5.3 (5.3 also for the validation it reports). The 5.2 README note that her surname was missing is replaced.
4. **Sibling citations:** standard `@unpublished` entries StrettonWP51–54, StrettonWP62–65, StrettonWP71 and StrettonWP72 (author Stretton, Stephen J.; title = final YAML title; note "Working paper X.Y"; 2026) replace the older ad hoc entries and are in all ten papers' `.bib` files. In-text mentions converted where natural: 5.1 (5.2, 5.3, 5.4, 6.2, 6.4), 5.2 (5.3, 5.4, 6.4), 5.3 (6.4), 5.4 (5.1), 6.3 (5.1, 5.2, 6.5; italic titles removed), 6.4 (5.1, 5.4, 6.2, 6.3), 7.1 (5.1), 6.5 (6.3, 7.2), 7.2 (7.1, 6.5). Overviews refer to papers by number and carry no citations, so no bib was added.
5. **AI tells and claim-first fixes (obvious only):** 5.2 "The gap is practical, not conceptual" heading rewritten as a claim; 6.4 "practical, not academic" trimmed; 6.2 "Three results stand out" followed by four results, now "Four".

## Rendering fixes found on the way

- 7.1, 6.5 and 7.2: table captions ran straight into the next paragraph or heading with no blank line, so pandoc merged the following paragraph into the caption. Blank lines added (7.1 four tables, 6.5 four, 7.2 two).

## Open items for Stephen

- *Resolved.* 5.4 and 6.2 carry `xref.py` in their `2.Source` folders.
- The CPAT user guide says "covers 192 countries" but its table marks about 190 as covered; the series now says "more than 180". Change if you prefer "about 190".
- *Resolved 30 Oct 2026.* 6.4's claim that the co-benefits module "ignores electric vehicles" contradicted register issue I100 (co-benefit vehicle-km, fuel economy and classes come from the engineer road model whatever the road-model switch; only the road share of each fuel follows the switch). 6.4 now states I100; the EV claim and the "twice the fleet model's elasticity" claim are removed; the common flag in 5.0–5.3 now says the three descriptions are not consistent (co-benefits on fleet-model vehicle-km even when fuel use follows the fuel equation) instead of "not linked", citing I100.
