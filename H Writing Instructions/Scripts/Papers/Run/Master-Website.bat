@echo off
setlocal
cd /d "%~dp0..\..\..\.."
cls
echo.
echo   ============================================================
echo     A Writing  -  website
echo   ============================================================
echo.
echo     Build-Website   the same build as Compile-Website.bat at the top
echo                     of the repository: every paper into
echo                     E Website\PaperArchive, the web papers, the section
echo                     pages, E Website\papers with only the linked files,
echo                     then quarto render. Nothing is uploaded.
echo.
echo   PDFs are not built from here. Run-Website.ps1 -Pdf builds them
echo   with Word, one document per process with a time limit.
echo.
echo   Check the result in E Website\_site\index.html.
echo.
set /p go=Type Y then Enter to run, anything else to cancel: 
if /i not "%go%"=="Y" goto cancel
echo.
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0..\Engine\Run-Website.ps1" -Apply <NUL
echo.
pause
goto done
:cancel
echo.
echo Cancelled. Nothing was changed.
pause
:done
endlocal
