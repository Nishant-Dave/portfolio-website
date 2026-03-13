#!/bin/bash
echo "Building the project..."
python3.9 -m pip install -r requirements.txt

echo "Make Static Directory..."
mkdir -p staticfiles_build/static

echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear
echo "Build Finished!"
