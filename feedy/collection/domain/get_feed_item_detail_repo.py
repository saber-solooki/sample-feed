from abc import ABCMeta, abstractmethod


class GetFeedItemDetailRepo(metaclass=ABCMeta):
    @abstractmethod
    def get_feed_item_detail(self, user_id, feed_item_id):
        pass
