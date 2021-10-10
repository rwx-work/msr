import os

import msys

KEY = '%'
SEPARATOR = f'{os.linesep}{os.linesep}'


class Package:
    def __init__(self, package, files):
        for binary in [package, files]:
            text = binary.decode(msys.CHARSET).strip()
            for item in text.split(SEPARATOR):
                line, *lines = item.split(os.linesep)
                key = line.split(KEY)[1].lower()
                if len(lines) == 1:
                    value = lines[0]
                else:
                    value = lines
                setattr(self, key, value)

    def __str__(self):
        lines = [
            f'Name: {self.name}',
            f'Size: {self.csize}',
            f'Hash: {self.sha256sum}',
        ]
        return os.linesep.join(lines)
