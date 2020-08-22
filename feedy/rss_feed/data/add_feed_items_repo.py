from rss_feed.domain.add_feed_items_repo import AddFeedItemsRepo
from rss_feed.models import FeedItem


class AddFeedItemsRepoDBImpl(AddFeedItemsRepo):
    def get_last_item(self, channel_id):
        return FeedItem.objects.only('published_datetime').order_by('published_datetime').last()

    def create_items(self, channel_id, items):
        feed_item_objects = []
        for item in items:
            feed_item_objects.append(
                FeedItem(channel_id=channel_id, link=item['link'], title=item['title'], summery=item['summary'],
                         published_datetime=item['published_parsed'])
            )

        FeedItem.objects.bulk_create(feed_item_objects)
