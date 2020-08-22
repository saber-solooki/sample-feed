import datetime
from time import mktime


def convert_feed_time_to_datetime(feed_time):
    return datetime.datetime.fromtimestamp(mktime(feed_time))
    # return datetime.datetime.strptime(feed_time, '%a, %d %b %Y %H:%M:%S %z')
