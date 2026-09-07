@echo off
setlocal EnableExtensions
title GraphPlot V4.4.5 - Port 8800 Inspection
cd /d "%~dp0..\.."

python launcher_helper.py --mode inspect --port 8800
echo.
pause
