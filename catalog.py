import io
import os
import tarfile

import package

CATALOG = '.files'
FILES = 'files'
PACKAGE = 'desc'


class Catalog:
    def __init__(self, subsystem):
        self.subsystem = subsystem
        self.path = os.path.join(self.subsystem.path,
                                 f'{self.subsystem.name}{CATALOG}')
        self.load()

    def load(self):
        binary = self.subsystem.architecture.repository.get_file(self.path)
        f = io.BytesIO(binary)
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
