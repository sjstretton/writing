# Scripts

You only need these scripts, and they sit at the top of the repo:

| Script | What it does | When |
|---|---|---|
| `Compile-Website.bat` | Copies every paper, brief, overview and deck into `E Website/PaperArchive`, builds the web version of each paper in `site_config.py`'s list, rewrites the Policy and Finance and Modelling and Analytics pages from the papers' current abstracts, copies into `E Website/papers` only the files those pages link to, writes `index.html` in `C Policy and FInance` and `D Modelling`, then builds the site with Quarto. Nothing goes online. | After papers change, to check the site locally (`E Website/_site/index.html`). |
| `Push-Website.bat` | Uploads the already-built site to the web server and deletes files retired from the site. No compiling. | After Compile, when you have checked the site and want it live. |
| `Deploy-Website.bat` | Compile then Push, in one go. | When you want the site live and haven't just compiled. |

All need Python; Compile also needs Quarto (or RStudio, which includes Quarto). Push and Deploy also need the FTP login file `Papers/Reference/_ftp.txt` (copy `_ftp.txt.example` and fill it in; it is never committed). It uses WinSCP if installed, otherwise Python, so nothing else needs installing. If your login file is still in the old place, `B Working Papers/B.Scripts/Reference/_ftp.txt`, Deploy finds it there too; move it here when convenient.

Everything below is optional. You can ignore this folder.

## What else is here

| Folder | What it is |
|---|---|
| `Website/deploy_ftp.py` | The upload step Push uses when WinSCP is not installed: plain Python FTP, sends only changed files, then makes the server's `papers/` match the built one (files no longer linked are deleted). |
| `Website/site_config.py` | The site's layout in one place: the two research parts (Policy and Finance: sections 1–4; Modelling and Analytics: 5–7), their sections, and `WEB_PAPERS`, the papers that also get a web version. When Modelling and Analytics moves to its own repository, delete its entry. |
| `Website/build_web_papers.py` | Makes the web version of each paper in `WEB_PAPERS` from its master .qmd (figures, references, an 'In brief' box from the policy brief, download links). The copy is marked GENERATED and rewritten on every compile; edit the master. |
| `Website/build_research_pages.py` | Writes each part's home page, one page per section (abstracts and links) and the sidebars, then fills `papers/` with exactly the linked files from `PaperArchive/`. `policy/more.qmd` (Books and other papers) is written by hand. |
| `Website/build_folder_index.py` | Writes `index.html` at the top of `C Policy and FInance` and `D Modelling`: every paper with relative links to its master .qmd, Word files, brief and slides, for browsing the folders locally. Generated, not a master. |
| `Website/publish_series.py` | The copy step Compile runs: puts every paper's current docx, brief and deck, the section overviews and theme decks, and the books into `E Website/PaperArchive` under stable names. The paper list comes from the section folders, so new papers need no edit. |
| `Website/InstallPackages.R` | R packages for rendering the site from RStudio. |
| `Website/Archive-batch/` | Old single-purpose website scripts (render, preview, push, deploy, remove old files), replaced by the two top-level scripts. |
| `Papers/Run/` | Double-click menus for the paper automation engine: `Start-Day`, `End-Day`, `Audit-Papers`, `Organise`, `Spring-Clean`, `Purge-Strays`, `Master-All`, `Master-Website`, `Preview-*`, `Push-Repo`, `Final-Check`, `Download-Literature`. Each explains itself and asks before changing anything. |
| `Papers/Engine/`, `Papers/Steps/` | The PowerShell and Python steps those menus call (PDF building, folder and file renaming, encoding repair, publishing, literature downloads). |
| `Papers/Reference/` | The paper folder layout, the paper index, the literature download list and the FTP login template. |
| `SyncRepo.bat` | Pull and push the repo in one go. |

These scripts moved here from `B Working Papers/B.Scripts` and `B Working Papers/A.Website` on 31 Oct 2026. They find the papers by walking up to the repo root and opening `B Working Papers`, so they work from this folder; they have not yet been run on Windows since the move, so if one stops with a path error, tell an agent.
