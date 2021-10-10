import os


class Distribution:
    def __init__(self, architecture):
        self.architecture = architecture

    def __str__(self):
        lines = [
            f'Architecture: {self.architecture.name}',
        ]
        return os.linesep.join(lines)
