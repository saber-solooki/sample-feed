import requests

from general.exceptions import ConnectionException


class RequestExceptionHandler:
    def handle(self, exception):
        if isinstance(exception, requests.RequestException):
            raise ConnectionException()
        else:
            raise exception


class RequestHandler:
    def __init__(self, timeout=15):
        self.timeout = timeout

    def request_url(self, feed_url):
        response = requests.request("GET", feed_url, timeout=self.timeout)
        response.raise_for_status()
        return response.text
