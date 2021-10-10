import os

import arguments
import distribution
import subsystem

MAIN = 'x86_64'

ARCHITECTURES = {
    MAIN:   (64, [subsystem.MAIN, 'clang64', 'mingw64', 'ucrt64']),
    'i686': (32, [subsystem.MAIN, 'clang32', 'mingw32']),
}


class Architecture:
    def __init__(self, repository, name):
        self.repository = repository
        self.name = name
        self.bits, subsystems = ARCHITECTURES[self.name]
        self.distribution = distribution.Distribution(self)
        self.subsystems = {s: subsystem.SubSystem(self, s)
                           for s in [f if f == subsystem.MAIN
                                     else f'{f}{self.bits}'
                                     for f in arguments.subsystems]
                           if s in subsystems}

    def __str__(self):
        lines = [
            f'Name: {self.name}',
            f'Bits: {self.bits}',
        ]
        return os.linesep.join(lines)
