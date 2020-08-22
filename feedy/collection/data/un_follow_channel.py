from collection.domain.un_follow_channel import UnFollowChannelRepo
from collection.models import UserChannel


class UnFollowChannelRepoDBImpl(UnFollowChannelRepo):
    def delete_user_channel(self, user_id, channel_id):
        UserChannel.objects.filter(user_id=user_id, channel_id=channel_id).delete()
