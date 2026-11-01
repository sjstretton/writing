"""Copy every paper, brief, deck, section overview and book into the website's PaperArchive/ folder.

PaperArchive/ is the full set under stable names. It is NOT uploaded. build_research_pages.py then copies into
papers/ only the files the site's pages actually link to, and papers/ is what goes online.

Stable names, one per paper and form, overwritten on each run:
    <PaperName>.docx           the working paper (current version), from the master's own .docx
    Brief-<PaperName>.docx     the Climate Fiscal Policy Brief, where there is one
    Slides-<PaperName>.pptx    the deck, where there is one
    Overview<Section>.docx     each section's overview, and Slides-<Section>.pptx its theme deck
    books (BOOKS below)
Each file's PDF (made beside it by render_pdfs.py) is archived with it, under the same name with .pdf; the
site links only the PDFs.

The papers are every numbered paper folder in the sections listed in site_config.py, so a new paper folder is
picked up without editing this file. Missing briefs and decks are reported and skipped.

Run from anywhere:  python "H Writing Instructions/Scripts/Website/publish_series.py" (Compile-Website.bat does this)
Log every publish in H Writing Instructions/Writing Standards/publishing-log.md.
"""
import shutil
from site_config import PARTS, ARCHIVE, paper_folders, paper_name, section_folder

# book folder (anywhere under a part's root), file inside it, published name
BOOKS = [
    ("3.3.TimeAndChance", "TimeAndChance.docx", "TimeAndChance.docx"),
    ("8.5.2.CarbonPricingRightPolicyWrongTime", "CarbonPricingRightPolicyWrongTime.docx", "CarbonPricingRightPolicyWrongTime.docx"),
    ("8.5.3.Plucked", "Plucked.docx", "Plucked.docx"),
    ("SLIDIs", "SLIDIs.docx", "SLIDIs.docx"),
]


def copy(src, dst):
    """Copy a file into the archive, and its PDF (made by render_pdfs.py) beside it under the same stable name."""
    if src and src.exists():
        shutil.copy2(src, dst)
        print(f"archived  {dst.name}")
        if src.with_suffix(".pdf").exists() and src.suffix != ".pdf":
            shutil.copy2(src.with_suffix(".pdf"), dst.with_suffix(".pdf"))
            print(f"archived  {dst.with_suffix('.pdf').name}")
    else:
        print(f"missing   {src}")


def main():
    ARCHIVE.mkdir(exist_ok=True)
    for part in PARTS:
        for sec in part["sections"]:
            num = sec[0].split(".")[0]
            ov_dir = section_folder(part, sec) / f"{num}.0.Overview"
            ov = next(iter(sorted(ov_dir.glob(f"{num}.0.Overview*.docx"))), None) if ov_dir.is_dir() else None
            copy(ov, ARCHIVE / sec[4])
            if sec[5]:
                copy(ov_dir / "1.Presentation" / sec[5], ARCHIVE / sec[5])
            for folder in paper_folders(part, sec):
                name = paper_name(folder)
                copy(folder / f"{name}.docx", ARCHIVE / f"{name}.docx")
                for f in (f"Brief-{name}.docx", f"Slides-{name}.pptx"):
                    if (folder / "1.Presentation" / f).exists():
                        copy(folder / "1.Presentation" / f, ARCHIVE / f)
                    else:
                        print(f"none      {f}")
        for folder_name, fname, pub in BOOKS:
            hits = [p for p in part["root"].rglob(folder_name) if p.is_dir()]
            if hits:
                copy(hits[0] / fname, ARCHIVE / pub)


if __name__ == "__main__":
    main()
