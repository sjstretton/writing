"""Keep the repo, the master Google Sheet and the printable tracker consistent.

Run before every push to main (AGENTS.md has the full procedure):

  python3 Scripts/update.py sync --snapshot S.json [--apply]
      Three-way compare: the repo, a snapshot of the Sheet (S.json, read with the Sheets connector)
      and the state at the last sync (Context/sync-state.json). A unit changed on one side only is
      taken from that side (the side that changed is the master); with --apply, Sheet-side changes
      are written into the repo files. A unit changed differently on both sides is a conflict:
      nothing is applied, the conflicts are listed (exit code 2) and Stephen decides.
  python3 Scripts/update.py build
      Rebuild Me-Printable-Tracker.docx (refuses if the .docx was edited by hand since the last
      build: fold those edits into the sources or the layout first, then use --force).
  python3 Scripts/update.py render --out P.json [--snapshot S.json]
      Write the payload that rewrites the Dashboard, Plan, Context, Regular lists and Updateable
      lists tabs from the repo (values plus desktop formatting). The snapshot keeps today's ticks
      on the lists and the Dashboard (Dashboard ticks reset on a new day).
  python3 Scripts/update.py baseline
      Record the repo as the agreed state, after the Sheet has been rewritten from the render.
  python3 Scripts/update.py check
      Consistency checks (also run by GitHub Actions on every push to main).

Snapshot format: {"Dashboard": rows, "Plan": rows, "Context": rows, "Regular lists": rows,
"Updateable lists": rows, "Tracker": rows}, each the `values` of get_values on A1:K400 of that tab.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]   # 0 Planning Instructions
REPO = ROOT.parent                           # combined repo root (planning 0-3, writing A-F)
sys.path.insert(0, str(ROOT / "Scripts"))
import make_printable as mp  # noqa: E402

STATE = ROOT / "Context" / "sync-state.json"
PLANS = REPO / "1 Day and Week Plans"
TASKS = PLANS / "3-TaskContextAndProjectPlans.md"
NEXT = PLANS / "1-Me-NextStep.txt"
DAYWEEK = PLANS / "2-Me-DayWeekPlan.txt"
ROUTINES = ROOT / "Context" / "routines.md"
PRINT_SOURCES = [TASKS, NEXT, DAYWEEK, ROUTINES, ROOT / "Context" / "3-Me-WeeklyLog.md", ROOT / "Scripts" / "make_printable.py"]
SHEET_IDS = {"Dashboard": 120, "Plan": 106, "Context": 103, "Regular lists": 108, "Updateable lists": 111}
ID_RE = re.compile(r"\b([TP]\d{2})\b")

# Context tab sections: (heading row text, task-file section)
CONTEXT_SECTIONS = [
    ("ACTIVE TASKS (100-200 points each)", "Active tasks"),
    ("MILESTONES (1000 points each)", "Milestones (1000 points each)"),
    ("PROJECTS (definitions)", "Projects"),
    ("PARKED (not now)", "Parked (not now)"),
    ("RECENTLY COMPLETED (last 14 days)", "Recently completed (last 14 days)"),
]
# Task-file tables shown on the Plan tab, synced as whole tables
PLAN_TABLES = ["Strategic priorities", "Avoided projects (next step only)", "Milestones (burndown)", "Key decisions"]
# Task-file tables shown (and edited) on the Dashboard tab
DASH_TABLES = ["Daily decisions", "Dashboard selections"]
LIST_ORDER = ["Buy", "Home", "Online", "Admin", "Ask AI"]
PLACE_TITLES = {"Buy": "BUY (things to order)", "Home": "HOME (indoors)", "Online": "ONLINE (quick wins, non-work)",
                "Admin": "ADMIN (at a desk)", "Ask AI": "ASK AI"}


def norm(v):
    v = ("" if v is None else str(v)).replace("\r", "").strip()
    if re.fullmatch(r"\d{1,3}(,\d{3})+", v):
        v = v.replace(",", "")
    return v


def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:16]


def file_hash(path):
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()[:16]


# ====================================================================== plan text files

def parse_item(line):
    """A plan line -> (kind, checked, text, ids, value), or None."""
    l = line.strip()
    m = re.match(r"- \[( |x)\] (.*)$", l)
    if m:
        kind, checked, rest = "box", m.group(1) == "x", m.group(2)
    elif re.match(r"\d+\.\s", l):
        kind, checked, rest = "num", False, re.sub(r"^\d+\.\s*", "", l)
    elif l.startswith("- "):
        kind, checked, rest = "bullet", False, l[2:]
    else:
        return None
    value = ""
    if ". Value: " in rest:
        rest, value = rest.split(". Value: ", 1)
    ids = list(dict.fromkeys(ID_RE.findall(rest)))
    return kind, checked, mp.strip_ids(rest), ids, value


def render_item(kind, checked, text, ids, value, n=1):
    body = text + (f" ({', '.join(ids)})" if ids else "") + (f". Value: {value}" if value else "")
    if kind == "num":
        return f"{n}. {body}"
    if kind == "bullet":
        return f"- {body}"
    return f"- [{'x' if checked else ' '}] {body}"


def parse_plan_file(path, prefix):
    """Sections of a plan file: {key: {"head": line, "title": str|None, "items": [...], "span": (a, b)}}.

    Headings are '# X' lines and upper-case or 'Word (tail)' lines that are not items; the line right
    after a '# X' heading (if it is not an item or a heading) is that section's title."""
    lines = path.read_text().replace("\r", "").split("\n")
    secs, order, cur = {}, [], None
    i = 0
    while i < len(lines):
        l = lines[i].strip()
        item = parse_item(l) if l else None
        if l and item is None:
            name = l.lstrip("# ").strip()
            base = re.sub(r"\s*\(.*\)$", "", name)
            key = f"{prefix}/{base}"
            n = 2
            while key in secs:
                key, n = f"{prefix}/{base} {n}", n + 1
            cur = secs[key] = {"head": lines[i], "title": None, "items": [], "span": [i, i + 1]}
            order.append(key)
            if l.startswith("# ") and i + 1 < len(lines) and lines[i + 1].strip() and parse_item(lines[i + 1]) is None \
                    and not re.match(r"^[A-Z][A-Z &]+(\s*\(.*\))?$", lines[i + 1].strip()):
                cur["title"] = lines[i + 1].strip()
                i += 1
                if i + 1 < len(lines) and not lines[i + 1].strip():
                    i += 1
                cur["span"][1] = i + 1
        elif item and cur is not None:
            cur["items"].append(item)
            cur["span"][1] = i + 1
        i += 1
    return secs, order, lines


def plan_units():
    units = {}
    for path, prefix in [(NEXT, "next"), (DAYWEEK, "dayweek")]:
        secs, order, _ = parse_plan_file(path, prefix)
        for k in order:
            s = secs[k]
            units["plan:" + k] = {"head": s["head"].strip(), "title": s["title"],
                                  "items": [list(it) for it in s["items"]]}
    return units


def write_plan_unit(key, unit):
    prefix, sec = key[5:].split("/", 1)
    path = NEXT if prefix == "next" else DAYWEEK
    secs, order, lines = parse_plan_file(path, prefix)
    new = [unit["head"]] + ([unit["title"], ""] if unit.get("title") else [])
    new += [render_item(*it, n=i + 1) for i, it in enumerate(unit["items"])]
    if f"{prefix}/{sec}" in secs:
        a, b = secs[f"{prefix}/{sec}"]["span"]
        lines[a:b] = new
    else:  # a section added on the Sheet: append before '# DONE' or at the end
        at = next((secs[k]["span"][0] for k in order if k.endswith("/DONE")), len(lines))
        lines[at:at] = new + [""]
    path.write_text("\n".join(lines))


# ====================================================================== task-file tables

def md_table_span(text, title):
    """(header line index, first row index, end index) of the first table under '## title'."""
    lines = text.split("\n")
    try:
        h = next(i for i, l in enumerate(lines) if l.strip() == f"## {title}")
    except StopIteration:
        return None, None, None, lines
    t = next(i for i in range(h + 1, len(lines)) if lines[i].startswith("|"))
    e = t + 2
    while e < len(lines) and lines[e].startswith("|"):
        e += 1
    return t, t + 2, e, lines


def cells(line):
    return [norm(c) for c in line.strip().strip("|").split("|")]


def row_key(row):
    return row[0] if row[0] not in ("", "-") else "-|" + row[1]


def decision_order(rows):
    """Daily decisions as the Dashboard shows them: open questions first, then the decided ones."""
    return sorted(rows, key=lambda r: (r + ["", "", ""])[2] != "To decide")


def task_units():
    text = TASKS.read_text().replace("\r", "")
    units = {}
    for _, sec in CONTEXT_SECTIONS:
        t, a, e, lines = md_table_span(text, sec)
        for line in lines[a:e]:
            r = cells(line)
            units[f"task:{row_key(r)}"] = {"section": sec, "row": r}
    for sec in PLAN_TABLES + DASH_TABLES + ["Lists by place", "Task scripts"]:
        t, a, e, lines = md_table_span(text, sec)
        if t is None:
            continue
        units[f"table:{sec}"] = {"head": cells(lines[t]), "rows": [cells(l) for l in lines[a:e]]}
    return units


def write_task_tables(units):
    """Rewrite the Context-section tables and whole tables of the task file from merged units."""
    text = TASKS.read_text().replace("\r", "")
    for _, sec in CONTEXT_SECTIONS:
        t, a, e, lines = md_table_span(text, sec)
        old = [cells(l) for l in lines[a:e]]
        keep = {k: u["row"] for k, u in units.items() if k.startswith("task:") and u["section"] == sec}
        rows = [keep.pop(f"task:{row_key(r)}") for r in old if f"task:{row_key(r)}" in keep] + list(keep.values())
        lines[a:e] = ["| " + " | ".join(r) + " |" for r in rows]
        text = "\n".join(lines)
    for k, u in units.items():
        if k.startswith("table:"):
            t, a, e, lines = md_table_span(text, k[6:])
            if t is not None:
                rows = decision_order(u["rows"]) if k == "table:Daily decisions" else u["rows"]
                lines[a:e] = ["| " + " | ".join(r) + " |" for r in rows]
                text = "\n".join(lines)
    TASKS.write_text(text)


# ====================================================================== regular lists (routines.md)

def routine_units():
    units, cur = {}, None
    for line in ROUTINES.read_text().replace("\r", "").split("\n"):
        m = re.match(r"^(##|###) (.*)", line)
        if m:
            cur = m.group(2).strip()
        elif line.startswith("- ") and cur:
            it = re.sub(r"^- (\[[ x]\] )?", "", line)
            label, text = it.split(" | ", 1) if " | " in it else ("", it)
            units.setdefault(f"list:{cur.lower()}", {"name": cur, "items": []})["items"].append([label.strip(), text.strip()])
    return units


def write_routines(units):
    lines = ROUTINES.read_text().replace("\r", "").split("\n")
    out, i, seen = [], 0, set()
    while i < len(lines):
        m = re.match(r"^(##|###) (.*)", lines[i])
        out.append(lines[i])
        i += 1
        if m and f"list:{m.group(2).strip().lower()}" in units:
            k = f"list:{m.group(2).strip().lower()}"
            seen.add(k)
            while i < len(lines) and lines[i].startswith("- "):
                i += 1
            out += [f"- [ ] {l} | {t}" if l else f"- [ ] {t}" for l, t in units[k]["items"]]
    for k, u in units.items():
        if k.startswith("list:") and k not in seen:
            out += ["", f"### {u['name']}"] + [f"- [ ] {l} | {t}" if l else f"- [ ] {t}" for l, t in u["items"]]
    ROUTINES.write_text("\n".join(out))


def repo_units():
    u = {}
    u.update(plan_units())
    u.update(task_units())
    u.update(routine_units())
    return {k: v for k, v in u.items()}


# ====================================================================== the Sheet: render

PLAN_NICE = {"NEXT STEP": "Next step", "HERE AND NOW": "Here and now", "QUICK WINS": "Quick wins",
             "TO PLAN": "To plan", "DONE": "Done", "TODAY": "Today", "THIS WEEK": "This week"}


def pts_formula(ids):
    if not ids:
        return ""
    parts = [f'IFERROR(VLOOKUP("{i}",Context!$A:$C,3,FALSE),0)' for i in ids]
    return "=" + "+".join(parts)


def render(units, snapshot=None, today=None):
    today = today or dt.date.today()
    ticks = sheet_ticks(snapshot) if snapshot else {}
    out = {"Dashboard": render_dashboard(units, snapshot, today)}

    # ---------------- Plan tab: same order as the printable ----------------
    tasks = mp.md_tables(TASKS.read_text())
    nxt = mp.sections(NEXT.read_text())
    sm = mp.summary(tasks, nxt, today)
    rows, fmt = [], []

    def add(row, kind, key=""):
        row = (row + [""] * 8)[:8] + [key]
        rows.append(row)
        fmt.append(kind)

    add(["", "Plan", "", "", f"Built {today.strftime('%a %d %b %Y').replace(' 0', ' ')} from the repo; edit here or in the repo, then sync"], "title")
    add([], "blank")
    add(["", "Summary"], "h1", "ro")
    total = sum(p for _, p in sm["earned"])
    got = f"earned today ({', '.join(f'{n} {p:,}' for n, p in sm['earned'])})" if sm["earned"] else "nothing earned yet today"
    add(["", "Points", "", total, f"{got}; {sm['open']:,} open in tasks"], "ro", "ro")
    if sm["upcoming"]:
        d, r = sm["upcoming"][0]
        add(["", "Next deadline", r["ID"], int(next((m["Pts"] for m in tasks["Milestones (1000 points each)"] if m["ID"] == r["ID"]), "1000").replace(",", "")), f"{r['Milestone']}: {d} day{'' if d == 1 else 's'} ({r['Done %'] or '?'}% done)"], "ro", "ro")
    add(["", "Milestones behind", "", "", ", ".join(sm["behind"]) or "nothing behind schedule"], "ro", "ro")
    add([], "blank")

    def plan_section(key, nice=None):
        u = units.get(key)
        if not u:
            return
        head = u["head"].lstrip("# ").strip()
        tail = re.search(r"\((.*)\)$", head)
        base = re.sub(r"\s*\(.*\)$", "", head)
        add(["", nice or PLAN_NICE.get(base, base), "Task", "Points", tail.group(1) if tail else ""], "h1" if base.isupper() or head.startswith("#") else "h2", f"sec|{key}|{u['head']}")
        if u.get("title"):
            add(["", u["title"]], "note", f"title|{key}")
        for kind, checked, text, ids, value in u["items"]:
            add([checked if kind == "box" else "", text, ", ".join(ids), pts_formula(ids), value], "item" if kind == "box" else "itemnb", f"item|{key}|{kind}")
        add([], "blank")

    for k in [k for k in units if k.startswith("plan:next/")]:
        if k.endswith("/NEXT STEP"):
            add(["", units[k]["title"] or ""], "note", f"title|{k}")
            rows[-1][8] = f"sec|{k}|{units[k]['head']}"
            continue
        plan_section(k)
    for k in [k for k in units if k.startswith("plan:dayweek/")]:
        plan_section(k)

    for sec in PLAN_TABLES:
        u = units.get(f"table:{sec}")
        if not u:
            continue
        add(["", sec], "h1", f"tsec|{sec}")
        add([""] + u["head"], "th", f"thead|{sec}")
        for r in u["rows"]:
            add([""] + r, "tr", f"trow|{sec}")
        add([], "blank")
    out["Plan"] = {"values": rows, "fmt": fmt, "widths": [34, 330, 90, 70, 420, 110, 110, 260, 10], "hide": [8]}

    # ---------------- Context tab ----------------
    rows, fmt = [], []
    rows.append(["Context", "=\"Open task points: \"&SUMIFS(C4:C{a},F4:F{a},\"<>Parked\")&\". Points: task 100-200; milestone 1000 (+4000 if done in its due week); Kriya 10 x streak; CPAP 1 per minute; gym 100\""])
    fmt.append("title")
    rows.append(["ID", "Task", "Pts", "Energy", "Q", "Status", "%", "Milestone", "Next action, detail, links"])
    fmt.append("th")
    ms_range = None
    burn_ids = {r[0] for r in units.get("table:Milestones (burndown)", {"rows": []})["rows"]}
    for head, sec in CONTEXT_SECTIONS:
        rows.append([head])
        fmt.append("h2")
        start = len(rows) + 1
        sec_rows = [u["row"] for k, u in units.items() if k.startswith("task:") and u["section"] == sec]
        for r in sec_rows:
            if sec == "Projects":
                n = len(rows) + 1
                rows.append([r[0], r[1], f"=SUMIFS($C${{ms0}}:$C${{ms1}},$H${{ms0}}:$H${{ms1}},A{n})", r[2], "-", r[3],
                             f"=IFERROR(AVERAGEIFS($G${{ms0}}:$G${{ms1}},$H${{ms0}}:$H${{ms1}},A{n}),\"\")", r[4], r[5]])
            else:
                row = (r + [""] * 9)[:9]
                if sec.startswith("Milestones") and row[0] in burn_ids:   # one source for milestone %: the Plan burndown
                    row[6] = f'=IFERROR(IF(VLOOKUP("{row[0]}",Plan!$B:$G,6,FALSE)="","?",VLOOKUP("{row[0]}",Plan!$B:$G,6,FALSE)/100),"?")'
                rows.append(row)
            fmt.append("tr")
        if sec == "Active tasks":
            active_end = len(rows)
        if sec.startswith("Milestones"):
            ms_range = (start, len(rows))
        rows.append([])
        fmt.append("blank")
    rows[0][1] = rows[0][1].format(a=active_end)
    rows = [[c.format(ms0=ms_range[0], ms1=ms_range[1]) if isinstance(c, str) and "{ms0}" in c else c for c in r] for r in rows]
    out["Context"] = {"values": rows, "fmt": fmt, "widths": [70, 380, 60, 60, 45, 100, 60, 110, 640], "freeze": 2, "percent_col": 6}

    # ---------------- Regular lists ----------------
    rows, fmt = [["", "Regular lists", "Same as Context/routines.md; printed at the end of the tracker"]], ["title"]
    for k, u in units.items():
        if k.startswith("list:"):
            m = re.match(r"^(.*?)(\s*\(.*\))?$", u["name"])
            rows.append(["", m.group(1).upper() + (m.group(2) or "")])
            fmt.append("h2")
            for label, text in u["items"]:
                rows.append([ticks.get(("Regular lists", u["name"].lower(), text), False), label, text])
                fmt.append("item")
            rows.append([])
            fmt.append("blank")
    out["Regular lists"] = {"values": rows, "fmt": fmt, "widths": [34, 110, 560]}

    # ---------------- Updateable lists ----------------
    rows, fmt = [["", "Updateable lists", "Same as Lists by place and Task scripts in the task file", "Points"]], ["title"]
    places = units.get("table:Lists by place", {"rows": []})["rows"]
    for name in LIST_ORDER:
        items = [r for r in places if r[0] == name]
        if items:
            rows.append(["", PLACE_TITLES[name]])
            fmt.append("h2")
            for r in items:
                rows.append([ticks.get(("Updateable lists", name.lower(), r[1]), False), r[2], r[1], pts_formula(ID_RE.findall(r[2]))])
                fmt.append("item")
            rows.append([])
            fmt.append("blank")
    scripts = units.get("table:Task scripts", {"rows": []})["rows"]
    if scripts:
        rows.append(["", "TASK SCRIPTS (what to do, word for word)"])
        fmt.append("h2")
        for r in scripts:
            rows.append([ticks.get(("Updateable lists", "task scripts", r[1]), False), r[0], r[1]])
            fmt.append("item")
    out["Updateable lists"] = {"values": rows, "fmt": fmt, "widths": [34, 150, 560, 70]}

    eod_file = ROOT / "Context" / ".eod-tracker.json"
    tracker = tracker_ranges(json.loads(eod_file.read_text()) if eod_file.exists() else None)
    for tab, t in out.items():
        t["sheetId"] = SHEET_IDS[tab]
        t["values"] = [[cellify(c) for c in r] for r in t["values"]]
        t["requests"] = format_requests(t) + t.pop("extra", [])
    for t in tracker:
        t["values"] = [[cellify(c) for c in r] for r in t["values"]]
    out["Tracker ranges"] = tracker   # write each with update_values; not a whole-tab rewrite
    return out


# ---------------- Dashboard tab: the morning game ----------------

MONTHS = '{"Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"}'
DASH_HEADS = {"Daily decisions": ["Day", "Question", "Status", "Recommended", "Answer"],
              "Dashboard selections": ["Selector", "Choice"]}


def dmy(ref):
    """Sheet formula: the date in a 'd Mon yy' text cell, as the burndown table writes it."""
    return (f'DATE(2000+VALUE(RIGHT({ref},2)),MATCH(MID({ref},FIND(" ",{ref})+1,3),{MONTHS},0),'
            f'VALUE(LEFT({ref},FIND(" ",{ref})-1)))')


def spark(ref, colour="#2E7D32"):
    return f'=IF({ref}="","",SPARKLINE({ref},{{"charttype","bar";"max",1;"color1","{colour}"}}))'


def dash_ticks(snapshot, today):
    """{row key: ticked} from the Dashboard, only if it was built today (a new day starts a new game)."""
    rows = (snapshot or {}).get("Dashboard") or []
    if not rows or norm((rows[0] + [""] * 7)[6]) != f"built|{today.isoformat()}":
        return {}
    return {norm(r[6]): r[0] == "TRUE" for r in ((r + [""] * 7)[:7] for r in rows) if r[6].startswith(("reward|", "routine|"))}


def render_dashboard(units, snapshot, today):
    """One screen for the morning: pick a project and a priority, see the next steps and the burndown,
    tick quick rewards against their deadlines and the morning routine, and see tonight's and
    yesterday's decisions. Column G (hidden) holds row keys: sel| and trow| rows sync with the task
    file (Dashboard selections, Daily decisions); reward| and routine| rows carry today's ticks."""
    ticks = dash_ticks(snapshot, today)
    rows, fmt, extra = [], [], []
    sid = SHEET_IDS["Dashboard"]

    def add(row, kind, key=""):
        rows.append((row + [""] * 6)[:6] + [key])
        fmt.append(kind)
        return len(rows)

    def cell(r, c):
        return {"sheetId": sid, "startRowIndex": r - 1, "endRowIndex": r, "startColumnIndex": c, "endColumnIndex": c + 1}

    def dropdown(r0, r1, c, options):
        extra.append({"setDataValidation": {"range": {**cell(r0, c), "endRowIndex": r1 - 1},
                      "rule": {"condition": {"type": "ONE_OF_LIST", "values": [{"userEnteredValue": o} for o in options]},
                               "showCustomUi": True, "strict": True}}})

    def percent(r, c=3):
        extra.append({"repeatCell": {"range": cell(r, c), "cell": {"userEnteredFormat": {"numberFormat": {"type": "PERCENT", "pattern": "0%"}}},
                                     "fields": "userEnteredFormat.numberFormat"}})

    def input_cell(r, c=2):
        extra.append({"repeatCell": {"range": cell(r, c), "cell": {"userEnteredFormat": {"backgroundColor": {"red": 1, "green": 0.95, "blue": 0.8}}},
                                     "fields": "userEnteredFormat.backgroundColor"}})

    sel = {r[0]: r[1] for r in units.get("table:Dashboard selections", {"rows": []})["rows"]}
    projects = [u["row"] for k, u in units.items() if k.startswith("task:") and u["section"] == "Projects"]
    burn = units.get("table:Milestones (burndown)", {"rows": []})["rows"]
    label = today.strftime('%a %d %b %Y').replace(' 0', ' ')

    add(["", "Dashboard", f"Morning game: tick fast, score points, beat the deadlines. Built {label}"], "title", f"built|{today.isoformat()}")
    score = add(["", "Morning score"], "score", "ro")
    add([], "blank")

    # 1. Focus project: two next steps
    add(["", "1. Focus project", "Pick a project; its two next steps show below"], "h2", "ro")
    pr = add(["", "Project", sel.get("Project", ""), f'=IFERROR(VLOOKUP(REGEXEXTRACT($C${len(rows) + 1},"^\\S+"),Context!$A:$G,7,FALSE),"")',
              spark(f"D{len(rows) + 1}", "#1F4E79")], "sel", "sel|Project")
    dropdown(pr, pr + 1, 2, [f"{r[0]} {r[1]}" for r in projects])
    input_cell(pr)
    percent(pr)
    add(["", "ID", "Next step", "Pts", "First action"], "th", "ro")
    pid = f'REGEXEXTRACT($C${pr},"^\\S+")'
    rng = lambda c: f"Context!${c}$3:${c}$400"
    steps = (f'=IFERROR(ARRAY_CONSTRAIN(SORT(FILTER({{{rng("A")},{rng("B")},{rng("C")},LEFT({rng("I")},160),{rng("E")}}},'
             f'REGEXMATCH({rng("F")},"^(Now|Open|Blocked)$"),'
             f'(({rng("H")}={pid})+ISNUMBER(MATCH({rng("H")},FILTER({rng("A")},{rng("H")}={pid}),0)))>0),5,TRUE),2,4),'
             f'"No open task for this project: add one on Context")')
    add(["", steps], "ro", "ro")
    add([], "ro", "ro")
    add([], "blank")

    # 2. Priority milestone: burndown
    add(["", "2. Priority milestone", "Done vs time used (start to due): done well behind time = behind. 1,000 pts, +4,000 if done in the target week"], "h2", "ro")
    mr = len(rows) + 1
    mid = f'REGEXEXTRACT($C${mr},"^\\S+")'
    look = lambda i: f"VLOOKUP({mid},Plan!$B:$H,{i},FALSE)"
    add(["", "Priority", sel.get("Priority", ""), f'=IFERROR(IF({look(6)}="","",{look(6)}/100),"")', spark(f"D{mr}")], "sel", "sel|Priority")
    dropdown(mr, mr + 1, 2, [f"{r[0]} {r[1]}" for r in burn])
    input_cell(mr)
    percent(mr)
    tr = add(["", "Time used", "", f'=IFERROR(LET(s,{look(4)},e,{look(5)},a,{dmy("s")},b,{dmy("e")},MAX(0,MIN(1,(TODAY()-a)/(b-a)))),"")',
              spark(f"D{len(rows) + 1}", "#9E9E9E")], "ro", "ro")
    percent(tr)
    add(["", "Due", f'=IFERROR(LET(e,{look(5)},b,{dmy("e")},e&": "&(b-TODAY())&" days left"),IFERROR("No date ("&{look(5)}&"): set one",""))'], "ro", "ro")
    add(["", "Status", f'=IF(C{mr}="","",IF(D{mr}="","No % yet: estimate it",IF(D{tr}="","No date: set one",IF(D{mr}>=1,"Done: 1,000 pts (+4,000 if in the target week)",'
              f'IF(D{mr}+0.1<D{tr},"Behind by "&ROUND((D{tr}-D{mr})*100)&" pts","On track")))))'], "ro", "ro")
    add(["", "Next step", f'=IFERROR({look(7)},"")'], "ro", "ro")
    add([], "blank")

    # 3. Quick rewards: list 1's here-and-now and quick wins, each with its deadline
    add(["", "3. Quick rewards", "Beat the deadline; tick when done. Task points from Context; 10 for a step with no task"], "h2", "ro")
    add(["", "By", "Reward", "Pts", "Why it pays", "Task"], "th", "ro")
    q0 = len(rows) + 1
    for k in units:
        if k in ("plan:next/HERE AND NOW", "plan:next/Do now", "plan:next/Do later"):
            for kind, checked, text, ids, value in units[k]["items"]:
                if kind != "box":
                    continue
                by, rest = mp.split_deadline(text)
                key = f"reward|{text}"
                add([ticks.get(key, False), by, rest, pts_formula(ids) or 10, value, ", ".join(ids)], "item", key)
    q1 = len(rows)
    add([], "blank")

    # 4. Morning routine: 10 points a step
    morning = next((u for k, u in units.items() if k.startswith("list:morning")), None)
    m0 = len(rows) + 2
    if morning:
        add(["", "4. Morning routine", "10 pts a step; the time is the deadline"], "h2", "ro")
        for lab, text in morning["items"]:
            key = f"routine|{text}"
            add([ticks.get(key, False), lab, text, 10], "item", key)
    m1 = len(rows)
    add([], "blank")
    got = f"SUMIF(A{q0}:A{q1},TRUE,D{q0}:D{q1})+SUMIF(A{m0}:A{m1},TRUE,D{m0}:D{m1})"
    rows[score - 1][2] = f'=({got})&" pts of "&(SUM(D{q0}:D{q1})+SUM(D{m0}:D{m1}))&" on offer this morning"'
    rows[score - 1][4] = f'=SPARKLINE(({got})/MAX(1,SUM(D{q0}:D{q1})+SUM(D{m0}:D{m1})),{{"charttype","bar";"max",1;"color1","#2E7D32"}})'

    # 5-6. Decisions: tonight's for tomorrow, then the ones already made
    dec = decision_order(units.get("table:Daily decisions", {"rows": []})["rows"])
    open_ = [r for r in dec if r[2] == "To decide"]
    add(["", "5. Decide tonight (for tomorrow)", "Write 1-3 questions with a recommended answer; answer them; set Status to Decided"], "h2", "ro")
    add([""] + DASH_HEADS["Daily decisions"], "th", "thead|Daily decisions")
    d0 = len(rows) + 1
    for r in open_:
        add([""] + r, "tr", "trow|Daily decisions")
    for _ in range(2):                                   # empty slots for new questions
        add([], "tr", "trow|Daily decisions")
    add([], "blank")
    add(["", "6. Already decided", "Settled yesterday or today: no need to think again"], "h2", "ro")
    for r in dec[len(open_):]:
        add([""] + r, "tr", "trow|Daily decisions")
    d1 = len(rows)
    dropdown(d0, d1 + 1, 3, ["To decide", "Decided"])
    return {"values": rows, "fmt": fmt, "widths": [34, 150, 380, 90, 300, 260, 10], "hide": [6], "freeze": 2, "extra": extra}


def cellify(v):
    """Numbers stay numbers, formulas and percentages are parsed; other text is kept as text (no dates)."""
    if isinstance(v, (bool, int, float)) or v is None:
        return v
    v = str(v)
    if v == "" or v.startswith("=") or re.fullmatch(r"\d+%", v):
        return v
    if re.fullmatch(r"\d+", v):
        return int(v)
    return "'" + v


def format_requests(t):
    """Desktop formatting: Arial 10, wrapped text, top-aligned; navy headings; check boxes on item rows."""
    sid, values, fmt = t["sheetId"], t["values"], t["fmt"]
    ncol = max(len(t["widths"]), max(len(r) for r in values))
    nrow = len(values) + 30
    navy, pale, grey = {"red": 0.12, "green": 0.31, "blue": 0.47}, {"red": 0.91, "green": 0.94, "blue": 0.97}, {"red": 0.35, "green": 0.35, "blue": 0.35}
    rng = lambda r0, r1, c0=0, c1=ncol: {"sheetId": sid, "startRowIndex": r0, "endRowIndex": r1, "startColumnIndex": c0, "endColumnIndex": c1}
    req = [
        {"unmergeCells": {"range": {"sheetId": sid}}},
        {"updateCells": {"range": {"sheetId": sid}, "fields": "userEnteredValue,userEnteredFormat,dataValidation"}},
        {"updateSheetProperties": {"properties": {"sheetId": sid, "gridProperties": {"rowCount": nrow, "columnCount": ncol, "frozenRowCount": t.get("freeze", 1), "hideGridlines": True}},
                                   "fields": "gridProperties.rowCount,gridProperties.columnCount,gridProperties.frozenRowCount,gridProperties.hideGridlines"}},
        {"repeatCell": {"range": rng(0, nrow), "cell": {"userEnteredFormat": {"textFormat": {"fontFamily": "Arial", "fontSize": 10}, "wrapStrategy": "WRAP", "verticalAlignment": "TOP"}},
                        "fields": "userEnteredFormat.textFormat,userEnteredFormat.wrapStrategy,userEnteredFormat.verticalAlignment"}},
    ]
    if "percent_col" in t:
        c = t["percent_col"]
        req.append({"repeatCell": {"range": rng(2, nrow, c, c + 1), "cell": {"userEnteredFormat": {"numberFormat": {"type": "PERCENT", "pattern": "0%"}}},
                                   "fields": "userEnteredFormat.numberFormat"}})
    for i, w in enumerate(t["widths"]):
        req.append({"updateDimensionProperties": {"range": {"sheetId": sid, "dimension": "COLUMNS", "startIndex": i, "endIndex": i + 1},
                                                  "properties": {"pixelSize": w}, "fields": "pixelSize"}})
    for i in t.get("hide", []):
        req.append({"updateDimensionProperties": {"range": {"sheetId": sid, "dimension": "COLUMNS", "startIndex": i, "endIndex": i + 1},
                                                  "properties": {"hiddenByUser": True}, "fields": "hiddenByUser"}})
    style = {
        "title": {"textFormat": {"fontFamily": "Arial", "fontSize": 18, "bold": True, "foregroundColor": navy}},
        "h1": {"textFormat": {"fontFamily": "Arial", "fontSize": 13, "bold": True, "foregroundColor": navy}},
        "h2": {"textFormat": {"fontFamily": "Arial", "fontSize": 11, "bold": True, "foregroundColor": navy}, "backgroundColor": pale},
        "th": {"textFormat": {"fontFamily": "Arial", "fontSize": 10, "bold": True, "foregroundColor": {"red": 1, "green": 1, "blue": 1}}, "backgroundColor": navy},
        "note": {"textFormat": {"fontFamily": "Arial", "fontSize": 9, "italic": True, "foregroundColor": grey}},
        "ro": {"textFormat": {"fontFamily": "Arial", "fontSize": 10, "foregroundColor": grey}},
        "score": {"textFormat": {"fontFamily": "Arial", "fontSize": 14, "bold": True, "foregroundColor": {"red": 0.18, "green": 0.49, "blue": 0.2}}},
        "sel": {"textFormat": {"fontFamily": "Arial", "fontSize": 11, "bold": True}},
    }
    runs, i = [], 0
    while i < len(fmt):  # merge neighbouring rows of the same kind into one request
        j = i
        while j + 1 < len(fmt) and fmt[j + 1] == fmt[i]:
            j += 1
        runs.append((fmt[i], i, j + 1))
        i = j + 1
    for kind, a, b in runs:
        if kind in style:
            f = style[kind]
            fields = ",".join("userEnteredFormat." + k for k in f)
            req.append({"repeatCell": {"range": rng(a, b), "cell": {"userEnteredFormat": f}, "fields": fields}})
        if kind == "item":
            req.append({"setDataValidation": {"range": rng(a, b, 0, 1), "rule": {"condition": {"type": "BOOLEAN"}}}})
    return req


def sheet_ticks(snapshot):
    """{(tab, list, text): ticked} so a re-render keeps today's ticks on the list tabs."""
    out = {}
    for tab in ("Regular lists", "Updateable lists"):
        cur = None
        for r in snapshot.get(tab, []):
            r = (r + ["", "", ""])[:3]
            if r[0] not in ("TRUE", "FALSE") and r[1]:
                cur = re.sub(r"\s*\(.*\)$", "", r[1]).strip().lower()
                if tab == "Regular lists":
                    cur = r[1].strip().lower()
            elif cur:
                text = r[2]
                out[(tab, cur, text)] = r[0] == "TRUE"
    return out


# ====================================================================== the Sheet: parse a snapshot

def sheet_units(snap, repo):
    """Turn a Sheet snapshot back into units, in the same shape as repo_units()."""
    units = {}
    # Plan tab: column I holds the key of each row
    for r in snap.get("Plan", []):
        r = [norm(c) for c in (r + [""] * 9)[:9]]
        key = r[8]
        if key.startswith("sec|"):
            _, k, head = key.split("|", 2)
            u = units.setdefault(k, {"head": head, "title": None, "items": []})
            tail = r[4]
            base = re.sub(r"\s*\(.*\)$", "", head.lstrip("# ").strip())
            if not k.endswith("/NEXT STEP"):
                hashes = "# " if head.startswith("# ") else ""
                u["head"] = f"{hashes}{base}" + (f" ({tail})" if tail else "")
            else:
                u["title"] = r[1] or None
        elif key.startswith("title|"):
            units[key.split("|", 1)[1]]["title"] = r[1] or None
        elif key.startswith("item|"):
            _, k, kind = key.split("|", 2)
            ids = [i.strip() for i in re.split(r"[,;\s]+", r[2]) if ID_RE.fullmatch(i.strip())]
            units[k]["items"].append([kind, r[0] == "TRUE", r[1], ids, r[4]])
        elif key.startswith("thead|"):
            sec = key.split("|", 1)[1]
            units[f"table:{sec}"] = {"head": [c for c in r[1:8] if c], "rows": []}
        elif key.startswith("trow|"):
            sec = key.split("|", 1)[1]
            u = units[f"table:{sec}"]
            u["rows"].append(r[1:1 + len(u["head"])])
    # Context tab
    sec = None
    heads = {h: s for h, s in CONTEXT_SECTIONS}
    for r in snap.get("Context", [])[2:]:
        r = [norm(c) for c in (r + [""] * 9)[:9]]
        if r[0] in heads:
            sec = heads[r[0]]
        elif sec and r[0]:
            row = [r[0], r[1], r[3], r[5], r[7], r[8]] if sec == "Projects" else r
            units[f"task:{row_key(row)}"] = {"section": sec, "row": row}
    # Regular lists
    cur = None
    for r in snap.get("Regular lists", [])[1:]:
        r = [norm(c) for c in (r + ["", "", ""])[:3]]
        if r[0] not in ("TRUE", "FALSE") and r[1]:
            name = r[1].lower()
            repo_name = repo.get(f"list:{name}", {}).get("name") or r[1].capitalize()
            cur = units[f"list:{name}"] = {"name": repo_name, "items": []}
        elif cur is not None and (r[1] or r[2]):
            cur["items"].append([r[1], r[2]])
    # Updateable lists -> Lists by place and Task scripts tables
    place = {v.lower(): k for k, v in PLACE_TITLES.items()}
    cur, places, scripts = None, [], []
    for r in snap.get("Updateable lists", [])[1:]:
        r = [norm(c) for c in (r + ["", "", "", ""])[:4]]
        if r[0] not in ("TRUE", "FALSE") and r[1]:
            cur = "scripts" if r[1].startswith("TASK SCRIPTS") else place.get(r[1].lower(), r[1].title())
        elif cur == "scripts" and (r[1] or r[2]):
            scripts.append([r[1], r[2]])
        elif cur and (r[1] or r[2]):
            places.append([cur, r[2], r[1]])
    if snap.get("Updateable lists"):
        units["table:Lists by place"] = {"head": ["List", "Item", "Task"], "rows": places}
        units["table:Task scripts"] = {"head": ["Script", "What to do"], "rows": scripts}
    # Dashboard: the two pickers and the daily decisions (column G holds the row keys)
    if snap.get("Dashboard"):
        sel, dec = [], []
        for r in snap["Dashboard"]:
            r = [norm(c) for c in (r + [""] * 7)[:7]]
            if r[6].startswith("sel|"):
                sel.append([r[6][4:], r[2]])
            elif r[6] == "trow|Daily decisions" and any(r[1:6]):
                row = r[1:6]
                if row[1] and not row[2]:
                    row[2] = "To decide"
                dec.append(row)
        units["table:Dashboard selections"] = {"head": DASH_HEADS["Dashboard selections"], "rows": sel}
        units["table:Daily decisions"] = {"head": DASH_HEADS["Daily decisions"], "rows": dec}
    return units


# ====================================================================== sync

def comparable(k, u):
    """What counts as a change: ignore cosmetic differences the round trip cannot keep."""
    if u is None:
        return None
    if k.startswith("plan:"):
        return {"head": norm(u["head"]), "title": norm(u.get("title")),
                "items": [[it[0], bool(it[1]), norm(it[2]), list(it[3]), norm(it[4])] for it in u["items"]]}
    if k == "table:Daily decisions":
        return {"rows": sorted([norm(c) for c in r] for r in u["rows"])}
    if k.startswith("table:"):
        return {"rows": [[norm(c) for c in r] for r in u["rows"]]}
    return u


def load_state():
    return json.loads(STATE.read_text()) if STATE.exists() else {"units": {}, "printable": {}}


def sync(snapshot_path, apply):
    state = load_state()
    base = state["units"]
    repo = repo_units()
    snap = json.loads(Path(snapshot_path).read_text())
    # the Dashboard may be missing only before its first write (nothing of it agreed yet)
    missing = [t for t in SHEET_IDS if not snap.get(t)
               and not (t == "Dashboard" and not any(f"table:{d}" in base for d in DASH_TABLES))]
    if missing:
        print(f"The snapshot has no rows for {', '.join(missing)}: read all the synced tabs first (a missing tab "
              "would look like everything on it was deleted).", file=sys.stderr)
        return 4
    sheet = sheet_units(snap, repo)
    keys = sorted(set(repo) | set(sheet) | set(base))
    take_sheet, take_repo, conflicts = {}, [], []
    for k in keys:
        r, s = comparable(k, repo.get(k)), comparable(k, sheet.get(k))
        rh, sh, bh = digest(r) if r is not None else None, digest(s) if s is not None else None, base.get(k)
        if rh == sh:
            continue
        if bh is None and rh is None:
            take_sheet[k] = sheet[k]          # added on the Sheet
        elif bh is None and sh is None:
            take_repo.append(k)               # added in the repo
        elif rh == bh:
            take_sheet[k] = sheet.get(k)      # changed (or deleted) on the Sheet only
        elif sh == bh:
            take_repo.append(k)               # changed (or deleted) in the repo only
        else:
            conflicts.append({"unit": k, "repo": r, "sheet": s})
    report = {"from_sheet": sorted(take_sheet), "from_repo": take_repo, "conflicts": conflicts}
    print(json.dumps(report, indent=1, ensure_ascii=False))
    if conflicts:
        print(f"\n{len(conflicts)} conflict(s): both sides changed. Nothing applied; ask Stephen which to keep.", file=sys.stderr)
        return 2
    if apply and take_sheet:
        merged = dict(repo)
        for k, u in take_sheet.items():
            if u is None:
                merged.pop(k, None)
            else:
                merged[k] = u
        for k, u in take_sheet.items():
            if k.startswith("plan:") and u is not None:
                write_plan_unit(k, u)
        if any(k.startswith(("task:", "table:")) for k in take_sheet):
            write_task_tables(merged)
        if any(k.startswith("list:") for k in take_sheet):
            write_routines({k: v for k, v in merged.items() if k.startswith("list:")})
        print(f"Applied {len(take_sheet)} Sheet-side change(s) to the repo.", file=sys.stderr)
    return 0


def baseline():
    state = load_state()
    state["units"] = {k: digest(comparable(k, u)) for k, u in repo_units().items()}
    state["synced"] = dt.datetime.now().isoformat(timespec="seconds")
    STATE.write_text(json.dumps(state, indent=1, sort_keys=True) + "\n")
    print(f"Baseline recorded: {len(state['units'])} units.")


# ====================================================================== printable and checks

def sources_hash():
    return digest([file_hash(p) for p in PRINT_SOURCES])


def build(force, date):
    state = load_state()
    pr = state.get("printable", {})
    if mp.OUT.exists() and pr.get("docx") and file_hash(mp.OUT) != pr["docx"] and not force:
        print(f"{mp.OUT.name} was changed by hand since the last build. That edit is the master: fold it into "
              "the sources or the layout (Scripts/make_printable.py), then run build --force.", file=sys.stderr)
        return 3
    today = dt.date.fromisoformat(date) if date else dt.date.today()
    out, heads = mp.build(today)
    pages = mp.page_numbers(out, heads)
    if pages:
        mp.build(today, pages)
    mp.ARCHIVE.mkdir(parents=True, exist_ok=True)
    (mp.ARCHIVE / f"{mp.OUT.stem}_v{mp.VERSION}.docx").write_bytes(out.read_bytes())
    state["printable"] = {"docx": file_hash(out), "sources": sources_hash(), "version": mp.VERSION, "built": today.isoformat()}
    STATE.write_text(json.dumps(state, indent=1, sort_keys=True) + "\n")
    print(f"Built {out.name} (v{mp.VERSION}){'' if pages else ' without contents page numbers (no soffice)'}.")
    return 0


def check():
    errors, warnings = [], []
    text = TASKS.read_text()
    tables = mp.md_tables(text)
    ids = []
    for _, sec in CONTEXT_SECTIONS:
        ids += [r["ID"] for r in tables.get(sec, []) if r.get("ID") not in ("", "-", None)]
    dup = sorted({i for i in ids if ids.count(i) > 1})
    if dup:
        errors.append(f"Duplicate IDs in the task file: {', '.join(dup)}")
    known = set(ids)
    for path in (NEXT, DAYWEEK):
        for i in set(ID_RE.findall(path.read_text())):
            if i not in known:
                errors.append(f"{path.name} names {i}, which is not in the task file")
    for r in tables.get("Lists by place", []):
        if r.get("Task") and r["Task"] not in known:
            errors.append(f"Lists by place item '{r['Item']}' names unknown task {r['Task']}")
        if len(r) != 3:
            errors.append(f"Lists by place row has the wrong number of columns: {r.get('Item')}")
    for doc in (ROOT / "README.md", ROOT / "AGENTS.md", ROOT / "NORMS.md", TASKS, ROOT / "Context" / "routines.md"):
        for ref in re.findall(r"`([^`*<>]+\.(?:md|txt|docx|py|xlsx|pptx|url|bat|json))`", doc.read_text(encoding="utf-8-sig")):
            if not (ROOT / ref).exists() and not (REPO / ref).exists() and not list(REPO.glob(f"**/{Path(ref).name}")):
                errors.append(f"{doc.relative_to(REPO)} refers to `{ref}`, which does not exist")
    if list(PLANS.glob("Me-Printable-Tracker_v*.docx")):
        errors.append("A versioned printable is in 1 Day and Week Plans; versions belong in 3 Archive/Printable versions/")
    state = load_state()
    pr = state.get("printable", {})
    if not mp.OUT.exists():
        errors.append(f"{mp.OUT.name} is missing: run Scripts/update.py build")
    elif pr.get("docx") and file_hash(mp.OUT) != pr["docx"]:
        warnings.append(f"{mp.OUT.name} was edited by hand: fold the edit into the sources, then build --force")
    elif pr.get("sources") and pr["sources"] != sources_hash():
        warnings.append(f"{mp.OUT.name} is older than its sources: run Scripts/update.py build")
    if state.get("units"):
        changed = [k for k, u in repo_units().items() if state["units"].get(k) != digest(comparable(k, u))]
        if changed:
            warnings.append(f"{len(changed)} repo unit(s) changed since the last Sheet sync (e.g. {', '.join(changed[:4])}): sync the Sheet")
    for w in warnings:
        print("WARNING:", w)
    for e in errors:
        print("ERROR:", e)
    print("OK" if not errors else f"{len(errors)} error(s)")
    return 1 if errors else 0


# ====================================================================== end of day: done anywhere = done everywhere

def _n(text):
    """Normalise item text for matching: no day prefix, no IDs, lower case."""
    t = mp.strip_ids(text or "").lower()
    t = re.sub(r"^(mon|tue|wed|thu|fri|sat|sun)( \d+(am|pm))?:\s*", "", t)
    t = re.sub(r"^(by [^:]{1,15}|any time[^:]*):\s*", "", t)
    t = re.sub(r"^(ask ai|get ai)( to)?:?\s*", "", t)
    return re.sub(r"[^a-z0-9 ]+", " ", t).split() and " ".join(re.sub(r"[^a-z0-9 ]+", " ", t).split())


def same_item(a, b):
    import difflib
    a, b = _n(a), _n(b)
    if not a or not b:
        return False
    return a == b or a.startswith(b) or b.startswith(a) or difflib.SequenceMatcher(None, a, b).ratio() >= 0.9


def matches_task(text, title):
    import difflib
    a, b = _n(text), _n(re.sub(r"^[^:]*priority:\s*", "", title, flags=re.I))
    return bool(a and b) and (a == b or a in b or b in a or difflib.SequenceMatcher(None, a, b).ratio() >= 0.75)


TRACKER_GRID = (8, 14)            # rows 9-14 (0-based 8..13): the week's goal tasks
TRACKER_COLS = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]   # (text, tick) per goal
TRACKER_MS = (19, 38)             # rows 20-38: milestones, then the two habits
HABITS = [
    ["Habit", "Rest: 2 rest days this week", '=IFERROR(MIN(1,VALUE(SUBSTITUTE(INDEX(E54:E119,MATCH("Week of "&TEXT(TODAY()-WEEKDAY(TODAY(),3),"d mmm"),A54:A119,0))," rest",""))/2),0)', "Weekly", "Tick Rest day in the daily tracker"],
    ["Habit", "Health: gym 3 times this week", '=IFERROR(MIN(1,VALUE(SUBSTITUTE(INDEX(D54:D119,MATCH("Week of "&TEXT(TODAY()-WEEKDAY(TODAY(),3),"d mmm"),A54:A119,0))," gym",""))/3),0)', "Weekly", "Log gym minutes in the daily tracker"],
]


def end_of_day(snapshot_path, date, apply):
    """Delete everything that is done, wherever it was ticked, and record it once in Recently completed.

    Done = ticked on the Plan tab, the Dashboard, the Updateable lists tab or the Tracker's week grid, or a task or
    milestone whose status starts with 'Done'. A ticked item is removed everywhere the same item
    appears; a task is done when a ticked item names it or when nothing of it is left open. Ticks on
    Regular lists are reset (the lists recur). Points already scored on the Tracker are banked."""
    today = dt.date.fromisoformat(date) if date else dt.date.today()
    day = f"Done {today.day} {today.strftime('%b')}"
    snap = json.loads(Path(snapshot_path).read_text())
    units = repo_units()
    tasks = {k[5:]: u for k, u in units.items() if k.startswith("task:")}
    active = {i: u for i, u in tasks.items() if u["section"] == "Active tasks"}
    title = {i: u["row"][1] for i, u in active.items()}
    ticked, report = [], []           # ticked: (text, ids, where)

    for k, u in units.items():
        if k.startswith("plan:") and not k.endswith("/DONE"):
            for it in u["items"]:
                if it[0] == "box" and it[1]:
                    ticked.append((it[2], it[3], k))
    for (tab, lst, text), on in sheet_ticks(snap).items():
        if on and tab == "Updateable lists":
            ticked.append((text, [], f"{tab}/{lst}"))
    for r in snap.get("Dashboard", []):
        r = (r + [""] * 7)[:7]
        if r[0] == "TRUE" and r[6].startswith("reward|"):
            ticked.append((r[6][7:], ID_RE.findall(r[5]), "Dashboard"))
    grid = [(r + [""] * 11)[:11] for r in snap.get("Tracker", [])[TRACKER_GRID[0]:TRACKER_GRID[1]]]
    banked_tasks = 0
    pts_each = [(snap.get("Tracker", [[]] * 8)[7] + [""] * 11)[c] for c, _ in TRACKER_COLS] if len(snap.get("Tracker", [])) > 7 else ["100"] * 5
    for r in grid:
        for g, (c, t) in enumerate(TRACKER_COLS):
            if r[c] and r[t] == "TRUE":
                ticked.append((r[c], [], "Tracker"))
                banked_tasks += int((re.findall(r"\d+", norm(pts_each[g])) or [100])[0])   # e.g. "100 pts each"

    # which tasks are done
    done = {i for i, u in active.items() if u["row"][5].startswith("Done")}
    places = units["table:Lists by place"]["rows"]
    for text, ids, where in ticked:
        for i in (ids or [i for i in active if matches_task(text, title[i])]):
            if i in active and matches_task(text, title[i]):
                done.add(i)
    removed_places = [r for r in places if any(same_item(r[1], t) for t, _, _ in ticked) or r[2] in done]
    left_places = [r for r in places if r not in removed_places]
    for i in {r[2] for r in removed_places} - done:      # every list item of a task ticked: the task is done
        if i in active and not any(r[2] == i for r in left_places):
            done.add(i)
    left_places = [r for r in left_places if r[2] not in done]

    # milestones whose status is Done
    ms_done = {i for i, u in tasks.items() if u["section"].startswith("Milestones") and (u["row"][5].startswith("Done") or u["row"][6] == "100%")}
    due_of = {r[0]: mp.parse_date(r[4]) for r in units["table:Milestones (burndown)"]["rows"]}
    ms_points = {i: int(norm(tasks[i]["row"][2]) or 1000)
                 + (4000 if due_of.get(i) and due_of[i].isocalendar()[:2] == today.isocalendar()[:2] else 0) for i in ms_done}   # +4000 if done in the target week

    def gone(text, ids):
        return any(same_item(text, t) for t, _, _ in ticked) or (ids and all(i in done for i in ids))

    # plan sections: drop done items; empty the DONE sections
    for k, u in units.items():
        if k.startswith("plan:"):
            keep = [] if k.endswith("/DONE") else [it for it in u["items"] if not (it[1] or gone(it[2], it[3]))]
            if keep != u["items"]:
                report.append(f"{k[5:]}: removed {len(u['items']) - len(keep)} item(s)")
                u["items"] = keep
    units["table:Lists by place"]["rows"] = left_places
    if removed_places:
        report.append(f"Lists by place: removed {', '.join(r[1] for r in removed_places)}")
    scripts = units["table:Task scripts"]["rows"]
    units["table:Task scripts"]["rows"] = [r for r in scripts if not any(same_item(r[0], t) or same_item(r[1], t) for t, _, _ in ticked)]

    # move done tasks and milestones to Recently completed; drop rows older than 14 days
    for i in sorted(done):
        row = list(active[i]["row"])
        row[5], row[6] = row[5] if row[5].startswith("Done") else day, "100%"
        tasks[i] = units[f"task:{i}"] = {"section": "Recently completed (last 14 days)", "row": row}
        report.append(f"{i} {row[1]}: done, moved to Recently completed")
    for i in sorted(ms_done):
        row = list(units[f"task:{i}"]["row"])
        status = row[5] if row[5].startswith("Done") else day
        units[f"task:{i}"] = {"section": "Recently completed (last 14 days)", "row": [row[0], row[1], row[2], row[3], "", status, "100%", row[7], row[8]]}
        report.append(f"{i} {row[1]}: milestone done ({ms_points[i]} pts incl. any target-week bonus), moved to Recently completed")
    for k, u in list(units.items()):
        if k.startswith("task:") and u["section"].startswith("Recently"):
            m = re.match(r"Done (\d+) (\w{3})", u["row"][5])
            if m:
                when = dt.datetime.strptime(f"{m.group(1)} {m.group(2)} {today.year}", "%d %b %Y").date()
                if (today - when).days > 14:
                    report.append(f"{u['row'][0]} {u['row'][1]}: completed over 14 days ago, deleted")
                    del units[k]
    burn = units["table:Milestones (burndown)"]
    burn["rows"] = [r for r in burn["rows"] if r[0] not in ms_done and norm(r[5]) != "100"]
    daily = units.get("table:Daily decisions")
    if daily:
        def old(r):
            m = re.match(r"(\d+) (\w{3})", r[0])
            return bool(m) and dt.datetime.strptime(f"{m.group(1)} {m.group(2)} {today.year}", "%d %b %Y").date() < today
        before = len(daily["rows"])
        daily["rows"] = [r for r in daily["rows"] if r[2] == "To decide" or not old(r)]
        if len(daily["rows"]) != before:
            report.append(f"Daily decisions: removed {before - len(daily['rows'])} decided before today")
    dec = units["table:Key decisions"]
    before = len(dec["rows"])
    dec["rows"] = [r for r in dec["rows"] if r[2] != "Closed"]
    if len(dec["rows"]) != before:
        report.append(f"Key decisions: removed {before - len(dec['rows'])} closed")
    for k, u in units.items():                           # projects no longer list done milestones
        if k.startswith("task:") and u["section"] == "Projects":
            ms = [m.strip() for m in u["row"][4].split(",")]
            if any(m in ms_done for m in ms):
                u["row"][4] = ", ".join(m for m in ms if m not in ms_done)

    # the Tracker: compact the week grid (ticked tasks banked), milestones from the burndown table
    cols = []
    for c, t in TRACKER_COLS:
        items = [r[c] for r in grid if r[c] and r[t] != "TRUE" and not any(same_item(r[c], x) for x, _, w in ticked if w != "Tracker")]
        items = [x for x in items if not any(same_item(x, title[i]) for i in done)]
        cols.append(items + [""] * (len(grid) - len(items)))
    row17 = (snap.get("Tracker", []) + [[]] * 17)[16] + [""] * 5
    prev_t = int(norm(row17[1]) or 0) if norm(row17[1]).isdigit() else 0
    prev_m = int(norm(row17[4]) or 0) if norm(row17[4]).isdigit() else 0
    tracker = {"banked_tasks": prev_t + banked_tasks, "banked_milestones": prev_m + sum(ms_points.values()), "grid": cols,
               "milestones": [r for r in burn["rows"]]}
    out = {"done_tasks": sorted(done), "done_milestones": sorted(ms_done), "ticked": [t for t, _, _ in ticked],
           "tracker_banked": {"tasks": banked_tasks, "milestones": sum(ms_points.values())}, "changes": report}
    print(json.dumps(out, indent=1, ensure_ascii=False))
    if apply:
        for k, u in units.items():
            if k.startswith("plan:"):
                write_plan_unit(k, u)
        write_task_tables(units)
        (ROOT / "Context" / ".eod-tracker.json").write_text(json.dumps(tracker, indent=1, ensure_ascii=False))
        print("Applied to the repo. Next: render (it includes the Tracker ranges), write the Sheet, baseline.", file=sys.stderr)
    return 0


def tracker_ranges(eod=None):
    """Tracker ranges kept in step with the repo: milestones (from the burndown table, % looked up
    from the Plan tab) and, after an end of day, the compacted week grid and banked points."""
    units = repo_units()
    burn = units.get("table:Milestones (burndown)", {"rows": []})["rows"]
    rows = []
    for r in sorted(burn, key=lambda r: r[2] != "Personal"):
        n = TRACKER_MS[0] + len(rows) + 1
        rows.append([r[2], f"{r[0]} {r[1]}", f'=IFERROR(IF(VLOOKUP("{r[0]}",Plan!$B:$G,6,FALSE)="","",VLOOKUP("{r[0]}",Plan!$B:$G,6,FALSE)/100),"")',
                     f'=IF(C{n}="","",SPARKLINE(C{n},{{"charttype","bar";"max",1;"color1","{"#2E7D32" if r[2] == "Personal" else "#1F4E79"}"}}))',
                     r[4], r[6]])
    for h in HABITS:
        n = TRACKER_MS[0] + len(rows) + 1
        rows.append([h[0], h[1], h[2], f'=IF(C{n}="","",SPARKLINE(C{n},{{"charttype","bar";"max",1;"color1","#2E7D32"}}))', h[3], h[4]])
    size = TRACKER_MS[1] - TRACKER_MS[0]
    if len(rows) > size:
        raise SystemExit(f"Tracker has room for {size} milestone rows, the burndown has {len(rows)}: add rows on the Tracker first")
    rows += [[""] * 6] * (size - len(rows))
    out = [{"range": f"Tracker!A{TRACKER_MS[0] + 1}:F{TRACKER_MS[1]}", "values": rows},
           {"range": "Tracker!B4", "values": [["=MAX(J54:J119)+1000*COUNTIFS(A20:A38,\"<>Habit\",C20:C38,\">=1\")+N(E17)"]]},
           {"range": "Tracker!B16", "values": [["=B15+D15+F15+H15+J15+N(B17)"]]}]
    if eod:
        grid = []
        for i in range(TRACKER_GRID[1] - TRACKER_GRID[0]):
            row = []
            for col in eod["grid"]:
                row += [col[i], False]
            grid.append(row)
        out.append({"range": f"Tracker!B{TRACKER_GRID[0] + 1}:K{TRACKER_GRID[1]}", "values": grid})
        out.append({"range": "Tracker!A17:E17", "values": [["Banked: tasks this week", eod["banked_tasks"], "", "Banked: milestones", eod["banked_milestones"]]]})
    return out


def check_sheet(snapshot_path):
    """Consistency inside the Sheet and between the Sheet and the repo."""
    snap = json.loads(Path(snapshot_path).read_text())
    repo = repo_units()
    sheet = sheet_units(snap, repo)
    problems = []
    active = {u["row"][0] for u in sheet.values() if isinstance(u, dict) and u.get("section") == "Active tasks"}
    for k, u in sheet.items():
        if k.startswith("plan:"):
            for it in u["items"]:
                for i in it[3]:
                    if i not in active:
                        problems.append(f"Plan {k[5:]}: '{it[2]}' names {i}, which is not an active task")
                if it[1] and not k.endswith("/DONE"):
                    problems.append(f"Plan {k[5:]}: '{it[2]}' is ticked: run the end of day to clear it everywhere")
    for r in sheet.get("table:Lists by place", {"rows": []})["rows"]:
        if r[2] and r[2] not in active:
            problems.append(f"Updateable lists: '{r[1]}' names {r[2]}, which is not an active task")
    burn = {r[0]: r for r in sheet.get("table:Milestones (burndown)", {"rows": []})["rows"]}
    for k, u in sheet.items():
        if k.startswith("task:") and u["section"].startswith("Milestones"):
            i, pct = u["row"][0], u["row"][6]
            if i in burn:
                want = f"{burn[i][5]}%" if burn[i][5] else "?"
                if norm(pct) != want:
                    problems.append(f"Context {i} shows {pct}, the Plan burndown shows {want}")
            elif u["row"][5].startswith("Done"):
                pass
            if u["row"][5].startswith("Done") or pct == "100%":
                problems.append(f"Context {i} is done: run the end of day to move it to Recently completed")
        if k.startswith("task:") and u["section"] == "Active tasks" and u["row"][5].startswith("Done"):
            problems.append(f"Context {u['row'][0]} is marked done but still active: run the end of day")
    for r in sheet.get("table:Key decisions", {"rows": []})["rows"]:
        if len(r) > 2 and r[2] == "Closed":
            problems.append(f"Key decision closed but not cleared: {r[1]}")
    tr = [(r + [""] * 11)[:11] for r in snap.get("Tracker", [])]
    plan_ticked = {it[2] for k, u in sheet.items() if k.startswith("plan:") for it in u["items"] if it[1]}
    plan_open = [it[2] for k, u in sheet.items() if k.startswith("plan:") and not k.endswith("/DONE") for it in u["items"] if not it[1]]
    for r in tr[TRACKER_GRID[0]:TRACKER_GRID[1]]:
        for c, t in TRACKER_COLS:
            if r[c] and r[t] == "TRUE":
                if any(same_item(r[c], x) for x in plan_open):
                    problems.append(f"Tracker: '{r[c]}' is ticked but still open on the Plan tab")
            elif r[c] and any(same_item(r[c], x) for x in plan_ticked):
                problems.append(f"Tracker: '{r[c]}' is open but ticked on the Plan tab")
    for r in tr[TRACKER_MS[0]:TRACKER_MS[1]]:
        m = re.match(r"^(\S+_m\d|SP\d)\s", r[1] or "")
        if m and m.group(1) in burn:
            want = f"{burn[m.group(1)][5]}%" if burn[m.group(1)][5] else ""
            if norm(r[2]) != want:
                problems.append(f"Tracker {m.group(1)} shows {r[2] or 'blank'}, the burndown shows {want or 'blank'}")
    diff = [k for k in set(repo) | set(sheet) if digest(comparable(k, repo.get(k))) != digest(comparable(k, sheet.get(k)))]
    for k in sorted(diff):
        problems.append(f"Repo and Sheet differ: {k} (run sync)")
    for p_ in problems:
        print("-", p_)
    print("Sheet consistent" if not problems else f"{len(problems)} issue(s)")
    return 1 if problems else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("sync"); s.add_argument("--snapshot", required=True); s.add_argument("--apply", action="store_true")
    b = sub.add_parser("build"); b.add_argument("--force", action="store_true"); b.add_argument("--date")
    r = sub.add_parser("render"); r.add_argument("--out", required=True); r.add_argument("--snapshot"); r.add_argument("--date")
    sub.add_parser("baseline")
    sub.add_parser("check")
    e = sub.add_parser("eod"); e.add_argument("--snapshot", required=True); e.add_argument("--date"); e.add_argument("--apply", action="store_true")
    c = sub.add_parser("check-sheet"); c.add_argument("--snapshot", required=True)
    a = ap.parse_args()
    if a.cmd == "sync":
        return sync(a.snapshot, a.apply)
    if a.cmd == "build":
        return build(a.force, a.date)
    if a.cmd == "render":
        snap = json.loads(Path(a.snapshot).read_text()) if a.snapshot else None
        today = dt.date.fromisoformat(a.date) if a.date else None
        Path(a.out).write_text(json.dumps(render(repo_units(), snap, today), ensure_ascii=False, indent=1))
        print(f"Wrote {a.out}")
        return 0
    if a.cmd == "eod":
        return end_of_day(a.snapshot, a.date, a.apply)
    if a.cmd == "check-sheet":
        return check_sheet(a.snapshot)
    if a.cmd == "baseline":
        baseline()
        return 0
    return check()


if __name__ == "__main__":
    sys.exit(main())
