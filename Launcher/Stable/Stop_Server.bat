@echo off
setlocal EnableExtensions
title GraphPlot V4.4.5 - Stop Server
cd /d "%~dp0..\.."

python launcher_helper.py --mode stop --port 8800
echo.
pause
