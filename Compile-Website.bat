@echo off
rem Compile the website: copy every paper, brief, overview and deck into the site's papers folder,
rem then build the site with Quarto. Nothing is uploaded. Run Deploy-Website.bat to put it online.
setlocal
cd /d "%~dp0"
echo.
echo   1/2  Copying papers into D Website\papers ...
python "%~dp0F Writing Instructions\Scripts\Website\publish_series.py"
if errorlevel 1 (echo Copy step failed - is Python installed? & pause & exit /b 1)
echo   Making the web version of each paper from its master .qmd ...
python "%~dp0F Writing Instructions\Scripts\Website\build_web_papers.py"
if errorlevel 1 (echo Web-paper step failed. & pause & exit /b 1)
echo   Writing the Research pages from the papers' current titles and abstracts ...
python "%~dp0F Writing Instructions\Scripts\Website\build_research_pages.py"
call :findquarto
if not defined QUARTO (echo Quarto not found - install Quarto or RStudio. & pause & exit /b 1)
echo.
echo   2/2  Building the site with Quarto ...
cd /d "%~dp0D Website"
"%QUARTO%" render
echo.
echo   Done. Open D Website\_site\index.html to check it, then run Deploy-Website.bat.
pause
exit /b 0

:findquarto
set "QUARTO="
for %%Q in (quarto.exe quarto.cmd) do if not defined QUARTO for %%P in (%%~$PATH:Q) do set "QUARTO=%%~fP"
for %%D in ("C:\Program Files\Quarto\bin" "C:\Program Files\RStudio\resources\app\bin\quarto\bin" "C:\Program Files\RStudio\resources\app\quarto\bin") do if not defined QUARTO if exist "%%~D\quarto.exe" set "QUARTO=%%~D\quarto.exe"
exit /b 0
