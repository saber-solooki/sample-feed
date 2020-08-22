#!/bin/bash

/usr/local/bin/gunicorn ${WEB_APP_NAME}.wsgi:application -w 3 -b :8000 &
/etc/init.d/celeryd start &
celery -A ${WEB_APP_NAME} beat -l info &
flower -A ${WEB_APP_NAME} --port=8181
