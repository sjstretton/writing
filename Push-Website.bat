@echo off
rem Push the website: upload the already-built site (E Website\_site) to the web server (WinSCP if installed,
rem otherwise Python's built-in FTP - nothing to install),
rem then make the server's papers folder match the site's (files no longer linked are deleted). It does not compile: run Compile-Website.bat first,
rem or Deploy-Website.bat to do both.
rem The FTP login is read from FTP-Login.txt, next to this file (host, user, password, remote, protocol, url).
rem After uploading it checks index.html on the server and, if FTP-Login.txt has url = ..., on the live website.
setlocal
cd /d "%~dp0"
set "FTPCFG=%~dp0FTP-Login.txt"
if not exist "%FTPCFG%" (echo FTP login not found. Create FTP-Login.txt next to this file with lines host = , user = , password = , remote = /public_html. & pause & exit /b 1)
for /f "usebackq eol=# tokens=1,* delims== " %%A in ("%FTPCFG%") do set "FTP_%%A=%%B"
if not defined FTP_remote set "FTP_remote=/public_html"
set "WINSCP=C:\Program Files (x86)\WinSCP\WinSCP.com"
if not exist "%WINSCP%" set "WINSCP=C:\Program Files\WinSCP\WinSCP.com"

if not exist "%~dp0E Website\_site\index.html" (echo No built site yet - run Compile-Website.bat first. & pause & exit /b 1)
echo.
if not exist "%WINSCP%" goto python_upload
echo   Uploading E Website\_site to %FTP_remote% with WinSCP ...
"%WINSCP%" /command ^
    "open ftp://%FTP_user%:%FTP_password%@%FTP_host%/" ^
    "synchronize remote ""%~dp0E Website\_site"" %FTP_remote%" ^
    "synchronize remote -delete ""%~dp0E Website\_site\papers"" %FTP_remote%/papers" ^
    "synchronize remote -delete ""%~dp0E Website\_site\policy"" %FTP_remote%/policy" ^
    "synchronize remote -delete ""%~dp0E Website\_site\modelling"" %FTP_remote%/modelling" ^
    "exit"
echo.
echo   Done. The server's papers, policy and modelling folders now hold only what the site has.
echo.
echo   Checking that the server and the live website have the new pages ...
python "%~dp0H Writing Instructions\Scripts\Website\deploy_ftp.py" "%FTPCFG%" "%~dp0E Website\_site" --check
echo.
pause
exit /b 0

:python_upload
rem No WinSCP: upload with Python's built-in FTP (only changed files are sent).
echo   Uploading E Website\_site to the server with Python ...
python "%~dp0H Writing Instructions\Scripts\Website\deploy_ftp.py" "%FTPCFG%" "%~dp0E Website\_site"
echo.
pause
