from collection.data.get_feed_item_detail_repo import GetFeedItemDetailRepoDBImpl
from collection.domain.get_feed_item_detail_repo import GetFeedItemDetailRepo
from collection.domain.use_cases.get_feed_item_detail import GetFeedItemDetailUseCase


def provide_use_case():
    return GetFeedItemDetailUseCase()


def provide_repo():
    return GetFeedItemDetailRepoDBImpl()


def get_feed_item_detail_binder(binder):
    binder.bind_to_provider(GetFeedItemDetailUseCase, provide_use_case)
    binder.bind_to_provider(GetFeedItemDetailRepo, provide_repo)
