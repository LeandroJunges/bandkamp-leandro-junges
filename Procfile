web: python manage.py collectstatic --no-input \
    && python manage.py migrate \
    && gunicorn bandkamp.wsgi --log-level debug