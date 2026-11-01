// Working-paper format: an academic working paper in the website's style.
// Text: Source Serif 4. Headings, labels and running heads: Source Sans 3, in the site's link blue.
// Fonts ship in fonts/ (SIL Open Font License), so the PDF looks the same on every machine.

#let wp-blue = rgb("#1a5490")
#let wp-grey = rgb("#5f6b7a")
#let wp-rule = rgb("#c9d3df")
#let wp-tint = rgb("#f3f6fa")
#let wp-serif = ("Source Serif 4", "Libertinus Serif")
#let wp-sans = ("Source Sans 3", "DejaVu Sans")

// Called by the Lua filter where the appendices begin: letters for any numbered headings after it.
#let appendix-start() = {
  counter(heading).update(0)
}

#let working-paper(
  title: none,
  subtitle: none,
  short-title: none,
  authors: (),
  date: none,
  series: none,
  version: none,
  abstract: none,
  keywords: (),
  jel: (),
  sectionnumbering: "1.1",
  toc: false,
  toc_depth: 2,
  doc,
) = {
  let author-names = if authors != none { authors.map(a => a.name) } else { () }

  set document(title: title, keywords: keywords)
  set document(author: author-names.map(n => content-to-string(n)).join(", ")) if author-names.len() > 0

  // ---- page ----
  set page(
    paper: "a4",
    margin: (x: 2.6cm, top: 2.9cm, bottom: 2.6cm),
    header: context {
      if counter(page).get().first() > 1 {
        set text(font: wp-sans, size: 8pt, fill: wp-grey)
        grid(columns: (1fr, auto),
          align(left, short-title),
          align(right, author-names.join(", ")))
        v(-0.55em)
        line(length: 100%, stroke: 0.4pt + wp-rule)
      }
    },
    footer: context {
      set text(font: wp-sans, size: 8.5pt, fill: wp-grey)
      align(center, counter(page).display("1"))
    },
  )

  // ---- text ----
  set text(font: wp-serif, size: 10.5pt, lang: "en", region: "GB", hyphenate: true,
           number-type: "lining")
  set par(justify: true, leading: 0.66em, spacing: 0.95em)
  show math.equation: set text(font: ("New Computer Modern Math",))
  show link: set text(fill: wp-blue)
  show ref: set text(fill: wp-blue)
  show footnote.entry: set text(size: 8.5pt)
  set footnote.entry(separator: line(length: 25%, stroke: 0.4pt + wp-rule))
  show raw: set text(font: ("DejaVu Sans Mono",), size: 0.88em)

  // ---- lists ----
  set list(indent: 0.6em, body-indent: 0.5em)
  set enum(indent: 0.6em, body-indent: 0.5em)

  // ---- headings ----
  set heading(numbering: sectionnumbering)
  show heading: set text(font: wp-sans, fill: wp-blue, hyphenate: false)
  show heading: set par(justify: false)
  show heading.where(level: 1): it => {
    set text(size: 13pt, weight: "semibold")
    block(above: 1.9em, below: 0.9em, sticky: true, {
      if it.numbering != none {
        box(width: 1.6em, counter(heading).display(it.numbering))
      }
      it.body
    })
  }
  show heading.where(level: 2): it => {
    set text(size: 11pt, weight: "semibold")
    block(above: 1.5em, below: 0.75em, sticky: true, {
      if it.numbering != none {
        box(width: 2.2em, counter(heading).display(it.numbering))
      }
      it.body
    })
  }
  show heading.where(level: 3): it => {
    set text(font: wp-serif, size: 10.5pt, weight: "regular", style: "italic", fill: black)
    block(above: 1.2em, below: 0.6em, sticky: true, it.body)
  }

  // ---- figures and tables ----
  show figure: set block(above: 1.4em, below: 1.4em)
  show figure.caption: it => {
    set text(font: wp-serif, size: 9pt)
    set par(justify: true, leading: 0.55em)
    block(width: 100%, inset: (x: 0.5em), align(left, {
      text(font: wp-sans, weight: "semibold", fill: wp-blue, size: 9pt, [#it.supplement #context it.counter.display(it.numbering).])
      h(0.4em)
      it.body
    }))
  }
  show figure.where(kind: table): set figure.caption(position: top)
  set table(stroke: none, inset: (x: 6pt, y: 4.5pt))
  show table: set text(size: 9.5pt)
  show table: set par(justify: false)
  show table: it => {
    // booktabs: a heavy rule above and below, a light one under the header row
    block(stroke: (top: 1pt + black, bottom: 1pt + black), it)
  }
  show table.cell.where(y: 0): set text(weight: "semibold")
  set table.hline(stroke: 0.5pt + black)

  // ---- quotes ----
  show quote: it => block(inset: (left: 1.2em, right: 1.2em), text(size: 10pt, it))

  // ---- title block ----
  block(width: 100%, below: 0pt, {
    set text(font: wp-sans, size: 8.5pt, fill: wp-blue, weight: "semibold", tracking: 0.06em)
    let bits = (if series != none { upper(series) } else { upper[Working paper] },)
    if version != none { bits.push([VERSION #version]) }
    if date != none { bits.push(upper(date)) }
    bits.join(h(0.6em) + text(fill: wp-rule)[|] + h(0.6em))
  })
  v(0.45em)
  line(length: 100%, stroke: 1.4pt + wp-blue)
  v(1.6em)

  if title != none {
    block(below: 0.9em, {
      set par(justify: false, leading: 0.4em)
      text(font: wp-serif, size: 22pt, weight: "semibold", hyphenate: false, title)
    })
  }
  if subtitle != none {
    block(below: 1.4em, {
      set par(justify: false, leading: 0.5em)
      text(font: wp-serif, size: 13.5pt, style: "italic", fill: wp-grey, hyphenate: false, subtitle)
    })
  }
  if authors != none and authors.len() > 0 {
    block(below: 1.6em, {
      set text(font: wp-sans, size: 11pt)
      authors.map(a => {
        text(weight: "semibold", a.name)
        let note = a.at("note", default: [])
        if note != [] and note != none {
          footnote(numbering: "*", note)
          counter(footnote).update(n => n - 1)
        }
        let aff = a.at("affiliation", default: [])
        if aff != [] and aff != none { linebreak(); text(size: 9.5pt, fill: wp-grey, aff) }
      }).join(h(2em))
    })
  }

  if abstract != none {
    block(width: 100%, fill: wp-tint, inset: (x: 1.3em, top: 1.1em, bottom: 1.1em),
          stroke: (left: 2.5pt + wp-blue), below: 1.8em, {
      text(font: wp-sans, size: 9pt, weight: "semibold", fill: wp-blue, tracking: 0.06em, upper[Abstract])
      v(0.2em)
      set text(size: 9.5pt)
      set par(leading: 0.6em)
      abstract
      if keywords != none and keywords.len() > 0 {
        v(0.5em)
        text(font: wp-sans, size: 8.5pt, [#text(weight: "semibold")[Keywords:] #keywords.join(", ")])
      }
      if jel != none and jel.len() > 0 {
        linebreak()
        text(font: wp-sans, size: 8.5pt, [#text(weight: "semibold")[JEL codes:] #jel.join(", ")])
      }
    })
  }

  if toc {
    block(below: 2em, {
      set text(font: wp-sans, size: 9.5pt)
      outline(title: text(size: 11pt, fill: wp-blue)[Contents], depth: toc_depth, indent: 1.2em)
    })
  }

  doc
}
