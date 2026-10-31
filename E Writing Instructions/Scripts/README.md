# Scripts

You only need two scripts, and they sit at the top of the repo:

| Script | What it does | When |
|---|---|---|
| `Compile-Website.bat` | Copies every paper, brief, overview and deck into the website folder, then builds the site with Quarto. Nothing goes online. | After papers change, to check the site locally (`B Working Papers/A.Website/_site/index.html`). |
| `Deploy-Website.bat` | Runs Compile, uploads the built site to the web server, and deletes files retired from the site. | When you want the site live. |

Both need Python and Quarto (or RStudio, which includes Quarto). Deploy also needs WinSCP and the FTP login file `Papers/Reference/_ftp.txt` (copy `_ftp.txt.example` and fill it in; it is never committed). If your login file is still in the old place, `B Working Papers/B.Scripts/Reference/_ftp.txt`, Deploy finds it there too; move it here when convenient.

Everything below is optional. You can ignore this folder.

## What else is here

| Folder | What it is |
|---|---|
| `Website/publish_series.py` | The copy step Compile runs: puts each paper's current docx, brief, overview and deck into the site's `papers/` folder under stable names. Add a new paper to its list. |
| `Website/InstallPackages.R` | R packages for rendering the site from RStudio. |
| `Website/Archive-batch/` | Old single-purpose website scripts (render, preview, push, deploy, remove old files), replaced by the two top-level scripts. |
| `Papers/Run/` | Double-click menus for the paper automation engine: `Start-Day`, `End-Day`, `Audit-Papers`, `Organise`, `Spring-Clean`, `Purge-Strays`, `Master-All`, `Master-Website`, `Preview-*`, `Push-Repo`, `Final-Check`, `Download-Literature`. Each explains itself and asks before changing anything. |
| `Papers/Engine/`, `Papers/Steps/` | The PowerShell and Python steps those menus call (PDF building, folder and file renaming, encoding repair, publishing, literature downloads). |
| `Papers/Reference/` | The paper folder layout, the paper index, the literature download list and the FTP login template. |
| `SyncRepo.bat` | Pull and push the repo in one go. |

These scripts moved here from `B Working Papers/B.Scripts` and `B Working Papers/A.Website` on 31 Oct 2026. They find the papers by walking up to the repo root and opening `B Working Papers`, so they work from this folder; they have not yet been run on Windows since the move, so if one stops with a path error, tell an agent.
