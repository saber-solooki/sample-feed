from collection.data.follow_channel_repo import FollowChannelRepoDBImpl
from collection.domain.follow_channel_repo import FollowChannelRepo
from collection.domain.use_cases.follow_channel import FollowChannelUseCase


def provide_use_case():
    return FollowChannelUseCase()


def provide_repo():
    return FollowChannelRepoDBImpl()


def follow_channel_binder(binder):
    binder.bind_to_provider(FollowChannelUseCase, provide_use_case)
    binder.bind_to_provider(FollowChannelRepo, provide_repo)
