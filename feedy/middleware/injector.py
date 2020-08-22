import inject

from collection.di.book_mark_binder import bookmark_binder
from collection.di.comment_feed_item_binder import comment_feed_item_binder
from collection.di.follow_channel_binder import follow_channel_binder
from collection.di.get_feed_item_detail_binder import get_feed_item_detail_binder
from collection.di.get_user_feed_item import get_user_feed_items_binder
from collection.di.read_feed_item_binder import read_feed_item_binder
from collection.di.un_follow_channel_binder import un_follow_channel_binder
from collection.di.user_channels_list_binder import user_channels_list_binder
from general.validator import PasswordValidator, DjangoPasswordValidator
from rss_feed.di.channel_list_binder import channel_list_binder
from rss_feed.di.create_channel_binder import create_channel_binder
from user.di.create_user_binder import create_user_binder


class InjectorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        inject.configure(self.di_configuration)

    def __call__(self, request):
        response = self.get_response(request)

        return response

    def di_configuration(self, binder):
        binder.bind(PasswordValidator, DjangoPasswordValidator())

        binder.install(create_user_binder)
        binder.install(create_channel_binder)
        binder.install(channel_list_binder)
        binder.install(follow_channel_binder)
        binder.install(un_follow_channel_binder)
        binder.install(user_channels_list_binder)
        binder.install(get_user_feed_items_binder)
        binder.install(read_feed_item_binder)
        binder.install(bookmark_binder)
        binder.install(comment_feed_item_binder)
        binder.install(get_feed_item_detail_binder)
