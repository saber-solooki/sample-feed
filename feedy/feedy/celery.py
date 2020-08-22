import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feedy.settings')

# app = Celery('feedy_tasks', broker=os.environ['CELERY_BROKER_URL'], backend=os.environ['CELERY_BACKEND_URL'])
app = Celery('feedy_tasks')

app.config_from_object('feedy.celerysetting', namespace='CELERY')

app.autodiscover_tasks(['rss_feed'])
