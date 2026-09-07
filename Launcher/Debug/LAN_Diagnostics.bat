@echo off
setlocal EnableExtensions
title GraphPlot V4.4.5 - LAN Diagnostics
cd /d "%~dp0..\.."

python launcher_helper.py --mode lan-info --port 8800

echo.
echo Windows network profile:
powershell -NoProfile -Command "Get-NetConnectionProfile | Format-Table Name,InterfaceAlias,NetworkCategory,IPv4Connectivity -AutoSize"

echo.
pause
