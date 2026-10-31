@rem Deletes files that were removed from the site but are still on the web server.
@rem deploy.bat uploads new and changed files but never deletes old ones, so run this once after deploying.
@rem Uses the same FTP login as deploy.bat (B.Scripts\Reference\_ftp.txt).
@set "FTPCFG=%~dp0..\B.Scripts\Reference\_ftp.txt"
@if not exist "%FTPCFG%" (echo Missing %FTPCFG% & pause & exit /b 1)
@set "FTP_remote=/public_html"
@for /f "usebackq eol=# tokens=1,* delims== " %%A in ("%FTPCFG%") do @set "FTP_%%A=%%B"
"C:\Program Files (x86)\WinSCP\WinSCP.com" /command ^
    "option batch continue" ^
    "open ftp://%FTP_user%:%FTP_password%@%FTP_host%/" ^
    "rm %FTP_remote%/papers/SustainabilityLinkedLending.pdf" ^
    "rm %FTP_remote%/papers/MDBClimateEnvelope.docx" ^
    "rm %FTP_remote%/papers/GeoprosperityIntro.docx" ^
    "rm %FTP_remote%/papers/CombinedOverview.docx" ^
    "exit"
pause
