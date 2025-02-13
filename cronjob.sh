#!/bin/sh
cd /app
python3 -m src.utils.xml_generator >> /var/log/cron/cron.log
python3 -m src.utils.scraper >> /var/log/cron/cron.log