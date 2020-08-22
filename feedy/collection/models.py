from django.contrib.auth.models import User
from django.db import models

from rss_feed.models import Channel, FeedItem


class UserChannel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'channel']


class UserFeedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feed_item = models.ForeignKey(FeedItem, on_delete=models.CASCADE, related_name='feed_item_ufi')
    is_bookmarked = models.BooleanField(default=False)
    comment = models.TextField(blank=True)

    class Meta:
        unique_together = ['user', 'feed_item']
