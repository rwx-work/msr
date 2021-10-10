import os
import shutil

import arguments
import file
import local
import msys
import remote


class Synchronization:
    def __init__(self, args):
        self.remote = remote.Remote(args)
        self.repository = local.Local(args)
        self.temporary = self.repository.get_temporary()
        self.threads = args[arguments.THREADS]

    def run(self):
        for architecture in self.remote.architectures:
            for subsystem in msys.get_subsystems(architecture,
                                                 self.remote.subsystems):
                catalog = self.remote.catalogs[architecture][subsystem]
                path = msys.get_subsystem(architecture, subsystem)
                for _, package in sorted(catalog.packages.items()):
                    f = file.File(
                        os.path.join(self.remote.location, path),
                        package.name,
                        package.csize,
                        os.path.join(self.repository.location, path),
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
            str(self.remote), str(),
            str(self.repository), str(),
            f'Temporary: {self.temporary}',
        ]
        return os.linesep.join(lines)
