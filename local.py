import arguments
import datetime
import os

import distribution
import msys
import repository


class Local(repository.Repository):
    def __init__(self, args):
        super().__init__(args[arguments.DIRECTORY])
        self.temporary = args[arguments.TEMPORARY]
        self.load()

    def load(self):
        distro = os.path.join(
            self.location, distribution.DISTRIBUTION)
        d = {}
        _, architectures, _ = next(os.walk(distro))
        for architecture in [a for a in architectures
                             if a in msys.ARCHITECTURES]:
            directory = os.path.join(distro, architecture)
            _, _, files = next(os.walk(directory))
            archives = sorted([file for file in files
                               if file.endswith(msys.ARCHIVE)])
            archive = archives[-1]
            d[architecture] = archive
        self.archives = d

    def get_temporary(self):
        return os.path.join(self.temporary,
                            datetime.datetime.now()
                            .strftime('%Y%m%d%H%M%S'))

    def __str__(self):
        lines = [
            super().__str__(),
            'Archives:',
        ]
        for architecture, archive in reversed(sorted(self.archives.items())):
            lines.append(f'{architecture} → {archive}')
        return os.linesep.join(lines)
