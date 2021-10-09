import os
import requests

import arguments
import hypertext


ARCHIVE = '.tar.xz'
ARCHITECTURES = ['x86_64', 'i686']
CHARSET = 'u8'
DISTRIBUTION = 'distrib'
FILES = '.files'
MINGW = 'mingw'
SIGNATURE = '.sig'
SUBSYSTEMS = ['msys', 'mingw64']


class Remote:
    def __init__(self, args):
        self.location = args[arguments.REMOTE]
        self.architectures = args[arguments.ARCHITECTURES]
        self.subsystems = args[arguments.SUBSYSTEMS]
        self.load()

    def load(self):
        a = {}
        c = {}
        for architecture in self.architectures:
            url = os.path.join(self.location, DISTRIBUTION, architecture)
            html = requests.get(url).content.decode(CHARSET)
            links = sorted(hypertext.get_links(html))
            archives = [link for link in links
                        if link.endswith(ARCHIVE)]
            archive = archives[-1]
            a[architecture] = archive
            #
            for subsystem in self.subsystems:
                location = [self.location]
                if subsystem != SUBSYSTEMS[0]:
                    location.append(MINGW)
                location = os.path.join(*location, subsystem, architecture,
                                        f'{subsystem}{FILES}')
                binary = requests.get(url).content
                c[architecture] = binary
        self.archives = a
        self.catalogs = c

    def __str__(self):
        lines = [f'Location: {self.location}',
                 'Archives:']
        for architecture, archive in reversed(sorted(self.archives.items())):
            lines.append(f'{architecture} → {archive}')
        lines.append(f'Subsystems: {self.subsystems}')
        return os.linesep.join(lines)
