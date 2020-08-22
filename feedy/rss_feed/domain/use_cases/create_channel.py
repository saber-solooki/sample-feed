import inject

from general.exceptions import BusinessException
from rss_feed.domain.create_feed_repo import CreateChannelRepo
from rss_feed.utils import FeedAggregator


class CreateChannelUseCase:
    @inject.autoparams()
    def __init__(self, repo: CreateChannelRepo, aggregator: FeedAggregator):
        self.repo = repo
        self.aggregator = aggregator

    def create_channel(self, rss_feed_address):
        if self.repo.is_channel_exist(rss_feed_address):
            raise BusinessException(BusinessException.FEED_ALREADY_EXIST)

        feed_info = self.aggregator.get_feeds(rss_feed_address)

        self.repo.create_channel(rss_feed_address, feed_info)

    @staticmethod
    def _is_feed_valid(feed_info):
        return feed_info.bozo == 0
