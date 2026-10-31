# Peer review of the section 7 overview, v0.2 (31 Oct 2026)

Review written before revision, as for the papers, and after papers 7.1 and 7.2 were peer-reviewed; points that depend on their revised content are marked (after papers).

## Summary judgement

A short, well-argued overview: analysis changes policy only when the budget holder can reproduce it, so each tool is built to a reproducibility standard. Its numbers and two of its claims have not survived the papers' reviews, it cites nothing, and its theme deck is on the old format.

## Major points

1. **The African benchmark is unsourced and wrong** (after papers). "An African average of 2.4" percent of GDP has no source. OECD *Revenue Statistics in Africa* gives an average of 1.32 percent of GDP across 37 countries in 2023 (median 1.03), as 7.1 v0.4 now reports.
2. **Liberia is compared on the wrong definition** (after papers). Its legal excise (0.37 percent of GDP) excludes the fuel levies that the African average counts as excise; on the same definition Liberia raises about 1.25 percent, close to the average.
3. **Sierra Leone's figure needs its caveat** (after papers). The diagnostic's 1.25–1.28 percent of GDP is about twice the OECD series (0.57 percent in 2023); 7.1 reports both and states the reconciliation as open. The overview must too.
4. **"Its largest unpriced cost is air pollution rather than carbon"** cannot be said: a gap cannot be split by component. 7.1 now splits the corrective rate instead: carbon 31, air pollution 35, road use 35 percent; local damage is about two-thirds.
5. **"Rebuilt by a script anyone can rerun" overclaims** (after papers). The 7.2 build is in a private repository and two appendices are read through an unpublished compilation; every input is public and every value names its source, but the claim that anyone can rerun the build holds only once the code is published.
6. **The carbon value is a policy choice, not a damage estimate.** USD 50 a tonne is a proposed price floor; 7.1 now shows USD 185 (Rennert et al. 2022) beside it. Say so when quoting results against it.
7. **No sources.** Give the overview a bibliography built from the papers' verified `.bib` files.

## Minor points

1. Paragraphs should open with their claim in bold, as the other overviews now do.
2. Add `paper:7.x` and `paper:6.5` links and update the status column.
3. 7.2's indicator is net interest, not interest, as a share of revenue.
4. Say what each paper's review changed, briefly: readers of the earlier versions need to know.

## Theme deck

The deck (`1.Presentation/Slides-Analytics.pptx`, from `slides-theme.json`) is on the old builder. Rebuild it at about ten slides from the revised papers' decks; keep the old one in `8.PreviousVersions`.

## Disposition

All points addressed in overview v0.3 (31 Oct 2026), after papers 7.1 (v0.4) and 7.2 (v0.2) were revised: African benchmark 1.32 percent of GDP (OECD, 37 countries, 2023); Liberia compared with and without its fuel levies; Sierra Leone's figure set beside the OECD series, reconciliation open; the corrective diesel rate split by component instead of the gap; the carbon value stated as a price floor, with USD 185 beside it; the reproducibility claim restated (public inputs, private build); net interest; a bibliography from the papers' verified `.bib` files; bold lead sentences and links. Theme deck rebuilt at 10 slides on the new builder (`1.Presentation/slides.json`); the old deck and spec are in `8.PreviousVersions`.
