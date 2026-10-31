"""Make a Climate Fiscal Policy Brief deck (about ten slides) from a JSON spec, with python-pptx.

Usage:  python make_deck.py <paper folder>/1.Presentation/slides.json <out.pptx>
        (paths to images in the spec are relative to the spec file)

The spec holds the series line, the deck title and a list of slides. Every slide's "title" is its message: a full
sentence a reader could stop at. Slide types:

  {"type": "title",   "title", "subtitle", "message", "author"}                 dark: the one-line finding
  {"type": "stats",   "title", "stats": [{"value", "label"}], "text", "source"}  two to four big numbers
  {"type": "points",  "title", "points": [{"lead", "text"}], "source"}          up to five claims, lead in bold
  {"type": "figure",  "title", "image", "caption", "points": [...], "source"}   a figure, with up to three points
  {"type": "table",   "title", "header": [...], "rows": [[...]], "note", "source"}
  {"type": "closing", "title", "left": {"title", "items"}, "right": {"title", "items"}}   dark: results and actions

Any slide may carry "notes" (speaker notes). Light slides carry the series line and the slide number.
This replaces make_deck.js (four slides, needed pptxgenjs); the theme is the same.
"""
import json
import re
import sys
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt

HEAD, BODY = "Cambria", "Calibri"
DARK = RGBColor(0x1E, 0x3A, 0x2B)      # dk2: dark green
INK = RGBColor(0x1B, 0x1B, 0x1B)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
PALE = RGBColor(0xEE, 0xF3, 0xEE)      # lt2
GREEN = RGBColor(0x2E, 0x7D, 0x32)     # accent1
BLUE = RGBColor(0x1F, 0x4E, 0x79)      # accent2
LEAF = RGBColor(0x97, 0xBC, 0x62)      # accent3
GREY = RGBColor(0x6B, 0x7B, 0x6E)      # accent5
W, H = 10.0, 5.625


def box(slide, x, y, w, h, fill=None):
    s = slide.shapes.add_shape(1, Inches(x), Inches(y), Inches(w), Inches(h))
    s.line.fill.background()
    if fill is None:
        s.fill.background()
    else:
        s.fill.solid()
        s.fill.fore_color.rgb = fill
    s.shadow.inherit = False
    return s


def text(slide, x, y, w, h, runs, size=14, color=INK, font=BODY, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
         space=6):
    """runs: a string, or a list of paragraphs; each paragraph a string or a list of (text, bold) pairs."""
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.05)
    tf.margin_top = tf.margin_bottom = Inches(0.03)
    paras = runs if isinstance(runs, list) else [runs]
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_after = Pt(space)
        for t, bold in ([(para, False)] if isinstance(para, str) else para):
            r = p.add_run()
            r.text = t
            r.font.size = Pt(size)
            r.font.bold = bold
            r.font.color.rgb = color
            r.font.name = font
    return tb


def light(prs, spec, n, title):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    box(s, 0, 0, W, 0.09, GREEN)
    text(s, 0.45, 0.25, 9.1, 0.95, title, size=22, color=DARK, font=HEAD, anchor=MSO_ANCHOR.MIDDLE)
    text(s, 0.45, 5.22, 7.5, 0.3, spec["series"], size=9, color=GREY)
    text(s, 8.6, 5.22, 0.95, 0.3, str(n), size=9, color=GREY, align=PP_ALIGN.RIGHT)
    return s


def dark(prs, spec):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    box(s, 0, 0, W, H, DARK)
    text(s, 0.5, 5.15, 9, 0.3, spec["series"], size=10, color=LEAF)
    return s


def source(s, src):
    if src:
        text(s, 0.45, 4.92, 9.1, 0.3, "Source: " + src, size=8.5, color=GREY)


def notes(s, d):
    if d.get("notes"):
        s.notes_slide.notes_text_frame.text = d["notes"]


def lead_paras(points, size):
    return [[(p["lead"] + " ", True), (p.get("text", ""), False)] if isinstance(p, dict) else p for p in points]


def make(spec_path, out):
    spec = json.loads(Path(spec_path).read_text(encoding="utf-8"))
    base = Path(spec_path).parent
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(W), Inches(H)
    prs.core_properties.author = "Stephen J. Stretton"
    prs.core_properties.title = spec["title"]

    for n, d in enumerate(spec["slides"], 1):
        t = d["type"]
        if t == "title":
            s = dark(prs, spec)
            text(s, 0.6, 0.55, 8.8, 1.4, d["title"], size=34, color=WHITE, font=HEAD, anchor=MSO_ANCHOR.BOTTOM)
            text(s, 0.6, 1.98, 8.8, 0.5, d.get("subtitle", ""), size=16, color=LEAF)
            box(s, 0.6, 2.62, 1.2, 0.05, LEAF)
            text(s, 0.6, 2.8, 8.6, 1.5, d.get("message", ""), size=15, color=WHITE)
            text(s, 0.6, 4.55, 8.8, 0.4, d.get("author", ""), size=11, color=PALE)
        elif t == "stats":
            s = light(prs, spec, n, d["title"])
            stats = d["stats"]
            cw = 9.1 / len(stats)
            for i, st in enumerate(stats):
                x = 0.45 + i * cw
                box(s, x + 0.05, 1.35, cw - 0.2, 1.85, PALE)
                text(s, x + 0.15, 1.45, cw - 0.4, 0.8, st["value"], size=32, color=GREEN, font=HEAD,
                     anchor=MSO_ANCHOR.MIDDLE)
                text(s, x + 0.15, 2.25, cw - 0.4, 0.95, st["label"], size=11.5, color=INK)
            if d.get("text"):
                text(s, 0.45, 3.4, 9.1, 1.4, d["text"], size=14)
            source(s, d.get("source"))
        elif t == "points":
            s = light(prs, spec, n, d["title"])
            pts = d["points"]
            size = {1: 20, 2: 19, 3: 18, 4: 16.5}.get(len(pts), 15)
            text(s, 0.55, 1.4, 8.9, 3.45, lead_paras(pts, size), size=size, space=16)
            source(s, d.get("source"))
        elif t == "figure":
            s = light(prs, spec, n, d["title"])
            pts = d.get("points", [])
            fw = 5.9 if pts else 9.1
            img = base / d["image"]
            pic = s.shapes.add_picture(str(img), Inches(0.45), Inches(1.3), width=Inches(fw))
            maxh = Inches(3.25 if d.get("caption") else 3.55)
            if pic.height > maxh:                               # keep the picture inside the frame
                ratio = maxh / pic.height
                pic.height, pic.width = int(pic.height * ratio), int(pic.width * ratio)
            if d.get("caption"):
                text(s, 0.45, 1.3 + pic.height / 914400 + 0.05, fw, 0.5, d["caption"], size=9.5, color=GREY)
            if pts:
                text(s, 6.6, 1.35, 2.95, 3.5, lead_paras(pts, 12.5), size=12.5, space=10)
            source(s, d.get("source"))
        elif t == "table":
            s = light(prs, spec, n, d["title"])
            rows = [d["header"]] + d["rows"]
            nrow, ncol = len(rows), len(d["header"])
            rh = min(0.42, 3.2 / nrow)
            tbl = s.shapes.add_table(nrow, ncol, Inches(0.55), Inches(1.35), Inches(8.9), Inches(rh * nrow)).table
            widths = d.get("widths") or [8.9 / ncol] * ncol
            for j, wj in enumerate(widths):
                tbl.columns[j].width = Inches(wj)
            for i, row in enumerate(rows):
                for j, val in enumerate(row):
                    c = tbl.cell(i, j)
                    c.fill.solid()
                    c.fill.fore_color.rgb = BLUE if i == 0 else (PALE if i % 2 == 0 else WHITE)
                    tf = c.text_frame
                    tf.paragraphs[0].text = ""
                    r = tf.paragraphs[0].add_run()
                    r.text = str(val)
                    r.font.size = Pt(12 if i else 11.5)
                    r.font.bold = i == 0 or j == 0
                    r.font.name = BODY
                    r.font.color.rgb = WHITE if i == 0 else INK
                    numeric = j > 0 and re.fullmatch(r"[-+−~$€£]?[\d.,]+\s*[%×x]?|[-+−]?\$?[\d.,]+[–-][\d.,]+%?", str(val).strip()) is not None
                    tf.paragraphs[0].alignment = PP_ALIGN.RIGHT if numeric else PP_ALIGN.LEFT
                    c.margin_top = c.margin_bottom = Inches(0.03)
            if d.get("note"):
                text(s, 0.55, 1.45 + rh * nrow, 8.9, 0.9, d["note"], size=12)
            source(s, d.get("source"))
        elif t == "closing":
            s = dark(prs, spec)
            text(s, 0.6, 0.3, 8.8, 0.8, d["title"], size=24, color=WHITE, font=HEAD, anchor=MSO_ANCHOR.MIDDLE)
            for k, (x, col) in enumerate(((0.6, d["left"]), (5.15, d["right"]))):
                text(s, x, 1.25, 4.25, 0.4, col["title"], size=14, color=LEAF, font=HEAD)
                text(s, x, 1.7, 4.25, 3.3, lead_paras(col["items"], 12.5), size=12.5, color=WHITE, space=9)
        else:
            raise SystemExit(f"unknown slide type {t}")
        notes(s, d)

    prs.save(out)
    print(f"wrote {out}: {len(spec['slides'])} slides")


if __name__ == "__main__":
    make(sys.argv[1], sys.argv[2])
