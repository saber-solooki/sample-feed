from collection.data.bookmark_feed_item_repo import BookMarkFeedItemRepoDBImpl
from collection.domain.bookmark_feed_item_repo import BookMarkFeedItemRepo
from collection.domain.use_cases.bookmark_feed_item import BookMarkFeedItemUseCase


def provide_use_case():
    return BookMarkFeedItemUseCase()


def provide_repo():
    return BookMarkFeedItemRepoDBImpl()


def bookmark_binder(binder):
    binder.bind_to_provider(BookMarkFeedItemUseCase, provide_use_case)
    binder.bind_to_provider(BookMarkFeedItemRepo, provide_repo)
