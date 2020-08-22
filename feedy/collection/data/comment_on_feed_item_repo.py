from collection.domain.comment_on_feed_item_repo import CommentOnFeedItemRepo
from collection.domain.entities.comment_feed_item_entity import CommentOnFeedItemRequestEntity
from collection.models import UserFeedItem


class CommentOnFeedItemRepoDBImpl(CommentOnFeedItemRepo):
    def update_feed_whit_comment(self, request: CommentOnFeedItemRequestEntity):
        UserFeedItem.objects\
            .filter(user_id=request.user_id, feed_item_id=request.feed_item_id)\
            .update(comment=request.comment)
