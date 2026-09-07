@echo off
setlocal EnableExtensions
title GraphPlot - Allow TCP Port 8800

net session >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Run this BAT as Administrator.
    pause
    exit /b 1
)

netsh advfirewall firewall delete rule name="GraphPlot TCP 8800" >nul 2>&1
netsh advfirewall firewall add rule name="GraphPlot TCP 8800" dir=in action=allow protocol=TCP localport=8800 profile=domain,private

echo.
echo GraphPlot TCP port 8800 is allowed for Domain/Private profiles.
pause
