from core_architecture.entity import PagedDataEntity
from core_architecture.pagination import PaginatorQueryWrapper
from rss_feed.domain.channe_list_repo import ChannelListRepo
from rss_feed.domain.entity.channel_list_entity import ChannelEntity
from rss_feed.models import Channel


class ChannelListRepoDBImpl(ChannelListRepo):
    def list_channel(self, request_data) -> PagedDataEntity[ChannelEntity]:
        filters = {}
        if request_data is not None:
            if request_data.get('address', None) is not None:
                filters.update({'address__contains': request_data.get('address')})
            if request_data.get('title', None) is not None:
                filters.update({'title__contains': request_data.get('title')})

        query = Channel.objects.filter(**filters)
        paginator_wrapper = PaginatorQueryWrapper(ChannelEntity)
        return paginator_wrapper.get_paginated_data(query, request_data.get("page", 1))
