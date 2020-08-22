import inject

from collection.domain.get_feed_item_detail_repo import GetFeedItemDetailRepo


class GetFeedItemDetailUseCase:
    @inject.autoparams()
    def __init__(self, repo: GetFeedItemDetailRepo):
        self.repo = repo

    def get_detail(self, user_id, feed_item_id):
        return self.repo.get_feed_item_detail(user_id, feed_item_id)
