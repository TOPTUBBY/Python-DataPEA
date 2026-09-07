@echo off
setlocal EnableExtensions
title GraphPlot V4.4.5 - Debug LAN
cd /d "%~dp0..\.."

python launcher_helper.py --mode debug --lan --port 8800
echo.
pause
