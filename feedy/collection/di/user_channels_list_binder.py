from collection.data.user_channels_list_repo import UserChannelsListRepoDBImpl
from collection.domain.use_cases.user_channels_list import UserChannelsListUseCase
from collection.domain.user_channels_list_repo import UserChannelsListRepo


def provide_use_case():
    return UserChannelsListUseCase()


def provide_repo():
    return UserChannelsListRepoDBImpl()


def user_channels_list_binder(binder):
    binder.bind_to_provider(UserChannelsListUseCase, provide_use_case)
    binder.bind_to_provider(UserChannelsListRepo, provide_repo)
