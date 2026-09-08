@echo off
setlocal EnableExtensions
title SignalWorks Studio V4.4.5 - Library Installer

echo ================================================================
echo   SignalWorks Studio V4.4.5
echo   Python Library Installer
echo ================================================================
echo.

REM ---------------------------------------------------------------
REM Find Python
REM ---------------------------------------------------------------
set "PY_CMD="

where python >nul 2>&1
if not errorlevel 1 (
    set "PY_CMD=python"
    goto :python_found
)

where py >nul 2>&1
if not errorlevel 1 (
    set "PY_CMD=py -3"
    goto :python_found
)

echo [ERROR] Python was not found.
echo.
echo Please install Python 3 first and enable:
echo   "Add Python to PATH"
echo.
pause
exit /b 1

:python_found
echo [INFO] Python command: %PY_CMD%
%PY_CMD% --version
if errorlevel 1 goto :failed

echo.
echo ================================================================
echo [1/3] Updating pip / setuptools / wheel...
echo ================================================================
%PY_CMD% -m pip install --upgrade pip setuptools wheel
if errorlevel 1 goto :failed

echo.
echo ================================================================
echo [2/3] Installing SignalWorks Studio V4.4.5 required libraries...
echo ================================================================

REM WebServer
%PY_CMD% -m pip install "fastapi>=0.100" "uvicorn>=0.20" "python-multipart>=0.0.6"
if errorlevel 1 goto :failed

REM Data processing and plotting
%PY_CMD% -m pip install "pandas>=1.5" "numpy>=1.23" "matplotlib>=3.6" "plotly>=5.18"
if errorlevel 1 goto :failed

REM Word report export
%PY_CMD% -m pip install "python-docx>=0.8.11"
if errorlevel 1 goto :failed

REM Image support used by Matplotlib/report assets.
REM Pillow is normally installed automatically with Matplotlib,
REM but it is installed explicitly here for a reliable fresh PC setup.
%PY_CMD% -m pip install Pillow
if errorlevel 1 goto :failed

echo.
echo ================================================================
echo [3/3] Verifying installed libraries...
echo ================================================================
%PY_CMD% -c "import fastapi, uvicorn, multipart, pandas, numpy, matplotlib, plotly, docx, PIL; print('All SignalWorks Studio V4.4.5 libraries imported successfully.')"
if errorlevel 1 goto :verify_failed

echo.
echo ================================================================
echo   INSTALLATION SUCCESSFUL
echo ================================================================
echo.
echo Installed/verified:
echo   - FastAPI
echo   - Uvicorn
echo   - python-multipart
echo   - pandas
echo   - NumPy
echo   - Matplotlib
echo   - Plotly
echo   - python-docx
echo   - Pillow
echo.
echo SignalWorks Studio V4.4.5 is ready to run.
echo.
pause
exit /b 0

:verify_failed
echo.
echo [ERROR] Installation finished, but one or more libraries
echo         could not be imported.
echo.
echo Please review the error shown above.
pause
exit /b 2

:failed
echo.
echo ================================================================
echo   INSTALLATION FAILED
echo ================================================================
echo.
echo Please check:
echo   1. Internet connection
echo   2. Company proxy / firewall settings
echo   3. Python installation
echo   4. pip permission
echo.
echo If Windows permission is blocking pip, try opening
echo Command Prompt as Administrator and run this BAT again.
echo.
pause
exit /b 1
