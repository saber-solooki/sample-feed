from django.db import models


class Channel(models.Model):
    address = models.URLField()
    title = models.CharField(max_length=100)
    last_update = models.DateTimeField(null=True, blank=True)


class FeedItem(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    link = models.URLField()
    title = models.TextField()
    summery = models.TextField()
    published_datetime = models.DateTimeField()
