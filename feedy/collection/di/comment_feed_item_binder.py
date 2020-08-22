from collection.data.comment_on_feed_item_repo import CommentOnFeedItemRepoDBImpl
from collection.domain.comment_on_feed_item_repo import CommentOnFeedItemRepo
from collection.domain.use_cases.comment_on_feed_item import CommentOnFeedItemUseCase


def provide_use_case():
    return CommentOnFeedItemUseCase()


def provide_repo():
    return CommentOnFeedItemRepoDBImpl()


def comment_feed_item_binder(binder):
    binder.bind_to_provider(CommentOnFeedItemUseCase, provide_use_case)
    binder.bind_to_provider(CommentOnFeedItemRepo, provide_repo)
