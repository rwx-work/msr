import os


class File:
    def __init__(self, remote, name, size, local, hash):
        self.remote = remote
        self.name = name
        self.size = size
        self.local = local
        self.hash = hash

    def __str__(self):
        lines = [
            f'Remote: {self.remote}',
            f'  Name: {self.name}',
            f'  Size: {self.size}',
            f' Local: {self.local}',
            f'  Hash: {self.hash}',
        ]
        return os.linesep.join(lines)
