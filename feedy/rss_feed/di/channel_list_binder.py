from rss_feed.data.channe_list_repo import ChannelListRepoDBImpl
from rss_feed.domain.channe_list_repo import ChannelListRepo
from rss_feed.domain.use_cases.channel_list import ChannelListUseCase


def provide_use_case():
    return ChannelListUseCase()


def provide_repo():
    return ChannelListRepoDBImpl()


def channel_list_binder(binder):
    binder.bind_to_provider(ChannelListUseCase, provide_use_case)
    binder.bind_to_provider(ChannelListRepo, provide_repo)
