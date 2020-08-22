from abc import ABCMeta, abstractmethod


class BookMarkFeedItemRepo(metaclass=ABCMeta):
    @abstractmethod
    def mark_as_favorite(self, user_id, user_feed_item_id):
        pass