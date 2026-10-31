@echo off
rem Push the website: upload the already-built site (D Website\_site) to the web server (WinSCP if installed,
rem otherwise Python's built-in FTP - nothing to install),
rem then delete files that were retired from the site. It does not compile: run Compile-Website.bat first,
rem or Deploy-Website.bat to do both.
rem The FTP login is read from FTP-Login.txt, next to this file (host, user, password, remote, protocol, url).
rem After uploading it checks research.html on the server and, if FTP-Login.txt has url = ..., on the live website.
setlocal
cd /d "%~dp0"
set "FTPCFG=%~dp0FTP-Login.txt"
if not exist "%FTPCFG%" (echo FTP login not found. Create FTP-Login.txt next to this file with lines host = , user = , password = , remote = /public_html. & pause & exit /b 1)
for /f "usebackq eol=# tokens=1,* delims== " %%A in ("%FTPCFG%") do set "FTP_%%A=%%B"
if not defined FTP_remote set "FTP_remote=/public_html"
set "WINSCP=C:\Program Files (x86)\WinSCP\WinSCP.com"
if not exist "%WINSCP%" set "WINSCP=C:\Program Files\WinSCP\WinSCP.com"

if not exist "%~dp0D Website\_site\index.html" (echo No built site yet - run Compile-Website.bat first. & pause & exit /b 1)
echo.
if not exist "%WINSCP%" goto python_upload
echo   Uploading D Website\_site to %FTP_remote% with WinSCP ...
"%WINSCP%" /command ^
    "open ftp://%FTP_user%:%FTP_password%@%FTP_host%/" ^
    "synchronize remote ""%~dp0D Website\_site"" %FTP_remote%" ^
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
python "%~dp0F Writing Instructions\Scripts\Website\deploy_ftp.py" "%FTPCFG%" "%~dp0D Website\_site" --check
echo.
pause
exit /b 0

:python_upload
rem No WinSCP: upload with Python's built-in FTP (only changed files are sent).
echo   Uploading D Website\_site to the server with Python ...
python "%~dp0F Writing Instructions\Scripts\Website\deploy_ftp.py" "%FTPCFG%" "%~dp0D Website\_site"
echo.
pause
