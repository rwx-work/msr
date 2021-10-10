import os

import distribution
import subsystem

X86 = 'x86_64'
I86 = 'i686'


class Architecture:
    def __init__(self, name, bits, subsystems):
        self.name = name
        self.bits = bits
        self.distribution = distribution.Distribution(self)
        self.subsystems = {s: subsystem.SubSystem(self, s) for s in subsystems}

    def __str__(self):
        lines = [
            f'Name: {self.name}',
        ]
        return os.linesep.join(lines)


x86 = Architecture(X86, 64, [subsystem.MAIN,
                             'clang64', 'mingw64', 'ucrt64'])
i86 = Architecture(I86, 32, [subsystem.MAIN,
                             'clang32', 'mingw32'])

ARCHITECTURES = {
    X86: x86,
    I86: i86,
}
