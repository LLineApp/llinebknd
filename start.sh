#!/bin/bash 
python3.6 -m venv venv
source venv/bin/activate
python manage.py migrate
python manage.py runserver