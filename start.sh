#!/bin/bash
cd /home/pi/Bot/SquidBot
git pull
python3 main.py
cd /home/pi/Bot2/SquidBot
git pull
python3 main.py
