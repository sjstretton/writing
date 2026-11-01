# Working-paper format

A Quarto extension that gives the papers an academic working-paper look, matching the website.

- **PDF** (`working-paper-typst`): typeset with Typst, which comes with Quarto 1.5+ (no LaTeX). A4; Source Serif 4 text and Source Sans 3 headings in the site's blue (`#1a5490`); a title band with series, version and date; the abstract in a tinted box with keywords and JEL codes; numbered sections; booktabs tables; running heads; appendices unnumbered on a new page. The fonts are in `fonts/` (SIL Open Font License), so the PDF is the same on every machine.
- **Word** (`working-paper-docx`): the same structure with `reference.docx` styles (Cambria text, Calibri headings in the same blue, A4, page numbers), because Word readers will not have the web fonts. Rebuild the styles with `make_reference_docx.py`.
- `working-paper.lua` (both forms): keeps only the text of `wp:`/`brief:`/`paper:` cross-links, leaves appendix headings unnumbered, and adds keywords and JEL codes under the abstract in Word.

YAML it reads from the master: `title`, `subtitle`, `short-title` (running head, optional), `author` (`name`, `note`, `affiliation`), `date`, `series` (e.g. "Climate Fiscal Policy Brief No. 1.1"; default "Working paper"), `version`, `abstract`, `keywords`, `jel`.

Render with `H Writing Instructions/Scripts/Website/render_pdfs.py` (it puts this extension beside the master while rendering, because Quarto looks for extensions only there):

    python "H Writing Instructions/Scripts/Website/render_pdfs.py" 1.1.OpenEconomyCarbonPricing --docx
