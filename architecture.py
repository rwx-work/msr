import os

import distribution

X86 = 'x86_64'
I86 = 'i686'


class Architecture:
    def __init__(self, name, bits):
        self.name = name
        self.bits = bits
        self.distribution = distribution.Distribution(self)
        # TODO subsystems
        self.subsystems = {}

    def __str__(self):
        lines = [
            f'Name: {self.name}',
        ]
        return os.linesep.join(lines)


ARCHITECTURES = {
    X86: Architecture(X86, 64),
    I86: Architecture(I86, 32),
}
