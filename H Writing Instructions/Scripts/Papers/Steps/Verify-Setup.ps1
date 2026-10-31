#requires -Version 5.1
<#
    Verify-Setup.ps1
    The pre-flight check. It reads and reports; there is no -Apply and nothing
    is ever changed. Run it after moving folders about, or before a day's first
    End-Day, to find out whether anything downstream is going to break.

    WHAT IT CHECKS

      1  THE TREE      the paper roots (C Policy and FInance, D Modelling,
                       F Other Writing) and E Website exist, numbered sections,
                       no folder name with a space, no two folders that differ
                       only by punctuation, and no <n>.0 overview folder left
                       unflattened.

      2  THE PAPERS    every paper folder has a master named after itself.
                       A folder with slots but no master is listed - that is a
                       paper waiting to be written, which is fine, but it
                       publishes nothing.

      3  THE SITE      every papers/... link in the site's pages resolves to a
                       file in E Website\papers; and the same file is in
                       _site\papers\ from the last render.

      4  THE SCRIPTS   the five-folder layout, nothing loose at the top, and no
                       spent one-off still sitting in Steps\ or Run\.

      5  THE TOOLS     git, quarto, pandoc and WinSCP on the machine, and where
                       the FTP credentials are going to come from.

      6  THE REPOSITORY  where it is, which branch, how much is uncommitted, and
                       whether deploy.bat is still tracked with the password in it.

    Every line is OK, NOTE or PROBLEM. A NOTE is something to know; a PROBLEM
    will break the next End-Day run.

    Usage
        Run\Final-Check.bat
        Reports\_VerifyReport.txt
#>

$ErrorActionPreference = 'Continue'

$me      = Split-Path -Parent $MyInvocation.MyCommand.Path
$scripts = Split-Path -Parent $me

# The paper roots, from the repository root: sections 1-4, sections 5-7, and the writing outside the
# series (8.x). The one place to change them in this script: D Modelling is due to move to its own repository.
$PaperRootNames = @('C Policy and FInance', 'D Modelling', 'F Other Writing')

# The paper roots that exist, as full paths under the repository root.
function Get-PaperRoots([string]$repo) {
    return @($PaperRootNames | ForEach-Object { Join-Path $repo $_ } | Where-Object { Test-Path -LiteralPath $_ })
}

function Find-WritingRoot([string]$s) {
    # Walk up to the repository root (the folder holding .git). The papers are in the paper roots under it.
    $d = $s
    for ($i = 0; $i -lt 8; $i++) {
        if (Test-Path -LiteralPath (Join-Path $d '.git')) { return $d }
        $p = Split-Path -Parent $d; if (-not $p -or $p -eq $d) { break }; $d = $p
    }
    return $null
}
$base = Find-WritingRoot $me
if (-not $base) { Write-Host 'Could not find the repository root (the folder holding .git).'; return }
$PaperRoots = @(Get-PaperRoots $base)
if ($PaperRoots.Count -eq 0) { Write-Host ('None of the paper roots is in {0}: {1}' -f $base, ($PaperRootNames -join ', ')); return }

$reportDir = Join-Path $scripts 'Reports'
if (-not (Test-Path -LiteralPath $reportDir)) { New-Item -ItemType Directory -Path $reportDir -Force | Out-Null }

$log = New-Object System.Collections.Generic.List[string]
$problems = 0; $notes = 0
function Log($m) { $log.Add([string]$m) | Out-Null; Write-Host $m }
function OK($m)      { Log ('   OK      {0}' -f $m) }
function Note($m)    { Log ('   NOTE    {0}' -f $m); $script:notes++ }
function Problem($m) { Log ('   PROBLEM {0}' -f $m); $script:problems++ }
function Rel([string]$f) { return $f.Substring($base.Length).TrimStart('\','/') }

$Slots    = @('1.Presentation','2.Source','3.BackgroundPapers','3.RelatedPiecesAndLinks','4.ExternalPapers',
              '5.Notes','6.Reserved','7.Reserved','8.PreviousVersions','9.Archive')
$SkipDirs = @('media','images','_site','.quarto','_freeze','papers','node_modules',
              'Run','Engine','Steps','Reference','Reports')

function Core-Name([string]$n) {
    $t = $n -replace '^\s*\d+(\.\d+)*[A-Za-z]?[.\s_-]+', ''
    $w = $t -split '[^A-Za-z0-9]+' | Where-Object { $_ -ne '' }
    $o = ''
    foreach ($x in $w) {
        if ($x -cmatch '^[A-Z0-9]+$' -or $x -cmatch '^[A-Z]{2,}' -or $x -cmatch '[A-Z].*[A-Z]') { $o += $x }
        else { $o += $x.Substring(0,1).ToUpper() + $x.Substring(1).ToLower() }
    }
    return $o
}

Log ('=== Final check   {0} ===' -f (Get-Date -Format 'yyyy-MM-dd HH:mm'))
Log ('Base : {0}' -f $base)
Log ('Papers : {0}' -f ($PaperRootNames -join ', '))
Log 'Report only. Nothing is changed.'
Log ''

# ------------------------------------------------------------------ 1 tree ---

Log '--- 1  the tree'
foreach ($n in $PaperRootNames) {
    if (Test-Path -LiteralPath (Join-Path $base $n)) { OK ('paper root      : {0}' -f $n) }
    else { Problem ('paper root      : {0} is missing' -f $n) }
}

$web = @(Get-Item -LiteralPath (Join-Path $base 'E Website') -EA SilentlyContinue)
if ($web.Count -eq 1) { OK ('Website folder  : {0}' -f $web[0].Name) }
else { Problem 'no E Website folder - nothing can be published' }

OK ('Scripts folder  : {0}' -f (Rel (Split-Path -Parent $scripts)))

# The folders at the top of each paper root: sections in C Policy and FInance
# and D Modelling, papers in F Other Writing.
$tops = @(Get-ChildItem -LiteralPath $PaperRoots -Directory -EA SilentlyContinue | Where-Object { $_.Name -notmatch '^[_.]' })

$sections = @($tops | Where-Object { $_.Name -match '^\d+[A-Za-z]?[.\s_-]' -and $_.Name -notmatch '^\d+\.\d+[.\s_-]' })
OK ('{0} section folder(s): {1}' -f $sections.Count, (($sections | ForEach-Object { $_.Name }) -join ', '))

$spaced = @($tops | Where-Object { $_.Name -match '\s' })
if ($spaced.Count -eq 0) { OK 'no folder name at the top of a paper root has a space in it' }
else { foreach ($d in $spaced) { Note ('"{0}" has a space - Rename-Folders will fix it' -f (Rel $d.FullName)) } }

foreach ($g in ($tops | Group-Object { ($_.Name -replace '[^A-Za-z0-9]','').ToLower() })) {
    if ($g.Count -gt 1) {
        Problem ('two folders that are the same name twice: {0}' -f (($g.Group | ForEach-Object { '"' + (Rel $_.FullName) + '"' }) -join '  and  '))
    }
}

$dotZero = @(Get-ChildItem -LiteralPath $PaperRoots -Directory -Recurse -EA SilentlyContinue |
             Where-Object { $_.Name -match '^\d+\.0[.\s_-]' -and $_.FullName -notmatch '[\\/](_site|\.quarto)[\\/]' })
if ($dotZero.Count -eq 0) { OK 'no .0 overview folder left - every section overview is a single Word file' }
else { foreach ($d in $dotZero) { Note ('{0}\ is still a folder' -f (Rel $d.FullName)) } }
Log ''

# ---------------------------------------------------------------- 2 papers ---

Log '--- 2  the papers'
function Find-PaperFolders([string]$root) {
    $found = New-Object System.Collections.Generic.List[object]
    $stack = New-Object System.Collections.Stack
    foreach ($d in (Get-ChildItem -LiteralPath $root -Directory -EA SilentlyContinue)) {
        if ($d.Name -match '[.\s_-]*Scripts$' -or $d.Name -match 'Website$') { continue }
        if ($d.Name -match '^[_.]') { continue }
        $stack.Push($d)
    }
    while ($stack.Count -gt 0) {
        $d = $stack.Pop()
        if ($SkipDirs -contains $d.Name -or $Slots -contains $d.Name) { continue }
        $core = Core-Name $d.Name
        $isPaper = $false
        foreach ($e in @('.docx','.qmd','.pdf','.tex')) {
            if (Test-Path -LiteralPath (Join-Path $d.FullName ($core + $e))) { $isPaper = $true; break }
        }
        $hasSlot = @(Get-ChildItem -LiteralPath $d.FullName -Directory -EA SilentlyContinue |
                     Where-Object { $Slots -contains $_.Name }).Count -gt 0
        $hasKids = @(Get-ChildItem -LiteralPath $d.FullName -Directory -EA SilentlyContinue |
                     Where-Object { $_.Name -match '^\d+\.\d+[.\s_-]' }).Count -gt 0
        if ($isPaper -or ($hasSlot -and -not $hasKids)) {
            $found.Add([pscustomobject]@{ Dir = $d; HasMaster = $isPaper }) | Out-Null
        } else {
            foreach ($s in (Get-ChildItem -LiteralPath $d.FullName -Directory -EA SilentlyContinue)) {
                if ($SkipDirs -notcontains $s.Name -and $s.Name -notmatch '^[_.]') { $stack.Push($s) }
            }
        }
    }
    return $found
}
$papers  = @($PaperRoots | ForEach-Object { Find-PaperFolders $_ } | Sort-Object { $_.Dir.FullName })
$noMaster = @($papers | Where-Object { -not $_.HasMaster })
OK ('{0} paper folder(s), {1} with a master document' -f $papers.Count, ($papers.Count - $noMaster.Count))
foreach ($p in $noMaster) { Note ('no master yet : {0}' -f (Rel $p.Dir.FullName)) }
Log ''

# ------------------------------------------------------------------ 3 site ---

Log '--- 3  the site'
if ($web.Count -eq 0) {
    Problem 'skipped - no E Website folder'
} else {
    # The pages are written by Compile-Website.bat (Scripts\Website). Every
    # papers/... link in them should resolve to a file in E Website\papers, and
    # to the same file in _site\papers after the last render.
    $webDir = $web[0].FullName
    if (Test-Path -LiteralPath (Join-Path $webDir '_quarto.yml')) { OK '_quarto.yml found' }
    else { Problem 'E Website\_quarto.yml is missing' }
    $pages = @(Get-ChildItem -LiteralPath $webDir -File -Recurse -Filter '*.qmd' -EA SilentlyContinue |
               Where-Object { $_.FullName -notmatch '[\\/](_site|\.quarto|_freeze|PaperArchive|papers)[\\/]' })
    $links = @(foreach ($pg in $pages) {
        $txt = Get-Content -LiteralPath $pg.FullName -Raw -Encoding UTF8
        if ($txt) { [regex]::Matches($txt, '\]\((?:\.\./)*(papers/[^)\s#]+)\)') | ForEach-Object { $_.Groups[1].Value } }
    }) | Select-Object -Unique
    $links = @($links)
    $bad = 0; $notRendered = 0
    foreach ($l in $links) {
        $localFile = Join-Path $webDir ($l -replace '/','\')
        $siteFile  = Join-Path $webDir (Join-Path '_site' ($l -replace '/','\'))
        if (-not (Test-Path -LiteralPath $localFile)) { Problem ('link with no file : {0}' -f $l); $bad++ }
        elseif (-not (Test-Path -LiteralPath $siteFile)) { Note ('not in _site yet  : {0}   (render pending)' -f $l); $notRendered++ }
    }
    OK ('{0} page(s), {1} paper link(s), {2} broken, {3} awaiting a render' -f $pages.Count, $links.Count, $bad, $notRendered)
    $pdir = Join-Path $webDir 'papers'
    if (Test-Path -LiteralPath $pdir) {
        $n = @(Get-ChildItem -LiteralPath $pdir -File -EA SilentlyContinue).Count
        OK ('{0} file(s) in papers\ - only the files the pages link to' -f $n)
    } else { Note 'papers\ does not exist yet - Compile-Website.bat creates it' }
}
Log ''

# --------------------------------------------------------------- 4 scripts ---

Log '--- 4  the scripts folder'
$layout = @('Run','Engine','Steps','Reference','Reports')
foreach ($d in $layout) {
    if (Test-Path -LiteralPath (Join-Path $scripts $d)) { OK ('{0}\' -f $d) }
    else { Problem ('{0}\ is missing' -f $d) }
}
$loose = @(Get-ChildItem -LiteralPath $scripts -File -EA SilentlyContinue)
if ($loose.Count -eq 0) { OK 'nothing loose at the top of the scripts folder' }
else { foreach ($f in $loose) { Note ('loose file : {0}   (Spring-Clean will bin it)' -f $f.Name) } }

$extra = @(Get-ChildItem -LiteralPath $scripts -Directory -EA SilentlyContinue |
           Where-Object { $layout -notcontains $_.Name })
foreach ($d in $extra) { Note ('extra folder : {0}\   (Spring-Clean will bin it)' -f $d.Name) }

$spent = @('Flatten-Overviews.ps1','Flatten-Overviews.bat',
           'Remove-TwinFolders.ps1','Remove-TwinFolders.bat',
           'Remove-StrayFolder.ps1','Remove-StrayFolder.bat',
           'Move-ToAdditional.ps1','Move-ToAdditional.bat',
           'Finalise-Content.ps1','Finalise-Content.bat')
$left = @()
foreach ($d in @('Steps','Run')) {
    $dir = Join-Path $scripts $d
    if (-not (Test-Path -LiteralPath $dir)) { continue }
    foreach ($f in (Get-ChildItem -LiteralPath $dir -File -EA SilentlyContinue)) {
        if ($spent -contains $f.Name) { $left += ($d + '\' + $f.Name) }
    }
}
if ($left.Count -eq 0) { OK 'no spent one-off left behind' }
else { foreach ($f in $left) { Note ('spent one-off : {0}   (Spring-Clean will bin it)' -f $f) } }
Log ''

# ----------------------------------------------------------------- 5 tools ---

Log '--- 5  the tools'
foreach ($t in @('git','quarto','pandoc')) {
    $c = Get-Command $t -EA SilentlyContinue
    if ($c) { OK ('{0,-8}: {1}' -f $t, $c.Source) }
    elseif ($t -eq 'quarto') { Problem 'quarto  : not on PATH - the site cannot be rendered' }
    elseif ($t -eq 'pandoc') { Problem 'pandoc  : not on PATH - documents cannot be converted' }
    else { Problem 'git     : not on PATH - nothing can be committed or pushed' }
}
$winscp = $null
foreach ($c in @('C:\Program Files (x86)\WinSCP\WinSCP.com','C:\Program Files\WinSCP\WinSCP.com')) {
    if (Test-Path -LiteralPath $c) { $winscp = $c; break }
}
if ($winscp) { OK ('WinSCP  : {0}' -f $winscp) } else { Problem 'WinSCP  : not found - the site cannot be uploaded' }

$cred = Join-Path $base 'FTP-Login.txt'   # at the repository root, git-ignored
if (Test-Path -LiteralPath $cred) {
    $keys = @(Get-Content -LiteralPath $cred -EA SilentlyContinue |
              Where-Object { $_ -match '^\s*([A-Za-z]+)\s*=\s*\S' } |
              ForEach-Object { ($_ -split '=')[0].Trim().ToLower() })
    $missing = @('host','user','password') | Where-Object { $keys -notcontains $_ }
    if ($missing.Count -eq 0) { OK 'FTP     : FTP-Login.txt, complete' }
    else { Problem ('FTP     : FTP-Login.txt is missing {0}' -f ($missing -join ', ')) }
} elseif ($web.Count -gt 0 -and (Test-Path -LiteralPath (Join-Path $web[0].FullName 'deploy.bat'))) {
    Note ('FTP     : no FTP-Login.txt - falling back to {0}\deploy.bat, which holds the password inline' -f $web[0].Name)
} else {
    Problem 'FTP     : no credentials anywhere - the upload will stop'
}
Log ''

# ------------------------------------------------------------ 6 repository ---

Log '--- 6  the repository'
$git = Get-Command git -EA SilentlyContinue
if (-not $git) {
    Problem 'skipped - git is not on PATH'
} else {
    $repo = $base
    $found = $null
    for ($i = 0; $i -lt 6; $i++) {
        if (Test-Path -LiteralPath (Join-Path $repo '.git')) { $found = $repo; break }
        $p = Split-Path -Parent $repo; if (-not $p -or $p -eq $repo) { break }; $repo = $p
    }
    if (-not $found) {
        Problem 'no .git at or above the scripts - nothing will be committed or pushed'
    } else {
        Push-Location -LiteralPath $found
        try {
            OK ('repository : {0}' -f $found)
            $remote = (& git remote get-url origin 2>&1 | Out-String).Trim()
            if ($remote -and $remote -notmatch '^(error|fatal)') { OK ('remote     : {0}' -f $remote) }
            else { Problem 'no origin remote - there is nowhere to push' }
            OK ('branch     : {0}' -f (& git rev-parse --abbrev-ref HEAD 2>&1 | Out-String).Trim())
            $st = @(& git status --porcelain 2>&1 | Where-Object { $_ -ne '' })
            OK ('{0} uncommitted change(s)' -f $st.Count)

            $tracked = @(& git ls-files 2>&1 | Where-Object { $_ -match 'deploy\.bat$' })
            if ($tracked.Count -gt 0) {
                Note 'deploy.bat is still tracked and holds the FTP password:'
                foreach ($t in $tracked) { Log ('              git rm --cached "{0}"' -f $t) }
                Log  '           and change the password on the server - the old one is in the history.'
            } else { OK 'deploy.bat is not tracked' }
        } finally { Pop-Location }
    }
}

# ---------------------------------------------------------------- finish -----

Log ''
Log '================================================================'
if ($problems -eq 0 -and $notes -eq 0) {
    Log 'Everything checks out. Run\End-Day.bat will work.'
} elseif ($problems -eq 0) {
    Log ('{0} note(s), nothing broken. Run\End-Day.bat will work.' -f $notes)
} else {
    Log ('{0} PROBLEM(s) and {1} note(s). Fix the problems before End-Day.bat.' -f $problems, $notes)
}

$path = Join-Path $reportDir '_VerifyReport.txt'
$log | Set-Content -LiteralPath $path -Encoding UTF8
Write-Host ''
Write-Host ('Report : {0}' -f $path)
