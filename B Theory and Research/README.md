# B Theory and Research

New research that Stephen has not yet reviewed: new papers in the series, and the substantive research behind the PhD applications and the papers (the thesis plan, the overview paper, the research notes and the documentation of the model that underpins them). The applications themselves (forms, proposals tailored to each university, statements, referees, transcripts) stay in `3 PhD Application/`. Created 3 November 2026.

New papers here are on the website under the **New Research** tab (`E Website/new/`). The thesis and PhD research documents are not on the site.

Every document here is written in the house working-paper format (norm 13 in `H Writing Instructions/NORMS.md`): a `.qmd` master with the house YAML (title, subtitle, series, version, author "writing in a personal capacity", date, abstract, keywords), rendered to Word with the house styles. Render with Quarto via `H Writing Instructions/Scripts/Website/render_pdfs.py <file.qmd> --docx`, or without Quarto via `render_docx.py` in this folder.

| Folder | What it holds | Status |
|---|---|---|
| `5.5.CarbonPriceNaturalExperiments` | **Carbon Prices Cut Emissions: Evidence from Ten Natural Experiments** (paper 5.5). Ten ex post cases, each with the price path over time, the retail price increase, the carbon price or its US$ equivalent and the measured cut; working paper v0.1.1, Climate Fiscal Policy Brief No. 5.5 v0.1 (the paper's page on the site) and a ten-slide deck | Awaiting review; on the New Research tab |
| `3.4.EnergyTransitionMacroeconomics` | **The Energy Transition Swaps a Fuel Bill for a Capital Bill** (note 3.4): a review of the literature on 32 stylized facts of the energy transition and what they mean for macroeconomic policy, for optimal and second-best carbon pricing and for development finance; ten indicators; three simple World Bank products from papers 3.1, 3.2 and 4.1–4.3; first estimates for Egypt by sector at a local and a de-risked cost of capital in an appendix (the author's illustrative calculations on public data). Two-page executive summary and twelve-page report. A lead-in to the global green deal work | v0.3, 20 Nov 2026 (peer-reviewed twice); awaiting review; not on the site; Egypt results not yet cleared for publication |
| `ThesisPlan/` | **Sovereign Incentives for Decarbonisation: Thesis Plan.** The question, the specialism gap, the Global Incentives Model as backbone, practical precedents (SECI, the MDB model, ADB's IF-CAP, CGIF, China's collateral), ten chapters in four parts with an analytical model each, the thesis-by-papers route, timelines and risks | v1.1, 3 Nov 2026 |
| `OverviewPaper/` | **Guarantee the Contract, Price the Policy, Pool the Risk.** The full overview paper (about 6,000 words, seven propositions), with its verified `references.bib` | v0.1; [VERIFY] markers to clear |
| `ResearchNotes/` | The addendum to the proposal (guaranteed payments, sovereign incentives, de-risking, currency, metrics, growth and fiscal story), the annotated bibliography, and the first raw research notes | v0.1 |
| `6.6.GlobalIncentivesModel` | **Model Technology Where It Decides Emissions** (paper 6.6): the Global Incentives Model's modelling plan, whose central research question is how much emissions can fall at zero cost at current interest rates, at the IBRD lending rate and with co-benefits. With read-only copies of the model's other documents (use-it-or-lose-it paper, data plan, November roadmap). Code and data in `cpmodelai/climate-fiscal-ai-tools` | v0.2, 3 Nov 2026; awaiting review |
| `6.8.InvestmentAndAbatementCosts` | **Pricing the Measures: Investment Needs, Abatement Costs and Public Money in CPAT** (note 6.8): methodology for public investment need, capex and abatement costs of public money and green subsidies by sector, built on the SISEPUEDE cost factors; fees and subsidies outside energy; capital/running taxonomy with a PPP switch; CPAT-to-CDPM mapping; integration rules; power plug-in to the combined penalty rule of paper 5.1 | v0.3, 18 Nov 2026 (peer-reviewed); awaiting review |

`index.html` lists the numbered papers with links to their files, grouped by the section each will join; `build_folder_index.py` rewrites it on every compile.

## New papers: layout, and how a paper gets here and leaves

New papers sit directly in this folder, with no section level: section folders (`5.Modelling` and so on) exist only in the final folders, `C Policy and FInance` and `D Modelling`. Each paper folder has the standard layout (`H Writing Instructions/Scripts/Papers/Reference/_PaperFolderLayout.md`) and keeps the number of the section it will join, so it needs no renumbering when it moves.

- **In:** a new paper starts here, in `<N>.<k>.<Name>/`, where `<N>.<k>` is the next free number in the section it will join (`H Writing Instructions/NUMBERING.md`). Same masters as everywhere: the `.qmd` working paper and, for the web page, `1.Presentation/Brief-<Name>.qmd`. Add the folder to `WEB_PAPERS` in `H Writing Instructions/Scripts/Website/site_config.py` to put it on the site.
- **Out:** once Stephen has reviewed it, `git mv` the paper folder into its section folder in `C Policy and FInance` or `D Modelling` (for 5.5: `D Modelling/5.Modelling/`), then run `Compile-Website.bat`. The site pages move from `new/` to the section's tab by themselves, and the paper's number and file names stay the same. On the site, New Research groups its papers by the section they will join: add that section to the New Research part in `site_config.py` when the first paper for it arrives here, and remove it when the last one leaves.

Section overviews and theme decks stay with their sections in C and D.

## How the PhD research connects

- The application documents in `3 PhD Application/` (the UCL expression of interest, the Oxford and UCL proposals) are short versions of `ThesisPlan/` and `OverviewPaper/`. Change the thesis here first, then the application text.
- The thesis cross-references the paper series in `C Policy and FInance/` (series 1, 3 and 4) and `D Modelling/` (5.1, 6.1–6.5).
