import inject

from collection.domain.comment_on_feed_item_repo import CommentOnFeedItemRepo
from collection.domain.entities.comment_feed_item_entity import CommentOnFeedItemRequestEntity


class CommentOnFeedItemUseCase:
    @inject.autoparams()
    def __init__(self, repo: CommentOnFeedItemRepo):
        self.repo = repo

    def set_comment(self, request: CommentOnFeedItemRequestEntity):
        self.repo.update_feed_whit_comment(request)
