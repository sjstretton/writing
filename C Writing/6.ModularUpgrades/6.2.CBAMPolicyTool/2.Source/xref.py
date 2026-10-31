"""Resolve Quarto-style cross-references (@sec-, @fig-, @tbl-, @eq-) for plain pandoc.
Usage: python3 xref.py in.qmd out.md"""
import re, sys

src = open(sys.argv[1]).read()
lines = src.split("\n")
num = {}
h1 = h2 = 0
fig = tbl = eq = 0
in_yaml = False
for i, ln in enumerate(lines):
    if i == 0 and ln.strip() == "---":
        in_yaml = True
        continue
    if in_yaml:
        if ln.strip() == "---":
            in_yaml = False
        continue
    m = re.match(r"^(#{1,2}) (.*?)\s*(\{[^}]*\})?\s*$", ln)
    if m:
        attrs = m.group(3) or ""
        if "unnumbered" in attrs:
            continue
        if len(m.group(1)) == 1:
            h1 += 1; h2 = 0; label = str(h1)
        else:
            h2 += 1; label = f"{h1}.{h2}"
        idm = re.search(r"#(sec-[\w-]+)", attrs)
        if idm:
            num[idm.group(1)] = ("Section", label)
        continue
    for idm in re.finditer(r"\{#(fig-[\w-]+)[^}]*\}", ln):
        fig += 1; num[idm.group(1)] = ("Figure", str(fig))
    m = re.match(r"^:\s.*\{#(tbl-[\w-]+)\}\s*$", ln)
    if m:
        tbl += 1; num[m.group(1)] = ("Table", str(tbl))
    m = re.match(r"^\$\$\s*\{#(eq-[\w-]+)\}\s*$", ln)
    if m:
        eq += 1; num[m.group(1)] = ("equation", f"({eq})")

out = []
for ln in lines:
    m = re.match(r"^\$\$\s*\{#(eq-[\w-]+)\}\s*$", ln)
    if m:
        # put the number inside the display math, before the closing $$
        k = len(out) - 1
        out[k] = out[k] + r" \qquad " + num[m.group(1)][1]
        out.append("$$")
        continue
    m = re.match(r"^(:\s)(.*?)\s*\{#(tbl-[\w-]+)\}\s*$", ln)
    if m:
        out.append(f": Table {num[m.group(3)][1]}. {m.group(2)}")
        continue
    m = re.match(r"^(!\[)(.*)(\]\(.*\))\{#(fig-[\w-]+)([^}]*)\}\s*$", ln)
    if m:
        w = re.search(r"width=[\w%.]+", m.group(5))
        out.append(f"{m.group(1)}Figure {num[m.group(4)][1]}. {m.group(2)}{m.group(3)}" + ("{" + w.group(0) + "}" if w else ""))
        continue
    out.append(ln)
text = "\n".join(out)


def rep(m):
    key = m.group(2)
    if key not in num:
        sys.stderr.write(f"unresolved {key}\n")
        return m.group(0)
    kind, lab = num[key]
    pre = m.group(1)
    return f"{pre}{kind} {lab}" if kind != "equation" else f"{pre}equation {lab}"


text = re.sub(r"(^|[^\w@])@((?:sec|fig|tbl|eq)-[\w-]+)", rep, text, flags=re.M)
# inside brackets like [@sec-x] leave as plain text: remove the brackets' citation semantics
text = re.sub(r"\[(Section|Figure|Table|equation) ([\d.()]+)\]", r"\1 \2", text)
open(sys.argv[2], "w").write(text)
