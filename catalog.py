import io
import os
import tarfile

import package

FILES = 'files'
PACKAGE = 'desc'


class Catalog:
    def __init__(self, binary):
        self.binary = binary
        self.load()

    def load(self):
        f = io.BytesIO(self.binary)
        archive = tarfile.open(fileobj=f)
        m = {}
        packages = {}
        for member in archive.getmembers():
            directory, *file = member.name.split(os.sep)
            if file:
                d = m[directory]
                d[file[0]] = archive.extractfile(member).read()
                if len(d) == 2:
                    p = package.Package(d[PACKAGE], d[FILES])
                    packages[p.name] = p
            else:
                m[directory] = {}
        archive.close()
        self.packages = packages
