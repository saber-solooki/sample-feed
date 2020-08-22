from collection.domain.bookmark_feed_item_repo import BookMarkFeedItemRepo
from collection.models import UserFeedItem


class BookMarkFeedItemRepoDBImpl(BookMarkFeedItemRepo):
    def mark_as_favorite(self, user_id, feed_item_id):
        UserFeedItem.objects.filter(user_id=user_id, feed_item_id=feed_item_id).update(is_bookmarked=True)
