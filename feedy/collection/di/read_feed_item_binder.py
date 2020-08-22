from collection.data.read_feed_item_repo import ReadFeedItemRepoDBImpl
from collection.domain.read_feed_item_repo import ReadFeedItemRepo
from collection.domain.use_cases.read_feed_item import ReadFeedItemUseCase


def provide_use_case():
    return ReadFeedItemUseCase()


def provide_repo():
    return ReadFeedItemRepoDBImpl()


def read_feed_item_binder(binder):
    binder.bind_to_provider(ReadFeedItemUseCase, provide_use_case)
    binder.bind_to_provider(ReadFeedItemRepo, provide_repo)
