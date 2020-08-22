class CommentOnFeedItemRequestEntity:
    def __init__(self, user_id, feed_item_id, comment):
        self.user_id = user_id
        self.feed_item_id = feed_item_id
        self.comment = comment
