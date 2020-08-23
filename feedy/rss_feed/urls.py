from django.urls import path

from rss_feed.views import ChannelView, ChannelListView

app_name = 'feed'

urlpatterns = [
    path('channels/', ChannelListView.as_view(), name='channels'),
    path('channels/channel/', ChannelView.as_view(), name='channel'),
]
