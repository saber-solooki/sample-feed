from celery.schedules import crontab

from feedy import settings

result_backend = 'rpc://'
result_persistent = False

timezone = settings.TIME_ZONE
enable_utc = True


CELERY_BEAT_SCHEDULE = {
    'fetch_feed': {
        'task': 'rss_feed.tasks.fetch_feed',
        'schedule': crontab(hour='*/1')
    },
}

MAX_RETRIES_FOR_BASIC_DATA = 3
RETRY_DELAY = 15 * 60

