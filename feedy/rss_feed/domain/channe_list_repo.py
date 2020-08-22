from abc import ABCMeta, abstractmethod

from core_architecture.entity import PagedDataEntity
from rss_feed.domain.entity.channel_list_entity import ChannelEntity


class ChannelListRepo(metaclass=ABCMeta):
    @abstractmethod
    def list_channel(self, request_data) -> PagedDataEntity[ChannelEntity]:
        pass
