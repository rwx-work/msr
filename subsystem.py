import os

MAIN = 'msys'

FAMILIES = [MAIN, 'clang', 'mingw', 'ucrt']


class SubSystem:
    def __init__(self, architecture, name):
        self.architecture = architecture
        self.name = name

    def __str__(self):
        lines = [
            f'Architecture: {self.architecture.name}',
            f'        Name: {self.name}',
        ]
        return os.linesep.join(lines)
