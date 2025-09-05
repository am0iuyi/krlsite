#!/usr/bin/env bash
set -o errexit

echo ">>> Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo ">>> Force installing whitenoise..."
pip install whitenoise==6.6.0

echo ">>> Collecting static files..."
python manage.py collectstatic --noinput

echo ">>> Applying database migrations..."
python manage.py migrate
