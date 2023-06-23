# !/bin/bash

cd /home/arnol/projects/weather-forecast/

git pull origin main

source .venv/bin/activate

python3 twilio_script.py

echo "the message was sent yet successfully!"