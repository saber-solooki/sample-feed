#!/bin/bash
/usr/local/bin/gunicorn ${WEB_APP_NAME}.wsgi:application -w -2 -b :8000 &
/etc/init.d/celeryd start &
flower -A ${WEB_APP_NAME} --port=8181
