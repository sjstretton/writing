-- quarto-xref.lua: Quarto-style cross-references for plain pandoc.
-- Quarto renders the masters' cross-references itself. Where only pandoc is available (a cloud session, or a PC
-- without Quarto), this filter does the same for the Word versions:
--   sections   # Title {#sec-x}          numbered (unless .unnumbered or .appendix) when number-sections: true
--   figures    ![Caption](f.png){#fig-x}  "Figure n: Caption"
--   tables     : Caption {#tbl-x}         "Table n: Caption"
--   equations  $$ ... $$ {#eq-x}          "(n)" after the equation
-- and replaces @sec-x, @fig-x, @tbl-x, @eq-x with "Section n", "Figure n", "Table n", "equation (n)".
-- Run it before --citeproc:
--   pandoc X.qmd --lua-filter=quarto-xref.lua --lua-filter=web-links.lua --citeproc ... -o X.docx

local labels = {}
local counts = { fig = 0, tbl = 0, eq = 0 }
local sec = {}
local number_sections = false

local function prefix(id) return id:match("^(%a+)%-") end

local in_unnumbered = false   -- inside a top-level section that is unnumbered or an appendix

local function number_header(h)
  if h.level == 1 then
    in_unnumbered = h.classes:includes("unnumbered") or h.classes:includes("appendix")
  end
  if not number_sections or in_unnumbered or h.classes:includes("unnumbered") then
    if h.identifier ~= "" then labels[h.identifier] = pandoc.utils.stringify(h.content) end
    return h
  end
  local lvl = h.level
  sec[lvl] = (sec[lvl] or 0) + 1
  for i = lvl + 1, 9 do sec[i] = nil end
  local parts = {}
  for i = 1, lvl do parts[#parts + 1] = tostring(sec[i] or 0) end
  local num = table.concat(parts, ".")
  if h.identifier ~= "" then labels[h.identifier] = num end
  h.content:insert(1, pandoc.Space())
  h.content:insert(1, pandoc.Str(num))
  return h
end

local function caption_prefix(kind, n)
  return { pandoc.Strong({ pandoc.Str(kind .. " " .. n .. ":") }), pandoc.Space() }
end

local function do_figure(fig)
  local id = fig.identifier
  if id == "" then
    -- the id may sit on the image inside
    pandoc.walk_block(fig, { Image = function(img) if img.identifier ~= "" then id = img.identifier end end })
  end
  if prefix(id) ~= "fig" then return fig end
  counts.fig = counts.fig + 1
  labels[id] = tostring(counts.fig)
  local cap = fig.caption.long
  if #cap > 0 and cap[1].content then
    local p = caption_prefix("Figure", counts.fig)
    for i = #p, 1, -1 do cap[1].content:insert(1, p[i]) end
  end
  return fig
end

local function do_table(tbl)
  local blocks = tbl.caption.long
  if #blocks == 0 then return tbl end
  local inl = blocks[#blocks].content
  local last = inl[#inl]
  if last and last.t == "Str" then
    local id = last.text:match("^{#(tbl%-[%w%-_]+)}$")
    if id then
      inl:remove(#inl)
      if inl[#inl] and inl[#inl].t == "Space" then inl:remove(#inl) end
      counts.tbl = counts.tbl + 1
      labels[id] = tostring(counts.tbl)
      local p = caption_prefix("Table", counts.tbl)
      for i = #p, 1, -1 do blocks[1].content:insert(1, p[i]) end
    end
  end
  return tbl
end

local function do_para(para)
  local c = para.content
  for i, el in ipairs(c) do
    if el.t == "Str" then
      local id = el.text:match("^{#(eq%-[%w%-_]+)}$")
      if id then
        counts.eq = counts.eq + 1
        labels[id] = tostring(counts.eq)
        for j = i - 1, 1, -1 do
          if c[j].t == "Math" and c[j].mathtype == "DisplayMath" then
            c[j].text = c[j].text .. " \\qquad (" .. counts.eq .. ")"
            break
          end
        end
        c:remove(i)
        if c[i - 1] and c[i - 1].t == "Space" then c:remove(i - 1) end
        return para
      end
    end
  end
  return para
end

local names = { sec = "Section", fig = "Figure", tbl = "Table", eq = "equation" }

local function do_cite(cite)
  local out = {}
  for i, c in ipairs(cite.citations) do
    local k = prefix(c.id)
    if not names[k] then return nil end
    local lab = labels[c.id] or "?"
    local text = (k == "eq") and ("equation (" .. lab .. ")") or (names[k] .. " " .. lab)
    if i > 1 then out[#out + 1] = pandoc.Str("; ") end
    out[#out + 1] = pandoc.Str(text)
  end
  return out
end

function Pandoc(doc)
  number_sections = doc.meta["number-sections"] == true
    or (doc.meta["number-sections"] and pandoc.utils.stringify(doc.meta["number-sections"]) == "true")
  local blocks = pandoc.List()
  -- pass 1: number, in document order
  doc.blocks = doc.blocks:walk({
    traverse = "topdown",
    Header = number_header,
    Figure = do_figure,
    Table = do_table,
    Para = do_para,
  })
  -- pass 2: resolve references
  doc.blocks = doc.blocks:walk({ Cite = do_cite })
  return doc
end
