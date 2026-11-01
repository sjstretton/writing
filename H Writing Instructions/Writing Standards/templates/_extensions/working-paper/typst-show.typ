// Fills the working-paper() template from the paper's YAML.
#show: doc => working-paper(
$if(title)$
  title: [$title$],
$endif$
$if(subtitle)$
  subtitle: [$subtitle$],
$endif$
$if(short-title)$
  short-title: [$short-title$],
$elseif(title)$
  short-title: [$title$],
$endif$
$if(by-author)$
  authors: (
$for(by-author)$
$if(it.name.literal)$
    ( name: [$it.name.literal$],
      affiliation: [$for(it.affiliations)$$it.name$$sep$, $endfor$],
      note: [$it.note.text$] ),
$endif$
$endfor$
  ),
$endif$
$if(date)$
  date: [$date$],
$endif$
$if(series)$
  series: [$series$],
$endif$
$if(version)$
  version: [$version$],
$endif$
$if(abstract)$
  abstract: [$abstract$],
$endif$
$if(keywords)$
  keywords: ($for(keywords)$"$keywords$",$endfor$),
$endif$
$if(jel)$
  jel: ($for(jel)$"$jel$",$endfor$),
$endif$
$if(section-numbering)$
  sectionnumbering: "$section-numbering$",
$endif$
$if(toc)$
  toc: $toc$,
$endif$
  toc_depth: $toc-depth$,
  doc,
)
