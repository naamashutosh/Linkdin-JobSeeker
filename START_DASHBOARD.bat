@echo off
title LinkedIn Job History Dashboard

echo ============================================
echo   LinkedIn Job History Dashboard
echo   Opens at: http://localhost:5000
echo ============================================
echo.

set "PATH=%PATH%;C:\Users\rohit\AppData\Local\Programs\Python\Python311"
set "PATH=%PATH%;C:\Users\rohit\AppData\Local\Programs\Python\Python311\Scripts"

cd /d "C:\Users\rohit\Auto_job_applier_linkedIn"

echo Starting dashboard...
start "" http://localhost:5000
C:\Users\rohit\AppData\Local\Programs\Python\Python311\python.exe app.py

pause
