import os
import shutil

import arguments
import file
import local
import remote


class Synchronization:
    def __init__(self):
        self.remote = remote.Remote()
        self.repository = local.Local()
        self.temporary = self.repository.get_temporary()
        self.threads = arguments.threads

    def run(self):
        for architecture in self.remote:
            for subsystem in architecture.subsystems.values():
                for _, package in sorted(subsystem.catalog.packages.items()):
                    f = file.File(
                        os.path.join(self.remote.location, subsystem.path),
                        package.name,
                        package.csize,
                        os.path.join(self.repository.location, subsystem.path),
                        package.sha256sum,
                    )
                    print()
                    print(f)
        tmp = os.path.join(self.repository.location,
                           self.repository.get_temporary())
        os.makedirs(tmp)
        # clean temporary directory
        shutil.rmtree(tmp)

    def __str__(self):
        lines = [
            str(self.remote),
            str(),
            str(self.repository),
            str(),
            f'Temporary: {self.temporary}',
        ]
        return os.linesep.join(lines)
