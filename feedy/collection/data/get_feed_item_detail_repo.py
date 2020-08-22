from collection.domain.entities.user_feed_entity import UserFeedEntity
from collection.domain.get_feed_item_detail_repo import GetFeedItemDetailRepo
from collection.models import UserFeedItem


class GetFeedItemDetailRepoDBImpl(GetFeedItemDetailRepo):
    def get_feed_item_detail(self, user_id, feed_item_id):
        query = UserFeedItem.objects.get(user_id=user_id, feed_item_id=feed_item_id)
        return UserFeedEntity(query.id, query.is_bookmarked, query.comment)

