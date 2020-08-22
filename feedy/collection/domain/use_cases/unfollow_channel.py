import inject

from collection.domain.un_follow_channel import UnFollowChannelRepo


class UnFollowChannelUseCase:
    @inject.autoparams()
    def __init__(self, repo: UnFollowChannelRepo):
        self.repo = repo

    def un_follow(self, user_id, channel_id):
        self.repo.delete_user_channel(user_id, channel_id)
