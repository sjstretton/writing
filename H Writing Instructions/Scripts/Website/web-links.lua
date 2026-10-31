-- web-links.lua: for the Word (and PDF) versions of a paper.
-- The masters link between the policy brief and the working paper with short targets
-- ([text](wp:sec-x), [text](brief:), [text](paper:1.2)); build_web_papers.py turns them into
-- real links on the website. In a Word file they would be dead links, so this keeps the text only.
-- Use it when rendering a master:  quarto render X.qmd --to docx -L <path>/web-links.lua
--                            or:  pandoc X.qmd --lua-filter=<path>/web-links.lua ...
function Link(el)
  if el.target:match("^wp:") or el.target:match("^brief:") or el.target:match("^paper:") then
    return el.content
  end
end
