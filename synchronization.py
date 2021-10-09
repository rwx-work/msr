import os

import remote
import repository


class Synchronization:
    def __init__(self, args):
        self.remote = remote.Remote(args)
        self.repository = repository.Repository(args)
        self.temporary = self.repository.get_temporary()

    def __str__(self):
        lines = [
            str(self.remote), str(),
            str(self.repository), str(),
            f'Temporary: {self.temporary}',
        ]
        return os.linesep.join(lines)
