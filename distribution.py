import os

DISTRIBUTION = 'distrib'


class Distribution:
    def __init__(self, architecture):
        self.architecture = architecture
        self.path = os.sep.join([DISTRIBUTION, self.architecture.name])

    def __str__(self):
        lines = [
            f'Architecture: {self.architecture.name}',
            f'        Path: {self.path}',
        ]
        return os.linesep.join(lines)
