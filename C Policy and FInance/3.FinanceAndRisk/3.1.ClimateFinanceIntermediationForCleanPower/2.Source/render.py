"""Render the working paper to docx with pandoc when Quarto is not installed.

Resolves Quarto cross-references (@sec-, @fig-, @tbl-, @eq-) into numbered text,
then calls pandoc with citeproc. Run from anywhere:
    python3 render.py [path/to/chicago.csl]
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME = "ClimateFinanceIntermediationForCleanPower"
CSL = sys.argv[1] if len(sys.argv) > 1 else "https://www.zotero.org/styles/chicago-author-date"


def resolve(text):
    labels = {}
    # sections (numbered unless .unnumbered)
    counters = [0, 0, 0]
    for m in re.finditer(r"^(#{1,3}) (.+?)(\{[^}]*\})?\s*$", text, flags=re.M):
        level = len(m.group(1))
        attrs = m.group(3) or ""
        if ".unnumbered" in attrs:
            ids = re.findall(r"#(sec-[\w-]+)", attrs)
            for i in ids:
                labels[i] = "Appendix " + m.group(2).split(":")[0].replace("Appendix ", "").strip()
            continue
        counters[level - 1] += 1
        for j in range(level, 3):
            counters[j] = 0
        num = ".".join(str(c) for c in counters[:level])
        for i in re.findall(r"#(sec-[\w-]+)", attrs):
            labels[i] = f"Section {num}"
    # figures
    n = 0

    def fig(m):
        nonlocal n
        n += 1
        labels[m.group(3)] = f"Figure {n}"
        return f"![Figure {n}. {m.group(1)}]({m.group(2)}){{{m.group(4).strip()}}}"
    text = re.sub(r"!\[(.*?)\]\((.*?)\)\{#(fig-[\w-]+)(.*?)\}", fig, text)
    # tables
    n = 0

    def tbl(m):
        nonlocal n
        n += 1
        labels[m.group(2)] = f"Table {n}"
        return f": Table {n}. {m.group(1).strip()}"
    text = re.sub(r"^: (.*?)\{#(tbl-[\w-]+)\}\s*$", tbl, text, flags=re.M)
    # equations
    n = 0

    def eq(m):
        nonlocal n
        n += 1
        labels[m.group(2)] = f"equation ({n})"
        return f"$${m.group(1).rstrip()} \\qquad ({n})\n$$"
    text = re.sub(r"\$\$(.*?)\$\$ \{#(eq-[\w-]+)\}", eq, text, flags=re.S)
    # strip remaining section attributes ids (keep classes)
    for key, val in labels.items():
        text = re.sub(r"(?<![\w-])@" + re.escape(key) + r"(?![\w-])", val, text)
    missing = re.findall(r"@((?:sec|fig|tbl|eq)-[\w-]+)", text)
    if missing:
        raise SystemExit(f"unresolved cross-references: {missing}")
    return text


def main():
    src = (ROOT / f"{NAME}.qmd").read_text()
    out = resolve(src)
    with tempfile.NamedTemporaryFile("w", suffix=".md", dir=ROOT, delete=False) as fh:
        fh.write(out)
        tmp = fh.name
    try:
        subprocess.run(["pandoc", tmp, "-f", "markdown", "--citeproc", "--number-sections",
                        f"--bibliography={NAME}.bib", f"--csl={CSL}", "--resource-path=.",
                        "-o", f"{NAME}.docx"], cwd=ROOT, check=True)
    finally:
        Path(tmp).unlink()
    print(f"wrote {NAME}.docx")


if __name__ == "__main__":
    main()
