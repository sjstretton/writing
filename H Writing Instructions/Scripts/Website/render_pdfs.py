"""Render papers to the working-paper format: an academic-style PDF (and, with --docx, a matching Word file).

The format is a Quarto extension kept once, in
    H Writing Instructions/Writing Standards/templates/_extensions/working-paper/
It typesets the PDF with Typst, which comes with Quarto (no LaTeX needed), in the website's look:
Source Serif 4 text, Source Sans 3 headings in the site's blue, a title block with the version and date,
the abstract with keywords and JEL codes, numbered sections, booktabs tables and running heads.
The fonts ship inside the extension, so every machine produces the same PDF.

Quarto only finds an extension in an _extensions folder beside the document, so for each master this script
copies the extension there, renders, and removes the copy. The masters' own YAML is not changed.

What it renders, for each paper (a paper folder name such as 1.1.OpenEconomyCarbonPricing):
    <PaperName>.qmd                      ->  <PaperName>.pdf           (beside the master)
    1.Presentation/Brief-<PaperName>.qmd ->  1.Presentation/Brief-<PaperName>.pdf
With --docx it also writes the .docx beside each (overwriting the existing Word file, which is made from the master).

Run from anywhere:
    python "H Writing Instructions/Scripts/Website/render_pdfs.py"                       every paper in WEB_PAPERS
    python "H Writing Instructions/Scripts/Website/render_pdfs.py" 1.1.OpenEconomyCarbonPricing --docx
    python "H Writing Instructions/Scripts/Website/render_pdfs.py" path/to/Any.qmd       any single .qmd
Compile-Website.bat runs it (PDF only) before publish_series.py, so the site links the PDFs.
"""
import shutil
import subprocess
import sys
from pathlib import Path
from site_config import REPO, SITE, WEB_PAPERS, PARTS, paper_name, master_qmd

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


def main(args):
    docx = "--docx" in args
    names = [a for a in args if not a.startswith("--")]
    formats = ["typst"] + (["docx"] if docx else [])
    quarto = find_quarto()
    if not quarto:
        print("Quarto not found - install Quarto (https://quarto.org). PDFs not rendered.")
        return 1
    qmds = []
    for n in names or WEB_PAPERS:
        if n.endswith(".qmd"):
            qmds.append(Path(n).resolve())
            continue
        folder = find_folder(n)
        if not folder:
            print(f"missing   {n}")
            continue
        name = paper_name(folder)
        for q in (master_qmd(folder), folder / "1.Presentation" / f"Brief-{name}.qmd"):
            if q and q.exists():
                qmds.append(q)
    ok = all([render(quarto, q, formats) for q in qmds])
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
