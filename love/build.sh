#!/usr/bin/env bash
set -o errexit

echo ">>> Collecting static files..."
python manage.py collectstatic --noinput --clear

echo ">>> Applying database migrations..."
python manage.py migrate