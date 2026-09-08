@echo off
setlocal EnableExtensions
title SignalWorks Studio V4.4.5 - Dedicated LAN Server

set "APP_FILE=SignalWorks_Studio_webserv_v4_4_5.py"
set "PORT=8800"

cd /d "%~dp0..\.."

echo.
echo ==================================================================
echo   SignalWorks Studio V4.4.5 - Dedicated LAN Server
echo ==================================================================
echo   Port          : %PORT%
echo   Server browser: OFF
echo   Auto shutdown : OFF
echo ==================================================================
echo.

if not exist "%APP_FILE%" (
    echo [ERROR] Cannot find %APP_FILE%
    pause
    exit /b 1
)

where python >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python was not found in PATH.
    pause
    exit /b 1
)

echo Keep this window open while SignalWorks Studio is in service.
echo Press CTRL+C to stop the server.
echo.

python "%APP_FILE%" --lan --port %PORT% --no-browser --no-auto-shutdown

set "RC=%ERRORLEVEL%"
echo.
echo SignalWorks Studio Server stopped. Exit code: %RC%
pause
exit /b %RC%
