from unittest import mock

import feedparser
import inject
import requests
from celery.exceptions import Retry
from django.test import TestCase

from feedy import celerysetting
from general.exceptions import BusinessException
from general.request_handler import RequestHandler
from rss_feed.domain.create_feed_repo import CreateChannelRepo
from rss_feed.domain.use_cases.create_channel import CreateChannelUseCase
from rss_feed.serializer import CreateFeedSerializer
from rss_feed.tasks import fetch_feed_for_channel
from rss_feed.utils import FeedAggregator


class CreateChannelRepoTest(CreateChannelRepo):

    def is_channel_exist(self, rss_feed_address):
        return True

    def create_channel(self, rss_feed_address, feed_info):
        pass


class CreateChannelBusinessTest(TestCase):
    def setUp(self):
        inject.clear_and_configure(
            lambda binder: binder
                .bind(CreateChannelRepo, CreateChannelRepoTest()) \
                .bind(FeedAggregator, FeedAggregator(RequestHandler(), feedparser))
            )

    def test_input_serializer_for_invalid_url(self):
        data = {'feed_address': "url"}
        serializer = CreateFeedSerializer(data=data)
        self.assertFalse(serializer.is_valid())

        data = {'feed_address': 1}
        serializer = CreateFeedSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_input_serializer_for_valid_url(self):
        data = {'feed_address': "https://google.com"}
        serializer = CreateFeedSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_channel_exist(self):
        use_case = CreateChannelUseCase()

        self.assertRaises(BusinessException, use_case.create_channel, rss_feed_address='url')

    def test_exception_code_for_channel_exist(self):
        use_case = CreateChannelUseCase()
        try:
            use_case.create_channel('url')
        except BusinessException as e:
            self.assertEqual(BusinessException.FEED_ALREADY_EXIST, e.code)


class FeedAggregatorTest(TestCase):
    def setUp(self):
        self.feed_aggregator = FeedAggregator(RequestHandler(), feedparser)

    class InvalidFeedObject:
        def __init__(self):
            self.bozo = 1

    @mock.patch('feedparser.parse', return_value=InvalidFeedObject())
    @mock.patch('general.request_handler.RequestHandler.request_url', return_value="")
    def test_channel_is_not_feed_rss(self, mock_request_handler, mock_url):
        self.assertRaises(BusinessException, self.feed_aggregator.get_feeds, feed_url='url')

    @mock.patch('feedparser.parse', return_value=InvalidFeedObject())
    @mock.patch('general.request_handler.RequestHandler.request_url', return_value="")
    def test_exception_code_for_channel_is_not_feed_rss_(self, mock_request_handler, mock_url):
        try:
            self.feed_aggregator.get_feeds("url")
        except BusinessException as e:
            self.assertEqual(BusinessException.FEED_IS_INVALID, e.code)


class FeedAggregatorTaskTest(TestCase):

    @mock.patch('rss_feed.utils.FeedAggregator.get_feeds', return_value={'entries': "response"})
    @mock.patch('rss_feed.domain.use_cases.add_feed_items.AddFeedItemsUseCase.add_items')
    def test_success_fetch_for_feed(self, add_items_use_case, get_feeds_aggregator):
        fetch_feed_for_channel(1, 'url')
        get_feeds_aggregator.assert_called_with("url")
        add_items_use_case.assert_called_with(1, 'response')

    @mock.patch('rss_feed.utils.FeedAggregator.get_feeds', return_value={'entries': "response"})
    @mock.patch('rss_feed.domain.use_cases.add_feed_items.AddFeedItemsUseCase.add_items')
    @mock.patch('rss_feed.tasks.fetch_feed_for_channel.retry')
    def test_failed_fetch_for_feed(self, fetch_feed_retry, add_items_use_case, get_feeds_aggregator):
        fetch_feed_retry.side_effect = Retry()
        get_feeds_aggregator.side_effect = exception = requests.RequestException()

        with self.assertRaises(Retry):
            fetch_feed_for_channel(1, 'url')

        fetch_feed_retry.assert_called_with(exc=exception, max_retries=celerysetting.MAX_RETRIES_FOR_BASIC_DATA)
