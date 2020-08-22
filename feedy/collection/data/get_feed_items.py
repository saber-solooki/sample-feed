from django.db.models import Q

from collection.domain.entities.feed_item_entity import FeedItemEntity
from collection.domain.get_feed_items import GetUserFeedItemsRepo
from core_architecture.entity import PagedDataEntity
from core_architecture.pagination import PaginatorQueryWrapper
from rss_feed.models import FeedItem


class GetUserFeedItemsRepoDBImpl(GetUserFeedItemsRepo):
    def get_feed_items(self, user_id, page) -> PagedDataEntity[FeedItemEntity]:
        query = FeedItem.objects.filter(~Q(feed_item_ufi__user__id=user_id))
        paginator_wrapper = PaginatorQueryWrapper(FeedItemEntity)
        return paginator_wrapper.get_paginated_data(query, page)
