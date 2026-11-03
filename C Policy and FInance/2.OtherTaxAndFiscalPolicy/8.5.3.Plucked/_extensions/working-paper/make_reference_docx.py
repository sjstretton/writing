"""Rebuild reference.docx, the Word styles for the working-paper format (pandoc copies its styles,
page set-up and footer into every .docx it writes). Run from this folder:
    quarto pandoc -o reference.docx --print-default-data-file reference.docx
    python make_reference_docx.py
Word cannot rely on the PDF's web fonts, so it uses Cambria (text) and Calibri (headings), which come with Office."""
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BLUE = RGBColor(0x1A, 0x54, 0x90)
GREY = RGBColor(0x5F, 0x6B, 0x7A)
SERIF, SANS = "Cambria", "Calibri"

d = Document("reference.docx")
st = d.styles


def font(name, face=None, size=None, bold=None, italic=None, color=None, before=None, after=None,
         align=None, line=None):
    try:
        s = st[name]
    except KeyError:
        return
    f = s.font
    if face:
        f.name = face
        rpr = s.element.get_or_add_rPr()
        rf = rpr.find(qn("w:rFonts"))
        if rf is None:
            rf = OxmlElement("w:rFonts"); rpr.append(rf)
        for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
            rf.set(qn(a), face)
        for a in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
            rf.attrib.pop(qn(a), None)
    if size: f.size = Pt(size)
    if bold is not None: f.bold = bold
    if italic is not None: f.italic = italic
    if color is not None: f.color.rgb = color
    pf = getattr(s, "paragraph_format", None)
    if pf is not None:
        if before is not None: pf.space_before = Pt(before)
        if after is not None: pf.space_after = Pt(after)
        if align is not None: pf.alignment = align
        if line is not None: pf.line_spacing = line


J = WD_ALIGN_PARAGRAPH.JUSTIFY
font("Normal", SERIF, 11, color=RGBColor(0x1F, 0x1F, 0x1F))
for n in ("Body Text", "First Paragraph"):
    font(n, SERIF, 11, before=0, after=7, align=J, line=1.15)
font("Compact", SERIF, 11, before=0, after=3, line=1.15)
font("Title", SERIF, 24, bold=True, color=RGBColor(0x11, 0x11, 0x11), before=6, after=4, align=WD_ALIGN_PARAGRAPH.LEFT)
font("Subtitle", SERIF, 14, italic=True, bold=False, color=GREY, before=0, after=12, align=WD_ALIGN_PARAGRAPH.LEFT)
font("Author", SANS, 11.5, bold=True, color=RGBColor(0x11, 0x11, 0x11), after=2, align=WD_ALIGN_PARAGRAPH.LEFT)
font("Date", SANS, 10, color=GREY, after=14, align=WD_ALIGN_PARAGRAPH.LEFT)
font("Abstract", SERIF, 10, before=4, after=6, align=J, line=1.1)
font("Abstract Title", SANS, 9.5, bold=True, color=BLUE, before=6, after=2)
for lvl, size in ((1, 14), (2, 12), (3, 11)):
    font(f"Heading {lvl}", SANS, size, bold=True, italic=False, color=BLUE,
         before=(18 if lvl == 1 else 12), after=6)
font("Heading 3", italic=True, bold=False, color=RGBColor(0x1F, 0x1F, 0x1F))
font("Heading 4", SANS, 11, bold=True, color=GREY)
for n in ("Caption", "Image Caption", "Table Caption"):
    font(n, SERIF, 9, italic=False, color=RGBColor(0x33, 0x33, 0x33), before=4, after=10)
font("Footnote Text", SERIF, 9)
font("Bibliography", SERIF, 10, after=4)
font("Hyperlink", color=BLUE)
font("Block Text", SERIF, 10.5)

# abstract: light tint and a blue rule on the left, as in the PDF
ab = st["Abstract"].element.get_or_add_pPr()
for tag, attrs in (("w:pBdr", None), ("w:shd", {"w:val": "clear", "w:color": "auto", "w:fill": "F3F6FA"}),
                   ("w:ind", {"w:left": "170", "w:right": "170"})):
    el = OxmlElement(tag)
    if tag == "w:pBdr":
        left = OxmlElement("w:left")
        for k, v in {"w:val": "single", "w:sz": "18", "w:space": "8", "w:color": "1A5490"}.items():
            left.set(qn(k), v)
        el.append(left)
    else:
        for k, v in attrs.items():
            el.set(qn(k), v)
    ab.append(el)

# Heading 1: thin rule beneath the title block is too much; keep headings clean but keep them with next
for lvl in (1, 2, 3):
    st[f"Heading {lvl}"].paragraph_format.keep_with_next = True

# A4, 2.5 cm margins, centred page number in the footer
for s in d.sections:
    s.page_width, s.page_height = Cm(21.0), Cm(29.7)
    s.left_margin = s.right_margin = Cm(2.5)
    s.top_margin, s.bottom_margin = Cm(2.6), Cm(2.4)
    p = s.footer.paragraphs[0] if s.footer.paragraphs else s.footer.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run()
    r.font.name, r.font.size, r.font.color.rgb = SANS, Pt(9), GREY
    for t, txt in (("begin", None), (None, "PAGE"), ("end", None)):
        if t:
            fc = OxmlElement("w:fldChar"); fc.set(qn("w:fldCharType"), t); r._r.append(fc)
        else:
            it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = txt; r._r.append(it)

# remove the sample text pandoc's reference doc carries (styles are what matters)
d.save("reference.docx")
print("reference.docx written")
