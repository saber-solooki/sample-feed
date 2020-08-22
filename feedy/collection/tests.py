import datetime

import inject
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory, force_authenticate

from collection.di.book_mark_binder import bookmark_binder
from collection.models import UserFeedItem
from collection.views import BookMarkFeedItemView
from rss_feed.models import FeedItem, Channel


class IntegrationTestForBookMarkFeedItem(TestCase):
    factory = APIRequestFactory()

    def setUp(self):
        inject.clear_and_configure(
            lambda binder: binder
                .install(bookmark_binder)
            )

    def test_bookmark_feed(self):
        user = User.objects.create_user('saber', "123")
        channel = Channel.objects.create(address="https://www.zoomit.ir/feed/", title="zoomit")
        feed_item = FeedItem.objects.create(channel_id=channel.id, link='https://www.zoomit.ir/khabar/', title="test",
                                            summery="summery", published_datetime=datetime.datetime.now())
        UserFeedItem.objects.create(user_id=user.id, feed_item_id=feed_item.id)

        view = BookMarkFeedItemView.as_view()

        request = self.factory.put(reverse('collections:bookmark_feed',  kwargs={'feed_item_id': feed_item.id}))
        force_authenticate(request, user=user)
        response = view(request, feed_item_id=feed_item.id)

        user_feed_obj = UserFeedItem.objects.first()

        self.assertEqual(response.status_code, 202)
        self.assertTrue(user_feed_obj.is_bookmarked)

