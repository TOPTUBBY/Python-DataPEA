@echo off
setlocal EnableExtensions
title GraphPlot V4.4.5 - Stable LAN
cd /d "%~dp0..\.."

echo Starting GraphPlot V4.4.5 in LAN mode...
echo Close all GraphPlot browser tabs to stop the server automatically.
echo.

python launcher_helper.py --mode stable --lan --port 8800
set "RC=%ERRORLEVEL%"

if not "%RC%"=="0" (
    echo.
    echo GraphPlot did not start. Review the message above.
    pause
)
exit /b %RC%
