"""Build Plucked.qmd (the Quarto master) from the 2020 R Markdown chapters.

Run from anywhere:  python3 build_qmd.py   (paths are relative to this file's folder)
Converts knitr include_graphics chunks to Markdown images, replaces the one
ggplot chunk (UK net debt) with a PNG drawn by matplotlib, strips per-chapter
YAML, and concatenates chapters 01-14 under one header.
Without matplotlib it keeps the existing chart and says so.
"""
import re, csv
from pathlib import Path

BOOK = Path(__file__).resolve().parent          # the book folder
CHAPTERS = BOOK / "Chapters-Rmd"
DEBT_CSV = BOOK / "Model" / "Data" / "netdebttogdp_uk.csv"
DEBT_PNG = BOOK / "ChapterPictures" / "1-2-UKNationalDebt.png"
MASTER = BOOK / "Plucked.qmd"

# figure for the one computational chunk
try:
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
except ImportError:
    print(f"matplotlib not installed: kept the existing {DEBT_PNG.name}")
else:
    with open(DEBT_CSV, newline="") as fh:
        rows = list(csv.reader(fh))
    x = [int(r[0]) for r in rows[1:] if r[0].isdigit() and int(r[0]) >= 1900]
    y = [float(r[1]) for r in rows[1:] if r[0].isdigit() and int(r[0]) >= 1900]
    plt.figure(figsize=(7, 3.5)); plt.plot(x, y, color="#1F4E79"); plt.ylabel("Public net debt, % of GDP")
    plt.tight_layout(); plt.savefig(DEBT_PNG, dpi=200); plt.close()
    print(f"drew {DEBT_PNG.name}")

def convert(t):
    t = re.sub(r"\A---\n.*?\n---\n", "", t, flags=re.S)  # chapter YAML
    def chunk(m):
        opts, body = m.group(1), m.group(2)
        cap = re.search(r"fig\.cap\s*=\s*['\"](.*?)['\"]\s*(,|$)", opts)
        cap = cap.group(1) if cap else ""
        g = re.search(r"include_graphics\(['\"]([^'\"]+)['\"]", body)
        if g:
            return f"![{cap}]({g.group(1)})"
        if "netdebttogdp_uk" in body:
            return f"![{cap}](ChapterPictures/1-2-UKNationalDebt.png)"
        return ""  # setup and other non-content chunks
    t = re.sub(r"```\{r([^}]*)\}\n(.*?)```", chunk, t, flags=re.S)
    t = re.sub(r"`r [^`]*`", "", t)  # inline R
    return t.strip() + "\n"

head = '''---
title: "Plucked!"
subtitle: "A guide to a fair, simple, efficient and politically feasible tax and benefits system"
author:
  - name: "Stephen Stretton"
  - name: "Gordon Styles"
date: "2020 manuscript; Quarto edition October 2026"
version: "1.0-2020"
bibliography: Plucked.bib
csl: https://www.zotero.org/styles/chicago-author-date
toc: true
format:
  docx: default
---

*Book manuscript, 2020, converted from R Markdown to Quarto in October 2026 without changes to the text. Retitled in October 2026; the 2020 title was 'Screwed?! Getting our future back with tax and benefit reform'. Original chapter files are in `Chapters-Rmd`; the 2020 PDF is in `8.PreviousVersions`.*

'''
chapters = sorted(CHAPTERS.glob("[01]*.Rmd"))
assert chapters, f"no chapter files found in {CHAPTERS}"
parts = [convert(f.read_text(encoding="utf-8")) for f in chapters]
MASTER.write_text(head + "\n\n".join(parts), encoding="utf-8")
print(f"wrote {MASTER.name}: {len(chapters)} chapters, {sum(len(p.split()) for p in parts)} words")
