import os
import requests

import arguments
import catalog
import hypertext
import msys
import repository


class Remote(repository.Repository):
    def __init__(self, args):
        super().__init__(args[arguments.REMOTE])
        self.load()

    def load(self):
        archives = {}
        c = {}
        for architecture in self.architectures:
            subsystems = architecture.subsystems.keys()
            location = os.path.join(self.location,
                                    msys.get_distribution(architecture))
            archives[architecture] = hypertext.HyperText(location).archive
            #
            c[architecture] = {}
            for subsystem in subsystems:
                location = os.path.join(self.location,
                                        msys.get_subsystem(architecture,
                                                           subsystem),
                                        f'{subsystem}{msys.CATALOG}')
                binary = requests.get(location).content
                c[architecture][subsystem] = catalog.Catalog(binary)
        self.archives = archives
        self.catalogs = c

    def __str__(self):
        lines = [
            super().__str__(),
            'Archives:',
        ]
        for architecture, archive in reversed(sorted(self.archives.items())):
            lines.append(f'{architecture} → {archive}')
        lines.append('Subsystems:')
        for arch, ss in reversed(sorted(self.catalogs.items())):
            lines.append(f'{arch} → {list(ss.keys())}')
        return os.linesep.join(lines)
