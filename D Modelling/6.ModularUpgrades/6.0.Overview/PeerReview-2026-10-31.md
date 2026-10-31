# Peer review of the section 6 overview, v0.1 (31 Oct 2026)

Review written before revision, as for the papers. The overview summarizes papers 6.1–6.5, which are being upgraded now; points that depend on their revised content are marked (after papers).

## Summary judgement

A clear overview with a good organizing idea: keep the CPAT core small enough to audit and add capability as modules that read its outputs, each stated in a few equations. It needs its numbers matched to the revised papers, one factual correction carried over from the section 5 review, sources, and a theme deck, which the section does not have.

## Major points

1. **"About eighteen equations"** contradicts section 5, which now states the mitigation module in fourteen equations (paper 5.1 v0.2; overview 5.0 v0.3). Use fourteen.
2. **The cost-of-capital sentence in 6.3 is wrong about CPAT's default.** "12.6 percent, almost exactly the rate CPAT already assumes for lower-middle-income countries" treats the income-group rates (7.5/10/12.5/15 percent) as the default. The 5.1 review, checked against the public CPAT-AI code, found that CPAT's default is a country cost of capital plus a technology premium; the income-group rates are an option. Restate: the break-even rate is close to the 12.5 percent that CPAT's income-group option assigns to lower-middle-income countries, and well within the range of country rates.
3. **Headline numbers must match the revised papers** (after papers): 6.1 (\$21 explicit against \$37 effective, \$32–38, \$28 after a year); 6.2 (Türkiye hot-rolled steel €107 to €252 per tonne; Egypt €595 million to €177 million); 6.3 (13.3 cents, 12.6 percent; the \$108 million island plant; 4–5 percent of GDP for Kenya, Uganda and St Lucia; under a fifth of Uganda's net-zero benefits reaching the budget); 6.4 (64 and 41 percent); 6.5 (186 countries; Kenya 0.5 percent of GDP, about 5 percent covered, about 7 points of debt by 2050).
4. **Country results** (Egypt, Kenya, Uganda, St Lucia) may appear only as each paper's README clears them, labelled illustrative; drop any the revised papers drop.
5. **No sources.** The overview cites nothing: the IMF carbon-price equivalent, the CBAM regulation and its 2025 amendments, SISEPUEDE, the FTT models and the papers themselves. Give it a bibliography built from the papers' verified `.bib` files and the StrettonWP6x keys.
6. **CBAM timing.** "Since January 2026 ... importers have owed a charge" should be checked against Regulation (EU) 2023/956 as amended in 2025 (certificate sales begin in 2027 for 2026 imports); state it as the papers do.

## Minor points

1. Paragraphs should open with their claim in bold, as the section 1–5 overviews now do.
2. Add `paper:6.x` links so the site links each paper, and update the status column (each paper now has a working paper, a brief and a deck).
3. 6.1's role across sections: it is cited in sections 1 and 4 (policy crediting, border recognition); say so once.
4. "The lite models are not their parents" — say plainly that the simplified versions approximate the IMF and World Bank models and are not endorsed by those institutions.

## Theme deck

Section 6 has none. Make one of about ten slides on the new builder (`1.Presentation/slides.json`, `Slides-ModularUpgrades.pptx`), drawing on the five papers' decks, and add it to `site_config.py`.

## Disposition

All points addressed in overview v0.2 (31 Oct 2026), after papers 6.1–6.5 were revised: fourteen equations; CPAT's default cost of capital stated as a country rate plus a technology premium, with the income-group rates as an option; numbers matched to the revised papers, including the corrected Egypt CBAM charge (€793 million at default values, €480 million with verified data, 2025 volumes; the €595/€177 million figures superseded), the 6.3 island case restated as a cash problem, 6.4's travel growth (35 percent) and crossing (about 55 years), and 6.5's Kenya run set beside the published IMF–World Bank debt analysis; country results only as the papers' READMEs clear them; CBAM timing as amended in 2025; a bibliography built from the papers' verified `.bib` files; bold lead sentences and `paper:` links. A first theme deck of 10 slides (`1.Presentation/slides.json`, `Slides-ModularUpgrades.pptx`) added to `site_config.py`.
