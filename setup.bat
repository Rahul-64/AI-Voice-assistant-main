@echo off
REM AI Voice Assistant - Quick Setup Script for Windows
REM This script automates the installation process

echo ============================================================
echo AI VOICE ASSISTANT - Quick Setup
echo ============================================================
echo.

REM Check Python version
echo [1/5] Checking Python version...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.12 or higher from python.org
    pause
    exit /b 1
)
python --version
echo.

REM Create virtual environment
echo [2/5] Creating virtual environment...
if exist venv (
    echo Virtual environment already exists, skipping...
) else (
    python -m venv venv
    echo Virtual environment created!
)
echo.

REM Activate virtual environment
echo [3/5] Activating virtual environment...
call venv\Scripts\activate
echo.

REM Install dependencies
echo [4/5] Installing dependencies...
pip install -r requirements.txt
echo.

REM Setup .env file
echo [5/5] Setting up environment variables...
if exist .env (
    echo .env file already exists, skipping...
) else (
    if exist .env.example (
        copy .env.example .env
        echo .env file created from template!
        echo.
        echo IMPORTANT: Edit .env and add your API keys:
        echo   - DEEPGRAM_API_KEY (get from https://console.deepgram.com)
        echo   - GROQ_API_KEY (get from https://console.groq.com)
    ) else (
        echo .env.example not found, skipping...
    )
)
echo.

echo ============================================================
echo Setup Complete!
echo ============================================================
echo.
echo Next steps:
echo   1. Edit .env file and add your API keys
echo   2. Run: python main.py
echo.
echo To activate the virtual environment later, run:
echo   venv\Scripts\activate
echo.
pause
