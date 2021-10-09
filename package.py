import os

CHARSET = 'u8'
KEY = '%'
SEPARATOR = f'{os.linesep}{os.linesep}'


class Package:
    def __init__(self, package, files):
        p = package.decode(CHARSET).strip()
        f = files.decode(CHARSET).strip()
        text = f'{p}{SEPARATOR}{f}'
        for item in text.split(SEPARATOR):
            line, *lines = item.split(os.linesep)
            key = line.split(KEY)[1].lower()
            if len(lines) == 1:
                value = lines[0]
            else:
                value = lines
            setattr(self, key, value)
            print()
            print(key)
            print(value)
