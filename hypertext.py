import html.parser
import requests

CHARSET = 'u8'


class Parser(html.parser.HTMLParser):
    def __init__(self):
        self.links = []
        super().__init__()

    def handle_starttag(self, tag, attributes):
        if tag == 'a':
            self.links.extend(
                [v for k, v in attributes if k == 'href'])


class HyperText:
    def __init__(self, location):
        self.location = location
        self.load()

    def load(self):
        hypertext = requests.get(self.location).content.decode(CHARSET)
        parser = Parser()
        parser.feed(hypertext)
        self.links = parser.links
