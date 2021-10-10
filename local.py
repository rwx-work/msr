import datetime
import os

import architecture
import arguments
import distribution
import msys
import repository


class Local(repository.Repository):
    def __init__(self):
        super().__init__(arguments.directory)
        self.temporary = arguments.temporary
        self.load()

    def load(self):
        distro = os.path.join(
            self.location, distribution.DISTRIBUTION)
        d = {}
        _, architectures, _ = next(os.walk(distro))
        for arch in [a for a in architectures
                     if a in architecture.ARCHITECTURES.keys()]:
            directory = os.path.join(distro, arch)
            _, _, files = next(os.walk(directory))
            archives = sorted([file for file in files
                               if file.endswith(msys.ARCHIVE)])
            archive = archives[-1]
            d[arch] = archive
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
        for arch, archive in reversed(sorted(self.archives.items())):
            lines.append(f'{arch} → {archive}')
        return os.linesep.join(lines)
