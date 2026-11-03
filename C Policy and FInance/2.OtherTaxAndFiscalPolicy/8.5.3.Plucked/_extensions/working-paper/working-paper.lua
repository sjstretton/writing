-- working-paper.lua: shared by the PDF (typst) and Word (docx) forms of the working-paper format.
--  1. The masters link between the brief and the working paper with short targets
--     ([text](wp:sec-x), [text](brief:), [text](paper:1.2)). Outside the website these would be dead
--     links, so only the text is kept (same rule as Scripts/Website/web-links.lua).
--  2. Appendices: a heading with class .appendix (e.g. "# Appendix A: Literature review {.appendix}")
--     and every heading after it are left unnumbered, because they carry their own letters (A.1, A.2).
--  3. Page breaks: before the executive summary, the section after it, the references and the appendices.
--  4. Word only: the keywords and JEL codes are added under the abstract (the PDF template prints them itself).

local function is_short_link(target)
  return target:match("^wp:") or target:match("^brief:") or target:match("^paper:")
end

function Link(el)
  if is_short_link(el.target) then
    return el.content
  end
end

local function stringify_list(v)
  if v == nil then return nil end
  if pandoc.utils.type(v) == "List" then
    local out = {}
    for _, x in ipairs(v) do table.insert(out, pandoc.utils.stringify(x)) end
    return table.concat(out, ", ")
  end
  return pandoc.utils.stringify(v)
end

local function page_break(extra)
  if quarto.doc.is_format("typst") then
    return pandoc.RawBlock("typst", "#pagebreak(weak: true)" .. (extra or ""))
  elseif quarto.doc.is_format("docx") then
    return pandoc.RawBlock("openxml", '<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
  end
end

local function is_references(h)
  local t = pandoc.utils.stringify(h.content):lower()
  return h.identifier == "refs" or t == "references" or t == "bibliography"
end

-- Page rules (H Writing Instructions/NORMS.md, section 11): new page for the executive summary (the first
-- top-level section), for the section after it, for the references and for the appendices.
-- Masters converted from Word can carry internal links to anchors that no longer exist (old contents
-- lists, Word footnote anchors) and images whose files are missing. Typst refuses both, so a link to a
-- missing anchor keeps only its text and a missing image is left out (with a warning).
local function drop_broken(doc)
  local ids = {}
  local function note(el) if el.identifier and el.identifier ~= "" then ids[el.identifier] = true end end
  doc:walk({ Header = note, Div = note, Span = note, Figure = note, Image = note, Table = note, CodeBlock = note })
  return doc:walk({
    Link = function(el)
      local t = el.target:match("^#(.+)$")
      if t and not ids[t] and not t:match("^sec%-") and not t:match("^fig%-") and not t:match("^tbl%-")
         and not t:match("^eq%-") and t ~= "refs" and not t:match("^ref%-") then
        return el.content
      end
    end,
    Image = function(el)
      local src = el.src
      if not src:match("^https?:") and not src:match("^data:") then
        local f = io.open(src, "rb")
        if f then f:close() else
          quarto.log.warning("working-paper: image not found, left out: " .. src)
          return pandoc.Str("")
        end
      end
    end,
  })
end

function Pandoc(doc)
  doc = drop_broken(doc)
  -- books (series: "Book") start each chapter or part on a new page instead
  local is_book = doc.meta.series and pandoc.utils.stringify(doc.meta.series):lower():match("^book") ~= nil
  if doc.meta["number-sections"] == false then doc.meta["wp-unnumbered"] = true end
  local in_appendix = false
  local h1 = 0
  -- a book whose chapters are "# CHAPTER n: ..." headings with its sub-sections also at level 1:
  -- push everything else down a level so the chapters lead the contents
  if is_book then
    local chapters = false
    for _, b in ipairs(doc.blocks) do
      if b.t == "Header" and b.level == 1 and pandoc.utils.stringify(b.content):match("^CHAPTER") then chapters = true end
    end
    if chapters then
      for _, b in ipairs(doc.blocks) do
        if b.t == "Header" and not (b.level == 1 and pandoc.utils.stringify(b.content):match("^CHAPTER"))
           and not b.classes:includes("unnumbered") or (b.t == "Header" and b.level > 1) then
          if not (b.level == 1 and is_references(b)) then b.level = b.level + 1 end
        end
      end
    end
  end
  local blocks = pandoc.List()
  for _, b in ipairs(doc.blocks) do
    if b.t == "Header" then
      local brk = nil
      if b.level == 1 then
        h1 = h1 + 1
        local txt = pandoc.utils.stringify(b.content)
        if is_book then
          if txt:match("^CHAPTER") or txt:match("^Chapter") or txt:match("^Part ") or txt:match("^PART ")
             or h1 == 1 or is_references(b) then brk = page_break() end
        elseif h1 <= 2 or is_references(b) then
          brk = page_break()
        end
      end
      if b.classes:includes("appendix") and not in_appendix then
        in_appendix = true
        brk = page_break("\n#appendix-start()")
      end
      if brk then blocks:insert(brk) end
      if in_appendix and not b.classes:includes("unnumbered") then
        b.classes:insert("unnumbered")
      end
    end
    blocks:insert(b)
  end
  doc.blocks = blocks

  if quarto.doc.is_format("docx") and doc.meta.abstract then
    local extra = {}
    local kw = stringify_list(doc.meta.keywords)
    local jel = stringify_list(doc.meta.jel)
    if kw then table.insert(extra, pandoc.Para({pandoc.Strong("Keywords: "), pandoc.Str(kw)})) end
    if jel then table.insert(extra, pandoc.Para({pandoc.Strong("JEL codes: "), pandoc.Str(jel)})) end
    if #extra > 0 then
      local abs = doc.meta.abstract
      local list = pandoc.List()
      if pandoc.utils.type(abs) == "Blocks" then list:extend(abs) else list:insert(pandoc.Plain(abs)) end
      list:extend(extra)
      doc.meta.abstract = pandoc.MetaBlocks(list)
    end
  end
  return doc
end
