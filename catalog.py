import io
import tarfile

import package


class Catalog:
    def __init__(self, binary):
        self.binary = binary
        self.load()

    def load(self):
        f = io.BytesIO(self.binary)
        archive = tarfile.open(fileobj=f)
        for member in archive.getmembers():
            print(member)
        archive.close()
