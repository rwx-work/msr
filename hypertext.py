import html.parser


class Parser(html.parser.HTMLParser):
    def __init__(self):
        self.links = []
        super().__init__()

    def handle_starttag(self, tag, attributes):
        if tag == 'a':
            self.links.extend(
                [v for k, v in attributes if k == 'href'])


def get_links(hypertext):
    parser = Parser()
    parser.feed(hypertext)
    return parser.links
