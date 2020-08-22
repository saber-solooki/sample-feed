from rss_feed.data.create_feed_repo import CreateChannelRepoDBImpl
from rss_feed.domain.create_feed_repo import CreateChannelRepo
from rss_feed.domain.use_cases.create_channel import CreateChannelUseCase


def provide_use_case():
    return CreateChannelUseCase()


def provide_repo():
    return CreateChannelRepoDBImpl()


def create_channel_binder(binder):
    binder.bind_to_provider(CreateChannelUseCase, provide_use_case)
    binder.bind_to_provider(CreateChannelRepo, provide_repo)