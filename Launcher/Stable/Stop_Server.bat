@echo off
setlocal EnableExtensions
title SignalWorks Studio V4.4.5 - Stop Server
cd /d "%~dp0..\.."

python signalworks_studio_launcher.py --mode stop --port 8800
echo.
pause
