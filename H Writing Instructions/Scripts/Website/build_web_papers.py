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

Compile-Website.bat runs this after publish_series.py and before build_research_pages.py.
To put another paper on the web, add its folder to WEB_PAPERS in site_config.py.
"""
import re
import shutil
from pathlib import Path
from site_config import REPO, PARTS, SITE, ARCHIVE, WEB_PAPERS, part_of_section, paper_name, master_qmd


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

    # figures: copy every local image the body refers to, keeping its relative path
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

    yaml = re.sub(r"^#.*\n?", "", yaml, flags=re.M)          # drop the master's own comment lines
    yaml = drop_key(yaml, "format")
    yaml = re.sub(r"^csl:.*$", "csl: ../../../chicago-author-date.csl", yaml, flags=re.M)
    rel_master = master.relative_to(REPO).as_posix()
    header = (f"# GENERATED - NOT THE MASTER. Made from {rel_master} by build_web_papers.py\n"
              f"# on every compile; edits here are lost. Edit the master instead.\n")
    yaml = header + yaml.rstrip("\n") + "\ntoc: true\ndate-format: \"MMMM YYYY\"\n"

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
    for folder_name in WEB_PAPERS:
        build(folder_name)


if __name__ == "__main__":
    main()
