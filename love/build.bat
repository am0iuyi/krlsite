@echo off
echo >>> Collecting static files...
python manage.py collectstatic --noinput

echo >>> Applying database migrations...
python manage.py migrate

echo >>> Build completed successfully!
pause