from abc import ABCMeta, abstractmethod

from core_architecture.entity import PagedDataEntity
from rss_feed.domain.entity.channel_list_entity import ChannelEntity


class UserChannelsListRepo(metaclass=ABCMeta):
    @abstractmethod
    def get_channels(self, user_id, page) -> PagedDataEntity[ChannelEntity]:
        pass
