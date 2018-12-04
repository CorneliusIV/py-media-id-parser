import re
from urllib.parse import urlparse
import requests


def get_id(url):

    if url[-1] == '/':
        url = url[:-1]

    matches = re.findall('fbid=[\d]+', url)
    if matches:
        fbid = matches[0].split('=')[1]
        return fbid

    resp = requests.get(url)
    matches = re.findall('"entity_id":"[\d]+"', resp.text)
    entity_id = matches[0].split(':')[1].strip('"')
    url_parts = urlparse(url)
    url_path = url_parts.path.rstrip('/')
    fbid = url_path.split('/')[-1]
    return '{}_{}'.format(entity_id, fbid)
