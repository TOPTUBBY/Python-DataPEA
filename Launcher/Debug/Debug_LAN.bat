@echo off
setlocal EnableExtensions
title SignalWorks Studio V4.4.5 - Debug LAN
cd /d "%~dp0..\.."

python signalworks_studio_launcher.py --mode debug --lan --port 8800
echo.
pause
