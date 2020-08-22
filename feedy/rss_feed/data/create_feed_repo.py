from rss_feed.domain.create_feed_repo import CreateChannelRepo
from rss_feed.models import Channel


class CreateChannelRepoDBImpl(CreateChannelRepo):
    def is_channel_exist(self, rss_feed_address):
        return Channel.objects.filter(address=rss_feed_address).exists()

    def create_channel(self, rss_feed_address, feed_info):
        Channel.objects.create(address=rss_feed_address, title=feed_info['feed']['title'])
