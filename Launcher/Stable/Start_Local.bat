@echo off
setlocal EnableExtensions
title GraphPlot V4.4.5 - Stable Local
cd /d "%~dp0..\.."

echo Starting GraphPlot V4.4.5...
echo Close all GraphPlot browser tabs to stop the server automatically.
echo.

python launcher_helper.py --mode stable --port 8800
set "RC=%ERRORLEVEL%"

if not "%RC%"=="0" (
    echo.
    echo GraphPlot did not start. Review the message above.
    pause
)
exit /b %RC%
