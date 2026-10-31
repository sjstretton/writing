@echo off
cd /d "%~dp0..\..\..\.."
cls
echo.
echo Website build, PREVIEW only. Nothing is changed.
echo.
pause
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0..\Engine\Run-Website.ps1" <NUL
echo.
pause
