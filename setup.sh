#!/bin/bash
# AI Voice Assistant - Quick Setup Script for Mac/Linux
# This script automates the installation process

echo "============================================================"
echo "AI VOICE ASSISTANT - Quick Setup"
echo "============================================================"
echo

# Check Python version
echo "[1/5] Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python is not installed"
    echo "Please install Python 3.12 or higher"
    exit 1
fi
python3 --version
echo

# Create virtual environment
echo "[2/5] Creating virtual environment..."
if [ -d "venv" ]; then
    echo "Virtual environment already exists, skipping..."
else
    python3 -m venv venv
    echo "Virtual environment created!"
fi
echo

# Activate virtual environment
echo "[3/5] Activating virtual environment..."
source venv/bin/activate
echo

# Install dependencies
echo "[4/5] Installing dependencies..."
pip install -r requirements.txt
echo

# Setup .env file
echo "[5/5] Setting up environment variables..."
if [ -f ".env" ]; then
    echo ".env file already exists, skipping..."
else
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo ".env file created from template!"
        echo
        echo "IMPORTANT: Edit .env and add your API keys:"
        echo "  - DEEPGRAM_API_KEY (get from https://console.deepgram.com)"
        echo "  - GROQ_API_KEY (get from https://console.groq.com)"
    else
        echo ".env.example not found, skipping..."
    fi
fi
echo

echo "============================================================"
echo "Setup Complete!"
echo "============================================================"
echo
echo "Next steps:"
echo "  1. Edit .env file and add your API keys"
echo "  2. Run: python main.py"
echo
echo "To activate the virtual environment later, run:"
echo "  source venv/bin/activate"
echo
