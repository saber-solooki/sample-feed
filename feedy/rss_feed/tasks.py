import requests
import feedparser

from general.request_handler import RequestHandler
from rss_feed.feed_parser import parse_decorator
from rss_feed.utils import FeedAggregator

from rss_feed.data.add_feed_items_repo import AddFeedItemsRepoDBImpl
from rss_feed.domain.use_cases.add_feed_items import AddFeedItemsUseCase

from feedy import celerysetting
from feedy.celery import app
from rss_feed.models import Channel


@app.task
def fetch_feed():
    channels = Channel.objects.all()
    for channel in channels:
        fetch_feed_for_channel.delay(channel.id, channel.address)


@app.task(bind=True, autoretry_for=(requests.RequestException,),
          retry_kwargs={'max_retries': celerysetting.MAX_RETRIES_FOR_BASIC_DATA},
          default_retry_delay=celerysetting.RETRY_DELAY)
def fetch_feed_for_channel(self, channel_id, channel_address):
    feedparser.parse = parse_decorator(feedparser.parse)
    aggregator = FeedAggregator(RequestHandler(), feedparser)
    add_feed_item_use_case = AddFeedItemsUseCase(AddFeedItemsRepoDBImpl())

    feed = aggregator.get_feeds(channel_address)
    add_feed_item_use_case.add_items(channel_id, feed['entries'])
