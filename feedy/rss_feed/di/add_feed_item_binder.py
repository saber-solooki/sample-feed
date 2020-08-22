from rss_feed.data.add_feed_items_repo import AddFeedItemsRepoDBImpl
from rss_feed.domain.add_feed_items_repo import AddFeedItemsRepo
from rss_feed.domain.use_cases.add_feed_items import AddFeedItemsUseCase


def provide_use_case():
    return AddFeedItemsUseCase()


def provide_repo():
    return AddFeedItemsRepoDBImpl()


def add_feed_item_binder(binder):
    binder.bind_to_provider(AddFeedItemsUseCase, provide_use_case)
    binder.bind_to_provider(AddFeedItemsRepo, provide_repo)
