@echo off
title Resume Generator Demo

echo ============================================
echo   Custom Resume Demo Generator
echo   Generates 4 sample PDFs for different jobs
echo ============================================
echo.

set "PATH=%PATH%;C:\Users\rohit\AppData\Local\Programs\Python\Python311"
set "PATH=%PATH%;C:\Users\rohit\AppData\Local\Programs\Python\Python311\Scripts"
set "PATH=%PATH%;C:\Users\rohit\AppData\Local\Programs\MiKTeX\miktex\bin\x64"

cd /d "C:\Users\rohit\Auto_job_applier_linkedIn"

C:\Users\rohit\AppData\Local\Programs\Python\Python311\python.exe demo_resume.py

echo.
echo Done! Check: C:\Users\rohit\Auto_job_applier_linkedIn\all resumes\Demo_*
pause
