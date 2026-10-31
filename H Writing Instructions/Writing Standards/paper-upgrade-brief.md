# Brief: upgrade one paper to the 1.1 standard (two forms, peer-reviewed, references checked, ~10-slide deck)

You are upgrading ONE paper in Stephen Stretton's writing repo at /home/user/writing (a git checkout; branch claude/charming-goodall-y6p60x). Stephen is a World Bank economist (climate, fiscal policy, finance); the papers go on his personal website and to journals. Your paper folder is given in your task message. Work carefully: quality matters more than speed.

## What Stephen asked for (his words, paraphrased)

- Every paper has TWO forms, each its own draft (master): a **policy brief** (`1.Presentation/Brief-<Name>.qmd`) that is concise, simple and easy to read, in World Bank style with the **first sentence of every paragraph in bold**; and an **academic working paper** (`<Name>.qmd`) that is comprehensive. Do not confuse the two forms: neither is made from the other, and each keeps its own master file. On the website the brief is the paper's page and the working paper sits below it.
- The working paper opens with a **non-technical executive summary as chapter 1**.
- **Improve the papers**: do a peer review first, then revise. Add detailed references and do a really good job. Avoid too much replication between the two forms, and cross-reference each to the other.
- **Slide decks of about ten slides.** Quality matters more than quantity: look through them carefully.
- **Peer review before editing.** Write the review first, from a full reading, and only then change the masters.
- **Be systematic and methodical, drawing on the literature**: for each claim and each result, find what the literature says (the closest prior work, the best evidence, the strongest counter-evidence) and cite it, verified.
- **The brief is brief and easy to read; the working paper is rigorous, and still easy to read.**
- **Any link to a document, deck or PDF says its file type in brackets inside the link text**: `[Policy brief (docx)](...)`, `[Slides (pptx)](...)`, `[Report (pdf)](https://...)`. This applies in the masters, notes and slides.

## Read first (in this order)

1. `/home/user/writing/AGENTS.md`, `H Writing Instructions/AGENTS.md`, `H Writing Instructions/NORMS.md`.
2. `H Writing Instructions/Writing Standards/briefing-series-spec.md` (format of the brief, cross-links, render commands: updated today), `paper-standard.md`, `writing-principles.md`, `ai-tells.md`.
3. `H Writing Instructions/Claude + Scripts/Setup Claude/_admin/voice.md` (how Stephen sounds).
4. **The worked model**, paper 1.1, in `C Policy and FInance/1.CarbonPricing/1.1.OpenEconomyCarbonPricing/`: `OpenEconomyCarbonPricing.qmd` (working paper v0.4: see the YAML, the first italic line, the `# Executive summary {#sec-summary}` chapter, section ids), `1.Presentation/Brief-OpenEconomyCarbonPricing.qmd` (brief v1.1: Key messages, bold lead sentences, cross-links), `1.Presentation/slides.json`, `5.Notes/PeerReview-2026-10-31.md`, `5.Notes/BibCheck-2026-10-31.md`. Match this pattern.
5. Your paper's folder: its README if any, every file in `5.Notes/`, its row in `H Writing Instructions/PAPERS.md` and in `H Writing Instructions/Writing-Status-Report.md`, and its section's `<n>.0.Overview/` folder (SeriesArchitecture.md and shared terms, if present).

## Steps

1. **Save the current versions** to `8.PreviousVersions/` with their version numbers (`<Name>-v0.X.qmd/.docx/.bib`, `Brief-<Name>-vX.Y.qmd/.docx/.bib`, `Slides-<Name>-vX.Y.pptx`). Copy, don't move (the masters stay where they are).
2. **Peer review**: write `5.Notes/PeerReview-<date>.md` as a referee would: summary judgement; major points (is the question and answer clear; is each result right and its conditions stated; check every derivation and every number yourself, recompute where possible; the strongest objection; the closest prior work and whether the contribution is stated against it); minor points; what the brief and the deck need. Find real errors. Then a "Disposition" line once you have revised.
3. **References**: check every source the two forms cite against the source itself, using WebSearch (mode "standard"; "extended" only when standard fails) and WebFetch (Crossref `https://api.crossref.org/works?query.bibliographic=...` or `/works/<doi>`, publisher pages, IDEAS/RePEc, NBER, SSRN abstract pages, World Bank Open Knowledge Repository, IMF, EUR-Lex, OECD). Read at least the abstract; read the passage when a claim is specific (a number, a range, an article of a law). Fix the bibliographic fields, re-word any sentence the source does not support, replace or cut what cannot be supported, and add the important missing literature (verified). Record what was read in each entry's `note = {verified <date>: ...}`. Write `5.Notes/BibCheck-<date>.md` (a table: source, problem, change). Never invent a citation, number or quote. **Do not put Stephen's email address (or any personal data) into any web request or API call** (for example, do not pass an `email=` parameter to Unpaywall or Crossref).
4. **Working paper** (bump `version:` by 0.1, date "October 2026"; first italic line links to the brief with `[Climate Fiscal Policy Brief No. X.Y](brief:)`): add `# Executive summary {#sec-summary}` as chapter 1 (about 500–700 words, non-technical, bold lead sentence in each paragraph, no equations, real numbers from the paper); fix everything the peer review found; make sure every section has an `{#sec-...}` id; keep it comprehensive and at the paper standard (`paper-standard.md`), but cut repetition. `number-sections: true` in the YAML. No `[VERIFY]` or `TODO` may remain; if something cannot be verified, cut it or state it as the author's assumption.
5. **Policy brief** (`1.Presentation/Brief-<Name>.qmd`; bump its version, or create it at version 1.0 if the paper has none, using the YAML in the spec; series line "Climate Fiscal Policy Brief No. X.Y"): about 2,000 words; `# Key messages {#sec-key-messages}` first (four or five bold one-or-two-sentence paragraphs); then short sections whose headings state a claim; **every paragraph's first sentence in bold**; plain words, no equations, no propositions, no proofs; one table and/or figure with the same real numbers as the working paper; links into the working paper's sections for the evidence (`[working paper, calibration](wp:sec-calibration)`), to the working paper as a whole (`[working paper](wp:)`) and to sibling papers (`[Brief 1.3](paper:1.3)`); "What to do"; "Related papers in this series"; references. The brief's `.bib` = the working paper's verified entries for exactly the keys the brief cites (copy them), plus the series' CFPB entries it cites. Brief figures must live under `1.Presentation/figures/` (generate or copy them with a `make_figures.py` there, as in 1.1).
6. **Figures and data**: regenerate any figure whose numbers change, from the scripts in the folder (`python3`; matplotlib, numpy are installed). Keep one set of numbers across the working paper, the brief and the deck.
7. **Render both to Word** with pandoc (Quarto is not installed here), from the folder each master is in:
   ```bash
   F="/home/user/writing/H Writing Instructions/Scripts/Website"; CSL="/home/user/writing/E Website/chicago-author-date.csl"
   pandoc <Name>.qmd -f markdown --lua-filter="$F/quarto-xref.lua" --lua-filter="$F/web-links.lua" --citeproc --bibliography=<Name>.bib --csl="$CSL" -o <Name>.docx
   ```
   (same for the brief in `1.Presentation/`). Check the result: `pandoc X.docx -t plain` must show no `???`, no `(wp:`, no `{#`, no unresolved `@` keys, and pandoc must print no "citation not found" warning.
8. **Deck**: write `1.Presentation/slides.json` in the format of 1.1's (types: title, stats, points, figure, table, closing; read the docstring of `H Writing Instructions/Writing Standards/templates/make_deck.py`); about ten slides; every slide title a full-sentence message; sources on the slides; numbers identical to the papers. Build it: `python3 "/home/user/writing/H Writing Instructions/Writing Standards/templates/make_deck.py" slides.json Slides-<Name>.pptx`. Then LOOK at it: render with `soffice --headless --convert-to pdf <pptx>` (run in a scratch directory under a scratch directory outside the repo) and `pdftoppm -r 60 -png`, view the images with the Read tool, and fix overflow, overlaps, empty slides or weak slides. Do not edit make_deck.py (it is shared); if it cannot do something you need, say so in your report.

## Rules

- **Edit only inside your paper folder.** Do not edit shared files: `PAPERS.md`, `TODO.md`, anything in `E Website/`, `H Writing Instructions/Scripts/`, the templates, other papers' folders, or the series overview. The coordinating session does those.
- Do not commit or push. Do not delete files (move superseded ones into `8.PreviousVersions/` with a version suffix if needed).
- Do not change the paper's title without saying so prominently in your report: titles are copied into other papers' `.bib` files (CFPB keys).
- Confidentiality: nothing marked confidential, internal, draft-for-discussion, not for citation, or World Bank internal goes in. Follow the paper's README on which country results are cleared.
- US spelling, Chicago author-date, numbers with units and years, one term for one thing, the first sentence of every paragraph carries its claim. Avoid the AI tells in `ai-tells.md`. Do not use "we" for a single author.
- Today's date is 31 October 2026; use "31 Oct 2026" in notes and file names (`PeerReview-2026-10-31.md`).

## Report back (concise)

1. The paper's question and answer in two sentences.
2. The main peer-review findings (errors found and fixed), and anything you could not resolve.
3. References: how many checked, how many re-worded, added or cut; anything still unverified.
4. Word counts: working paper body, executive summary, brief. Deck: slide count; confirm you viewed the rendered slides.
5. Any title change, any new CFPB key, anything the coordinator must update in shared files.
6. The list of files you created, changed or moved.

## Extra rules for the modelling papers (sections 5–7)

- These papers have NO policy brief yet (except 6.1): create `1.Presentation/Brief-<Name>.qmd` and `.bib` (series line "Climate Fiscal Policy Brief No. X.Y", key CFPB<X><Y>; working paper key StrettonWP<X><Y>). On the website they sit in the Modelling and Analytics part (`modelling/`); cross-links to sibling papers use `paper:5.2` etc.
- The brief for a methods or validation paper is still a policy brief: who should care (finance ministries, development-bank teams using CPAT), what the result means for decisions, what to do. Plain words, no equations, bold lead sentences.
- CONFIDENTIALITY: CPAT is a World Bank/IMF tool. Use only public sources: the public CPAT documentation and papers, the public CPAT-AI repository (https://github.com/cpmodelai/cpat_ai, if public — check), published articles. Do not include anything marked confidential, internal, PFR (Public Finance Review), draft-for-discussion or not-for-citation, and follow each paper's README on which country results are cleared as illustrative. If unsure, leave it out and say so in your report.
- Read the section overview and plan first: `D Modelling/5.Modelling/5.0.Overview/` (SeriesArchitecture.md if present) and PAPERS.md's section 5–7 table. Keep terms consistent with 6.1 (Total Effective Carbon Price) and across 5.1–5.4.
- Each existing deck (`1.Presentation/`) should become about ten slides on the new builder (slides.json + make_deck.py).
