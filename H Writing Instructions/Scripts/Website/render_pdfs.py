"""Render papers to the working-paper format: an academic-style PDF (and, with --docx, a matching Word file).

The format is a Quarto extension kept once, in
    H Writing Instructions/Writing Standards/templates/_extensions/working-paper/
It typesets the PDF with Typst, which comes with Quarto (no LaTeX needed), in the website's look:
Source Serif 4 text, Source Sans 3 headings in the site's blue, a title block with the version and date,
the abstract with keywords and JEL codes, numbered sections, booktabs tables and running heads.
The fonts ship inside the extension, so every machine produces the same PDF.

Quarto only finds an extension in an _extensions folder beside the document, so for each master this script
copies the extension there, renders, and removes the copy. The masters' own YAML is not changed.

What it renders (everything the website offers for download; the site links PDFs only):
    each paper's master <PaperName>.qmd       ->  <PaperName>.pdf        (beside the master)
    1.Presentation/Brief-<PaperName>.qmd      ->  Brief-<PaperName>.pdf
    each section overview <N>.0.Overview/*.qmd and each book in publish_series.BOOKS, the same way
    each deck 1.Presentation/Slides-*.pptx    ->  Slides-*.pdf           (with LibreOffice, if installed;
                                                  otherwise save the deck as PDF from PowerPoint)
With --docx it also writes the .docx beside each .qmd (overwriting the Word file, which is made from the master).

Run from anywhere:
    python "H Writing Instructions/Scripts/Website/render_pdfs.py"                       everything
    python "H Writing Instructions/Scripts/Website/render_pdfs.py" 1.1.OpenEconomyCarbonPricing --docx
    python "H Writing Instructions/Scripts/Website/render_pdfs.py" path/to/Any.qmd       any single .qmd
Compile-Website.bat runs it (PDF only) before publish_series.py.
"""
import shutil
import subprocess
import sys
from pathlib import Path
from site_config import REPO, SITE, PARTS, paper_name, master_qmd, paper_folders, section_folder
from publish_series import BOOKS

EXT = REPO / "H Writing Instructions" / "Writing Standards" / "templates" / "_extensions" / "working-paper"
CSL = SITE / "chicago-author-date.csl"   # local copy, so rendering needs no internet


def find_quarto():
    q = shutil.which("quarto")
    if q:
        return q
    for d in (r"C:\Program Files\Quarto\bin", r"C:\Program Files\RStudio\resources\app\bin\quarto\bin",
              r"C:\Program Files\RStudio\resources\app\quarto\bin"):
        p = Path(d) / "quarto.exe"
        if p.exists():
            return str(p)
    return None


def find_folder(folder_name):
    for part in PARTS:
        hits = [p for p in part["root"].rglob(folder_name) if p.is_dir() and "8.PreviousVersions" not in p.parts]
        if hits:
            return hits[0]
    return None


def render(quarto, qmd, formats):
    """Render one .qmd to each format, with the extension copied beside it for the duration."""
    ext_root = qmd.parent / "_extensions"
    made_root = not ext_root.exists()
    target = ext_root / "working-paper"
    shutil.copytree(EXT, target, dirs_exist_ok=True)
    ok = True
    try:
        for fmt in formats:
            cmd = [quarto, "render", qmd.name, "--to", f"working-paper-{fmt}"]
            if CSL.exists():
                cmd += ["-M", f"csl:{CSL.as_posix()}"]
            r = subprocess.run(cmd, cwd=qmd.parent, capture_output=True, text=True)
            out = qmd.with_suffix(".pdf" if fmt == "typst" else ".docx")
            if r.returncode == 0 and out.exists():
                print(f"rendered  {out.relative_to(REPO)}")
            else:
                ok = False
                print(f"FAILED    {qmd.relative_to(REPO)} ({fmt})\n{r.stderr[-2000:]}")
    finally:
        shutil.rmtree(target, ignore_errors=True)
        if made_root:
            shutil.rmtree(ext_root, ignore_errors=True)
    return ok


def find_soffice():
    for n in ("soffice", "libreoffice"):
        if shutil.which(n):
            return shutil.which(n)
    for d in (r"C:\Program Files\LibreOffice\program", r"C:\Program Files (x86)\LibreOffice\program"):
        p = Path(d) / "soffice.exe"
        if p.exists():
            return str(p)
    return None


def deck_to_pdf(soffice, pptx):
    """Save a deck as PDF beside it, unless the PDF is already newer than the deck."""
    pdf = pptx.with_suffix(".pdf")
    if pdf.exists() and pdf.stat().st_mtime >= pptx.stat().st_mtime:
        return True
    r = subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir", str(pptx.parent), str(pptx)],
                       capture_output=True, text=True)
    ok = r.returncode == 0 and pdf.exists()
    print(f"{'converted' if ok else 'FAILED   '} {pdf.relative_to(REPO)}")
    return ok


def paper_targets(folder):
    """The .qmd masters and the decks of one paper folder."""
    name = paper_name(folder)
    pres = folder / "1.Presentation"
    qmds = [q for q in (master_qmd(folder), pres / f"Brief-{name}.qmd") if q and q.exists()]
    decks = [pres / f"Slides-{name}.pptx"] if (pres / f"Slides-{name}.pptx").exists() else []
    return qmds, decks


def everything():
    qmds, decks = [], []
    for part in PARTS:
        for sec in part["sections"]:
            num = sec[0].split(".")[0]
            ov = section_folder(part, sec) / f"{num}.0.Overview"
            qmds += sorted(ov.glob(f"{num}.0.Overview*.qmd")) if ov.is_dir() else []
            if sec[5] and (ov / "1.Presentation" / sec[5]).exists():
                decks.append(ov / "1.Presentation" / sec[5])
            for folder in paper_folders(part, sec):
                q, d = paper_targets(folder)
                qmds += q
                decks += d
        for folder_name, fname, pub in BOOKS:
            hits = [p for p in part["root"].rglob(folder_name) if p.is_dir() and "9.Archive" not in p.parts]
            if hits and (hits[0] / fname).with_suffix(".qmd").exists():
                qmds.append((hits[0] / fname).with_suffix(".qmd"))
    return list(dict.fromkeys(qmds)), list(dict.fromkeys(decks))


def main(args):
    docx = "--docx" in args
    names = [a for a in args if not a.startswith("--")]
    formats = ["typst"] + (["docx"] if docx else [])
    quarto = find_quarto()
    if not quarto:
        print("Quarto not found - install Quarto (https://quarto.org). PDFs not rendered.")
        return 1
    if names:
        qmds, decks = [], []
        for n in names:
            if n.endswith(".qmd"):
                qmds.append(Path(n).resolve())
                continue
            folder = find_folder(n)
            if not folder:
                print(f"missing   {n}")
                continue
            q, d = paper_targets(folder)
            qmds += q
            decks += d
    else:
        qmds, decks = everything()
    ok = all([render(quarto, q, formats) for q in qmds])
    soffice = find_soffice()
    if decks and not soffice:
        print("LibreOffice not found: decks not converted. Save each Slides-*.pptx as PDF from PowerPoint.")
    elif decks:
        ok = all([deck_to_pdf(soffice, d) for d in decks]) and ok
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
