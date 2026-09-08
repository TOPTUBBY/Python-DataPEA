@echo off
setlocal EnableExtensions
title SignalWorks Studio V4.4.5 - Debug Local
cd /d "%~dp0..\.."

python signalworks_studio_launcher.py --mode debug --port 8800
echo.
pause
