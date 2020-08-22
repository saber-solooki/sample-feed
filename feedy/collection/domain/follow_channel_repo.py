from abc import ABCMeta, abstractmethod


class FollowChannelRepo(metaclass=ABCMeta):
    @abstractmethod
    def is_follow_already(self, user_id, channel_id):
        pass

    @abstractmethod
    def create_relation(self, user_id, channel_id):
        pass
