"""Make the web versions of each paper from its two masters, so the site shows the papers themselves.

A paper in WEB_PAPERS has two forms, each with its own master in the paper folder:
    the policy brief     1.Presentation/Brief-<PaperName>.qmd   short, plain, for a busy official
    the working paper    <PaperName>.qmd                       the full academic paper
They are separate drafts; neither is made from the other.

For each paper this writes, in E Website/<part>/<section-slug>/<PaperName>/:
    index.qmd            the policy brief: the paper's page on the site, higher in the hierarchy
    working-paper.qmd    the working paper, one level below (linked from the brief and the sidebar)
    the .bib files and every figure each master uses, at the same relative paths
A paper with no brief gets only index.qmd, made from the working paper.

The masters stay where they are and are the only files to edit. The web copies are NOT masters: they are deleted
and rewritten on every compile, and their first line says so.

What changes in the copies:
    - format: docx is dropped (the site's own html format applies), and web settings are added
      (contents sidebar, hover citations and cross-references, figure lightbox);
    - csl: points at the site's local copy of the Chicago style, so the build needs no internet;
    - under the first heading (the executive summary): links to the other form and to the slides;
    - at the end of the text, before the references: the Word downloads;
    - cross-links written in the masters as short targets become real links:
          [text](wp:)            the working paper          [text](wp:sec-crediting)    a section of it
          [text](brief:)         the policy brief           [text](brief:sec-what-to-do) a section of it
          [text](paper:1.2)      another paper's page (or its entry on the section page if it has none)
      In the Word versions these show as plain text (Scripts/Website/web-links.lua, used when rendering).

Compile-Website.bat runs this after publish_series.py and before build_research_pages.py.
To put another paper on the web, add its folder to WEB_PAPERS in site_config.py.
"""
import re
import shutil
from pathlib import Path
from site_config import REPO, PARTS, SITE, ARCHIVE, WEB_PAPERS, part_of_section, paper_name, master_qmd, \
    paper_folders

WEB_SETTINGS = ("toc: true\ndate-format: \"MMMM YYYY\"\ncitations-hover: true\ncrossrefs-hover: true\n"
                "lightbox: auto\n")


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


def paper_page(num, depth):
    """Relative link from a paper page `depth` folders below the site root to paper `num` (e.g. '1.2')."""
    up = "../" * depth
    part, sec = part_of_section(num.split(".")[0])
    if not part:
        return None
    for pf in paper_folders(part, sec):
        if ".".join(pf.name.split(".")[:2]) == num:
            name = paper_name(pf)
            if (SITE / part["dir"] / sec[1] / name / "index.qmd").exists() or pf.name in WEB_PAPERS:
                return f"{up}{part['dir']}/{sec[1]}/{name}/index.qmd"
            return f"{up}{part['dir']}/{sec[1]}.qmd#paper-{num.replace('.', '-')}"
    return None


def web_links(body, has_brief):
    """Turn the masters' short link targets into links between the two pages and to other papers."""
    wp_file = "working-paper.qmd" if has_brief else "index.qmd"

    def sub(m):
        kind, target = m.group(1), m.group(2)
        if kind == "wp":
            return f"]({wp_file}{'#' + target if target else ''})"
        if kind == "brief":
            if not has_brief:
                return "]()"
            return f"](index.qmd{'#' + target if target else ''})"
        link = paper_page(target, 3)
        return f"]({link})" if link else "]()"

    body = re.sub(r"\]\((wp|brief|paper):([\w.-]*)\)", sub, body)
    return re.sub(r"\[([^\]]*)\]\(\)", r"\1", body)      # a link with nowhere to go becomes plain text


def copy_assets(base, body, yaml, dest):
    """Copy every local figure the body uses, and the bibliography, keeping relative paths."""
    for rel in sorted(set(re.findall(r"\]\(([^)\s]+?\.(?:png|jpe?g|svg|gif))\)", body, re.I))):
        src = base / rel
        if src.exists():
            (dest / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest / rel)
        else:
            print(f"missing figure {src}")
    bib = yaml_value(yaml, "bibliography")
    if bib and (base / bib).exists():
        shutil.copy2(base / bib, dest / bib)


def web_yaml(yaml, master):
    yaml = re.sub(r"^#.*\n?", "", yaml, flags=re.M)          # drop the master's own comment lines
    yaml = drop_key(yaml, "format")
    yaml = re.sub(r"^csl:.*$", "csl: ../../../chicago-author-date.csl", yaml, flags=re.M)
    rel_master = master.relative_to(REPO).as_posix()
    header = (f"# GENERATED - NOT THE MASTER. Made from {rel_master} by build_web_papers.py\n"
              f"# on every compile; edits here are lost. Edit the master instead.\n")
    return header + yaml.rstrip("\n") + "\n" + WEB_SETTINGS


def insert_under_first_heading(body, text):
    m = re.search(r"^# .*\n", body, re.M)
    if not m:
        return text + "\n\n" + body
    return body[:m.end()] + "\n" + text + "\n" + body[m.end():]


def insert_before_references(body, text):
    m = re.search(r"^# References.*\n", body, re.M)
    if not m:
        return body.rstrip("\n") + "\n\n" + text + "\n"
    return body[:m.start()] + text + "\n" + body[m.start():]


def write_page(master, dest_file, near_top, downloads, has_brief):
    text = master.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    yaml, body = split_front_matter(text)
    copy_assets(master.parent, body, yaml, dest_file.parent)
    body = web_links(body, has_brief)
    if near_top:
        body = insert_under_first_heading(body, near_top)
    if downloads:
        body = insert_before_references(body, downloads)
    dest_file.write_text(f"---\n{web_yaml(yaml, master)}---\n\n" + body.lstrip("\n"), encoding="utf-8")
    print(f"web page  {dest_file}")


def build(folder_name):
    folder = find(folder_name)
    if not folder:
        print(f"missing   {folder_name}")
        return
    part, sec = part_of_section(folder_name.split(".")[0])
    name = paper_name(folder)
    wp = master_qmd(folder)
    brief = folder / "1.Presentation" / f"Brief-{name}.qmd"
    has_brief = brief.exists()

    dest = SITE / part["dir"] / sec[1] / name
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)

    def dl(label, f):
        return f"[{label}](../../../papers/{f})" if (ARCHIVE / f).exists() else None

    slides = dl("Slides (PowerPoint)", f"Slides-{name}.pptx")
    words = [l for l in (dl("Policy brief (Word)", f"Brief-{name}.docx"),
                         dl("Working paper (Word)", f"{name}.docx")) if l]
    downloads = ("# Downloads {.unnumbered}\n\n" + " · ".join(words) + "\n") if words else None

    if has_brief:
        to_wp = "[**Read the full working paper →**](working-paper.qmd)"
        write_page(brief, dest / "index.qmd", " · ".join(l for l in (to_wp, slides) if l) + "\n",
                   downloads, True)
        to_brief = "[**Policy brief (short version) →**](index.qmd)"
        write_page(wp, dest / "working-paper.qmd", " · ".join(l for l in (to_brief, slides) if l) + "\n",
                   downloads, True)
    else:
        write_page(wp, dest / "index.qmd", (slides + "\n") if slides else None, downloads, False)


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
