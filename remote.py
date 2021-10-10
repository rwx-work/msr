import os
import requests

import arguments
import hypertext
import repository

MAIN = 'https://repo.msys2.org'


class Remote(repository.Repository):
    def __init__(self):
        super().__init__(arguments.remote)

    def get_file(self, path):
        return requests.get(os.path.join(self.location, path)).content

    def get_files(self, path):
        return hypertext.HyperText(os.path.join(self.location, path)).links

    def __str__(self):
        lines = [
            super().__str__(),
        ]
        return os.linesep.join(lines)
