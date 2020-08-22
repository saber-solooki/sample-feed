from collection.data.get_feed_items import GetUserFeedItemsRepoDBImpl
from collection.domain.get_feed_items import GetUserFeedItemsRepo
from collection.domain.use_cases.get_feed_items import GetUserFeedItemsUseCase


def provide_use_case():
    return GetUserFeedItemsUseCase()


def provide_repo():
    return GetUserFeedItemsRepoDBImpl()


def get_user_feed_items_binder(binder):
    binder.bind_to_provider(GetUserFeedItemsUseCase, provide_use_case)
    binder.bind_to_provider(GetUserFeedItemsRepo, provide_repo)
