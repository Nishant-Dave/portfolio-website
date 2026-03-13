#!/bin/bash
mkdir -p staticfiles_build/static
pip install -r requirements.txt --no-cache-dir
python3.9 manage.py collectstatic --noinput --clear
