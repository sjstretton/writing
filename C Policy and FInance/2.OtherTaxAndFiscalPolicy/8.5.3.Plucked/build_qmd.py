"""Build Plucked.qmd (the Quarto master) from the 2020 R Markdown chapters.

Run from the book folder:  python3 2.Source/build_qmd.py
Converts knitr include_graphics chunks to Markdown images, replaces the one
ggplot chunk (UK net debt) with a PNG drawn by matplotlib, strips per-chapter
YAML, and concatenates chapters 01-14 under one header.
"""
import re, glob, csv, os
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt

here = "2.Source/Chapters-Rmd"
# figure for the one computational chunk
rows = list(csv.reader(open("2.Source/Model/Data/netdebttogdp_uk.csv")))
x = [int(r[0]) for r in rows[1:] if r[0].isdigit() and int(r[0]) >= 1900]
y = [float(r[1]) for r in rows[1:] if r[0].isdigit() and int(r[0]) >= 1900]
plt.figure(figsize=(7, 3.5)); plt.plot(x, y, color="#1F4E79"); plt.ylabel("Public net debt, % of GDP")
plt.tight_layout(); plt.savefig("ChapterPictures/1-2-UKNationalDebt.png", dpi=200); plt.close()

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

*Book manuscript, 2020, converted from R Markdown to Quarto in October 2026 without changes to the text. Retitled in October 2026; the 2020 title was 'Screwed?! Getting our future back with tax and benefit reform'. Original chapter files are in `2.Source/Chapters-Rmd`; the 2020 PDF is in `8.PreviousVersions`.*

'''
parts = [convert(open(f).read()) for f in sorted(glob.glob(f"{here}/[01]*.Rmd"))]
open("Plucked.qmd", "w").write(head + "\n\n".join(parts))
print("wrote Plucked.qmd", sum(len(p.split()) for p in parts), "words")
