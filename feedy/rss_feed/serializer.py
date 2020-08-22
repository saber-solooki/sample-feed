from rest_framework import serializers

from collection.models import UserFeedItem
from rss_feed.models import Channel, FeedItem


class CreateFeedSerializer(serializers.Serializer):
    feed_address = serializers.URLField()


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('id', 'address', 'title', )


class FeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedItem
        fields = ('id', 'link', 'title', 'summery')


class UserFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFeedItem
        fields = ('id', 'is_bookmarked', 'comment',)