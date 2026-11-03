"""Take the author's name and institutional affiliation out of everything the website publishes.

site_config.ANONYMOUS switches it on. The masters are never changed: only the copies made for the site are.
    build_web_papers.py   runs folder() over the web copies (.qmd and .bib) after writing them
    render_pdfs.py        renders each PDF from an anonymised copy of its master (and of its .bib),
                          and converts each deck to PDF from an anonymised copy of the .pptx
    site_config.py        leaves out SECTION_EXTRAS and WEB_BOOKS entries marked "named": True
                          (works already published under the author's name, which would identify him)

What changes:
    - the author block (author:) in the front matter is dropped
    - the byline "Stephen J. Stretton, writing in a personal capacity." is dropped
    - the World Bank's staff disclaimer becomes the plain personal one used elsewhere
    - in .bib files the author's name becomes {Author}, the usual form for a blinded self-citation
    - any other "Stretton" (citation keys such as @StrettonWP53) becomes "Author", in the text and the .bib alike,
      so keys still match
check(text) lists anything that still looks like the name, for a last look after a build.
"""
import re
import shutil
import tempfile
from pathlib import Path

PLAIN_DISCLAIMER = ("The views expressed are the author's own and do not represent those of any institution "
                    "with which he is or has been affiliated.")

TEXT_SUBS = [
    # the World Bank staff disclaimer
    (re.compile(r"The findings, interpretations,? and conclusions expressed in this (?:paper|brief|note|work) are "
                r"entirely those of the author(?:\(s\)|s)?\.\s*They do not necessarily represent the views of the "
                r"World Bank(?: Group)? and its affiliated organizations, or those of the Executive Directors of "
                r"the World Bank or the governments they represent\.", re.S), PLAIN_DISCLAIMER),
    # the byline
    (re.compile(r"Stephen J\.? Stretton,? writing in a personal capacity\.\s*"), ""),
    (re.compile(r"Stephen (?:J\.? )?Stretton"), "the author"),
    (re.compile(r"\bS\. ?J\. Stretton\b"), "the author"),
]

BIB_SUBS = [
    (re.compile(r"Stretton,\s*(?:Stephen|S\.)(?:\s*J\.?)?(?:\s*Stephen)?"), "{Author}"),
    (re.compile(r"Stephen\s+(?:J\.?\s+)?Stretton"), "{Author}"),
]

CATCH_ALL = (re.compile(r"Stretton"), "Author")


def drop_author_block(text):
    """Remove the author: key and its indented list from the front matter, if the text starts with one."""
    m = re.match(r"(---\n)(.*?\n)(---\n)", text, re.S)
    if not m:
        return text
    yaml = re.sub(r"^author:[^\n]*\n(?:(?:[ \t]+[^\n]*|[ \t]*-[^\n]*)?\n)*?(?=\S|\Z)", "", m.group(2), flags=re.M)
    return m.group(1) + yaml + m.group(3) + text[m.end():]


def text(s):
    s = drop_author_block(s)
    for pat, rep in TEXT_SUBS:
        s = pat.sub(rep, s)
    return CATCH_ALL[0].sub(CATCH_ALL[1], s)


def bib(s):
    for pat, rep in BIB_SUBS:
        s = pat.sub(rep, s)
    return CATCH_ALL[0].sub(CATCH_ALL[1], s)


def file(path):
    """Anonymise one .qmd or .bib in place."""
    path = Path(path)
    s = path.read_text(encoding="utf-8-sig")
    new = bib(s) if path.suffix.lower() == ".bib" else text(s)
    if new != s:
        path.write_text(new, encoding="utf-8")


def folder(root):
    for p in Path(root).rglob("*"):
        if p.is_file() and p.suffix.lower() in (".qmd", ".bib"):
            file(p)


def qmd_copy(qmd):
    """Write an anonymised copy of a master beside it (so relative paths still work), with anonymised copies of
    its .bib files. Returns the copy and the list of temporary files to delete afterwards."""
    qmd = Path(qmd)
    s = qmd.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    made = []

    def swap_bib(m):
        name = m.group(2)
        src = qmd.parent / name
        if not src.exists():
            return m.group(0)
        dst = src.with_name(f"_anon-{src.name}")
        dst.write_text(bib(src.read_text(encoding="utf-8-sig")), encoding="utf-8")
        made.append(dst)
        return m.group(1) + Path(name).with_name(dst.name).as_posix() + m.group(3)

    s = re.sub(r"^(\s*(?:bibliography:|-)\s*\"?)([^\s\"]+\.bib)(\"?\s*)$", swap_bib, s, flags=re.M)
    out = qmd.with_name(f"_anon-{qmd.name}")
    out.write_text(text(s), encoding="utf-8")
    made.append(out)
    return out, made


def pptx_copy(pptx):
    """An anonymised copy of a deck in a temporary folder, under the deck's own name (so the PDF is named the
    same). Returns the copy's path; the caller removes its folder."""
    from pptx import Presentation
    prs = Presentation(str(pptx))

    def fix(tf):
        for para in tf.paragraphs:
            whole = "".join(r.text for r in para.runs)
            if not re.search(r"Stretton|Stephen J", whole):
                continue
            new = re.sub(r"Stephen (?:J\.? )?Stretton", "", whole)
            new = re.sub(r"[,;:·•|–—-]?\s*writing in a personal capacity\.?", "", new, flags=re.I)
            new = CATCH_ALL[0].sub(CATCH_ALL[1], new).strip(" \t,;:·•|–—-")
            for i, run in enumerate(para.runs):
                run.text = new if i == 0 else ""

    def walk(shapes):
        for sh in shapes:
            if sh.has_text_frame:
                fix(sh.text_frame)
            if getattr(sh, "has_table", False) and sh.has_table:
                for row in sh.table.rows:
                    for cell in row.cells:
                        fix(cell.text_frame)
            if sh.shape_type == 6:          # group
                walk(sh.shapes)

    for slide in prs.slides:
        walk(slide.shapes)
        if slide.has_notes_slide:
            fix(slide.notes_slide.notes_text_frame)
    cp = prs.core_properties
    cp.author = ""
    cp.last_modified_by = ""
    d = Path(tempfile.mkdtemp(prefix="anon-deck-"))
    out = d / Path(pptx).name
    prs.save(str(out))
    return out


def check(s):
    """Fragments that still look like the author's name."""
    return re.findall(r".{0,40}(?:Stretton|Stephen J\.).{0,40}", s)
