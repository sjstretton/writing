"""Render a .qmd master in this folder to Word in the house working-paper format, without Quarto.

The house format is the Quarto extension in
    H Writing Instructions/Writing Standards/templates/_extensions/working-paper/
On a machine with Quarto, prefer the house script, which also makes the PDF:
    python "H Writing Instructions/Scripts/Website/render_pdfs.py" "path/to/Any.qmd" --docx
Where Quarto is not installed (for example a cloud session), this script gives the same Word file:
it runs pandoc with the extension's reference.docx (styles) and its working-paper.lua filter, with a small
shim for the two Quarto functions the filter calls.

    python "B Theory and Research/render_docx.py" "B Theory and Research/ThesisPlan/ThesisPlan-SovereignIncentives.qmd"
    python "B Theory and Research/render_docx.py" --all        every .qmd under B Theory and Research
"""
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
EXT = REPO / "H Writing Instructions" / "Writing Standards" / "templates" / "_extensions" / "working-paper"

SHIM = """
quarto = quarto or {
  doc = { is_format = function(f) return FORMAT == f or (f == "docx" and FORMAT == "docx") end },
  log = { warning = function(msg) io.stderr:write(msg .. "\\n") end },
}
"""


def render(qmd: Path) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".lua", delete=False) as f:
        f.write(SHIM + (EXT / "working-paper.lua").read_text(encoding="utf-8"))
        filt = f.name
    out = qmd.with_suffix(".docx")
    cmd = ["pandoc", qmd.name, "-f", "markdown", "--citeproc",
           f"--reference-doc={EXT / 'reference.docx'}", f"--lua-filter={filt}",
           f"--resource-path=.:{qmd.parent}", "-o", out.name]
    subprocess.run(cmd, cwd=qmd.parent, check=True)
    print("wrote", out.relative_to(REPO))


if __name__ == "__main__":
    args = sys.argv[1:]
    targets = sorted(HERE.rglob("*.qmd")) if args == ["--all"] else [Path(a).resolve() for a in args]
    for t in targets:
        render(t)
