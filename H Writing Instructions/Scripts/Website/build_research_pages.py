"""Build the website's research pages from the papers themselves, so the site is never out of date.

For each part in site_config.PARTS (Policy and Finance; Modelling and Analytics) this writes, in E Website:
    the part's home page (policy/index.qmd, modelling/index.qmd)  a short intro and, per section, a line and its papers
    <part>/<n>-<slug>.qmd     one page per section: the overview abstract, then each paper's title, subtitle,
                              abstract (the policy brief's where there is one) and links: the brief and the
                              working paper online, then the PDFs of the slides, brief and working paper
    the part's sidebar in _quarto.yml (between its BEGIN/END markers): sections; under each, the papers that
                              have a web version (the policy brief's page); under each paper, its working paper;
                              then the section's books and earlier papers (site_config.SECTION_EXTRAS), a web book
                              with its chapters
Books and earlier papers are listed at the end of their section's page; there is no separate Books page.
The site links PDFs only (render_pdfs.py makes them).

Then it fills papers/ with exactly the files the site's pages link to, copied from PaperArchive/ (filled by
publish_series.py). papers/ is uploaded; PaperArchive/ is not. A linked file missing from the archive is reported.

Titles, subtitles and abstracts are read from each paper's master .qmd. Old addresses (research/...) are kept
working with redirects (Quarto 'aliases').
Compile-Website.bat runs this after publish_series.py and build_web_papers.py and before quarto render.
"""
import re
import shutil
from site_config import (PARTS, SITE, ARCHIVE, PAPERS, WEB_BOOKS, SECTION_EXTRAS, paper_folders, paper_name, master_qmd, section_folder,
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
    pdf = lambda f: f.rsplit(".", 1)[0] + ".pdf"   # the site links PDFs only
    links = [l for l in (link("Section overview", pdf(overview), page), link("Series slides", pdf(deck), page) if deck else None) if l]
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
        words = [l for l in (link("Policy brief", f"Brief-{stem}.pdf", page),
                             link("Working paper", f"{stem}.pdf", page)) if l]
        ls = online + [l for l in (link("Slides", f"Slides-{stem}.pdf", page),) if l]
        if words:
            ls += words
        if ls:
            out.append(" · ".join(ls) + "\n")
        titles.append((pnum, title.split(":")[0].strip(), anchor, web if has_web else None,
                       wp_web if has_wp_web else None))
    extras = []
    for x in SECTION_EXTRAS.get(folder_name, []):
        anchor = "extra-" + re.sub(r"[^a-z0-9]+", "-", x["title"].lower()).strip("-")
        out.append(f"## {x['title']} {{#{anchor}}}\n")
        sub = " · ".join(t for t in (x["kind"], x.get("subtitle"), x.get("by")) if t)
        out.append(f"*{sub}*\n")
        out.append(x["text"] + "\n")
        web = None
        if x.get("web"):
            d = book_dir(part, book_name(x["web"]))
            if (SITE / d / "index.qmd").exists():
                web = f"{d}/index.qmd"
        ls = [l for l in ((f"[Read online →]({up(page)}{web})" if web else None),
                          link(x["kind"], x["pdf"], page)) if l]
        if ls:
            out.append(" · ".join(ls) + "\n")
        extras.append((x["title"], anchor, web, x["kind"]))
    (SITE / part["dir"]).mkdir(exist_ok=True)
    (SITE / page).write_text("\n".join(out), encoding="utf-8")
    return titles, extras


def home_page(part, index):
    page = part["home"]
    pre = up(page)
    # old addresses of the Policy and Finance home (it was the site's index.html until 1 Nov 2026)
    aliases = ("aliases:\n  - ../research.html\n  - more.html\n  - ../research/more.html\n"
               if page == "policy/index.qmd" else "")
    out = [f"---\ntitle: \"{part['title']}\"\n{aliases}---\n", part["intro"] + "\n"]
    for sec, (titles, extras) in index:
        num = sec[0].split(".")[0]
        sp = f"{pre}{part['dir']}/{sec[1]}.qmd"
        out.append(f"### [{num}. {sec[2]}]({sp})\n")
        out.append(sec[3] + "\n")
        items = [f"- [{p} {t}]({pre + w if w else f'{sp}#{a}'})" for p, t, a, w, _ in titles]
        items += [f"- [{t}]({pre + w if w else f'{sp}#{a}'}) ({k.lower()})" for t, a, w, k in extras]
        if items:
            out.append("\n".join(items) + "\n")
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
    the papers that have a web version, then the section's books (a book read on the site with its chapters),
    so the sidebar works like a book's table of contents."""
    ind = " " * 8
    lines = [f"{ind}- text: {yq(part['title'])}", f"{ind}  href: {part['home']}"]
    books = {home: chapters for _, home, chapters in web_books(part)}
    for sec, (titles, extras) in index:
        num = sec[0].split(".")[0]
        sp = f"{part['dir']}/{sec[1]}.qmd"
        web = [(p, t, w, wpw) for p, t, a, w, wpw in titles if w]
        if web or extras:
            lines += [f"{ind}- section: {yq(f'{num}. {sec[2]}')}", f"{ind}  href: {sp}", f"{ind}  contents:"]
            for p, t, w, wpw in web:
                if wpw:
                    lines += [f"{ind}    - section: {yq(f'{p} {t}')}", f"{ind}      href: {w}",
                              f"{ind}      contents:",
                              f"{ind}        - text: \"Working paper\"", f"{ind}          href: {wpw}"]
                else:
                    lines += [f"{ind}    - text: {yq(f'{p} {t}')}", f"{ind}      href: {w}"]
            for t, a, w, k in extras:
                if w and books.get(w):
                    lines += [f"{ind}    - section: {yq(t)}", f"{ind}      href: {w}", f"{ind}      contents:"]
                    for ct, cp in books[w]:
                        lines += [f"{ind}        - text: {yq(ct)}", f"{ind}          href: {cp}"]
                else:
                    lines += [f"{ind}    - text: {yq(t)}", f"{ind}      href: {w or sp + '#' + a}"]
        else:
            lines.append(f"{ind}- {sp}")
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
