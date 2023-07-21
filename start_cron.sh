#!/bin/bash

crontab -l | { cat; echo "* * * * * cd /home && python3 /home/crawlers/run.py"; } | crontab -

chmod +x /home/crawlers/run.py

service cron start

bash