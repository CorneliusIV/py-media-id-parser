import re
from urllib.parse import urlparse
from .facebook import get_id


def parse_youtube(url):
    o = urlparse(url)
    return o.query.split('=')[1]


def parse_twitter(url):
    url = url.rstrip('/')
    return url.split('/')[-1]


def parse_facebook(url):
    return get_id(url)


def parse_spotify(url):
    o = urlparse(url)
    return o.path.split('/track/')[1]


def parse_instagram(url):
    url = url.rstrip('/')
    return url.split('/')[-1]


def parse_vimeo(url):
    url = url.rstrip('/')
    return url.split('/')[-1]
