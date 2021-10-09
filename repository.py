import arguments
import datetime
import os

import remote


class Repository:
    def __init__(self, args):
        self.directory = args[arguments.DIRECTORY]
        self.temporary = args[arguments.TEMPORARY]
        self.tmp = os.path.join(self.temporary,
                                datetime.datetime.now()
                                .strftime('%Y%m%d%H%M%S'))
        self.load()

    def load(self):
        distribution = os.path.join(
            self.directory, remote.DISTRIBUTION)
        d = {}
        _, architectures, _ = next(os.walk(distribution))
        for architecture in [a for a in architectures
                             if a in remote.ARCHITECTURES]:
            directory = os.path.join(distribution, architecture)
            _, _, files = next(os.walk(directory))
            archives = sorted([file for file in files
                        if file.endswith(remote.ARCHIVE)])
            archive = archives[-1]
            d[architecture] = archive
        self.archives = d

    def __str__(self):
        lines = [
            f'Directory: {self.directory}',
            f'         → {os.path.realpath(self.directory)}',
            f'Archives:',
        ]
        for architecture, archive in reversed(sorted(self.archives.items())):
            lines.append(f'{architecture} → {archive}')
        lines.append(f'Temporary: {self.tmp}')
        return os.linesep.join(lines)
