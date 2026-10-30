# Instructions for the section 4 and 5 writing agents (29 Oct 2026)

Follow `WRITER-BRIEF.md` (same folder) for reading list, rules, rendering, confidentiality, git and the final report, with these changes:

1. **Plan:** `B Working Papers/4.Modelling/SeriesArchitecture.md` (covers sections 4 and 5). Read it first.
2. **One paper per item, medium form:** no separate brief, no deck. Master `<Name>.qmd` + `<Name>.bib` + `<Name>.docx` at the folder root; about 4,000–6,000 words of body (4.1 up to about 9,000). Working-paper front matter as in `B Working Papers/2.FinanceAndRisk/2.2.CleanPowerAssetClasses/CleanPowerAssetClasses.qmd` (use its YAML and first italic line as the template; the italic line names the companion repository instead of a brief, e.g. "Companion paper to the CPAT-AI repository, https://github.com/cpmodelai/cpat_ai"; for section 5 say "companion paper to the Climate Fiscal AI Tools" without a URL, because that repository is private).
3. **Sources are mostly in other repositories**, cloned read-only at `/home/user/cpmodelai/cpat_ai`, `/home/user/climate-fiscal-ai-tools` and `/home/user/cpmodelai/CPAT-CDPM`. Do not edit those repositories. Convert docx with `pandoc -t plain`; read pptx with `python3 -c` and the zip XML or skip them. The source digests in this folder cover section 2/3 material only.
4. **Condense, do not transcribe.** These papers make the tools legible to an economist in an afternoon: what the tool is for, its core method (key equations in LaTeX math), what it shows (one worked example with public or stylized numbers), its validation and limits, and how to use it. Figures optional; one table minimum.
5. **Existing masters:** where a master exists at the folder root (5.1), move it to `8.PreviousVersions/<Name>-v0.1.*` with `git mv` and make the new one v0.2. New papers start at v0.1.
6. **Folder README:** status, files, sources used, items held back for confidentiality.
7. Do not edit `SeriesArchitecture.md`, the overviews, `PAPERS.md`, `TODO.md` or the website.
