#!/bin/bash

# Stop the navlab screen session
screen -S navlab -X quit

# Wait for a few seconds to ensure the session is stopped
sleep 5

# Restart the navlab screen session
export PRODUCTION=True && screen -dmS navlab python3 /home/pi/navlab/app.py
