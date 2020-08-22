from collection.domain.user_channels_list_repo import UserChannelsListRepo
from core_architecture.pagination import PaginatorQueryWrapper
from rss_feed.domain.entity.channel_list_entity import ChannelEntity
from rss_feed.models import Channel


class UserChannelsListRepoDBImpl(UserChannelsListRepo):
    def get_channels(self, user_id, page):
        query = Channel.objects.filter(userchannel__user__id=user_id)
        paginator_wrapper = PaginatorQueryWrapper(ChannelEntity)
        return paginator_wrapper.get_paginated_data(query, page)
