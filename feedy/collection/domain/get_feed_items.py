from abc import ABCMeta, abstractmethod

from collection.domain.entities.feed_item_entity import FeedItemEntity
from core_architecture.entity import PagedDataEntity


class GetUserFeedItemsRepo(metaclass=ABCMeta):
    @abstractmethod
    def get_feed_items(self, user_id, page) -> PagedDataEntity[FeedItemEntity]:
        pass
