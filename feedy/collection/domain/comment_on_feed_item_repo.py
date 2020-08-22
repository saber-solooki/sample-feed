from abc import ABCMeta, abstractmethod

from collection.domain.entities.comment_feed_item_entity import CommentOnFeedItemRequestEntity


class CommentOnFeedItemRepo(metaclass=ABCMeta):
    @abstractmethod
    def update_feed_whit_comment(self, request: CommentOnFeedItemRequestEntity):
        pass
