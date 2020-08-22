from collection.domain.read_feed_item_repo import ReadFeedItemRepo
from collection.models import UserFeedItem


class ReadFeedItemRepoDBImpl(ReadFeedItemRepo):
    def create_user_feed_item(self, user_id, feed_item_id):
        if not UserFeedItem.objects.filter(user_id=user_id, feed_item_id=feed_item_id).exists():
            UserFeedItem.objects.create(user_id=user_id, feed_item_id=feed_item_id)
