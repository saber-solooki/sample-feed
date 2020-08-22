import inject

from collection.domain.entities.feed_item_entity import FeedItemEntity
from collection.domain.get_feed_items import GetUserFeedItemsRepo
from core_architecture.entity import PagedDataEntity


class GetUserFeedItemsUseCase:
    @inject.autoparams()
    def __init__(self, repo: GetUserFeedItemsRepo):
        self.repo = repo

    def get_feed_items(self, user_id, page) -> PagedDataEntity[FeedItemEntity]:
        return self.repo.get_feed_items(user_id, page)
