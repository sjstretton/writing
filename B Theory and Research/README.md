# B Theory and Research

New research that Stephen has not yet reviewed. On the website it is the **New Research** tab (`E Website/new/`).

## Layout

The same as `C Policy and FInance` and `D Modelling`: section folders named like the series, each holding numbered paper folders in the standard layout (`H Writing Instructions/Scripts/Papers/Reference/_PaperFolderLayout.md`). A paper keeps the number of the section it will join, so it needs no renumbering when it moves.

| Folder | Paper | Status |
|---|---|---|
| `5.Modelling/5.5.CarbonPriceNaturalExperiments` | 5.5 *Carbon Prices Cut Emissions: Evidence from Ten Natural Experiments* (working paper v0.1.1, Climate Fiscal Policy Brief No. 5.5 v0.1) | Awaiting review |

`index.html` lists every paper with links to its files; `build_folder_index.py` rewrites it on every compile.

## How a paper gets here and leaves

- **In:** a new paper starts here, in `<N>.<Section>/<N>.<k>.<Name>/`, where `<N>.<k>` is the next free number in the section it belongs to (`H Writing Instructions/NUMBERING.md`). Same masters as everywhere: the `.qmd` working paper and, for the web page, `1.Presentation/Brief-<Name>.qmd`. Add the folder to `WEB_PAPERS` in `H Writing Instructions/Scripts/Website/site_config.py` to put it on the site.
- **Out:** once Stephen has reviewed it, `git mv` the paper folder into the same section folder in `C Policy and FInance` or `D Modelling`, then run `Compile-Website.bat`. The site pages move from `new/` to the section's tab by themselves, and the paper's number and file names stay the same. Add the section to `site_config.py` (New Research part) when the first paper for a new section arrives here, and remove it when the last one leaves.

Section overviews and theme decks stay with their sections in C and D; sections here have none.
