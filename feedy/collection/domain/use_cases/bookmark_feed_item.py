import inject

from collection.domain.bookmark_feed_item_repo import BookMarkFeedItemRepo


class BookMarkFeedItemUseCase:
    @inject.autoparams()
    def __init__(self, repo: BookMarkFeedItemRepo):
        self.repo = repo

    def bookmark(self, user_id, feed_item_id):
        self.repo.mark_as_favorite(user_id, feed_item_id)
