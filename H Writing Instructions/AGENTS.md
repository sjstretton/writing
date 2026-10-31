# AGENTS.md (writing)

Instructions for AI agents working on the **writing** part of the combined repo: folders A–H. The repo root `AGENTS.md` covers both parts (planning, folders 1–4; writing, folders A–H) and says which instructions apply; read it first, then this file, then `NORMS.md` (in this folder).

## What the writing part is for

This is Stephen Stretton's research workspace. Its job right now is to turn a large set of draft papers into a small set of excellent ones, and to support two PhD applications. Everything an agent does should serve the priorities in `STRATEGY.md`.

## Where things are

Read the file that matches your task before you start. Files in this folder (`H Writing Instructions/`) are named alone; folders are named from the repo root.

| File or folder | Use it for |
|---|---|
| `NORMS.md` | The rules every piece of writing must meet. Short. Always applies. |
| `STRATEGY.md` | Stephen's strategic priorities and specialisms. Decides what matters. |
| `TODO.md` | The live task list. Take work from the top. Update it when you finish. |
| `PAPERS.md` | Prioritised papers, introductory papers, concept papers and position papers. |
| `NUMBERING.md` | The canonical paper numbers (section folder plus place in the section), with the old-to-new map and citation-key rules. |
| `H Writing Instructions/Writing Standards/` | Writing principles, writing types, the paper standard, AI tells to avoid, exemplars and templates. |
| `B PhD Application/` | The PhD research proposals. Its `README.md` tracks their status. |
| `C Policy and FInance/`, `D Modelling/` | The papers, numbered by section: 1.x to 4.x in `C Policy and FInance`, 5.x to 7.x in `D Modelling` (due to move to its own repo). Each section has one `<N>.0.Overview` folder. `index.html` at the top of each lists every paper with links to its files. |
| `F Other Writing/` | Writing outside the series and not on the website (8.x: other fiscal policy, The Sollar, MDB papers, political economy, philosophy, politics). |
| `E Website/` | The Quarto site. Layout and the list of papers with a web version: `Scripts/Website/site_config.py`. |
| `H Writing Instructions/Scripts/` | Website scripts and the paper automation engine. Its `README.md` says which you need. |
| `G Climate Econ Course/` | Course materials. |
| `H Writing Instructions/Templates and Info/` | Older Word templates (briefing, one-page pitch). |
| `H Writing Instructions/Claude + Scripts/Setup Claude/_admin/` | `about-me.md` and `voice.md`: who Stephen is and how he sounds. Read before drafting anything in his name. |
| `Writing-Status-Report.md` | 29 Oct 2026 audit of every paper and the housekeeping problems (H1–H17). |

Folders with their own `README.md` have local conventions. Read that first.

## How to upgrade a paper

Follow these steps in order. A paper is not finished until it passes the checklist in `H Writing Instructions/Writing Standards/paper-standard.md`.

1. Read the paper, its folder README, its entry in `PAPERS.md` and its line in `Writing-Status-Report.md`.
2. Write down, in two sentences, the paper's question and its answer. If you cannot, the paper's problem is thinking, not prose. Fix that first and tell Stephen.
3. Decide the writing type (`H Writing Instructions/Writing Standards/writing-types.md`) and the reader.
4. Restructure to the paper standard. Then rewrite paragraph by paragraph using `writing-principles.md`.
5. Run the skim test: read only the title, abstract, headings and the first sentence of every paragraph. A busy reader should get the whole argument.
6. Check every citation and number. Mark anything you could not verify with `[VERIFY: ...]`. Never invent a source.
7. Save the upgrade as a new version (see "Files" below), update `PAPERS.md` and `TODO.md`, and commit.

## General rules

- Make the changes asked for. Don't reorganise, rename or delete files unless asked.
- Read a file before editing it, and match the surrounding style and formatting.
- Don't invent citations, figures, quotes or results. Mark anything uncertain.
- Don't commit secrets, credentials or personal data. The FTP login lives in `FTP-Login.txt` at the repo root, which is git-ignored.
- Treat World Bank internal or confidential material as non-public. Never publish it (see below).

## Files

- Keep the paper folder layout: `1.Presentation`, `2.Source`, `3.RelatedPiecesAndLinks` (older folders still say `3.BackgroundPapers`), `5.Notes`, `8.PreviousVersions`, `9.Archive`, plus `RelatedWork.md` for related pieces that live in other main folders. Convention: `H Writing Instructions/Scripts/Papers/Reference/_PaperFolderLayout.md`.
- The `.qmd` file at the paper's root is the master unless its README says otherwise. Where qmd and docx disagree (status report H13), ask which is the master before editing.
- Versions: the master carries `version:` in its YAML; older versions go in `8.PreviousVersions/` as `<Name>-v0.1.<ext>`, `<Name>-v0.2.<ext>`. Before a major rewrite, move the current master there under its version number and bump the master.
- New papers start from `H Writing Instructions/Writing Standards/templates/`.

## Publishing (standing authorization)

Stephen has given standing authorization (29 Oct 2026) for agents to publish to his own websites without asking each time. That currently means the Quarto site in `E Website`. Publishing means editing the site source, rendering it and deploying it.

This authorization holds only when every item below is true. If any fails, stop and ask.

- The content passes `NORMS.md`, and papers pass the paper-standard checklist.
- Nothing is marked confidential, internal, draft-for-comment or "not for circulation", and nothing contains World Bank internal material.
- Every citation is verified. No `[VERIFY]` or `TODO` markers remain.
- The change is logged in `H Writing Instructions/Writing Standards/publishing-log.md` (date, what, where, commit).

Social media, email and any channel other than Stephen's own websites still need his explicit approval each time.

Deployment needs the FTP credentials and WinSCP on Stephen's Windows machine (`Push-Website.bat` at the repo root). A cloud agent without them should commit and push the site source, log the change as "ready to deploy", and say so.

## Git

- Work on the branch you were assigned. Don't push to other branches.
- Write clear, descriptive commit messages.
- Don't open pull requests unless asked.
- Don't commit generated output (`_site/`, `Scripts/Papers/Reports/`) unless the repo already tracks it.

## Website and scripts

- The Quarto site source is in `E Website`, and the automation engine is in `H Writing Instructions/Scripts`. Check their READMEs before changing them.
- The website scripts (`Scripts/Website/`) and the paper automation engine (`Scripts/Papers/`) both use the current folders. The engine walks `C Policy and FInance`, `D Modelling` and `F Other Writing` (listed once per script as `$PaperRootNames` in `Scripts/Papers/Steps/`). It was updated on 31 Oct 2026 without being run on Windows, so preview first (`Run/Preview-All.bat`, `Run/Final-Check.bat`) before any run that changes files.
- The master for each paper is its `.qmd`; its first YAML line says `# MASTER`. Web copies under `E Website/policy/` and `E Website/modelling/` say `# GENERATED - NOT THE MASTER` and are rewritten on every compile: never edit them.
