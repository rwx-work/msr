import os
import requests

import arguments
import hypertext


CHARSET = 'u8'
DISTRIBUTION = 'distrib'


class Remote:
    def __init__(self, args):
        self.location = args[arguments.REMOTE]

    def fetch_latest_distribution(self, architecture):
        url = os.path.join(self.location, DISTRIBUTION, architecture)
        html = requests.get(url).content.decode(CHARSET)
        links = hypertext.get_links(html)
        print(links)

    def __str__(self):
        return f'''\
Location: {self.location}
'''
