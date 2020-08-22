from abc import ABCMeta, abstractmethod


class AddFeedItemsRepo(metaclass=ABCMeta):
    @abstractmethod
    def get_last_item(self, channel_id):
        pass

    @abstractmethod
    def create_items(self, channel_id, items):
        pass
