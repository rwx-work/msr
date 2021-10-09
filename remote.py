import os
import requests

import arguments
import catalog
import hypertext


ARCHIVE = '.tar.xz'
ARCHITECTURES = ['x86_64', 'i686']
ARCHITECTURES_BITS = {
    'x86_64': 64,
    'i686': 32,
}
ARCHITECTURES_SUBSYSTEMS = {
    'x86_64': ['msys', 'clang64', 'mingw64', 'ucrt64'],
    'i686': ['msys', 'clang32', 'mingw32'],
}
CHARSET = 'u8'
DISTRIBUTION = 'distrib'
FILES = '.files'
MINGW = 'mingw'
SIGNATURE = '.sig'
SUBSYSTEMS = ['msys', 'clang', 'mingw', 'ucrt']


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
            location = os.path.join(self.location, DISTRIBUTION, architecture)
            html = requests.get(location).content.decode(CHARSET)
            links = sorted(hypertext.get_links(html))
            archives = [link for link in links
                        if link.endswith(ARCHIVE)]
            archive = archives[-1]
            a[architecture] = archive
            #
            c[architecture] = {}
            for ss in self.subsystems:
                location = self.location
                if ss == SUBSYSTEMS[0]:
                    subsystem = ss
                    location = os.path.join(location, subsystem, architecture)
                else:
                    subsystem = f'{ss}{ARCHITECTURES_BITS[architecture]}'
                    location = os.path.join(location, MINGW, subsystem)
                if subsystem in ARCHITECTURES_SUBSYSTEMS[architecture]:
                    location = os.path.join(location, f'{subsystem}{FILES}')
                    binary = requests.get(location).content
                    c[architecture][subsystem] = catalog.Catalog(binary)
        self.archives = a
        self.catalogs = c

    def __str__(self):
        lines = [f'Location: {self.location}',
                 'Archives:']
        for architecture, archive in reversed(sorted(self.archives.items())):
            lines.append(f'{architecture} → {archive}')
        lines.append('Subsystems:')
        for arch, ss in reversed(sorted(self.catalogs.items())):
            lines.append(f'{arch} → {list(ss.keys())}')
        return os.linesep.join(lines)
