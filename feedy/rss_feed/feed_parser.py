from time import struct_time

import pytz

from general import utils


def parse_decorator(f):
    def parse(*args, **kwargs):
        feed_content = f(*args, **kwargs)

        for item in feed_content['entries']:
            if isinstance(item['published_parsed'], struct_time):
                published_datetime = utils.convert_feed_time_to_datetime(item['published_parsed'])
                item['published_parsed'] = published_datetime.replace(tzinfo=pytz.UTC)

        feed_content['entries'] = sorted(feed_content['entries'], key=lambda k: k['published_parsed'], reverse=True)

        return feed_content

    return parse
