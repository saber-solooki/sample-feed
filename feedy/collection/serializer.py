from rest_framework import serializers


class FollowChannelSerializer(serializers.Serializer):
    channel_id = serializers.IntegerField()


class ReadFeedItemSerializer(serializers.Serializer):
    feed_item_id = serializers.IntegerField()


class CommentOnFeedItemSerializer(serializers.Serializer):
    comment = serializers.CharField(allow_blank=True)
