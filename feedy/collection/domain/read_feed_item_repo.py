from abc import ABCMeta, abstractmethod


class ReadFeedItemRepo(metaclass=ABCMeta):
    @abstractmethod
    def create_user_feed_item(self, user_id, feed_item_id):
        pass
