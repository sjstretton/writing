"""Build the printable tracker (Day and Week Plans/Me-Printable-Tracker.docx) from the master lists.

The root file never carries a version number, so links to it stay valid; a copy of each layout
version goes to X - Archive/Printable versions/. Normally run through Scripts/update.py build.

Changing lists come from 3-TaskContextAndProjectPlans.md, 1-Me-NextStep.txt,
2-Me-DayWeekPlan.txt and Context/3-Me-WeeklyLog.md; the fixed routines from Context/routines.md.
Every task and milestone shows its points. Tick boxes are Word check-box controls (click to tick).
Page 1: the morning briefing (the Dashboard tab on paper: quick rewards with deadlines, the focus
project's two next steps, the priority burndown, list 2, decisions, the morning routine).
Page 2: contents, immediate steps, today, this week.
The contents page numbers come from a LibreOffice render when soffice is installed.

Usage: python3 Scripts/make_printable.py [--date 2026-10-18]
"""
import argparse
import datetime as dt
import re
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

from docx import Document
from docx.enum.text import WD_BREAK, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.oxml import parse_xml
from docx.shared import Pt, RGBColor, Inches

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.6"
PLANS = ROOT / "Day and Week Plans"
OUT = PLANS / "Me-Printable-Tracker.docx"
ARCHIVE = ROOT / "X - Archive" / "Printable versions"
TASKS = "3-TaskContextAndProjectPlans.md"
NAVY = RGBColor(0x1F, 0x4E, 0x79)
GREY = RGBColor(0x59, 0x59, 0x59)
RED = RGBColor(0xC0, 0x00, 0x00)
GREEN = RGBColor(0x2E, 0x7D, 0x32)
W14 = "http://schemas.microsoft.com/office/word/2010/wordml"
MC = "http://schemas.openxmlformats.org/markup-compatibility/2006"
CHECKBOX = (
    '<w:sdt xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:w14="%s">'
    '<w:sdtPr><w14:checkbox><w14:checked w14:val="0"/>'
    '<w14:checkedState w14:val="2612" w14:font="MS Gothic"/>'
    '<w14:uncheckedState w14:val="2610" w14:font="MS Gothic"/></w14:checkbox></w:sdtPr>'
    '<w:sdtContent><w:r><w:rPr><w:rFonts w:ascii="MS Gothic" w:eastAsia="MS Gothic" w:hAnsi="MS Gothic"/>'
    '<w:sz w:val="%d"/></w:rPr><w:t>☐</w:t></w:r></w:sdtContent></w:sdt>'
)
ID = re.compile(r"\b([TP]\d{2})\b")


# ---------- reading the sources ----------

def md_tables(text):
    """Return {section heading: [row dicts]} for the first table under each '## ' heading."""
    tables = {}
    for block in re.split(r"^## ", text, flags=re.M)[1:]:
        title, _, body = block.partition("\n")
        lines = [l for l in body.splitlines() if l.startswith("|")]
        if len(lines) < 2:
            continue
        head = [c.strip() for c in lines[0].strip("|").split("|")]
        rows = []
        for l in lines[2:]:
            cells = [c.strip() for c in l.strip("|").split("|")]
            rows.append(dict(zip(head, cells)))
        tables[title.strip()] = rows
    return tables


def sections(text):
    """{SECTION heading: [(text, value)]} for the upper-case headings in a plan file, plus 'DONE'.

    A heading's parenthesised tail is kept as its context, e.g. HERE AND NOW (home, Sun evening)."""
    out, cur = {}, None
    for line in text.splitlines():
        l = line.strip()
        if l.startswith("# DONE"):
            cur = out.setdefault("DONE", [])
        elif re.match(r"^[A-Z][A-Z &]+(\(.*\))?$", l) or l.startswith("# "):
            cur = out.setdefault(l.lstrip("# ").strip(), [])
        elif cur is not None:
            m = re.match(r"- \[[ x]\] (.*?)(?:\. Value: (.*))?$", l) or re.match(r"^\d+\.\s*(.*)()$", l)
            if m:
                cur.append((m.group(1), m.group(2) or ""))
    return out


def section(secs, prefix):
    """The (context, items) for the first heading starting with prefix."""
    for k, v in secs.items():
        if k.startswith(prefix):
            ctx = re.search(r"\((.*)\)", k)
            return (ctx.group(1) if ctx else ""), v
    return "", []


def week_plan(text):
    part = text.split("# THIS WEEK", 1)[1].split("# DONE", 1)[0]
    lines = [l.strip() for l in part.strip().splitlines()]
    title = lines[0] if lines else ""
    goals = [re.sub(r"^\d+\.\s*", "", l) for l in lines if re.match(r"^\d+\.", l)]
    return title, goals


def last_week(text):
    entry = text.split("\n## ", 2)[1]
    title = entry.splitlines()[0]
    m = re.search(r"\*\*Outcome against last week's objectives\*\*\s*\n((?:\|.*\n)+)", entry)
    rows = []
    if m:
        for l in m.group(1).strip().splitlines()[2:]:
            c = [x.strip() for x in l.strip("|").split("|")]
            rows.append((c[1], re.sub(r"\*\*", "", c[2])))
    return title, rows


def routines(text):
    out = []  # (level, title, items)
    for line in text.splitlines():
        if line.startswith("## "):
            out.append((1, line[3:].strip(), []))
        elif line.startswith("### "):
            out.append((2, line[4:].strip(), []))
        elif line.startswith("- ") and out:
            out[-1][2].append(line[2:])
    return out


def points_of(text, pts, none="no points"):
    """'T03 · 200 pts' for each task ID in text, or the `none` label."""
    found = [i for i in dict.fromkeys(ID.findall(text)) if i in pts]
    if found:
        return ", ".join(f"{i} · {pts[i]} pts" for i in found)
    return none


def split_deadline(text):
    """'By 7pm: book the hotel' -> ('7pm', 'Book the hotel'); 'Any time, ...: x' -> ('Any time', 'X')."""
    m = re.match(r"^(?:By ([^:]{1,15})|(Any time)[^:]*):\s*(.*)$", text)
    if not m:
        return "", text
    rest = m.group(3)
    return m.group(1) or m.group(2), rest[:1].upper() + rest[1:]


def project_steps(tasks, pid, n=2):
    """The next n open tasks of a project (directly or through its milestones), Q1 first."""
    ms = {r["ID"] for r in tasks["Milestones (1000 points each)"] if r.get("Project") == pid}
    rows = [r for r in tasks["Active tasks"] if r["Status"] in ("Now", "Open", "Blocked")
            and (r["Milestone"] == pid or r["Milestone"] in ms)]
    return sorted(rows, key=lambda r: r["Q"])[:n]


def strip_ids(text):
    text = re.sub(r"\s*\((?:[TP]\d{2}[,;]?\s*)+\)", "", text)
    text = re.sub(r"\((?:[TP]\d{2}[,;]?\s*)+", "(", text)
    return ID.sub("", text).replace("()", "").replace(" ,", ",").strip(" .:")


# ---------- burndown ----------

def parse_date(s):
    try:
        return dt.datetime.strptime(s.strip(), "%d %b %y").date()
    except ValueError:
        return None


def bar(frac, n=10):
    k = round(max(0.0, min(1.0, frac)) * n)
    return "■" * k + "□" * (n - k)


def burndown(row, today):
    start, due = parse_date(row["Start"]), parse_date(row["Due"])
    done = row["Done %"].strip()
    done = int(done) / 100 if done.isdigit() else None
    used = None
    if start and due and due > start:
        used = max(0.0, min(1.0, (today - start).days / (due - start).days))
    if done is not None and done >= 1:
        status, colour = "Done: milestone points earned", GREEN
    elif due is None:
        status, colour = "No date: set one", RED
    elif done is None:
        status, colour = "No % yet: estimate it", RED
    elif today > due:
        status, colour = "Overdue", RED
    elif used is not None and done + 0.1 < used:
        status, colour = f"Behind by {round((used - done) * 100)} pts", RED
    else:
        status, colour = "On track", GREEN
    days_left = (due - today).days if due else None
    return done, used, status, colour, days_left


# ---------- writing ----------

class Doc:
    def __init__(self):
        self.d = Document()
        s = self.d.sections[0]
        s.page_width, s.page_height = Inches(8.5), Inches(11)
        s.left_margin = s.right_margin = Inches(0.83)
        s.top_margin = s.bottom_margin = Inches(0.69)
        st = self.d.styles["Normal"]
        st.font.name, st.font.size = "Arial", Pt(12)
        for name, size, colour in [("Title", 24, NAVY), ("Heading 1", 17, NAVY),
                                   ("Heading 2", 15, NAVY), ("Heading 3", 13, GREY)]:
            h = self.d.styles[name]
            h.font.name, h.font.size, h.font.bold, h.font.color.rgb = "Arial", Pt(size), True, colour
            for attr in ("asciiTheme", "hAnsiTheme", "eastAsiaTheme", "cstheme"):
                h.element.rPr.rFonts.attrib.pop(
                    "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}" + attr, None)
            h.paragraph_format.space_before = Pt(8 if name != "Title" else 0)
            h.paragraph_format.space_after = Pt(4)
            h.paragraph_format.keep_with_next = True
        self.first = True
        self.toc = []

    def run(self, p, text, size=12, bold=False, colour=None, italic=False):
        r = p.add_run(text)
        r.font.name, r.font.size, r.bold, r.italic = "Arial", Pt(size), bold, italic
        if colour:
            r.font.color.rgb = colour
        return r

    def page(self):
        if not self.first:
            self.d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        self.first = False

    def heading(self, text, level=1):
        if level == 1:
            self.toc.append(text)
        return self.d.add_heading(text, level)

    def contents(self, marker, pages):
        """Insert a Word TOC field before marker; its shown result lists the H1 headings with pages."""
        w = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
        fld = lambda t: parse_xml(f'<w:r xmlns:w="{w}"><w:fldChar w:fldCharType="{t}"/></w:r>')
        paras = []
        for i, text in enumerate(self.toc):
            p = marker.insert_paragraph_before()
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.tab_stops.add_tab_stop(Inches(6.8), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
            if i == 0:
                p._p.append(fld("begin"))
                p._p.append(parse_xml(f'<w:r xmlns:w="{w}"><w:instrText xml:space="preserve"> TOC \\o "1-1" \\h \\z \\u </w:instrText></w:r>'))
                p._p.append(fld("separate"))
            self.run(p, f"{text}\t{pages.get(text, '')}", 10)
            paras.append(p)
        paras[-1]._p.append(fld("end"))

    def para(self, text="", size=12, colour=None, italic=False, after=6):
        p = self.d.add_paragraph()
        p.paragraph_format.space_after = Pt(after)
        if text:
            self.run(p, text, size, colour=colour, italic=italic)
        return p

    def note(self, text):
        return self.para(text, 10, GREY, True)

    def bullet(self, text, bold_lead=None):
        p = self.d.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after = Pt(3)
        if bold_lead:
            self.run(p, bold_lead + " ", 12, True)
        self.run(p, text, 12)
        return p

    def item(self, text, box=True, size=12, label=None, tail=None, tail_colour=GREY, after=6, strike=False):
        p = self.d.add_paragraph()
        p.paragraph_format.space_after = Pt(after)
        p.paragraph_format.left_indent = Inches(0.35)
        p.paragraph_format.first_line_indent = Inches(-0.35)
        if box:
            p._p.append(parse_xml(CHECKBOX % (W14, size * 2)))
            self.run(p, "  ", size)
        runs = []
        if label:
            runs.append(self.run(p, label + "   ", size, True, NAVY))
        runs.append(self.run(p, text, size))
        if tail:
            runs.append(self.run(p, "   " + tail, size - 2, colour=tail_colour))
        for r in runs:
            r.font.strike = strike
        return p

    def lines(self, label, n=2):
        self.heading(label, 3)
        for _ in range(n):
            self.para("_" * 62, 12, GREY, after=8)

    def save(self, path):
        self.d.save(path)
        # Declare w14 on the root so every Word version reads the check boxes.
        with zipfile.ZipFile(path) as z:
            parts = {n: z.read(n) for n in z.namelist()}
        xml = parts["word/document.xml"].decode("utf-8")
        if "xmlns:w14=" not in xml.split(">", 2)[1]:
            xml = xml.replace("<w:document ", f'<w:document xmlns:w14="{W14}" xmlns:mc="{MC}" mc:Ignorable="w14" ', 1)
        parts["word/document.xml"] = xml.encode("utf-8")
        settings = parts["word/settings.xml"].decode("utf-8")
        settings = re.sub(r'<w:zoom(?![^>]*w:percent)', '<w:zoom w:percent="100"', settings)
        parts["word/settings.xml"] = settings.encode("utf-8")
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
            for n, b in parts.items():
                z.writestr(n, b)


def summary(tasks, nxt, today):
    """Points earned today, open task points, burndown states, milestones behind and the next deadline."""
    active = tasks["Active tasks"]
    day = f"Done {today.day} {today.strftime('%b')}"
    # Points earned today: tasks and milestones marked done today, plus the gym if the workout is ticked.
    earned = []
    for r in tasks["Recently completed (last 14 days)"]:
        if r["Status"] == day:
            earned.append((r["ID"], int(r["Pts"].replace(",", ""))))
    for r in tasks["Milestones (1000 points each)"]:
        if r["Due"] == day:
            earned.append((r["ID"], int(r["Pts"].replace(",", "") or 1000)))
    if any("workout" in t.lower() for t, _ in nxt.get("DONE", [])):
        earned.append(("gym", 100))
    open_pts = sum(int(r["Pts"].replace(",", "")) for r in active
                   if r["Status"] != "Parked" and r["Pts"].replace(",", "").isdigit())
    states = [(r, burndown(r, today)) for r in tasks["Milestones (burndown)"]]
    behind = [r["ID"] for r, b in states if b[2].startswith(("Behind", "Overdue"))]
    upcoming = sorted([(b[4], r) for r, b in states if b[4] is not None and b[4] >= 0 and (b[0] or 0) < 1],
                      key=lambda x: x[0])

    return {"earned": earned, "open": open_pts, "states": states, "behind": behind, "upcoming": upcoming}


def build(today, pages=None):
    pages = pages or {}
    tasks = md_tables((PLANS / TASKS).read_text())
    nxt = sections((PLANS / "1-Me-NextStep.txt").read_text())
    plan = sections((PLANS / "2-Me-DayWeekPlan.txt").read_text())
    lw_title, lw_rows = last_week((ROOT / "Context/3-Me-WeeklyLog.md").read_text())
    fixed = routines((ROOT / "Context/routines.md").read_text())
    active = tasks["Active tasks"]
    pts = {r["ID"]: int(r["Pts"].replace(",", "")) for r in active if r["Pts"].replace(",", "").isdigit()}
    places = tasks["Lists by place"]
    burn = tasks["Milestones (burndown)"]
    day = f"Done {today.day} {today.strftime('%b')}"
    here_ctx, here = section(nxt, "HERE AND NOW")
    quick = section(nxt, "QUICK WINS")[1]
    to_plan = section(nxt, "TO PLAN")[1]
    today_items = section(plan, "TODAY")[1]
    week_items = section(plan, "THIS WEEK")[1]
    week_title = (PLANS / "2-Me-DayWeekPlan.txt").read_text().split("# THIS WEEK", 1)[1].strip().splitlines()[0]

    sm = summary(tasks, nxt, today)
    earned, open_pts, states, behind, upcoming = sm["earned"], sm["open"], sm["states"], sm["behind"], sm["upcoming"]

    doc = Doc()

    def task_item(text, value="", size=12, after=4, none="no points"):
        doc.item(strip_ids(text), size=size, after=after,
                 tail=points_of(text, pts, none) + (f" · {value}" if value else ""))

    # ----- Page 1: morning briefing (the Dashboard on paper) -----
    sel = {r["Selector"]: r["Choice"] for r in tasks.get("Dashboard selections", [])}
    pid = (sel.get("Project") or "").split(" ")[0]
    mid = (sel.get("Priority") or "").split(" ")[0]
    doc.page()
    doc.heading("Morning briefing", 1)
    doc.note(f"{today.strftime('%a %d %b %Y').replace(' 0', ' ')}. Tick fast, score points, beat the deadlines.")
    total = sum(p for _, p in earned)
    nxt_dl = f" Next deadline: {upcoming[0][1]['ID']}, {upcoming[0][0]} days." if upcoming else ""
    doc.para(f"Points: {total:,} earned today; {open_pts:,} open.{nxt_dl} Behind: {', '.join(behind) or 'nothing'}.", 10, GREY, after=2)

    doc.heading("Quick rewards (list 1)", 3)
    for text, value in here + quick:
        by, rest = split_deadline(strip_ids(text))
        doc.item(rest, size=11, label=f"by {by}" if by and by != "Any time" else by or None, after=1,
                 tail=points_of(text, pts, "10 pts") + (f" · {value}" if value else ""))

    morning = next((items for level, title, items in fixed if title.startswith("Morning")), [])
    if morning:
        doc.heading("Morning routine (10 pts a step; the time is the deadline)", 3)
        p = doc.para(after=2)
        for it in morning:
            text = it[4:] if it.startswith("[ ] ") else it
            label, text = text.split(" | ", 1) if " | " in text else ("", text)
            p._p.append(parse_xml(CHECKBOX % (W14, 20)))
            doc.run(p, f" {label} ", 10, True, NAVY)
            doc.run(p, text + "    ", 10)

    proj = next((r for r in tasks["Projects"] if r["ID"] == pid), None)
    if proj:
        doc.heading(f"Focus project: {pid} {proj['Project']}", 3)
        for r in project_steps(tasks, pid):
            doc.item(strip_ids(r["Task"]), size=11, label=r["ID"], after=1,
                     tail=f"{r['Pts']} pts · " + r["Next action, detail, links"][:70].rsplit(" ", 1)[0] + "…")

    for r, (done, used, status, colour, days_left) in states:
        if r["ID"] == mid:
            doc.heading(f"Priority: {mid} {r['Milestone']}", 3)
            q = doc.para(after=1)
            doc.run(q, "Done " + (bar(done) + f" {round(done * 100)}%" if done is not None else "?") + "   ", 10)
            doc.run(q, "Time " + (bar(used) + f" {round(used * 100)}%" if used is not None else "-") + "   ", 10, colour=GREY)
            doc.run(q, status, 10, True, colour)
            doc.para(f"Due {r['Due']}. Next: {r['Next step']}", 9, GREY, after=2)

    doc.heading("Today and this week (list 2)", 3)
    for text, _ in today_items:
        doc.item(strip_ids(text), size=11, after=0, tail=points_of(text, pts, ""))
    doc.para("This week: " + " · ".join(f"{i + 1}. {strip_ids(g)}" for i, (g, _) in enumerate(week_items)), 10, after=2)

    daily = tasks.get("Daily decisions", [])
    if daily:
        doc.heading("Decide tonight (for tomorrow)", 3)
        for r in [r for r in daily if r["Status"] == "To decide"]:
            doc.item(r["Question"], size=10, after=0, tail="Recommended: " + r["Recommended"])
        doc.item("New question: " + "_" * 40, size=10, after=0)
        decided = [r for r in daily if r["Status"] != "To decide"]
        if decided:
            q = doc.para(after=0)
            doc.run(q, "Already decided: ", 10, True, NAVY)
            doc.run(q, " · ".join(f"{r['Question'].rstrip('?')}: {r['Answer'] or r['Recommended']}" for r in decided), 10)

    # ----- Page 2: contents, immediate steps, today, this week -----
    doc.page()
    doc.d.add_heading("Printable tracker", 0)
    doc.d.add_heading("Contents", 2)
    marker = doc.para(after=2)
    doc.heading("Immediate steps", 1)
    for text, value in quick[:3] + to_plan:
        task_item(text, size=12, after=3)
    doc.heading("Today", 1)
    for text, _ in today_items:
        none = "100-200 pts each" if "Here and now" in text else "rest · no points"
        task_item(text, size=12, after=3, none=none)
    doc.heading("This week", 1)
    doc.note(week_title)
    for text, _ in week_items:
        task_item(text, size=12, after=3)

    # ----- Page 3: strategic priorities, avoided projects, burndown -----
    doc.page()
    doc.heading("Strategic priorities", 1)
    for r in tasks["Strategic priorities"]:
        doc.item(strip_ids(r["Priority"]), size=12, label=r["#"],
                 tail=points_of(r["Priority"], pts) + " · " + r["Next steps"], after=4)
    doc.heading("Avoided projects: next step only", 1)
    doc.note("Each step is 15 minutes or less. Do one, then stop if you want.")
    for r in tasks["Avoided projects (next step only)"]:
        doc.item(r["Next step"], label=strip_ids(r["Project"]), size=12,
                 tail=points_of(r["Project"], pts, "parked · no points yet"), after=4)
    doc.heading("Milestones: burndown (1,000 pts; +4,000 if done in the target week)", 1)
    doc.note("Done vs time used (start to due). Done well behind time used = behind. Personal first.")
    for r, (done, used, status, colour, days_left) in states:
        p = doc.item(r["Milestone"], box=False, size=11, label=r["ID"])
        doc.run(p, "   " + status, 10, True, colour)
        p.paragraph_format.space_after = Pt(1)
        p.paragraph_format.keep_with_next = True
        q = doc.para(after=4)
        q.paragraph_format.left_indent = Inches(0.35)
        due = r["Due"] if r["Due"] != "tbc" else "no date"
        left = f", {days_left} days left" if days_left is not None and days_left >= 0 and (done or 0) < 1 else ""
        doc.run(q, "Done " + (bar(done) + f" {round(done * 100)}%" if done is not None else "? ") + "   ", 10)
        doc.run(q, "Time " + (bar(used) + f" {round(used * 100)}%" if used is not None else "-") + "   ", 10, colour=GREY)
        doc.run(q, f"Due {due}{left}. Next: {r['Next step']}", 9, colour=GREY)

    # ----- Decisions and last week -----
    doc.page()
    doc.heading("Key decisions", 1)
    doc.note("Struck through: closed.")
    for r in tasks["Key decisions"]:
        doc.item(r["Decision"], box=r["Status"] == "To decide", size=12,
                 label=r["Date"] if r["Date"] != "-" else None, tail=r["Status"], after=3,
                 strike=r["Status"] == "Closed")
    doc.heading("Last week: retrospective", 1)
    doc.note(lw_title)
    for obj, outcome in lw_rows:
        doc.item(obj, box=False, size=12, tail=outcome, after=3)
    doc.lines("What went well", 1)
    doc.lines("What I will change this week", 1)

    # ----- Lists by place -----
    doc.page()
    doc.heading("Lists by place", 1)
    doc.note("Points are for the whole task; tick the items as you go.")
    for name, title in [("Buy", "Buy"), ("Home", "Indoors (at home)"),
                        ("Online", "Online quick wins (non-work)"), ("Admin", "Admin (at a desk)"),
                        ("Ask AI", "Ask AI")]:
        rows = [r for r in places if r["List"] == name]
        if rows:
            doc.heading(title, 2)
            for r in rows:
                doc.item(r["Item"], size=11, tail=points_of(r["Task"], pts), after=2)

    # ----- Fixed routines, one page per top-level list -----
    for level, title, items in fixed:
        if level == 1:
            doc.page()
            doc.heading(title, 1)
            if title.startswith("Morning"):
                doc.note("Points: Kriya 10 x current streak; gym session 100; CPAP 1 per minute. Log them on the Tracker tab.")
        else:
            doc.heading(title, 2)
        for it in items:
            box = it.startswith("[ ] ")
            text = it[4:] if box else it
            label = None
            if " | " in text:
                label, text = text.split(" | ", 1)
            doc.item(text, box=box, size=14, label=label)

    doc.contents(marker, pages)
    doc.save(OUT)
    return OUT, doc.toc


def page_numbers(path, headings):
    """Render with LibreOffice and find the page each H1 heading starts on; {} if soffice is missing."""
    soffice = shutil.which("soffice")
    if not soffice:
        return {}
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([soffice, f"-env:UserInstallation=file://{tmp}/profile", "--headless",
                        "--convert-to", "pdf", "--outdir", tmp, str(path)], capture_output=True, timeout=180)
        pdf = Path(tmp) / (path.stem + ".pdf")
        if not pdf.exists():
            return {}
        text = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True).stdout
    found, page = {}, 1
    pages = text.split("\f")
    for h in headings:
        for n in range(page, len(pages) + 1):
            if any(l.strip() == h for l in pages[n - 1].splitlines()):
                found[h], page = n, n
                break
    return found


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="Burndown date, YYYY-MM-DD (default: today)")
    a = ap.parse_args()
    today = dt.date.fromisoformat(a.date) if a.date else dt.date.today()
    out, heads = build(today)
    pages = page_numbers(out, heads)
    if pages:
        build(today, pages)
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(out, ARCHIVE / f"{OUT.stem}_v{VERSION}.docx")
    print(out, "(contents with page numbers)" if pages else "(contents without page numbers: soffice not found)")
