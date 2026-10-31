"""Render a Quarto .qmd to .docx with plain pandoc (Quarto is not installed).

Quarto cross-references (@sec-, @tbl-, @fig-, @eq-) are resolved to numbers
before pandoc runs, so the docx shows "Section 4", "Table 2", "equation (3)".
The .qmd stays the master and still renders correctly under Quarto.

Usage:  python3 render.py <file.qmd> <file.bib> <style.csl>
Run from anywhere; pandoc runs in the qmd's folder so figure paths resolve.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path


def resolve(text: str) -> str:
    head, body = text.split("\n---\n", 1) if text.startswith("---") else ("", text)
    numbered = "number-sections: true" in head
    labels = {}
    # sections
    out, sec, sub = [], 0, 0
    for line in body.split("\n"):
        m = re.match(r"^(#{1,2}) (.*?)(\s*\{(.*)\})?\s*$", line)
        if m and numbered:
            level, title, attrs = len(m.group(1)), m.group(2), m.group(4) or ""
            unnum = ".unnumbered" in attrs
            ident = re.search(r"#(sec-[\w-]+)", attrs)
            if not unnum:
                if level == 1:
                    sec, sub = sec + 1, 0
                    num = f"{sec}"
                else:
                    sub += 1
                    num = f"{sec}.{sub}"
                if ident:
                    labels[ident.group(1)] = f"Section {num}"
                line = f"{m.group(1)} {num} {title}" + (" {.unnumbered}")
            else:
                if ident:
                    labels[ident.group(1)] = title.split(":")[0]
                line = f"{m.group(1)} {title} {{.unnumbered}}"
        out.append(line)
    body = "\n".join(out)
    # tables: caption lines ": text {#tbl-x}"
    n = 0
    def tbl(m):
        nonlocal n
        n += 1
        labels[m.group(2)] = f"Table {n}"
        return f": Table {n}. {m.group(1)}"
    body = re.sub(r"^: (.*?) \{#(tbl-[\w-]+)\}\s*$", tbl, body, flags=re.M)
    # figures: ![caption](path){#fig-x}
    n = 0
    def fig(m):
        nonlocal n
        n += 1
        labels[m.group(3)] = f"Figure {n}"
        return f"![Figure {n}. {m.group(1)}]({m.group(2)})"
    body = re.sub(r"!\[(.*?)\]\((.*?)\)\{#(fig-[\w-]+)\}", fig, body, flags=re.S)
    # equations: $$ ... $$ {#eq-x}
    n = 0
    def eq(m):
        nonlocal n
        n += 1
        labels[m.group(2)] = f"equation ({n})"
        return f"$${m.group(1)} \\qquad ({n})$$"
    body = re.sub(r"\$\$(.*?)\$\$\s*\{#(eq-[\w-]+)\}", eq, body, flags=re.S)
    # references
    def ref(m):
        key = m.group(1)
        return labels.get(key, m.group(0))
    body = re.sub(r"@((?:sec|tbl|fig|eq)-[\w-]+)", ref, body)
    head = head.replace("number-sections: true", "number-sections: false")
    return (head + "\n---\n" + body) if head else body


def main():
    qmd, bib, csl = (Path(a).resolve() for a in sys.argv[1:4])
    text = resolve(qmd.read_text())
    with tempfile.NamedTemporaryFile("w", suffix=".md", dir=qmd.parent, delete=False) as tmp:
        tmp.write(text)
    try:
        cmd = ["pandoc", tmp.name, "-f", "markdown", "--citeproc", f"--bibliography={bib}",
               f"--csl={csl}", "--resource-path=.", "-o", str(qmd.with_suffix(".docx"))]
        r = subprocess.run(cmd, cwd=qmd.parent, capture_output=True, text=True)
        sys.stderr.write(r.stderr)
    finally:
        Path(tmp.name).unlink()
    unresolved = sorted(set(re.findall(r"@((?:sec|tbl|fig|eq)-[\w-]+)", text)))
    if unresolved:
        print("UNRESOLVED:", unresolved)
    print("wrote", qmd.with_suffix(".docx"))


if __name__ == "__main__":
    main()
