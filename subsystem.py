import os

CRT = 'mingw'
MAIN = 'msys'

FAMILIES = [MAIN, 'clang', 'mingw', 'ucrt']


class SubSystem:
    def __init__(self, architecture, name):
        self.architecture = architecture
        self.name = name
        # path
        list = []
        if self.name != MAIN:
            list.append(CRT)
        list.append(self.name)
        if self.name == MAIN:
            list.append(self.architecture.name)
        self.path = os.sep.join(list)

    def __str__(self):
        lines = [
            f'Architecture: {self.architecture.name}',
            f'        Name: {self.name}',
            f'        Path: {self.path}',
        ]
        return os.linesep.join(lines)
