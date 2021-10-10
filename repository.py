import arguments
import datetime
import os

import msys


class Repository:
    def __init__(self, args):
        self.directory = args[arguments.DIRECTORY]
        self.temporary = args[arguments.TEMPORARY]
        self.load()

    def load(self):
        distribution = os.path.join(
            self.directory, msys.DISTRIBUTION)
        d = {}
        _, architectures, _ = next(os.walk(distribution))
        for architecture in [a for a in architectures
                             if a in msys.ARCHITECTURES]:
            directory = os.path.join(distribution, architecture)
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
            f'Directory: {self.directory}',
            f'         → {os.path.realpath(self.directory)}',
            'Archives:',
        ]
        for architecture, archive in reversed(sorted(self.archives.items())):
            lines.append(f'{architecture} → {archive}')
        return os.linesep.join(lines)
