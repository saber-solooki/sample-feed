import inject

from collection.domain.follow_channel_repo import FollowChannelRepo
from general.exceptions import BusinessException


class FollowChannelUseCase:
    @inject.autoparams()
    def __init__(self, repo: FollowChannelRepo):
        self.repo = repo

    def follow(self, user_id, channel_id):
        if self.repo.is_follow_already(user_id, channel_id):
            raise BusinessException(BusinessException.CHANNEL_ALREADY_FOLLOWED)

        self.repo.create_relation(user_id, channel_id)
