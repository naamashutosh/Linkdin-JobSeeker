@echo off
title LinkedIn Auto Job Applier

echo ============================================
echo   LinkedIn Auto Job Applier
echo   Powered by Ollama + LaTeX Resume Engine
echo ============================================
echo.

REM Set required PATH entries
set "PATH=%PATH%;C:\Users\rohit\AppData\Local\Programs\Python\Python311"
set "PATH=%PATH%;C:\Users\rohit\AppData\Local\Programs\Python\Python311\Scripts"
set "PATH=%PATH%;C:\Users\rohit\AppData\Local\Programs\MiKTeX\miktex\bin\x64"
set "PATH=%PATH%;C:\Users\rohit\AppData\Local\Programs\Ollama"

REM Change to project directory
cd /d "C:\Users\rohit\Auto_job_applier_linkedIn"

echo Starting bot...
echo.

C:\Users\rohit\AppData\Local\Programs\Python\Python311\python.exe runAiBot.py

echo.
echo Bot finished. Press any key to close.
pause
