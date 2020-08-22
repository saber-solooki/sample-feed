import inject

from collection.domain.user_channels_list_repo import UserChannelsListRepo
from core_architecture.entity import PagedDataEntity
from rss_feed.domain.entity.channel_list_entity import ChannelEntity


class UserChannelsListUseCase:
    @inject.autoparams()
    def __init__(self, repo: UserChannelsListRepo):
        self.repo = repo

    def get_list(self, user_id, page) -> PagedDataEntity[ChannelEntity]:
        return self.repo.get_channels(user_id, page)
