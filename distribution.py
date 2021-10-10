import os

ARCHIVE = '.tar.xz'
DISTRIBUTION = 'distrib'


class Distribution:
    def __init__(self, architecture):
        self.architecture = architecture
        self.path = os.sep.join([DISTRIBUTION, self.architecture.name])
        self.load()

    def load(self):
        files = self.architecture.repository.get_files(self.path)
        self.archives = [f for f in files if f.endswith(ARCHIVE)]
        self.archive = self.archives[-1]

    def __str__(self):
        lines = [
            f'Architecture: {self.architecture.name}',
            f'        Path: {self.path}',
        ]
        return os.linesep.join(lines)
