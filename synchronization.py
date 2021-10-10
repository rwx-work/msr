import os
import shutil

import arguments
import msys
import remote
import repository


class Synchronization:
    def __init__(self, args):
        self.remote = remote.Remote(args)
        self.repository = repository.Repository(args)
        self.temporary = self.repository.get_temporary()
        self.threads = args[arguments.THREADS]

    def run(self):
        for architecture in self.remote.architectures:
            for subsystem in msys.get_subsystems(architecture,
                                                 self.remote.subsystems):
                catalog = self.remote.catalogs[architecture][subsystem]
                for _, package in sorted(catalog.packages.items()):
                    print()
                    print(package)
        tmp = os.path.join(self.repository.directory,
                           self.repository.get_temporary())
        os.makedirs(tmp)
        # clean temporary directory
        shutil.rmtree(tmp)

    def __str__(self):
        lines = [
            str(self.remote), str(),
            str(self.repository), str(),
            f'Temporary: {self.temporary}',
        ]
        return os.linesep.join(lines)
