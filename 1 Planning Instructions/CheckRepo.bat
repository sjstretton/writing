@echo off
REM Check the repo is consistent (IDs, links, printable, Sheet sync state). Needs Python with python-docx.
cd /d "%~dp0"
python Scripts\update.py check
pause
