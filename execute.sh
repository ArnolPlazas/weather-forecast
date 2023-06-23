# !/bin/bash


git pull origin main

source .venv/bin/activate

python3 twilio_script.py

echo "the message was sent yet successfully!"
