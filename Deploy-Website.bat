@echo off
rem Deploy the website in one go: Compile-Website.bat (copy papers, rewrite Research pages, build with Quarto),
rem then Push-Website.bat (upload the built site and delete retired files).
rem To upload without rebuilding, run Push-Website.bat on its own.
call "%~dp0Compile-Website.bat" <NUL
if errorlevel 1 exit /b 1
call "%~dp0Push-Website.bat"
