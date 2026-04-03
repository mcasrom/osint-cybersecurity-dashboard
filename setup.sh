#!/bin/bash

echo "lock OSINT Cybersecurity Dashboard - Setup"
echo "=========================================="

sudo apt update
sudo apt upgrade -y

echo "Installing system dependencies..."
sudo apt install -y python3 python3-pip python3-venv git curl wget build-essential tree

echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

mkdir -p data reports logs

if [ ! -f "config/config.yaml" ]; then
    cp config/config.example.yaml config/config.yaml
    echo "IMPORTANT: Edit config/config.yaml with your API keys"
fi

echo ""
echo "Setup completed!"
echo "Next steps:"
echo "1. source venv/bin/activate"
echo "2. bash run_dashboard.sh"
