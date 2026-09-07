@echo off
setlocal EnableExtensions
title GraphPlot V4.4.5 - Debug Local
cd /d "%~dp0..\.."

python launcher_helper.py --mode debug --port 8800
echo.
pause
