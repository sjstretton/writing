# Scripts

You only need these scripts, and they sit at the top of the repo:

| Script | What it does | When |
|---|---|---|
| `Compile-Website.bat` | Copies every paper, brief, overview and deck into `E Website/PaperArchive`, builds the web version of each paper in `site_config.py`'s list, rewrites the Policy and Finance and Modelling and Analytics pages from the papers' current abstracts, copies into `E Website/papers` only the files those pages link to, writes `index.html` in `C Policy and FInance` and `D Modelling`, then builds the site with Quarto. Nothing goes online. | After papers change, to check the site locally (`E Website/_site/index.html`). |
| `Push-Website.bat` | Uploads the already-built site to the web server and deletes files retired from the site. No compiling. | After Compile, when you have checked the site and want it live. |
| `Deploy-Website.bat` | Compile then Push, in one go. | When you want the site live and haven't just compiled. |

All need Python; Compile also needs Quarto (or RStudio, which includes Quarto). Push and Deploy also need the FTP login file `FTP-Login.txt` at the repo root (lines `host = `, `user = `, `password = `, `remote = /public_html`; it is git-ignored and never committed). Push uses WinSCP if installed, otherwise Python, so nothing else needs installing.

Everything below is optional. You can ignore this folder.

## What else is here

| Folder | What it is |
|---|---|
| `Website/deploy_ftp.py` | The upload step Push uses when WinSCP is not installed: plain Python FTP, sends only changed files, then makes the server's `papers/` match the built one (files no longer linked are deleted). |
| `Website/site_config.py` | The site's layout in one place: the two research parts (Policy and Finance: sections 1–4; Modelling and Analytics: 5–7), their sections, `WEB_PAPERS`, the papers that also get a web version, and `WEB_BOOKS`, the books read on the site chapter by chapter (now *Plucked!*, 8.5.3). When Modelling and Analytics moves to its own repository, delete its entry. |
| `Website/build_web_papers.py` | Makes the two web pages of each paper in `WEB_PAPERS`, each from its own master: the policy brief (`1.Presentation/Brief-<Name>.qmd`) as the paper's page, and the working paper (`<Name>.qmd`) one level below it. Under the first heading of each it puts links to the other form, its PDF and the slides; the PDF downloads go at the end. Cross-links written in the masters as `wp:`, `brief:` and `paper:1.2` become real links. Books in `WEB_BOOKS` get a contents page (with the whole-book PDF) under `policy/books/<Book>/` and one page per `# CHAPTER N:` heading, each with its own references and previous/next links. The copies are marked GENERATED and rewritten on every compile; edit the masters. |
| `Website/web-links.lua`, `Website/quarto-xref.lua` | Filters for rendering a master to Word: the first turns the `wp:`/`brief:`/`paper:` cross-links into plain text; the second numbers sections, figures, tables and equations and resolves `@sec-`/`@fig-` references when only pandoc is available. The render commands are in `Writing Standards/briefing-series-spec.md`. |
| `Website/render_pdfs.py` | Makes the PDF of everything the site offers (the site links PDFs only): every paper's master and brief, each section overview and each book, in the **working-paper format** (the Quarto extension in `Writing Standards/templates/_extensions/working-paper/`: Typst, which comes with Quarto, so no LaTeX; the site's fonts and blue; title band, abstract box with keywords and JEL codes, booktabs tables; the page rules in `NORMS.md` section 11); and each deck's PDF with LibreOffice if installed (otherwise save decks as PDF from PowerPoint). Each PDF goes beside its source. `--docx` also writes the matching Word file. Compile runs it first. One paper: `python render_pdfs.py 1.1.OpenEconomyCarbonPricing --docx`. |
| `Website/build_research_pages.py` | Writes each part's home page, one page per section (abstracts and links) and the sidebars (books and earlier papers, from `SECTION_EXTRAS` in `site_config.py`, go at the end of their section, and a web book's chapters under it in the sidebar), then fills `papers/` with exactly the linked files from `PaperArchive/`. There is no separate Books page. |
| `Website/build_folder_index.py` | Writes `index.html` at the top of `C Policy and FInance` and `D Modelling`: every paper with relative links to its master .qmd, Word files, brief and slides, for browsing the folders locally. Generated, not a master. |
| `Website/publish_series.py` | The copy step Compile runs: puts every paper's current docx, brief and deck, each with its PDF, the section overviews and theme decks, and the books into `E Website/PaperArchive` under stable names. The paper list comes from the section folders, so new papers need no edit. |
| `Website/InstallPackages.R` | R packages for rendering the site from RStudio. |
| `Website/Archive-batch/` | Old single-purpose website scripts (render, preview, push, deploy, remove old files), replaced by the two top-level scripts. |
| `Papers/Run/` | Double-click menus for the paper automation engine: `Start-Day`, `End-Day`, `Audit-Papers`, `Organise`, `Spring-Clean`, `Purge-Strays`, `Master-All`, `Master-Website`, `Preview-*`, `Push-Repo`, `Final-Check`, `Download-Literature`. Each explains itself and asks before changing anything. |
| `Papers/Engine/`, `Papers/Steps/` | The PowerShell and Python steps those menus call (PDF building, folder and file renaming, encoding repair, the website build and upload, literature downloads). |
| `Papers/Reference/` | The paper folder layout, the paper index, and the literature download list. |
| `SyncRepo.bat` | Pull and push the repo in one go. |

Both parts use the folders as they are after the 31 Oct 2026 restructure. The website scripts (`Website/`) read the papers in `C Policy and FInance` and `D Modelling` (`PARTS` in `site_config.py`). The paper engine (`Papers/`) walks `C Policy and FInance`, `D Modelling` and `F Other Writing`, listed once near the top of each script in `Papers/Steps/` as `$PaperRootNames`; when `D Modelling` moves to its own repository, remove it there and from `PARTS`. The engine's website step runs the same Python build as `Compile-Website.bat`, and its upload reads `FTP-Login.txt` at the repo root. The engine has not yet been run on Stephen's PC since this change: try `Run/Preview-All.bat` and `Run/Final-Check.bat` (both change nothing) before `Master-All` or `End-Day`.
