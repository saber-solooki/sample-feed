from abc import ABCMeta, abstractmethod


class CreateChannelRepo(metaclass=ABCMeta):
    @abstractmethod
    def is_channel_exist(self, rss_feed_address):
        pass

    @abstractmethod
    def create_channel(self, rss_feed_address, feed_info):
        pass
