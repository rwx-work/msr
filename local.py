import datetime
import os

import arguments
import repository


class Local(repository.Repository):
    def __init__(self):
        super().__init__(arguments.directory)
        self.temporary = arguments.temporary

    def get_file(self, path):
        with open(os.path.join(self.location, path), 'br') as f:
            return f.read()

    def get_files(self, path):
        *_, files = next(os.walk(os.path.join(self.location, path)))
        return files

    def get_temporary(self):
        return os.path.join(self.temporary,
                            datetime.datetime.now()
                            .strftime('%Y%m%d%H%M%S'))

    def __str__(self):
        lines = [
            super().__str__(),
            f'Temporary: {self.temporary}',
        ]
        return os.linesep.join(lines)
