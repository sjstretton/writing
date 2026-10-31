"""Build the website's research pages from the papers themselves, so the site is never out of date.

For each part in site_config.PARTS (Policy and Finance; Modelling and Analytics) this writes, in E Website:
    the part's home page (index.qmd, modelling/index.qmd)  a short intro and, per section, a line and its papers
    <part>/<n>-<slug>.qmd     one page per section: the overview abstract, then each paper's title, subtitle,
                              abstract (the policy brief's where there is one) and links: the brief and the
                              working paper online, the slides, then the Word files
    the part's sidebar in _quarto.yml (between its BEGIN/END markers): sections; under each, the papers that
                              have a web version (the policy brief's page); under each paper, its working paper;
                              under Books and other papers, each web book and its chapters
policy/more.qmd (Books and other papers) is hand-written and left alone.

Then it fills papers/ with exactly the files the site's pages link to, copied from PaperArchive/ (filled by
publish_series.py). papers/ is uploaded; PaperArchive/ is not. A linked file missing from the archive is reported.

Titles, subtitles and abstracts are read from each paper's master .qmd. Old addresses (research/...) are kept
working with redirects (Quarto 'aliases').
Compile-Website.bat runs this after publish_series.py and build_web_papers.py and before quarto render.
"""
import re
import shutil
from site_config import (PARTS, SITE, ARCHIVE, PAPERS, WEB_BOOKS, paper_folders, paper_name, master_qmd, section_folder,
                         web_page, book_dir, book_name)


def front_matter(qmd):
    text = qmd.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    meta, lines, i = {}, m.group(1).split("\n"), 0
    while i < len(lines):
        line = lines[i]
        km = re.match(r"^(title|subtitle|abstract):\s*(.*)$", line)
        if km:
            key, val = km.group(1), km.group(2).strip()
            if val in ("|", ">", "|-", ">-"):
                block = []
                i += 1
                while i < len(lines) and (lines[i].startswith("  ") or not lines[i].strip()):
                    block.append(lines[i].strip())
                    i += 1
                meta[key] = " ".join(b for b in block if b)
                continue
            meta[key] = val.strip('"').strip("'")
        i += 1
    return meta


def up(page):
    """Relative prefix from a site-relative page back to the site root."""
    return "../" * page.count("/")


def link(label, fname, page):
    """A link to a file in papers/, its file type in brackets in the link text: 'Slides (pptx) →'."""
    ext = fname.rsplit(".", 1)[-1].lower()
    return f"[{label} ({ext}) →]({up(page)}papers/{fname})" if (ARCHIVE / fname).exists() else None


def section_page(part, sec):
    folder_name, slug, name, line, overview, deck = sec
    folder = section_folder(part, sec)
    num = folder_name.split(".")[0]
    page = f"{part['dir']}/{slug}.qmd"
    ov = next(iter(sorted((folder / f"{num}.0.Overview").glob("*.qmd"))), None) if folder.is_dir() else None
    ovm = front_matter(ov) if ov else {}
    out = [f"---\ntitle: \"{num}. {name}\"\naliases:\n  - ../research/{slug}.html\n---\n"]
    if ovm.get("abstract"):
        out.append(ovm["abstract"] + "\n")
    links = [l for l in (link("Section overview", overview, page), link("Series slides", deck, page) if deck else None) if l]
    if links:
        out.append(" · ".join(links) + "\n")
    titles = []
    for pf in paper_folders(part, sec):
        q = master_qmd(pf)
        if not q:
            continue
        meta = front_matter(q)
        pnum = ".".join(pf.name.split(".")[:2])
        stem = q.stem
        brief = pf / "1.Presentation" / f"Brief-{stem}.qmd"
        bmeta = front_matter(brief) if brief.exists() else {}
        title = meta.get("title", stem)
        anchor = f"paper-{pnum.replace('.', '-')}"
        web = web_page(part, sec, stem)
        has_web = (SITE / web).exists()
        wp_web = web.replace("index.qmd", "working-paper.qmd")
        has_wp_web = (SITE / wp_web).exists()
        out.append(f"## {pnum} {title} {{#{anchor}}}\n")
        if meta.get("subtitle"):
            out.append(f"*{meta['subtitle']}*\n")
        abstract = bmeta.get("abstract") or meta.get("abstract")
        if abstract:
            out.append(abstract + "\n")
        if has_wp_web:
            online = [f"[Policy brief →]({slug}/{stem}/index.qmd)", f"[Working paper →]({slug}/{stem}/working-paper.qmd)"]
        elif has_web:
            online = [f"[Read online →]({slug}/{stem}/index.qmd)"]
        else:
            online = []
        words = [l for l in (link("Policy brief", f"Brief-{stem}.docx", page),
                             link("Working paper", f"{stem}.docx", page)) if l]
        ls = online + [l for l in (link("Slides", f"Slides-{stem}.pptx", page),) if l]
        if words:
            ls += words
        if ls:
            out.append(" · ".join(ls) + "\n")
        titles.append((pnum, title.split(":")[0].strip(), anchor, web if has_web else None,
                       wp_web if has_wp_web else None))
    (SITE / part["dir"]).mkdir(exist_ok=True)
    (SITE / page).write_text("\n".join(out), encoding="utf-8")
    return titles


def home_page(part, index):
    page = part["home"]
    pre = up(page)
    aliases = "aliases:\n  - research.html\n" if page == "index.qmd" else ""
    out = [f"---\ntitle: \"{part['title']}\"\n{aliases}---\n", part["intro"] + "\n"]
    for sec, titles in index:
        num = sec[0].split(".")[0]
        sp = f"{pre}{part['dir']}/{sec[1]}.qmd"
        out.append(f"### [{num}. {sec[2]}]({sp})\n")
        out.append(sec[3] + "\n")
        if titles:
            out.append("\n".join(f"- [{p} {t}]({pre + w if w else f'{sp}#{a}'})" for p, t, a, w, _ in titles) + "\n")
    if part["more"]:
        out.append(f"### [Books and other papers]({pre}{part['more']})\n")
        out.append("Three books: *Time and Chance*, *The Right Policy at the Wrong Time* and the tax book *Plucked!*; "
                   "and an earlier paper on sustainability-linked intermediated debt.\n")
    (SITE / page).parent.mkdir(exist_ok=True)
    (SITE / page).write_text("\n".join(out), encoding="utf-8")


def yq(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


def web_books(part):
    """(title, contents page, [(chapter label, page)]) for each web book of this part (build_web_papers.py made them)."""
    out = []
    for folder_name, cfg in WEB_BOOKS.items():
        if cfg["part"] != part["key"]:
            continue
        d = book_dir(part, book_name(folder_name))
        if not (SITE / d / "index.qmd").exists():
            continue
        chapters = []
        for q in sorted((SITE / d).glob("[0-9][0-9]-*.qmd")):
            m = re.match(r"Chapter (\d+): (.*)", front_matter(q).get("title", q.stem))
            chapters.append((f"{m.group(1)}. {m.group(2)}" if m else q.stem, f"{d}/{q.name}"))
        out.append((front_matter(SITE / d / "index.qmd").get("title", book_name(folder_name)), f"{d}/index.qmd", chapters))
    return out


def write_sidebar(part, index):
    """Rewrite this part's sidebar between its BEGIN/END markers in _quarto.yml: each section, and under it
    the papers that have a web version, so the sidebar works like a book's table of contents."""
    ind = " " * 8
    lines = [f"{ind}- text: {yq(part['title'])}", f"{ind}  href: {part['home']}"]
    for sec, titles in index:
        num = sec[0].split(".")[0]
        sp = f"{part['dir']}/{sec[1]}.qmd"
        web = [(p, t, w, wpw) for p, t, a, w, wpw in titles if w]
        if web:
            lines += [f"{ind}- section: {yq(f'{num}. {sec[2]}')}", f"{ind}  href: {sp}", f"{ind}  contents:"]
            for p, t, w, wpw in web:
                if wpw:
                    lines += [f"{ind}    - section: {yq(f'{p} {t}')}", f"{ind}      href: {w}",
                              f"{ind}      contents:",
                              f"{ind}        - text: \"Working paper\"", f"{ind}          href: {wpw}"]
                else:
                    lines += [f"{ind}    - text: {yq(f'{p} {t}')}", f"{ind}      href: {w}"]
        else:
            lines.append(f"{ind}- {sp}")
    if part["more"]:
        books = web_books(part)
        if books:
            lines += [f"{ind}- section: {yq(front_matter(SITE / part['more']).get('title', 'Books'))}",
                      f"{ind}  href: {part['more']}", f"{ind}  contents:"]
            for title, home, chapters in books:
                lines += [f"{ind}    - section: {yq(title)}", f"{ind}      href: {home}", f"{ind}      contents:"]
                for ct, cp in chapters:
                    lines += [f"{ind}        - text: {yq(ct)}", f"{ind}          href: {cp}"]
        else:
            lines.append(f"{ind}- {part['more']}")
    cfg = SITE / "_quarto.yml"
    text = cfg.read_text(encoding="utf-8")
    b = text.index(f"# BEGIN {part['key']} sidebar")
    b = text.index("\n", b) + 1
    e = text.index(f"{ind}# END {part['key']} sidebar")
    cfg.write_text(text[:b] + "\n".join(lines) + "\n" + text[e:], encoding="utf-8")


def sync_papers():
    """papers/ = exactly the files the pages link to, copied from PaperArchive/."""
    wanted = set()
    for q in SITE.rglob("*.qmd"):
        if any(x in q.parts for x in ("_site", "PaperArchive", ".quarto")):
            continue
        wanted |= set(re.findall(r"papers/([^)\s#]+)\)", q.read_text(encoding="utf-8")))
    PAPERS.mkdir(exist_ok=True)
    for f in PAPERS.iterdir():
        if f.is_file() and f.name not in wanted:
            f.unlink()
    for name in sorted(wanted):
        src = ARCHIVE / name
        if src.exists():
            shutil.copy2(src, PAPERS / name)
        else:
            print(f"LINKED BUT MISSING from PaperArchive: {name}")
    print(f"papers/ holds the {len(list(PAPERS.iterdir()))} linked files")


def main():
    for part in PARTS:
        index = [(sec, section_page(part, sec)) for sec in part["sections"]]
        home_page(part, index)
        write_sidebar(part, index)
    sync_papers()
    print("wrote", sum(len(p["sections"]) for p in PARTS), "section pages, the home pages and the sidebars")


if __name__ == "__main__":
    main()
