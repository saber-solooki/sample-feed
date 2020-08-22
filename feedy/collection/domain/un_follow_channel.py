from abc import ABCMeta, abstractmethod


class UnFollowChannelRepo(metaclass=ABCMeta):
    @abstractmethod
    def delete_user_channel(self, user_id, channel_id):
        pass
