@echo off
rem Compile the website: copy every paper, brief, overview and deck into the site's papers folder,
rem then build the site with Quarto. Nothing is uploaded. Run Deploy-Website.bat to put it online.
setlocal
cd /d "%~dp0"
echo.
echo   1/2  Copying papers into B Working Papers\A.Website\papers ...
python "%~dp0E Writing Instructions\Scripts\Website\publish_series.py"
if errorlevel 1 (echo Copy step failed - is Python installed? & pause & exit /b 1)
call :findquarto
if not defined QUARTO (echo Quarto not found - install Quarto or RStudio. & pause & exit /b 1)
echo.
echo   2/2  Building the site with Quarto ...
cd /d "%~dp0B Working Papers\A.Website"
"%QUARTO%" render
echo.
echo   Done. Open B Working Papers\A.Website\_site\index.html to check it, then run Deploy-Website.bat.
pause
exit /b 0

:findquarto
set "QUARTO="
for %%Q in (quarto.exe quarto.cmd) do if not defined QUARTO for %%P in (%%~$PATH:Q) do set "QUARTO=%%~fP"
for %%D in ("C:\Program Files\Quarto\bin" "C:\Program Files\RStudio\resources\app\bin\quarto\bin" "C:\Program Files\RStudio\resources\app\quarto\bin") do if not defined QUARTO if exist "%%~D\quarto.exe" set "QUARTO=%%~D\quarto.exe"
exit /b 0
