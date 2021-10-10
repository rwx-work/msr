import os


class Repository:
    def __init__(self, location):
        self.location = location

    def __str__(self):
        lines = [
            f'Location: {self.location}',
        ]
        return os.linesep.join(lines)
