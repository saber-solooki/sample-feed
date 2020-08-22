import inject

from core_architecture.entity import PagedDataEntity
from rss_feed.domain.channe_list_repo import ChannelListRepo
from rss_feed.domain.entity.channel_list_entity import ChannelEntity


class ChannelListUseCase:
    @inject.autoparams()
    def __init__(self, repo: ChannelListRepo):
        self.repo = repo

    def get_list(self, request_data) -> PagedDataEntity[ChannelEntity]:
        return self.repo.list_channel(request_data)
