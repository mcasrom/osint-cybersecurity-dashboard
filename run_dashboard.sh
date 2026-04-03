#!/bin/bash

echo "lock Starting OSINT Cybersecurity Dashboard..."

if [ ! -d "venv" ]; then
    echo "ERROR: Virtual environment not found. Run setup.sh first"
    exit 1
fi

source venv/bin/activate

mkdir -p data reports logs

echo "Starting Streamlit..."
echo "Access at: http://localhost:8506"

streamlit run app.py --server.port=8506 --server.address=0.0.0.0
