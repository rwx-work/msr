import os

import architecture
import arguments


class Repository:
    def __init__(self, location):
        self.location = location
        self.architectures = [architecture.Architecture(self, a)
                              for a in arguments.architectures]

    def __iter__(self):
        return self.architectures.__iter__()

    def __str__(self):
        lines = [
            f'     Location: {self.location}',
            f'Architectures: {[architecture.name for architecture in self]}',
        ]
        return os.linesep.join(lines)
