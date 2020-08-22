from django.urls import path

from collection.views import UserChannelView, UserChannelsList, UserUnreadFeedListView, FeedItemView, \
    BookMarkFeedItemView, CommentOnFeedItemView

app_name = 'collections'

urlpatterns = [
    path('user/channel/', UserChannelView.as_view()),
    path('user/channel/<int:channel_id>/', UserChannelView.as_view()),
    path('user/', UserChannelsList.as_view()),
    path('user/feeds/', UserUnreadFeedListView.as_view()),
    path('user/feeds/feed/', FeedItemView.as_view()),
    path('user/feeds/feed/<int:feed_item_id>/', FeedItemView.as_view()),
    path('user/feeds/feed/<int:feed_item_id>/bookmark/', BookMarkFeedItemView.as_view(), name='bookmark_feed'),
    path('user/feeds/feed/<int:feed_item_id>/comment/', CommentOnFeedItemView.as_view()),
]