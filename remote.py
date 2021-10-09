import os
import requests

import arguments
import hypertext


ARCHIVE = '.tar.xz'
ARCHITECTURES = ['x86_64', 'i686']
CHARSET = 'u8'
DISTRIBUTION = 'distrib'
SIGNATURE = '.sig'
SUBSYSTEMS = ['msys', 'mingw']


class Remote:
    def __init__(self, args):
        self.location = args[arguments.REMOTE]
        self.architectures = args[arguments.ARCHITECTURES]
        self.load()

    def load(self):
        d = {}
        for architecture in self.architectures:
            url = os.path.join(self.location, DISTRIBUTION, architecture)
            html = requests.get(url).content.decode(CHARSET)
            links = sorted(hypertext.get_links(html))
            archives = [link for link in links
                        if link.endswith(ARCHIVE)]
            signatures = [link for link in links
                          if link.endswith(SIGNATURE)]
            archive = archives[-1]
            d[architecture] = archive
        self.archives = d

    def __str__(self):
        lines = [f'Location: {self.location}',
                 'Archives:']
        for architecture, archive in reversed(sorted(self.archives.items())):
            lines.append(f'{architecture} → {archive}')
        return os.linesep.join(lines)
