@echo off
setlocal EnableExtensions
title SignalWorks Studio V4.4.5 - Stable LAN
cd /d "%~dp0..\.."

echo Starting SignalWorks Studio V4.4.5 in LAN mode...
echo Close all SignalWorks Studio browser tabs to stop the server automatically.
echo.

python signalworks_studio_launcher.py --mode stable --lan --port 8800
set "RC=%ERRORLEVEL%"

if not "%RC%"=="0" (
    echo.
    echo SignalWorks Studio did not start. Review the message above.
    pause
)
exit /b %RC%
