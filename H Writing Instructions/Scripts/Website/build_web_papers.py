"""Make the web version of each paper from its master .qmd, so the site shows the paper itself, not only a download.

For each paper in WEB_PAPERS this writes, in E Website:
    <part>/<section-slug>/<PaperName>/index.qmd   a copy of the master with web settings
    <part>/<section-slug>/<PaperName>/<PaperName>.bib
    <part>/<section-slug>/<PaperName>/<figure paths>   every figure the paper uses, at the same relative path

The master stays where it is (C Policy and FInance or D Modelling/<section>/<paper folder>/<PaperName>.qmd) and is the only file to edit.
The web copy is NOT a master: it is deleted and rewritten on every compile, and its first line says so.

What changes in the copy:
    - format: docx is dropped (the site's own html format applies);
    - csl: points at the site's local copy of the Chicago style, so the build needs no internet;
    - an "In brief" box (the policy brief's abstract, if there is a brief) and download links are added at the top.

Books in WEB_BOOKS get the same treatment, split into one page per chapter, in E Website:
    <part>/books/<BookName>/index.qmd          the book's contents page (title, description, download, chapters)
    <part>/books/<BookName>/NN-<chapter>.qmd   one page per "# CHAPTER N: TITLE" heading in the master
    <part>/books/<BookName>/<BookName>.bib and the figures, as for papers
Each chapter page ends with its own references and links to the previous and next chapters.

Compile-Website.bat runs this after publish_series.py and before build_research_pages.py.
To put another paper on the web, add its folder to WEB_PAPERS in site_config.py; for a book, add it to WEB_BOOKS.
"""
import re
import shutil
from pathlib import Path
from site_config import (REPO, PARTS, SITE, ARCHIVE, WEB_PAPERS, WEB_BOOKS, part_of_section, part_by_key,
                         paper_name, master_qmd, book_dir, book_name)


def find(folder_name):
    for part in PARTS:
        hits = [p for p in part["root"].rglob(folder_name) if p.is_dir() and "8.PreviousVersions" not in p.parts]
        if hits:
            return hits[0]
    return None


def split_front_matter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise SystemExit("no front matter")
    return m.group(1), text[m.end():]


def drop_key(yaml, key):
    """Remove a top-level key and its indented block from simple YAML text."""
    out, skip = [], False
    for line in yaml.split("\n"):
        if re.match(rf"^{key}:", line):
            skip = True
            continue
        if skip and (line.startswith(" ") or not line.strip()):
            continue
        skip = False
        out.append(line)
    return "\n".join(out)


def yaml_value(yaml, key):
    m = re.search(rf"^{key}:\s*(\|[-+]?|>[-+]?)?\s*\n((?:  .*\n?)+)", yaml, re.M)
    if m:
        return " ".join(l.strip() for l in m.group(2).split("\n") if l.strip())
    m = re.search(rf"^{key}:\s*\"?(.*?)\"?\s*$", yaml, re.M)
    return m.group(1) if m else None


def copy_figures_and_bib(folder, dest, yaml, body):
    """Copy every local image the body refers to (keeping its relative path) and the bibliography."""
    for rel in sorted(set(re.findall(r"\]\(([^)\s]+?\.(?:png|jpe?g|svg|gif))\)", body, re.I))):
        src = folder / rel
        if src.exists():
            (dest / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest / rel)
        else:
            print(f"missing figure {src}")
    bib = yaml_value(yaml, "bibliography")
    if bib and (folder / bib).exists():
        shutil.copy2(folder / bib, dest / bib)


def generated_header(master):
    return (f"# GENERATED - NOT THE MASTER. Made from {master.relative_to(REPO).as_posix()} by build_web_papers.py\n"
            f"# on every compile; edits here are lost. Edit the master instead.\n")


SMALL = {"a", "an", "and", "as", "at", "but", "by", "for", "in", "of", "or", "the", "to", "with"}


def title_case(s):
    """'MONEY, DEBT, AND FINANCE' -> 'Money, Debt, and Finance' (small words lower case except first and after a colon)."""
    words, out, start = s.lower().split(), [], True
    for w in words:
        out.append(w if (w in SMALL and not start) else w[:1].upper() + w[1:])
        start = w.endswith(":")
    return " ".join(out)


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def yq(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


def build_book(folder_name, cfg):
    """A book's web version: a contents page and one page per chapter, split at '# CHAPTER N: TITLE' headings."""
    folder = find(folder_name)
    if not folder:
        print(f"missing   {folder_name}")
        return
    part = part_by_key(cfg["part"])
    name = book_name(folder_name)
    master = folder / f"{name}.qmd"
    text = master.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    yaml, body = split_front_matter(text)
    body = re.sub(r"^\\newpage\s*$\n?", "", body, flags=re.M)        # LaTeX page breaks mean nothing on the web

    dest = SITE / book_dir(part, name)
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    copy_figures_and_bib(folder, dest, yaml, body)

    heads = list(re.finditer(r"^# CHAPTER (\d+):\s*(.+?)\s*$", body, re.M))
    if not heads:
        raise SystemExit(f"{master}: no '# CHAPTER N: TITLE' headings to split at")
    preface = body[:heads[0].start()].strip()
    chapters = []
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(body)
        title = title_case(h.group(2))
        chapters.append({"num": h.group(1), "title": title, "body": body[h.end():end].strip(),
                         "file": f"{i + 1:02d}-{slugify(title)}.qmd"})

    book_title = yaml_value(yaml, "title")
    subtitle = yaml_value(yaml, "subtitle")
    full_title = f"{book_title} {subtitle}" if subtitle else book_title
    csl = "csl: ../../../chicago-author-date.csl"
    bib = yaml_value(yaml, "bibliography")
    header = generated_header(master)
    names = re.findall(r"^\s*-?\s*name:\s*\"?(.*?)\"?\s*$", yaml, re.M)
    authors = " and ".join([", ".join(names[:-1]), names[-1]]) if len(names) > 1 else (names[0] if names else "")

    # contents page
    contents_yaml = re.sub(r"^#.*\n?", "", yaml, flags=re.M)
    contents_yaml = drop_key(drop_key(drop_key(contents_yaml, "format"), "bibliography"), "csl")
    contents_yaml = drop_key(drop_key(contents_yaml, "toc"), "version")
    top = [cfg.get("blurb", "") + "\n"]
    if (ARCHIVE / f"{name}.docx").exists():
        top.append(f"**Download:** [The whole book (Word)](../../../papers/{name}.docx)\n")
    if preface:
        top.append(preface + "\n")
    top.append("# Contents {.unnumbered}\n")
    top.append("\n".join(f"- [Chapter {c['num']}: {c['title']}]({c['file']})" for c in chapters) + "\n")
    (dest / "index.qmd").write_text(f"---\n{header}{contents_yaml.rstrip()}\ntoc: false\n---\n\n" + "\n".join(top),
                                    encoding="utf-8")

    # chapter pages
    for i, c in enumerate(chapters):
        prev = chapters[i - 1] if i > 0 else None
        nxt = chapters[i + 1] if i + 1 < len(chapters) else None
        nav = " · ".join(x for x in (
            f"[← Chapter {prev['num']}: {prev['title']}]({prev['file']})" if prev else None,
            f"[Contents](index.qmd)",
            f"[Chapter {nxt['num']}: {nxt['title']} →]({nxt['file']})" if nxt else None) if x)
        chapter_title = f"Chapter {c['num']}: {c['title']}"
        cy = (f"---\n{header}title: {yq(chapter_title)}\n"
              f"subtitle: {yq(full_title)}\n"
              f"bibliography: {bib}\n{csl}\ntoc: true\n---\n\n")
        page = (cy + f"*From [{book_title}](index.qmd), by {authors}.*\n\n"
                + c["body"] + "\n\n# References {.unnumbered}\n\n::: {#refs}\n:::\n\n---\n\n" + nav + "\n")
        (dest / c["file"]).write_text(page, encoding="utf-8")
    print(f"web book  {dest} ({len(chapters)} chapters)")


def build(folder_name):
    folder = find(folder_name)
    if not folder:
        print(f"missing   {folder_name}")
        return
    part, sec = part_of_section(folder_name.split(".")[0])
    slug = sec[1]
    name = paper_name(folder)
    master = master_qmd(folder)
    text = master.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    yaml, body = split_front_matter(text)

    dest = SITE / part["dir"] / slug / name
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)

    copy_figures_and_bib(folder, dest, yaml, body)

    yaml = re.sub(r"^#.*\n?", "", yaml, flags=re.M)          # drop the master's own comment lines
    yaml = drop_key(yaml, "format")
    yaml = re.sub(r"^csl:.*$", "csl: ../../../chicago-author-date.csl", yaml, flags=re.M)
    yaml = generated_header(master) + yaml.rstrip("\n") + "\ntoc: true\ndate-format: \"MMMM YYYY\"\n"

    # the "In brief" box and the downloads
    top = []
    brief = folder / "1.Presentation" / f"Brief-{name}.qmd"
    if brief.exists():
        byaml, _ = split_front_matter(brief.read_text(encoding="utf-8-sig").replace("\r\n", "\n"))
        babs = yaml_value(byaml, "abstract")
        if babs:
            top.append(f"::: {{.callout-note appearance=\"simple\" icon=false}}\n## In brief\n\n{babs}\n:::\n")
    downloads = [(label, f) for label, f in (("Working paper (Word)", f"{name}.docx"),
                                              ("Policy brief (Word)", f"Brief-{name}.docx"),
                                              ("Slides (PowerPoint)", f"Slides-{name}.pptx"))
                 if (ARCHIVE / f).exists()]
    if downloads:
        top.append("**Download:** " + " · ".join(f"[{l}](../../../papers/{f})" for l, f in downloads) + "\n")

    (dest / "index.qmd").write_text(f"---\n{yaml}---\n\n" + "\n".join(top) + "\n" + body.lstrip("\n"),
                                    encoding="utf-8")
    print(f"web page  {dest / 'index.qmd'}")


def main():
    # clear web copies of papers no longer listed, so retired pages do not linger
    listed = {paper_name(Path(f)) for f in WEB_PAPERS}
    for part in PARTS:
        for sec in part["sections"]:
            sd = SITE / part["dir"] / sec[1]
            if sd.is_dir():
                for d in sd.iterdir():
                    if d.is_dir() and d.name not in listed:
                        shutil.rmtree(d)
    books = {book_name(f) for f in WEB_BOOKS}
    for part in PARTS:
        bd = SITE / part["dir"] / "books"
        if bd.is_dir():
            for d in bd.iterdir():
                if d.is_dir() and d.name not in books:
                    shutil.rmtree(d)
    for folder_name in WEB_PAPERS:
        build(folder_name)
    for folder_name, cfg in WEB_BOOKS.items():
        build_book(folder_name, cfg)


if __name__ == "__main__":
    main()
