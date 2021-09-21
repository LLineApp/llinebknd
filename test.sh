#!/bin/bash 
python3.6 -m venv venv
source venv/bin/activate
reset
python manage.py test