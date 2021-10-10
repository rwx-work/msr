import os

import architecture
import arguments


class Repository:
    def __init__(self, location):
        self.location = location
        self.architectures = [architecture.Architecture(self, a)
                              for a in arguments.architectures]

    def __str__(self):
        lines = [
            f'     Location: {self.location}',
            f'Architectures: {[a.name for a in self.architectures]}',
        ]
        return os.linesep.join(lines)
