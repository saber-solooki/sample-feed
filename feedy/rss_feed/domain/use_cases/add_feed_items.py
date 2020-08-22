import inject

from rss_feed.domain.add_feed_items_repo import AddFeedItemsRepo


class AddFeedItemsUseCase:
    @inject.autoparams()
    def __init__(self, repo: AddFeedItemsRepo):
        self.repo = repo

    def add_items(self, channel_id, items):
        last_item = self.repo.get_last_item(channel_id)

        creating_candidate = self.get_candidate_for_add(items, last_item)

        self.repo.create_items(channel_id, creating_candidate)

    def get_candidate_for_add(self, items, last_item):
        if last_item is None:
            creating_candidate = items
        else:
            creating_candidate = []
            for item in items:
                if item['published_parsed'] > last_item.published_datetime:
                    creating_candidate.append(item)
                else:
                    break

        return creating_candidate
