@rem The FTP login is read from 8.Scripts\Reference\_ftp.txt, which .gitignore
@rem excludes (format: 8.Scripts\Reference\_ftp.txt.example). Never put it here.
@set "FTPCFG=%~dp0..\8.Scripts\Reference\_ftp.txt"
@if not exist "%FTPCFG%" (echo Missing %FTPCFG% - copy _ftp.txt.example to _ftp.txt and fill it in. & pause & exit /b 1)
@set "FTP_remote=/public_html"
@for /f "usebackq eol=# tokens=1,* delims== " %%A in ("%FTPCFG%") do @set "FTP_%%A=%%B"
quarto render
"C:\Program Files (x86)\WinSCP\WinSCP.com" /command ^
    "open ftp://%FTP_user%:%FTP_password%@%FTP_host%/" ^
    "synchronize remote _site %FTP_remote%" ^
    "exit"
pause 
