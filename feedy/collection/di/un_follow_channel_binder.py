from collection.data.un_follow_channel import UnFollowChannelRepoDBImpl
from collection.domain.un_follow_channel import UnFollowChannelRepo
from collection.domain.use_cases.unfollow_channel import UnFollowChannelUseCase


def provide_use_case():
    return UnFollowChannelUseCase()


def provide_repo():
    return UnFollowChannelRepoDBImpl()


def un_follow_channel_binder(binder):
    binder.bind_to_provider(UnFollowChannelUseCase, provide_use_case)
    binder.bind_to_provider(UnFollowChannelRepo, provide_repo)
