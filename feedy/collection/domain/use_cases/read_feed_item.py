import inject

from collection.domain.read_feed_item_repo import ReadFeedItemRepo


class ReadFeedItemUseCase:
    @inject.autoparams()
    def __init__(self, repo: ReadFeedItemRepo):
        self.repo = repo

    def read_feed(self, user_id, feed_item_id):
        self.repo.create_user_feed_item(user_id, feed_item_id)
