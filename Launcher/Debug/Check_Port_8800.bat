@echo off
setlocal EnableExtensions
title SignalWorks Studio V4.4.5 - Port 8800 Inspection
cd /d "%~dp0..\.."

python signalworks_studio_launcher.py --mode inspect --port 8800
echo.
pause
