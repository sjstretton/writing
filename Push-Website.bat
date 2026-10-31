@echo off
rem Push the website: upload the already-built site (B Working Papers\A.Website\_site) to the web server (WinSCP if installed,
rem otherwise Python's built-in FTP - nothing to install),
rem then delete files that were retired from the site. It does not compile: run Compile-Website.bat first,
rem or Deploy-Website.bat to do both.
rem The FTP login is read from _ftp.txt (git-ignored; format in _ftp.txt.example):
rem   E Writing Instructions\Scripts\Papers\Reference\_ftp.txt   (new place)
rem   B Working Papers\B.Scripts\Reference\_ftp.txt               (old place, still read if present)
rem After uploading it checks research.html on the server and, if _ftp.txt has url = ..., on the live website.
setlocal
cd /d "%~dp0"
set "FTPCFG=%~dp0E Writing Instructions\Scripts\Papers\Reference\_ftp.txt"
if not exist "%FTPCFG%" set "FTPCFG=%~dp0B Working Papers\B.Scripts\Reference\_ftp.txt"
if not exist "%FTPCFG%" (echo FTP login not found. Copy E Writing Instructions\Scripts\Papers\Reference\_ftp.txt.example to _ftp.txt there and fill it in. & pause & exit /b 1)
for /f "usebackq eol=# tokens=1,* delims== " %%A in ("%FTPCFG%") do set "FTP_%%A=%%B"
if not defined FTP_remote set "FTP_remote=/public_html"
set "WINSCP=C:\Program Files (x86)\WinSCP\WinSCP.com"
if not exist "%WINSCP%" set "WINSCP=C:\Program Files\WinSCP\WinSCP.com"

if not exist "%~dp0B Working Papers\A.Website\_site\index.html" (echo No built site yet - run Compile-Website.bat first. & pause & exit /b 1)
echo.
if not exist "%WINSCP%" goto python_upload
echo   Uploading B Working Papers\A.Website\_site to %FTP_remote% with WinSCP ...
"%WINSCP%" /command ^
    "open ftp://%FTP_user%:%FTP_password%@%FTP_host%/" ^
    "synchronize remote ""%~dp0B Working Papers\A.Website\_site"" %FTP_remote%" ^
    "option batch continue" ^
    "rm %FTP_remote%/papers/SustainabilityLinkedLending.pdf" ^
    "rm %FTP_remote%/papers/MDBClimateEnvelope.docx" ^
    "rm %FTP_remote%/papers/GeoprosperityIntro.docx" ^
    "rm %FTP_remote%/papers/CombinedOverview.docx" ^
    "exit"
echo.
echo   Done. Errors from the rm lines just mean those retired files are already gone.
echo.
echo   Checking that the server and the live website have the new pages ...
python "%~dp0E Writing Instructions\Scripts\Website\deploy_ftp.py" "%FTPCFG%" "%~dp0B Working Papers\A.Website\_site" --check
echo.
pause
exit /b 0

:python_upload
rem No WinSCP: upload with Python's built-in FTP (only changed files are sent).
echo   Uploading B Working Papers\A.Website\_site to the server with Python ...
python "%~dp0E Writing Instructions\Scripts\Website\deploy_ftp.py" "%FTPCFG%" "%~dp0B Working Papers\A.Website\_site"
echo.
pause
