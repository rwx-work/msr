import os

import distribution


class Architecture:
    def __init__(self, name):
        self.name = name
        self.distribution = distribution.Distribution(self)
        # TODO subsystems
        self.subsystems = {}

    def __str__(self):
        lines = [
            f'Name: {self.name}',
        ]
        return os.linesep.join(lines)

X86 = Architecture('x86_64')
I86 = Architecture('i686')
