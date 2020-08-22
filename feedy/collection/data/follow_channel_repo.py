from collection.domain.follow_channel_repo import FollowChannelRepo
from collection.models import UserChannel


class FollowChannelRepoDBImpl(FollowChannelRepo):
    def is_follow_already(self, user_id, channel_id):
        return UserChannel.objects.filter(user_id=user_id, channel_id=channel_id).exists()

    def create_relation(self, user_id, channel_id):
        UserChannel.objects.create(user_id=user_id, channel_id=channel_id)
