#requires -Version 5.1
<#
    Publish-Ftp.ps1
    Uploads the rendered site - the website folder's _site\ - to the web server.

    CREDENTIALS
    It reads FTP-Login.txt at the top of the repository. One setting per line:

        host     = ftp.example.com
        user     = someone
        password = ********
        remote   = /public_html
        protocol = ftp            (ftp, ftps or sftp - ftp if left out)

    If FTP-Login.txt is not there it falls back to the website folder's own
    deploy.bat, if one exists.

    It uses WinSCP. "synchronize remote" uploads what changed; a second pass
    with -delete makes the server's papers/ match _site\papers, so files the
    site no longer links to are removed - the same as Push-Website.bat.

    Nothing local is changed. -WhatIf asks WinSCP to list the transfers without
    making them.

    Usage
        called by Engine\End-Day.ps1, or on its own:
        powershell -File Steps\Publish-Ftp.ps1 -Apply
#>

[CmdletBinding()]
param(
    [switch]$Apply,
    [switch]$WhatIf
)

$ErrorActionPreference = 'Continue'

$me      = Split-Path -Parent $MyInvocation.MyCommand.Path      # ...\Steps
$scripts = Split-Path -Parent $me                                # ...\<n>.Scripts
$repo    = [IO.Path]::GetFullPath((Join-Path $scripts '..\..\..'))   # Scripts\Papers -> the repository root
$web     = Get-Item -LiteralPath (Join-Path $repo 'E Website') -EA SilentlyContinue   # the website folder
if (-not $web) { Write-Host ('   no E Website folder in {0}' -f $repo); exit 1 }

$site = Join-Path $web.FullName '_site'
if (-not (Test-Path -LiteralPath $site)) {
    Write-Host ('   {0}\_site does not exist - render the site first.' -f $web.Name)
    exit 1
}
$pages = @(Get-ChildItem -LiteralPath $site -File -Recurse -EA SilentlyContinue)
Write-Host ('   source : {0}   ({1} file(s))' -f $site, $pages.Count)

# --- WinSCP -------------------------------------------------------------------

$winscp = $null
foreach ($c in @('C:\Program Files (x86)\WinSCP\WinSCP.com',
                 'C:\Program Files\WinSCP\WinSCP.com')) {
    if (Test-Path -LiteralPath $c) { $winscp = $c; break }
}
if (-not $winscp) {
    $cmd = Get-Command WinSCP.com -EA SilentlyContinue
    if ($cmd) { $winscp = $cmd.Source }
}
if (-not $winscp) {
    Write-Host '   WinSCP not found. Install it, or put WinSCP.com on PATH.'
    exit 1
}
Write-Host ('   winscp : {0}' -f $winscp)

# --- credentials --------------------------------------------------------------

$cred = Join-Path $repo 'FTP-Login.txt'   # at the repository root, git-ignored
$cfg  = @{}
if (Test-Path -LiteralPath $cred) {
    foreach ($line in (Get-Content -LiteralPath $cred -EA SilentlyContinue)) {
        if ($line -match '^\s*#') { continue }
        if ($line -match '^\s*([A-Za-z]+)\s*=\s*(.+?)\s*$') { $cfg[$Matches[1].ToLower()] = $Matches[2] }
    }
}

$haveCfg = $cfg.ContainsKey('host') -and $cfg.ContainsKey('user') -and $cfg.ContainsKey('password')

if (-not $haveCfg) {
    $deploy = Join-Path $web.FullName 'deploy.bat'
    if (-not (Test-Path -LiteralPath $deploy)) {
        Write-Host ''
        Write-Host ('   No credentials. Write them into {0}' -f $cred)
        Write-Host '   as host / user / password / remote, one per line.'
        exit 1
    }
    Write-Host ''
    Write-Host ('   FTP-Login.txt not found - falling back to {0}\deploy.bat' -f $web.Name)
    if (-not $Apply) { Write-Host '   PREVIEW - deploy.bat not run.'; exit 0 }
    Push-Location -LiteralPath $web.FullName
    try {
        & cmd.exe /c ('"' + $deploy + '"')
        $rc = $LASTEXITCODE
    } finally { Pop-Location }
    if ($rc -eq 0) { Write-Host '   deploy.bat finished.' } else { Write-Host ('   deploy.bat exited {0}' -f $rc) }
    exit $rc
}

$proto  = if ($cfg.ContainsKey('protocol')) { $cfg['protocol'] } else { 'ftp' }
$remote = if ($cfg.ContainsKey('remote'))   { $cfg['remote']   } else { '/public_html' }
Write-Host ('   target : {0}://{1}{2}   as {3}' -f $proto, $cfg['host'], $remote, $cfg['user'])

# WinSCP wants its own URL escaping for anything odd in a password.
function Esc([string]$s) {
    $out = ''
    foreach ($ch in $s.ToCharArray()) {
        if ($ch -match '[A-Za-z0-9._~-]') { $out += $ch }
        else { $out += ('%{0:X2}' -f [int][char]$ch) }
    }
    return $out
}

$open = ('open {0}://{1}:{2}@{3}/' -f $proto, (Esc $cfg['user']), (Esc $cfg['password']), $cfg['host'])
# Two commands, as in Push-Website.bat: upload the whole site, then make the
# server's papers/ match the built one, so files the site no longer links to are
# deleted there. Nothing outside papers/ is ever deleted on the server.
$pv = if ($WhatIf) { '-preview ' } else { '' }
$sync      = ('synchronize remote {0}"{1}" "{2}"' -f $pv, $site, $remote)
$syncPaper = ('synchronize remote {0}-delete "{1}" "{2}/papers"' -f $pv, (Join-Path $site 'papers'), $remote.TrimEnd('/'))

if (-not $Apply) {
    Write-Host ''
    Write-Host '   PREVIEW - nothing uploaded. Run with -Apply.'
    exit 0
}

# The password is passed to WinSCP as an argument and is never written to a log
# or echoed here. /log is deliberately not set for the same reason.
$wsArgs = @(
    '/command',
    ('"' + $open.Replace('"','""') + '"'),
    '"option batch abort"',
    '"option confirm off"',
    ('"' + $sync.Replace('"','""') + '"'),
    ('"' + $syncPaper.Replace('"','""') + '"'),
    '"exit"'
) -join ' '

$p = Start-Process -FilePath $winscp -ArgumentList $wsArgs -NoNewWindow -Wait -PassThru
if ($p.ExitCode -eq 0) {
    Write-Host ''
    Write-Host '   uploaded.'
} else {
    Write-Host ''
    Write-Host ('   WinSCP exited {0} - nothing was uploaded, or only part of it was.' -f $p.ExitCode)
}
exit $p.ExitCode
