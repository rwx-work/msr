import os
import requests

import arguments
import catalog
import hypertext
import msys


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
            subsystems = msys.get_subsystems(architecture, self.subsystems)
            location = os.path.join(self.location,
                                    msys.DISTRIBUTION, architecture)
            a[architecture] = hypertext.HyperText(location).archive
            #
            c[architecture] = {}
            for subsystem in subsystems:
                location = self.location
                if subsystem == msys.SUBSYSTEM:
                    location = os.path.join(location, subsystem, architecture)
                else:
                    location = os.path.join(location, msys.CRT, subsystem)
                location = os.path.join(location,
                                        f'{subsystem}{msys.CATALOG}')
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
