#requires -Version 5.1
<#
    Run-Website.ps1
    The PDF and website half of the workflow, on its own.

        1  Build-Pdfs      only with -Pdf. A PDF for every paper with a
                           master .docx, one document per process with a time
                           limit, so a document Word cannot open is skipped
                           rather than stopping the run.
        2  Build-Website   the same build as Compile-Website.bat at the top of
                           the repository: the Python scripts in Scripts\Website
                           (PaperArchive, web papers, section pages, papers\
                           with only the linked files, the folder index.html
                           pages), then quarto render in E Website. Nothing is
                           uploaded; End-Day.ps1 does that.

    PDFs are not built by default. Driving Word to make PDFs is the one part of
    this pipeline that depends on a desktop application behaving. -Pdf runs it.

    Run it with Run\Master-Website.bat. Run-All.ps1 calls this as its last step,
    so there is only one copy of this logic.

    Switches
        -Apply              do it (otherwise both steps report only)
        -Pdf                also build a PDF of every paper with Word
        -TimeoutSeconds N   per document, default 180, only with -Pdf
        -SkipRender         run the Python build without quarto render
        -Only <pattern>     build only papers whose folder name matches
        -Force              rebuild PDFs even where they are already current
#>

[CmdletBinding()]
param(
    [switch]$Apply,
    [switch]$Pdf,
    [int]$TimeoutSeconds = 180,
    [switch]$SkipRender,
    [string]$Only,
    [switch]$Force
)

$ErrorActionPreference = 'Continue'

$me      = Split-Path -Parent $MyInvocation.MyCommand.Path
$scripts = Split-Path -Parent $me
$mode    = if ($Apply) { 'APPLY' } else { 'PREVIEW' }

$reportDir = Join-Path $scripts 'Reports'
if (-not (Test-Path -LiteralPath $reportDir)) { New-Item -ItemType Directory -Path $reportDir -Force | Out-Null }
$transcript = Join-Path $reportDir ("RunWebsite-{0}-{1}.txt" -f $mode, (Get-Date -Format 'yyyyMMdd-HHmmss'))
try { Start-Transcript -LiteralPath $transcript -Force | Out-Null } catch { }

function Banner([string]$t) {
    Write-Host ''
    Write-Host ('=' * 70)
    Write-Host ("  {0}" -f $t)
    Write-Host ('=' * 70)
}

Banner ("Run-Website  [{0}]   {1}" -f $mode, (Get-Date -Format 'yyyy-MM-dd HH:mm'))

$results = New-Object System.Collections.Generic.List[object]

# --- prerequisites ------------------------------------------------------------

Write-Host ''
Write-Host '-- prerequisites'
# No Word probe. Creating and quitting a COM instance just to test for Word is
# itself a way to hang or fail, and when it failed it silently skipped the whole
# PDF step. Build-Pdfs runs each document in its own killable process, so if Word
# really is missing every document fails fast and says so.
Write-Host '   Word     : not probed - Build-Pdfs reports per document'
foreach ($t in @('quarto', 'pandoc')) {
    if (Get-Command $t -ErrorAction SilentlyContinue) { Write-Host ("   found  : {0}" -f $t) }
    else { Write-Host ("   MISSING: {0}" -f $t) }
}

# --- 1  PDFs ------------------------------------------------------------------

$buildPdfs = Join-Path $scripts 'Steps\Build-Pdfs.ps1'
if (-not $Pdf) {
    Write-Host ''
    Write-Host '-- step 1  PDFs not built. Pass -Pdf to build them with Word.'
    $results.Add([pscustomobject]@{ Step=1; Name='Build-Pdfs'; Status='not wanted'; Seconds=0; Note='no -Pdf' }) | Out-Null
} elseif (-not (Test-Path -LiteralPath $buildPdfs)) {
    Write-Host ''
    Write-Host '-- step 1  Build-Pdfs.ps1 NOT FOUND in Steps\'
    $results.Add([pscustomobject]@{ Step=1; Name='Build-Pdfs'; Status='missing'; Seconds=0; Note='not in Steps\' }) | Out-Null
} else {
    Banner 'step 1 of 2   Build-Pdfs.ps1   -   a PDF for every paper'
    $sw = [System.Diagnostics.Stopwatch]::StartNew()
    $err = $null
    try {
        $p = @{ TimeoutSeconds = $TimeoutSeconds }
        if ($Apply) { $p['Apply'] = $true }
        if ($Force) { $p['Force'] = $true }
        if ($Only)  { $p['Only']  = $Only }
        & $buildPdfs @p
    } catch { $err = $_.Exception.Message }
    $sw.Stop()
    $results.Add([pscustomobject]@{
        Step=1; Name='Build-Pdfs'
        Status=$(if ($err) { 'FAILED' } else { 'ok' })
        Seconds=[int]$sw.Elapsed.TotalSeconds; Note=$err }) | Out-Null
}

# --- 2  the website: the same build as Compile-Website.bat --------------------
# The site is built by the Python scripts in Scripts\Website (site_config.py says
# where the papers are: C Policy and FInance and D Modelling). Publish-Site.ps1,
# which copied every paper into the site's papers\ folder, is retired: the site
# now links, and uploads, only the files its pages point at.

$repo       = [IO.Path]::GetFullPath((Join-Path $scripts '..\..\..'))   # Scripts\Papers -> the repository root
$webScripts = Join-Path (Split-Path -Parent $scripts) 'Website'          # Scripts\Website
$webDir     = Join-Path $repo 'E Website'
$build = @(
    @{ Script = 'publish_series.py';       What = 'copy every paper, brief, overview and deck into E Website\PaperArchive' },
    @{ Script = 'build_web_papers.py';     What = 'the web version of each paper in WEB_PAPERS' },
    @{ Script = 'build_research_pages.py'; What = 'the section pages, and E Website\papers with only the linked files' },
    @{ Script = 'build_folder_index.py';   What = 'index.html in C Policy and FInance and D Modelling' }
)

function Find-Quarto {
    $c = Get-Command quarto -EA SilentlyContinue
    if ($c) { return $c.Source }
    foreach ($d in @('C:\Program Files\Quarto\bin', 'C:\Program Files\RStudio\resources\app\bin\quarto\bin', 'C:\Program Files\RStudio\resources\app\quarto\bin')) {
        foreach ($exe in @('quarto.exe', 'quarto.cmd')) {
            $p = Join-Path $d $exe
            if (Test-Path -LiteralPath $p -EA SilentlyContinue) { return $p }
        }
    }
    return $null
}

$python = $null
foreach ($c in @('python', 'py', 'python3')) {
    $cmd = Get-Command $c -EA SilentlyContinue
    if ($cmd) { $python = $cmd.Source; break }
}

Banner 'step 2 of 2   build the website   -   the same build as Compile-Website.bat'
$sw = [System.Diagnostics.Stopwatch]::StartNew()
$err = $null
if (-not (Test-Path -LiteralPath $webDir)) {
    $err = ('no website folder at {0}' -f $webDir)
} elseif (-not $python) {
    $err = 'Python not found on PATH'
} else {
    Write-Host ('   website : {0}' -f $webDir)
    Write-Host ('   python  : {0}' -f $python)
    Push-Location -LiteralPath $repo
    try {
        foreach ($b in $build) {
            $py = Join-Path $webScripts $b.Script
            if (-not (Test-Path -LiteralPath $py)) { $err = ('{0} not in Scripts\Website' -f $b.Script); break }
            if (-not $Apply) { Write-Host ('   would run : {0}   ({1})' -f $b.Script, $b.What); continue }
            Write-Host ''
            Write-Host ('-- {0}   ({1})' -f $b.Script, $b.What)
            & $python $py
            if ($LASTEXITCODE -ne 0) { $err = ('{0} exited {1}' -f $b.Script, $LASTEXITCODE); break }
        }
        if (-not $err) {
            $quarto = Find-Quarto
            if ($SkipRender) {
                Write-Host '   quarto render skipped (-SkipRender)'
            } elseif (-not $quarto) {
                $err = 'quarto not found (on PATH, in Program Files or in RStudio) - render skipped'
            } elseif (-not $Apply) {
                Write-Host '   would run : quarto render   (in E Website)'
            } else {
                Write-Host ''
                Write-Host '-- quarto render'
                Push-Location -LiteralPath $webDir
                try { & $quarto render; if ($LASTEXITCODE -ne 0) { $err = ('quarto render exited {0}' -f $LASTEXITCODE) } }
                finally { Pop-Location }
            }
        }
    } catch { $err = $_.Exception.Message }
    finally { Pop-Location }
}
$sw.Stop()
if ($err) { Write-Host ('   FAILED: {0}' -f $err) }
$results.Add([pscustomobject]@{
    Step=2; Name='Build-Website'
    Status=$(if ($err) { 'FAILED' } else { 'ok' })
    Seconds=[int]$sw.Elapsed.TotalSeconds; Note=$err }) | Out-Null

# --- summary ------------------------------------------------------------------

Banner ("Summary  [{0}]" -f $mode)
Write-Host ("{0,3}  {1,-16} {2,-10} {3,6}  {4}" -f '#', 'Step', 'Result', 'Secs', 'Note')
Write-Host ("{0,3}  {1,-16} {2,-10} {3,6}  {4}" -f '---', ('-' * 16), ('-' * 10), '-----', ('-' * 20))
foreach ($r in ($results | Sort-Object Step)) {
    Write-Host ("{0,3}  {1,-16} {2,-10} {3,6}  {4}" -f $r.Step, $r.Name, $r.Status, $r.Seconds, $r.Note)
}

$bad = @($results | Where-Object { $_.Status -eq 'FAILED' -or $_.Status -eq 'missing' })
Write-Host ''
if ($bad.Count -eq 0) { Write-Host 'Both steps completed. Open E Website\_site\index.html to check the site.' }
else { foreach ($b in $bad) { Write-Host ("   {0}  {1}" -f $b.Name, $b.Note) } }

if (-not $Apply) {
    Write-Host ''
    Write-Host 'PREVIEW only - nothing was changed. Run Run\Master-Website.bat to apply.'
}

try { Stop-Transcript | Out-Null } catch { }
Write-Host ''
Write-Host ("Log: {0}" -f $transcript)
