@echo off
rem Compile the website: render every paper, brief, overview, book and deck to PDF, copy every paper, brief, overview and deck into E Website\PaperArchive, build the web pages,
rem put only the files the pages link to into E Website\papers, write the index.html in each paper folder,
rem then build the site with Quarto. Nothing is uploaded. Run Deploy-Website.bat to put it online.
setlocal
cd /d "%~dp0"
echo.
echo   0/2  Rendering the PDF of every paper, brief, overview, book and deck (Quarto + Typst; LibreOffice for decks) ...
python "%~dp0H Writing Instructions\Scripts\Website\render_pdfs.py"
if errorlevel 1 (echo Some PDFs did not render - see above. The site links PDFs only, so those files will have no download link.)
echo.
echo   1/2  Copying papers into E Website\PaperArchive ...
python "%~dp0H Writing Instructions\Scripts\Website\publish_series.py"
if errorlevel 1 (echo Copy step failed - is Python installed? & pause & exit /b 1)
echo   Making the web version of each paper from its master .qmd ...
python "%~dp0H Writing Instructions\Scripts\Website\build_web_papers.py"
if errorlevel 1 (echo Web-paper step failed. & pause & exit /b 1)
echo   Writing the Research pages from the papers' current titles and abstracts ...
python "%~dp0H Writing Instructions\Scripts\Website\build_research_pages.py"
echo   Writing index.html in B Theory and Research, C Policy and FInance and D Modelling ...
python "%~dp0H Writing Instructions\Scripts\Website\build_folder_index.py"
call :findquarto
if not defined QUARTO (echo Quarto not found - install Quarto or RStudio. & pause & exit /b 1)
echo.
echo   2/2  Building the site with Quarto ...
cd /d "%~dp0E Website"
"%QUARTO%" render
echo.
echo   Done. Open E Website\_site\index.html to check it, then run Deploy-Website.bat.
pause
exit /b 0

:findquarto
set "QUARTO="
for %%Q in (quarto.exe quarto.cmd) do if not defined QUARTO for %%P in (%%~$PATH:Q) do set "QUARTO=%%~fP"
for %%D in ("C:\Program Files\Quarto\bin" "C:\Program Files\RStudio\resources\app\bin\quarto\bin" "C:\Program Files\RStudio\resources\app\quarto\bin") do if not defined QUARTO if exist "%%~D\quarto.exe" set "QUARTO=%%~D\quarto.exe"
exit /b 0
