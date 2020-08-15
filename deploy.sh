#!/bin/bash

cd Ayen
git pull origin master
source ~/.virtualenvs/ayen/bin/activate
pip install -r requirements.txt
python manage.py migrate
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl restart nginx
