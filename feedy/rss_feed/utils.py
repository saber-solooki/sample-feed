from general.exceptions import BusinessException


class FeedAggregator:
    def __init__(self, request_handler, feed_parser, exception_handler=None):
        self.exception_handler = exception_handler
        self.request_handler = request_handler
        self.feed_parser = feed_parser

    def get_feeds(self, feed_url):
        try:
            feed_content = self.request_feed_content(feed_url)
            feed = self.parse_feed_content(feed_content)
        except Exception as e:
            if self.exception_handler is not None:
                self.exception_handler.handle(e)
            raise e
        else:
            return feed

    def request_feed_content(self, feed_url):
        feed_content = self.request_handler.request_url(feed_url)
        return feed_content

    def parse_feed_content(self, feed_content):
        feed = self.feed_parser.parse(feed_content)
        if self._is_feed_valid(feed) is False:
            raise BusinessException(BusinessException.FEED_IS_INVALID)
        else:
            return feed

    def _is_feed_valid(self, feed_info):
        return feed_info.bozo == 0
