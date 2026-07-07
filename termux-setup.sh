#!/data/data/com.termux/files/usr/bin/bash
clear
echo "========================================"
echo "   BOMBER - Termux Setup"
echo "   Created by ihosi"
echo "========================================"
echo ""
echo "Updating packages..."
pkg update && pkg upgrade -y
echo "Installing Python..."
pkg install python python-pip -y
echo "Installing requirements..."
pip install -r requirements.txt
echo "Giving execute permission..."
chmod +x bomber.py
echo ""
echo "Setup complete!"
echo ""
echo "To run BOMBER:"
echo "  python bomber.py"
echo ""
echo "Press any key to start..."
read -n 1
python bomber.py